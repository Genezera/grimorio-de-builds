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
import ninja   # noqa: E402
import jewels as _jw  # noqa: E402  (grow_order, NODES, arte dos itens)

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
    return {"m": m, "s1": [], "s2": [], "a": asc, "attr": None, "jewels": _jw.from_pob(root)}


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


_STAT = re.compile(r"(\d+)% (?:increased|more) ([^;]*)", re.I)
_LIFE = re.compile(r"\+(\d+) to maximum Life", re.I)


def node_score(n):
    """Valor de um nó para quem está subindo de nível: dano, velocidade, crítico e vida (números do próprio nó). Atributos e nós vazios valem 0."""
    s = 0.0
    for line in ninja.NODES[str(n)].get("stats") or []:
        m = _STAT.match(line)
        if m:
            v, t = int(m.group(1)), m.group(2).lower()
            if "damage" in t and not any(k in t for k in ("taken", "recovery", "duration", "threshold")): s += v
            elif any(k in t for k in ("attack speed", "cast speed", "skill speed")): s += 1.5 * v
            elif "projectile speed" in t or "movement speed" in t: s += .5 * v
            elif "critical" in t: s += .7 * v
            elif "maximum life" in t: s += 3 * v
            continue
        m = _LIFE.match(line)
        if m: s += int(m.group(1)) / 8
    return s


def walk_greedy(nodes, start, score=node_score):
    """Ordem de alocação 'dano primeiro': a cada passo pega o alvo com maior (valor do caminho até ele) / (nº de pontos gastos), sempre conectado ao que já está alocado.
    Nós que não ligam ao início entram no fim, na ordem dada."""
    from collections import deque
    ADJ = ninja.ADJ
    allowed = set(nodes) | {start}; have, order = {start}, []
    sc = {n: score(n) for n in allowed}
    remaining = [n for n in nodes if n != start]
    while remaining:
        prev, dq = {h: None for h in have}, deque(have)
        while dq:
            u = dq.popleft()
            for v in ADJ.get(u, ()):
                if v in allowed and v not in prev:
                    prev[v] = u; dq.append(v)
        best, best_key = None, None
        for t in remaining:
            if t not in prev: continue
            path, x = [], t
            while x not in have:
                path.append(x); x = prev[x]
            key = (sum(sc[y] for y in path) / len(path), -len(path))
            if best_key is None or key > best_key: best, best_key = list(reversed(path)), key
        if best is None: break
        for x in best:
            have.add(x); order.append(x)
        remaining = [n for n in remaining if n not in have]
    return order + remaining


def walk_greedy_root(root):
    """Como walk_order (parte do início da classe pelo caminho da árvore do PoB), mas com a ordem 'dano primeiro'. Devolve (ordem, nós que exigem outro ponto de partida)."""
    conector, resto = walk_order(root, [])
    start = ninja.CLASS_START[root.find("Build").get("className")]
    order = walk_greedy(conector + resto, start)
    conn = set(walk_greedy_reach(order, start))
    return [n for n in order if n in conn], [n for n in order if n not in conn]


def walk_greedy_reach(order, start):
    have, changed, rest = {start}, True, list(order)
    while changed:
        changed = False
        for n in list(rest):
            if ninja.ADJ.get(n, set()) & have:
                have.add(n); rest.remove(n); changed = True
    return have - {start}


def staged_greedy(nodes, start, score, cuts, must=None, ban=None):
    """Ordem 'dano primeiro' em ESTÁGIOS que fecham exatamente nos cortes da fase (ex.: 17/34/50/72/95).
    - `must[i]`: nomes de nós que precisam estar alocados até o corte i (a fase que os libera); o caminho até eles entra primeiro.
    - `ban[i]`: nomes que ficam de fora até o corte i (keystones que só fazem sentido depois).
    - Cada passo escolhe o alvo com maior (valor do caminho)/(pontos gastos) que caiba nos pontos que faltam para o corte; tudo conectado ao que já está alocado.
    Devolve (ordem conectada, nós que não ligam ao início — vão para o fim)."""
    from collections import deque
    ADJ = ninja.ADJ
    must, ban = must or {}, ban or {}
    allowed = set(nodes) | {start}
    sc = {n: score(n) for n in allowed}
    by_name = {}
    for n in allowed:
        by_name.setdefault(ninja.NODES[str(n)].get("name"), []).append(n)
    have, order = {start}, []

    def paths(banned):
        prev, dq = {h: None for h in have}, deque(have)
        while dq:
            u = dq.popleft()
            for v in ADJ.get(u, ()):
                if v in allowed and v not in prev and ninja.NODES[str(v)].get("name") not in banned:
                    prev[v] = u; dq.append(v)
        return prev

    def path_to(prev, t):
        p, x = [], t
        while x not in have:
            p.append(x); x = prev[x]
        return list(reversed(p))

    for i, cut in enumerate(cuts):
        banned = {nm for j, names in ban.items() if j >= i for nm in names}
        for nm in must.get(i, ()):
            for t in by_name.get(nm, ()):
                if t in have: continue
                prev = paths(banned - {nm})
                if t not in prev: continue
                p = path_to(prev, t)
                if len(order) + len(p) <= cut:
                    for x in p: have.add(x); order.append(x)
        while len(order) < cut:
            prev = paths(banned)
            best, best_key = None, None
            for t in allowed:
                if t in have or t not in prev: continue
                p = path_to(prev, t)
                if len(order) + len(p) > cut: continue
                key = (sum(sc[y] for y in p) / len(p), -len(p))
                if best_key is None or key > best_key: best, best_key = p, key
            if best is None: break
            for x in best: have.add(x); order.append(x)
    prev = paths(set())                                                   # o que sobrar: tudo que ainda liga, o resto vai para o fim
    while True:
        rest = [n for n in nodes if n not in have and n != start and n in prev]
        if not rest: break
        t = max(rest, key=lambda n: sc[n])
        for x in path_to(prev, t): have.add(x); order.append(x)
        prev = paths(set())
    return order, [n for n in nodes if n not in have and n != start]
