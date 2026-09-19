# -*- coding: utf-8 -*-
"""Gera dl/whirling_variants.json: WHIRLING Glacial Bolt Gemling [POE2 0.5] (Phylaris POE, Mobalytics, 13/08/2026).

O guia do autor tem 3 variantes — Leveling, Endgame (Early) e Endgame — e um PoB do endgame (nível 97, dl/whirling_pob.txt).
Os ids de passivas (mainTree/set1Tree/set2Tree/ascendancyTree) e os itens das duas primeiras variantes foram lidos da página; os itens do endgame vêm do PoB.
O plano de leveling é uma adaptação: as fases A1–Mapas são cortes (17/34/50/72/85 pontos) da árvore Endgame (Early) do autor, na ordem que a Mercenary consegue alocar, com os Weapon Sets crescendo junto.
Uso: python mkvariants.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(ROOT, "kit"))
import pobxml, ninja, jewels  # noqa: E402

URL = "https://mobalytics.gg/poe-2/profile/stone-dagger-zuckm8/builds/whirling-glacial-bolt-gemling-poe2-0-5"
root = pobxml.decode(open(os.path.join(ROOT, "dl", "whirling_pob.txt"), encoding="utf-8").read().strip())
E = pobxml.eco_item

# ---------------------------------------------------------------- árvores (ids de nós, lidos do Mobalytics)
LEVELING = [59915, 2455, 48588, 13081, 44605, 59881, 28556, 16489, 10909, 33053, 4844, 58013, 50795, 17726, 11826, 48401, 35987, 19470, 10053, 50328, 28992, 22795, 42781, 13783, 30695,
            8092, 59028, 41210, 43578, 49657, 63526, 48635, 21755, 54127, 28370, 14997, 47856, 32561, 51825, 9164, 25513, 47363, 62051, 17340, 56978, 21274, 39298, 3995, 12311, 64119,
            38814, 17118, 27493, 19342, 46296, 62510, 56818, 43423, 8697, 38895, 30905, 64140, 3985, 34201, 24922, 17077, 51463, 4364, 23736, 36114, 23360, 53566, 46882, 38463, 30657,
            24786, 24287, 5305, 3431, 43082, 6842, 3700, 36723, 28329, 12893, 65167, 712]
EARLY = dict(
    m=[59779, 97, 52442, 34061, 56910, 14926, 50609, 11916, 28370, 14997, 47856, 32561, 51825, 47363, 9164, 63526, 48635, 21755, 54127, 54282, 52125, 2847, 54099, 8493, 64471, 28175, 2491,
       51561, 62498, 3446, 27082, 53719, 59777, 27296, 59785, 1200, 55190, 28982, 31295, 9352, 32071, 21387, 63114, 26725, 57703, 54485, 25482, 28304, 52556, 16347, 52373, 37276, 36522,
       9737, 24813, 20397, 28492, 55802, 23702, 57196, 3660, 25619, 58814, 51048, 17702, 46882, 34201, 24922, 38463, 30657, 24786, 24287, 34015, 54984, 11825, 60735, 36576, 25055, 41580,
       14226, 5305, 3431, 43082, 62051, 17340],
    s1=[64492, 5191, 35863, 46961, 10774, 42658, 4238, 63566, 39598, 46688, 28613, 63445, 7163, 28142, 3949, 62350, 56928, 43263, 40244, 37258, 17316, 45100, 26568, 51732, 23702, 28304,
        60735, 34201, 17702, 27296],
    s2=[38895, 25513, 18505, 34210, 52392, 18073, 30123, 8697, 45090, 36027, 23736, 30905, 51463, 64939, 4364, 17077, 54811, 26092, 58814, 24922, 63114, 57703, 9737, 34201, 9164, 64140,
        3985, 19223, 25213, 21871, 37872])
FINAL = dict(
    m=[59779, 97, 52442, 34061, 56910, 14926, 50609, 11916, 28370, 14997, 47856, 32561, 51825, 47363, 9164, 63526, 48635, 21755, 54127, 54282, 52125, 2847, 54099, 8493, 64471, 28175, 2491,
       51561, 62498, 3446, 27082, 53719, 59777, 27296, 59785, 1200, 55190, 28982, 31295, 9352, 32071, 21387, 63114, 26725, 57703, 54485, 25482, 28304, 52556, 16347, 52373, 37276, 36522,
       9737, 24813, 20397, 23888, 29399, 51446, 28492, 55802, 23702, 57196, 3660, 25619, 58814, 51048, 17702, 46882, 34201, 24922, 38463, 30657, 24786, 24287, 34015, 54984, 11825, 60735,
       36576, 25055, 41580, 14226, 5305, 3431, 43082, 62051, 17340, 19223, 25213, 21871, 37872],
    s1=EARLY["s1"],
    s2=[38895, 25513, 26952, 18505, 34210, 52392, 18073, 30123, 35739, 8697, 42410, 31626, 50516, 45090, 36027, 2814, 23736, 30905, 51463, 64939, 4364, 17077, 54811, 26092, 58814, 24922,
        63114, 57703, 9737, 34201, 9164])
ASC = [34882, 11641, 45248, 14429, 55582, 60287, 63259, 3084, 30996]      # as 9 do Gemling nas duas variantes de endgame (as mesmas do PoB do Legionnaire)
START = ninja.CLASS_START["Mercenary"]

# ---------------------------------------------------------------- itens
def rare(base, mods=(), runes=(), stats=()):
    return {"n": base, "u": 0, "icon": ninja.ART_BY_BASE.get(base), "mods": list(mods), "stats": list(stats), "runes": list(runes), "skill": None}


def uniq(name, base, runes=()):
    d = E(name, base); d["runes"] = list(runes); return d


RR = lambda base, runes: uniq("Rampart Raptor", base, runes)
_spears = sorted([b for b in ninja.BASES.values() if b.get("item_class") == "Spear" and b.get("name") and (b.get("visual_identity") or {}).get("dds_file")], key=lambda b: b.get("drop_level", 0))
SPEAR = rare(_spears[0]["name"], runes=[])               # spear branca do vendor: só precisa existir para a Whirling Slash
SKY = lambda base, runes=(): uniq("Skysliver", base, runes)
BASE_A1 = {"mainHand_set1": SPEAR, "mainHand_set2": RR("Tense Crossbow", ["Lesser Glacial Rune"]), "body": uniq("Tabula Rasa", "Garment"), "leftRing": uniq("Blackheart", "Iron Ring"),
           "rightRing": uniq("Blackheart", "Iron Ring"), "belt": uniq("Meginord's Girdle", "Rawhide Belt")}
A2 = dict(BASE_A1, boots=uniq("Wanderlust", "Wrapped Sandals"), helmet=uniq("Thrillsteel", "Spired Greathelm"), mainHand_set1=SKY("Winged Spear"),
          mainHand_set2=RR("Tense Crossbow", ["Greater Glacial Rune"]))
A3 = dict(A2, mainHand_set1=SKY("Runeforged Winged Spear", ["Soul Core of Speed"]), mainHand_set2=RR("Runeforged Tense Crossbow", ["Greater Glacial Rune", "Greater Glacial Rune"]),
          boots=uniq("Wanderlust", "Runemastered Wrapped Sandals"))
A4 = dict(A3, mainHand_set2=RR("Runemastered Tense Crossbow", ["Greater Glacial Rune", "Greater Glacial Rune"]),
          helmet=uniq("Thrillsteel", "Runemastered Spired Greathelm"))
EARLY_ITEMS = {
    "helmet": rare("Imperial Greathelm"), "body": uniq("Morior Invictus", "Grand Regalia", ["Warding Rune of Heart", "Fox Idol", "Panther Idol", "Tecrod's Gaze", "Rune of the Ancients"]),
    "gloves": rare("Massive Mitts", runes=["Rune of Warping"]), "boots": rare("Vaal Greaves", runes=["Perfect Life Rune"]), "amulet": rare("Absent Amulet"),
    "leftRing": rare("Ruby Ring"), "rightRing": rare("Topaz Ring"), "belt": uniq("Headhunter", "Heavy Belt"), "charm1": rare("Dousing Charm"), "charm2": rare("Silver Charm"),
    "charm3": uniq("Rite of Passage", "Golden Charm"), "flask1": rare("Ultimate Life Flask"), "flask2": uniq("Lavianga's Spirits", "Gargantuan Mana Flask"),
    "mainHand_set1": uniq("Skysliver", "Runeforged Winged Spear", ["Soul Core of Speed", "Soul Core of Speed"]), "mainHand_set2": rare("Desolate Crossbow", runes=["Rune of Special", "Rune of Special"]),
}
FULL = pobxml.items(root)

PRIORITY = ["Hard to Kill", "Battle-hardened", "Sand in the Eyes", "Authority", "Adrenaline Rush", "Acceleration", "Colossal Weapon", "Dance with Death", "Battle Trance", "Primal Growth",
            "Maiming Strike", "Beef", "Iron Reflexes"]
WALK = pobxml.walk_nodes(EARLY["m"], START, PRIORITY)                      # árvore do Endgame (Early): 79+ (respec)
# CAMPANHA: a árvore de LEVELING do autor (87 pontos). Nos primeiros 72 pontos ela tem +251% de dano de projétil; a do endgame tem 0% (medido nos nós): por isso a campanha NÃO segue a do endgame.
LWALK = ninja.grow_order(LEVELING, START)


def reachable(extra):
    seen, st, allowed = {START}, [START], set(LEVELING) | set(extra) | {START}
    while st:
        u = st.pop()
        for w in ninja.ADJ.get(u, ()):
            if w in allowed and w not in seen: seen.add(w); st.append(w)
    return seen
_r1, _r2 = reachable(EARLY["s1"]), reachable(EARLY["s2"])
S1 = pobxml.order_set(EARLY["s1"], EARLY["m"], START)
S2 = pobxml.order_set(EARLY["s2"], EARLY["m"], START)
S1C = [n for n in pobxml.order_set(EARLY["s1"], LEVELING, START) if n not in set(LEVELING) and n in _r1]      # nós de Weapon Set que ligam à árvore de leveling
S2C = [n for n in pobxml.order_set(EARLY["s2"], LEVELING, START) if n not in set(LEVELING) and n in _r2]
# fase: (nome, pontos da árvore de leveling, nós de Weapon Set 1, nós de Weapon Set 2, itens): os pontos de Weapon Set vêm 2 a 2 das quests
CUTS = [("A1", 17, 0, 0, BASE_A1), ("A2", 34, 2, 2, A2), ("A3", 50, 4, 4, A3), ("A4", 72, 8, 4, A4), ("Mapas", 87, 10, 4, A4)]
G = pobxml.gems(root)
out = []
for nome, pts, n1, n2, its in CUTS:
    v = pobxml.variant(root, nome, pts, its, G, LWALK)
    v["tree"]["s1"] = S1C[:n1]; v["tree"]["s2"] = S2C[:n2]
    v["tree"]["a"] = []                  # a ascendência de cada fase é liberada por ASC_PHASE (bdata)
    out.append(v)
FINAL_WALK = pobxml.walk_nodes(FINAL["m"], START, PRIORITY)
for nome, tr, m_order, its in (("Endgame", EARLY, WALK, EARLY_ITEMS), ("Aspiracional", FINAL, FINAL_WALK, FULL)):
    out.append({"src": "mobalytics", "name": nome, "items": its, "gems": G, "level": 97,
                "tree": {"m": m_order, "s1": S1 if tr is EARLY else tr["s1"], "s2": S2 if tr is EARLY else tr["s2"], "a": ASC, "attr": None, "jewels": jewels.from_pob(root)}, "desc": ""})
pobxml.write("whirling", root, out, URL)
