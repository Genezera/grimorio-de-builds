# Converte o JSON bruto da build do Lowepe (Mobalytics) em um formato compacto, com nomes reais de gems/supports (Path of Building).
import json, re, os, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT = ".."
R = json.load(open(f"{ROOT}/dl/oracle_raw.json", encoding="utf-8"))
NOTES = json.load(open(f"{ROOT}/dl/oracle_notes.json", encoding="utf-8"))
T = json.load(open(f"{ROOT}/tree.json", encoding="utf-8"))

# grantedEffectId (minúsculo) -> nome
gems_lua = open(f"{ROOT}/dl/pob/Gems.lua", encoding="utf-8").read()
SLUG = {}
for m in re.finditer(r'name = "([^"]+)",\s*\n\s*gameId = "[^"]*",\s*\n\s*variantId = "[^"]*",\s*\n\s*grantedEffectId = "([^"]+)"', gems_lua):
    SLUG[m.group(2).lower()] = m.group(1)

def gname(slug):
    return SLUG.get(slug, slug)

def item(x):
    if not x:
        return None
    ci = x.get("commonItem") or x.get("uniqueItem")
    if not ci:
        if x.get("providedSkill"):
            return {"skill": x["providedSkill"]["name"]}
        return None
    mods = [d["description"] for d in (ci.get("explicitDescriptions") or []) if d.get("description")]
    imp = [d["description"] for d in (ci.get("implicitDescriptions") or []) if isinstance(d, dict) and d.get("description")]
    runes = [r.get("name") or r.get("slug") for r in (x.get("runes") or []) if r]
    return {"n": ci.get("name"), "u": 1 if ci.get("isUnique") else 0, "icon": ci.get("iconURL"), "mods": imp + mods,
            "stats": ci.get("stats") or [], "runes": runes, "skill": (x.get("providedSkill") or {}).get("name")}

def ids(tree):
    return [int(s.split("-")[1]) for s in ((tree or {}).get("selectedSlugs") or []) if s.startswith("node-")]

out = []
for i, v in enumerate(R["data"]["buildVariants"]["values"]):
    eq = v["equipment"]
    items = {}
    for slot in ("helmet", "body", "gloves", "boots", "amulet", "leftRing", "rightRing", "belt", "charm1", "charm2", "charm3", "flask1", "flask2"):
        items[slot] = item(eq.get(slot))
    for hand in ("mainHand", "offHand"):
        for s in ("set1", "set2"):
            items[f"{hand}_{s}"] = item((eq.get(hand) or {}).get(s))
    gems = []
    for g in (v.get("skillGems") or {}).get("gems", []):
        a = g.get("activeSkill")
        if not a:
            continue
        gems.append({"skill": a["name"], "slug": a.get("gemSlug"), "icon": a.get("gemIconURL") or a.get("iconURL"), "skillIcon": a.get("iconURL"),
                     "sup": [gname(s["gemSlug"]) for s in (g.get("subSkills") or [])],
                     "supIcons": {gname(s["gemSlug"]): s.get("iconURL") for s in (g.get("subSkills") or [])},
                     "supSlugs": [s["gemSlug"] for s in (g.get("subSkills") or [])],
                     "weaponSet": g.get("weaponSet")})
    pt = v["passiveTree"]
    asc_ids = ids(pt.get("ascendancyTree"))
    jewels = pt.get("jewels") or []
    out.append({"idx": i, "name": R["names"][i], "items": items, "gems": gems,
                "tree": {"m": ids(pt.get("mainTree")), "s1": ids(pt.get("set1Tree")), "s2": ids(pt.get("set2Tree")), "a": asc_ids,
                         "attr": pt.get("attributeNodes"), "jewels": jewels},
                "req": (v.get("skillGems") or {}).get("gemRequirements"),
                "notes": next((x for x in NOTES["variants"] if x["title"] == R["names"][i]), {})})
unknown = sorted({s for v in out for g in v["gems"] for s in g["sup"] if s == s.lower()})
json.dump({"title": R["title"], "variants": out, "text": R["text"], "sections": NOTES["sections"], "questRewards": R["data"].get("questRewards")},
          open(f"{ROOT}/dl/oracle_variants.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("variants", len(out), "unknown support slugs:", unknown)
for v in out:
    print(v["idx"], v["name"], "| asc", [T["nodes"][str(a)].get("name") for a in v["tree"]["a"] if str(a) in T["nodes"]], "| jewels", [j.get("name") if isinstance(j, dict) else j for j in v["tree"]["jewels"]][:5])
    for g in v["gems"]:
        print("    ", g["skill"], g["sup"], "ws", g["weaponSet"])
    print("    items:", {k: (x["n"] + ("*" if x.get("u") else "")) if x and x.get("n") else (x or {}).get("skill") for k, x in v["items"].items() if x})
