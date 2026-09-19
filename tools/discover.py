# -*- coding: utf-8 -*-
"""Descobre candidatas a novas builds: combinações ascendência + skill FORA do meta, fortes e ainda sem guia neste site.

Fonte: tools/dl/meta_snapshot.json (poe.ninja, ninja_meta.py). Critérios (todos números, nada de opinião):
  · amostra: pelo menos 300 personagens usam a skill na ascendência e há DPS/EHP dos personagens do topo;
  · fora do meta: a skill é usada por menos de 25% da ascendência (e a ascendência tem menos de 15% de todos os personagens, ou a skill menos de 10%);
  · força: percentil de DPS e de EHP entre todas as combinações;
  · não coberta: nenhuma build do registro usa essa ascendência + skill.
Saída: docs/candidates.md e tools/dl/candidates.json. A escrita do guia (fases, itens, árvore, teste) continua sendo um passo com revisão: veja docs/AUTOMACAO.md.
Uso: python discover.py [--top 20]"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
import registry  # noqa: E402

SNAP = os.path.join(HERE, "dl", "meta_snapshot.json")
BLOCK = {"Herald of Ice", "Herald of Thunder", "Herald of Blood", "Herald of Ash", "Elemental Weakness", "Frost Bomb", "Temporal Chains", "Enfeeble", "Vulnerability", "Freezing Mark", "Sigil of Power", "Cast on Dodge",
         "Wind Dancer", "Charge Regulation", "Mana Remnants", "Arctic Armour", "Virtuous Barrier", "Wild Protector", "Archon of Chayula", "Grim Pillars", "Entangle"}    # buffs/curses/utilidades: não são "a build"


def main():
    top_n = int(next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--top"), 20))
    snap = json.load(open(SNAP, encoding="utf-8"))
    combos = []
    for a, d in snap["ascendancies"].items():
        for s in d["skills"]:
            if s["n"] >= 300 and s.get("dps") and s.get("ehp") and s["skill"] not in BLOCK:
                combos.append(dict(asc=a, skill=s["skill"], n=s["n"], share=s["share"], ascShare=d["share"], dps=s["dps"], ehp=s["ehp"], lv=s.get("lv")))
    dps = [c["dps"] for c in combos]; ehp = [c["ehp"] for c in combos]
    covered = {(b["asc"], n) for b in registry.IDENT for n in b["ninja"]}
    out = []
    for c in combos:
        c["dpsPct"] = round(registry.percentile(c["dps"], dps), 2); c["ehpPct"] = round(registry.percentile(c["ehp"], ehp), 2)
        c["offmeta"] = c["share"] < 25 and (c["ascShare"] < 15 or c["share"] < 10)
        c["covered"] = (c["asc"], c["skill"]) in covered
        c["score"] = round(.5 * c["dpsPct"] + .3 * c["ehpPct"] + .2 * (1 - min(1, c["share"] / 50)), 3)
        if c["offmeta"] and not c["covered"] and (c.get("lv") or 0) >= 90: out.append(c)
    out.sort(key=lambda c: -c["score"])
    json.dump(dict(snapshot=snap["snapshot"], fetched=snap["fetched"], candidates=out[:100]), open(os.path.join(HERE, "dl", "candidates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    L = [f"# Candidatas a novas builds — {snap['league']} ({snap['fetched']})", "",
         "Combinações ascendência + skill **fora do meta**, com DPS e EHP altos entre os personagens do topo e **sem guia neste site**. Números do poe.ninja; a decisão de escrever o guia (e o teste de "
         "\"dá para seguir\") é o passo seguinte.", "", "| # | Ascendência | Skill | Uso na asc. | DPS mediano (top) | EHP mediano (top) | Pct DPS | Pct EHP | Nota |", "|---|---|---|---|---|---|---|---|---|"]
    fmt = lambda v: f"{v / 1e6:.1f}M" if v >= 1e6 else f"{v / 1e3:.0f}k"
    for k, c in enumerate(out[:top_n], 1):
        L.append(f"| {k} | {c['asc']} | {c['skill']} | {c['share']}% ({c['n']}) | {fmt(c['dps'])} | {fmt(c['ehp'])} | {int(c['dpsPct'] * 100)} | {int(c['ehpPct'] * 100)} | {c['score']} |")
    open(os.path.join(REPO, "docs", "candidates.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("\n".join(L[6:6 + top_n]))


if __name__ == "__main__":
    main()
