# -*- coding: utf-8 -*-
"""Registro e classificador das builds: classe, ascendência, estilo e rankings (mais fácil, mais difícil, dano, clear, boss, clear + boss, sobrevivência, fora do meta).

Nada aqui é digitado à mão, exceto a IDENTIDADE de cada build (classe, ascendência, skills que o poe.ninja usa para reconhecê-la, tags) e as notas EDITORIAIS de clear e boss:
  · facilidade  — calculada do próprio guia (skills ativas, passos de rotação, reservas de Spirit, fases, peças exigidas); relativa às builds do site;
  · dano / sobrevivência — percentil do DPS e do EHP medianos dos personagens do topo (poe.ninja, meta_snapshot.json) entre TODAS as combinações ascendência+skill;
  · meta — parcela de uso da ascendência e da skill no snapshot;
  · clear / boss — nota editorial (1–5) enquanto o poe.ninja não expõe medidas de clear; boss mistura a nota editorial com o percentil de dano.
Saída: tools/dl/registry.json (usado pela landing e por audit.py). Uso: python registry.py"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "kit"))
SNAP = os.path.join(HERE, "dl", "meta_snapshot.json")
OUT = os.path.join(HERE, "dl", "registry.json")

# key = classe CSS da landing; folder = pasta; kit = tem bdata em tools/builds (complexidade calculada); ninja = nomes de skill que o poe.ninja mostra para essa build.
# clear/boss: nota editorial 1–5 (fonte do guia de referência e da mecânica); ease0: facilidade editorial quando não há bdata.
IDENT = [
 dict(key="sf", folder="silverfist", cls="Huntress", asc="Spirit Walker", title="Mighty Silverfist", ninja=["Azmerian Wolf", "Wolf Pack"], tags=["companions", "minions", "melee"], clear=4, boss=4, ease0=3),
 dict(key="or", folder="oracle", cls="Druid", asc="Oracle", title="Oracle Spell Totem", ninja=["Grim Pillars", "Entangle", "Spark"], tags=["totems", "spells", "mana"], clear=4, boss=4, ease0=3),
 dict(key="ta", folder="tactician", cls="Mercenary", asc="Tactician", title="Tactician Pin2Win", ninja=["Explosive Grenade", "Gas Grenade", "Flash Grenade", "Oil Grenade"], tags=["grenades", "crossbow", "ranged"], clear=4, boss=5, ease0=3, kit=True),
 dict(key="in", folder="infernalist", cls="Witch", asc="Infernalist", title="Infernalist Comet", ninja=["Comet", "Spark", "Cast on Critical"], tags=["spells", "meta-skills", "crit"], clear=4, boss=4, ease0=2, kit=True),
 dict(key="ac", folder="acolyte", cls="Monk", asc="Acolyte of Chayula", title="Poisonburst → Tornado Sprinkler", ninja=["Tornado", "Molten Shower", "Poisonburst Arrow"], tags=["poison", "melee", "archon"], clear=4, boss=4, ease0=2, kit=True),
 dict(key="pf", folder="pathfinder", cls="Ranger", asc="Pathfinder", title="Pathfinder Decompose", ninja=["Decompose", "Poisonburst Arrow"], tags=["poison", "bow", "minions"], clear=4, boss=3, ease0=3, kit=True),
 dict(key="sk", folder="smith", cls="Warrior", asc="Smith of Kitava", title="Smith of Kitava Shield Wall", ninja=["Shield Wall", "Earthquake"], tags=["tank", "melee", "fire"], clear=3, boss=4, ease0=4, kit=True),
 dict(key="ma", folder="martial", cls="Monk", asc="Martial Artist", title="Oil Barrage Teleport", ninja=["Storm Wave", "Lightning Warp", "Barrage"], tags=["crit", "teleport", "lightning"], clear=5, boss=4, ease0=2, kit=True),
 dict(key="sh", folder="shaman", cls="Druid", asc="Shaman", title="Tempestade de Mana", ninja=["Spark", "Comet"], tags=["spells", "mana", "lightning"], clear=4, boss=4, ease0=4, kit=True),
 dict(key="lg", folder="legionnaire", cls="Mercenary", asc="Gemling Legionnaire", title="Trovão Cortante", ninja=["Falling Thunder"], tags=["quarterstaff", "lightning", "charges"], clear=4, boss=4, ease0=3, kit=True),
 dict(key="gw", folder="whirling", cls="Mercenary", asc="Gemling Legionnaire", title="Ciclone de Gelo", ninja=["Whirling Slash", "Glacial Bolt"], tags=["crossbow", "cold", "spear"], clear=5, boss=4, ease0=4, kit=True),
]


def complexity(bid):
    """Custo de seguir o guia: quanto MENOR, mais fácil. Vem dos dados da própria build."""
    import common
    B = common.load_build(bid)
    ph = B.PHASES
    gems = max(len(p["gems"]) for p in ph)
    rot = max(len(p.get("rotation") or []) for p in ph)
    reserv = max(sum(1 for g in p["gems"] if g.get("sp") == "core") for p in ph)
    sups = max(sum(len(g.get("sup") or g.get("sups") or []) for g in p["gems"]) for p in ph)
    return dict(phases=len(ph), gems=gems, rotation=rot, reservations=reserv, supports=sups, uniques=len(getattr(B, "UNIQUES", [])), tricks=len(getattr(B, "TRICKS", [])),
                score=round(gems * 1.2 + rot * 1.5 + reserv * 1.5 + sups * .35 + len(getattr(B, "TRICKS", [])) * .4 + len(getattr(B, "UNIQUES", [])) * .15, 1))


def percentile(v, arr):
    arr = sorted(x for x in arr if x)
    return (sum(1 for x in arr if x <= v) / len(arr)) if arr and v else None


def stars(p):
    return None if p is None else max(1, min(5, 1 + int(p * 5 - 1e-9)))


def main():
    snap = json.load(open(SNAP, encoding="utf-8")) if os.path.exists(SNAP) else None
    # todas as combinações ascendência+skill com amostra, para os percentis
    combos = []
    if snap:
        for a, d in snap["ascendancies"].items():
            for s in d["skills"]:
                if s.get("dps") and s.get("ehp") and s["n"] >= 100: combos.append((a, s))
    alldps = [s["dps"] for _, s in combos]; allehp = [s["ehp"] for _, s in combos]
    builds = []
    for b in IDENT:
        e = dict(b); e["ranks"] = {}
        if b.get("kit"):
            e["complexity"] = complexity(b["folder"])
        a = snap["ascendancies"].get(b["asc"]) if snap else None
        best = None
        if a:
            by = {s["skill"]: s for s in a["skills"]}                       # a ordem de b["ninja"] é a de preferência (skill de dano primeiro)
            cand = [by[n] for n in b["ninja"] if n in by and by[n].get("dps")]           # com amostra suficiente (>=100) vale a ordem de preferência; senão a maior amostra
            best = next((c for c in cand if c["n"] >= 100), None) or (max(cand, key=lambda c: c["n"]) if cand else next((by[n] for n in b["ninja"] if n in by), None))
        e["ninja"] = dict(ascShare=a["share"] if a else None, ascN=a["n"] if a else None, skill=best["skill"] if best else None, skillShare=best["share"] if best else None,
                          dps=best["dps"] if best else None, ehp=best["ehp"] if best else None, top=best["top"] if best else None)
        e["dmgPct"] = percentile(best["dps"], alldps) if best else None
        e["ehpPct"] = percentile(best["ehp"], allehp) if best else None
        builds.append(e)
    cs = sorted(e["complexity"]["score"] for e in builds if "complexity" in e)
    for e in builds:
        if "complexity" in e:                                     # 5 = mais fácil (menor custo relativo dentre as builds do site)
            p = sum(1 for x in cs if x >= e["complexity"]["score"]) / len(cs)
            e["ease"] = max(1, min(5, round(1 + p * 4)))
            e["easeSrc"] = "guia"
        else:
            e["ease"] = e["ease0"]; e["easeSrc"] = "editorial"
        e["damage"] = stars(e["dmgPct"]) or e["boss"]
        e["damageSrc"] = "poe.ninja" if e["dmgPct"] is not None else "editorial"
        e["survival"] = stars(e["ehpPct"])
        boss = e["boss"] if e["dmgPct"] is None else round((e["boss"] + stars(e["dmgPct"])) / 2)
        e["scores"] = dict(ease=e["ease"], hard=6 - e["ease"], damage=e["damage"], clear=e["clear"], boss=boss, clearboss=round((e["clear"] + boss) / 2, 1), survival=e["survival"] or 3)
        sh = e["ninja"]["skillShare"]; ash = e["ninja"]["ascShare"]
        e["meta"] = "sem dados" if sh is None and ash is None else ("meta" if (sh or 0) >= 25 else "alternativa" if (sh or 0) >= 5 else "fora do meta")
        # estado automático: sem nenhum personagem usando a skill principal na ascendência = candidata a aposentar
        e["status"] = "ativa"
        if snap and a and sh is None and a["n"] >= 500 and b.get("kit"):
            e["status"] = "revisar"
    order = {k: [b["key"] for b in sorted(builds, key=lambda x: -x["scores"][k])] for k in ("ease", "hard", "damage", "clear", "boss", "clearboss", "survival")}
    order["offmeta"] = [b["key"] for b in sorted(builds, key=lambda x: (x["ninja"]["skillShare"] if x["ninja"]["skillShare"] is not None else 999))]
    out = dict(snapshot=snap and {k: snap[k] for k in ("league", "snapshot", "fetched", "passiveTree", "characters")}, builds=builds, order=order)
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for b in builds:
        print(f"{b['key']} {b['title'][:32]:32} facil {b['scores']['ease']} dano {b['scores']['damage']} clear {b['scores']['clear']} boss {b['scores']['boss']} tank {b['scores']['survival']} | {b['meta']:12} {b['ninja']['skill'] or '-'} {b['ninja']['skillShare']}% | {b['status']}")


if __name__ == "__main__":
    main()
