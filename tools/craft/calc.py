# -*- coding: utf-8 -*-
"""Conditional weight models and cached prices, not verified in-game probabilities.

Only models adding ONE modifier to the supplied state. Does not simulate the
removal phase of Chaos, catalysts, base-specific exceptions or a complete craft.
"""
import json, os, re, math
try:
    from . import db
except ImportError:
    import db

HERE = os.path.dirname(os.path.abspath(__file__))
DL = os.path.join(HERE, "..", "dl")

# ---------------------------------------------------------------- preços
PRICE = {}
for t in ["Currency", "Essences", "Abyss", "Omens", "Ritual", "Breach", "Runes"]:
    p = os.path.join(DL, "ex_%s.json" % t)
    if not os.path.exists(p):
        continue
    d = json.load(open(p, encoding="utf-8"))
    if d.get('core', {}).get('primary') != 'divine':
        continue
    names = {i["id"]: i["name"] for i in d.get("items", []) + d.get('core', {}).get('items', [])}
    for l in d.get("lines", []):
        if l["id"] in names:
            PRICE[names[l["id"]]] = l["primaryValue"]
EX_PER_DIV = 1 / PRICE["Exalted Orb"] if PRICE.get("Exalted Orb") else None

def price(name):
    return PRICE.get(name)

# ---------------------------------------------------------------- pool
MIN_LVL = {"normal": 0, "greater": 35, "perfect": 50, "gtrans": 44, "ptrans": 70}

def _pool(page, ilvl, minlvl=0):
    ms = [m for m in db.pool(page, [], "normal") if minlvl <= m["level"] <= ilvl and m["weight"] > 0]
    return ms

def chance(page, ilvl, target, side=None, orb="normal", taken=(), sides_open=("Prefix", "Suffix"), *, assume_published_weights=False):
    """Probabilidade de o próximo mod adicionado casar com `target` (regex no texto e nível mínimo opcional).
    target = (regex, min_level)  |  side = 'Prefix'/'Suffix' se um omen força o lado  |  taken = famílias já no item."""
    rx, minlv = target if isinstance(target, tuple) else (target, 0)
    rx = re.compile(rx, re.I)
    if not isinstance(ilvl, int) or not 1 <= ilvl <= 100:
        raise ValueError('ilvl must be an integer from 1 to 100')
    if side is not None and side not in ('Prefix', 'Suffix'):
        raise ValueError('Unknown affix side')
    if side and side not in sides_open:
        return 0.0
    sides = [side] if side else list(sides_open)
    pool = [m for m in _pool(page, ilvl, MIN_LVL[orb]) if m["gen"] in sides and not set(m.get('families') or [m['family']]).intersection(taken)]
    if any(m['weight'] == 1 for m in pool) and not assume_published_weights:
        raise ValueError('Pool contains weight-1 entries of unverified meaning; explicitly opt into a hypothetical published-weight model')
    tot = sum(m["weight"] for m in pool)
    hit = sum(m["weight"] for m in pool if rx.search(m["text"]) and m["level"] >= minlv)
    return hit / tot if tot else 0.0

def tries(p):
    if not 0 <= p <= 1:
        raise ValueError('Probability must be in [0, 1]')
    return math.inf if p <= 0 else 1 / p

def desecrate(n_options_pool, echoes=False, *, assume_uniform=False):
    """Hypothetical uniform, unique 3-option sampling. NOT a verified reveal model."""
    if not assume_uniform:
        raise ValueError('Desecration sampling is unverified; explicitly opt into the uniform model')
    if not isinstance(n_options_pool, int) or n_options_pool < 1:
        raise ValueError('Pool size must be a positive integer')
    if n_options_pool <= 3:
        return 1.0
    miss = math.comb(n_options_pool - 1, 3) / math.comb(n_options_pool, 3)
    return 1 - miss ** (2 if echoes else 1)

def desecrated_count(page, side, lich=None):
    ms = [m for m in db.pool(page, [], "desecrated") if m["gen"] == side]
    if lich:
        ms = [m for m in ms if lich.lower() in m["name"].lower()]
    return len(ms)

def fmt_pct(p):
    if p >= .1:
        return "%d%%" % round(p * 100)
    if p >= .01:
        return "%.1f%%" % (p * 100)
    return "%.2f%%" % (p * 100)

def est(p, per_try_div):
    """Texto curto: chance, tentativas médias e custo médio em div."""
    t = tries(p)
    cost = t * per_try_div if per_try_div is not None and t != math.inf else None
    return dict(p=fmt_pct(p), tries=("~%d" % round(t)) if t != math.inf else "∞", div=(round(cost, 2) if cost is not None else None))

if __name__ == "__main__":
    for n in ["Chaos Orb", "Exalted Orb", "Perfect Exalted Orb", "Orb of Annulment", "Fracturing Orb", "Omen of Light", "Preserved Collarbone", "Essence of Hysteria", "Neural Catalyst"]:
        print(n, PRICE.get(n))
    print('Cached prices only; source payloads lack original league and collection timestamp.')
    print('Use chance() for an explicit conditional model; no verified Chaos or Desecration odds are published here.')
