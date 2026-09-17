# -*- coding: utf-8 -*-
"""Converte guias do Mobalytics (dl/<fonte>_raw.json) em variantes compactas: gems/supports com nomes reais,
itens, árvore por fase e notas do autor.  Uso: python extract.py <bid> <fonte1> [<fonte2> ...]
Com mais de uma fonte, os nomes das variantes ganham o prefixo "<fonte>: "."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pob

ROOT = os.path.join(HERE, "..")
T = json.load(open(os.path.join(ROOT, "tree.json"), encoding="utf-8"))
SLUG = pob.slug_names()


def gname(slug):
    s2 = slug.replace("player", ""); return SLUG.get(slug, SLUG.get(s2, SLUG.get(s2.replace("support", "", 1), slug)))


def item(x):
    if not x:
        return None
    ci = x.get("commonItem") or x.get("uniqueItem")
    if not ci:
        return {"skill": x["providedSkill"]["name"]} if x.get("providedSkill") else None
    mods = [d["description"] for d in (ci.get("explicitDescriptions") or []) if d.get("description")]
    imp = [d["description"] for d in (ci.get("implicitDescriptions") or []) if isinstance(d, dict) and d.get("description")]
    runes = [r.get("name") or r.get("slug") for r in (x.get("runes") or []) if r]
    return {"n": ci.get("name"), "u": 1 if ci.get("isUnique") else 0, "icon": ci.get("iconURL"), "mods": imp + mods,
            "stats": ci.get("stats") or [], "runes": runes, "skill": (x.get("providedSkill") or {}).get("name")}


def ids(tree):
    return [int(s.split("-")[1]) for s in ((tree or {}).get("selectedSlugs") or []) if s.startswith("node-")]


def convert(src, prefix):
    R = json.load(open(os.path.join(ROOT, "dl", f"{src}_raw.json"), encoding="utf-8"))
    out = []
    for i, v in enumerate(R["data"]["buildVariants"]["values"]):
        eq = v["equipment"]
        items = {s: item(eq.get(s)) for s in ("helmet", "body", "gloves", "boots", "amulet", "leftRing", "rightRing", "belt", "charm1", "charm2", "charm3", "flask1", "flask2")}
        for hand in ("mainHand", "offHand"):
            for s in ("set1", "set2"):
                items[f"{hand}_{s}"] = item((eq.get(hand) or {}).get(s))
        gems = []
        for g in (v.get("skillGems") or {}).get("gems", []):
            a = g.get("activeSkill")
            if not a:
                continue
            subs = g.get("subSkills") or []
            gems.append({"skill": a["name"], "slug": a.get("gemSlug"), "icon": a.get("gemIconURL") or a.get("iconURL"), "skillIcon": a.get("iconURL"),
                         "sup": [gname(s["gemSlug"]) for s in subs], "supIcons": {gname(s["gemSlug"]): s.get("iconURL") for s in subs},
                         "weaponSet": g.get("weaponSet")})
        pt = v["passiveTree"]
        name = R["names"][i]
        out.append({"src": src, "name": (prefix + name) if prefix else name, "items": items, "gems": gems,
                    "tree": {"m": ids(pt.get("mainTree")), "s1": ids(pt.get("set1Tree")), "s2": ids(pt.get("set2Tree")), "a": ids(pt.get("ascendancyTree")),
                             "attr": pt.get("attributeNodes"), "jewels": pt.get("jewels") or []},
                    "desc": (R.get("variantDesc") or [""] * 99)[i]})
    return R, out


if __name__ == "__main__":
    bid, srcs = sys.argv[1], sys.argv[2:]
    variants, meta = [], []
    for s in srcs:
        R, vs = convert(s, (s + ": ") if len(srcs) > 1 else "")
        variants += vs
        meta.append({"src": s, "title": R["title"], "url": R.get("url"), "author": R.get("author"), "updatedAt": R.get("updatedAt"), "widgets": R.get("widgets", [])})
    json.dump({"guides": meta, "variants": variants}, open(os.path.join(ROOT, "dl", f"{bid}_variants.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    unknown = sorted({s for v in variants for g in v["gems"] for s in g["sup"] if s == s.lower()})
    print(bid, "variants", len(variants), "unknown slugs:", unknown)
    for v in variants:
        asc = [T["nodes"][str(a)].get("name") for a in v["tree"]["a"] if str(a) in T["nodes"] and T["nodes"][str(a)].get("isNotable")]
        print(f"- {v['name']} | tree {len(v['tree']['m'])}+{len(v['tree']['s1'])}+{len(v['tree']['s2'])} | asc {asc}")
