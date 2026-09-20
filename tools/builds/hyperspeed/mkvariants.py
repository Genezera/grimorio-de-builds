# -*- coding: utf-8 -*-
"""Gera dl/hyperspeed_variants.json: [0.5] Hyper SPEED — Hollow Palm Monk Build (Ronarray, Mobalytics, atualizado em 02/07/2026).

O guia do autor tem SEIS variantes, cada uma com equipamento, gems, árvore e notas próprias:
  Lvl 1-23 · 23+ Unarmed · Act 3-6 · Waystones / 85+ Wave · Normal Endgame · Final Endgame
A captura do guia está em dl/hollowpalm_payload.json (variantes compactadas: equipamento, gems, árvore, joias) e dl/hollowpalm_text.json (as notas do autor por variante).
Este script devolve o mesmo formato do kit/extract.py (nomes reais de gem, itens, árvore, joias) e faz os CORTES DE ÁRVORE por fase:
  · cada variante do autor é uma árvore (24, 36, 88, 114, 108 nós); as fases do guia usam cortes de pontos (17/34/50/72/95) DENTRO da variante que o autor indica para aquele momento;
  · a ordem dentro do corte é 'dano primeiro' (pobxml.staged_greedy + kit/treescore.py), sempre conectada ao início do Monk, e Hollow Palm Technique entra no corte em que o autor manda.
Uso: python builds/hyperspeed/mkvariants.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(ROOT, "kit"))
import ninja, pob, pobxml, treescore  # noqa: E402

PAYLOAD = json.load(open(os.path.join(ROOT, "dl", "hollowpalm_payload.json"), encoding="utf-8-sig"))
TEXT = json.load(open(os.path.join(ROOT, "dl", "hollowpalm_text.json"), encoding="utf-8"))
ART = "https://cdn.mobalytics.gg/assets/poe-2/images/game/Art/"
START = ninja.CLASS_START["Monk"]
SLUG = pob.slug_names()
NAMES = ["Normal Endgame", "Final Endgame", "Lvl 1-23", "23+ Unarmed", "Act 3-6", "Waystones / 85+ Wave"]
URL = "https://mobalytics.gg/poe-2/builds/ronarray-unarmed-hollow-palm-monk"


def _dec(o, T):
    if isinstance(o, list): return [_dec(x, T) for x in o]
    if isinstance(o, dict): return {k: _dec(v, T) for k, v in o.items()}
    if isinstance(o, str) and o.startswith("~"): return T[int(o[1:])]
    return o


SRC = dict(zip(NAMES, _dec(PAYLOAD["v"], PAYLOAD["T"])))
NOTES = {r["t"].strip(): r for r in TEXT["res"]}
missing = set()


def gname(slug):
    s2 = slug.replace("player", "")
    n = SLUG.get(slug, SLUG.get(s2, SLUG.get(s2.replace("support", "", 1))))
    if not n: missing.add(slug)
    return n or slug


def item(x):
    if not x: return None
    if "n" not in x: return {"skill": x.get("skill")}
    return {"n": x["n"], "u": x.get("u", 0), "icon": ART + x["i"] if x.get("i") else None, "mods": x.get("m", []), "stats": [], "runes": x.get("r", []), "skill": x.get("s")}


def items(v):
    return {k: item(x) for k, x in v["it"].items() if x}


def gems(v):
    out = []
    for g in v["gems"]:
        out.append({"skill": g["k"], "slug": g["g"], "icon": ART + g["i"], "skillIcon": ART + g["si"], "sup": [gname(s[0]) for s in g["sup"]],
                    "supIcons": {gname(s[0]): ART + s[1] for s in g["sup"]}, "weaponSet": g["w"], "level": g["l"]})
    return out


def jewels(v):
    out = []
    for j in v["jw"]:
        kind = "SapphireJewel" if j["jewelSlug"] in ("jewel-jewelint", "jewel-jeweldiamond") else "EmeraldJewel" if "dex" in j["jewelSlug"] else "RubyJewel"
        out.append(dict(j, iconURL=ART + "2DItems/Jewels/" + kind + ".avif"))
    return out


# ---------------------------------------------------------------- árvore
# O que um Monk de ataque desarmado (Hollow Palm) quer de cada nó: dano de ataque/melee/elemental/crítico, velocidade, vida, ES e Evasion (a velocidade dele SOBE com Evasion).
_score = treescore.make(good=("attack", "melee", "quarterstaff", "unarmed", "lightning", "elemental", "cold", "fire", "physical", "damage"),
                        bad=("spell", "minion", "totem", "trap", "mine", "bow", "crossbow", "grenade", "companion", "projectile", "chain", "pierce", "fork", "one handed", "one-handed", "ally", "allies"),
                        life=3.0, es=0.35, crit_bonus=.3)


def score(n):
    s = _score(n)
    for line in ninja.NODES[str(n)].get("stats") or []:                       # Evasion e ES em % também valem: a velocidade do Hollow Palm vem da Evasion e o crítico do ES
        low = line.lower()
        if low.endswith("increased evasion rating") or "% increased evasion rating" in low: s += 8
    return s


def cut(name, cuts, must=None, bonus=None):
    """bonus = {nó: pontos a mais}: puxa para o corte os nós que já estavam na fase anterior (ou que ficam na seguinte), para o jogador não desfazer ponto à toa."""
    bonus = bonus or {}
    v = SRC[name]
    order, _ = pobxml.staged_greedy(v["m"], START, lambda n: score(n) + bonus.get(n, 0), cuts, must or {}, {})
    return order


def favor(*groups):
    out = {}
    for pts, nodes in groups:
        for n in nodes: out[n] = out.get(n, 0) + pts
    return out


# (variante-fonte, cortes, nós que precisam entrar até o corte). São OITO fases: a variante Act 3-6 do autor cobre três (Atos 3, 4 e o começo dos mapas) e a Waystones vem depois dela.
A1 = cut("Lvl 1-23", [17])[:17]
A2 = cut("23+ Unarmed", [34], {0: ["Hollow Palm Technique"]}, favor((300, A1)))[:34]
_act = cut("Act 3-6", [50, 72, 88], {0: ["Hollow Palm Technique"]}, favor((300, A2)))
A3, A4, MAPS = _act[:50], _act[:72], _act[:88]
ENDGAME = cut("Normal Endgame", [108])[:108]
MAX = cut("Final Endgame", [108])[:108]
WAVE = cut("Waystones / 85+ Wave", [105], {0: ["Hollow Palm Technique", "Chaos Inoculation"]}, favor((80, MAPS), (40, ENDGAME)))[:105]
for nm, o, want in (("A1", A1, 17), ("A2", A2, 34), ("A3", A3, 50), ("A4", A4, 72), ("Mapas", MAPS, 88), ("Waystones", WAVE, 105), ("Endgame", ENDGAME, 108), ("Aspiracional", MAX, 108)):
    print(f"{nm:13} {len(o):3} nós (pedido {want}) | notáveis novos:", [ninja.NODES[str(n)]["name"] for n in o if ninja.NODES[str(n)].get("isNotable") or ninja.NODES[str(n)].get("isKeystone")][-6:])


DROPPED = []


def variant(name, src_name, order, note_from=None):
    v = SRC[src_name]
    allowed = set(v["m"]) | set(v["s1"]) | set(v["s2"])                        # joias em sockets que a árvore do autor não aloca (Sinister Jewel Socket) ficam de fora: o guia não diz como abrem
    for j in v["jw"]:
        if int(j["nodeSlug"].split("-")[1]) not in allowed and (name, j["nodeSlug"]) not in DROPPED: DROPPED.append((name, j["nodeSlug"]))
    v = dict(v, jw=[j for j in v["jw"] if int(j["nodeSlug"].split("-")[1]) in allowed])
    desc = NOTES.get((note_from or src_name).strip(), {}).get("desc", "")
    return {"src": "mobalytics", "name": name, "items": items(v), "gems": gems(v),
            "tree": {"m": order, "s1": v["s1"], "s2": v["s2"], "a": v["a"], "attr": None, "jewels": jewels(v)}, "desc": desc, "source": src_name}


out = [variant("A1", "Lvl 1-23", A1), variant("A2", "23+ Unarmed", A2), variant("A3", "Act 3-6", A3), variant("A4", "Act 3-6", A4), variant("Mapas", "Act 3-6", MAPS),
       variant("Waystones", "Waystones / 85+ Wave", WAVE), variant("Endgame", "Normal Endgame", ENDGAME), variant("Aspiracional", "Final Endgame", MAX)]
meta = [{"src": "mobalytics", "title": "[0.5] Hyper SPEED - Hollow Palm Monk Build (12-18 Attacks Per Second)", "url": URL, "author": "Ronarray", "updatedAt": "2026-07-02T20:21:02Z", "widgets": []}]
json.dump({"guides": meta, "variants": out}, open(os.path.join(ROOT, "dl", "hyperspeed_variants.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for v in out:
    print(f"- {v['name']} ({v['source']}): árvore {len(v['tree']['m'])} | s1 {len(v['tree']['s1'])} s2 {len(v['tree']['s2'])} | asc {len(v['tree']['a'])} | gems {len(v['gems'])} | itens {len(v['items'])} | joias {len(v['tree']['jewels'])}")
if missing: print("slugs sem nome no PoB:", sorted(missing))
print("joias fora da árvore alocada (não entram no painel):", DROPPED)
