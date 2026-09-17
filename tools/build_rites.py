# -*- coding: utf-8 -*-
"""Forbidden Rites challenges page: ../rites/index.html (PT) and ../rites/en.html (EN)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "rites"))
import rdata, rtext
sys.path.insert(0, HERE)
from enhance import asset_version
LV = (asset_version("loader.css"), asset_version("loader.js"))

OUT = os.path.join(HERE, "..", "rites")
os.makedirs(OUT, exist_ok=True)

UI = {
 "pt": dict(lang="pt-BR", title="Forbidden Rites · Guia das Challenges", desc="Guia completo das 8 challenges da liga Forbidden Rites (Path of Exile 2 0.5.5): o que cada uma pede, onde encontrar, o que usar e como fazer, com progresso salvo.",
   kicker="Path of Exile 2 · 0.5.5 · Liga de evento", h1a="Forbidden", h1b="Rites", sub="O grimório das 8 challenges",
   lead="Tudo o que cada challenge pede, onde encontrar cada Rite, cada Rare e cada chefe, quais Omens valem a pena e a ordem mais rápida — com o seu progresso salvo neste navegador.",
   start="Começar pela campanha", rewards="Recompensas da liga", progress="challenges concluídas", ends="A liga termina em", days="dias", ended="A liga terminou",
   totem="Cada challenge concluída adiciona uma peça ao Forbidden Rites Totem do seu hideout.", nav="Challenges", how="Como fazer", tips="Dicas e armadilhas", where="Onde encontrar",
   req="Requisito oficial", phase="Quando", effort="Esforço", done="Concluída", of="de", reset="Zerar progresso", resetq="Apagar todo o progresso desta página?",
   area="Área", boss="Chefe", reward="Recompensa", poi="Ponto de interesse", act="Ato", rite="Rite", allRite="Marcar Rite inteiro",
   trialPts="pontos", level="Seu nível", count="Uniques recebidos", omen="Omen", trigger="Como ativar", cost="Custo", used="Usado", hc="Hardcore (sem morrer)", nolow="Evitar Low Life",
   plan="Plano pelos preços disponíveis", partialCost="subtotal conhecido", incompletePlan="Plano incompleto: faltam opções com preço conhecido que atendam aos filtros", costScope="Estimativa do cache, sem atualização automática. Não inclui bases, Catalysts nem outros materiais de preparação. Confirme preços e requisitos antes de gastar.", planLeft="Faltam", planCost="custo estimado dos que faltam", total="Omen + currency que ativa", exch="Preços do poe.ninja (Forbidden Rites) em",
   tree="Árvore", points="pontos alocados", region="Região", key="Chave", drop="Drop marcante", unlock="Como liberar",
   mech="Mecânicas da liga", mechLead="O que é novo em Forbidden Rites e ajuda nas challenges.", chaos="Novidades do Trial of Chaos no 0.5.5",
   order="Ordem recomendada", orderSteps=["Campanha: The Riteseeker + The Hunter + 1ª e 2ª provas (The Ascendant).", "Primeiros mapas: The Nameless e The Reliquarian andam juntos nos altares de Ritual.", "Mapas médios: árvore de Ritual → Delirium → Abyss (The Cartographer) e 3ª prova.", "Mapas altos: prova final, nível 90 (The Master) e os 3 pinnacles (The Vanquisher)."],
   sources="Fontes", reviewed="Revisado em", fan="Projeto de fã, sem vínculo com a Grinding Gear Games. Arte e ícones © Grinding Gear Games.", builds="← Builds", other="English", otherHref="en.html",
   need="precisa de", rewardAt="com", locked="bloqueada", unlocked="desbloqueada", saved="Progresso salvo neste navegador", jump="Ir para"),
 "en": dict(lang="en", title="Forbidden Rites · Challenge Guide", desc="Complete guide to the 8 Forbidden Rites league challenges (Path of Exile 2 0.5.5): what each one requires, where to find everything, what to use and how to do it, with saved progress.",
   kicker="Path of Exile 2 · 0.5.5 · Event league", h1a="Forbidden", h1b="Rites", sub="The grimoire of the 8 challenges",
   lead="Everything each challenge asks for, where to find every Rite, every Rare and every boss, which Omens are worth it and the fastest order — with your progress saved in this browser.",
   start="Start with the campaign", rewards="League rewards", progress="challenges completed", ends="The league ends in", days="days", ended="The league has ended",
   totem="Every completed challenge adds a piece to the Forbidden Rites Totem in your hideout.", nav="Challenges", how="How to do it", tips="Tips and pitfalls", where="Where to find",
   req="Official requirement", phase="When", effort="Effort", done="Completed", of="of", reset="Reset progress", resetq="Erase all progress on this page?",
   area="Area", boss="Boss", reward="Reward", poi="Point of interest", act="Act", rite="Rite", allRite="Tick whole Rite",
   trialPts="points", level="Your level", count="Uniques received", omen="Omen", trigger="How to trigger", cost="Cost", used="Used", hc="Hardcore (no dying)", nolow="Avoid Low Life",
   plan="Plan using available prices", partialCost="known subtotal", incompletePlan="Incomplete plan: not enough priced options meet the filters", costScope="Cached estimate, not updated automatically. Excludes bases, Catalysts and other preparation materials. Check prices and requirements before spending.", planLeft="Remaining", planCost="estimated cost of the remaining ones", total="Omen + triggering currency", exch="poe.ninja prices (Forbidden Rites) on",
   tree="Tree", points="points allocated", region="Region", key="Key", drop="Notable drop", unlock="How to unlock",
   mech="League mechanics", mechLead="What is new in Forbidden Rites and helps with the challenges.", chaos="Trial of Chaos changes in 0.5.5",
   order="Recommended order", orderSteps=["Campaign: The Riteseeker + The Hunter + 1st and 2nd trials (The Ascendant).", "First maps: The Nameless and The Reliquarian progress together at Ritual altars.", "Mid maps: Ritual → Delirium → Abyss trees (The Cartographer) and the 3rd trial.", "High maps: final trial, level 90 (The Master) and the 3 pinnacles (The Vanquisher)."],
   sources="Sources", reviewed="Reviewed on", fan="Fan project, not affiliated with Grinding Gear Games. Art and icons © Grinding Gear Games.", builds="← Builds", other="Português", otherHref="index.html",
   need="needs", rewardAt="at", locked="locked", unlocked="unlocked", saved="Progress saved in this browser", jump="Jump to"),
}


def page(lang):
    u = UI[lang]
    d = rdata.data(lang)
    d["challenges"] = rdata.resolve(rtext.CHALLENGES, lang)
    safe = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    home = "../index.html" if lang == "pt" else "../en.html"
    return f"""<!doctype html>
<html lang="{u['lang']}" data-page="rites">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{u['title']}</title>
<meta name="description" content="{u['desc']}">
<meta name="theme-color" content="#07050c">
<link rel="icon" href="../shared/art/rites/ritual-node.webp">
<link rel="alternate" hreflang="pt-BR" href="index.html"><link rel="alternate" hreflang="en" href="en.html">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Cinzel+Decorative:wght@700;900&family=Alegreya+SC:wght@500;700&family=Crimson+Pro:ital,wght@0,400;0,500;0,600;1,400&display=swap">
<link rel="stylesheet" href="../shared/rites.css"><link rel="stylesheet" href="../shared/loader.css?v={LV[0]}"><script src="../shared/loader.js?v={LV[1]}"></script>
</head>
<body>
<a class="skip" href="#challenges">{u['jump']}: {u['nav']}</a>
<div class="void" aria-hidden="true"><div class="totem-bg"></div><div class="fog f1"></div><div class="fog f2"></div><canvas id="embers"></canvas><div class="vignette"></div></div>
<header class="top">
  <a class="homelink" href="{home}">{u['builds']}</a>
  <nav class="lang" aria-label="Idioma / Language"><a href="index.html" {'aria-current="page"' if lang == 'pt' else ''}>PT</a><a href="en.html" {'aria-current="page"' if lang == 'en' else ''}>EN</a></nav>
</header>
<main id="app"></main>
<noscript><p style="padding:24px;color:#e9dcc0">JavaScript</p></noscript>
<script>window.RITES={safe(d)};window.RT={safe(u)};</script>
<script src="../shared/rites.js"></script>
</body>
</html>
"""


for lang, fn in (("pt", "index.html"), ("en", "en.html")):
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(page(lang))
print("rites ok", {f: os.path.getsize(os.path.join(OUT, f)) for f in ("index.html", "en.html")})
