# -*- coding: utf-8 -*-
"""Auditoria de conexão entre as abas de cada build do kit.

A regra é simples: nada pode ser citado em um canto e esquecido no resto. Para cada build:

  1. toda unique da aba Uniques precisa aparecer no plano — em alguma fase (barato/completo),
     na progressão por nível de um slot, nos tiers do slot ou na ordem de compra;
  2. toda unique usada no plano precisa ser marcável em "Meu personagem" (senão o usuário não
     consegue dizer que já tem e a adaptação nunca liga);
  3. todo nome citado na progressão por nível precisa ter ícone (unique, gem ou base) ou ser frase;
  4. todo support usado nas fases precisa ter explicação em supWhy;
  5. chaves de regras/trocas/timing existem; fases citadas existem; marcos caem dentro de fases;
  6. ascendência por fase existe na árvore e cabe nos Trials liberados até o nível da fase.
"""
import json
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, os.path.join(ROOT, "kit"))
sys.path.insert(0, ROOT)
import common  # noqa: E402

BUILDS = ["tactician", "infernalist", "acolyte", "pathfinder", "smith", "martial"]
TREE = json.load(open(os.path.join(ROOT, "tree.json"), encoding="utf-8"))["nodes"]
PHRASE = re.compile(r"\b(rare|rares|magic|com|de|do|da|até|sem|mãos|qualquer|any|with|and|or|the)\b", re.I)


def assets(bid):
    with open(os.path.join(ROOT, "builds", bid, "assets.json"), encoding="utf-8") as f:
        return json.load(f)


def audit(bid):
    D = common.load_build(bid)
    A = assets(bid)
    DATA = D.build([])                     # dados finais da página
    common.ensure_own(DATA)
    out = []
    phases = {p["id"] for p in D.PHASES}
    uniq = {u["n"] for u in D.UNIQUES}
    gems = {g["skill"] for p in D.PHASES for g in p["gems"]}
    sups = {s for p in D.PHASES for g in p["gems"] for s in g["sup"]}
    icons = set(A["uniqIcon"]) | set(A["gemIcon"]) | set(A["supIcon"]) | set(A.get("baseIcon", {}))
    own_keys = {k for _, k, _ in DATA["char"]["own"]}
    own_labels = " ; ".join(lbl for _, _, lbl in DATA["char"]["own"])

    # texto onde uma unique pode ser citada no plano
    plano = []
    for p in D.PHASES:
        plano += list(p["cheap"]) + list(p["full"]) + [p["goal"], p["tag"]]
    for g in D.GEAR:
        plano += [g["cheap"], g["value"], g["full"], g.get("note", "")]
        plano += [x["n"] for x in g.get("lvls", [])]
    plano += [b["item"] for b in D.BUY_ORDER]
    plano += [t["n"] for t in D.timing_rows] if hasattr(D, "timing_rows") else []
    plano_txt = " ;; ".join(plano)

    # 1) unique citada só na aba Uniques
    for u in D.UNIQUES:
        if u["n"] not in plano_txt:
            out.append(f"{bid}: unique '{u['n']}' aparece só na aba Uniques — não está em nenhuma fase, slot ou ordem de compra")

    # 2) unique do plano sem caixinha em "Meu personagem"
    for n in sorted(uniq):
        if n in plano_txt and n not in own_keys and n not in own_labels:
            out.append(f"{bid}: unique '{n}' está no plano mas não dá para marcar em Meu personagem")

    # 3) nome sem ícone na progressão por nível
    for g in D.GEAR:
        for x in g.get("lvls", []):
            n = x["n"]
            if n in uniq or n in gems or n in sups or n in icons or PHRASE.search(n) or "(" in n or ":" in n:
                continue
            out.append(f"{bid}: '{n}' (slot {g['slot']}, nv {x['lv']}) não tem ícone nem é frase explicativa")

    # 4) support sem explicação
    for s in sorted(sups):
        if s not in D.SUPWHY:
            out.append(f"{bid}: support '{s}' é usado nas fases mas não tem explicação em supWhy")

    # 5) chaves e fases
    tabs = {t[0] for t in D.TABS}
    for r in D.CHAR["rules"]:
        for k in (r["when"].get("own") or []) + (r["when"].get("notOwn") or []) + (r["when"].get("anyOwn") or []):
            if k not in own_keys:
                out.append(f"{bid}: regra de Meu personagem usa a chave '{k}', que não existe na lista de marcar")
        if r.get("tab") and r["tab"] not in tabs:
            out.append(f"{bid}: regra aponta para a aba '{r['tab']}', que não existe")
    for s in getattr(D, "ADAPT_SWAPS", []):
        for pid in ([s["pid"]] if s.get("pid") else s.get("pids", [])):
            if pid not in phases:
                out.append(f"{bid}: troca declarada para a fase '{pid}', que não existe")
        if s.get("gemsFrom") and s["gemsFrom"] not in phases:
            out.append(f"{bid}: troca puxa gems da fase '{s['gemsFrom']}', que não existe")
        for k in (s["when"].get("own") or []) + (s["when"].get("notOwn") or []):
            if k not in own_keys:
                out.append(f"{bid}: troca usa a chave '{k}', que não existe na lista de marcar")
    for nome, k in getattr(D, "TIMING_KEY", {}).items():
        if k not in own_keys:
            out.append(f"{bid}: timing de '{nome}' aponta para a chave '{k}', que não existe na lista de marcar")
    for lv in D.MILESTONES:
        if not any(p["lv"][0] <= lv <= p["lv"][1] for p in D.PHASES):
            out.append(f"{bid}: marco do nível {lv} está fora de todas as fases")

    # 6) ascendência por fase
    names = {n.get("name") for n in TREE.values() if n.get("ascendancyName") == D.ASC}
    for pid, want in getattr(D, "ASC_PHASE", {}).items():
        if pid not in phases:
            out.append(f"{bid}: ASC_PHASE cita a fase '{pid}', que não existe")
        for nm in want:
            if nm not in names:
                out.append(f"{bid}: ASC_PHASE cita '{nm}', que não é notable de {D.ASC}")
        lv = next((p["lv"][1] for p in D.PHASES if p["id"] == pid), 0)
        trials = sum(1 for u in D.ASC_UNLOCK if u <= lv)
        if len(want) > trials:
            out.append(f"{bid}: fase '{pid}' aloca {len(want)} notables, mas só {trials} Trials liberam até o nível {lv}")
    return out


class Links(unittest.TestCase):
    def test_builds(self):
        todos = []
        for bid in BUILDS:
            todos += audit(bid)
        self.assertEqual(todos, [], "\n" + "\n".join(todos))


if __name__ == "__main__":
    alvo = sys.argv[1:] or BUILDS
    tudo = []
    for b in alvo:
        p = audit(b)
        tudo += p
        print(f"== {b}: {len(p)} desconexões")
        for x in p:
            print("   -", x)
    print("\nTOTAL:", len(tudo))
