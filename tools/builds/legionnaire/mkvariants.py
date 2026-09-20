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
# CAMPANHA (A1–Mapas): o caminho do PoB até as notables de crítico de cajado fica a 16–30 passos do início da Mercenary (uma fila de atributos: 0% de dano até o nível 30).
# Aqui a campanha é uma ADAPTAÇÃO: nós de dano de ataque/melee/elemental/crítico perto do início da Mercenary, na ordem 'dano primeiro' (pobxml.staged_greedy) com o valor de
# cada nó medido para esta build (kit/treescore.py: sem projétil, spell, minion...). O respec do 79 troca tudo pela árvore exata do PoB.
import treescore  # noqa: E402
from collections import deque  # noqa: E402
_MAIN = {n for n in (int(x) for x in root.find("Tree").findall("Spec")[0].get("nodes").split(",") if x) if not ninja.NODES[str(n)].get("ascendancyName")}
_START = ninja.CLASS_START["Mercenary"]


def _local(start, radius):
    dist, dq = {start: 0}, deque([start])
    while dq:
        u = dq.popleft()
        if dist[u] >= radius: continue
        for v in ninja.ADJ.get(u, ()):
            nd = ninja.NODES.get(str(v))
            if v in dist or not nd or nd.get("ascendancyName") or nd.get("isMastery") or nd.get("classStartIndex") is not None: continue
            dist[v] = dist[u] + 1; dq.append(v)
    return set(dist) - {start}


_score = treescore.make(good=("attack", "melee", "quarterstaff", "staves", "staff", "lightning", "elemental", "physical", "damage"),
                        bad=("spell", "minion", "totem", "trap", "mine", "bow", "crossbow", "grenade", "companion", "projectile", "chain", "pierce", "fork",
                              "one handed", "one-handed", "ally", "allies", "presence", "fire damage", "cold damage", "chaos", "flammability"))
WALK, _ = pobxml.staged_greedy(list(_MAIN | _local(_START, 14)), _START, lambda n: _score(n) * (1 if n in _MAIN else .75), [17, 34, 50, 72, 95],
                              {3: ["The Fabled Stag"], 4: ["The Power Within", "One with the Storm"]})   # as cargas entram quando o guia já tem fonte de carga (Redflare no 33)
RESTO = []
print("campanha (adaptação): ", len(WALK), "nós, a até 14 passos do início da Mercenary;", sum(1 for n in WALK if n in _MAIN), "deles também estão na árvore do PoB")
# (nome, pontos, usa o caminho da Mercenary?)
CUTS = [("A1", 17, True), ("A2", 34, True), ("A3", 50, True), ("A4", 72, True), ("Mapas", 95, True), ("Endgame", 111, False), ("Aspiracional", None, False)]
# Endgame e Aspiracional: a árvore EXATA do PoB. Ela parte do início do Monk (44683), aberto pela joia Split Personality no socket 21984.
_main = [n for n in (int(x) for x in root.find("Tree").findall("Spec")[0].get("nodes").split(",") if x) if not ninja.NODES[str(n)].get("ascendancyName")]
POB_ORDER = ninja.grow_order(_main, 44683)
G = pobxml.gems(root)
pobxml.write("legionnaire", root, [pobxml.variant(root, n, p, ITEMS[n], G, WALK + RESTO if w else POB_ORDER) for n, p, w in CUTS], URL)
