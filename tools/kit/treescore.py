# -*- coding: utf-8 -*-
"""Valor de um nó da árvore para UMA build específica (o pobxml.node_score conta qualquer '% dano', o que puxa a árvore de campanha para o lado errado:
um caster acaba com nós de melee, um melee com nós de spell).  make(...) devolve score(n) que:
  · só conta dano cujo texto tem uma palavra de `good` e nenhuma de `bad`;
  · velocidade, crítico, vida e mana têm pesos próprios;
  · nós condicionais (while/when/against/recently...) valem 35%, porque a build só cumpre a condição às vezes."""
import re, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ninja  # noqa: E402

COND = ("while ", "when ", "against ", "recently", " per ", " if ", "on full", "low life", "echoed", "hindered", "within ")
ALWAYS_BAD = ("taken", "recovery", "threshold", "cost life", "life cost", "flask", "charm", "stun", "curse", "aura", "herald", "warcry")


def make(good, bad=(), speed=("attack speed", "skill speed", "attack and cast speed"), crit_chance=.7, crit_bonus=.35, life=3.0, mana=0.0, es=0.0, attr=0.0, cond=.35, extra=None):
    def score(n):
        s = 0.0
        for line in ninja.NODES[str(n)].get("stats") or []:
            low = line.lower()
            m = re.match(r"(\d+)% (?:increased|more) (.*)", low)
            if m:
                v, t = int(m.group(1)), m.group(2)
                if any(b in t for b in ALWAYS_BAD) or any(b in t for b in bad): continue
                f = cond if any(k in t for k in COND) else 1.0
                if any(k in t for k in speed): s += 1.5 * v * f
                elif "critical hit chance" in t: s += crit_chance * v * f
                elif "critical damage bonus" in t: s += crit_bonus * v * f
                elif "maximum life" in t: s += life * v * f
                elif "maximum mana" in t: s += mana * v * f
                elif "energy shield" in t: s += es * v * f
                elif "damage" in t and any(g in t for g in good): s += v * f
                continue
            m = re.match(r"\+(\d+) to maximum life", low)
            if m: s += int(m.group(1)) / 8
            m = re.match(r"\+(\d+) to maximum mana", low)
            if m: s += mana * int(m.group(1)) / 6
            m = re.match(r"\+(\d+) to (?:strength|dexterity|intelligence|all attributes)", low)
            if m: s += attr * int(m.group(1))
        if extra: s += extra(n)
        return s
    return score
