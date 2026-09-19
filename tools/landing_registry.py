# -*- coding: utf-8 -*-
"""Camada de classificação da landing: selos de nota em cada card, filtros por classe/ascendência/estilo e ordenação por ranking. Dados de tools/dl/registry.json (registry.py)."""
import json, os, re
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "dl", "registry.json")
RANKS = [("default", "Ordem do guia", "Guide order"), ("ease", "Mais fácil de seguir", "Easiest to follow"), ("hard", "Mais difícil / avançada", "Hardest / advanced"), ("damage", "Mais dano", "Most damage"),
         ("clear", "Melhor clear", "Best clear"), ("boss", "Mais dano em boss", "Most boss damage"), ("clearboss", "Clear + boss", "Clear + boss"), ("survival", "Mais resistente", "Tankiest"),
         ("offmeta", "Fora do meta primeiro", "Off-meta first")]
TAGS = {"companions": ("companions", "companions"), "minions": ("minions", "minions"), "melee": ("corpo a corpo", "melee"), "totems": ("totems", "totems"), "spells": ("spells", "spells"), "mana": ("mana", "mana"),
        "grenades": ("granadas", "grenades"), "crossbow": ("besta", "crossbow"), "ranged": ("à distância", "ranged"), "meta-skills": ("meta skills", "meta skills"), "crit": ("crítico", "crit"),
        "poison": ("veneno", "poison"), "archon": ("archon", "archon"), "bow": ("arco", "bow"), "tank": ("tanque", "tank"), "fire": ("fogo", "fire"), "teleport": ("teleporte", "teleport"),
        "lightning": ("raio", "lightning"), "quarterstaff": ("cajado", "quarterstaff"), "charges": ("cargas", "charges"), "cold": ("gelo", "cold"), "spear": ("spear", "spear")}
META = {"meta": ("meta", "meta"), "alternativa": ("alternativa", "alternative"), "fora do meta": ("fora do meta", "off-meta"), "sem dados": ("sem dados", "no data")}


def load():
    return json.load(open(REG, encoding="utf-8")) if os.path.exists(REG) else None


def stars(n):
    n = int(round(n or 0))
    return "★" * n + "☆" * (5 - n)


def layer(cards, lang):
    """cards: {key: html} na ordem do guia. Devolve (html dos cards decorados, html dos filtros, nº de builds mostradas)."""
    reg = load()
    en = lang == "en"
    L = lambda pt, e: e if en else pt
    if not reg:
        return "".join(cards.values()), "", len(cards)
    by = {b["key"]: b for b in reg["builds"]}
    out, shown, ranks = [], [], reg["order"]
    guide_order = list(cards)
    pos = {k: {r: i for i, r in enumerate(v)} for k, v in ranks.items()}
    for i, (key, html) in enumerate(cards.items()):
        b = by.get(key)
        if not b or b["status"] == "aposentada":
            continue
        s = b["scores"]
        m = META.get(b["meta"], (b["meta"], b["meta"]))[1 if en else 0]
        rate = (f'<div class="build-rate" aria-label="{L("Notas da build", "Build ratings")}">'
                f'<span title="{L("Facilidade de seguir (calculada do guia)", "Ease of following (computed from the guide)")}">{L("Fácil", "Easy")} <b>{stars(s["ease"])}</b></span>'
                f'<span title="{L("Dano (percentil do poe.ninja)" if b["damageSrc"] == "poe.ninja" else "Dano (estimativa)", "Damage (poe.ninja percentile)" if b["damageSrc"] == "poe.ninja" else "Damage (estimate)")}">{L("Dano", "Damage")} <b>{stars(s["damage"])}</b></span>'
                f'<span title="{L("Clear (estimativa do guia)", "Clear (guide estimate)")}">Clear <b>{stars(s["clear"])}</b></span>'
                f'<span title="{L("Boss (estimativa + dano)", "Boss (estimate + damage)")}">Boss <b>{stars(s["boss"])}</b></span>'
                f'<em class="meta-{b["meta"].replace(" ", "-")}">{escape(m)}</em></div>')
        tags = " ".join(b["tags"])
        attrs = (f' data-class="{escape(b["cls"])}" data-asc="{escape(b["asc"])}" data-tags="{escape(tags)}" data-meta="{escape(b["meta"])}" data-guide="{i}"'
                 + "".join(f' data-r-{k}="{pos[k][key]}"' for k in pos))
        html = html.replace(f'<article class="build {key}">', f'<article class="build {key}"{attrs}>', 1).replace('<div class="build-facts">', rate + '<div class="build-facts">', 1)
        out.append(html); shown.append(b)
    classes = sorted({b["cls"] for b in shown})
    ascs = sorted({b["asc"] for b in shown})
    tags = sorted({t for b in shown for t in b["tags"]}, key=lambda t: TAGS.get(t, (t, t))[1 if en else 0])
    opt = lambda v, t: f'<option value="{escape(v)}">{escape(t)}</option>'
    bar = (f'<form class="build-filter" aria-label="{L("Filtrar e ordenar as builds", "Filter and sort the builds")}" onsubmit="return false">'
           f'<label><span>{L("Classe", "Class")}</span><select id="fClass"><option value="">{L("Todas", "All")}</option>{"".join(opt(c, c) for c in classes)}</select></label>'
           f'<label><span>{L("Ascendência", "Ascendancy")}</span><select id="fAsc"><option value="">{L("Todas", "All")}</option>{"".join(opt(a, a) for a in ascs)}</select></label>'
           f'<label><span>{L("Estilo", "Style")}</span><select id="fTag"><option value="">{L("Todos", "All")}</option>{"".join(opt(t, TAGS.get(t, (t, t))[1 if en else 0]) for t in tags)}</select></label>'
           f'<label><span>{L("Ordenar por", "Sort by")}</span><select id="fSort">{"".join(opt(k, e if en else p) for k, p, e in RANKS)}</select></label>'
           f'<label><span>{L("Uso no poe.ninja", "poe.ninja usage")}</span><select id="fMeta"><option value="">{L("Qualquer", "Any")}</option>{"".join(opt(k, v[1 if en else 0]) for k, v in META.items() if k != "sem dados")}</select></label>'
           f'<output id="fCount" aria-live="polite"></output></form>')
    snap = reg.get("snapshot")
    note = ""
    if snap:
        note = (f'<p class="rank-note">{L("Ranking calculado com o poe.ninja", "Ranking computed from poe.ninja")} · {escape(snap["league"])} · {escape(snap["fetched"])} · {snap["characters"]:,} {L("personagens", "characters")}. '
                f'{L("Facilidade sai do próprio guia; dano é o percentil do DPS dos personagens do topo; clear e boss começam como estimativa do guia.", "Ease comes from the guide itself; damage is the percentile of top characters’ DPS; clear and boss start as guide estimates.")}</p>')
    return "".join(out), bar + note, len(shown)
