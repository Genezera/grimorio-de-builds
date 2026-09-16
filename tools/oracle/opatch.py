# -*- coding: utf-8 -*-
"""Gera tools/oracle/app_template.html a partir do template do Silverfist, trocando o que é específico da build."""
import os, re, colorsys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
t = open(os.path.join(ROOT, "app_template.html"), encoding="utf-8").read()
J = lambda f: open(os.path.join(HERE, f), encoding="utf-8").read()

def rep(a, b, count=1):
    global t
    assert a in t, "NOT FOUND: " + a[:90]
    t = t.replace(a, b, count)

def line(marker, new):
    global t
    lines = t.split("\n"); hits = [i for i, l in enumerate(lines) if marker in l]
    assert len(hits) == 1, f"marker {marker[:60]!r} hits {len(hits)}"
    lines[hits[0]] = new; t = "\n".join(lines)

def block(start, end, new):
    global t
    i = t.index(start); j = t.index(end, i)
    t = t[:i] + new + "\n" + t[j:]

# ------------------------------------------------------------------ cabeçalho, fontes, storage
rep("<title>Trilha do Silverfist</title>", "<title>__TITLE__</title>")
rep('content="Guia interativo Spirit Walker / Mighty Silverfist — PoE 2 Forbidden Rites"', 'content="__DESC__"')
rep("family=Cinzel:wght@500;700;900&family=Alegreya+SC:wght@400;500;700&family=Alegreya:ital,wght@0,400;0,500;0,700;1,400&family=IBM+Plex+Mono:wght@400;600",
    "family=Cinzel+Decorative:wght@700;900&family=Marcellus&family=Marcellus+SC&family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;600")
rep('--display:"Cinzel","Trajan Pro",Georgia,serif;', '--display:"Marcellus","Cinzel","Trajan Pro",Georgia,serif;')
rep('--ui:"Alegreya SC","Palatino Linotype",Georgia,serif;', '--ui:"Marcellus SC","Palatino Linotype",Georgia,serif;')
rep('--body:"Alegreya","Palatino Linotype",Georgia,serif;', '--body:"Spectral","Palatino Linotype",Georgia,serif;')
rep('<span class="pill">Huntress · Spirit Walker</span>', '<span class="pill">Druid · Oracle</span>')
line("<h1><small>Rota Chober Chaber · guia Mattjestic explicado</small>", '        <h1 class="orh1"><small>__H1S__</small>__H1__</h1>')
line("<p>Spear no começo, o macaco no Ato 3", "        <p>__LEAD__</p>")
rep('localStorage.getItem("silverfist2:" + k)', 'localStorage.getItem("oracle1:" + k)')
rep('localStorage.setItem("silverfist2:" + k, JSON.stringify(v))', 'localStorage.setItem("oracle1:" + k, JSON.stringify(v))')

# ------------------------------------------------------------------ abas e views
line("const TABS = [", 'const TABS = __TABS__;')
line("const VIEWS = {", "const VIEWS = { meu: vMeu, quando: vQuando, totem: vTotem, uniques: vUniques, agora: vAgora, arvore: vArvore, rota: vRota, skills: vSkills, gear: vGear, asc: vAsc, quests: vQuests, tricks: vTricks, atlas: vAtlas, diag: vDiag, fontes: vFontes };")
rep('<section class="view" id="v-caca"></section>', '<section class="view" id="v-totem"></section>')

# blocos específicos do Silverfist → Oracle
block("/* ------------------------------------------------ meu personagem: checklist + recomendações automáticas */", "/* ------------------------------------------------ adaptar ao meu personagem */", J("ochar.js"))
block("/* ------------------------------------------------ adaptar ao meu personagem */", "/* ------------------------------------------------ caçar companions */", J("oadapt.js"))
block("/* ------------------------------------------------ caçar companions */", "/* ------------------------------------------------ quando usar */", J("ototem.js"))
block("/* ---- spirit */", "function vAsc() {", "/* ---- spirit: ver Totems & Mana */")
rep("""function qStatus(e) {""", """function qStatus(e) {
  const key = TIMING_KEY[e.n] || e.n; const owned = !!(S.ch.own || {})[key];
  if (e.lvl == null) return { k: owned ? "have" : "unknown", t: T("Confira o requisito no item", "Check the requirement on the item"), owned };
  if (e.lvl > S.lv) return { k: "lock", t: T(`Nível ${e.lvl} — faltam ${e.lvl - S.lv}`, `Level ${e.lvl} — ${e.lvl - S.lv} to go`), owned };
  return { k: owned ? "have" : "ok", t: owned ? T("Você já tem", "You have it") : T("Já pode usar", "Usable now"), owned };
}
function qStatusOld(e) {""")

# ------------------------------------------------------------------ building blocks
rep("const carry = /Silverfist|Zekoa|Azmerian/.test(g.skill);", "const carry = /^Spell Totem/.test(g.skill);")
rep("<small>ESQUELETOS</small>", "<small>${T(\"TOTEMS\", \"TOTEMS\")}</small>")
line("mainHtml = skelBox(p) + (p.spiritTotal ?", """    mainHtml = skelBox(p) + (p.spiritTotal ? `<div class="spnote frame"><b>${T("Seu Spirit", "Your Spirit")}</b><p>${T(`Com ${p.spiritTotal} de Spirit máximo, totems e skills persistentes reservam ≈ ${p.spiritUsed}. Malice e Spellslinger não têm custo nos dados: digite em Meu personagem. Cartões marcados como "não cabe" são os primeiros a sair.`, `With ${p.spiritTotal} max Spirit, totems and persistent skills reserve ≈ ${p.spiritUsed}. Malice and Spellslinger have no cost in the data: type it in My character. Cards marked "doesn't fit" are the first to go.`)}</p></div>` : "") + `${p.spiritNote ? `<div class="spnote frame"><b>Spirit</b><p>${esc(p.spiritNote)}</p></div>` : ""}` +""")
rep('"companions e auras"', 'T("skills persistentes", "persistent skills")')
line("return `<div class=\"label\" style=\"margin:0 0 8px\">Barra principal${useLv", """  return `<div class="label" style="margin:0 0 8px">${T("Barra principal", "Main bar")}${useLv ? "" : T(` (nv ${u}+)`, ` (lv ${u}+)`)}</div>${mainHtml}` +""")
line("(hideEarly ? `<p style=\"color:var(--faint);margin:12px 0 0\">Twister, Whirling Slash", """    (hideEarly ? `<p style="color:var(--faint);margin:12px 0 0">${T(`Volcano e Frost Bomb já saíram da barra: você passou do nível ${u} e o Bonestorm assumiu.`, `Volcano and Frost Bomb are already off the bar: you're past level ${u} and Bonestorm took over.`)}</p>`""")
line(": `<div class=\"panel frame\" style=\"margin-top:16px;border-color:rgba(224,102,79,.45)\"><h3>Só até capturar o Silverfist", """      : `<div class="panel frame" style="margin-top:16px;border-color:rgba(224,102,79,.45)"><h3>${T(`Só no começo (nv ${p.lv[0]}–${u - 1})`, `Early only (lv ${p.lv[0]}–${u - 1})`)}</h3><p style="margin:0 0 12px;color:var(--mute)">${T(`Skills de início do Ato 1. Antes do boss do Ato 1 (nv ~${u}) o Bonestorm substitui os dois.`, `Act 1 starting skills. Before the Act 1 boss (lv ~${u}) Bonestorm replaces both.`)}</p><div class="gems">${early.map(g => gemCard(g, null, detailed)).join("")}</div></div>`);""")

# ------------------------------------------------------------------ painel lateral
rep('title="${esc(pa.skeletons.note)}">Esqueletos: <b>', 'title="${esc(pa.skeletons.note)}">${T("Totems", "Totems")}: <b>')
rep('${T("(companions estimados)", "(estimated companions)")}', '${T("(totems + persistentes)", "(totems + persistent)")}')
rep('<button class="btn" type="button" data-gotab="zoo">Abrir planner de Spirit</button>', '<button class="btn" type="button" data-gotab="totem">${T("Abrir Totems & Mana", "Open Totems & Mana")}</button>')

# ------------------------------------------------------------------ views
rep("<span>Zoo ≈ ${p.dmgSplit[1]}%</span>", "<span>${T(\"Totems\", \"Totems\")} ≈ ${p.dmgSplit[1]}%</span>")
rep('${A.sets[p.id] ? "Set principal desta fase" : "Set de leveling (spear)"}', '${T("Set principal desta fase", "Main set this phase")}')
line("const OPT_PHASE = {", "const OPT_PHASE = {};")
line("const TREE_ORDER = [", 'const TREE_ORDER = ["a1", "a2", "a3", "a4", "sw", "int", "ea", "w1", "fin", "uber"];')
rep('const name = pid === "uber" ? "Bossing (endgame)" : D.phases.find(p => p.id === pid).name;', 'const name = (D.phases.find(p => p.id === pid) || D.phases[D.phases.length - 1]).name;')
line("return `<div class=\"sechead\"><div><h2>Árvore de Passivas</h2><p>Árvore real do patch 0.5.5", """  return `<div class="sechead"><div><h2>${T("Árvore de Passivas", "Passive Tree")}</h2><p>${T("Árvore real do patch 0.5.5 com o caminho do guia do Lowepe em cada fase. Atos 1–4: spells físicos e Wildsurge Incantation. Troca: Ancestral Bond, Efficient Inscriptions e nós de totem. Endgame: mana e Mind Over Matter.", "Real patch 0.5.5 tree with Lowepe's guide path for each phase. Acts 1–4: physical spells and Wildsurge Incantation. Swap: Ancestral Bond, Efficient Inscriptions and totem nodes. Endgame: mana and Mind Over Matter.")} <b style="color:#E3BE78">${T("Principal", "Main")}</b> · <b style="color:var(--set1)">Weapon Set I = ${T("totem", "totem")}</b> · <b style="color:var(--set2)">Weapon Set II = ${T("o resto", "everything else")}</b>. ${T("Contorno verde-claro = nó novo nesta fase.", "Light-green outline = new node this phase.")}</p></div></div>""")
rep('${phaseSel(pid, "tree", [["uber", "Bossing (endgame)"]])}', '${phaseSel(pid, "tree")}')
line('Notables do meta (% dos 24 zoos top) — contorno roxo na árvore</p>', """      ${A.metaNotables.length ? `<div class="divider"></div><p class="label" style="padding:0 6px">${T("Notables do meta", "Meta notables")}</p>` : ""}""")
rep('<div class="plate">Ascendência Spirit Walker</div>', '<div class="plate">${T("Ascendência Oracle", "Oracle Ascendancy")}</div>')
line('<li>Abra a árvore (tecla P), busque o nome do notable', '      <li>${T("Abra a árvore (tecla P), busque o nome do notable na caixa \\"Search here\\" e siga as linhas a partir do início da Druid.", "Open the tree (P key), search the notable name in the \\"Search here\\" box and follow the lines from the Druid start.")}</li>')
line("<li>Nos respecs (Ato 3 e ao pegar Sylvan's Effigy)", """      <li>${T("No respec da troca para totem, compare com a fase anterior: nós sem contorno verde já eram seus. Weapon Set 1 = passivas de totem.", "At the totem-swap respec, compare with the previous phase: nodes without a green outline were already yours. Weapon Set 1 = totem passives.")}</li>""")
line("return `<div class=\"sechead\"><div><h2>Rota 1 → 100</h2>", """  return `<div class="sechead"><div><h2>${T("Rota 1 → 100", "Route 1 → 100")}</h2><p>${T("Nove fases do guia do Lowepe. Até o Ato 4 você lança os spells; na troca, o dano passa para os Spell Totems.", "Nine phases from Lowepe's guide. Until Act 4 you cast the spells; at the swap, damage moves to the Spell Totems.")}</p></div></div>""")
rep('title="Dano seu / do zoo (aprox.)"', 'title="${T("Dano seu / dos totems (aprox.)", "Your damage / totem damage (approx.)")}"')
line("<p style=\"color:var(--faint);font-size:.88rem;margin:6px 0 20px\">Barra: <span", """  <p style="color:var(--faint);font-size:.88rem;margin:6px 0 20px">${T("Barra", "Bar")}: <span style="color:#bdbdbd">■</span> ${T("dano seu", "your damage")} · <span style="color:var(--wisp)">■</span> ${T("dano dos totems (proporção aproximada)", "totem damage (approximate ratio)")}.</p>""")
line("<div class=\"panel frame\"><h3>Prioridade de sockets (Jeweller's)</h3>", """    <div class="panel frame"><h3>${T("Prioridade de sockets (Jeweller's)", "Socket priority (Jeweller's)")}</h3><ul class="clean gold"><li>Spell Totem (Urgent Totems III ${T("primeiro", "first")})</li><li>Entangle</li><li>Archmage · Mana Remnants</li><li>Frost Bomb · Mana Tempest</li></ul></div>""")
line('<p style="color:var(--mute);margin:12px 0 0">${A.sets[sel.id] ? `Set principal da nossa rota no modo', '  <p style="color:var(--mute);margin:12px 0 0">${T(`Set principal da fase no modo <b>${S.mode === "cheap" ? "barato" : "completo"}</b>: rares com +níveis de spell, Spirit, mana e resistências. Troque o modo no topo para ver o outro set.`, `Main phase set in <b>${S.mode === "cheap" ? "budget" : "full"}</b> mode: rares with +spell levels, Spirit, mana and resistances. Switch the mode at the top to see the other set.`)}</p><div class="items stagger" style="margin-top:14px">${setItems(sel.id).map(itemCard).join("")}</div>')
line("const unlocked = [20, 33, 65, 75]; const allAsc = A.notables.uber.asc;", "  const unlocked = D.ascUnlock; const allAsc = A.notables.uber.asc;")
t = t.replace('["I", "II", "III", "IV"][i]', '["I", "II", "III", "IV", "V", "VI"][i]')
rep('${["I", "II", "III", "IV", "V", "VI"][i]} ascensão</span>', '${["I", "II", "III", "IV", "V", "VI"][i]}</span>')
line("return `<div class=\"sechead\"><div><h2>Recompensas permanentes</h2>", """  return `<div class="sechead"><div><h2>${T("Recompensas permanentes", "Permanent rewards")}</h2><p>${T("Nada disso volta depois. Cada Spirit conta para os totems (75 por totem) e os Weapon Set Points alimentam as passivas de totem no Set 1.", "None of this comes back later. Every Spirit counts for totems (75 per totem) and Weapon Set Points fuel the totem passives on Set 1.")}</p></div>""")
line('<h2 style="font-size:1.4rem">Árvore do Atlas (guia T15+)</h2>', "")
line('<div class="atlasgrp stagger">${Object.entries(D.atlas)', """  <div class="grid g2" style="margin-top:16px"><div class="panel frame"><h3>${T("Grim Pillars no Atlas", "Grim Pillars in the Atlas")}</h3><p style="margin:0">${T("Grim Pillars, Bitter Dead e Repulsion são skills de Runic Ward. No 0.5.5, Remnants e Expedition começam no Ato 4. Rode esses conteúdos no início do Atlas para conseguir as gems e as peças Runeforged.", "Grim Pillars, Bitter Dead and Repulsion are Runic Ward skills. In 0.5.5, Remnants and Expedition start in Act 4. Run that content early in the Atlas to get the gems and the Runeforged pieces.")}</p></div><div class="panel frame"><h3>${T("Totems nos mapas", "Totems in maps")}</h3><p style="margin:0">${T("2 totems bastam para mapear (Lowepe). No boss, coloque todos e desligue o Mana Remnants se precisar de Spirit para mais um.", "2 totems are enough for mapping (Lowepe). On bosses, place all of them and turn off Mana Remnants if you need Spirit for one more.")}</p></div></div>`;""")
line('<h2 style="font-size:1.4rem">Seu setup atual</h2>', "  `;")
line('<div class="setup stagger">${D.current.items.map', "")
line("return `<div class=\"sechead\"><div><h2>Uniques da build</h2>", """  return `<div class="sechead"><div><h2>${T("Uniques da build", "Build uniques")}</h2><p>${T(`${D.uniques.length} uniques com mods e preço da liga ${esc(D.league)} (poe.ninja, ${esc(D.snap)}). Os marcados como fora do guia são alternativas. Borda verde = já vale para o seu nível e modo.`, `${D.uniques.length} uniques with mods and ${esc(D.league)} league prices (poe.ninja, ${esc(D.snap)}). The ones marked as outside the guide are alternatives. Green border = already relevant for your level and mode.`)}</p></div></div>""")
block('  <div class="sechead" style="margin-top:28px"><div><h2 style="font-size:1.4rem">Idols e soul cores</h2>', "function barList(rows, withIcons) {", "`;\n}")
line("$(\"#foot\").textContent =", """$("#foot").textContent = T(`Guia baseado no build do Lowepe (Mobalytics), dados de jogo do Path of Building e preços do poe.ninja · ${D.patch} · ${D.updated}. Seu progresso fica salvo neste navegador.`, `Guide based on Lowepe's build (Mobalytics), Path of Building game data and poe.ninja prices · ${D.patch} · ${D.updated}. Your progress is saved in this browser.`);""")
rep('"167,123,224" : i % 3 === 0 ? "235,210,154" : "127,216,176"', '"179,140,255" : i % 3 === 0 ? "210,226,255" : "111,227,224"')

# ------------------------------------------------------------------ tema de cores Oracle (noite estrelada: índigo, prata e ciano)
KEEP = {"#AF6025", "#E18C47", "#FFFF77", "#8888FF", "#1BA29B", "#D20000", "#D9544A", "#62B462", "#E0664F", "#ffb3a3", "#7a4a22", "#bdbdbd"}
def shift(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255); hd = h * 360
    if s < .06 and l < .25:
        h2, s2 = 228 / 360, .28
    elif 12 <= hd <= 62 and s >= .06:
        if l < .42: h2, s2 = 228 / 360, min(.5, s * 1.1 + .05)
        else: h2, s2, l = 218 / 360, max(.45, s * .75), min(.9, l + .02)
    elif 140 <= hd <= 170:
        h2, s2 = 181 / 360, s
    elif 260 <= hd <= 290:
        h2, s2 = 268 / 360, s
    else:
        return None
    rr, gg, bb = colorsys.hls_to_rgb(h2, l, s2)
    return round(rr * 255), round(gg * 255), round(bb * 255)
def hexrep(m):
    hx = m.group(0)
    if hx.upper() in {k.upper() for k in KEEP}: return hx
    v = hx[1:]
    if len(v) == 3: v = "".join(c * 2 for c in v)
    try: r, g, b = int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16)
    except ValueError: return hx
    s = shift(r, g, b)
    return hx if s is None else "#%02X%02X%02X" % s
def rgbarep(m):
    r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3)); s = shift(r, g, b)
    return m.group(0) if s is None else f"rgba({s[0]},{s[1]},{s[2]},{m.group(4)})"
style_end = t.index("</style>")
css, rest = t[:style_end], t[style_end:]
css = re.sub(r"#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b", hexrep, css)
css = re.sub(r"rgba\((\d+),(\d+),(\d+),([.\d]+)\)", rgbarep, css)
rest = re.sub(r'"#(E3BE78|C8A56A|EBD29A|7FD8B0|0e0c0a|120e0a|15110c|14110d|0b0907|0d0b09|1f1a14|221c15|2e271e|3b3124|2a241c|5a4a34|8a7b64|EBD29A)"', lambda m: '"' + hexrep(re.match(r"#[0-9A-Fa-f]+", "#" + m.group(1))) + '"', rest)
rest = re.sub(r'(style="[^"]*?)(#[0-9A-Fa-f]{6})', lambda m: m.group(1) + hexrep(re.match(r"#[0-9A-Fa-f]{6}", m.group(2))), rest)
t = css + rest
t = t.replace("</style>", """.orh1 small{color:#9FD8FF}
.console h1{text-shadow:0 0 24px rgba(159,216,255,.25)}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.5;background-image:radial-gradient(1px 1px at 12% 22%,#fff 50%,transparent 51%),radial-gradient(1px 1px at 67% 12%,#dfe8ff 50%,transparent 51%),radial-gradient(1.5px 1.5px at 84% 64%,#b8d8ff 50%,transparent 51%),radial-gradient(1px 1px at 32% 78%,#fff 50%,transparent 51%),radial-gradient(1px 1px at 51% 41%,#cfe0ff 50%,transparent 51%),radial-gradient(1.5px 1.5px at 7% 58%,#e6d8ff 50%,transparent 51%),radial-gradient(1px 1px at 93% 31%,#fff 50%,transparent 51%)}
.app{position:relative;z-index:1}
</style>""", 1)
open(os.path.join(HERE, "app_template.html"), "w", encoding="utf-8").write(t)
print("oracle template ok", len(t))
