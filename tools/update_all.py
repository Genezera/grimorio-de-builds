# -*- coding: utf-8 -*-
"""Ciclo de atualização automática: coleta → classificação → descoberta → reconstrução → auditoria → testes → relatório.

Cada etapa é independente e o ciclo continua mesmo se uma falhar (o relatório diz qual). Sai com código 1 se a AUDITORIA ou os TESTES reprovarem; nesse caso nada deve ser publicado
(o workflow .github/workflows/update.yml só faz commit quando o ciclo passa).
Uso: python update_all.py [--no-fetch] [--no-build]     (--no-fetch: usa o snapshot já salvo; --no-build: só dados e auditoria)"""
import json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "..")
PY = [sys.executable, "-X", "utf8"]
ENV = {**os.environ, "PYTHONUTF8": "1"}


def run(name, args, cwd=HERE, must=False, timeout=1800):
    t0 = time.time()
    try:
        r = subprocess.run(PY + args, cwd=cwd, env=ENV, capture_output=True, text=True, timeout=timeout)
        ok, tail = r.returncode == 0, (r.stdout + r.stderr).strip().splitlines()[-6:]
    except subprocess.TimeoutExpired:
        ok, tail = False, ["timeout"]
    print(f"{'OK ' if ok else 'FALHOU'} {name} ({time.time() - t0:.0f}s)", flush=True)
    if not ok:
        print("   " + "\n   ".join(tail), flush=True)
    return dict(step=name, ok=ok, must=must, tail=tail)


def main():
    fetch, build = "--no-fetch" not in sys.argv, "--no-build" not in sys.argv
    steps = []
    if fetch:
        steps.append(run("coleta poe.ninja (ninja_meta)", ["ninja_meta.py"], timeout=2400))
    steps.append(run("registro e rankings (registry)", ["registry.py"]))
    steps.append(run("candidatas a novas builds (discover)", ["discover.py", "--top", "25"]))
    if build:
        steps.append(run("reconstrução de todas as páginas (build_all)", ["build_all.py"], timeout=1800))
    steps.append(run("auditoria de coerência (audit)", ["audit.py"], must=True))
    steps.append(run("testes unitários", ["-m", "unittest", "discover", "-s", "tests"], must=True))
    bad = [s for s in steps if not s["ok"] and s["must"]]
    audit = json.load(open(os.path.join(HERE, "dl", "audit.json"), encoding="utf-8")) if os.path.exists(os.path.join(HERE, "dl", "audit.json")) else {}
    out = dict(date=time.strftime("%Y-%m-%d %H:%M"), passed=not bad, steps=[{k: v for k, v in s.items() if k != "tail"} for s in steps], audit={k: audit.get(k) for k in ("errors", "warnings", "info")})
    json.dump(out, open(os.path.join(HERE, "dl", "last_update.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("resultado:", "APROVADO" if not bad else "REPROVADO: " + ", ".join(s["step"] for s in bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
