# -*- coding: utf-8 -*-
"""Converte um planner do Maxroll (dl/<fonte>.json, baixado de planners.maxroll.gg/profiles/poe2/<id>) no mesmo formato de extract.py.
Nomes/ícones de bases e gems: RePoE2 (dl/repoe_base_items.json); textos de mods: Path of Building (ModItem*.lua); uniques sem nome: poe.ninja.
Uso: python maxroll.py <bid> <fonte> [Perfil|pontos|nome ...]   — cada corte cria uma variante com os N primeiros pontos da árvore do perfil."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
import common

T = json.load(open(os.path.join(ROOT, "tree.json"), encoding="utf-8"))["nodes"]
BASES = json.load(open(os.path.join(ROOT, "dl", "repoe_base_items.json"), encoding="utf-8"))
UNIQ_ART = {u["name"]: (u.get("visual_identity") or {}).get("dds_file") for u in json.load(open(os.path.join(ROOT, "dl", "repoe_uniques.json"), encoding="utf-8")).values()}
SLOTS = {"Weapon": "mainHand_set1", "Offhand": "offHand_set1", "Weapon2": "mainHand_set2", "Offhand2": "offHand_set2", "Helm": "helmet", "BodyArmour": "body",
         "Gloves": "gloves", "Boots": "boots", "Amulet": "amulet", "Ring": "leftRing", "Ring2": "rightRing", "Belt": "belt", "Charm1": "charm1", "Charm2": "charm2",
         "Charm3": "charm3", "Flask1": "flask1", "Flask2": "flask2"}


def _mods():
    out = {}
    for f in ("ModItem.lua", "ModItemExclusive.lua", "ModCorrupted.lua"):
        p = os.path.join(ROOT, "dl", "pob", f)
        if not os.path.exists(p):
            continue
        for m in re.finditer(r'^\t\["([^"]+)"\] = \{ (.*?) statOrder', open(p, encoding="utf-8").read(), re.M):
            lines = re.findall(r'(?<![=\w] )"((?:[^"\\]|\\.)*)",', m.group(2))
            out.setdefault(m.group(1), [l for l in lines if l])
    return out


MODS = _mods()


def base(meta):
    b = BASES.get(meta) or BASES.get(meta.replace("/Gem/", "/Gems/")) or BASES.get(meta.replace("/Gems/", "/Gem/")) or {}
    return b.get("name"), (b.get("visual_identity") or {}).get("dds_file")


def fmt(v):
    return str(int(v)) if float(v).is_integer() else f"{v:.1f}".rstrip("0").rstrip(".")


def mod_text(mid, stats):
    lines = MODS.get(mid)
    if not lines:
        return []
    vals = list(stats.values())
    out = []
    for line in lines:
        def rep(m):
            if not vals:
                return m.group(0)
            a, b = sorted((float(m.group(1)), float(m.group(2))))
            for i, v in enumerate(vals):
                for w in (abs(v), abs(v) / 60):
                    if a <= w <= b:
                        vals.pop(i); return fmt(w)
            return fmt(abs(vals.pop(0)))
        out.append(re.sub(r"\((-?[\d.]+)-(-?[\d.]+)\)", rep, line))
    return out


OVERRIDE = {"local_unique_mages_legacy_1": "Mageblood"}


def unique_name(bname, texts, stat_ids=()):
    for k, v in OVERRIDE.items():
        if k in stat_ids:
            return v
    cands = [(n, e) for n, e in common.ECO.items() if e.get("base") == bname]
    if not cands:
        return None
    words = set(re.findall(r"[a-z]{4,}", " ".join(texts).lower()))
    score = lambda e: len(words & set(re.findall(r"[a-z]{4,}", " ".join(e["mods"]).lower())))
    best = max(cands, key=lambda c: score(c[1]))
    return best[0] if score(best[1]) >= 2 or len(cands) == 1 else None


def item(it):
    bname, dds = base(it["base"])
    texts = []
    for kind in ("implicit", "enchant", "explicit", "fractured", "crafted"):
        for mid, st in (it.get("mods", {}).get(kind) or {}).items():
            texts += mod_text(mid, st)
    runes = [base(s)[0] for s in it.get("sockets") or [] if s]
    name, u = bname, 0
    if it["rarity"] == "unique":
        name = it.get("name") or unique_name(bname, texts, {k for st in (it.get("stats") or {}).values() for k in st})
        u = 1 if name else 0
        name = name or bname
        e = common.ECO.get(name)
        dds = UNIQ_ART.get(name) or dds
        if e and e.get("mods"):
            imp = [t for mid, st in (it.get("mods", {}).get("implicit") or {}).items() for t in mod_text(mid, st)]
            texts = imp + e["mods"]
    return {"n": name, "u": u, "icon": dds, "mods": texts, "stats": [], "runes": runes, "skill": None}


def gems(steps, key):
    out = []
    for g in steps[0]["skills"]:
        gg = [x for x in g["gems"] if x.get("id")]
        if not gg:
            continue
        name, dds = base(gg[0]["id"])
        sups = [base(x["id"]) for x in gg[1:]]
        out.append({"skill": name, "slug": gg[0]["id"].split("/")[-1], "icon": dds, "skillIcon": dds, "sup": [s[0] for s in sups], "supIcons": {s[0]: s[1] for s in sups},
                    "weaponSet": None})
    return out


def tree(pv, limit=None, ascs=None):
    m, s1, s2, a = [], [], [], []
    events = []
    for h in pv["history"]:
        if isinstance(h, dict) and "remove" in h:
            events += [("rm", x, None) for x in h["remove"]]
        elif isinstance(h, dict) and "add" in h:
            events += [("add", x, None) for x in h["add"]]
        else:
            events.append(("add",) + ((h["id"], h.get("set")) if isinstance(h, dict) else (h, None)))
    for op, nid, st in events:
        if op == "rm":
            if limit is not None and len(m) >= limit:
                continue
            for lst in (m, s1, s2, a):
                if nid in lst: lst.remove(nid)
            continue
        n = T.get(str(nid), {})
        full = limit is not None and len(m) >= limit
        if n.get("ascendancyName"):
            if not full or (ascs is not None and nid in ascs): a.append(nid)
            continue
        if full:
            continue
        if st == 1: s1.append(nid)
        elif st == 2: s2.append(nid)
        else: m.append(nid)
    return {"m": m, "s1": s1, "s2": s2, "a": a, "attr": pv.get("attributes"), "jewels": pv.get("jewels") or {}}


if __name__ == "__main__":
    bid, src, cuts = sys.argv[1], sys.argv[2], sys.argv[3:]
    R = json.load(open(os.path.join(ROOT, "dl", f"{src}.json"), encoding="utf-8"))
    d = json.loads(R["data"]) if isinstance(R["data"], str) else R["data"]
    items = d["items"]
    variants, profiles = [], {}
    for p in d["profiles"]:
        eq = p["equipment"]["variants"][0]["items"]
        its = {SLOTS[k]: item(items[str(i)]) for k, i in eq.items() if k in SLOTS and str(i) in items}
        profiles[p["name"]] = (p, its)
        variants.append({"src": src, "name": p["name"], "items": its, "gems": gems(p["skills"]["steps"], p["name"]), "tree": tree(p["passives"]["variants"][0]), "desc": "", "level": p["level"]})
    for c in cuts:
        prof, n, nm, *asc = c.split("|")
        nm = [nm]; p, its = profiles[prof]
        ascs = {x for x in T if T[x].get("name") in asc} if asc else set()
        ascs = {int(x) for x in ascs} | {int(x) for x in T if asc and T[x].get("ascendancyName") and not T[x].get("isNotable")}
        variants.append({"src": src, "name": nm[0] if nm else f"{prof} {n}", "items": its, "gems": gems(p["skills"]["steps"], prof), "tree": tree(p["passives"]["variants"][0], int(n), ascs if asc else None), "desc": ""})
    meta = [{"src": src, "title": R["name"], "url": f"https://maxroll.gg/poe2/planner/{R['id']}", "author": (d.get("author") or {}).get("contentCreator"), "updatedAt": R.get("date"),
             "widgets": [], "notes": d.get("globalNotes"), "profileNotes": {p["name"]: p.get("widgetNotes") for p in d["profiles"]},
             "rotations": {p["name"]: p.get("skillRotations") for p in d["profiles"]}}]
    json.dump({"guides": meta, "variants": variants}, open(os.path.join(ROOT, "dl", f"{bid}_variants.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for v in variants:
        asc = [T[str(x)].get("name") for x in v["tree"]["a"] if T.get(str(x), {}).get("isNotable")]
        print(f"- {v['name']} | tree {len(v['tree']['m'])}+{len(v['tree']['s1'])}+{len(v['tree']['s2'])} | asc {asc} | gems {[g['skill'] for g in v['gems']]}")
    for v in variants[:len(d["profiles"])]:
        for s, it in v["items"].items():
            print("   ", v["name"], s, it["u"], it["n"], "|", " ; ".join(it["mods"])[:150], "| runes", it["runes"], "| icon", bool(it["icon"]))
