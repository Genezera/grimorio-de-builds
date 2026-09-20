# -*- coding: utf-8 -*-
"""Página inicial (escolha de build): ../index.html (PT) e ../en.html (EN)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..")
SF = json.load(open(os.path.join(HERE, "assets.json"), encoding="utf-8"))
OR = json.load(open(os.path.join(HERE, "oracle", "assets.json"), encoding="utf-8"))
def ico(A, table, name):
    for t in (table, "gemIcon", "supIcon", "uniqIcon"):   # gems encaixadas em meta skills ficam em supIcon
        k = A.get(t, {}).get(name)
        if k and A["icons"].get(k): return A["icons"][k]
    raise SystemExit(f"landing: ícone vazio para {name!r}")
IC = {
 "sf_main": ico(SF, "gemIcon", "Tame Beast"), "sf_a": ico(SF, "uniqIcon", "Chober Chaber"), "sf_b": ico(SF, "uniqIcon", "Sylvan's Effigy"), "sf_c": ico(SF, "gemIcon", "Pain Offering"),
 "or_main": ico(OR, "gemIcon", "Spell Totem"), "or_a": ico(OR, "supIcon", "Grim Pillars"), "or_b": ico(OR, "gemIcon", "Archmage"), "or_c": ico(OR, "uniqIcon", "Soul Mantle"),
}
def kit(bid): return json.load(open(os.path.join(HERE, "builds", bid, "assets.json"), encoding="utf-8"))
for key, bid, picks in (("ta", "tactician", [("gemIcon", "Explosive Grenade"), ("gemIcon", "Cluster Grenade"), ("gemIcon", "Mirage Archer"), ("uniqIcon", "Sanguis Heroum")]),
                        ("in", "infernalist", [("gemIcon", "Spark"), ("gemIcon", "Cast on Critical"), ("gemIcon", "Demon Form"), ("uniqIcon", "Sacrosanctum")]),
                        ("ac", "acolyte", [("gemIcon", "Poisonburst Arrow"), ("gemIcon", "Herald of Blood"), ("gemIcon", "Toxic Growth"), ("uniqIcon", "Splinterheart")]),
                        ("pf", "pathfinder", [("gemIcon", "Decompose"), ("gemIcon", "Poisonburst Arrow"), ("gemIcon", "Plague Bearer"), ("uniqIcon", "Corpsewade")]),
                        ("sk", "smith", [("gemIcon", "Shield Wall"), ("gemIcon", "Resonating Shield"), ("gemIcon", "Infernal Cry"), ("uniqIcon", "Nebuloch")]),
                        ("ma", "martial", [("gemIcon", "Oil Barrage"), ("gemIcon", "Lightning Warp"), ("gemIcon", "Cast on Critical"), ("uniqIcon", "Forgotten Warden")]),
                        ("sh", "shaman", [("gemIcon", "Spark"), ("gemIcon", "Comet"), ("gemIcon", "Archmage"), ("uniqIcon", "Sire of Shards")]),
                        ("lg", "legionnaire", [("gemIcon", "Falling Thunder"), ("gemIcon", "Charged Staff"), ("gemIcon", "Herald of Thunder"), ("uniqIcon", "Redflare Conduit")]),
                        ("gw", "whirling", [("gemIcon", "Permafrost Bolts"), ("gemIcon", "Glacial Bolt"), ("gemIcon", "Whirling Slash"), ("uniqIcon", "Rampart Raptor")]),
                        ("tw", "twister", [("gemIcon", "Twister"), ("gemIcon", "Whirling Slash"), ("gemIcon", "Barrage"), ("uniqIcon", "Sacred Flame")]),
                        ("hs", "hyperspeed", [("gemIcon", "Tempest Flurry"), ("gemIcon", "Staggering Palm"), ("gemIcon", "Falling Thunder"), ("uniqIcon", "Mageblood")])):
    A = kit(bid)
    for suf, (table, name) in zip(("main", "a", "b", "c"), picks):
        IC[f"{key}_{suf}"] = ico(A, table, name)
TXT = {
 "pt": dict(lang="pt-BR", title="Grimório de Builds · PoE 2", eyebrow="Path of Exile 2 · 0.5.5 · Forbidden Rites", h1="Grimório de Builds",
   lead="Escolha a build. Cada guia vai do nível 1 ao 100, explica cada gem, support, item e passiva, e se adapta ao que você marca: seu nível, seu Spirit e os itens que você já tem.",
   start="Começar o guia", cont="Continuar do nível", other="English", other_href="en.html", self_suffix="index.html",
   sf=dict(cls="Huntress · Spirit Walker", name="The Mighty Silverfist Trail", pitch="Zoo de companions: o macaco Mighty Silverfist carrega o dano com Chober Chaber e The Catha's Balance.",
           facts=["Estilo: companions e minions (1–2 botões)", "Virada: captura do macaco no Ato 3", "Endgame: Sylvan's Effigy, auras e Azmerian Wolf", "Base: guia do Mattjestic"]),
   orc=dict(cls="Druid · Oracle", name="The Oracle of Totems", pitch="Spell Totems lançando Spark e depois Grim Pillars + Bitter Dead, com mana virando dano e defesa (Archmage, Mind Over Matter).",
           facts=["Estilo: totems e spells (2 botões)", "Virada: troca para Spell Totem no fim do Ato 4", "Endgame: Grim Pillars, Archmage e Soul Mantle", "Base: guia do Lowepe"]),
   both="Nas duas: PT/EN · rota 1→100 · árvore que acompanha o nível · Meu personagem com recomendações · Quando usar cada peça · planilha no repositório.",
   foot="Projeto de fã, sem vínculo com a Grinding Gear Games. Dados de jogo: Path of Building; preços: poe.ninja."),
 "en": dict(lang="en", title="Build Grimoire · PoE 2", eyebrow="Path of Exile 2 · 0.5.5 · Forbidden Rites", h1="Build Grimoire",
   lead="Pick a build. Each guide goes from level 1 to 100, explains every gem, support, item and passive, and adapts to what you tick: your level, your Spirit and the items you already have.",
   start="Start the guide", cont="Continue from level", other="Português", other_href="index.html", self_suffix="en.html",
   sf=dict(cls="Huntress · Spirit Walker", name="The Mighty Silverfist Trail", pitch="Companion zoo: the Mighty Silverfist monkey carries the damage with Chober Chaber and The Catha's Balance.",
           facts=["Style: companions and minions (1–2 buttons)", "Turning point: capturing the monkey in Act 3", "Endgame: Sylvan's Effigy, auras and Azmerian Wolf", "Based on Mattjestic's guide"]),
   orc=dict(cls="Druid · Oracle", name="The Oracle of Totems", pitch="Spell Totems casting Spark and later Grim Pillars + Bitter Dead, with mana turning into damage and defence (Archmage, Mind Over Matter).",
           facts=["Style: totems and spells (2 buttons)", "Turning point: Spell Totem swap at the end of Act 4", "Endgame: Grim Pillars, Archmage and Soul Mantle", "Based on Lowepe's guide"]),
   both="Both: PT/EN · route 1→100 · tree that follows your level · My character with recommendations · When to use each piece · spreadsheet in the repo.",
   foot="Fan project, not affiliated with Grinding Gear Games. Game data: Path of Building; prices: poe.ninja."),
}
from landing_v2 import render
for l, fn in (("pt", "index.html"), ("en", "en.html")):
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(render(l, TXT[l], IC))
print("landing ok", {k: len(v) for k, v in IC.items()})
