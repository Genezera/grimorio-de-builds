/* ------------------------------------------------ meu personagem: checklist + recomendações automáticas (kit) */
const T = (pt, en) => LANG === "en" ? en : pt;
const CHAR = D.char || { own: [], nums: [], buffs: [], rules: [] };
const OWN = CHAR.own;
const CH_DEFAULT = Object.assign({ own: {}, skillsConfigured: false, combatProfile: "clear" }, Object.fromEntries((CHAR.nums || []).map(n => [n[0], ""])));
S.ch = Object.assign(JSON.parse(JSON.stringify(CH_DEFAULT)), store.get("char", {}));
if (!S.ch.own) S.ch.own = {};
// Preserve checklist state from the older abbreviated keys.
const ownAliases = {obliterator:"Obliterator Bow", seske:"Countess Seske's Rune of Archery", thruldana:"Idol of Thruldana", absent:"Absent Amulet", talisman:"Hysseg's Claw"};
for (const [oldKey, newKey] of Object.entries(ownAliases)) if (S.ch.own[oldKey] && !S.ch.own[newKey]) S.ch.own[newKey] = true;
const own = k => !!S.ch.own[k];
const num = k => +S.ch[k] || 0;
const PIDX = id => D.phases.findIndex(p => p.id === id);
const saveCh = defer => {
  store.set("char", S.ch);
  if (!defer) return render();
  clearTimeout(spTimer);
  spTimer = setTimeout(() => { const a = document.activeElement; const k = a && a.dataset.ch; render(); const n = k ? document.querySelector(`[data-ch="${k}"]`) : null; if (n) { n.focus(); const v = n.value; n.value = ""; n.value = v; } }, 450);
};
/* Spirit das skills persistentes: custo do Path of Building; "halve" = nó/efeito que corta a reserva pela metade */
function buffCalc(o) {
  o = o || {};
  const spirit = +(o.spirit ?? S.ch.spirit) || 0;
  const mult = CHAR.halve && (o.halve ?? own(CHAR.halve)) ? .5 : 1;
  const rows = (CHAR.buffs || []).filter(b => o.all || own(b.key)).map(b => ({ ...b, eff: Math.ceil(b.cost * mult) }));
  const used = rows.reduce((a, b) => a + b.eff, 0);
  return { spirit, mult, rows, used, free: spirit - used, pct: spirit ? used / spirit : 0 };
}
/* regras declarativas (dados da build): todas as condições presentes precisam valer */
function ruleOk(w) {
  if (!w) return true;
  const lv = S.lv, pi = PIDX(curPhase().id);
  if (w.lvMin != null && lv < w.lvMin) return false;
  if (w.lvMax != null && lv > w.lvMax) return false;
  if (w.phaseMin && pi < PIDX(w.phaseMin)) return false;
  if (w.phaseMax && pi > PIDX(w.phaseMax)) return false;
  if (w.skillsConfigured != null && !!S.ch.skillsConfigured !== w.skillsConfigured) return false;
  if (w.own && !w.own.every(own)) return false;
  if (w.anyOwn && !w.anyOwn.some(own)) return false;
  if (w.notOwn && w.notOwn.some(own)) return false;
  if (w.numLt && !(num(w.numLt[0]) && num(w.numLt[0]) < w.numLt[1])) return false;
  if (w.numGt && !(num(w.numGt[0]) > w.numGt[1])) return false;
  if (w.numMissing && num(w.numMissing)) return false;
  if (w.numLtNum && !(num(w.numLtNum[0]) && num(w.numLtNum[1]) && num(w.numLtNum[0]) < num(w.numLtNum[1]))) return false;
  if (w.spiritShort && !(num("spirit") && buffCalc().free < 0)) return false;
  return true;
}
function charRecs() {
  const R = [], add = (lvl, t, d, tab) => R.push({ lvl, t, d, tab });
  const tc = buffCalc();
  for (const r of CHAR.rules || []) if (ruleOk(r.when)) add(r.lvl, r.t, r.d, r.tab);
  const prof = S.ch.combatProfile || "clear";
  const req = (((CHAR.phaseSkills || {})[curPhase().id] || {})[prof] || []);
  if (!S.ch.skillsConfigured) {
    add("tip", T("Conte ao guia quais skills você tem", "Tell the guide which skills you have"), T("Abra Meu personagem ou Skills e marque as gems disponíveis. A barra e as prioridades passarão a refletir seu personagem.", "Open My character or Skills and tick the available gems. Your bar and priorities will then reflect your character."), "meu");
  } else {
    const missingSkills = req.filter(k => !own(k)).map(k => ((CHAR.skillInfo || {})[k] || {}).name || k);
    if (missingSkills.length) add("warn", T(`Faltam ${missingSkills.length} skill(s) para ${prof === "boss" ? "boss" : "clear"}`, `${missingSkills.length} skill(s) missing for ${prof}`), missingSkills.join(" · "), "skills");
  }
  if (num("spirit") && (CHAR.buffs || []).length) {
    if (tc.free < 0) add("bad", T(`Spirit estourado em ${-tc.free}`, `Spirit over by ${-tc.free}`), T(`As skills marcadas reservam ${tc.used} de ${tc.spirit}. Desligue a última da ordem de Spirit da fase (aba Skills).`, `Ticked skills reserve ${tc.used} of ${tc.spirit}. Turn off the last one in this phase's Spirit order (Skills tab).`), "skills");
    else if (tc.rows.length) add("ok", T(`Spirit: ${tc.used}/${tc.spirit} reservados`, `Spirit: ${tc.used}/${tc.spirit} reserved`), T(`Sobram ${tc.free}.`, `${tc.free} left.`) + (CHAR.halve && !own(CHAR.halve) ? " " + (CHAR.halveTip || "") : ""), "mech");
  } else if ((CHAR.buffs || []).length && S.lv >= 20) add("tip", T("Informe seu Spirit máximo", "Enter your max Spirit"), T("Com o número, o app confere se suas skills persistentes cabem.", "With the number, the app checks whether your persistent skills fit."), "meu");
  // ascendência pelo nível
  (D.ascendancy || []).forEach((a, i) => { const need = (D.ascUnlock || [])[i]; if (a.key && need && S.lv >= need + 3 && !own(a.key)) add("warn", T(`Falta a ascendência ${a.node}`, `Missing ascendancy ${a.node}`), T(`Disponível por volta do nível ${need}.`, `Available around level ${need}.`), "asc"); });
  // uniques do set da fase
  const want = setItemsRaw(curPhase().id).filter(it => it.u && !/Charm/.test(it.slot) && OWN.some(o => o[1] === it.n));
  const missing = want.filter(it => !own(it.n));
  if (missing.length) add("warn", T(`Faltam ${missing.length} unique(s) do set da fase`, `${missing.length} unique(s) of the phase set missing`), missing.map(it => `${it.n}${it.price != null ? " " + fmtPrice(it.price) : ""}`).join(" · "), "gear");
  // quests de Spirit que ficaram para trás
  const actNum = q => { const m = String(q.act).match(/\d+/); return m ? +m[0] : 5; };
  const act = (D.phaseAct || {})[curPhase().id] || 1;
  const spq = D.quests.map((q, i) => ({ q, i })).filter(o => /Spirit/.test(o.q.reward) && !S.done["q:" + o.i] && actNum(o.q) < act);
  if (spq.length) add("warn", T("Quests de Spirit que ficaram para trás", "Spirit quests left behind"), spq.map(o => `${o.q.boss} (${o.q.reward})`).join(" · "), "quests");
  const order = { bad: 0, warn: 1, tip: 2, ok: 3 };
  return { recs: R.sort((a, b) => order[a.lvl] - order[b.lvl]), tc };
}
function vMeu() {
  const c = S.ch, r = charRecs(), tc = r.tc;
  const icon = { bad: "✖", warn: "!", tip: "➜", ok: "✔" };
  const box = ([grp, k, label]) => { const im = uniqImg(k) || gemImg(label.split(" (")[0]) || supImg(label.split(" (")[0]); return `<label class="chk"><input type="checkbox" data-own="${esc(k)}" data-own-kind="${esc(grp)}" ${own(k) ? "checked" : ""}><span>${im ? `<img src="${im}" alt="">` : ""}${esc(label)}</span></label>`; };
  const grp = g => OWN.filter(o => o[0] === g).map(box).join("");
  const field = ([k, label, ph]) => `<label class="field"><span>${esc(label)}</span><input type="number" min="0" data-ch="${k}" value="${esc(c[k])}" placeholder="${esc(ph || "")}"></label>`;
  const tiles = (CHAR.tiles || []).map(([label, expr]) => `<div><b>${esc(String(expr === "free" ? (tc.spirit ? tc.free : "—") : expr === "used" ? tc.used : c[expr] || "—"))}</b><span>${esc(label)}</span></div>`).join("");
  const groups = CHAR.sections || [["gear", T("Itens que eu tenho", "Items I have")], ["gem", T("Gems que eu tenho/uso", "Gems I have/use")], ["tree", T("Árvore", "Tree")], ["asc", T("Ascendência", "Ascendancy")]];
  return `<div class="sechead"><div><h2>${T("Meu personagem", "My character")}</h2><p>${esc(CHAR.intro || "")}</p></div></div>
  ${tiles ? `<div class="stat charstat">${tiles}</div>` : ""}
  <div class="charwrap">
    <div class="panel frame recs"><h3>${T("Recomendações para você agora", "Recommendations for you now")}</h3>
      ${r.recs.length ? r.recs.map(x => `<div class="rec ${x.lvl}" ${x.tab && x.tab !== "meu" ? `data-gotab="${x.tab}"` : ""}><span class="ri">${icon[x.lvl]}</span><div><b>${esc(x.t)}</b><small>${esc(x.d)}</small></div></div>`).join("") : `<p style="color:var(--mute)">${T("Preencha o formulário ao lado: as recomendações aparecem aqui.", "Fill in the form: recommendations show up here.")}</p>`}
    </div>
    <div class="grid" style="gap:14px">
      ${(CHAR.nums || []).length ? `<div class="panel frame"><h3>${T("Números do personagem", "Character numbers")}</h3><div class="grid g2" style="gap:10px">${CHAR.nums.map(field).join("")}</div></div>` : ""}
      ${groups.map(([g, h, d]) => OWN.some(o => o[0] === g) ? `<div class="panel frame"><h3>${h}</h3>${d ? `<p style="margin:-2px 0 10px;color:var(--mute);font-size:.9rem">${esc(d)}</p>` : ""}<div class="chkgrid ${g === "gear" ? "items" : ""}">${grp(g)}</div></div>` : "").join("")}
    </div>
  </div>`;
}
document.addEventListener("change", e => { const t = e.target; if (t.dataset && t.dataset.own !== undefined && t.closest && t.closest("#v-meu, #v-mech, #v-skills")) { S.ch.own[t.dataset.own] = t.checked; if (["active", "persistent", "support"].includes(t.dataset.ownKind)) S.ch.skillsConfigured = true; saveCh(); } });
document.addEventListener("input", e => { const t = e.target; if (t.dataset && t.dataset.ch && t.closest && t.closest("#v-meu, #v-mech")) { S.ch[t.dataset.ch] = t.value; saveCh(true); } });
