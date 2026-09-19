# -*- coding: utf-8 -*-
"""Converte um código do Path of Building (PoE2) — o texto de https://poe.ninja/poe2/pob/raw/<id> — no formato de variantes do kit.

A árvore vem do PoB; os cortes por pontos viram as fases (a ordem de alocação é calculada a partir do início da classe, igual ao kit/ninja.py).
Os itens de cada fase são declarados aqui (nome do unique + base) e completados com os mods do poe.ninja (dl/eco_*.json); o último corte usa os itens reais do PoB.

Uso: python pobxml.py <bid> <arquivo-com-o-codigo-pob> [Nome|pontos ...]   (o último corte, sem pontos, é o build inteiro)
"""
import base64, json, os, re, sys, zlib
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
import common  # noqa: E402
import ninja   # noqa: E402  (grow_order, NODES, arte dos itens)

SLOTS = {"Weapon 1": "mainHand_set1", "Weapon 2": "offHand_set1", "Weapon 1 Swap": "mainHand_set2", "Weapon 2 Swap": "offHand_set2", "Helmet": "helmet", "Body Armour": "body",
         "Gloves": "gloves", "Boots": "boots", "Amulet": "amulet", "Ring 1": "leftRing", "Ring 2": "rightRing", "Belt": "belt", "Charm 1": "charm1", "Charm 2": "charm2",
         "Charm 3": "charm3", "Flask 1": "flask1", "Flask 2": "flask2"}
TAG = re.compile(r"\{[^}]*\}")


def decode(code):
    raw = code.strip().replace("-", "+").replace("_", "/")
    raw += "=" * (-len(raw) % 4)
    return ET.fromstring(zlib.decompress(base64.b64decode(raw)).decode("utf-8"))


def parse_item(text):
    """Um <Item> do PoB → dict do kit (n, u, icon, mods, stats, runes)."""
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    rar = lines[0].split(":", 1)[1].strip().upper()
    name = lines[1]
    base = lines[2] if rar in ("UNIQUE", "RARE") and not re.match(r"^[A-Za-z' ]+:", lines[2]) else None
    if base is None:  # mágico: a base está dentro do nome
        base = next((b for b in sorted({x.get("name") for x in ninja.BASES.values() if x.get("name")}, key=len, reverse=True) if b in name), name)
    stats, runes, mods, i = [], [], [], 3 if rar in ("UNIQUE", "RARE") else 2
    skip = ("Unique ID", "Item Level", "LevelReq", "Limited to", "Quality", "Sockets", "Rune", "Implicits", "Charm Slots", "Requires", "Rarity", "Corrupted", "Twice Corrupted")
    for l in lines[i:]:
        if re.match(r"^(Energy Shield|Ward|Evasion|Armour|Spirit): ", l):
            k, v = l.split(":", 1); stats.append({"name": k.strip(), "value": v.strip()}); continue
        if l.startswith("Rune:"):
            runes.append(l.split(":", 1)[1].strip()); continue
        if any(l.startswith(s) for s in skip):
            continue
        if "{rune}" in l:  # linhas que vêm da runa entram em "runes", não em "mods"
            continue
        m = TAG.sub("", l).strip()
        if m and not m.startswith("Bonded"):
            mods.append(m)
    uniq = rar == "UNIQUE"
    icon = (ninja.UNIQ_ART.get(name) if uniq else None) or ninja.ART_BY_BASE.get(base)
    return {"n": name if (uniq or rar == "RARE") else base, "u": 1 if uniq else 0, "icon": icon, "mods": mods[:8], "stats": stats, "runes": runes, "skill": None}


def eco_item(name, base=None):
    """Item de fase vindo do poe.ninja (unique com preço/mods conhecidos) — sem runas, com a base pedida."""
    e = common.ECO.get(name, {})
    b = base or e.get("base") or ""
    return {"n": name, "u": 1, "icon": ninja.UNIQ_ART.get(name) or ninja.ART_BY_BASE.get(b), "mods": e.get("mods", [])[:8], "stats": [], "runes": [], "skill": None}


def gems(root):
    out, seen = [], {}
    for g in root.find("Skills").iter("Skill"):
        gl = [(x.get("nameSpec"), x.get("enabled") != "false") for x in g.findall("Gem")]
        gl = [n for n, on in gl if on and n]
        if not gl:
            continue
        slot = g.get("slot") or ""
        ws = 2 if "Swap" in slot else None
        skill, sup = gl[0], gl[1:]
        if skill in seen and len(sup) <= len(seen[skill]["sup"]):
            continue
        d = {"skill": skill, "slug": re.sub(r"[^a-z]", "", skill.lower()), "icon": None, "skillIcon": None, "sup": sup, "supIcons": {}, "weaponSet": ws}
        if skill in seen:
            out[out.index(seen[skill])] = d
        else:
            out.append(d)
        seen[skill] = d
    return out


def items(root):
    res = {}
    by_id = {x.get("id"): x for x in root.find("Items").findall("Item")}
    active = root.find("Items").find("ItemSet")
    for s in active.findall("Slot"):
        slot, iid = SLOTS.get(s.get("name")), s.get("itemId")
        if slot and iid and iid != "0" and iid in by_id:
            res[slot] = parse_item(by_id[iid].text)
    return res


def walk_order(root, priority):
    """Ordem de alocação que a classe REALMENTE consegue seguir: do início da classe até a região do build pelo caminho mais curto e, dali, notable por notable
    na ordem de `priority` (sempre pelo menor caminho dentro dos nós do build). Nós que só se alcançam por outro ponto inicial (ex.: joia Split Personality)
    ficam de fora e voltam em `resto`."""
    from collections import deque
    N, ADJ = ninja.NODES, ninja.ADJ
    sp = root.find("Tree").findall("Spec")[0]
    start = ninja.CLASS_START[root.find("Build").get("className")]
    S = {n for n in (int(x) for x in sp.get("nodes").split(",") if x) if not N[str(n)].get("ascendancyName")} - {start}
    prev, dq, hit = {start: None}, deque([start]), None
    while dq:
        u = dq.popleft()
        if u in S:
            hit = u; break
        for v in ADJ.get(u, ()):
            d = N.get(str(v))
            if d is None or v in prev or d.get("ascendancyName"):
                continue
            prev[v] = u; dq.append(v)
    conector = []
    x = hit
    while x is not None:
        conector.append(x); x = prev[x]
    conector = list(reversed(conector))[1:]
    allowed = S | set(conector) | {start}
    have, order = {start}, []

    def add(p):
        for n in p:
            if n not in have:
                have.add(n); order.append(n)

    def path_to(target):
        pv, q = {h: None for h in have}, deque(have)
        while q:
            u = q.popleft()
            if u == target:
                out, y = [], u
                while y is not None:
                    out.append(y); y = pv[y]
                return list(reversed(out))
            for v in ADJ.get(u, ()):
                if v in pv or v not in allowed:
                    continue
                pv[v] = u; q.append(v)
        return []
    add(conector)
    byname = {N[str(n)]["name"]: n for n in S if N[str(n)].get("isNotable")}
    for nome in priority:
        if nome in byname and byname[nome] not in have:
            add(path_to(byname[nome]))
    resto = [n for n in S if n not in have]
    return order, sorted(resto)


def walk_nodes(nodes, start, priority):
    """Ordem de alocação de uma lista de nós que JÁ é alcançável a partir de `start`: notable por notable na ordem de `priority`
    (sempre pelo menor caminho dentro de `nodes`); o resto entra no fim pela vizinhança."""
    from collections import deque
    N, ADJ = ninja.NODES, ninja.ADJ
    allowed = set(nodes) | {start}
    have, order = {start}, []
    byname = {}
    for n in nodes:
        d = N[str(n)]
        if d.get("isNotable") or d.get("isKeystone"):
            byname[d["name"]] = n

    def path_to(target):
        pv, q = {h: None for h in have}, deque(have)
        while q:
            u = q.popleft()
            if u == target:
                out, y = [], u
                while y is not None:
                    out.append(y); y = pv[y]
                return list(reversed(out))
            for v in ADJ.get(u, ()):
                if v in pv or v not in allowed:
                    continue
                pv[v] = u; q.append(v)
        return []
    for nome in priority:
        if nome in byname and byname[nome] not in have:
            for n in path_to(byname[nome]):
                if n not in have:
                    have.add(n); order.append(n)
    rest = [n for n in nodes if n not in have]
    changed = True
    while rest and changed:
        changed = False
        for n in list(rest):
            if ADJ.get(n, set()) & have:
                have.add(n); order.append(n); rest.remove(n); changed = True
    return order + rest


def order_set(setnodes, main_nodes, start):
    """Ordem dos nós de Weapon Set: sempre vizinhos do que já está alocado (árvore principal + set)."""
    have = {start} | set(main_nodes); out = []; rem = [n for n in setnodes if n not in have]; ch = True
    while rem and ch:
        ch = False
        for n in list(rem):
            if ninja.ADJ.get(n, set()) & have:
                have.add(n); out.append(n); rem.remove(n); ch = True
    return out + rem


def tree(root, limit=None, order=None):
    sp = root.find("Tree").findall("Spec")[0]
    todos = [int(x) for x in sp.get("nodes").split(",") if x]
    asc = [n for n in todos if ninja.NODES.get(str(n), {}).get("ascendancyName")]
    main = [n for n in todos if not ninja.NODES.get(str(n), {}).get("ascendancyName")]
    ordem = order if order is not None else ninja.grow_order(main, ninja.CLASS_START[root.find("Build").get("className")])
    m = ordem[:limit] if limit else ordem
    return {"m": m, "s1": [], "s2": [], "a": asc, "attr": None, "jewels": {}}


def main():
    bid, arq = sys.argv[1], sys.argv[2]
    cortes = [a for a in sys.argv[3:] if "|" in a]
    root = decode(open(arq, encoding="utf-8").read())
    b = root.find("Build")
    level = int(b.get("level"))
    G = gems(root)
    full_items = items(root)
    variants = []
    for c in cortes:
        nome, pts = c.split("|")
        variants.append(variant(root, nome, int(pts) if pts else None, full_items, G))
    write(bid, root, variants)


def variant(root, nome, pontos, its, G=None, order=None):
    """Uma fase: árvore cortada em `pontos` (na ordem `order`, se dada), com os itens `its` (dict de slots do kit)."""
    return {"src": "pob", "name": nome, "items": its, "gems": G if G is not None else gems(root), "level": int(root.find("Build").get("level")),
            "tree": tree(root, pontos, order), "desc": ""}


def write(bid, root, variants, url=""):
    b = root.find("Build")
    meta = [{"src": "pob", "title": f"{b.get('ascendClassName')} {b.get('level')} — poe.ninja PoB", "url": url or os.environ.get("POB_URL", ""), "author": "poe.ninja",
             "updatedAt": None, "widgets": [], "notes": None, "profileNotes": {}, "rotations": {}}]
    json.dump({"guides": meta, "variants": variants}, open(os.path.join(ROOT, "dl", f"{bid}_variants.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for v in variants:
        print(f"- {v['name']}: árvore {len(v['tree']['m'])} | asc {len(v['tree']['a'])} | gems {len(v['gems'])} | itens {len(v['items'])}")


if __name__ == "__main__":
    main()
