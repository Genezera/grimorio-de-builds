# -*- coding: utf-8 -*-
"""Gera tools/builds/<bid>/app_template.html a partir do template do Oracle, trocando tudo que é específico da build
por textos de D.ui (dados da build) e pelos blocos char.js / adapt.js / mech.js da pasta da build.
Uso: python kpatch.py <bid>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
sys.path.insert(0, HERE)
import common

BID = sys.argv[1]
B = common.load_build(BID)
BDIR = os.path.join(ROOT, "builds", BID)
t = open(os.path.join(ROOT, "oracle", "app_template.html"), encoding="utf-8").read()
J = lambda f: open(os.path.join(BDIR, f) if os.path.exists(os.path.join(BDIR, f)) else os.path.join(HERE, "js", f), encoding="utf-8").read()


def rep(a, b, count=1):
    global t
    assert a in t, "NOT FOUND: " + a[:120]
    t = t.replace(a, b, count)


def line(marker, new):
    global t
    lines = t.split("\n"); hits = [i for i, l in enumerate(lines) if marker in l]
    assert len(hits) == 1, f"marker {marker[:60]!r} hits {len(hits)}"
    lines[hits[0]] = new; t = "\n".join(lines)


def block(start, end, new):
    global t
    i = t.index(start); j = t.index(end, i)
    t = t[:i] + new.rstrip() + "\n" + t[j:]


C = B.CONFIG
# ------------------------------------------------------------------ cabeçalho, fontes, storage
rep("family=Cinzel+Decorative:wght@700;900&family=Marcellus&family=Marcellus+SC&family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;600",
    C["fonts"] + "&family=IBM+Plex+Mono:wght@400;600")
rep('<span class="pill">Druid · Oracle</span>', '<span class="pill">__PILL__</span>')
rep('localStorage.getItem("oracle1:" + k)', f'localStorage.getItem("{C["store"]}:" + k)')
rep('localStorage.setItem("oracle1:" + k, JSON.stringify(v))', f'localStorage.setItem("{C["store"]}:" + k, JSON.stringify(v))')
rep('<section class="view" id="v-totem"></section>', '<section class="view" id="v-mech"></section>')
rep("totem: vTotem,", "mech: vMech,")
line("const TREE_ORDER = [", "const TREE_ORDER = D.treeOrder;")
t = t.replace('["I", "II", "III", "IV", "V", "VI"][i]', '["I", "II", "III", "IV", "V", "VI", "VII", "VIII"][i]')

# ------------------------------------------------------------------ blocos JS específicos
block("/* ------------------------------------------------ meu personagem: checklist + recomendações automáticas (Oracle) */",
      "/* ------------------------------------------------ quando usar */", J("char.js") + "\n" + J("adapt.js") + "\n" + J("mech.js"))

# ------------------------------------------------------------------ building blocks
rep("const carry = /^Spell Totem/.test(g.skill);", "const carry = !!D.ui.carry && new RegExp(D.ui.carry).test(g.skill);")
rep('<small>${T("TOTEMS", "TOTEMS")}</small>', "<small>${esc(D.ui.box)}</small>")
rep('${T(`Com ${p.spiritTotal} de Spirit máximo, totems e skills persistentes reservam ≈ ${p.spiritUsed}. Malice e Spellslinger não têm custo nos dados: digite em Meu personagem. Cartões marcados como "não cabe" são os primeiros a sair.`, `With ${p.spiritTotal} max Spirit, totems and persistent skills reserve ≈ ${p.spiritUsed}. Malice and Spellslinger have no cost in the data: type it in My character. Cards marked "doesn\'t fit" are the first to go.`)}',
    '${T(`Com ${p.spiritTotal} de Spirit máximo, as skills persistentes reservam ≈ ${p.spiritUsed}. Cartões marcados como "não cabe" são os primeiros a sair.`, `With ${p.spiritTotal} max Spirit, persistent skills reserve ≈ ${p.spiritUsed}. Cards marked "doesn\'t fit" are the first to go.`)}')
rep('${T(`Volcano e Frost Bomb já saíram da barra: você passou do nível ${u} e o Bonestorm assumiu.`, `Volcano and Frost Bomb are already off the bar: you\'re past level ${u} and Bonestorm took over.`)}',
    '${esc(D.ui.earlyGone.replace("{u}", u))}')
rep('${T(`Skills de início do Ato 1. Antes do boss do Ato 1 (nv ~${u}) o Bonestorm substitui os dois.`, `Act 1 starting skills. Before the Act 1 boss (lv ~${u}) Bonestorm replaces both.`)}',
    '${esc(D.ui.earlyNote.replace("{u}", u))}')

# ------------------------------------------------------------------ painel lateral
rep('${T("Totems", "Totems")}: <b>${esc(pa.skeletons.n)}</b>', '${esc(D.ui.box)}: <b>${esc(pa.skeletons.n)}</b>')
rep('${T("(totems + persistentes)", "(totems + persistent)")}', '${esc(D.ui.spiritWhat)}')
rep('<button class="btn" type="button" data-gotab="totem">${T("Abrir Totems & Mana", "Open Totems & Mana")}</button>', '<button class="btn" type="button" data-gotab="mech">${esc(D.ui.mechBtn)}</button>')

# ------------------------------------------------------------------ views
rep('<span>${T("Totems", "Totems")} ≈ ${pa.dmgSplit[1]}%</span>', '<span>${esc(D.ui.dmg2)} ≈ ${pa.dmgSplit[1]}%</span>')
line('Árvore real do patch 0.5.5 com o caminho do guia do Lowepe em cada fase.',
     '''  return `<div class="sechead"><div><h2>${T("Árvore de Passivas", "Passive Tree")}</h2><p>${esc(D.ui.treeIntro)} <b style="color:#8DA9D8">${T("Principal", "Main")}</b> · <b style="color:var(--set1)">Weapon Set I = ${esc(D.ui.set1)}</b> · <b style="color:var(--set2)">Weapon Set II = ${esc(D.ui.set2)}</b>. ${T("Contorno verde-claro = nó novo nesta fase.", "Light-green outline = new node this phase.")}</p></div></div>''')
rep('${T("Ascendência Oracle", "Oracle Ascendancy")}', '${T("Ascendência", "Ascendancy")} ${esc(D.ui.asc)}')
line('siga as linhas a partir do início da Druid.',
     '      <li>${T(`Abra a árvore (tecla P), busque o nome do notable na caixa "Search here" e siga as linhas a partir do início da ${D.ui.cls}.`, `Open the tree (P key), search the notable name in the "Search here" box and follow the lines from the ${D.ui.cls} start.`)}</li>')
line('No respec da troca para totem, compare com a fase anterior', '      <li>${esc(D.ui.respecTip)}</li>')
line('Nove fases do guia do Lowepe.', '''  return `<div class="sechead"><div><h2>${T("Rota 1 → 100", "Route 1 → 100")}</h2><p>${esc(D.ui.routeIntro)}</p></div></div>''')
rep('${T("Dano seu / dos totems (aprox.)", "Your damage / totem damage (approx.)")}', '${esc(D.ui.dmgBar)}')
rep('${T("dano dos totems (proporção aproximada)", "totem damage (approximate ratio)")}', '${esc(D.ui.dmgLegend)}')
line('<div class="panel frame"><h3>${T("Prioridade de sockets (Jeweller\'s)", "Socket priority (Jeweller\'s)")}</h3>',
     '''    <div class="panel frame"><h3>${T("Prioridade de sockets (Jeweller's)", "Socket priority (Jeweller's)")}</h3><ul class="clean gold">${D.ui.socketPrio.map(x => `<li>${esc(x)}</li>`).join("")}</ul></div>''')
if os.path.exists(os.path.join(BDIR, "view_skills.js")):
    block("function vSkills() {", "function vGear() {", J("view_skills.js"))
line("Nada disso volta depois. Cada Spirit conta para os totems", '''  return `<div class="sechead"><div><h2>${T("Recompensas permanentes", "Permanent rewards")}</h2><p>${esc(D.ui.permIntro)}</p></div>''')
line('<h3>${T("Grim Pillars no Atlas", "Grim Pillars in the Atlas")}</h3>',
     '''  <div class="grid g2" style="margin-top:16px">${D.ui.atlasCards.map(([h, b]) => `<div class="panel frame"><h3>${esc(h)}</h3><p style="margin:0">${esc(b)}</p></div>`).join("")}</div>`;''')
line('$("#foot").textContent =', '$("#foot").textContent = D.ui.foot + ` · ${D.patch} · ${D.updated}. ` + T("Seu progresso fica salvo neste navegador.", "Your progress is saved in this browser.");')

# ------------------------------------------------------------------ tema: acentos inline do Oracle → paleta da build (as variáveis vêm de poe2.css)
t = t.replace("</style>", "\n" + C.get("css", "") + "\n</style>", 1)
for a, b in C.get("recolor", {}).items():
    t = t.replace(a, b)

leftover = [w for w in ("Lowepe", "Spell Totem", "totemCalc", "Grim Pillars", "Druid") if w in t]
assert not leftover, f"sobras do Oracle: {leftover}"
exec(open(os.path.join(HERE, "gearopts_patch.py"), encoding="utf-8").read())      # ranking por nível (com opts) e linhas travadas por nível (sem opts)
open(os.path.join(BDIR, "app_template.html"), "w", encoding="utf-8").write(t)
print(BID, "template ok", len(t))
