import json, glob, base64, zlib, re, sys, collections
out = []
cnt = collections.Counter()
for f in sorted(glob.glob("char_*.json")):
    d = json.load(open(f, encoding="utf-8"))
    ds = d["defensiveStats"]
    print("=" * 100)
    print(d["name"], d["level"], d["class"], "life", ds.get("life"), "ES", ds.get("energyShield"), "spirit", ds.get("spirit"), "MS", ds.get("movementSpeed"))
    print("  keystones:", [k["name"] for k in d["keystones"]])
    for s in d["skills"]:
        gems = [g["name"] for g in s["allGems"]]
        dps = [(x.get("name"), x.get("dps")) for x in s.get("dps", [])][:2]
        print("  SKILL:", gems, dps if dps else "")
        cnt.update(["G:" + gems[0]])
    for it in d["items"]:
        i = it["itemData"]
        tag = i["name"] + " / " + i["typeLine"] if i["frameTypeId"] == "Unique" else i["typeLine"]
        mods = (i.get("implicitMods") or []) + (i.get("explicitMods") or []) + (i.get("runeMods") or []) + (i.get("enchantMods") or [])
        print("  ITEM", i["inventoryId"], "|", i["frameTypeId"], "|", tag, "|", " ; ".join(re.sub(r"\[([^|\]]*\|)?([^\]]*)\]", r"\2", m) for m in mods)[:260])
        if i["frameTypeId"] == "Unique": cnt.update(["U:" + i["name"]])
    for it in d["flasks"]:
        i = it["itemData"]; print("  FLASK", i["name"], i["typeLine"])
        if i["frameTypeId"] == "Unique": cnt.update(["U:" + i["name"]])
    for it in d["jewels"]:
        i = it["itemData"]; print("  JEWEL", i["name"], i["typeLine"], " ; ".join(re.sub(r"\[([^|\]]*\|)?([^\]]*)\]", r"\2", m) for m in (i.get("explicitMods") or []))[:200])
    try:
        x = zlib.decompress(base64.urlsafe_b64decode(d["pathOfBuildingExport"] + "==")).decode("utf-8", "ignore")
        asc = re.search(r'ascendClassName="([^"]*)"', x)
        tree = re.search(r'<Spec[^>]*nodes="([^"]*)"', x)
        print("  ASC", asc and asc.group(1), "| mainSkill", re.search(r'mainSocketGroup="(\d+)"', x) and re.search(r'mainSocketGroup="(\d+)"', x).group(1))
        open("pob_" + d["name"] + ".xml", "w", encoding="utf-8").write(x)
    except Exception as e:
        print("  pob err", e)
print("\nCOUNTS", cnt.most_common(60))
