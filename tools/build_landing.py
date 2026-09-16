# -*- coding: utf-8 -*-
"""Página inicial (escolha de build): ../index.html (PT) e ../en.html (EN)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..")
SF = json.load(open(os.path.join(HERE, "assets.json"), encoding="utf-8"))
OR = json.load(open(os.path.join(HERE, "oracle", "assets.json"), encoding="utf-8"))
def ico(A, table, name):
    k = A[table].get(name); return A["icons"].get(k, "") if k else ""
IC = {
 "sf_main": ico(SF, "gemIcon", "Tame Beast"), "sf_a": ico(SF, "uniqIcon", "Chober Chaber"), "sf_b": ico(SF, "uniqIcon", "Sylvan's Effigy"), "sf_c": ico(SF, "gemIcon", "Pain Offering"),
 "or_main": ico(OR, "gemIcon", "Spell Totem"), "or_a": ico(OR, "supIcon", "Grim Pillars"), "or_b": ico(OR, "gemIcon", "Archmage"), "or_c": ico(OR, "uniqIcon", "Soul Mantle"),
}
TXT = {
 "pt": dict(lang="pt-BR", title="Grimório de Builds · PoE 2", eyebrow="Path of Exile 2 · 0.5.5 · Forbidden Rites", h1="Grimório de Builds",
   lead="Escolha a build. Cada guia vai do nível 1 ao 100, explica cada gem, support, item e passiva, e se adapta ao que você marca: seu nível, seu Spirit e os itens que você já tem.",
   start="Começar o guia", cont="Continuar do nível", other="English", other_href="en.html", self_suffix="index.html",
   sf=dict(cls="Huntress · Spirit Walker", name="A Trilha do Mighty Silverfist", pitch="Zoo de companions: o macaco Mighty Silverfist carrega o dano com Chober Chaber e The Catha's Balance.",
           facts=["Estilo: companions e minions (1–2 botões)", "Virada: captura do macaco no Ato 3", "Endgame: Sylvan's Effigy, auras e Azmerian Wolf", "Base: guia do Mattjestic"]),
   orc=dict(cls="Druid · Oracle", name="O Oráculo dos Totems", pitch="Spell Totems lançando Spark e depois Grim Pillars + Bitter Dead, com mana virando dano e defesa (Archmage, Mind Over Matter).",
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
def card(key, x, folder, prefix, main, a, b, c, tt):
    return f"""<article class="card {key}">
  <div class="art"><div class="orb"><img src="{main}" alt=""></div><div class="sat s1"><img src="{a}" alt=""></div><div class="sat s2"><img src="{b}" alt=""></div><div class="sat s3"><img src="{c}" alt=""></div></div>
  <div class="body">
    <span class="cls">{x['cls']}</span>
    <h2>{x['name']}</h2>
    <p class="pitch">{x['pitch']}</p>
    <ul>{''.join(f'<li>{f}</li>' for f in x['facts'])}</ul>
    <div class="cta"><a class="go" href="{folder}/{tt['self_suffix']}" data-prefix="{prefix}"><span class="lbl">{tt['start']}</span><span class="arr">→</span></a>
      <a class="alt" href="{folder}/{'en.html' if tt['self_suffix'] == 'index.html' else 'index.html'}">{tt['other']}</a></div>
  </div>
</article>"""
def page(l):
    tt = TXT[l]
    return f"""<!doctype html>
<html lang="{tt['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{tt['title']}</title>
<meta name="description" content="{tt['lead']}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📜</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Alegreya+SC:wght@500;700&family=Alegreya:ital,wght@0,400;0,500;1,400&display=swap">
<style>
:root{{--bg:#07070a;--text:#ddd3c0;--mute:#9a907f;--edge:#2d2a26;color-scheme:dark}}
*{{box-sizing:border-box}}
html,body{{margin:0;background:var(--bg);color:var(--text)}}
body{{font-family:"Alegreya",Georgia,serif;font-size:17px;line-height:1.55;min-height:100vh;padding:0 16px;
  background:radial-gradient(900px 600px at 15% -10%,rgba(200,165,106,.12),transparent 60%),radial-gradient(900px 600px at 85% 110%,rgba(120,150,255,.12),transparent 60%),var(--bg)}}
.wrap{{max-width:1180px;margin:0 auto;padding:40px 0 60px}}
header{{display:flex;flex-wrap:wrap;align-items:flex-end;gap:16px 24px;margin-bottom:34px}}
header .t{{flex:1 1 520px}}
.eyebrow{{font-family:"Alegreya SC",Georgia,serif;letter-spacing:.14em;font-size:.82rem;color:var(--mute)}}
h1{{font-family:"Cinzel",Georgia,serif;font-weight:900;font-size:clamp(2.2rem,5vw,3.6rem);margin:.15em 0 .2em;letter-spacing:.04em;
  background:linear-gradient(90deg,#ebd29a,#f4ead2 45%,#bcd3ff);-webkit-background-clip:text;background-clip:text;color:transparent}}
.lead{{margin:0;max-width:760px;color:#cfc4ae}}
.lang{{display:inline-flex;border:1px solid #5a4832}}
.lang a{{padding:6px 14px;font-family:"Alegreya SC",Georgia,serif;font-weight:700;text-decoration:none;color:var(--mute)}}
.lang a.on{{background:#c8a56a;color:#120d07}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr));gap:24px}}
.card{{position:relative;border:1px solid var(--edge);background:linear-gradient(180deg,var(--c1),var(--c0));padding:22px;display:grid;grid-template-columns:150px 1fr;gap:20px;
  box-shadow:0 20px 50px rgba(0,0,0,.45);transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s,border-color .35s;overflow:hidden}}
.card::before{{content:"";position:absolute;inset:-40% -20% auto auto;width:360px;height:360px;background:radial-gradient(circle,var(--glow),transparent 65%);opacity:.55;transition:opacity .35s;pointer-events:none}}
.card:hover{{transform:translateY(-4px);border-color:var(--acc);box-shadow:0 26px 60px rgba(0,0,0,.55),0 0 0 1px var(--acc)}}
.card:hover::before{{opacity:.9}}
.sf{{--c0:#0c0a08;--c1:#1a1510;--acc:#c8a56a;--acc2:#7fd8b0;--glow:rgba(200,165,106,.35)}}
.orc{{--c0:#07091a;--c1:#111732;--acc:#9fb8e8;--acc2:#6fe3e0;--glow:rgba(120,150,255,.38)}}
.art{{position:relative;width:150px;height:150px}}
.orb{{position:absolute;inset:14px;border-radius:50%;border:1px solid var(--acc);display:grid;place-items:center;background:radial-gradient(circle,rgba(255,255,255,.06),rgba(0,0,0,.5));box-shadow:0 0 30px var(--glow)}}
.orb img{{width:74px;height:74px;object-fit:contain;filter:drop-shadow(0 4px 10px #000)}}
.sat{{position:absolute;width:44px;height:44px;border:1px solid var(--edge);background:#0b0b10;display:grid;place-items:center;animation:float 6s ease-in-out infinite}}
.sat img{{width:34px;height:34px;object-fit:contain}}
.s1{{left:0;top:0}}.s2{{right:0;top:18px;animation-delay:-2s}}.s3{{left:18px;bottom:0;animation-delay:-4s}}
@keyframes float{{50%{{transform:translateY(-6px)}}}}
.cls{{font-family:"Alegreya SC",Georgia,serif;letter-spacing:.12em;font-size:.82rem;color:var(--acc2)}}
.card h2{{font-family:"Cinzel",Georgia,serif;font-weight:700;font-size:1.55rem;margin:.1em 0 .35em;color:var(--acc);letter-spacing:.03em}}
.pitch{{margin:0 0 10px}}
.card ul{{margin:0 0 16px;padding-left:18px;color:#cabfa9;font-size:.95rem;display:grid;gap:3px}}
.card li::marker{{color:var(--acc)}}
.cta{{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px}}
.go{{display:inline-flex;align-items:center;gap:10px;padding:10px 18px;border:1px solid var(--acc);color:#0b0906;background:var(--acc);font-family:"Alegreya SC",Georgia,serif;font-weight:700;text-decoration:none;transition:gap .25s}}
.go:hover{{gap:16px}}
.alt{{color:var(--mute);font-family:"Alegreya SC",Georgia,serif;text-decoration:none;border-bottom:1px dotted var(--mute)}}
.alt:hover{{color:var(--text)}}
.both{{margin:28px 0 0;padding:14px 16px;border:1px solid var(--edge);color:#cfc4ae;background:rgba(255,255,255,.02)}}
footer{{margin-top:26px;color:var(--mute);font-size:.88rem}}
footer a{{color:var(--mute)}}
@media (max-width:560px){{.card{{grid-template-columns:1fr}}.art{{margin:0 auto}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style>
</head>
<body>
<div class="wrap">
  <header><div class="t"><div class="eyebrow">{tt['eyebrow']}</div><h1>{tt['h1']}</h1><p class="lead">{tt['lead']}</p></div>
    <nav class="lang" aria-label="Idioma / Language"><a href="index.html" class="{'on' if l == 'pt' else ''}" hreflang="pt-BR">Português</a><a href="en.html" class="{'on' if l == 'en' else ''}" hreflang="en">English</a></nav></header>
  <main class="grid">
    {card("sf", tt["sf"], "silverfist", "silverfist2:", IC["sf_main"], IC["sf_a"], IC["sf_b"], IC["sf_c"], tt)}
    {card("orc", tt["orc"], "oracle", "oracle1:", IC["or_main"], IC["or_a"], IC["or_b"], IC["or_c"], tt)}
  </main>
  <p class="both">{tt['both']}</p>
  <footer>{tt['foot']} · <a href="https://github.com/Genezera/trilha-silverfist" target="_blank" rel="noopener">GitHub</a></footer>
</div>
<script>
document.querySelectorAll(".go[data-prefix]").forEach(a => {{
  try {{ const v = localStorage.getItem(a.dataset.prefix + "lv"); if (v !== null) a.querySelector(".lbl").textContent = {json.dumps(tt['cont'])} + " " + JSON.parse(v); }} catch (e) {{}}
}});
</script>
</body>
</html>
"""
for l, fn in (("pt", "index.html"), ("en", "en.html")):
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(page(l))
print("landing ok", {k: len(v) for k, v in IC.items()})
