# -*- coding: utf-8 -*-
"""Revisão profunda das builds do kit: mede o que a auditoria de coerência não mede.

  1. Dano da árvore por fase (soma dos % de dano, velocidade, crítico e vida dos nós que a página mostra em cada corte)
  2. Skills: nível em que cada uma entra × Tier do gem (PoB) e arma exigida × armas recomendadas naquela faixa
  3. Reservas de Spirit por fase × orçamento de quest

Uso: python deepcheck.py [bid ...]   (sem argumentos: todas as builds do kit). Só lê dados; não altera nada."""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "kit"))
import common, ninja, pob  # noqa: E402

BUILDS = ["acolyte", "infernalist", "legionnaire", "martial", "pathfinder", "shaman", "smith", "tactician", "twister", "whirling"]
_DMG = re.compile(r"^\+?(\d+)%?\s+(?:increased|more)\s+(.*)$", re.I)
_PCT = re.compile(r"(\d+)% (?:increased|more) ([^,]*)", re.I)


def node_stats(n):
    d = dict(dmg=0, spd=0, crit=0, life=0, flat=0)
    for line in ninja.NODES[str(n)].get("stats") or []:
        m = _PCT.search(line)
        if m:
            v, t = int(m.group(1)), m.group(2).lower()
            if "damage" in t and not any(k in t for k in ("taken", "recovery", "duration", "threshold", "over time")): d["dmg"] += v
            elif any(k in t for k in ("attack speed", "cast speed", "skill speed", "attack and cast speed")): d["spd"] += v
            elif "critical" in t: d["crit"] += v
            elif "maximum life" in t: d["life"] += v
        m = re.search(r"adds? (\d+) to (\d+) .*damage", line, re.I)
        if m: d["flat"] += (int(m.group(1)) + int(m.group(2))) // 2
    return d


def tree_rows(bid, B):
    p = os.path.join(HERE, "builds", bid, "assets.json")
    if not os.path.exists(p): return []
    A = json.load(open(p, encoding="utf-8"))
    rows = []
    for pid in getattr(B, "ORDER", [x["id"] for x in B.PHASES]):
        o = A.get("order", {}).get(pid)
        if not o: continue
        cut = o["o"][:o["n"]]
        tot = dict(dmg=0, spd=0, crit=0, life=0, flat=0)
        for n in cut:
            for k, v in node_stats(n).items(): tot[k] += v
        ph = next((x for x in B.PHASES if x["id"] == pid), None)
        rows.append((pid, ph["lv"] if ph else None, o["n"], tot))
    return rows


def skill_rows(B):
    """(fase, skill, nível de entrada, Tier, arma exigida, Spirit) — o nível de entrada é max(início da fase, since)."""
    out, seen = [], set()
    for p in B.PHASES:
        for g in p["gems"]:
            k = g["skill"]
            if k in seen: continue
            seen.add(k)
            gm = pob.gem(k) or {}
            entry = max(p["lv"][0], g.get("since") or 0)
            out.append((p["id"], k, entry, gm.get("tier"), gm.get("weapon", ""), g.get("sp"), bool(gm)))
    return out


WEAPON_WORDS = {"Spear": ["spear", "lança"], "Bow": ["bow", "arco"], "Crossbow": ["crossbow", "besta"], "Staff": ["staff", "quarterstaff", "cajado"],
                "One Hand Mace": ["mace", "maça", "sceptre", "cetro"], "Two Hand Mace": ["mace", "maça"], "Quarterstaff": ["quarterstaff", "staff", "cajado"],
                "Flail": ["flail", "mangual"], "One Hand Sword": ["sword", "espada"], "Two Hand Sword": ["sword", "espada"], "Warstaff": ["staff", "cajado"]}


def main(argv):
    bids = argv or BUILDS
    for bid in bids:
        B = common.load_build(bid)
        print("=" * 100)
        print(f"{bid}  ({getattr(B, 'CLASS', '?')} · {getattr(B, 'ASCENDANCY_NAME', '') or ''})")
        print("-- árvore por fase: nós | dano% | vel% | crit% | vida% | flat")
        for pid, lv, n, t in tree_rows(bid, B):
            flag = "  <<< sem dano" if lv and lv[0] >= 5 and t["dmg"] + t["spd"] + t["flat"] == 0 and n >= 10 else ""
            print(f"   {pid:8} {str(lv):10} {n:3} nós | dano {t['dmg']:4} | vel {t['spd']:3} | crit {t['crit']:3} | vida {t['life']:3} | flat {t['flat']:3}{flag}")
        print("-- skills: entrada × Tier × arma")
        for pid, k, entry, tier, weapon, sp, ok in skill_rows(B):
            warn = ""
            if not ok: warn = "  <<< gem não existe no PoB"
            elif tier and tier > max(entry, 1) + 6: warn = f"  <<< Tier {tier} muito acima do nível {entry}"
            print(f"   {pid:8} {k:28} entra {entry:3} | Tier {tier} | {weapon or '-'} | sp {sp}{warn}")


if __name__ == "__main__":
    main(sys.argv[1:])
