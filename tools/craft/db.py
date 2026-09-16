# -*- coding: utf-8 -*-
"""Extract published PoE2DB tables. DropChance values are not independently verified."""
import re, json, html, os, glob
HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(HERE, "..", "dl", "web")
KEEP = ["normal", "desecrated", "essence", "perfect_essence", "corruption_upgrade", "breach_minion", "breach_caster", "breach_otherworldly", "corrupted"]

def clean(s):
    s = re.sub(r'<br\s*/?>', ' / ', s or '', flags=re.I)
    s = re.sub(r"<[^>]+>", "", s or "")
    return html.unescape(s).replace("—", "-").strip()

def views(page):
    s = open(os.path.join(WEB, page + ".html"), encoding="utf-8").read()
    dec = json.JSONDecoder(); out = []
    for m in re.finditer(r"ModsView\(", s):
        j = s.find("{", m.end())
        try:
            obj, _ = dec.raw_decode(s[j:])
        except Exception:
            continue
        out.append(obj)
    return out

def norm(obj):
    res = []
    for kind in KEEP:
        for x in obj.get(kind) or []:
            name = clean(x.get("Name", ""))
            res.append(dict(kind=kind, name=name, level=int(x.get("Level") or 0),
                            gen={"1": "Prefix", "2": "Suffix"}.get(str(x.get("ModGenerationTypeID")), str(x.get("ModGenerationTypeID"))),
                            family=(x.get("ModFamilyList") or [""])[0], families=x.get("ModFamilyList") or [], weight=int(x.get("DropChance") or 0),
                            text=clean(x.get("str", "")).replace("\n", " / "),
                            spawn=x.get("spawn_no") or [], tags=x.get("fossil_no") or [], code=x.get("Code", "")))
    return res

def load(page):
    p = os.path.join(WEB, "mods_%s.json" % page)
    if not os.path.exists(p):
        vs = views(page)
        data = [dict(opt=v.get("opt"), mods=norm(v)) for v in vs]
        json.dump(data, open(p, "w", encoding="utf-8"), ensure_ascii=False)
    return json.load(open(p, encoding="utf-8"))

def pool(page, base_tags, kind="normal", view=0):
    d = load(page)[view]["mods"]
    return [m for m in d if m["kind"] == kind and (not base_tags or any(t in base_tags for t in m["spawn"]))]

def show(page, base_tags, pattern=".", kind="normal", top=3):
    rx = re.compile(pattern, re.I)
    ms = pool(page, base_tags, kind)
    tot = {g: sum(m["weight"] for m in ms if m["gen"] == g) for g in ("Prefix", "Suffix")}
    fam = {}
    for m in ms:
        if rx.search(m["text"]):
            fam.setdefault((m["gen"], m["family"]), []).append(m)
    for (g, f), l in sorted(fam.items()):
        l.sort(key=lambda m: -m["level"])
        w = sum(m["weight"] for m in l)
        print(f"[{g}] {f}  peso família {w}/{tot.get(g, 0)} ({100*w/max(1,tot.get(g,1)):.1f}%)")
        for i, m in enumerate(l[:top]):
            print(f"   T{i+1} ilvl{m['level']:>3} w{m['weight']:>5} {m['text']}  [{m['name']}]")

if __name__ == "__main__":
    import sys
    page, tags = sys.argv[1], [t for t in sys.argv[2].split(",") if t]
    show(page, tags, sys.argv[3] if len(sys.argv) > 3 else ".", sys.argv[4] if len(sys.argv) > 4 else "normal", int(sys.argv[5]) if len(sys.argv) > 5 else 3)
