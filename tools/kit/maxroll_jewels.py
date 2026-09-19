# -*- coding: utf-8 -*-
"""Joias dos planners do Maxroll: lê dl/<fonte>.json (perfis → tree.jewels {nó: id do item}) e grava a lista normalizada (kit/jewels.py) em todas as variantes de dl/<bid>_variants.json.
Usa o perfil com mais joias (o do endgame). Uso: python maxroll_jewels.py <bid> <fonte>"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
import maxroll as M  # noqa: E402

CAMEL = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")


def main(bid, src):
    R = json.load(open(os.path.join(ROOT, "dl", f"{src}.json"), encoding="utf-8"))
    d = json.loads(R["data"]) if isinstance(R["data"], str) else R["data"]
    items = d["items"]; best = {}
    for p in d["profiles"]:
        for pv in (p.get("passives") or {}).get("variants") or []:
            j = pv.get("jewels") or {}
            if len(j) > len(best): best = j
    out = []
    for node, iid in best.items():
        it = items.get(str(iid))
        if not it: continue
        k = M.item(it)
        rare = it["rarity"] != "unique"
        base_name = k["n"]
        radius = "radius" in it["base"].lower() or (it.get("stats", {}).get("implicit") or {}).get("local_jewel_effect_base_radius")
        mods = list(k["mods"])
        if not mods:                                                                   # rare: nomes legíveis dos mods explícitos
            mods = [CAMEL.sub(" ", re.sub(r"^(Jewel|Crafted)+", "", mid)).strip() for mid in (it.get("mods", {}).get("explicit") or {})]
        out.append({"node": int(node), "n": (base_name if base_name.startswith("Time-Lost") else f"Rare {base_name}") if rare else base_name, "u": not rare, "base": base_name, "mods": mods[:6],
                    "radius": "variável" if radius else None, "corrupted": bool(it.get("corrupted")), "note": ""})
    p = os.path.join(ROOT, "dl", f"{bid}_variants.json")
    V = json.load(open(p, encoding="utf-8"))
    for v in V["variants"]:
        v["tree"]["jewels"] = out
    json.dump(V, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(bid, "joias:", [(j["node"], j["n"]) for j in out])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
