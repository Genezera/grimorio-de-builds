# -*- coding: utf-8 -*-
"""Gera dl/legionnaire_variants.json a partir do PoB do poe.ninja (dl/legionnaire_pob.txt): árvore cortada por pontos e itens por fase.  Uso: python mkvariants.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(ROOT, "kit"))
import pobxml  # noqa: E402
import ninja  # noqa: E402

URL = "https://poe.ninja/poe2/pob/29764"
root = pobxml.decode(open(os.path.join(ROOT, "dl", "legionnaire_pob.txt"), encoding="utf-8").read())
FULL = pobxml.items(root)
E = pobxml.eco_item


def without(*slots):
    return {k: v for k, v in FULL.items() if k not in slots}


ITEMS = {
    "A1": {},
    "A2": {"charm1": E("Breath of the Mountains", "Sapphire Charm")},
    "A3": {"charm1": E("Breath of the Mountains", "Sapphire Charm"), "body": E("Redflare Conduit", "Anchorite Garb"), "boots": E("Powertread", "Hunting Shoes")},
    "A4": {"charm1": E("Nascent Hope", "Thawing Charm"), "body": E("Redflare Conduit", "Anchorite Garb"), "boots": E("Powertread", "Hunting Shoes"),
           "leftRing": E("Grip of Kulemak", "Abyssal Signet")},
    "Mapas": without("rightRing", "offHand_set2", "mainHand_set2"),
    "Endgame": without("rightRing", "offHand_set2"),
    "Aspiracional": FULL,
}
# Notables na ordem em que fazem sentido para quem sobe de nível (o caminho até elas é sempre o mais curto a partir da Mercenary)
PRIORITY = ["Martial Artistry", "Stand and Deliver", "The Fabled Stag", "One with the Storm", "The Power Within", "Deadly Force", "Heartbreaking", "Moment of Truth", "For the Jugular",
            "Tainted Strike", "Coming Calamity", "Catalysis", "Crashing Wave", "Heartstopping", "Struck Through", "Maiming Strike", "Acceleration", "Flow Like Water",
            "Critical Exploit", "Careful Assassin", "True Strike", "Throatseeker", "Overflowing Power"]
WALK, RESTO = pobxml.walk_order(root, PRIORITY)
print("caminho da Mercenary:", len(WALK), "nós; exigem a joia Split Personality:", len(RESTO))
# (nome, pontos, usa o caminho da Mercenary?)
CUTS = [("A1", 17, True), ("A2", 34, True), ("A3", 50, True), ("A4", 72, True), ("Mapas", 95, True), ("Endgame", 111, False), ("Aspiracional", None, False)]
# Endgame e Aspiracional: a árvore EXATA do PoB. Ela parte do início do Monk (44683), aberto pela joia Split Personality no socket 21984.
_main = [n for n in (int(x) for x in root.find("Tree").findall("Spec")[0].get("nodes").split(",") if x) if not ninja.NODES[str(n)].get("ascendancyName")]
POB_ORDER = ninja.grow_order(_main, 44683)
G = pobxml.gems(root)
pobxml.write("legionnaire", root, [pobxml.variant(root, n, p, ITEMS[n], G, WALK + RESTO if w else POB_ORDER) for n, p, w in CUTS], URL)
