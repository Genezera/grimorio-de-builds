/* ------------------------------------------------ adaptar ao meu personagem (Oracle) */
S.adapt = store.get("adapt", true);
const clone = o => JSON.parse(JSON.stringify(o));
const setItemsRaw = pid => (A.sets[pid] ? A.sets[pid][S.mode] : A.guide[pid]) || [];
const phaseById = id => D.phases.find(x => x.id === id);
const canUse = n => { const u = D.uniques.find(x => x.n === n); return !u || !u.lvl || u.lvl <= S.lv; };
const hasUse = n => own(n) && canUse(n);
const adaptOn = () => !!S.adapt && !!S.ch && (Object.values(S.ch.own || {}).some(Boolean) || +S.ch.spirit > 0);

function adaptNotes() {
  const n = []; if (!adaptOn()) return n;
  const p = curPhase(), pi = PIDX(p.id), sw = PIDX("sw");
  if (pi >= sw && !own("ab")) n.push(T("Sem Ancestral Bond: mostrando o setup de leveling do Ato 4 até você fazer a troca.", "No Ancestral Bond: showing the Act 4 leveling setup until you swap."));
  if (pi < sw && own("ab")) n.push(T("Você já tem Ancestral Bond: mostrando o setup de totem.", "You already have Ancestral Bond: showing the totem setup."));
  if (own("grim") && own("runeforged") && pi >= sw && pi < PIDX("w1")) n.push(T("Grim Pillars + Runic Ward: totem já no setup de Grim Pillars.", "Grim Pillars + Runic Ward: totem already on the Grim Pillars setup."));
  if (pi >= PIDX("w1") && !(own("grim") && own("runeforged"))) n.push(T("Sem Grim Pillars com Runic Ward: totem continua com Spark.", "No Grim Pillars with Runic Ward: totem stays on Spark."));
  const tc = totemCalc(); if (tc.spirit && tc.ab) n.push(T(`${tc.fit} totem(s) cabem (limite ${tc.limit}, ${tc.perR} Spirit cada).`, `${tc.fit} totem(s) fit (limit ${tc.limit}, ${tc.perR} Spirit each).`));
  return n;
}
function adaptPhase(p) {
  if (!p || !adaptOn() || p.id !== curPhase().id) return p;
  const pi = PIDX(p.id), sw = PIDX("sw");
  let q = clone(p); q._adapted = true;
  // troca antes/depois do planejado
  if (pi >= sw && !own("ab")) { const a4 = clone(phaseById("a4")); q.gems = a4.gems; q.skeletons = a4.skeletons; q.spiritNote = T("Você ainda não pegou Ancestral Bond: continue com o setup do Ato 4 até ter 210+ Spirit, sceptre e wand. ", "You haven't taken Ancestral Bond yet: stay on the Act 4 setup until you have 210+ Spirit, sceptre and wand. ") + (a4.spiritNote || ""); }
  if (pi < sw && own("ab")) { const s = clone(phaseById("sw")); q.gems = s.gems; q.skeletons = s.skeletons; q.spiritNote = s.spiritNote; }
  const totemPhase = q.gems.some(g => g.skill === "Spell Totem");
  if (totemPhase) {
    const grimReady = own("grim") && own("runeforged");
    const tpl = grimReady ? (pi >= PIDX("fin") && own("rakiata") ? phaseById("fin") : phaseById("w1")) : phaseById(pi >= PIDX("ea") ? "ea" : pi >= PIDX("int") ? "int" : "sw");
    const tg = tpl.gems.find(g => g.skill === "Spell Totem");
    const first = q.gems.findIndex(g => g.skill === "Spell Totem");
    q.gems = q.gems.filter((g, i) => g.skill !== "Spell Totem" || i === first);
    if (first >= 0 && tg) { const g = q.gems.find(x => x.skill === "Spell Totem"); g.sup = tg.sup.slice(); g.why = tg.why; }
    if (grimReady && !q.gems.some(g => g.skill === "Entangle")) { const en = clone(phaseById("w1").gems.find(g => g.skill === "Entangle")); q.gems.push(en); }
    if (!grimReady) for (const g of q.gems) if (g.skill === "Entangle" && pi >= PIDX("w1")) { g.role = T("Clear (sem Grim Pillars)", "Clear (no Grim Pillars)"); }
    if (own("pierce") && !own("bb")) { const g = q.gems.find(x => x.skill === "Spell Totem"); if (g && g.sup.includes("Spark") && !g.sup.includes("Pierce II")) { g.sup = g.sup.slice(0, -1).concat("Pierce II"); g.why += T(" Você marcou Pierce II (sem Branching Bolts): entra no último slot.", " You ticked Pierce II (no Branching Bolts): it takes the last slot."); } }
    // Spirit e totems
    const tc = totemCalc();
    const tg2 = q.gems.find(g => g.skill === "Spell Totem");
    if (tg2) { tg2.cost = T(`${tc.perR} Spirit por totem`, `${tc.perR} Spirit per totem`); if (tc.spirit) tg2.spEst = tc.fit * tc.perR; }
    for (const g of q.gems) {
      if (g.skill === "Archmage" && tc.spirit) { const withArch = totemCalc({ archmage: true }); if (withArch.fit < 3 || withArch.left < 0) { g.sp = "opt"; g.pr = 1; g.why += T(` Com ${tc.spirit} Spirit, o Archmage deixaria só ${withArch.fit} totem(s): ative quando tiver mais Spirit.`, ` With ${tc.spirit} Spirit, Archmage would leave only ${withArch.fit} totem(s): activate it once you have more Spirit.`); } }
      if (g.skill === "Ravenous Swarm") { g.sp = "opt"; g.pr = 9; }
    }
    const box = q.skeletons || { n: "", types: [], note: "" };
    q.skeletons = { n: tc.ab ? String(tc.fit) : "0", types: [T(`limite ${tc.limit}`, `limit ${tc.limit}`), T(`${tc.perR} Spirit cada`, `${tc.perR} Spirit each`)], note: tc.spirit ? T(`Com ${tc.spirit} Spirit e ${tc.otherSum} reservados em outras skills cabem ${tc.fit} totem(s). ${box.note}`, `With ${tc.spirit} Spirit and ${tc.otherSum} reserved on other skills, ${tc.fit} totem(s) fit. ${box.note}`) : T("Informe seu Spirit em Meu personagem para calcular.", "Enter your Spirit in My character to calculate.") };
    if (tc.spirit) { q.spiritUsed = tc.used; q.spiritTotal = tc.spirit; }
    q.spiritNote = (q.spiritNote || "") + (grimReady ? "" : T(" Sem Grim Pillars + Runic Ward: o totem usa Spark.", " Without Grim Pillars + Runic Ward: the totem uses Spark."));
  }
  return q;
}
function adaptItems(pid, items) {
  if (!adaptOn() || pid !== curPhase().id) return items;
  const out = clone(items); const ringSlot = s => /Anel|Ring/i.test(s); const pool = []; const cur = PH_ORDER.indexOf(pid);
  for (const ph of PH_ORDER) for (const m of [S.mode, S.mode === "cheap" ? "full" : "cheap"]) for (const it of (A.sets[ph] || {})[m] || []) if (it.u) pool.push(Object.assign({}, it, { _d: Math.abs(PH_ORDER.indexOf(ph) - cur) * 2 + (PH_ORDER.indexOf(ph) < cur ? 1 : 0) }));
  pool.sort((x, y) => x._d - y._d);
  for (let i = 0; i < out.length; i++) {
    const it = out[i];
    if (it.u && hasUse(it.n)) { it.have = 1; continue; }
    const cand = pool.find(c => (c.slot === it.slot || (ringSlot(c.slot) && ringSlot(it.slot))) && hasUse(c.n));
    if (cand) { out[i] = Object.assign(clone(cand), { slot: it.slot, have: 1, swapped: it.n }); continue; }
    if (it.u) it.miss = 1;
  }
  return out;
}
function adaptBanner() {
  if (!Object.values(S.ch.own || {}).some(Boolean) && !+S.ch.spirit) return `<div class="adaptbar frame"><span>${T("Marque o que você tem em <b>Meu personagem</b> e esta aba se adapta ao seu personagem.", "Tick what you have in <b>My character</b> and this tab adapts to your character.")}</span><button class="btn" type="button" data-gotab="meu">${T("Marcar agora", "Tick now")}</button></div>`;
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
  const out = []; const spirit = +S.ch.spirit || 0;
  if (!own("ab") && S.lv >= 45) out.push(T(`Ancestral Bond é a base da troca. Só pegue com ${own("ei") ? 210 : 255}+ Spirit.`, `Ancestral Bond is the core of the swap. Only take it with ${own("ei") ? 210 : 255}+ Spirit.`) + link("Ancestral Bond"));
  if (own("ab") && !own("ei") && spirit && spirit < 255) out.push(T("Menos de 255 Spirit: pegue Efficient Inscriptions (75 → 63 por totem).", "Under 255 Spirit: take Efficient Inscriptions (75 → 63 per totem).") + link("Efficient Inscriptions"));
  if (own("pierce") && own("bb")) out.push(T("Pierce II marcado: tire Branching Bolts.", "Pierce II ticked: remove Branching Bolts.") + link("Branching Bolts"));
  if (own("mom") && +S.ch.mana && +S.ch.life && +S.ch.mana <= +S.ch.life) out.push(T("Mind Over Matter com mana menor que a vida: perigoso. Teste Mental Perseverance.", "Mind Over Matter with mana below life: dangerous. Try Mental Perseverance.") + link("Mental Perseverance"));
  if (own("ab") && own("wild")) out.push(T("Wildsurge Incantation é do leveling (Storm/Plant). Depois da troca os pontos podem ir para totem/mana.", "Wildsurge Incantation is for leveling (Storm/Plant). After the swap those points can go to totem/mana.") + link("Wildsurge Incantation"));
  return out.length ? `<div class="adaptbar frame on"><b>${T("Ajustes da árvore para o seu personagem", "Tree adjustments for your character")}</b><ul>${out.map(x => `<li>${x}</li>`).join("")}</ul></div>` : "";
}
document.addEventListener("change", e => { if (e.target.id === "adaptTgl") { S.adapt = e.target.checked; store.set("adapt", S.adapt); render(); } });
