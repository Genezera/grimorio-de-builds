# -*- coding: utf-8 -*-
"""Joias da árvore de passivas: em qual jewel socket cada joia vai, o que procurar e a partir de qual fase o socket está alocado.

Duas fontes, mesmo formato de saída {node, n, u, base, mods, note}:
  · PoB (poe.ninja): <Sockets> do <Spec> + o <Item> de cada socket  → from_pob(root)
  · Mobalytics: tree.jewels = [{nodeSlug, jewelSlug, isUnique, prefixSlugs, suffixSlugs, iconURL}]  → from_mobalytics(lista)
kassets.py chama collect() e grava A.jewels; o app mostra o painel "Joias" na aba Árvore e um anel dourado no socket."""
import re
from collections import deque

TAG = re.compile(r"\{[^}]*\}")


def _clean(l):
    return TAG.sub("", l).strip()


def from_pob(root):
    sp = root.find("Tree").findall("Spec")[0]
    sk = sp.find("Sockets")
    if sk is None:
        return []
    items = {x.get("id"): x for x in root.find("Items").findall("Item")}
    out = []
    for s in sk.findall("Socket"):
        it = items.get(s.get("itemId"))
        if it is None or s.get("itemId") == "0":
            continue
        lines = [l.strip() for l in it.text.strip().split("\n") if l.strip()]
        rar = lines[0].split(":", 1)[1].strip().upper()
        name, base = lines[1], (lines[2] if len(lines) > 2 else "")
        mods, radius, corrupted = [], None, False
        for l in lines[3:]:
            if re.match(r"^(Unique ID|Item Level|LevelReq|Limited to|Implicits|Quality|Sockets):", l):
                continue
            if l.startswith("Radius:"):
                radius = l.split(":", 1)[1].strip(); continue
            if l in ("Corrupted", "Twice Corrupted"):
                corrupted = True; continue
            if l.startswith("Rune:"):
                continue
            m = _clean(l)
            if m and not m.startswith("Bonded"):
                mods.append(m)
        out.append({"node": int(s.get("nodeId")), "n": name, "u": rar == "UNIQUE", "base": base, "mods": mods[:6], "radius": radius, "corrupted": corrupted, "note": ""})
    return out


def _hum(slug):
    s = re.sub(r"^(Crafted|Jewel|Attack|Radius)+(?=[A-Z])", lambda m: m.group(0) if m.group(0) == "Attack" else "", slug)
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", s)
    return re.sub(r"\s+\d+$", "", s).strip()


def from_mobalytics(lst):
    out = []
    for j in lst:
        m = re.search(r"node-(\d+)", j.get("nodeSlug", ""))
        if not m:
            continue
        slug = j.get("jewelSlug", "")
        if j.get("isUnique"):
            name = re.sub(r"^jewel-(?:[a-z]*unique[a-z]*\d*-+)", "", slug).replace("-", " ").title().replace("'S", "'s")
            name = re.sub(r"\b(Of|The|And)\b", lambda m: m.group(0).lower(), name)
            mods = []
        else:
            icon = j.get("iconURL", "")
            kind = next((k for k in ("Emerald", "Ruby", "Sapphire", "Diamond", "Amethyst") if k in icon), "")
            radius = "radius" in slug
            name = ("Time-Lost " + (kind or "jewel")) if radius else (f"Rare {kind} Jewel" if kind else "Rare Jewel")
            mods = [_hum(x) for x in (j.get("prefixSlugs") or [])] + [_hum(x) for x in (j.get("suffixSlugs") or [])]
        out.append({"node": int(m.group(1)), "n": name, "u": bool(j.get("isUnique")), "base": "", "mods": mods, "radius": None, "corrupted": False,
                    "note": "prefixos e sufixos que o guia procura" if mods else "", "trade": (j.get("poe2TradeRequest") or {}).get("query")})
    return out


def normalize(raw):
    """Lista do JSON de variantes (qualquer formato) → lista normalizada; {} / None → []."""
    if not raw or isinstance(raw, dict):
        return []
    if "nodeSlug" in raw[0]:
        return from_mobalytics(raw)
    return [dict(r) for r in raw]


def collect(VAR, D, alloc, ORDER, N, adj):
    """Devolve as joias da build com: soquete, joia, vizinhança (notable mais próximo) e a primeira fase em que o socket está alocado."""
    best = []
    for pid in reversed(ORDER):                          # a variante mais completa que tiver joias
        best = normalize(VAR[D.VMAP[pid]]["tree"].get("jewels"))
        if best:
            break
    out = []
    for j in best:
        nid = j["node"]
        if str(nid) not in N:
            continue
        first = next((pid for pid in ORDER if nid in alloc[pid]["m"] or nid in alloc[pid]["s1"] or nid in alloc[pid]["s2"]), None)
        where = "s1" if first and nid in alloc[first]["s1"] else "s2" if first and nid in alloc[first]["s2"] else "m"
        near, seen, dq = None, {nid}, deque([(nid, 0)])
        while dq and near is None:                      # notable/keystone mais perto (até 8 passos), ignorando Attribute
            u, d = dq.popleft()
            if d > 8:
                break
            for w in adj.get(u, ()):
                if w in seen:
                    continue
                seen.add(w)
                nn = N.get(str(w), {})
                if (nn.get("isNotable") or nn.get("isKeystone")) and not nn.get("ascendancyName"):
                    near = nn.get("name"); break
                dq.append((w, d + 1))
        out.append(dict(j, first=first, where=where, near=near))
    out.sort(key=lambda x: (x["first"] is None, ORDER.index(x["first"]) if x["first"] else 99))
    return out
