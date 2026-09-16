/* ------------------------------------------------ meu personagem: checklist + recomendações automáticas (Oracle) */
const T = (pt, en) => LANG === "en" ? en : pt;
const OWN = [
 ["gear", "sceptre", T("Sceptre com 130+ Spirit", "Sceptre with 130+ Spirit")],
 ["gear", "wand", T("Wand com +Lightning/All Spells", "Wand with +Lightning/All Spells")],
 ["gear", "dueling", "Dueling Wand (Spellslinger)"],
 ["gear", "runeforged", T("Peças Runeforged/Runemastered (Runic Ward)", "Runeforged/Runemastered pieces (Runic Ward)")],
 ["gear", "archamu", T("Amuleto de Archmage craftado", "Crafted Archmage amulet")],
 ["gear", "Soul Mantle", "Soul Mantle"], ["gear", "Waveshaper", "Waveshaper"], ["gear", "Lavianga's Spirits", "Lavianga's Spirits"], ["gear", "Cloak of Defiance", "Cloak of Defiance"],
 ["gem", "spark", "Spark"], ["gem", "grim", "Grim Pillars"], ["gem", "bitter", "Bitter Dead"], ["gem", "archmage", "Archmage (100 Spirit)"], ["gem", "tempest", "Mana Tempest"],
 ["gem", "remnants", "Mana Remnants (30 Spirit)"], ["gem", "swarm", "Ravenous Swarm (30 Spirit)"], ["gem", "malice", "Malice"], ["gem", "sling", "Spellslinger"], ["gem", "rakiata", "Rakiata's Flow"], ["gem", "pierce", "Pierce II"],
 ["tree", "wild", "Wildsurge Incantation"], ["tree", "ab", "Ancestral Bond"], ["tree", "ei", "Efficient Inscriptions"], ["tree", "bb", "Branching Bolts"], ["tree", "mom", "Mind Over Matter"], ["tree", "mp", "Mental Perseverance"],
 ["asc", "lh", "The Lesser Harm"], ["asc", "fo", "Forced Outcome"], ["asc", "hw", "Unnamed Heartwood"], ["asc", "up", "The Unseen Path"], ["asc", "hwi", "Harmony Within"], ["asc", "er", "Entwined Realities"],
];
const CH_DEFAULT = { spirit: "", mana: "", life: "", gemLv: "", malice: "", sling: "", own: {} };
S.ch = Object.assign(JSON.parse(JSON.stringify(CH_DEFAULT)), store.get("char", {}));
if (!S.ch.own) S.ch.own = {};
const own = k => !!S.ch.own[k];
const PIDX = id => D.phases.findIndex(p => p.id === id);
const saveCh = defer => {
  store.set("char", S.ch);
  if (!defer) return render();
  clearTimeout(spTimer);
  spTimer = setTimeout(() => { const a = document.activeElement; const k = a && a.dataset.ch; render(); const n = k ? document.querySelector(`[data-ch="${k}"]`) : null; if (n) { n.focus(); const v = n.value; n.value = ""; n.value = v; } }, 450);
};
/* cálculo de totems com dados do jogo (Path of Building): 1 totem até gem nível 13, 2 a partir do 14; Heartwood/Soul Mantle +1; Ancestral Bond dobra e cada totem reserva 75 */
function totemCalc(o) {
  o = o || {};
  const c = S.ch; const spirit = +(o.spirit ?? c.spirit) || 0;
  const gemLv = +(o.gemLv ?? c.gemLv) || (S.lv >= 58 ? 14 : 1);
  const ab = o.ab ?? own("ab"), ei = o.ei ?? own("ei"), hw = o.hw ?? own("hw"), soul = o.soul ?? own("Soul Mantle");
  const base = gemLv >= 14 ? 2 : 1;
  const limit = (base + (hw ? 1 : 0) + (soul ? 1 : 0)) * (ab ? 2 : 1);
  const per = 75 / (1 + (ei ? .2 : 0));
  const others = [];
  if (o.remnants ?? own("remnants")) others.push(["Mana Remnants", 30]);
  if (o.archmage ?? own("archmage")) others.push(["Archmage", 100]);
  if (o.swarm ?? own("swarm")) others.push(["Ravenous Swarm", 30]);
  if ((o.malice ?? own("malice")) && +c.malice) others.push(["Malice", +c.malice]);
  if ((o.sling ?? own("sling")) && +c.sling) others.push(["Spellslinger", +c.sling]);
  const otherSum = others.reduce((a, x) => a + x[1], 0);
  const freeForTotems = spirit - otherSum;
  const fit = ab ? Math.max(0, Math.min(limit, Math.floor(freeForTotems / Math.ceil(per)))) : 0;
  const used = otherSum + fit * Math.ceil(per);
  return { spirit, gemLv, base, limit, per, perR: Math.ceil(per), others, otherSum, fit, used, left: spirit - used, ab, ei, hw, soul };
}
function charRecs() {
  const c = S.ch, lv = S.lv, p = curPhase(), pi = PIDX(p.id), R = [];
  const add = (lvl, t, d, tab) => R.push({ lvl, t, d, tab });
  const tc = totemCalc();
  const swapIdx = PIDX("sw");
  const spirit = +c.spirit || 0, mana = +c.mana || 0, life = +c.life || 0;
  // ---- troca para totem
  if (!own("ab") && lv >= 40) {
    const need = own("ei") ? 210 : 255;
    const miss = [];
    if (!spirit) miss.push(T("informe seu Spirit máximo", "enter your max Spirit"));
    else if (spirit < need) miss.push(T(`Spirit ${spirit}/${need}`, `Spirit ${spirit}/${need}`));
    if (!own("sceptre")) miss.push(T("sceptre com 130+ Spirit", "sceptre with 130+ Spirit"));
    if (!own("wand")) miss.push(T("wand com +Lightning/All Spells", "wand with +Lightning/All Spells"));
    if (miss.length) add(pi >= swapIdx ? "bad" : "warn", T("Ainda não dá para trocar para totem", "Not ready to swap to totems yet"), T("Falta: ", "Missing: ") + miss.join(" · ") + T(". O Lowepe recomenda ficar no setup anterior o máximo possível.", ". Lowepe recommends staying on the previous setup as long as possible."), "totem");
    else add("tip", T("Pronto para a troca", "Ready for the swap"), T(`Com ${spirit} Spirit cabem ${totemCalc({ ab: true }).fit} totem(s). Guarde gold e pontos para Ancestral Bond${own("ei") ? "" : " e Efficient Inscriptions"}.`, `With ${spirit} Spirit, ${totemCalc({ ab: true }).fit} totem(s) fit. Keep gold and points for Ancestral Bond${own("ei") ? "" : " and Efficient Inscriptions"}.`), "totem");
  }
  if (own("ab")) {
    if (!spirit) add("warn", T("Informe seu Spirit máximo", "Enter your max Spirit"), T("Sem esse número não dá para calcular quantos totems cabem.", "Without it we can't calculate how many totems fit."), "meu");
    else if (tc.fit < 3) add("warn", T(`Só cabem ${tc.fit} totem(s)`, `Only ${tc.fit} totem(s) fit`), T(`Cada totem custa ${tc.perR} Spirit e você reserva ${tc.otherSum} em outras skills. ${own("ei") ? "" : "Efficient Inscriptions baixa para 63 por totem. "}No boss, desligue o Mana Remnants para caber mais um.`, `Each totem costs ${tc.perR} Spirit and you reserve ${tc.otherSum} on other skills. ${own("ei") ? "" : "Efficient Inscriptions lowers it to 63 per totem. "}On bosses, turn off Mana Remnants to fit one more.`), "totem");
    else add("ok", T(`${tc.fit} totems cabem no seu Spirit`, `${tc.fit} totems fit your Spirit`), T(`Limite ${tc.limit} · ${tc.perR} Spirit cada · sobram ${tc.left}.`, `Limit ${tc.limit} · ${tc.perR} Spirit each · ${tc.left} left.`), "totem");
    if (spirit && tc.fit < tc.limit && tc.left >= 0) add("tip", T(`Seu limite é ${tc.limit}, mas o Spirit só dá ${tc.fit}`, `Your limit is ${tc.limit}, but Spirit only allows ${tc.fit}`), T(`Faltam ${tc.perR - tc.left} Spirit para o próximo totem.`, `${tc.perR - tc.left} Spirit short of the next totem.`), "totem");
    if (spirit && tc.fit >= tc.limit && tc.left >= tc.perR) add("tip", T("Spirit sobrando, limite atingido", "Spare Spirit, limit reached"), T(`Sobram ${tc.left}. ${tc.hw || tc.soul ? "" : "Unnamed Heartwood ou Soul Mantle dão +1 no limite (vira +2 com Ancestral Bond). "}${own("archmage") ? "" : "Ou ative o Archmage (100)."}`, `${tc.left} left. ${tc.hw || tc.soul ? "" : "Unnamed Heartwood or Soul Mantle add +1 to the limit (+2 with Ancestral Bond). "}${own("archmage") ? "" : "Or activate Archmage (100)."}`), "totem");
    if (tc.limit <= 2) add("warn", T(`Limite de totems só ${tc.limit}`, `Totem limit only ${tc.limit}`), T("Gem do Spell Totem nível 14+ (2 base), Unnamed Heartwood ou Soul Mantle aumentam o limite.", "A level 14+ Spell Totem gem (2 base), Unnamed Heartwood or Soul Mantle raise the limit."), "totem");
    if (!own("ei") && spirit && spirit < 255) add("tip", T("Efficient Inscriptions", "Efficient Inscriptions"), T("Com menos de 255 Spirit, pegue Efficient Inscriptions: cada totem cai de 75 para 63.", "With under 255 Spirit, take Efficient Inscriptions: each totem drops from 75 to 63."), "arvore");
    if (own("swarm")) add("tip", T("Ravenous Swarm ainda ativo", "Ravenous Swarm still active"), T("Depois da troca ele não faz parte da build: os 30 Spirit rendem mais em totems.", "After the swap it's not part of the build: those 30 Spirit are better spent on totems."), "skills");
  } else if (pi >= swapIdx && lv >= 51) add("bad", T("Sem Ancestral Bond", "No Ancestral Bond"), T("Sem ele o Spell Totem pede 3 charges por totem. Se ainda não tem o Spirit, selecione 'Ato 4' em 'Onde você está' e continue no leveling.", "Without it Spell Totem needs 3 charges per totem. If you don't have the Spirit yet, pick 'Act 4' in 'Where you are' and keep leveling."), "arvore");
  // ---- skills de Runic Ward
  if ((own("grim") || own("bitter")) && !own("runeforged")) add("bad", T("Grim Pillars/Bitter Dead sem Runic Ward", "Grim Pillars/Bitter Dead without Runic Ward"), T("Eles gastam Runic Ward, não mana. Sem peças Runeforged/Runemastered o totem não lança: use Spark até lá.", "They spend Runic Ward, not mana. Without Runeforged/Runemastered pieces the totem can't cast: use Spark until then."), "gear");
  if (own("grim") && own("runeforged") && pi < PIDX("w1") && own("ab")) add("tip", T("Você já pode usar Grim Pillars", "You can already use Grim Pillars"), T("Tem a gem e Runic Ward: troque o Spark pelo setup Grim Pillars + Bitter Dead (aba Skills adapta).", "You have the gem and Runic Ward: swap Spark for the Grim Pillars + Bitter Dead setup (the Skills tab adapts)."), "skills");
  if (!own("grim") && pi >= PIDX("w1")) add("warn", T("Fase de Grim Pillars sem a gem", "Grim Pillars phase without the gem"), T("Grim Pillars vem de Expedition/Remnants (só a partir do Ato 4). Enquanto isso, fique no Spark.", "Grim Pillars comes from Expedition/Remnants (only from Act 4). Meanwhile, stay on Spark."), "skills");
  // ---- árvore
  if (own("pierce") && own("bb")) add("bad", T("Pierce II com Branching Bolts", "Pierce II with Branching Bolts"), T("O Lowepe avisa: se usar Pierce II, não pegue Branching Bolts.", "Lowepe warns: if you use Pierce II, don't take Branching Bolts."), "arvore");
  if (own("mom") && mana && life && mana <= life) add("bad", T("Mind Over Matter com mana menor que a vida", "Mind Over Matter with mana below life"), T(`Mana ${mana} x vida ${life}: todo dano sai da mana primeiro. Suba mana ou volte para Mental Perseverance.`, `Mana ${mana} vs life ${life}: all damage comes from mana first. Raise mana or go back to Mental Perseverance.`), "arvore");
  if (own("hwi") && mana && life && mana <= life) add("warn", T("Harmony Within inativo", "Harmony Within inactive"), T("Ele só protege quando a mana atual é maior que a vida atual.", "It only protects when current mana is higher than current life."), "asc");
  if (own("archmage") && !mana) add("tip", T("Informe sua mana máxima", "Enter your max mana"), T("Archmage e Zenith dependem da mana: com o número o app mostra o limite de 90% do Zenith.", "Archmage and Zenith depend on mana: with the number the app shows Zenith's 90% threshold."), "totem");
  if (own("wild") && own("ab") && pi >= PIDX("ea")) add("tip", "Wildsurge Incantation", T("Serviu para Storm/Plant no leveling. Com totems, veja se os pontos rendem mais em nós de totem/mana.", "It served Storm/Plant while leveling. With totems, check whether those points are better on totem/mana nodes."), "arvore");
  // ---- ascendência por nível
  const ascNeed = [["lh", "The Lesser Harm", 22], ["fo", "Forced Outcome", 36], ["up", "The Unseen Path", 66]];
  for (const [k, n, need] of ascNeed) if (lv >= need && !own(k)) add("warn", T(`Falta a ascendência ${n}`, `Missing ascendancy ${n}`), T(`Disponível por volta do nível ${need - 2}.`, `Available around level ${need - 2}.`), "asc");
  if (own("ab") && !own("hw") && !own("Soul Mantle") && (+c.gemLv || 0) < 14) add("warn", "Unnamed Heartwood", T("Sem Heartwood, sem Soul Mantle e com a gem abaixo do nível 14, o limite é só 2 totems.", "Without Heartwood, without Soul Mantle and with the gem below level 14, the limit is only 2 totems."), "asc");
  if (own("hw") && own("Soul Mantle")) add("tip", T("Heartwood + Soul Mantle", "Heartwood + Soul Mantle"), T("A Soul Mantle já dá o +1 totem: o Lowepe troca o Heartwood por Harmony Within na semana 1.", "Soul Mantle already gives the +1 totem: Lowepe swaps Heartwood for Harmony Within in week 1."), "asc");
  // ---- itens da fase
  const want = setItemsRaw(p.id).filter(it => it.u && !/Charm/.test(it.slot));
  const missing = want.filter(it => !own(it.n));
  if (missing.length) add("warn", T(`Faltam ${missing.length} unique(s) do set da fase`, `${missing.length} unique(s) of the phase set missing`), missing.map(it => `${it.n}${it.price != null ? " " + fmtPrice(it.price) : ""}`).join(" · "), "gear");
  // ---- quests de Spirit
  const ACT = { a1: 1, a2: 2, a3: 3, a4: 4, sw: 5, int: 5, ea: 6, w1: 6, fin: 6 }; const act = ACT[p.id] || 1;
  const actNum = q => { const m = String(q.act).match(/\d+/); return m ? +m[0] : 5; };
  const spq = D.quests.map((q, i) => ({ q, i })).filter(o => /Spirit/.test(o.q.reward) && !S.done["q:" + o.i] && actNum(o.q) < act);
  if (spq.length) add("warn", T("Quests de Spirit que ficaram para trás", "Spirit quests left behind"), spq.map(o => `${o.q.boss} (${o.q.reward})`).join(" · ") + T(" — cada Spirit conta para os totems.", " — every Spirit point counts for totems."), "quests");
  const order = { bad: 0, warn: 1, tip: 2, ok: 3 };
  return { recs: R.sort((a, b) => order[a.lvl] - order[b.lvl]), tc };
}
function vMeu() {
  const c = S.ch, r = charRecs(), tc = r.tc;
  const icon = { bad: "✖", warn: "!", tip: "➜", ok: "✔" };
  const box = ([grp, k, label]) => { const u = D.uniques.find(x => x.n === k); const im = u ? uniqImg(k) : gemImg(label.split(" (")[0]) || supImg(label.split(" (")[0]); return `<label class="chk"><input type="checkbox" data-own="${esc(k)}" ${own(k) ? "checked" : ""}><span>${im ? `<img src="${im}" alt="">` : ""}${esc(label)}</span>${u && u.price != null ? `<small class="px">${fmtPrice(u.price)}</small>` : ""}</label>`; };
  const grp = g => OWN.filter(o => o[0] === g).map(box).join("");
  const num = (k, label, ph) => `<label class="field"><span>${label}</span><input type="number" min="0" data-ch="${k}" value="${esc(c[k])}" placeholder="${ph || ""}"></label>`;
  return `<div class="sechead"><div><h2>${T("Meu personagem", "My character")}</h2><p>${T("Marque o que você tem. As recomendações e as abas Skills, Itens, Árvore e Totems & Mana se adaptam na hora ao seu Spirit, mana e ao que você marcou. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items, Tree and Totems & Mana tabs adapt instantly to your Spirit, mana and what you ticked. Everything is saved in this browser.")}</p></div></div>
  <div class="stat charstat"><div><b>${tc.ab ? tc.fit : "—"}</b><span>${T("totems que cabem", "totems that fit")}</span></div><div><b>${tc.limit}</b><span>${T("limite de totems", "totem limit")}</span></div><div><b>${tc.ab ? tc.perR : "—"}</b><span>${T("Spirit por totem", "Spirit per totem")}</span></div><div><b>${tc.spirit ? tc.left : "—"}</b><span>${T("Spirit sobrando", "Spirit left")}</span></div><div><b>${+c.mana ? Math.round(+c.mana * .9) : "—"}</b><span>${T("mana p/ Zenith (90%)", "mana for Zenith (90%)")}</span></div></div>
  <div class="charwrap">
    <div class="panel frame recs"><h3>${T("Recomendações para você agora", "Recommendations for you now")}</h3>
      ${r.recs.length ? r.recs.map(x => `<div class="rec ${x.lvl}" ${x.tab && x.tab !== "meu" ? `data-gotab="${x.tab}"` : ""}><span class="ri">${icon[x.lvl]}</span><div><b>${esc(x.t)}</b><small>${esc(x.d)}</small></div></div>`).join("") : `<p style="color:var(--mute)">${T("Preencha o formulário ao lado.", "Fill in the form.")}</p>`}
    </div>
    <div class="grid" style="gap:14px">
      <div class="panel frame"><h3>${T("Números do personagem", "Character numbers")}</h3>
        <div class="grid g2" style="gap:10px">${num("spirit", T("Spirit máximo", "Max Spirit"))}${num("mana", T("Mana máxima", "Max mana"))}${num("life", T("Vida máxima", "Max life"))}${num("gemLv", T("Nível da gem Spell Totem", "Spell Totem gem level"), T("ex.: 16", "e.g. 16"))}${num("malice", T("Spirit do Malice (se usa)", "Malice Spirit (if used)"))}${num("sling", T("Spirit do Spellslinger (se usa)", "Spellslinger Spirit (if used)"))}</div>
      </div>
      <div class="panel frame"><h3>${T("Árvore e ascendência", "Tree and ascendancy")}</h3><div class="chkgrid">${grp("tree")}${grp("asc")}</div></div>
      <div class="panel frame"><h3>${T("Gems que eu tenho/uso", "Gems I have/use")}</h3><div class="chkgrid">${grp("gem")}</div></div>
      <div class="panel frame"><h3>${T("Itens que eu tenho", "Items I have")}</h3><div class="chkgrid items">${grp("gear")}</div></div>
    </div>
  </div>`;
}
document.addEventListener("change", e => { const t = e.target; if (t.dataset && t.dataset.own !== undefined && t.closest && t.closest("#v-meu")) { S.ch.own[t.dataset.own] = t.checked; saveCh(); } });
document.addEventListener("input", e => { const t = e.target; if (t.dataset && t.dataset.ch && t.closest && t.closest("#v-meu, #v-totem")) { S.ch[t.dataset.ch] = t.value; saveCh(true); } });
