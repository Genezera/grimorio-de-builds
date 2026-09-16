# -*- coding: utf-8 -*-
"""Assets do Oracle: árvore (opções da Druid), ascendência Oracle, alocação por fase, ícones, sets."""
import json, math, os, io, re, base64, hashlib, urllib.request, sys
from collections import deque
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
import odata as D
os.chdir(ROOT)  # iconcache/ e tree.json da raiz de tools

MOBA = "https://cdn.mobalytics.gg/assets/poe-2/images/game/Art/"
P2DB = "https://cdn.poe2db.tw/image/Art/"
CLASS = "Druid"; ASC = "Oracle"; START = 61525

def fetch(path):
    path = re.sub(r"^.*?/Art/", "", path); path = re.sub(r"^Art/", "", re.sub(r"\.(dds|webp|avif|png)$", "", path))
    fn = "iconcache/" + hashlib.md5(path.encode()).hexdigest() + ".webp"
    if os.path.exists(fn) and os.path.getsize(fn) > 100:
        return open(fn, "rb").read()
    for base, ref, ext in ((MOBA, None, ".webp"), (MOBA, None, ".avif"), (P2DB, "https://poe2db.tw/", ".webp")):
        try:
            h = {"User-Agent": "Mozilla/5.0"}
            if ref: h["Referer"] = ref
            b = urllib.request.urlopen(urllib.request.Request(base + path + ext, headers=h), timeout=30).read()
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
    try:
        im = Image.open(io.BytesIO(b)).convert("RGBA")
    except Exception as e:
        print("BADIMG", path, e); return None
    bb = im.getbbox()
    if bb: im = im.crop(bb)
    im.thumbnail((box, box), Image.LANCZOS)
    out = io.BytesIO(); im.save(out, "WEBP", quality=82, method=6)
    ICONS[key] = "data:image/webp;base64," + base64.b64encode(out.getvalue()).decode()
    return key

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

T = json.load(open("tree.json", encoding="utf-8"))
N = T["nodes"]; GR = T["groups"]; C = T["constants"]

def pos(nid):
    n = N[str(nid)]; g = GR[n["group"] - 1]
    r = C["orbitRadii"][n["orbit"]]; a = C["orbitAnglesByOrbit"][n["orbit"]][n["orbitIndex"]]
    return g["x"] + r * math.sin(a), g["y"] - r * math.cos(a)

def info(nid):
    n = N[str(nid)]
    opts = n.get("options"); o = opts.get(CLASS) if isinstance(opts, dict) else None
    name = (o or n).get("name", n.get("name")); stats = (o or n).get("stats", n.get("stats", [])); ic = (o or n).get("icon", n.get("icon"))
    kind = 2 if n.get("isKeystone") else 3 if n.get("isJewelSocket") else 1 if n.get("isNotable") else 4 if n.get("isAttribute") else 0
    return name, stats, ic, kind

def build_graph(filter_fn):
    ids = [int(k) for k, n in N.items() if filter_fn(n) and not n.get("isOnlyImage") and isinstance(n.get("group"), int) and 1 <= n["group"] <= len(GR) and GR[n["group"] - 1] and "orbit" in n]
    idx = {nid: i for i, nid in enumerate(ids)}
    nodes, meta = [], {}
    for nid in ids:
        x, y = pos(nid); name, stats, ic, kind = info(nid)
        nodes.append([nid, round(x), round(y), kind]); meta[nid] = [name, stats]
    edges, seen = [], set()
    for nid in ids:
        n = N[str(nid)]
        for cn in n["connections"]:
            j = cn["id"]; o = cn["orbit"]
            if j not in idx or o == 2147483647: continue
            k = tuple(sorted((nid, j)))
            if k in seen: continue
            seen.add(k); m = N[str(j)]
            x1, y1 = pos(nid); x2, y2 = pos(j); arc = None
            if o == 0 and n["group"] == m["group"] and n["orbit"] == m["orbit"] and n["orbit"] > 0:
                g = GR[n["group"] - 1]; arc = (g["x"], g["y"], C["orbitRadii"][n["orbit"]])
            elif o != 0:
                r = C["orbitRadii"][abs(o)]; dx, dy = x2 - x1, y2 - y1; d = math.hypot(dx, dy)
                if d > 0 and r >= d / 2:
                    h = math.sqrt(r * r - (d / 2) ** 2); mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    px, py = -dy / d, dx / d; s = 1 if o > 0 else -1
                    arc = (mx + s * px * h, my + s * py * h, r)
            if arc:
                cx, cy, r = arc; edges.append([idx[nid], idx[j], round(cx), round(cy), round(r)])
            else:
                edges.append([idx[nid], idx[j]])
    return nodes, edges, meta

main_nodes, main_edges, main_meta = build_graph(lambda n: not n.get("ascendancyName"))
asc_nodes, asc_edges, asc_meta = build_graph(lambda n: n.get("ascendancyName") == ASC)
print("main", len(main_nodes), "asc", len(asc_nodes))

VAR = {v["name"]: v for v in D.V["variants"]}
ORDER = ["a1", "a2", "a3", "a4", "sw", "int", "ea", "w1", "fin"]
alloc, passive_icons = {}, {}
for pid in ORDER:
    t = VAR[D.VMAP[pid]]["tree"]
    alloc[pid] = {"m": t["m"], "s1": t["s1"], "s2": t["s2"], "a": t["a"]}
    for nid in t["m"] + t["s1"] + t["s2"] + t["a"]:
        if str(nid) not in N: continue
        name, stats, ic, kind = info(nid)
        if kind in (1, 2, 3) or N[str(nid)].get("ascendancyName"):
            k = icon(ic, 52)
            if k: passive_icons[nid] = k

notables = {}; prev = set()
for pid in ORDER:
    a = alloc[pid]; cur = set(a["m"] + a["s1"] + a["s2"]); lst = []
    for nid in a["m"] + a["s1"] + a["s2"]:
        if str(nid) not in N: continue
        name, stats, ic, kind = info(nid)
        if kind in (1, 2, 3):
            set_ = "s1" if nid in a["s1"] else "s2" if nid in a["s2"] else "m"
            lst.append({"id": nid, "n": name, "s": stats, "k": kind, "ic": passive_icons.get(nid), "new": nid not in prev, "set": set_, "pass": False})
    removed = [info(x)[0] for x in prev - cur if str(x) in N and info(x)[3] in (1, 2)]
    notables[pid] = {"list": lst, "count": len(a["m"]), "s1": len(a["s1"]), "s2": len(a["s2"]), "removed": removed,
                     "asc": [{"id": x, "n": info(x)[0], "s": info(x)[1], "ic": passive_icons.get(x)} for x in a["a"] if str(x) in N and N[str(x)].get("isNotable")]}
    prev = cur
# todas as notables da ascendência (para a aba Ascendência)
all_asc = []
for k, n in N.items():
    if n.get("ascendancyName") == ASC and n.get("isNotable"):
        nm, st, ic, _ = info(int(k)); kk = icon(ic, 52)
        if kk: passive_icons[int(k)] = kk
        all_asc.append({"id": int(k), "n": nm, "s": st, "ic": kk})
notables["uber"] = dict(notables["fin"]); notables["uber"]["asc"] = all_asc

# ------------------------------------------------------------ gems / supports
gem_icon, sup_icon = {}, {}
for v in D.V["variants"]:
    for g in v["gems"]:
        k = icon(g["icon"], 64)
        if k: gem_icon.setdefault(g["skill"], k)
        for sname, url in g["supIcons"].items():
            nm = {"grimpillarsplayer": "Grim Pillars", "bitterdeadplayer": "Bitter Dead", "sparkplayer": "Spark", "uniqueearthboundtriggeredsparkplayer": "Spark"}.get(sname, sname)
            kk = icon(url, 40)
            if kk: sup_icon.setdefault(nm, kk)
for extra, path in {"Spark": "2DItems/Gems/New/SparkSkillGem", "Grim Pillars": "2DArt/SkillIcons/ExpeditionGrimPillars", "Pierce II": "2DItems/Gems/New/NewSupport/PierceSupportGem"}.items():
    if extra not in sup_icon:
        kk = icon(path, 40)
        if kk: sup_icon[extra] = kk
for g in ("Spark", "Grim Pillars", "Bitter Dead"):
    if g in sup_icon and g not in gem_icon: gem_icon[g] = sup_icon[g]

# ------------------------------------------------------------ itens
SLOT_PT = {"mainHand_set1": "Arma (Set 1)", "offHand_set1": "Offhand (Set 1)", "mainHand_set2": "Arma (Set 2)", "offHand_set2": "Offhand (Set 2)", "helmet": "Capacete", "body": "Body Armour",
           "gloves": "Luvas", "boots": "Botas", "amulet": "Amuleto", "leftRing": "Anel E", "rightRing": "Anel D", "belt": "Cinto", "charm1": "Charm", "charm2": "Charm", "charm3": "Charm",
           "flask1": "Flask vida", "flask2": "Flask mana"}
def hint(slot, name):
    if slot.startswith("Offhand"): return [D.L("Soul Core/runa de resistência que faltar", "Whatever resistance Soul Core/rune you're missing")]
    if slot.startswith("Arma"): return [D.L("Runa de resistência que faltar", "Whatever resistance rune you're missing")]
    if slot in ("Capacete", "Body Armour", "Luvas", "Botas"): return [D.L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio) · resist no cap: Body Rune (vida)", "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning) · resists capped: Body Rune (life)")]
    return []
uniq_icon = {}
def rows(pid_variant):
    out = []
    for slot, it in VAR[pid_variant]["items"].items():
        if not it or not it.get("n") or slot not in SLOT_PT: continue
        sp = SLOT_PT[slot]
        ic = icon(it["icon"], 96)
        if it["u"]: uniq_icon.setdefault(it["n"], ic)
        u = next((x for x in D.UNIQUES if x["n"] == it["n"]), None)
        runes = [r for r in it.get("runes") or [] if r]
        extra = [f"{s['name']}: {s['value']}" for s in it.get("stats") or [] if s.get("name") in ("Spirit", "Energy Shield")]
        mods = [m for m in it["mods"]] + extra
        out.append({"slot": sp, "n": it["n"], "u": it["u"], "ic": ic, "x": " ; ".join(mods[:7]), "r": runes or hint(sp, it["n"]), "rs": 1 if runes else 0,
                    "note": ("Spellslinger" if it["n"] == "Dueling Wand" else ""), "price": (u or {}).get("price")})
    return out
FULLMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a4", "sw": "sw", "int": "ea", "ea": "w1", "w1": "fin", "fin": "fin"}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a4", "sw": "sw", "int": "int", "ea": "ea", "w1": "w1", "fin": "w1"}
guide, sets_out = {}, {}
for pid in ORDER:
    guide[pid] = rows(D.VMAP[pid])
    sets_out[pid] = {"cheap": rows(D.VMAP[CHEAPMAP[pid]]), "full": rows(D.VMAP[FULLMAP[pid]])}
for u in D.UNIQUES:
    k = icon_url(u.get("iconUrl"), "U_" + re.sub(r"[^A-Za-z]", "", u["n"]), 96)
    if k: uniq_icon[u["n"]] = k

# ------------------------------------------------------------ ordem de alocação por nível
adj = {}
for k, n in N.items():
    for c in n.get("connections", []):
        adj.setdefault(int(k), set()).add(c["id"]); adj.setdefault(c["id"], set()).add(int(k))
def important(nid):
    n = N[str(nid)]; return n.get("isNotable") or n.get("isKeystone") or n.get("isJewelSocket")
def grow(have, targets, prefer, out):
    remaining = [t for t in targets if t not in have and str(t) in N]; rem = set(remaining)
    changed = True
    while changed:
        changed = False
        for t in remaining:
            if t in rem and t in prefer and any(v in have for v in adj.get(t, ())):
                have.add(t); rem.discard(t); out.append(t); changed = True
    while rem:
        prevd = {}; dq = deque()
        for h in have:
            for v in adj.get(h, ()):
                if v in rem and v not in prevd: prevd[v] = None; dq.append(v)
        best = None
        while dq:
            u = dq.popleft()
            if important(u): best = u; break
            for v in adj.get(u, ()):
                if v in rem and v not in prevd: prevd[v] = u; dq.append(v)
        if best is not None:
            path = []; x = best
            while x is not None: path.append(x); x = prevd[x]
            for x in reversed(path):
                if x in rem: have.add(x); rem.discard(x); out.append(x)
            continue
        front = [t for t in remaining if t in rem and any(v in have for v in adj.get(t, ()))]
        if not front: break
        t = front[0]; have.add(t); rem.discard(t); out.append(t)
orders = {}; prev_set = set()
for i, pid in enumerate(ORDER):
    P = alloc[pid]["m"]; have = {START}; out = []
    grow(have, P, prev_set, out)
    for nxt in ORDER[i + 1:]:
        grow(have, alloc[nxt]["m"], set(), out)
        if len(out) >= 123: break
    orders[pid] = {"o": out, "n": len(P)}; prev_set = set(P)
    print(pid, "fase", len(P), "ordem", len(out))
orders["uber"] = orders["fin"]; alloc["uber"] = alloc["fin"]
QUEST = [[8, 1], [12, 2], [18, 3], [22, 4], [26, 5], [30, 6], [34, 8], [40, 10], [45, 12], [50, 14], [54, 16], [58, 18], [62, 20], [66, 22], [70, 24]]
kinds = {n[0]: n[3] for n in main_nodes}

A = dict(icons=ICONS, tree=dict(nodes=main_nodes, edges=main_edges, meta={str(k): v for k, v in main_meta.items()}),
         asc=dict(nodes=asc_nodes, edges=asc_edges, meta={str(k): v for k, v in asc_meta.items()}),
         alloc=alloc, notables=notables, passiveIcon={str(k): v for k, v in passive_icons.items()}, gemIcon=gem_icon, metaNotables=[],
         sets=sets_out, supIcon=sup_icon, uniqIcon=uniq_icon, guide=guide, order=orders, quest=QUEST,
         nodeKind={str(k): v for k, v in kinds.items() if v in (1, 2, 3)})
json.dump(A, open(os.path.join(HERE, "assets.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
need_sup = sorted({s for p in D.PHASES for g in p["gems"] for s in g["sup"]} - set(sup_icon))
need_gem = sorted({g["skill"] for p in D.PHASES for g in p["gems"]} - set(gem_icon))
print("icons", len(ICONS), "sups sem ícone:", need_sup, "gems sem ícone:", need_gem, "uniq", len(uniq_icon))
