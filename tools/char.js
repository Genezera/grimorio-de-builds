/* ------------------------------------------------ meu personagem: checklist + recomendações automáticas */
const T = (pt, en) => LANG === "en" ? en : pt;
const SKEL_TYPES = ["Skeletal Warrior", "Skeletal Arsonist", "Skeletal Sniper", "Skeletal Frost Mage", "Skeletal Reaver", "Skeletal Cleric"];
const AURAS = [["none", "—", "—"], ["haste", "Haste", "Haste"], ["phys", "Physical Damage", "Physical Damage"], ["es", "Energy Shield", "Energy Shield"], ["heal", "Heals Allies", "Heals Allies"], ["hinder", "Hinder", "Hinder"], ["other", "Outra aura", "Other aura"]];
const ASC_KEYS = [["wp", "Wild Protector", 20], ["no", "The Natural Order", 33], ["catha", "The Catha's Balance", 65], ["idol", "Idolatry", 75]];
const CH_DEFAULT = { spirit: "", free: "", tk: false, eg: false, gb: false, po: false, wither: false, asc: {}, items: {}, sk: {}, pets: [{ b: 0, aura: "none", on: false }, { b: -1, aura: "none", on: false }, { b: -1, aura: "none", on: false }] };
S.ch = Object.assign(JSON.parse(JSON.stringify(CH_DEFAULT)), store.get("char", {}));
const saveCh = defer => {
  store.set("char", S.ch);
  if (S.ch.spirit !== "" && !isNaN(+S.ch.spirit)) { S.sp.total = +S.ch.spirit; store.set("sp", S.sp); }
  if (!defer) return render();
  clearTimeout(spTimer);
  spTimer = setTimeout(() => { const a = document.activeElement; const k = a && a.dataset.ch; render(); const n = k ? document.querySelector(`[data-ch="${k}"]`) : null; if (n) { n.focus(); const v = n.value; n.value = ""; n.value = v; } }, 450);
};
const ACT_OF = { a1: 1, a2: 2, a3: 3, a4: 4, int: 5, ea: 6, t15: 6, mm: 6 };
function charItemList() {
  const seen = new Map();
  for (const pid of ["a3", "a4", "int", "ea", "t15", "mm"]) for (const m of ["cheap", "full"]) for (const it of (A.sets[pid] || {})[m] || []) {
    if ((it.u || it.n === "Rattling Sceptre") && !seen.has(it.n)) seen.set(it.n, { n: it.n, pid, ic: it.ic, price: it.price });
  }
  if (!seen.has("Yriel's Fostering")) seen.set("Yriel's Fostering", { n: "Yriel's Fostering", pid: "a4", ic: null, price: (D.uniques.find(u => u.n === "Yriel's Fostering") || {}).price });
  return [...seen.values()];
}
function charRecs() {
  const c = S.ch, lv = S.lv, p = phaseOf(lv), act = ACT_OF[p.id] || 1, R = [];
  const add = (lvl, t, d, tab) => R.push({ lvl, t, d, tab });
  const has = n => !!c.items[n];
  const effigy = has("Sylvan's Effigy");
  const tk = !!c.tk || has("Yriel's Fostering");
  const limit = effigy ? Infinity : tk ? 2 : 1;
  const total = +c.spirit || 0, free = c.free === "" || c.free == null ? null : +c.free;
  const eff = (c.tk ? 1.3 : 1) * (1 + (c.eg ? .25 : 0));
  const est = pct => total && pct ? pct / 100 * total / eff : null;
  const pets = c.pets.filter(x => x.on && x.b >= 0 && D.beasts[x.b]);
  const beast = x => D.beasts[x.b];
  const isSilver = x => /Silverfist|Zekoa/.test(beast(x).name);
  const auraPets = pets.filter(x => !isSilver(x));
  const cheapAura = D.beasts.map((b, i) => ({ b, i })).filter(o => o.b.cost && !/Silverfist|Zekoa|Diretusk|Antlion/.test(o.b.name)).sort((a, b) => a.b.cost - b.b.cost);
  const skN = SKEL_TYPES.filter(s => c.sk[s]).length;
  const skMax = p.skeletons ? Math.max(...(p.skeletons.n.match(/\d+/g) || ["0"]).map(Number)) : 0;
  const skMin = p.skeletons ? +((p.skeletons.n.match(/\d+/) || ["0"])[0]) : 0;

  // ---- ascendência
  for (const [k, name, need] of ASC_KEYS) {
    if (lv >= need + 2 && !c.asc[k] && !(k === "idol" && S.mode === "cheap")) add(k === "no" || k === "catha" ? "bad" : "warn", T(`Falta a ascendência ${name}`, `Missing ascendancy ${name}`), T(`Disponível a partir do nível ~${need}.`, `Available from level ~${need}.`) + " " + ((D.ascendancy.find(a => a.node === name) || {}).why || ""), "asc");
  }
  // ---- companions
  if (lv >= 33 && !pets.some(isSilver)) add("bad", T("Capture e ative o Mighty Silverfist", "Capture and activate Mighty Silverfist"), T("Precisa da The Natural Order. Ele é o dano da build.", "Needs The Natural Order. It's the build's damage."), "zoo");
  if (lv >= 33 && !tk && !effigy) add("warn", T("Pegue o keystone Trusted Kinship", "Take the Trusted Kinship keystone"), T("Sem ele o limite é 1 companion: você não consegue ter o macaco + um beast de aura.", "Without it the limit is 1 companion: you can't run the monkey + an aura beast."), "arvore");
  if (pets.length > limit) add("bad", T(`${pets.length} companions ativos, mas o seu limite é ${limit}`, `${pets.length} active companions, but your limit is ${limit}`), T("Trusted Kinship / Yriel's Fostering: 2 companions de tipos diferentes. Mais que isso só com Sylvan's Effigy. Desative o excedente (o urso do Wild Protector não conta).", "Trusted Kinship / Yriel's Fostering: 2 companions of different types. More only with Sylvan's Effigy. Deactivate the extra one (the Wild Protector bear doesn't count)."), "zoo");
  const names = pets.map(x => beast(x).name); if (new Set(names).size < names.length) add("bad", T("Dois companions do mesmo tipo", "Two companions of the same type"), T("O limite exige tipos diferentes: troque um deles por outro beast.", "The limit requires different types: swap one for another beast."), "zoo");
  if (tk && !effigy && pets.some(isSilver) && auraPets.length === 0 && lv >= 38) add("warn", T("Capture um beast de aura (2º companion)", "Capture an aura beast (2nd companion)"), T("Mais baratos em Spirit: ", "Cheapest in Spirit: ") + cheapAura.slice(0, 4).map(o => `${o.b.name} (${o.b.cost}%)`).join(" · ") + T(". Prioridade de aura: Haste > Physical > Energy Shield.", ". Aura priority: Haste > Physical > Energy Shield."), "zoo");
  for (const x of auraPets) {
    const b = beast(x);
    if (b.cost >= 35) {
      const alt = cheapAura.find(o => /Crab/.test(o.b.name)) || cheapAura[0];
      const save = est(b.cost) != null && est(alt.b.cost) != null ? Math.round(est(b.cost) - est(alt.b.cost)) : null;
      add("tip", T(`${b.name} é um beast de aura caro (${b.cost}% do Spirit)`, `${b.name} is an expensive aura beast (${b.cost}% of Spirit)`), T(`Um ${alt.b.name} (${alt.b.cost}%) com a mesma aura libera`, `A ${alt.b.name} (${alt.b.cost}%) with the same aura frees`) + (save != null ? ` ~${save} Spirit` : T(" Spirit", " Spirit")) + T(` — dá para um esqueleto a mais ou o Withering Presence. Onde: ${alt.b.where}.`, ` — enough for another skeleton or Withering Presence. Where: ${alt.b.where}.`), "zoo");
    }
    if (x.aura === "none") add("warn", T(`Marque a aura do ${b.name}`, `Set the aura of ${b.name}`), T("Beast de aura sem aura boa não vale o Spirit. Prioridade: Haste > Physical > Energy Shield.", "An aura beast without a good aura isn't worth the Spirit. Priority: Haste > Physical > Energy Shield."), "meu");
  }
  if (auraPets.length && !auraPets.some(x => x.aura === "haste")) add("tip", T("Nenhum companion com Haste", "No companion with Haste"), T("Haste é a melhor aura. Quill Crab / Coconut Crab (Ato 4, Whakapanu Island) rolam Haste com facilidade.", "Haste is the best aura. Quill Crab / Coconut Crab (Act 4, Whakapanu Island) roll Haste easily."), "zoo");
  if (!effigy && pets.length >= 2) add("ok", T("Limite de 2 companions atingido", "2-companion limit reached"), T("O 3º companion só entra com o Sylvan's Effigy", "The 3rd companion only comes with Sylvan's Effigy") + ((D.uniques.find(u => u.n === "Sylvan's Effigy") || {}).price != null ? ` (${fmtPrice(D.uniques.find(u => u.n === "Sylvan's Effigy").price)}).` : ".") + T(" Enquanto isso, capture e guarde um Swarming Wisp / Plague Swarm com aura Physical.", " Meanwhile, capture and keep a Swarming Wisp / Plague Swarm with a Physical aura."), "uniques");
  if (effigy && pets.length < 4 && lv >= 62) add("tip", T("Com o Effigy cabem mais companions", "With the Effigy more companions fit"), T("Adicione beasts de aura de tipos diferentes (Haste, Physical, ES) enquanto houver Spirit, e o Azmerian Wolf do Effigy.", "Add aura beasts of different types (Haste, Physical, ES) while Spirit allows, plus the Effigy's Azmerian Wolf."), "zoo");
  // ---- arma
  if (has("Chober Chaber") && (has("Rattling Sceptre") || effigy) && !c.gb && !has("Treefingers")) add("bad", T("Chober Chaber + sceptre precisa de Giant's Blood", "Chober Chaber + sceptre needs Giant's Blood"), T("Use Treefingers (luvas) ou o keystone Giant's Blood na árvore.", "Use Treefingers (gloves) or the Giant's Blood keystone on the tree."), "gear");
  if (has("Chober Chaber") && (c.gb || has("Treefingers")) && !has("The Vertex")) add("warn", T("Requisitos de atributo triplicados", "Tripled attribute requirements"), T("Giant's Blood triplica os requisitos. The Vertex (versão 'Equipment has no Attribute Requirements') resolve.", "Giant's Blood triples requirements. The Vertex ('Equipment has no Attribute Requirements' version) fixes it."), "uniques");
  // ---- esqueletos / Spirit
  if (p.skeletons && lv >= 31) {
    if (skN < skMin) add("warn", T(`Esqueletos: você tem ${skN}, esta fase pede ${p.skeletons.n}`, `Skeletons: you have ${skN}, this phase asks for ${p.skeletons.n}`), p.skeletons.note, "skills");
    else if (skN > skMax) add("tip", T(`Esqueletos: ${skN} ativos, a fase pede ${p.skeletons.n}`, `Skeletons: ${skN} active, the phase asks for ${p.skeletons.n}`), T("Os extras só valem se sobrar Spirit. Se faltar, desligue o último que entrou.", "Extras are only worth it with spare Spirit. If short, turn off the last one added."), "skills");
    else add("ok", T(`Esqueletos certos para a fase (${skN})`, `Right number of skeletons for the phase (${skN})`), p.skeletons.types.join(" · "), "skills");
    if (c.po && skN === 0) add("bad", T("Pain Offering sem esqueleto", "Pain Offering without a skeleton"), T("Ele precisa de pelo menos 1 esqueleto vivo para espetar.", "It needs at least 1 living skeleton to skewer."), "skills");
    if (c.po && skN === 1) add("tip", T("Com 1 esqueleto: sem Danse Macabre", "With 1 skeleton: no Danse Macabre"), T("Use Prolonged Duration II + Sacrificial Offering no Pain Offering.", "Use Prolonged Duration II + Sacrificial Offering on Pain Offering."), "skills");
  }
  if (free != null) {
    if (free < 0) add("bad", T("Spirit negativo", "Negative Spirit"), T("Desligue o último minion que entrou (esqueleto extra antes de companion).", "Turn off the last minion you added (extra skeleton before a companion)."), "skills");
    else if (free >= 30 && p.skeletons && skN < skMax && lv >= 56) { const nxt = SKEL_TYPES.find(s => !c.sk[s] && s !== "Skeletal Cleric"); add("tip", T(`Sobram ${free} de Spirit`, `${free} Spirit left`), T(`Teste ativar mais um tipo de esqueleto (${nxt || "Cleric"}) — cada tipo é +7% more dano com Muster.`, `Try activating another skeleton type (${nxt || "Cleric"}) — each type is +7% more damage with Muster.`), "skills"); }
    else if (free >= 30 && !c.wither && lv >= 46) add("tip", T(`Sobram ${free} de Spirit`, `${free} Spirit left`), T("Cabe o Withering Presence (com 2× Evergrasping Ring).", "Withering Presence fits (with 2× Evergrasping Ring)."), "skills");
  }
  if (c.wither && !has("Evergrasping Ring")) add("warn", T("Withering Presence sem Evergrasping Ring", "Withering Presence without Evergrasping Ring"), T("O Wither só aumenta dano de chaos. Sem 2× Evergrasping Ring (chaos nos aliados) ele quase não faz nada: troque por outra coisa.", "Wither only boosts chaos damage. Without 2× Evergrasping Ring (chaos on allies) it does almost nothing: swap it."), "skills");
  // ---- itens da fase
  const want = setItems(p.id).filter(it => (it.u || it.n === "Rattling Sceptre") && !/Charm/.test(it.slot));
  const missing = want.filter(it => !has(it.n)).filter((it, i, arr) => arr.findIndex(x => x.n === it.n) === i);
  if (missing.length) add("warn", T(`Faltam ${missing.length} peça(s) do set da fase (${S.mode === "cheap" ? "barato" : "completo"})`, `${missing.length} piece(s) of the phase set missing (${S.mode === "cheap" ? "budget" : "full"})`), missing.slice(0, 5).map(it => `${it.n}${it.price != null ? " " + fmtPrice(it.price) : ""}`).join(" · "), "gear");
  else if (want.length) add("ok", T("Set da fase completo", "Phase set complete"), T("Todas as peças-chave da fase estão marcadas.", "All key pieces of the phase are checked."), "gear");
  // ---- quests de Spirit
  const actNum = q => { const m = String(q.act).match(/\d+/); return m ? +m[0] : 5; };
  const spq = D.quests.map((q, i) => ({ q, i })).filter(o => /Spirit/.test(o.q.reward) && !S.done["q:" + o.i] && actNum(o.q) < act);
  if (spq.length) add("warn", T("Quests de Spirit que ficaram para trás", "Spirit quests left behind"), spq.map(o => `${o.q.boss} (${o.q.reward})`).join(" · ") + T(". Marque na aba Quests se já fez.", ". Tick them on the Quests tab if done."), "quests");
  const order = { bad: 0, warn: 1, tip: 2, ok: 3 };
  return { recs: R.sort((a, b) => order[a.lvl] - order[b.lvl]), limit, pets, est, tk, effigy, skN, want, missing, total };
}
function vMeu() {
  const c = S.ch, r = charRecs(), p = phaseOf(S.lv);
  const items = charItemList();
  const box = (k, label, checked, extra = "") => `<label class="chk"><input type="checkbox" ${k} ${checked ? "checked" : ""}><span>${label}</span>${extra}</label>`;
  const icon = { bad: "✖", warn: "!", tip: "➜", ok: "✔" };
  const petRow = (x, i) => `<div class="petrow">
    <label class="chk"><input type="checkbox" data-pet="${i}" data-pf="on" ${x.on ? "checked" : ""}><span>${T("Ativo", "Active")}</span></label>
    <select data-pet="${i}" data-pf="b" aria-label="Beast"><option value="-1">${T("— nenhum —", "— none —")}</option>${D.beasts.map((b, bi) => b.cost ? `<option value="${bi}" ${bi === x.b ? "selected" : ""}>${esc(b.name)} (${b.cost}%)</option>` : "").join("")}</select>
    <select data-pet="${i}" data-pf="aura" aria-label="Aura">${AURAS.map(([k, pt, en]) => `<option value="${k}" ${k === x.aura ? "selected" : ""}>${T(pt, en)}</option>`).join("")}</select>
    <span class="px">${x.b >= 0 && D.beasts[x.b] && r.est(D.beasts[x.b].cost) != null ? "≈ " + Math.round(r.est(D.beasts[x.b].cost)) + " Spirit" : ""}</span></div>`;
  const petSpirit = r.pets.reduce((a, x) => a + (r.est(D.beasts[x.b].cost) || 0), 0);
  const byPhase = PH_ORDER.map(pid => ({ pid, list: items.filter(it => it.pid === pid) })).filter(g => g.list.length);
  return `<div class="sechead"><div><h2>${T("Meu personagem", "My character")}</h2><p>${T("Marque o que você já tem. As recomendações abaixo mudam na hora com base no seu nível, no modo e no que você marcou. Tudo fica salvo neste navegador.", "Tick what you already have. The recommendations below update instantly based on your level, mode and what you ticked. Everything is saved in this browser.")}</p></div></div>
  <div class="stat charstat"><div><b>${r.limit === Infinity ? "∞" : r.limit}</b><span>${T("limite de companions", "companion limit")}</span></div><div><b>${r.pets.length}</b><span>${T("companions ativos", "active companions")}</span></div><div><b>${r.total ? "≈ " + Math.round(petSpirit) : "—"}</b><span>${T("Spirit dos companions (estimado)", "companion Spirit (estimated)")}</span></div><div><b>${r.skN}</b><span>${T("esqueletos", "skeletons")} · ${T("fase pede", "phase asks")} ${esc((p.skeletons || {}).n || "0")}</span></div><div><b>${r.want.length ? `${r.want.length - r.missing.length}/${r.want.length}` : "—"}</b><span>${T("peças do set da fase", "phase set pieces")}</span></div></div>
  <div class="charwrap">
    <div class="panel frame recs"><h3>${T("Recomendações para você agora", "Recommendations for you now")}</h3>
      ${r.recs.length ? r.recs.map(x => `<div class="rec ${x.lvl}" ${x.tab && x.tab !== "meu" ? `data-gotab="${x.tab}"` : ""}><span class="ri">${icon[x.lvl]}</span><div><b>${esc(x.t)}</b><small>${esc(x.d)}</small></div></div>`).join("") : `<p style="color:var(--mute)">${T("Preencha o formulário ao lado.", "Fill in the form.")}</p>`}
    </div>
    <div class="grid" style="gap:14px">
      <div class="panel frame"><h3>${T("Spirit e keystones", "Spirit and keystones")}</h3>
        <div class="grid g2" style="gap:10px">
          <label class="field"><span>${T("Spirit máximo (painel do personagem)", "Max Spirit (character panel)")}</span><input type="number" min="0" data-ch="spirit" value="${esc(c.spirit)}"></label>
          <label class="field"><span>${T("Spirit sobrando agora (painel de skills)", "Spirit left now (skills panel)")}</span><input type="number" data-ch="free" value="${esc(c.free)}" placeholder="${T("opcional", "optional")}"></label>
        </div>
        <div class="chkgrid">${box('data-chk="tk"', "Trusted Kinship", c.tk)}${box('data-chk="eg"', "Easy Going", c.eg)}${box('data-chk="gb"', T("Giant's Blood na árvore", "Giant's Blood on tree"), c.gb)}${box('data-chk="po"', T("Uso Pain Offering", "I use Pain Offering"), c.po)}${box('data-chk="wither"', T("Uso Withering Presence", "I use Withering Presence"), c.wither)}</div>
        <div class="label" style="margin:12px 0 6px">${T("Ascendência", "Ascendancy")}</div>
        <div class="chkgrid">${ASC_KEYS.map(([k, n]) => box(`data-asc="${k}"`, n, c.asc[k])).join("")}</div>
      </div>
      <div class="panel frame"><h3>${T("Companions", "Companions")}</h3>
        <p style="margin:0 0 8px;color:var(--mute);font-size:.9rem">${T("Limite confirmado no texto do jogo: 1 base · 2 de tipos diferentes com Trusted Kinship ou Yriel's Fostering · qualquer número com Sylvan's Effigy. O urso do Wild Protector não conta.", "Limit confirmed from game text: 1 base · 2 of different types with Trusted Kinship or Yriel's Fostering · any number with Sylvan's Effigy. The Wild Protector bear doesn't count.")}</p>
        ${c.pets.map(petRow).join("")}
        <button class="btn" type="button" id="petAdd">${T("+ Companion", "+ Companion")}</button>
        <div class="label" style="margin:14px 0 6px">${T("Esqueletos ativos", "Active skeletons")}</div>
        <div class="chkgrid">${SKEL_TYPES.map(s => box(`data-sk="${s}"`, s, c.sk[s])).join("")}</div>
      </div>
      <div class="panel frame"><h3>${T("Itens que eu já tenho", "Items I already have")}</h3>
        ${byPhase.map(g => `<div class="label" style="margin:10px 0 6px">${esc(phaseName(g.pid))}</div><div class="chkgrid items">${g.list.map(it => box(`data-item="${esc(it.n)}"`, `${uniqImg(it.n) || ic(it.ic) ? `<img src="${uniqImg(it.n) || ic(it.ic)}" alt="">` : ""}${esc(it.n)}`, c.items[it.n], it.price != null ? `<small class="px">${fmtPrice(it.price)}</small>` : "")).join("")}</div>`).join("")}
      </div>
    </div>
  </div>`;
}
document.addEventListener("change", e => {
  const t = e.target; const c = S.ch; if (!t.closest || !t.closest("#v-meu, #side")) return;
  if (t.dataset.chk) { c[t.dataset.chk] = t.checked; saveCh(); }
  else if (t.dataset.asc) { c.asc[t.dataset.asc] = t.checked; saveCh(); }
  else if (t.dataset.item) { c.items[t.dataset.item] = t.checked; saveCh(); }
  else if (t.dataset.sk) { c.sk[t.dataset.sk] = t.checked; saveCh(); }
  else if (t.dataset.pet !== undefined) { const x = c.pets[+t.dataset.pet]; const f = t.dataset.pf; x[f] = f === "on" ? t.checked : f === "b" ? +t.value : t.value; if (f === "b" && +t.value >= 0 && !x.on) x.on = true; saveCh(); }
});
document.addEventListener("input", e => { const t = e.target; if (t.dataset && t.dataset.ch) { S.ch[t.dataset.ch] = t.value; saveCh(true); } });
document.addEventListener("click", e => { if (e.target.id === "petAdd") { S.ch.pets.push({ b: -1, aura: "none", on: false }); saveCh(); } });
