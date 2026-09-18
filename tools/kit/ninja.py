# -*- coding: utf-8 -*-
"""Converte personagens do poe.ninja (dl/<pasta>/char_*.json) no mesmo formato de variantes do kit.

Serve para builds que não têm planner público: a árvore vem do personagem real, e os cortes por pontos
viram as fases (a ordem de alocação é calculada a partir do início da classe, igual à aba Árvore).

Uso: python ninja.py <bid> <pasta> [char_01] ["Nome|pontos" ...]
"""
import glob
import json
import os
import sys
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
import common  # noqa: E402

TREE = json.load(open(os.path.join(ROOT, "tree.json"), encoding="utf-8"))
NODES = TREE["nodes"]
BASES = json.load(open(os.path.join(ROOT, "dl", "repoe_base_items.json"), encoding="utf-8"))
UNIQ_ART = {u["name"]: (u.get("visual_identity") or {}).get("dds_file") for u in json.load(open(os.path.join(ROOT, "dl", "repoe_uniques.json"), encoding="utf-8")).values()}
ART_BY_BASE = {b.get("name"): (b.get("visual_identity") or {}).get("dds_file") for b in BASES.values() if b.get("name")}
SLOTS = {"Weapon": "mainHand_set1", "Offhand": "offHand_set1", "Weapon2": "mainHand_set2", "Offhand2": "offHand_set2", "Helm": "helmet", "BodyArmour": "body",
         "Gloves": "gloves", "Boots": "boots", "Amulet": "amulet", "Ring": "leftRing", "Ring2": "rightRing", "Belt": "belt", "Charm1": "charm1", "Charm2": "charm2",
         "Charm3": "charm3", "Flask1": "flask1", "Flask2": "flask2"}
CLASS_START = {"Monk": 44683, "Warrior": 47175, "Ranger": 50459, "Huntress": 50459, "Mercenary": 50986, "Witch": 54447, "Sorceress": 54447, "Druid": 61525}


def adj():
    g = {}
    for k, n in NODES.items():
        for c in n.get("connections", []):
            g.setdefault(int(k), set()).add(c["id"])
            g.setdefault(c["id"], set()).add(int(k))
    return g


ADJ = adj()


def grow_order(alvo, start):
    """Ordem de alocação: caminha do início da classe pelos nós escolhidos, sempre pelo vizinho já ligado."""
    want, have, out = set(alvo) - {start}, {start}, []
    while want:
        passo = [n for n in want if ADJ.get(n, set()) & have]
        if not passo:                                     # nó solto (jewel/cluster): entra no fim
            out += sorted(want)
            break
        passo.sort(key=lambda n: (not NODES.get(str(n), {}).get("isNotable"), n))
        for n in passo:
            have.add(n); want.discard(n); out.append(n)
    return out


def item(it):
    d = it["itemData"]
    uniq = d["frameTypeId"] == "Unique"
    name = d["name"] if uniq and d.get("name") else d["typeLine"]
    mods = (d.get("implicitMods") or []) + (d.get("explicitMods") or []) + (d.get("runeMods") or [])
    clean = [common.re.sub(r"\[([^|\]]*\|)?([^\]]*)\]", r"\2", m) for m in mods] if hasattr(common, "re") else mods
    return {"n": name, "u": 1 if uniq else 0, "icon": (UNIQ_ART.get(name) if uniq else None) or ART_BY_BASE.get(d["typeLine"]),
            "mods": clean[:8], "stats": [], "runes": [], "skill": None}


def gems(ch):
    out = []
    for s in ch["skills"]:
        g = [x["name"] for x in s["allGems"]]
        if not g:
            continue
        meta = [common.re.sub(r"\s+", "", g[0])] if False else None
        out.append({"skill": g[0], "slug": g[0].lower().replace(" ", ""), "icon": None, "skillIcon": None,
                    "sup": g[1:], "supIcons": {}, "weaponSet": None})
    return out


def variant(ch, nome, limite=None):
    start = CLASS_START.get(ch.get("baseClass") or ch.get("class"), 0)
    todos = [int(x) for x in ch["passiveSelection"]]
    asc = [n for n in todos if NODES.get(str(n), {}).get("ascendancyName")]
    main = [n for n in todos if not NODES.get(str(n), {}).get("ascendancyName")]
    ordem = grow_order(main, start)
    m = ordem[:limite] if limite else ordem
    s1 = [int(x) for x in (ch.get("passiveSelectionSet1") or [])]
    s2 = [int(x) for x in (ch.get("passiveSelectionSet2") or [])]
    items = {}
    for it in ch["items"] + ch.get("flasks", []):
        slot = SLOTS.get(it["itemData"]["inventoryId"])
        if slot:
            items[slot] = item(it)
    return {"src": "ninja", "name": nome, "items": items, "gems": gems(ch), "level": ch.get("level"),
            "tree": {"m": m, "s1": s1, "s2": s2, "a": asc, "attr": None, "jewels": {}}, "desc": ""}


if __name__ == "__main__":
    import re
    common.re = re
    bid, pasta = sys.argv[1], sys.argv[2]
    cortes = [a for a in sys.argv[3:] if "|" in a]
    base = sys.argv[3] if len(sys.argv) > 3 and "|" not in sys.argv[3] else "char_01"
    arq = os.path.join(ROOT, "dl", pasta, base + ".json")
    ch = json.load(open(arq, encoding="utf-8"))
    variants = [variant(ch, os.environ.get("FULL", "Endgame"))]
    for c in cortes:
        nome, pts = c.split("|")
        variants.append(variant(ch, nome, int(pts)))
    meta = [{"src": "ninja", "title": f"{ch['name']} ({ch['class']} {ch['level']}) — poe.ninja", "url": f"https://poe.ninja/poe2/builds/forbiddenrites/character/{ch['account']}/{ch['name']}",
             "author": ch["account"], "updatedAt": ch.get("updatedUtc"), "widgets": [], "notes": None, "profileNotes": {}, "rotations": {}}]
    json.dump({"guides": meta, "variants": variants}, open(os.path.join(ROOT, "dl", f"{bid}_variants.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for v in variants:
        print(f"- {v['name']}: árvore {len(v['tree']['m'])}+{len(v['tree']['s1'])}+{len(v['tree']['s2'])} | asc {len(v['tree']['a'])} | gems {[g['skill'] for g in v['gems']][:6]}")
