# Aba "Caçar companions"
t = open("app_template.html", encoding="utf-8").read()
def rep(a, b):
    global t
    assert a in t, "NOT FOUND: " + a[:80]
    t = t.replace(a, b, 1)
if "function vHunt" in t:
    raise SystemExit("already")
rep('<section class="view" id="v-quando"></section>', '<section class="view" id="v-quando"></section>\n    <section class="view" id="v-caca"></section>')
rep('["quando","Quando usar"],', '["quando","Quando usar"],["caca","Caçar companions"],')
rep("const VIEWS = { meu: vMeu, quando: vQuando,", "const VIEWS = { meu: vMeu, quando: vQuando, caca: vHunt,")
rep("/* ------------------------------------------------ quando usar */", r"""/* ------------------------------------------------ caçar companions */
S.hf = store.get("hf", "all");
function vHunt() {
  const H = D.hunt;
  const hasteTxt = h => h === "sim" ? `<span class="chip wisp">${T("Rola Haste", "Rolls Haste")}</span>` : h === "nao" ? `<span class="chip danger">${T("Não rola Haste", "No Haste")}</span>` : `<span class="chip">${T("Haste: não confirmado", "Haste: unconfirmed")}</span>`;
  const list = H.beasts.filter(b => S.hf === "all" || (S.hf === "haste" && b.haste === "sim") || (S.hf === "cheap" && b.cost <= 26.7) || (S.hf === "act" && !/Mapas|Maps/.test(b.where)) || (S.hf === "maps" && /Mapas|Maps/.test(b.where)));
  const est = pct => { const tot = +S.ch.spirit || 0; if (!tot) return ""; const eff = (S.ch.tk ? 1.3 : 1) * (1 + (S.ch.eg ? .25 : 0)); return ` · ≈ ${Math.round(pct / 100 * tot / eff)} Spirit`; };
  const tierName = { primary: T("Principais — capture por causa deles", "Primary — capture for these"), secondary: T("Secundários — bons junto com um principal", "Secondary — good alongside a primary"), tertiary: T("Terciários — só bônus", "Tertiary — just a bonus") };
  return `<div class="sechead"><div><h2>${T("Caçar companions", "Hunting companions")}</h2><p>${T("Como capturar, onde achar cada beast (campanha e mapas), truques de farm e quais modificadores procurar. O custo em Spirit usa o seu Spirit máximo de Meu personagem.", "How to capture, where to find each beast (campaign and maps), farming tricks and which modifiers to look for. Spirit cost uses your max Spirit from My character.")}</p></div></div>
  <div class="grid g2">
    <div class="panel frame"><h3>${T("Como capturar (passo a passo)", "How to capture (step by step)")}</h3><ol class="huntol">${H.steps.map(s => `<li>${esc(s)}</li>`).join("")}</ol></div>
    <div class="panel frame"><h3>${T("Rota mais rápida para auras T1 (Mattjestic)", "Fastest route for T1 auras (Mattjestic)")}</h3><div class="checklist">${H.route.map((r, i) => `<label class="check ${S.done["hunt:" + i] ? "done" : ""}"><input type="checkbox" data-key="hunt:${i}" ${S.done["hunt:" + i] ? "checked" : ""}><span><b class="ui">${esc(r.t)}</b><br>${esc(r.d)}</span></label>`).join("")}</div></div>
  </div>
  <div class="sechead" style="margin-top:26px"><div><h2 style="font-size:1.4rem">${T("Truques de farm", "Farming tricks")}</h2></div></div>
  <div class="qgrid">${H.tricks.map(x => `<article class="qcard frame"><h3 style="margin:0">${esc(x.t)}</h3><p style="margin:0">${esc(x.d)}</p></article>`).join("")}</div>
  <div class="sechead" style="margin-top:26px"><div><h2 style="font-size:1.4rem">${T("Onde achar cada beast", "Where to find each beast")}</h2><p>${T("Ordenado pelo menor custo de Spirit. Com o Effigy, junte auras T1 de TIPOS diferentes; antes dele, só cabe 1 beast de aura.", "Sorted by lowest Spirit cost. With the Effigy, collect T1 auras of DIFFERENT types; before it, only 1 aura beast fits.")}</p></div></div>
  <div class="filters" style="margin-bottom:12px">${[["all", T("Todos", "All")], ["haste", T("Rolam Haste", "Roll Haste")], ["cheap", T("Mais baratos (≤ 26,7%)", "Cheapest (≤ 26.7%)")], ["act", T("Campanha", "Campaign")], ["maps", T("Mapas", "Maps")]].map(([k, l]) => `<button type="button" data-hf="${k}" aria-pressed="${S.hf === k}">${l}</button>`).join("")}</div>
  <div class="tablewrap frame"><table><thead><tr><th>${T("Beast", "Beast")}</th><th>${T("Spirit", "Spirit")}</th><th>${T("Onde", "Where")}</th><th>${T("Como aparece", "How it spawns")}</th><th>Haste</th><th>${T("Observação", "Note")}</th></tr></thead><tbody>
  ${list.map(b => `<tr><td><b class="ui">${esc(b.n)}</b></td><td class="num">${b.cost}%${est(b.cost)}</td><td>${esc(b.where)}</td><td>${esc(b.how)}</td><td>${hasteTxt(b.haste)}</td><td>${esc(b.note)}</td></tr>`).join("")}
  </tbody></table></div>
  <div class="sechead" style="margin-top:26px"><div><h2 style="font-size:1.4rem">${T("Nos mapas (Atlas)", "In maps (Atlas)")}</h2></div></div>
  <div class="qgrid">${H.atlas.map(x => `<article class="qcard frame"><h3 style="margin:0">${esc(x.t)}</h3><p style="margin:0">${esc(x.d)}</p></article>`).join("")}</div>
  <div class="sechead" style="margin-top:26px"><div><h2 style="font-size:1.4rem">${T("Quais modificadores procurar", "Which modifiers to look for")}</h2><p>${T("Um beast pode ter até 4 modificadores. Procure pelo menos 1 principal; o ideal é 1 principal + 1 secundário.", "A beast can have up to 4 modifiers. Look for at least 1 primary; ideally 1 primary + 1 secondary.")}</p></div></div>
  <div class="grid g3">${["primary", "secondary", "tertiary"].map(k => `<div class="panel frame"><h3>${tierName[k]}</h3><ul class="clean ${k === "primary" ? "gold" : ""}">${H.mods.filter(m => m.tier === k).map(m => `<li><span><b class="ui">${esc(m.n)}</b><br><small style="color:var(--mute)">${esc(m.d)}</small></span></li>`).join("")}</ul></div>`).join("")}</div>
  <p style="color:var(--faint);font-size:.85rem;margin-top:16px">${T("Fontes:", "Sources:")} ${H.sources.map(s => `<a href="${esc(s.url)}" target="_blank" rel="noopener">${esc(s.name)}</a>`).join(" · ")}</p>`;
}
document.addEventListener("click", e => { const b = e.target.closest && e.target.closest("[data-hf]"); if (b) { S.hf = b.dataset.hf; store.set("hf", S.hf); render(); } });

/* ------------------------------------------------ quando usar */""")
rep(".spnote{", """.huntol{margin:0;padding-left:20px;display:grid;gap:6px}
.grid.g3{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.spnote{""")
# links para a nova aba
rep("""Use a aba <a href="#" data-gotab="meu">Meu personagem</a> para ver o que cabe no seu Spirit.</p>""", """Use a aba <a href="#" data-gotab="meu">Meu personagem</a> para ver o que cabe no seu Spirit e a aba <a href="#" data-gotab="caca">Caçar companions</a> para saber onde e como capturar.</p>""")
open("app_template.html", "w", encoding="utf-8").write(t)
print("ok")
