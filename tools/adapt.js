/* ------------------------------------------------ adaptar ao meu personagem */
S.adapt = store.get("adapt", true);
const clone = o => JSON.parse(JSON.stringify(o));
const chItems = () => Object.keys((S.ch && S.ch.items) || {}).filter(k => S.ch.items[k]);
const canUse = n => { const u = D.uniques.find(x => x.n === n); return !u || !u.lvl || u.lvl <= S.lv; };
const hasUse = n => !!(S.ch && S.ch.items && S.ch.items[n]) && canUse(n);
const adaptOn = () => !!S.adapt && !!S.ch && (chItems().length > 0 || (S.ch.pets || []).some(x => x.on && x.b >= 0) || Object.values(S.ch.sk || {}).some(Boolean));
const setItemsRaw = pid => (A.sets[pid] ? A.sets[pid][S.mode] : A.guide[pid]) || [];
const isAuraBeast = g => /^Tame Beast/.test(g.skill) && !/Silverfist|Zekoa/.test(g.skill);
const isWarrior = g => /^Skeletal Warrior/.test(g.skill);
const phaseById = id => D.phases.find(x => x.id === id);
const AURA_NAME = { haste: "Haste", phys: "Physical Damage", es: "Energy Shield", heal: "Heals Allies", hinder: "Hinder", other: T("outra aura", "other aura") };

function adaptNotes() {
  const n = [];
  if (!adaptOn()) return n;
  const owned = chItems();
  for (const it of owned) if (!canUse(it)) { const u = D.uniques.find(x => x.n === it); n.push(T(`${it} ainda não entra (requer nível ${u.lvl}) — o plano usa o item anterior.`, `${it} doesn't come in yet (requires level ${u.lvl}) — the plan uses the previous item.`)); }
  if (hasUse("Sylvan's Effigy")) n.push(T("Sylvan's Effigy: companions ilimitados, Azmerian Wolf + Discipline, Skeletal Cleric como alvo do Pain Offering, sem Skeletal Warrior.", "Sylvan's Effigy: unlimited companions, Azmerian Wolf + Discipline, Skeletal Cleric as Pain Offering target, no Skeletal Warrior."));
  if (hasUse("Forgotten Warden")) n.push(T("Forgotten Warden: entra o Spirit Vessel; você perde os +100 Spirit da Enfolding Dawn.", "Forgotten Warden: Spirit Vessel comes in; you lose Enfolding Dawn's +100 Spirit."));
  if (!hasUse("Evergrasping Ring")) n.push(T("Sem Evergrasping Ring: Withering Presence vira opcional (quase não faz nada sem os anéis).", "No Evergrasping Ring: Withering Presence becomes optional (it does almost nothing without the rings)."));
  return n;
}

function adaptPhase(p) {
  if (!p || !adaptOn() || p.id !== curPhase().id) return p;
  const q = clone(p); q._adapted = true;
  const t15 = phaseById("t15"), ea = phaseById("ea");
  const pick = (ph, re) => { const g = ph && ph.gems.find(x => re.test(x.skill)); return g ? clone(g) : null; };
  const skOn = SKEL_TYPES.filter(s => S.ch.sk[s]);
  const effigy = hasUse("Sylvan's Effigy");
  const pets = (S.ch.pets || []).filter(x => x.on && x.b >= 0 && D.beasts[x.b] && !/Silverfist|Zekoa/.test(D.beasts[x.b].name));

  // ---- Sylvan's Effigy
  if (effigy) {
    const silver = q.gems.find(g => /^Tame Beast/.test(g.skill) && /Silverfist|Zekoa/.test(g.skill));
    const auraTpl = q.gems.find(isAuraBeast) || pick(t15, /^Tame Beast \(aura/) || { sup: ["Loyalty", "Last Gasp"], set: "—" };
    const keep = q.gems.filter(g => !isWarrior(g) && !isAuraBeast(g) && !/^Tame Beast \((vazia|empty)/i.test(g.skill) && !/^(Azmerian Wolf|Discipline|Skeletal Cleric|Spirit Vessel)/.test(g.skill) && g !== silver);
    const wantAuras = ["haste", "phys", "es"];
    const petList = pets.map(x => Object.assign({}, x));
    for (const a of wantAuras) if (!petList.some(x => x.aura === a)) petList.push({ b: -1, aura: a, capture: true });
    const cheapest = D.beasts.filter(b => b.cost && !/Silverfist|Zekoa|Diretusk|Antlion/.test(b.name)).sort((a, b) => a.cost - b.cost).slice(0, 3).map(b => `${b.name} (${b.cost}%)`).join(" · ");
    const auras = petList.map((x, i) => ({
      skill: `Tame Beast (${x.capture ? T("capturar: ", "capture: ") : x.b >= 0 ? D.beasts[x.b].name + " · " : ""}${T("aura", "aura")} ${AURA_NAME[x.aura] || "Haste"})`,
      set: "—", sup: ["Loyalty", "Last Gasp", "Elemental Army", "Meat Shield II"], role: T("Aura bot", "Aura bot"),
      why: (x.capture ? T(`Você ainda não marcou um beast com aura ${AURA_NAME[x.aura]}. Capture um de tipo diferente dos que já tem — mais baratos em Spirit: ${cheapest}. `, `You haven't ticked a beast with a ${AURA_NAME[x.aura]} aura yet. Capture one of a different type from the ones you have — cheapest in Spirit: ${cheapest}. `) : "") + T("Com o Effigy não há limite de companions: cada beast de aura de TIPO diferente entra enquanto houver Spirit. Loyalty + Last Gasp mantêm a aura viva; Meat Shield II e Elemental Army deixam ele durar no Atlas.", "With the Effigy there's no companion limit: each aura beast of a DIFFERENT type comes in while Spirit allows. Loyalty + Last Gasp keep the aura alive; Meat Shield II and Elemental Army make it last in the Atlas."),
      sp: "core", pr: ({ haste: 2, phys: 5, es: 7 })[x.aura] || 8 + i, cost: x.b >= 0 && D.beasts[x.b] ? `${D.beasts[x.b].cost}% ${T("do Spirit", "of Spirit")}` : T("~21–25% do Spirit", "~21–25% of Spirit") }));
    const wolf = pick(t15, /^Azmerian Wolf/); if (wolf) { wolf.sp = "core"; wolf.pr = 4; wolf.cost = T("Reserva Spirit (vem do Effigy)", "Reserves Spirit (from the Effigy)"); wolf.why = T("Vem do Sylvan's Effigy. É o 2º companion de dano: entra depois do beast de Haste e do Cleric.", "Comes from Sylvan's Effigy. It's the 2nd damage companion: after the Haste beast and the Cleric."); }
    const disc = pick(t15, /^Discipline/); if (disc) { disc.sp = "opt"; disc.pr = 1; disc.cost = T("Reserva Spirit (vem do Effigy)", "Reserves Spirit (from the Effigy)"); disc.why = T("Aura de Energy Shield que vem do Effigy. Só ative se sobrar Spirit depois dos beasts de aura.", "Energy Shield aura from the Effigy. Only activate it if Spirit is left after the aura beasts."); }
    const cleric = pick(t15, /^Skeletal Cleric/) || pick(ea, /^Skeletal Cleric/);
    if (cleric) { cleric.sp = "core"; cleric.pr = 3; cleric.cost = T("Pouco Spirit (1 minion)", "Low Spirit (1 minion)"); cleric.why = T("Com o Rattling Sceptre fora, o Skeletal Warrior some: o Cleric vira o esqueleto que o Pain Offering espeta (Sacrificial Lamb II) e ainda cura o zoo.", "With the Rattling Sceptre gone, the Skeletal Warrior disappears: the Cleric becomes the skeleton Pain Offering skewers (Sacrificial Lamb II) and heals the zoo."); }
    const pack = pick(t15, /^Wolf Pack/);
    if (pack) { pack.sp = "core"; pack.pr = 6; pack.cost = T("Reserva Spirit (vários lobos = 1 companion)", "Reserves Spirit (several wolves = 1 companion)"); pack.why = T("Com o Effigy, o Wolf Pack entra como companion de dano: vários lobos contam como UM companion, Withering Touch aplica Wither (mais dano de chaos com o Evergrasping Ring) e ele soma mais um TIPO para o Muster.", "With the Effigy, Wolf Pack comes in as a damage companion: several wolves count as ONE companion, Withering Touch applies Wither (more chaos damage with Evergrasping Ring) and it adds another TYPE for Muster."); }
    const po = keep.find(g => /^Pain Offering/.test(g.skill));
    if (po) {
      const skeletons = 1 + skOn.filter(s => s !== "Skeletal Warrior" && s !== "Skeletal Cleric").length;
      po.sup = ["Prolonged Duration II", "Sacrificial Offering", "Brutus' Brain"].concat(skeletons >= 2 ? ["Danse Macabre"] : []);
      po.why = T(`Alvo: Skeletal Cleric. Brutus' Brain impede o espinho de morrer. ${skeletons >= 2 ? "Você marcou 2+ esqueletos: Danse Macabre funciona." : "Com só o Cleric, sem Danse Macabre (precisa de 2 esqueletos)."}`, `Target: Skeletal Cleric. Brutus' Brain keeps the spike alive. ${skeletons >= 2 ? "You ticked 2+ skeletons: Danse Macabre works." : "With only the Cleric, no Danse Macabre (needs 2 skeletons)."}`);
    }
    q.gems = [silver, ...auras, cleric, wolf, pack, disc, ...keep.filter(g => !/^Wolf Pack/.test(g.skill))].filter(Boolean);
    q.spiritNote = T("Com Sylvan's Effigy (sem limite de companions), ordem para o MÁXIMO de dano, ativando enquanto houver Spirit: 1) Silverfist (o dano) → 2) beast de Haste (acelera tudo) → 3) Skeletal Cleric (barato e libera o buff do Pain Offering) → 4) Azmerian Wolf → 5) beast de Physical → 6) Wolf Pack → 7) beast de ES (defesa). Discipline, Withering Presence e tipos extras de esqueleto (Muster) só se sobrar. Se o Spirit ficar negativo, desligue o último que entrou — nunca o macaco ou o Haste.",
      "With Sylvan's Effigy (no companion limit), order for MAXIMUM damage, activating while Spirit allows: 1) Silverfist (the damage) → 2) Haste beast (speeds everything) → 3) Skeletal Cleric (cheap and enables the Pain Offering buff) → 4) Azmerian Wolf → 5) Physical beast → 6) Wolf Pack → 7) ES beast (defence). Discipline, Withering Presence and extra skeleton types (Muster) only if Spirit is left. If Spirit goes negative, turn off the last one added — never the monkey or the Haste beast.");
    q.skeletons = { n: String(Math.max(1, 1 + skOn.filter(s => s !== "Skeletal Warrior" && s !== "Skeletal Cleric").length)), types: ["Skeletal Cleric"].concat(skOn.filter(s => s !== "Skeletal Warrior" && s !== "Skeletal Cleric")), note: T("Sem Rattling Sceptre não há Skeletal Warrior. O Cleric é o alvo do Pain Offering; outros tipos só se sobrar Spirit (Muster conta tipos).", "Without Rattling Sceptre there's no Skeletal Warrior. The Cleric is the Pain Offering target; other types only if Spirit is left (Muster counts types).") };
    q.tag = `${q.tag} · Sylvan's Effigy`;
  }
  // ---- Withering Presence marcado mas fora da fase
  if (S.ch.wither && !q.gems.some(g => /^Withering Presence/.test(g.skill))) {
    const wp = pick(phaseById("a4"), /^Withering Presence/);
    if (wp) { wp.sp = hasUse("Evergrasping Ring") ? "opt" : "opt"; wp.pr = 2; wp.cost = T("Reserva fixa", "Flat reservation"); wp.why = hasUse("Evergrasping Ring") ? T("Você usa Withering Presence com Evergrasping Ring: continua valendo, mas no Atlas entra depois dos companions (Despair já tira resistência a chaos).", "You use Withering Presence with Evergrasping Ring: still worth it, but in the Atlas it comes after companions (Despair already lowers chaos resistance).") : T("Sem Evergrasping Ring ele quase não faz nada: desligue.", "Without Evergrasping Ring it does almost nothing: turn it off."); q.gems.push(wp); }
  }
  // ---- Chober Chaber: Mace Strike + Einhar's Beastrite (rouba modificadores = mais dano)
  if (hasUse("Chober Chaber") && S.ch.asc && S.ch.asc.catha && !q.gems.some(g => /^Mace Strike/.test(g.skill))) {
    const ms = pick(phaseById("t15"), /^Mace Strike/);
    if (ms) { ms.sp = "free"; ms.pr = 0; ms.cost = T("Sem Spirit", "No Spirit"); ms.why = T("Você tem Chober Chaber: Mace Strike com Einhar's Beastrite finaliza raros e te dá 2 modificadores deles por 5 minutos (Haste, Extra Damage…). É dano extra de graça no mapping.", "You have Chober Chaber: Mace Strike with Einhar's Beastrite finishes rares and gives you 2 of their modifiers for 5 minutes (Haste, Extra Damage…). Free extra damage while mapping."); q.gems.push(ms); }
  }
  // ---- Forgotten Warden
  if (hasUse("Forgotten Warden") && !q.gems.some(g => /^Spirit Vessel/.test(g.skill))) {
    const sv = pick(t15, /^Spirit Vessel/);
    if (sv) { sv.sp = "core"; sv.pr = 8; sv.cost = T("Reserva Spirit (vem do Forgotten Warden)", "Reserves Spirit (from Forgotten Warden)"); q.gems.push(sv); }
  }
  // ---- sem Evergrasping Ring
  if (!hasUse("Evergrasping Ring")) for (const g of q.gems) if (/^Withering Presence/.test(g.skill)) { g.sp = "opt"; g.pr = 9; g.why = T("Você não marcou Evergrasping Ring: sem os anéis o Wither quase não aumenta o dano. Deixe desligado e use o Spirit em companions.", "You didn't tick Evergrasping Ring: without the rings Wither barely adds damage. Keep it off and spend the Spirit on companions."); }
  // ---- sem Rattling Sceptre (e sem Effigy): troque o Warrior pelo esqueleto marcado
  if (!effigy && !hasUse("Rattling Sceptre") && chItems().length) {
    const alt = skOn.find(s => s !== "Skeletal Warrior") || "Skeletal Arsonist";
    for (const g of q.gems) if (isWarrior(g) && g.sp !== "opt") { g.skill = alt; g.why = T(`Você não marcou Rattling Sceptre, então não há gem de Skeletal Warrior: use ${alt} como o esqueleto do Pain Offering (Sacrificial Lamb).`, `You didn't tick Rattling Sceptre, so there's no Skeletal Warrior gem: use ${alt} as the Pain Offering skeleton (Sacrificial Lamb).`); }
  }
  // ---- sem Effigy: usa os beasts que você marcou nas vagas de aura
  if (!effigy && pets.length) {
    let k = 0;
    for (const g of q.gems) if (isAuraBeast(g) && !/vazia|empty/i.test(g.skill) && pets[k]) { const b = D.beasts[pets[k].b]; g.skill = `Tame Beast (${b.name} · ${T("aura", "aura")} ${AURA_NAME[pets[k].aura] || "—"})`; g.cost = `${b.cost}% ${T("do Spirit", "of Spirit")}`; k++; }
  }
  // ---- 2 companions: beasts de aura além do limite viram opcionais
  if (!effigy) {
    const limit = (S.ch.tk || hasUse("Yriel's Fostering")) ? 2 : 1;
    let used = 1;
    for (const g of q.gems) if (isAuraBeast(g) && g.sp !== "free") { used++; if (used > limit) { g.sp = "opt"; g.pr = 9; g.why = T(`Seu limite é ${limit} companion(s). Este só entra com Sylvan's Effigy${limit === 1 ? " ou Trusted Kinship" : ""}.`, `Your limit is ${limit} companion(s). This one only comes in with Sylvan's Effigy${limit === 1 ? " or Trusted Kinship" : ""}.`); } }
  }
  // ---- Spirit: estimativa com o seu Spirit máximo
  const total = +S.ch.spirit || 0;
  if (total) {
    const eff = (S.ch.tk ? 1.3 : 1) * (1 + (S.ch.eg ? .25 : 0)); let used = 0;
    for (const g of q.gems.filter(g => g.sp === "core").sort((a, b) => a.pr - b.pr)) {
      let pct = null;
      if (/^Tame Beast/.test(g.skill) && /Silverfist|Zekoa/.test(g.skill)) pct = 47.4;
      else if (isAuraBeast(g)) { const m = D.beasts.find(b => b.cost && g.skill.includes(b.name)); pct = m ? m.cost : 24.9; }
      if (pct != null) { const est = pct / 100 * total / eff; used += est; g.spEst = Math.round(est); }
      g.fits = used <= total;
    }
    q.spiritUsed = Math.round(used); q.spiritTotal = total;
  }
  return q;
}

function adaptItems(pid, items) {
  if (!adaptOn() || pid !== curPhase().id) return items;
  const out = clone(items);
  const ringSlot = s => /Anel|Ring/i.test(s);
  const pool = [];
  for (const ph of PH_ORDER) for (const m of ["cheap", "full"]) for (const it of (A.sets[ph] || {})[m] || []) if (it.u || it.n === "Rattling Sceptre") pool.push(it);
  const sameSlot = (a, b) => a === b || (ringSlot(a) && ringSlot(b));
  const used = new Set();
  for (let i = 0; i < out.length; i++) {
    const it = out[i];
    if ((it.u || it.n === "Rattling Sceptre") && hasUse(it.n) && !used.has(it.n + i)) { it.have = 1; continue; }
    // o que você tem para este slot (o mais avançado na rota)
    const cands = pool.filter(c => sameSlot(c.slot, it.slot) && hasUse(c.n)).reverse();
    const pickC = cands.find(c => !(ringSlot(c.slot) && out.some((o, j) => j !== i && o.n === c.n && o.have && c.n !== "Evergrasping Ring")));
    if (pickC) { out[i] = Object.assign(clone(pickC), { slot: it.slot, have: 1, swapped: it.n }); continue; }
    if (it.u || it.n === "Rattling Sceptre") it.miss = 1;
  }
  // Effigy na offhand
  if (hasUse("Sylvan's Effigy")) {
    const eff = pool.find(c => c.n === "Sylvan's Effigy");
    const k = out.findIndex(o => /Offhand \(Set 1\)/.test(o.slot)) ;
    if (eff && k >= 0 && out[k].n !== "Sylvan's Effigy") out[k] = Object.assign(clone(eff), { slot: out[k].slot, have: 1, swapped: out[k].n });
  }
  // Giant's Blood na árvore: Treefingers não é mais necessária
  if (S.ch.gb) { const g = out.findIndex(o => o.n === "Treefingers"); if (g >= 0) { const rare = (A.sets.t15 || {})[S.mode] ? A.sets.t15[S.mode].find(o => o.slot === out[g].slot && !o.u) : null; if (rare) out[g] = Object.assign(clone(rare), { swapped: "Treefingers" }); } }
  return out;
}

function adaptBanner(kind) {
  const on = adaptOn(); const notes = adaptNotes();
  if (!chItems().length && !(S.ch.pets || []).some(x => x.on && x.b >= 0)) return `<div class="adaptbar frame"><span>${T("Marque o que você tem em <b>Meu personagem</b> e esta aba se adapta ao seu personagem.", "Tick what you have in <b>My character</b> and this tab adapts to your character.")}</span><button class="btn" type="button" data-gotab="meu">${T("Marcar agora", "Tick now")}</button></div>`;
  return `<div class="adaptbar frame ${on ? "on" : ""}"><label class="chk"><input type="checkbox" id="adaptTgl" ${S.adapt ? "checked" : ""}><span>${T("Adaptar ao que eu tenho", "Adapt to what I have")}</span></label>
    <span>${on ? T(`Mostrando o plano ajustado para ${esc(curPhase().name)} com base em Meu personagem.`, `Showing the plan adjusted for ${esc(curPhase().name)} based on My character.`) : T("Mostrando o plano padrão da fase.", "Showing the phase's default plan.")}</span>
    ${on && notes.length ? `<ul>${notes.map(x => `<li>${esc(x)}</li>`).join("")}</ul>` : ""}
    <button class="btn" type="button" data-gotab="meu">${T("Editar o que eu tenho", "Edit what I have")}</button></div>`;
}
function treeAdaptNotes() {
  if (!adaptOn()) return "";
  const gbId = Object.keys(A.tree.meta).find(k => A.tree.meta[k][0] === "Giant's Blood");
  const tkId = Object.keys(A.tree.meta).find(k => A.tree.meta[k][0] === "Trusted Kinship");
  const out = [];
  const twoHand = hasUse("Chober Chaber") && (hasUse("Rattling Sceptre") || hasUse("Sylvan's Effigy"));
  if (twoHand && hasUse("Treefingers") && !S.ch.gb) out.push(T("Você tem Treefingers: NÃO precisa do keystone Giant's Blood agora. Se o caminho mostrar o Giant's Blood, pule e use o ponto no próximo nó.", "You have Treefingers: you do NOT need the Giant's Blood keystone now. If the path shows Giant's Blood, skip it and use the point on the next node.") + (gbId ? ` <a href="#" data-gotree="${gbId}">Giant's Blood</a>` : ""));
  if (twoHand && !hasUse("Treefingers") && !S.ch.gb) out.push(T("Chober Chaber + sceptre sem Treefingers: pegue o keystone Giant's Blood o quanto antes.", "Chober Chaber + sceptre without Treefingers: take the Giant's Blood keystone as soon as possible.") + (gbId ? ` <a href="#" data-gotree="${gbId}">Giant's Blood</a>` : ""));
  if (S.ch.gb && hasUse("Treefingers")) out.push(T("Você já tem o keystone Giant's Blood: troque a Treefingers por luvas rare com vida/resist.", "You already have the Giant's Blood keystone: swap Treefingers for rare gloves with life/resists."));
  if (!S.ch.tk && lvOk(33)) out.push(T("Você não marcou Trusted Kinship: ele é prioridade (limite de companions e 30% more eficiência).", "You didn't tick Trusted Kinship: it's a priority (companion limit and 30% more efficiency).") + (tkId ? ` <a href="#" data-gotree="${tkId}">Trusted Kinship</a>` : ""));
  if (hasUse("Sylvan's Effigy") && !S.ch.tk) out.push(T("Com o Effigy o limite some, mas o Trusted Kinship continua valendo pelos 30% more de eficiência.", "With the Effigy the limit is gone, but Trusted Kinship is still worth it for the 30% more efficiency."));
  return out.length ? `<div class="adaptbar frame on"><b>${T("Ajustes da árvore para o seu personagem", "Tree adjustments for your character")}</b><ul>${out.map(x => `<li>${x}</li>`).join("")}</ul></div>` : "";
}
const lvOk = n => S.lv >= n;
document.addEventListener("change", e => { if (e.target.id === "adaptTgl") { S.adapt = e.target.checked; store.set("adapt", S.adapt); render(); } });
