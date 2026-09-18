/* ------------------------------------------------ adaptar ao meu personagem (kit) */
S.adapt = store.get("adapt", true);
const clone = o => JSON.parse(JSON.stringify(o));
const setsRedirect = pid => { const s = (D.adaptSwaps || []).find(x => x.setsFrom && (x.pid ? x.pid === pid : x.pids ? x.pids.includes(pid) : true) && ruleOk(x.when)); return s && adaptOn() ? s.setsFrom : pid; };
const setItemsRaw = pid => { const src = setsRedirect(pid); return (A.sets[src] ? A.sets[src][S.mode] : A.guide[src]) || []; };
const phaseById = id => D.phases.find(x => x.id === id);
const canUse = n => { const u = D.uniques.find(x => x.n === n); return !u || !u.lvl || u.lvl <= S.lv; };
const hasUse = n => own(n) && canUse(n);
const adaptOn = () => !!S.adapt && !!S.ch && (Object.values(S.ch.own || {}).some(Boolean) || +S.ch.spirit > 0);
/* trocas declaradas nos dados: {pid, when:{...regra}, gemsFrom, note} */
/* a troca só vale nas fases declaradas (pid ou pids); sem nenhuma das duas, vale em qualquer fase */
const swapsFor = pid => (D.adaptSwaps || []).filter(s => (s.pid ? s.pid === pid : s.pids ? s.pids.includes(pid) : true) && ruleOk(s.when));

function adaptNotes() {
  const n = []; if (!adaptOn()) return n;
  const p = curPhase();
  swapsFor(p.id).forEach(s => s.note && n.push(s.note));
  const tc = buffCalc();
  if (tc.spirit && tc.rows.length) n.push(T(`Spirit: ${tc.used}/${tc.spirit} reservados pelas skills que você marcou.`, `Spirit: ${tc.used}/${tc.spirit} reserved by the skills you ticked.`));
  return n;
}
function adaptPhase(p) {
  if (!p || !adaptOn() || p.id !== curPhase().id) return p;
  const q = clone(p); q._adapted = true;
  for (const s of swapsFor(p.id)) {
    if (s.gemsFrom) { const src = clone(phaseById(s.gemsFrom)); q.gems = src.gems; q.skeletons = src.skeletons; q.spiritNote = src.spiritNote; }
    /* copyFields: {from: "<fase>", fields: [...]} troca também os textos da fase (goal, rotação, metas) */
    if (s.copyFields) { const src = clone(phaseById(s.copyFields.from)); for (const k of s.copyFields.fields) if (src[k] !== undefined) q[k] = src[k]; }
    if (s.fields) Object.assign(q, clone(s.fields));
    if (s.dropGems) q.gems = q.gems.filter(g => !s.dropGems.includes(g.skill));
    if (s.addGems) for (const ag of s.addGems) if (!q.gems.some(g => g.skill === ag.skill)) q.gems.push(clone(ag));
  }
  const spirit = +S.ch.spirit || 0;
  if (spirit) {
    const tc = buffCalc({ spirit, all: true });
    let run = 0;
    const order = q.gems.filter(g => g.sp === "core" || g.sp === "opt").sort((a, b) => (a.sp === b.sp ? a.pr - b.pr : a.sp === "core" ? -1 : 1));
    for (const g of order) {
      const b = tc.rows.find(x => x.name === g.skill); if (!b) continue;
      run += b.eff; g.spEst = b.eff; if (run > spirit) g.fits = false;
    }
    q.spiritUsed = Math.min(run, spirit); q.spiritTotal = spirit;
  }
  return q;
}
function adaptItems(pid, items) {
  if (!adaptOn() || pid !== curPhase().id) return items;
  const out = clone(items); const ringSlot = s => /Anel|Ring/i.test(s); const pool = []; const cur = PH_ORDER.indexOf(pid);
  for (const ph of PH_ORDER) for (const m of [S.mode, S.mode === "cheap" ? "full" : "cheap"]) for (const it of (A.sets[ph] || {})[m] || []) if (it.u) pool.push(Object.assign({}, it, { _d: Math.abs(PH_ORDER.indexOf(ph) - cur) }));
  /* uniques da aba Uniques que você marcou também entram no set recomendado (elas não estão nos sets do planner) */
  const SLOT_ALIAS = { "Arco": "Arma", "Bow": "Arma", "Aljava": "Offhand", "Quiver": "Offhand", "Talisman (Set 2)": "Arma (Set 2)", "Anel": "Anel", "Ring": "Anel" };
  const slotKey = t => { const x = String(t || ""); const al = SLOT_ALIAS[x] || x; return al.replace(/\s*\(.*/, "").replace(/\s+[ED]$/, "").toLowerCase(); };
  for (const u of D.uniques || []) {
    if (!hasUse(u.n) || pool.some(c => c.n === u.n)) continue;
    const d = Math.abs(PH_ORDER.indexOf(u.p) - cur);
    pool.push({ n: u.n, u: 1, ic: (A.uniqIcon || {})[u.n], x: (u.mods || []).slice(0, 6).join(" ; "), r: [], rs: 0, note: "", price: u.price, slot: u.slot, _d: isNaN(d) ? 9 : d });
  }
  pool.sort((x, y) => x._d - y._d);
  for (let i = 0; i < out.length; i++) {
    const it = out[i];
    if (it.u && hasUse(it.n)) { it.have = 1; continue; }
    const cand = pool.find(c => (c.slot === it.slot || slotKey(c.slot) === slotKey(it.slot) || (ringSlot(c.slot) && ringSlot(it.slot))) && hasUse(c.n));
    if (cand) { out[i] = Object.assign(clone(cand), { slot: it.slot, have: 1, swapped: it.n }); continue; }
    if (it.u) it.miss = 1;
  }
  return out;
}
function adaptBanner() {
  if (!Object.values(S.ch.own || {}).some(Boolean) && !+S.ch.spirit) return `<div class="adaptbar frame"><span>${T("Marque o que você tem em <b>Meu personagem</b> e esta aba se adapta ao seu personagem.", "Tick what you have in <b>My character</b> and this tab adapts to your character.")}</span><button class="btn" type="button" data-gotab="meu">${T("Abrir Meu personagem", "Open My character")}</button></div>`;
  const on = adaptOn(), notes = adaptNotes();
  return `<div class="adaptbar frame ${on ? "on" : ""}"><label class="chk"><input type="checkbox" id="adaptTgl" ${S.adapt ? "checked" : ""}><span>${T("Adaptar ao que eu tenho", "Adapt to what I have")}</span></label>
    <span>${on ? T(`Plano ajustado para ${esc(curPhase().name)} com base em Meu personagem.`, `Plan adjusted for ${esc(curPhase().name)} based on My character.`) : T("Mostrando o plano padrão da fase.", "Showing the phase's default plan.")}</span>
    ${on && notes.length ? `<ul>${notes.map(x => `<li>${esc(x)}</li>`).join("")}</ul>` : ""}
    <button class="btn" type="button" data-gotab="meu">${T("Editar o que eu tenho", "Edit what I have")}</button></div>`;
}
function treeAdaptNotes() {
  if (!adaptOn()) return "";
  const idOf = name => Object.keys(A.tree.meta).find(k => A.tree.meta[k][0] === name);
  const link = n => { const id = idOf(n); return id ? ` <a href="#" data-gotree="${id}">${esc(n)}</a>` : ""; };
  const out = (D.treeRules || []).filter(r => ruleOk(r.when)).map(r => esc(r.t) + (r.node ? link(r.node) : ""));
  return out.length ? `<div class="adaptbar frame on"><b>${T("Ajustes da árvore para o seu personagem", "Tree adjustments for your character")}</b><ul>${out.map(x => `<li>${x}</li>`).join("")}</ul></div>` : "";
}
document.addEventListener("change", e => { if (e.target.id === "adaptTgl") { S.adapt = e.target.checked; store.set("adapt", S.adapt); render(); } });
