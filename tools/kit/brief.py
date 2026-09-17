# -*- coding: utf-8 -*-
"""Resumo de estudo de uma build: notas do guia, gems com descrição do jogo, ascendência e itens por variante."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pob
ROOT = os.path.join(HERE, "..")
bid = sys.argv[1]
V = json.load(open(os.path.join(ROOT, "dl", f"{bid}_variants.json"), encoding="utf-8"))
T = json.load(open(os.path.join(ROOT, "tree.json"), encoding="utf-8"))["nodes"]
seen = set()
for g in V["guides"]:
    print("=== GUIDE", g["title"], g["author"], g["updatedAt"], g["url"])
    for w in g["widgets"]:
        k = w[:200]
        if k in seen: continue
        seen.add(k); print("\n---\n" + w[:4000])
print("\n\n=== VARIANTS")
names = set()
for v in V["variants"]:
    print(f"\n## {v['name']}  (tree {len(v['tree']['m'])})")
    print("  asc:", [T[str(a)]["name"] for a in v["tree"]["a"] if str(a) in T and T[str(a)].get("isNotable")])
    for g in v["gems"]:
        print(f"  - {g['skill']} [{g.get('weaponSet')}] <- {', '.join(g['sup'])}")
        names.add(g["skill"]); names.update(g["sup"])
    print("  items:", {k: (x.get("n") or x.get("skill")) + ("*" if x.get("u") else "") for k, x in v["items"].items() if x})
print("\n\n=== GEMS")
for n in sorted(names):
    gm = pob.gem(n) or {}
    print(f"* {n} | tier {gm.get('tier')} | {gm.get('type')} | {gm.get('tags')} | {pob.desc(n)}")
print("\n=== ASC NOTABLES")
asc = {a for v in V["variants"] for a in v["tree"]["a"]}
for a in sorted(asc):
    n = T.get(str(a))
    if n and n.get("isNotable"): print(f"* {n['name']}: {' / '.join(n.get('stats', []))}")
