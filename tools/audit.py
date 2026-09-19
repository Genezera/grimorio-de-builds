# -*- coding: utf-8 -*-
"""Auditoria de coerência de todas as builds: acha o que ficou perdido, quebrado, incoerente ou impossível de seguir.

Erros (E) reprovam a execução; avisos (W) entram no relatório; informações (I) mostram o estado. Cada verificação é uma função pequena em CHECKS.
Saída: docs/audit.md e tools/dl/audit.json. Uso: python audit.py [--strict]   (--strict: avisos também reprovam)"""
import json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "..")
sys.path.insert(0, os.path.join(HERE, "kit"))
import common, ninja  # noqa: E402

REG = os.path.join(HERE, "dl", "registry.json")
issues = []


def add(lvl, bid, code, msg):
    issues.append(dict(level=lvl, build=bid, code=code, msg=msg))


def load(bid):
    try:
        return common.load_build(bid)
    except Exception as e:                                                        # noqa: BLE001
        add("E", bid, "load", f"bdata não carrega: {e}")
        return None


SPIRIT_QUESTS = [(62, 100), (38, 60), (10, 30), (1, 0)]        # (nível, Spirit de quest acumulado): King in the Mists, Ignagduk, Lythara


def spirit_budget(lv):
    return next(v for l, v in SPIRIT_QUESTS if lv >= l)


def check_phases(bid, B):
    ph = B.PHASES
    prev_end = 0
    for p in ph:
        a, b = p["lv"]
        if a > b: add("E", bid, "phase-range", f"{p['id']}: faixa {a}–{b} invertida")
        if a != prev_end + 1 and prev_end and a <= prev_end: add("E", bid, "phase-overlap", f"{p['id']}: começa em {a} mas a anterior termina em {prev_end}")
        if prev_end and a > prev_end + 1: add("W", bid, "phase-gap", f"{p['id']}: lacuna de níveis {prev_end + 1}–{a - 1} sem fase")
        prev_end = max(prev_end, b)
        if not p.get("gems"): add("E", bid, "phase-empty", f"{p['id']}: sem gems")
        if not p.get("rotation"): add("W", bid, "phase-rotation", f"{p['id']}: sem rotação")
        for g in p["gems"]:
            if g.get("since") and g["since"] > b: add("W", bid, "gem-since", f"{p['id']}: {g['skill']} só entra no nível {g['since']}, depois do fim da fase ({b}): não aparece nela")
            if g.get("until") and g["until"] < a: add("W", bid, "gem-until", f"{p['id']}: {g['skill']} já saiu no nível {g['until']} (antes da fase)")
    if ph and ph[0]["lv"][0] != 1: add("E", bid, "phase-start", f"a primeira fase começa no nível {ph[0]['lv'][0]}, não no 1")
    if ph and ph[-1]["lv"][1] < 100: add("W", bid, "phase-end", f"a última fase termina no nível {ph[-1]['lv'][1]}")
    for lv in getattr(B, "MILESTONES", {}):
        if not 1 <= lv <= 100: add("E", bid, "milestone", f"marco no nível {lv}")


def check_spirit(bid, B):
    for p in B.PHASES:
        cost = 0
        for g in p["gems"]:
            if g.get("sp") == "core":
                m = re.search(r"\d+", str(g.get("cost", "")))
                if m and not (g.get("until") and g["until"] < p["lv"][0]) and not (g.get("since") and g["since"] > p["lv"][1]): cost += int(m.group())
        lv = p["lv"][1] if p["lv"][1] <= 100 else 100
        if cost > spirit_budget(lv) + 200: add("W", bid, "spirit", f"{p['id']}: {cost} de Spirit em reservas no nível {lv}, com {spirit_budget(lv)} de quests (+ 200 de itens, ascendência e atlas é o teto plausível)")


def check_uniques(bid, B):
    uniq = {u["n"] for u in getattr(B, "UNIQUES", [])}
    used = set()
    for p in B.PHASES:
        for k in ("cheap", "full"):
            used.update(x for x in p.get(k, []) if isinstance(x, str))
    for g in getattr(B, "GEAR", []):
        for k in ("cheap", "value", "full", "slot"):
            v = g.get(k)
            if isinstance(v, str): used.add(v)
        for o in g.get("opts") or []: used.add(o["n"])
    for b in getattr(B, "BUY_ORDER", []): used.add(b["item"])
    blob = " ".join(used)
    for n in sorted(uniq):
        if n not in blob: add("W", bid, "unique-orphan", f"{n}: está em UNIQUES mas nenhuma fase, slot ou compra usa")
    for p in B.PHASES:
        for k in ("cheap", "full"):
            for x in p.get(k, []):
                if isinstance(x, str) and re.match(r"^[A-Z][A-Za-z']*(?: (?:of|the|and)| [A-Z][A-Za-z']*)*$", x) and x not in uniq and len(x) < 30 and not any(x in str(g.get("slot", "")) for g in getattr(B, "GEAR", [])):
                    add("W", bid, "unique-missing", f"{p['id']}.{k}: '{x}' não tem entrada em UNIQUES")
    for u in getattr(B, "UNIQUES", []):
        if u.get("p") not in {p["id"] for p in B.PHASES}: add("E", bid, "unique-phase", f"{u['n']}: fase '{u.get('p')}' não existe")
    for g in getattr(B, "GEAR", []):
        for o in g.get("opts") or []:
            if o["lv"] < 1 or o["lv"] > 100: add("E", bid, "opt-level", f"{g['slot']}: {o['n']} com nível {o['lv']}")
        if g.get("opts"):
            for lv in (1, 10, 25, 40, 60, 80, 95):
                if not [o for o in g["opts"] if o["lv"] <= lv and o["c"] in ("free", "cheap")]: add("W", bid, "opt-empty", f"{g['slot']}: nenhuma opção barata no nível {lv}")


def check_supports(bid, B):
    why = getattr(B, "SUPWHY", {})
    used = {s for p in B.PHASES for g in p["gems"] for s in g["sup"]}
    for s in sorted(used - set(why)): add("E", bid, "support-why", f"{s}: support usado sem explicação (SUPWHY)")
    for s in sorted(set(why) - used): add("I", bid, "support-orphan", f"{s}: explicado em SUPWHY mas nunca usado")


def check_tree(bid, B):
    p = os.path.join(HERE, "dl", f"{bid}_variants.json")
    if not os.path.exists(p):
        add("W", bid, "tree-missing", "sem variantes de árvore"); return
    V = {v["name"]: v for v in json.load(open(p, encoding="utf-8"))["variants"]}
    start = getattr(B, "START", None) or ninja.CLASS_START.get(getattr(B, "CLASS", ""))
    prev, prev_id = None, None
    for pid in getattr(B, "ORDER", [p_["id"] for p_ in B.PHASES]):
        v = V.get(getattr(B, "VMAP", {}).get(pid))
        if not v: add("W", bid, "tree-phase", f"{pid}: sem variante de árvore"); continue
        m = set(v["tree"]["m"])
        if start and m:                                                            # conectado a partir do início da classe (ou de uma joia que o guia usa)
            seen, stack = {start}, [start]
            while stack:
                u = stack.pop()
                for w in ninja.ADJ.get(u, ()):
                    if w in m and w not in seen: seen.add(w); stack.append(w)
            lost = m - seen
            if lost and len(lost) > .8 * len(m): add("I", bid, "tree-start", f"{pid}: a árvore não parte do início conhecido da classe (a build usa outro ponto de partida, como uma joia): conexão não verificada")
            elif lost and len(lost) > 3: add("W", bid, "tree-connect", f"{pid}: {len(lost)} nós da árvore principal não ligam ao início da classe")
        if prev is not None and pid != "max" and prev_id != "endgame":
            drop = prev - m
            if drop: add("I", bid, "tree-respec", f"{prev_id}→{pid}: {len(drop)} nós saem da árvore (respec)")
        prev, prev_id = m, pid


def check_sources(bid, B):
    if not getattr(B, "SOURCES", None): add("E", bid, "sources", "sem fontes")
    for s in getattr(B, "SOURCES", []):
        if not str(s.get("url", "")).startswith("http"): add("E", bid, "source-url", f"fonte sem URL: {s.get('name')}")
    if not getattr(B, "GUIDE_URL", ""): add("W", bid, "guide-url", "sem GUIDE_URL do guia de referência")


def check_pages(entry):
    folder, bid = entry["folder"], entry["key"]
    for f in ("index.html", "en.html"):
        p = os.path.join(REPO, folder, f)
        if not os.path.exists(p): add("E", bid, "page-missing", f"{folder}/{f} não existe"); continue
        t = open(p, encoding="utf-8").read()
        for bad in ("undefined", "NaN", "[object Object]", "None</"):
            n = len(re.findall(r"(?<![A-Za-z\"'_.])" + re.escape(bad) + r"(?![A-Za-z\"'_:])", re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)))
            if n: add("W", bid, "page-text", f"{folder}/{f}: '{bad}' aparece {n}x no texto visível")
        for m in set(re.findall(r'(?:src|href)="((?:\.\./)?(?:shared|assets)/[^"?#]+)', t)):
            if not os.path.exists(os.path.normpath(os.path.join(REPO, folder, m))): add("E", bid, "asset-missing", f"{folder}/{f}: {m} não existe")


def check_registry(reg):
    snap = reg.get("snapshot")
    if not snap: add("W", "-", "snapshot", "sem snapshot do poe.ninja (rode ninja_meta.py)")
    else:
        age = (time.time() - time.mktime(time.strptime(snap["fetched"], "%Y-%m-%d"))) / 86400
        if age > 14: add("W", "-", "snapshot-old", f"snapshot do poe.ninja tem {int(age)} dias")
    for e in reg["builds"]:
        if e["status"] != "ativa": add("W", e["key"], "status", f"status '{e['status']}': ninguém usa mais {e['ninja']['skill'] or e['ninja']['ascN']}? revisar ou aposentar")
        if e["meta"] == "sem dados": add("I", e["key"], "meta", "sem dados do poe.ninja para a skill principal")
    folders = {e["folder"] for e in reg["builds"]}
    for d in sorted(os.listdir(REPO)):
        if os.path.exists(os.path.join(REPO, d, "index.html")) and d not in folders and d not in ("rites", "docs", "planilha", "shared", "tools"):
            add("W", d, "orphan-folder", f"pasta '{d}' tem index.html mas não está no registro")


def main():
    reg = json.load(open(REG, encoding="utf-8"))
    check_registry(reg)
    for e in reg["builds"]:
        bid = e["folder"]
        if e.get("kit"):
            B = load(bid)
            if B:
                for fn in (check_phases, check_spirit, check_uniques, check_supports, check_tree, check_sources): fn(bid, B)
        check_pages(dict(e, key=e["key"]))
    E = [i for i in issues if i["level"] == "E"]; W = [i for i in issues if i["level"] == "W"]; I = [i for i in issues if i["level"] == "I"]
    json.dump(dict(date=time.strftime("%Y-%m-%d"), errors=len(E), warnings=len(W), info=len(I), issues=issues), open(os.path.join(HERE, "dl", "audit.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    lines = [f"# Auditoria das builds — {time.strftime('%Y-%m-%d')}", "", f"**{len(E)} erros · {len(W)} avisos · {len(I)} informações**", ""]
    for title, arr in (("Erros", E), ("Avisos", W), ("Informações", I)):
        if arr:
            lines += [f"## {title}", ""] + [f"- `{i['build']}` **{i['code']}** — {i['msg']}" for i in arr] + [""]
    open(os.path.join(REPO, "docs", "audit.md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"{len(E)} erros · {len(W)} avisos · {len(I)} informações  →  docs/audit.md")
    for i in E + W[:25]: print(f"  {i['level']} {i['build']:12} {i['code']:14} {i['msg']}")
    sys.exit(1 if E or (W and "--strict" in sys.argv) else 0)


if __name__ == "__main__":
    main()
