# -*- coding: utf-8 -*-
"""Leitura mínima dos dados do Path of Building (PoE2) já baixados em tools/dl/pob: gems, descrições, tiers e Spirit."""
import glob, os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
POB = os.path.join(HERE, "..", "dl", "pob")
_cache = {}


def _gems():
    if "gems" in _cache:
        return _cache["gems"]
    s = open(os.path.join(POB, "Gems.lua"), encoding="utf-8").read()
    out = {}
    for m in re.finditer(r'\["(Metadata/Items/Gems?/[^"]+)"\] = \{(.*?)\n\t\},', s, re.S):
        body = m.group(2)
        g = lambda k: (re.search(k + r' = "([^"]*)"', body) or [None, None])[1]
        n = lambda k: int((re.search(k + r' = (\d+)', body) or [None, 0])[1])
        name = g("name")
        if not name:
            continue
        out[name] = dict(name=name, gameId=g("gameId"), variantId=g("variantId"), effect=g("grantedEffectId"), tags=g("tagString") or "",
                         type=g("gemType") or "", weapon=g("weaponRequirements") or "", tier=n("Tier"), str=n("reqStr"), dex=n("reqDex"), int=n("reqInt"),
                         support="Support" in (g("gemType") or "") or "SupportGem" in (g("gameId") or ""))
    _cache["gems"] = out
    return out


def _skills():
    if "skills" in _cache:
        return _cache["skills"]
    out = {}
    for f in glob.glob(os.path.join(POB, "skills_*.lua")):
        s = open(f, encoding="utf-8").read()
        for m in re.finditer(r'skills\["([^"]+)"\] = \{(.*?)\n\}', s, re.S):
            body = m.group(2)
            name = (re.search(r'\n\tname = "([^"]*)"', body) or [None, None])[1]
            desc = (re.search(r'\n\tdescription = "((?:[^"\\]|\\.)*)"', body) or [None, ""])[1]
            lv = {}
            lvb = re.search(r'\n\tlevels = \{(.*?)\n\t\},', body, re.S)
            for lm in re.finditer(r'\[(\d+)\] = \{ ([^\n]*)\},', lvb.group(1) if lvb else ""):
                req = re.search(r'levelRequirement = (\d+)', lm.group(2))
                sp = re.search(r'spiritReservationFlat = (\d+)', lm.group(2))
                lv[int(lm.group(1))] = dict(req=int(req.group(1)) if req else None, spirit=int(sp.group(1)) if sp else None)
            out[m.group(1)] = dict(id=m.group(1), name=name, desc=desc.replace('\\"', '"').replace("\\n", " "), levels=lv)
    _cache["skills"] = out
    return out


def gem(name):
    return _gems().get(name)


def desc(name):
    g = gem(name)
    if g and g["effect"] and g["effect"] in _skills():
        return _skills()[g["effect"]]["desc"]
    for k, v in _skills().items():
        if v["name"] == name and v["desc"]:
            return v["desc"]
    return ""


def slug_names():
    """grantedEffectId/variantId (minúsculo) -> nome, para slugs do Mobalytics como 'arcplayer'."""
    m = {}
    for n, g in _gems().items():
        for k in (g["effect"], g["variantId"]):
            if k:
                m[k.lower()] = n
    return m


if __name__ == "__main__":
    import sys
    for n in sys.argv[1:]:
        print(n, json.dumps(gem(n), ensure_ascii=False), "|", desc(n))
