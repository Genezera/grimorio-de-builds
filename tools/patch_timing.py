# Patch: "Onde você está" (fase independente do nível), aba "Quando usar", avisos de nível nos itens.
import re
t = open("app_template.html", encoding="utf-8").read()

def rep(old, new, count=1):
    global t
    assert old in t, "NOT FOUND: " + old[:90]
    t = t.replace(old, new, count)

if "function curPhase" in t:
    raise SystemExit("already patched")

# ---- fase atual = escolhida pelo jogador ou pelo nível
rep("const phaseOf = lv =>", """S.stage = store.get("stage", "auto");
function curPhase() { return (S.stage && S.stage !== "auto" && D.phases.find(p => p.id === S.stage)) || phaseOf(S.lv); }
const phaseOf = lv =>""")
n_before = t.count("phaseOf(S.lv)")
t = t.replace("phaseOf(S.lv)", "curPhase()").replace("|| curPhase(); }", "|| phaseOf(S.lv); }")
t = t.replace("const c = S.ch, lv = S.lv, p = phaseOf(lv), act", "const c = S.ch, lv = S.lv, p = curPhase(), act")
# curPhase é definida antes de phaseOf, mas usa phaseOf só em tempo de execução
print("replaced phaseOf(S.lv):", n_before)

# ---- seletor "Onde você está no jogo"
rep('<div class="tg" id="phTag">—</div></div>',
    '<div class="tg" id="phTag">—</div><label class="stagesel"><span id="stageLbl">Onde você está no jogo</span><select id="stageSel" aria-label="Onde você está no jogo"></select></label></div>')
rep("""  const p = curPhase(); $("#phName").textContent = p.name; $("#phTag").textContent = `Nv ${p.lv[0]}–${p.lv[1]} · ${p.tag}`;""",
    """  paintStage();""")
rep("function setMode(m) {", """function paintStage() {
  const p = curPhase(); $("#phName").textContent = p.name;
  const manual = S.stage && S.stage !== "auto";
  $("#phTag").textContent = `${T("Nv", "Lv")} ${p.lv[0]}–${p.lv[1]} · ${p.tag}` + (manual && (S.lv < p.lv[0] || S.lv > p.lv[1]) ? T(` · escolhida manualmente (você é nível ${S.lv})`, ` · picked manually (you are level ${S.lv})`) : "");
  const sel = $("#stageSel");
  sel.innerHTML = `<option value="auto">${T("Automático pelo nível", "Automatic by level")} (${esc(phaseOf(S.lv).name)})</option>` + D.phases.map(x => `<option value="${x.id}" ${x.id === S.stage ? "selected" : ""}>${esc(x.name)}</option>`).join("");
  sel.value = manual ? S.stage : "auto";
  $("#stageLbl").textContent = T("Onde você está no jogo", "Where you are in the game");
}
function setMode(m) {""")
rep("""document.addEventListener("change", e => {""", """document.addEventListener("change", e => {
  if (e.target.id === "stageSel") { S.stage = e.target.value; store.set("stage", S.stage); S.skillPhase = S.treePhase = S.gearPhase = null; paintStage(); paintRail(); render(); return; }""")

# ---- aviso de nível nos cartões de item
rep("""function itemCard(it) {
  const im = ic(it.ic);""", """function lvlReq(name) { const u = D.uniques.find(x => x.n === name); return u && u.lvl ? u : null; }
function itemCard(it) {
  const im = ic(it.ic); const lr = lvlReq(it.n);
  const lvWarn = lr && lr.lvl > S.lv ? `<div class="lvwarn">${T(`Requer nível ${lr.lvl} — você é ${S.lv}. Guarde até lá.`, `Requires level ${lr.lvl} — you are ${S.lv}. Keep it until then.`)}</div>` : (lr && lr.lvlRf && lr.lvlRf > S.lv && (it.r || []).some(x => /Rune(forged|mastered)/.test(x)) ? `<div class="lvwarn">${T(`Versão Runeforged/Runemastered requer nível ${lr.lvlRf}; a normal, ${lr.lvl}.`, `Runeforged/Runemastered version requires level ${lr.lvlRf}; the normal one, ${lr.lvl}.`)}</div>` : "");""")
rep("""    <div class="th">${esc(it.n)}<small>${esc(it.slot)}${it.u ? " · Único" : ""}</small></div>""",
    """    <div class="th">${esc(it.n)}<small>${esc(it.slot)}${it.u ? " · Único" : ""}${lr ? ` · ${T("nível", "level")} ${lr.lvl}${lr.lvlRf ? "/" + lr.lvlRf : ""}` : ""}</small></div>${lvWarn}""")

# ---- aba "Quando usar"
rep('<section class="view" id="v-meu"></section>', '<section class="view" id="v-meu"></section>\n    <section class="view" id="v-quando"></section>')
rep('["meu","Meu personagem"],', '["meu","Meu personagem"],["quando","Quando usar"],')
rep("const VIEWS = { meu: vMeu,", "const VIEWS = { meu: vMeu, quando: vQuando,")
rep("/* ------------------------------------------------ events */", r"""/* ------------------------------------------------ quando usar */
S.qf = store.get("qf", "all");
function qStatus(e) {
  const owned = e.kind === "item" ? !!S.ch.items[e.n] : e.kind === "asc" ? !!S.ch.asc[{ "Wild Protector": "wp", "The Natural Order": "no", "The Catha's Balance": "catha", "Idolatry": "idol" }[e.n]] : e.kind === "key" ? (e.n === "Trusted Kinship" ? S.ch.tk : e.n === "Giant's Blood" ? S.ch.gb : false) : false;
  if (e.lvl > S.lv) return { k: "lock", t: T(`Nível ${e.lvl} — faltam ${e.lvl - S.lv}`, `Level ${e.lvl} — ${e.lvl - S.lv} to go`), owned };
  return { k: owned ? "have" : "ok", t: owned ? T("Você já tem", "You have it") : T("Já pode usar", "Usable now"), owned };
}
function vQuando() {
  const kinds = [["all", T("Tudo", "All")], ["item", T("Itens", "Items")], ["asc", T("Ascendência", "Ascendancy")], ["key", T("Keystones", "Keystones")], ["skill", T("Skills", "Skills")]];
  const list = D.timing.filter(e => S.qf === "all" || e.kind === S.qf).slice().sort((a, b) => (qStatus(a).owned && a.lvl > S.lv ? -1 : 0) - (qStatus(b).owned && b.lvl > S.lv ? -1 : 0) || a.lvl - b.lvl);
  const early = D.timing.filter(e => qStatus(e).owned && e.lvl > S.lv);
  const card = e => { const st = qStatus(e); const im = uniqImg(e.n) || gemImg(e.n.replace(/\s*\(.*\)/, "")) || "";
    return `<article class="qcard frame ${st.k}" id="q-${esc(e.n.replace(/[^A-Za-z]/g, ""))}">
      <div class="qh">${im ? `<img src="${im}" alt="">` : `<span class="qi">${esc(e.n[0])}</span>`}<div><h3>${esc(e.n)}</h3><small>${esc(e.req)}</small></div><span class="qst ${st.k}">${esc(st.t)}</span></div>
      <div class="qrow"><b>${T("Quando usar", "When to use")}</b><p>${esc(e.when)}</p></div>
      <div class="qrow"><b>${T("O que faz", "What it does")}</b><p>${esc(e.gives)}</p></div>
      ${e.early && e.early !== "—" ? `<div class="qrow early"><b>${T("Se conseguir antes", "If you get it early")}</b><p>${esc(e.early)}</p></div>` : ""}
      ${e.late && e.late !== "—" ? `<div class="qrow late"><b>${T("Se ainda não tem", "If you don't have it yet")}</b><p>${esc(e.late)}</p></div>` : ""}
      ${e.steps.length ? `<div class="qrow"><b>${T("O que mudar quando entrar", "What to change when it comes in")}</b><ol>${e.steps.map(s => `<li>${esc(s)}</li>`).join("")}</ol></div>` : ""}
      ${e.watch.length ? `<div class="qrow watch"><b>${T("Cuidado", "Watch out")}</b><ul>${e.watch.map(s => `<li>${esc(s)}</li>`).join("")}</ul></div>` : ""}
    </article>`; };
  return `<div class="sechead"><div><h2>${T("Quando usar cada peça", "When to use each piece")}</h2><p>${T("Requisito real de nível (texto do item na liga), momento ideal na rota e o que fazer se você conseguir o item, a ascendência ou a skill antes ou depois do planejado. O status de cada cartão usa o seu nível e o que você marcou em Meu personagem.", "Real level requirement (item text in the league), ideal moment in the route and what to do if you get the item, ascendancy or skill earlier or later than planned. Each card's status uses your level and what you ticked in My character.")}</p></div></div>
  ${early.length ? `<div class="spnote frame"><b>${T("Você tem", "You have")}</b><p>${early.map(e => `<a href="#q-${esc(e.n.replace(/[^A-Za-z]/g, ""))}">${esc(e.n)}</a> (${T("nível", "level")} ${e.lvl})`).join(" · ")} — ${T("ainda não dá para usar no seu nível. Veja o que preparar em cada cartão.", "not usable at your level yet. See what to prepare on each card.")}</p></div>` : ""}
  <div class="panel frame" style="margin-bottom:16px"><h3>${T("Casos comuns", "Common cases")}</h3>${D.timingCases.map((c, i) => `<details class="acc" ${i === 0 ? "open" : ""}><summary>${esc(c.q)}</summary><div>${esc(c.a)}</div></details>`).join("")}</div>
  <div class="filters" id="qfilt" style="margin-bottom:14px">${kinds.map(([k, l]) => `<button type="button" data-qf="${k}" aria-pressed="${S.qf === k}">${l}</button>`).join("")}</div>
  <div class="qgrid stagger">${list.map(card).join("")}</div>`;
}
document.addEventListener("click", e => { const b = e.target.closest && e.target.closest("[data-qf]"); if (b) { S.qf = b.dataset.qf; store.set("qf", S.qf); render(); } });

/* ------------------------------------------------ events */""")

# ---- recomendações: itens que ainda não dá para usar + dica de fase
rep("""  // ---- arma""", """  // ---- itens acima do nível / fase
  for (const e of D.timing) if (e.kind === "item" && c.items[e.n] && e.lvl > lv) add("warn", T(`${e.n}: requer nível ${e.lvl} (você é ${lv})`, `${e.n}: requires level ${e.lvl} (you are ${lv})`), e.early, "quando");
  if ((!S.stage || S.stage === "auto") && lv >= 58 && lv <= 64) add("tip", T("Já está no Atlas?", "Already in the Atlas?"), T("Escolha 'Início do Atlas' em 'Onde você está no jogo' no topo. O guia passa a mostrar a fase certa sem mudar o seu nível.", "Pick 'Early Atlas' in 'Where you are in the game' at the top. The guide shows the right phase without changing your level."), "quando");
  // ---- arma""")

# ---- CSS
rep(".spnote{", """.stagesel{display:grid;gap:3px;margin-top:8px}
.stagesel span{font-family:var(--ui);font-size:.72rem;color:var(--mute);letter-spacing:.04em}
.stagesel select{max-width:260px}
.lvwarn{margin:6px 12px 0;padding:5px 8px;border:1px solid rgba(224,102,79,.55);color:#ffb3a3;font-family:var(--ui);font-size:.8rem}
.qgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px}
@media (max-width:600px){.qgrid{grid-template-columns:1fr}}
.qcard{padding:14px;display:grid;gap:8px;align-content:start}
.qcard.lock{border-color:rgba(224,102,79,.35)}
.qcard.have{border-color:#2f5b4c}
.qh{display:grid;grid-template-columns:48px 1fr auto;gap:10px;align-items:center}
.qh img{width:48px;height:48px;object-fit:contain}
.qh .qi{display:grid;place-items:center;width:44px;height:44px;border:1px solid var(--edge2);font-family:var(--display);color:var(--gild-hi)}
.qh h3{margin:0;font-size:1.05rem}
.qh small{color:var(--mute);font-size:.8rem}
.qst{padding:3px 8px;font-family:var(--ui);font-size:.74rem;font-weight:700;border:1px solid var(--edge2);white-space:nowrap}
.qst.lock{border-color:rgba(224,102,79,.6);color:#ffb3a3}
.qst.ok{border-color:#8a6a38;color:var(--gild-hi)}
.qst.have{border-color:#2f5b4c;color:#8fd9b8}
.qrow b{display:block;font-family:var(--ui);font-size:.8rem;color:var(--gild);letter-spacing:.03em}
.qrow p{margin:2px 0 0;font-size:.92rem}
.qrow ol,.qrow ul{margin:4px 0 0;padding-left:18px;font-size:.9rem;display:grid;gap:3px}
.qrow.early b{color:#9fd2ff}.qrow.late b{color:#e0b36a}.qrow.watch b{color:#ffb3a3}
.spnote{""")

open("app_template.html", "w", encoding="utf-8").write(t)
print("ok")
