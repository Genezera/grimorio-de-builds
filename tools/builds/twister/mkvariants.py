# -*- coding: utf-8 -*-
"""Gera dl/twister_variants.json: Spear Throw Twister Gemling Legionnaire (Maxroll PoB 834d3y0q, nível 100, dl/twister_pob.txt).

O PoB é só o ENDGAME: não há guia nem leveling do autor. O plano de leveling deste guia é uma ADAPTAÇÃO:
  · as fases A1–Mapas são cortes (17/34/50/72/95 pontos) da árvore do PoB numa ordem 'dano primeiro' (pobxml.walk_greedy) a partir do início da Mercenary;
  · as skills do endgame (Twister + Whirling Slash na spear) entram no nível 1;
  · os itens de cada fase seguem o ranking de opções por nível (gear_opts.py) e os uniques do PoB quando o nível deixa.
Uso: python mkvariants.py"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(ROOT, "kit"))
import pobxml, ninja, jewels  # noqa: E402

URL = "https://maxroll.gg/poe2/pob/834d3y0q"
root = pobxml.decode(open(os.path.join(ROOT, "dl", "twister_pob.txt"), encoding="utf-8").read().strip())
E = pobxml.eco_item
START = ninja.CLASS_START["Mercenary"]


def rare(base, mods=(), runes=(), stats=()):
    return {"n": base, "u": 0, "icon": ninja.ART_BY_BASE.get(base), "mods": list(mods), "stats": list(stats), "runes": list(runes), "skill": None}


def uniq(name, base, runes=()):
    d = E(name, base); d["runes"] = list(runes); return d


# ---------------------------------------------------------------- árvore: 'dano primeiro' com o que vale para um ataque de spear
_SKIP = ("spell", "chaos", "low life", "no life", "heavy stunned", "dazed", "flask", "charm", "mana",              # condições e armas que esta build não usa (a spear é de UMA mão)
         "two handed", "crossbow", " bow", "quarterstaff", "sceptre", "staff", "mace", "wand", "unarmed", "companion", "minion", "ally", "allies", "totem", "reload", "ammunition")


def tw_score(n):
    s = 0.0
    for line in ninja.NODES[str(n)].get("stats") or []:
        if any(k in line.lower() for k in _SKIP):
            continue
        m = pobxml._STAT.match(line)
        if m:
            v, t = int(m.group(1)), m.group(2).lower()
            if "damage" in t and not any(k in t for k in ("taken", "recovery", "duration", "threshold")): s += v
            elif any(k in t for k in ("attack speed", "skill speed")): s += 1.5 * v
            elif "projectile speed" in t or "movement speed" in t: s += .5 * v
            elif "critical" in t: s += .7 * v
            elif "maximum life" in t: s += 3 * v
            continue
        m = pobxml._LIFE.match(line)
        if m: s += int(m.group(1)) / 8
    return s


conector, resto = pobxml.walk_order(root, [])
POB = set(conector) | set(resto)
# Campanha: os nós de dano de projétil perto do início da Mercenary (Remorseless, Ricochet, Heavy Ammunition...) valem MUITO nos primeiros pontos (+96% aos 17 contra +8% só com a árvore do PoB),
# mas saem no respec do endgame: por isso valem 40% (o PoB manda quando o ganho é parecido). Resultado: só 10 nós fora do PoB até o nível ~45 e 26 até os 95 pontos.
sys.path.insert(0, HERE)
import near_start_projectile as NS  # noqa: E402
_ord = pobxml.walk_greedy(list(POB | set(NS.NODES)), START, score=lambda n: tw_score(n) * (1 if n in POB else .4))
_reach = pobxml.walk_greedy_reach(_ord, START)
WALK = [n for n in _ord if n in _reach]
_pob_ord = pobxml.walk_greedy(conector + resto, START, score=tw_score); _pr = pobxml.walk_greedy_reach(_pob_ord, START)
PWALK = [n for n in _pob_ord if n in _pr]; RESTO = [n for n in _pob_ord if n not in _pr]        # árvore do PoB pura (endgame, depois do respec)
print("campanha:", len(WALK), "nós; PoB puro:", len(PWALK), "+", len(RESTO), "que exigem a joia Split Personality; fora do PoB nos 95 primeiros:", len([n for n in WALK[:95] if n not in POB]))

# ---------------------------------------------------------------- itens por fase (o ranking completo por nível está em gear_opts.py)
SPEAR = rare("Hardwood Spear")
BASE_A1 = {"mainHand_set1": SPEAR, "body": uniq("Enfolding Dawn", "Pilgrim Vestments"), "leftRing": uniq("Blackheart", "Iron Ring"), "rightRing": uniq("Blackheart", "Iron Ring"),
           "belt": uniq("Meginord's Girdle", "Rawhide Belt")}
A2 = dict(BASE_A1, mainHand_set1=uniq("Skysliver", "Winged Spear"), boots=uniq("Wanderlust", "Wrapped Sandals"), helmet=uniq("Thrillsteel", "Spired Greathelm"),
          charm1=uniq("The Fall of the Axe", "Silver Charm"))
A3 = dict(A2, mainHand_set1=uniq("Skysliver", "Runeforged Winged Spear", ["Thrud's Might"]), charm2=uniq("Nascent Hope", "Thawing Charm"))
A4 = dict(A3, body=uniq("Widow's Reign", "Knight Armour"), belt=uniq("Cat O' Nine Tails", "Utility Belt"))
MAPAS = dict(A4, rightRing=uniq("The Taming", "Prismatic Ring"), flask2=uniq("Lavianga's Spirits", "Gargantuan Mana Flask"))
FULL = pobxml.items(root)
ENDGAME = {k: v for k, v in FULL.items() if k not in ("belt", "charm2")}
ENDGAME["belt"] = uniq("Cat O' Nine Tails", "Utility Belt")

G = pobxml.gems(root)
CUTS = [("A1", 17, BASE_A1), ("A2", 34, A2), ("A3", 50, A3), ("A4", 72, A4), ("Mapas", 95, MAPAS)]
out = []
for nome, pts, its in CUTS:
    v = pobxml.variant(root, nome, pts, its, G, WALK)
    v["tree"]["a"] = []                              # a ascendência de cada fase é liberada por ASC_PHASE (bdata)
    out.append(v)
for nome, its in (("Endgame", ENDGAME), ("Aspiracional", FULL)):
    v = pobxml.variant(root, nome, None, its, G, PWALK + RESTO)
    out.append(v)
pobxml.write("twister", root, out, URL)
