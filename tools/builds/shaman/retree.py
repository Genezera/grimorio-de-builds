# -*- coding: utf-8 -*-
"""Refaz os cortes de árvore A1–Endgame do Shaman em dl/shaman_variants.json.

O JSON original tinha cortes que não ligavam ao início do Druid (a fase A1 mostrava 1 dos 17 nós do corte; o resto era um caminho de atributos sem dano).
Aqui a árvore final do poe.ninja (Aspiracional, 122 nós) é reordenada 'dano primeiro' e CONECTADA a partir do início do Druid, em estágios que fecham nos
cortes 17/34/50/72/95/118 e respeitam o nível em que cada keystone/notável da build faz sentido (KEY_PASSIVES do bdata):
  Arcane Intensity até o 2º corte (nível 16+) · Elemental Equilibrium até o 3º (36+) · Eldritch Battery e Mind Over Matter até o 4º (52+) ·
  Invocated Efficiency até o 5º (65+) · Pain Attunement e Final Barrage só no último (85+).
Uso: python builds/shaman/retree.py   (depois: kassets → kpatch → kbuild)"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(TOOLS, "kit"))
import ninja, pobxml  # noqa: E402

PATH = os.path.join(TOOLS, "dl", "shaman_variants.json")
START = ninja.CLASS_START["Druid"]
CUTS = [17, 34, 50, 72, 95, 118]
NAMES = ["A1", "A2", "A3", "A4", "Mapas", "Endgame"]
MUST = {1: ["Arcane Intensity"], 2: ["Elemental Equilibrium"], 3: ["Eldritch Battery", "Mind Over Matter"], 4: ["Invocated Efficiency"], 5: ["Pain Attunement", "Final Barrage"]}
BAN = {0: ["Elemental Equilibrium", "Eldritch Battery", "Mind Over Matter", "Pain Attunement", "Final Barrage", "Invocated Efficiency"],
       1: ["Elemental Equilibrium", "Eldritch Battery", "Mind Over Matter", "Pain Attunement", "Final Barrage", "Invocated Efficiency"],
       2: ["Eldritch Battery", "Mind Over Matter", "Pain Attunement", "Final Barrage", "Invocated Efficiency"],
       3: ["Pain Attunement", "Final Barrage", "Invocated Efficiency"],
       4: ["Pain Attunement", "Final Barrage"]}
_BAD = ("attack", "melee", "physical", "minion", "warcry", "bow", "totem", "trap", "mine", "bleed", "poison", "ignite", "armour", "evasion", "block", "thorns", "companion", "curse", "aura", "herald", "flask", "charm", "stun")
_COND = ("while ", "when ", "against ", "recently", " per ", " if ", "hindered", "on full", "low life", "echoed")
_GOOD = ("spell", "lightning", "cast speed", "critical", "elemental", "cold", "fire", "mana", "energy shield", "projectile", "skill speed", "damage")


def score(n):
    """O que um Druid de mana e raio (Spark/Comet) quer de cada nó: dano de spell/raio/elemental, cast speed, crítico, mana máxima e regeneração, ES e vida.
    Nós de melee, físico, ataque, minion etc. valem 0 (o pobxml.node_score conta qualquer 'dano', o que puxa a árvore para o lado errado)."""
    s = 0.0
    for line in ninja.NODES[str(n)].get("stats") or []:
        low = line.lower()
        m = re.match(r"(\d+)% (?:increased|more) (.*)", low)
        if m:
            v, t = int(m.group(1)), m.group(2)
            if any(b in t for b in _BAD) or any(k in t for k in ("taken", "recovery", "threshold", "cost life", "life cost")): continue
            if any(k in t for k in _COND): v = v * .35                    # condicional (Arcane Surge, Hindered, recentemente...): vale pouco enquanto a build não cumpre a condição
            if "cast speed" in t or "skill speed" in t: s += 1.5 * v
            elif "critical" in t: s += .7 * v
            elif "maximum mana" in t: s += 1.2 * v
            elif "mana regeneration" in t: s += .4 * v
            elif "energy shield" in t: s += .4 * v
            elif "maximum life" in t: s += 3 * v
            elif "damage" in t and any(g in t for g in _GOOD): s += v
            continue
        m = re.match(r"\+(\d+) to maximum mana", low)
        if m: s += int(m.group(1)) / 6
        m = re.match(r"\+(\d+) to maximum life", low)
        if m: s += int(m.group(1)) / 8
        m = re.match(r"\+(\d+) to intelligence", low)
        if m: s += int(m.group(1)) * .3
    return s


def local_nodes(start, radius):
    """Nós comuns (sem ascendência, mastery ou início de classe) a até `radius` passos do início do Druid: é onde há dano de spell barato para quem está subindo."""
    from collections import deque
    dist, dq = {start: 0}, deque([start])
    while dq:
        u = dq.popleft()
        if dist[u] >= radius: continue
        for v in ninja.ADJ.get(u, ()):
            nd = ninja.NODES.get(str(v))
            if v in dist or not nd or nd.get("ascendancyName") or nd.get("isMastery") or nd.get("classStartIndex") is not None: continue
            dist[v] = dist[u] + 1; dq.append(v)
    return set(dist) - {start}


LEVELING = ["A1", "A2", "A3", "A4", "Mapas"]     # 17/34/50/72/95: árvore de campanha (dano de spell perto do início + as keystones no nível certo)
RADIUS, OFF_FACTOR = 14, .75                        # nós fora da árvore final valem 75% (a ordem prefere os que ficam no respec)


def main():
    V = json.load(open(PATH, encoding="utf-8"))
    byname = {v["name"]: v for v in V["variants"]}
    asp = byname["Aspiracional"]["tree"]["m"]
    aset = set(asp)
    # 1) campanha: a árvore final + os nós de dano de spell perto do início; a partir do 80 é respec para a árvore final
    lev, _ = pobxml.staged_greedy(list(aset | local_nodes(START, RADIUS)), START, lambda n: score(n) * (1 if n in aset else OFF_FACTOR), CUTS[:5],
                                  {k: v for k, v in MUST.items() if k <= 4}, BAN)
    for nm, cut in zip(LEVELING, CUTS[:5]):
        byname[nm]["tree"]["m"] = lev[:cut]
    # 2) endgame: exatamente a árvore do poe.ninja, conectada a partir do início do Druid
    order, unreach = pobxml.staged_greedy(list(asp), START, score, CUTS, MUST, BAN)
    full = order + unreach
    assert set(full) == aset, "a ordem tem que cobrir exatamente a árvore Aspiracional"
    byname["Endgame"]["tree"]["m"] = full[:CUTS[5]]
    print("árvore final: conectados", len(order), "| não ligam ao início (vão para o fim)", len(unreach))
    json.dump(V, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    prev = set()
    for nm in LEVELING + ["Endgame"]:
        m = byname[nm]["tree"]["m"]
        new = [ninja.NODES[str(n)]["name"] for n in m if n not in prev and (ninja.NODES[str(n)].get("isNotable") or ninja.NODES[str(n)].get("isKeystone"))]
        print(f"{nm:8} {len(m):3} nós | fora da árvore final: {sum(1 for n in m if n not in aset):3} | novos: {', '.join(new)}")
        prev = set(m)


if __name__ == "__main__":
    main()
