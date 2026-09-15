# -*- coding: utf-8 -*-
"""Baixa ícones, calcula geometria da árvore e cruza com as fases -> assets.json"""
import json, math, os, io, re, base64, hashlib, urllib.request
from PIL import Image
import chober as D

MOBA = "https://cdn.mobalytics.gg/assets/poe-2/images/game/Art/"
P2DB = "https://cdn.poe2db.tw/image/Art/"
os.makedirs("iconcache", exist_ok=True)

def fetch(path):
    """path relativo a Art/ (sem extensão ou com .webp/.dds)"""
    path = re.sub(r"^Art/", "", re.sub(r"\.(dds|webp|avif|png)$", "", path))
    fn = "iconcache/" + hashlib.md5(path.encode()).hexdigest() + ".webp"
    if os.path.exists(fn) and os.path.getsize(fn) > 100:
        return open(fn, "rb").read()
    for base, ref in ((MOBA, None), (P2DB, "https://poe2db.tw/")):
        try:
            h = {"User-Agent": "Mozilla/5.0"}
            if ref: h["Referer"] = ref
            b = urllib.request.urlopen(urllib.request.Request(base + path + ".webp", headers=h), timeout=30).read()
            if len(b) > 100:
                open(fn, "wb").write(b); return b
        except Exception:
            pass
    print("MISS", path); return None

ICONS = {}
def icon(path, box):
    if not path: return None
    key = re.sub(r"\.(dds|webp|avif|png)$", "", path).split("/")[-1] + f"_{box}"
    if key in ICONS: return key
    b = fetch(path)
    if not b: return None
    im = Image.open(io.BytesIO(b)).convert("RGBA")
    bb = im.getbbox()
    if bb: im = im.crop(bb)
    im.thumbnail((box, box), Image.LANCZOS)
    out = io.BytesIO(); im.save(out, "WEBP", quality=82, method=6)
    ICONS[key] = "data:image/webp;base64," + base64.b64encode(out.getvalue()).decode()
    return key

T = json.load(open("tree.json", encoding="utf-8"))
N = T["nodes"]; G = T["groups"]; C = T["constants"]
MATT = json.load(open("dl/matt.json", encoding="utf-8"))
def conv(v):
    """variante Mattjestic -> formato (v, w) usado abaixo"""
    it = v["items"]; clean = lambda n: re.sub(r"\s*\((helmet|equipment)\)", "", n)
    fix = lambda x: dict(x, n=clean(x["n"])) if x else None
    w = {"mh1": fix(it.get("mainHand1")), "mh2": fix(it.get("mainHand2")), "oh1": fix(it.get("offHand1")), "oh2": fix(it.get("offHand2")),
         "runes": {k: x["r"] for k, x in it.items() if x and x.get("r")}}
    e = [[k, clean(x["n"]), x["u"], x["i"], x["x"]] for k, x in it.items() if x and not k.startswith(("mainHand", "offHand"))]
    return {"t": v["t"], "g": v["gems"], "e": e}, w

# fase -> (lista, índice)
# fase -> índice da variante no guia do Mattjestic
VMAP = {"a1": 5, "a2": 7, "a3": 8, "a4": 9, "int": 10, "ea": 11, "t15": 13, "mm": 17, "uber": 18}
def V(pid):
    return conv(MATT["vs"][VMAP[pid]])

# ------------------------------------------------------------ geometria
def pos(nid):
    n = N[str(nid)]; g = G[n["group"] - 1]
    r = C["orbitRadii"][n["orbit"]]; a = C["orbitAnglesByOrbit"][n["orbit"]][n["orbitIndex"]]
    return g["x"] + r * math.sin(a), g["y"] - r * math.cos(a)

def info(nid):
    n = N[str(nid)]
    opts = n.get("options"); o = opts.get("Huntress") if isinstance(opts, dict) else None
    name = (o or n).get("name", n.get("name")); stats = (o or n).get("stats", n.get("stats", [])); ic = (o or n).get("icon", n.get("icon"))
    kind = 2 if n.get("isKeystone") else 3 if n.get("isJewelSocket") else 1 if n.get("isNotable") else 4 if n.get("isAttribute") else 0
    return name, stats, ic, kind

def build_graph(filter_fn):
    ids = [int(k) for k, n in N.items() if filter_fn(n) and not n.get("isOnlyImage") and isinstance(n.get("group"), int) and 1 <= n["group"] <= len(G) and G[n["group"] - 1] and "orbit" in n]
    idx = {nid: i for i, nid in enumerate(ids)}
    nodes, meta = [], {}
    for nid in ids:
        x, y = pos(nid); name, stats, ic, kind = info(nid)
        nodes.append([nid, round(x), round(y), kind])
        if kind in (1, 2, 3):
            meta[nid] = [name, stats]
        elif kind in (0, 4):
            meta[nid] = [name, stats]
    edges, seen = [], set()
    for nid in ids:
        n = N[str(nid)]
        for cn in n["connections"]:
            j = cn["id"]; o = cn["orbit"]
            if j not in idx or o == 2147483647: continue
            k = tuple(sorted((nid, j)))
            if k in seen: continue
            seen.add(k)
            m = N[str(j)]
            x1, y1 = pos(nid); x2, y2 = pos(j)
            arc = None
            if o == 0 and n["group"] == m["group"] and n["orbit"] == m["orbit"] and n["orbit"] > 0:
                g = G[n["group"] - 1]; arc = (g["x"], g["y"], C["orbitRadii"][n["orbit"]])
            elif o != 0:
                r = C["orbitRadii"][abs(o)]; dx, dy = x2 - x1, y2 - y1; d = math.hypot(dx, dy)
                if d > 0 and r >= d / 2:
                    h = math.sqrt(r * r - (d / 2) ** 2); mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    px, py = -dy / d, dx / d; s = 1 if o > 0 else -1
                    arc = (mx + s * px * h, my + s * py * h, r)
            if arc:
                cx, cy, r = arc
                edges.append([idx[nid], idx[j], round(cx), round(cy), round(r)])
            else:
                edges.append([idx[nid], idx[j]])
    return nodes, edges, meta

main_nodes, main_edges, main_meta = build_graph(lambda n: not n.get("ascendancyName"))
asc_nodes, asc_edges, asc_meta = build_graph(lambda n: n.get("ascendancyName") == "Spirit Walker")
print("main", len(main_nodes), len(main_edges), "asc", len(asc_nodes))

# ícones das passivas alocadas (notables/keystones/asc/jewel)
alloc = {}
passive_icons = {}
for pid in VMAP:
    v, w = V(pid)
    t = v["t"]
    alloc[pid] = {"m": t["m"], "s1": t["s1"], "s2": t["s2"], "a": t["a"]}
    for nid in t["m"] + t["s1"] + t["s2"] + t["a"]:
        name, stats, ic, kind = info(nid)
        if kind in (1, 2, 3) or N[str(nid)].get("ascendancyName"):
            k = icon(ic, 52)
            if k: passive_icons[nid] = k

# notáveis por fase (em ordem do caminho mobalytics) + novos vs fase anterior
order = ["a1", "a2", "a3", "a4", "int", "ea", "t15", "mm", "uber"]
notables = {}
prev = set()
for pid in order:
    a = alloc[pid]; cur = set(a["m"] + a["s1"] + a["s2"])
    lst = []
    for nid in a["m"] + a["s1"] + a["s2"]:
        name, stats, ic, kind = info(nid)
        if kind in (1, 2, 3):
            set_ = "s1" if nid in a["s1"] else "s2" if nid in a["s2"] else "m"
            lst.append({"id": nid, "n": name, "s": stats, "k": kind, "ic": passive_icons.get(nid), "new": nid not in prev, "set": set_, "pass": name == "Inspiring Ally" and pid not in ("a1", "a2")})
    removed = [info(x)[0] for x in prev - cur if info(x)[3] in (1, 2)]
    notables[pid] = {"list": lst, "count": len(a["m"]), "s1": len(a["s1"]), "s2": len(a["s2"]), "removed": removed,
                     "asc": [{"id": x, "n": info(x)[0], "s": info(x)[1], "ic": passive_icons.get(x)} for x in a["a"] if N[str(x)].get("isNotable")]}
    prev = cur

# ------------------------------------------------------------ gems / supports / itens
SLOT_PT = {"mh1": "Arma (Set 1)", "mh2": "Arma (Set 2)", "oh1": "Offhand (Set 1)", "oh2": "Offhand (Set 2)", "helmet": "Capacete", "body": "Body Armour",
           "gloves": "Luvas", "boots": "Botas", "amulet": "Amuleto", "leftRing": "Anel E", "rightRing": "Anel D", "belt": "Cinto",
           "flask1": "Flask vida", "flask2": "Flask mana", "charm1": "Charm", "charm2": "Charm", "charm3": "Charm"}
RUNE_PT = {"soulcore-talismanmonkey": "Primate Idol", "soulcore-talismanfox": "Fox Idol", "soulcore-talismancat": "Cat Idol",
           "soulcore-idolhawk": "Hawk Idol", "soulcore-talismanspecial2": "Idol (especial)", "soulcore-talismanspecial6": "Idol (especial)", "soulcore-idolspecial2": "Idol (especial)", "soulcore-idolcorrupted1": "Idol corrompido", "soulcore-runespecial1": "Runa especial", "soulcore-runelightninglesser": "Lesser Storm Rune",
           "soulcore-runefirelesser": "Lesser Desert Rune", "soulcore-runecoldlesser": "Lesser Glacial Rune", "soulcore-runeenhancegreater": "Greater Rune of Leadership"}
gem_icon, sup_icon, guide = {}, {}, {}
norm = lambda s: re.sub(r"[^a-z]", "", s.lower().replace(" iii", "three").replace(" ii", "two").replace(" i", ""))
for p in D.PHASES:
    v, w = V(p["id"])
    vg = list(v["g"]); used = [False] * len(vg)
    for g in p["gems"]:
        base = re.sub(r"\s*\(.*\)", "", g["skill"]).strip()
        for i, x in enumerate(vg):
            alias = x[0] in ("Companion: {0}", "Tame Beast") if base == "Tame Beast" else x[0] == base
            if base == "Tame Beast" and not g["sup"]: alias = x[0] == "Tame Beast"
            if not used[i] and alias:
                used[i] = True
                k = icon(x[1], 64)
                if k and not (base == "Tame Beast" and x[0] != "Tame Beast"): gem_icon.setdefault(base, k)
                subs = x[2]
                if len(subs) == len(g["sup"]):
                    for sname, sub in zip(g["sup"], subs):
                        sk = icon(sub.split("|", 1)[1], 40)
                        if sk: sup_icon.setdefault(sname, sk)
                else:
                    for sname in g["sup"]:
                        for sub in subs:
                            if norm(sname) and norm(sname) in sub.split("|")[0]:
                                sk = icon(sub.split("|", 1)[1], 40)
                                if sk: sup_icon.setdefault(sname, sk)
                break
    items = []
    for key in ("mh1", "oh1", "mh2", "oh2"):
        it = w.get(key)
        if it:
            items.append({"slot": SLOT_PT[key], "n": it["n"], "u": 1 if it["u"] else 0, "ic": icon(it["i"], 96), "x": it["x"], "r": [RUNE_PT.get(r, r.replace("soulcore-", "")) for r in it["r"]]})
    for e in v["e"]:
        slot, name, uniq, ic, mods = e
        if slot.startswith("flask"): continue
        items.append({"slot": SLOT_PT.get(slot, slot), "n": name.replace(" (helmet)", ""), "u": uniq, "ic": icon(ic, 96), "x": mods,
                      "r": [RUNE_PT.get(r, r.replace("soulcore-", "")) for r in w["runes"].get(slot, [])]})
    guide[p["id"]] = items

# ícones extras: skills/uniques que não aparecem nos planners
EXTRA = {
 "gem:Mana Remnants": "2DItems/Gems/New/EnergyRemnantsSkillGem",
 "u:Tyranny's Grip": "2DItems/Weapons/OneHandWeapons/OneHandSpears/Uniques/ArmsLength",
 "u:Sylvan's Effigy": "2DItems/Weapons/OneHandWeapons/Scepters/Uniques/Packleader",
 "u:Trenchtimbre": "2DItems/Weapons/OneHandWeapons/OneHandMaces/Uniques/Trenchtimbre",
 "u:Meginord's Girdle": "2DItems/Belts/Uniques/MeginordsGirdle",
 "u:Prism of Belief": "2DItems/Jewels/SacredFlameJewel",
 "u:From Nothing": "2DItems/Jewels/RitualJewel",
 "u:Primate Idol": "2DItems/Currency/TormentedSpiritSocketables/AzmeriSocketableMonkey",
 "u:Idol of Ralakesh": "2DItems/Currency/TormentedSpiritSocketables/AzmeriSocketableMonkeySpecial",
 "u:Fox Idol": "2DItems/Currency/TormentedSpiritSocketables/AzmeriSocketableFox",
}
uniq_icon = {}
for k, path in EXTRA.items():
    ik = icon(path, 96 if k.startswith("u:") else 64)
    if not ik: continue
    if k.startswith("gem:"): gem_icon[k[4:]] = ik
    else: uniq_icon[k[2:]] = ik
for pid in VMAP:
    v, w = V(pid)
    for e in v["e"]:
        if e[2]: uniq_icon.setdefault(e[1].replace(" (helmet)", ""), icon(e[3], 96))
# Tame Beast genérico
for v_ in MATT["vs"]:
    for x in v_["gems"]:
        if x[0] == "Tame Beast" and x[1]: gem_icon.setdefault("Tame Beast", icon(x[1], 64))


# ---- uniques / idols (ícones oficiais do poecdn via poe.ninja)
def icon_url(url, key, box):
    if not url: return None
    k = key + f"_{box}"
    if k in ICONS: return k
    fn = "iconcache/" + hashlib.md5(url.encode()).hexdigest() + ".img"
    if not os.path.exists(fn):
        try:
            open(fn, "wb").write(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read())
        except Exception as e:
            print("MISS url", key, e); return None
    im = Image.open(fn).convert("RGBA"); bb = im.getbbox()
    if bb: im = im.crop(bb)
    im.thumbnail((box, box), Image.LANCZOS); out = io.BytesIO(); im.save(out, "WEBP", quality=84, method=6)
    ICONS[k] = "data:image/webp;base64," + base64.b64encode(out.getvalue()).decode(); return k
for u in D.UNIQUES:
    k = icon_url(u.get("iconUrl"), "U_" + re.sub(r"[^A-Za-z]", "", u["n"]), 96)
    if k: uniq_icon[u["n"]] = k
for i in D.IDOLS:
    k = icon_url(i.get("iconUrl"), "I_" + re.sub(r"[^A-Za-z]", "", i["n"]), 64)
    if k: uniq_icon[i["n"]] = k
def poe2db_icon(page):
    try:
        t = urllib.request.urlopen(urllib.request.Request("https://poe2db.tw/us/" + page, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126"}), timeout=25).read().decode("utf-8", "ignore")
        m = re.findall(r"cdn\.poe2db\.tw/image/Art/(2DItems/Gems/[A-Za-z0-9_/]+)\.webp", t)
        return m[0] if m else None
    except Exception as e:
        print("poe2db", page, e); return None
need_sup = sorted({s for p in D.PHASES for g in p["gems"] for s in g["sup"]} - set(sup_icon))
for sname in need_sup:
    base = re.sub(r"\s*\(.*\)", "", sname).strip()
    path = poe2db_icon(base.replace(" ", "_").replace("'", ""))
    if path:
        k = icon(path, 40)
        if k: sup_icon[sname] = k
need_gem = sorted({re.sub(r"\s*\(.*\)", "", g["skill"]).strip() for p in D.PHASES for g in p["gems"]} - set(gem_icon))
for gname in need_gem:
    first = gname.split(" / ")[0]
    path = poe2db_icon(first.replace(" ", "_").replace("'", ""))
    if path:
        k = icon(path, 64)
        if k: gem_icon[gname] = k

# ---- notables do meta (amostra poe.ninja) -> ids na árvore
meta_notables = []
byname = {}
for k, n in N.items():
    if n.get("ascendancyName"): continue
    nm = info(int(k))[0]
    if n.get("isNotable") or n.get("isKeystone"):
        byname.setdefault(nm, []).append(int(k))
# frequência real por id na amostra
C_ = json.load(open("dl/ninja.json", encoding="utf-8"))
zoo = [c for c in C_ if any(("Tame Beast" in g or "Companion:" in g) for s_ in c["skills"] for g in s_[0])]
from collections import Counter
cnt = Counter(pid for c in zoo for pid in (c["ps"] or []))
for nm, pct in D.META["sample"]["notables"]:
    ids = byname.get(nm, [])
    if not ids: print("meta notable not found", nm); continue
    best = max(ids, key=lambda i: cnt.get(i, 0))
    n0 = N[str(best)]
    meta_notables.append({"id": best, "n": nm, "pct": pct, "s": info(best)[1], "ic": icon(info(best)[2], 52), "k": 2 if n0.get("isKeystone") else 1})
    if meta_notables[-1]["ic"]: passive_icons[best] = meta_notables[-1]["ic"]
print("meta notables", len(meta_notables))

sets_out = {}
for pid, modes in D.SETS.items():
    sets_out[pid] = {}
    planner = {i["slot"]: i for i in guide.get(pid, [])}
    for mode, items in modes.items():
        rows = []
        for it in items:
            ic_key = uniq_icon.get(it["n"]) if it["u"] else (planner.get(it["slot"]) or {}).get("ic")
            if not ic_key and not it["u"]:
                base = next((g for g in guide.get("ea", []) if g["slot"] == it["slot"]), None) or next((g for g in guide.get("t15", []) if g["slot"] == it["slot"]), None)
                ic_key = base and base["ic"]
            u = next((x for x in D.UNIQUES if x["n"] == it["n"]), None)
            mods = it["mods"] or ((u or {}).get("mods") or [])
            if it["u"]:
                catha = pid in ("ea", "t15", "mm") and it["slot"].startswith("Arma")
                keep = re.compile(r"(Minion|Companion|Spirit|Allies|Presence|maximum Life|Resistance|Evasion|Deflect|Energy Shield|Giant|Attribute|Movement Speed|maximum Mana|Charge|Ground|Recover|Flask|Augment|Socket|Strength|Onslaught|Critical Damage Bonus per|Possessed)", re.I)
                shown = [m for m in mods if (keep.search(m) and not re.search(r"to Attacks|Attack Speed|Physical Damage to Attacks", m, re.I)) or (catha and re.search(r"Physical Damage", m) and not re.search(r"to Attacks", m))]
                hidden = len(mods) - len(shown)
                mods = shown + ([f"(+{hidden} mod{'s' if hidden > 1 else ''} de ataque/utilidade que não {'importam' if hidden > 1 else 'importa'} para o zoo)"] if hidden else [])
            rows.append({"slot": it["slot"], "n": it["n"], "u": it["u"], "ic": ic_key, "x": " ; ".join(mods[:6]), "r": it["r"], "note": it.get("note", ""), "price": (u or {}).get("price")})
        sets_out[pid][mode] = rows
print("sets", {k: len(v["cheap"]) for k, v in sets_out.items()})
A = dict(icons=ICONS, tree=dict(nodes=main_nodes, edges=main_edges, meta={str(k): v for k, v in main_meta.items()}),
         asc=dict(nodes=asc_nodes, edges=asc_edges, meta={str(k): v for k, v in asc_meta.items()}),
         alloc=alloc, notables=notables, passiveIcon={str(k): v for k, v in passive_icons.items()},
         gemIcon=gem_icon, metaNotables=meta_notables, sets=sets_out, supIcon=sup_icon, uniqIcon=uniq_icon, guide=guide)
s = json.dumps(A, ensure_ascii=False, separators=(",", ":"))
open("assets.json", "w", encoding="utf-8").write(s)
print("icons", len(ICONS), "bytes", len(s), "gems", len(gem_icon), "sups", len(sup_icon), "uniq", len(uniq_icon))
missing_sup = sorted({s for p in D.PHASES for g in p["gems"] for s in g["sup"]} - set(sup_icon))
print("sups sem ícone:", missing_sup)
print("gems sem ícone:", sorted({re.sub(r"\s*\(.*\)", "", g["skill"]).strip() for p in D.PHASES for g in p["gems"]} - set(gem_icon)))
