# -*- coding: utf-8 -*-
"""Lê ModItem.lua (Path of Building PoE2) e responde: quais mods/tiers existem para um conjunto de tags de base."""
import re, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "dl", "pob", "ModItem.lua")

def _parse():
    out = []
    for line in open(SRC, encoding="utf-8"):
        m = re.match(r'\s*\["([^"]+)"\] = \{ (.*) \},?\s*$', line)
        if not m:
            continue
        name, body = m.groups()
        typ = re.search(r'type = "(\w+)"', body)
        affix = re.search(r'affix = "([^"]*)"', body)
        lvl = re.search(r'level = (\d+)', body)
        grp = re.search(r'group = "([^"]*)"', body)
        head = body.split("statOrder")[0]
        head = re.sub(r'^.*?affix = "[^"]*",', "", head) if "affix =" in head else head
        texts = re.findall(r'"([^"]*)"', head)
        wk = re.search(r'weightKey = \{ ([^}]*)\}', body)
        wv = re.search(r'weightVal = \{ ([^}]*)\}', body)
        keys = re.findall(r'"([^"]+)"', wk.group(1)) if wk else []
        vals = [int(x) for x in re.findall(r'-?\d+', wv.group(1))] if wv else []
        tags = re.search(r'modTags = \{ ([^}]*)\}', body)
        out.append(dict(id=name, type=typ.group(1) if typ else "", affix=affix.group(1) if affix else "",
                        text=texts, level=int(lvl.group(1)) if lvl else 0, group=grp.group(1) if grp else "",
                        weights=list(zip(keys, vals)), tags=re.findall(r'"([^"]+)"', tags.group(1)) if tags else []))
    return out

MODS = _parse()

def spawns(mod, base_tags):
    """Primeira chave do weightKey que casa com as tags da base decide (regra do PoE)."""
    for k, v in mod["weights"]:
        if k in base_tags:
            return v > 0
    return False

def pool(base_tags):
    return [m for m in MODS if m["type"] in ("Prefix", "Suffix") and spawns(m, base_tags)]

def tiers(base_tags, pattern):
    """Tiers (T1 = maior) dos mods cujo texto casa com pattern."""
    rx = re.compile(pattern, re.I)
    groups = {}
    for m in pool(base_tags):
        if any(rx.search(t) for t in m["text"]):
            groups.setdefault((m["group"], m["type"], " / ".join(re.sub(r"\(\d+(\.\d+)?-\d+(\.\d+)?\)", "#", t) for t in m["text"])), []).append(m)
    res = []
    for (g, typ, label), ms in groups.items():
        ms.sort(key=lambda m: -m["level"])
        res.append(dict(group=g, type=typ, label=label,
                        tiers=[dict(t=i + 1, ilvl=m["level"], text=" / ".join(m["text"]), affix=m["affix"]) for i, m in enumerate(ms)]))
    return res

if __name__ == "__main__":
    import sys
    tags = sys.argv[1].split(",")
    pat = sys.argv[2] if len(sys.argv) > 2 else "."
    for r in tiers(tags, pat):
        print(f"[{r['type']}] {r['label']}  ({r['group']})")
        for t in r["tiers"][:4]:
            print(f"   T{t['t']} ilvl{t['ilvl']:>3} {t['text']}")
