function vSkills() {
  const sel = S.skillPhase ? D.phases.find(p => p.id === S.skillPhase) : curPhase();
  const current = sel.id === curPhase().id;
  const profile = S.ch.combatProfile || "clear";
  const profiles = [
    ["clear", T("Clear", "Clear"), T("Tela inteira", "Whole screen")],
    ["gasboss", T("Boss · Gas", "Boss · Gas"), T("Recomendado nv 22+", "Recommended lv 22+")],
    ["boss", T("Boss · Poisonburst", "Boss · Poisonburst"), T("Fallback simples", "Simple fallback")],
  ];
  const required = ((((CHAR.phaseSkills || {})[sel.id] || {})[profile]) || []);
  const info = CHAR.skillInfo || {};
  const status = k => k === "gas" && S.lv < 22 ? "future" : own(k) ? "have" : "miss";
  const statusText = s => s === "have" ? T("Tenho", "Owned") : s === "future" ? T("Futuro", "Future") : T("Falta", "Missing");
  const loadout = required.map(k => {
    const x = info[k] || { name: k }, st = status(k), im = gemImg(x.name);
    return `<label class="ac-skill ${st}"><input type="checkbox" data-own="${esc(k)}" data-own-kind="active" ${own(k) ? "checked" : ""} ${st === "future" ? "disabled" : ""}><span class="ac-skill-art">${im ? `<img src="${im}" alt="">` : "◇"}</span><span><b>${esc(x.name)}</b><small>${statusText(st)}</small></span></label>`;
  }).join("");
  const rotations = {
    clear: [T("Poisonburst Arrow no centro do pack; siga em movimento.", "Fire Poisonburst Arrow into the pack centre; keep moving."), T("Herald of Blood + Herald of Plague propagam a primeira morte.", "Herald of Blood + Herald of Plague propagate the first kill."), T("Plague Bearer a 100% em packs densos; Toxic Growth apenas em raros resistentes.", "Use Plague Bearer at 100% on dense packs; Toxic Growth only on tough rares.")],
    gasboss: [T("Despair e Vine Arrow antes da janela de dano, quando disponíveis.", "Use Despair and Vine Arrow before the damage window, when available."), T("Toxic Growth uma vez, centrada no boss; não relance enquanto as pústulas antigas existirem.", "Cast Toxic Growth once, centred on the boss; do not recast while the old pustules exist."), T("Gas Arrow no mesmo ponto: a nuvem mantém veneno sobre boss e pústulas.", "Put Gas Arrow on the same spot: the cloud keeps poison on boss and pustules."), T("Plague Bearer a 100%; no endgame, Archon detona e mantém pressão com os tornados.", "Use Plague Bearer at 100%; in endgame, Archon detonates and keeps pressure with tornadoes.")],
    boss: [T("Despair e Vine Arrow antes da janela de dano, quando disponíveis.", "Use Despair and Vine Arrow before the damage window, when available."), T("Toxic Growth uma vez, centrada no boss.", "Cast Toxic Growth once, centred on the boss."), T("Poisonburst de perto para a explosão de veneno alcançar as pústulas.", "Use Poisonburst at close range so its poison burst reaches the pustules."), T("Plague Bearer a 100%; no endgame, use Archon sempre que a Glory chegar a 100.", "Use Plague Bearer at 100%; in endgame, use Archon whenever Glory reaches 100.")],
  };
  const ownedCount = required.filter(k => own(k)).length;
  const gasAudit = profile === "gasboss" ? `<div class="panel frame ac-verdict"><h3>${T("Por que Gas Arrow funciona aqui", "Why Gas Arrow works here")}</h3><p>${T("A nuvem causa 70–218% do dano de ataque, dura 4 s, tem limite de 6 e envenena sem hit. Toxic Growth guarda o dano esperado dos venenos aplicados às pústulas; portanto a sobreposição é mecanicamente compatível e reduz o tempo atirando parado.", "The cloud deals 70–218% attack damage, lasts 4s, has a limit of 6 and poisons without hitting. Toxic Growth stores expected damage from poisons inflicted on its pustules; the overlap is therefore mechanically compatible and reduces stationary attack time.")}</p><p><b>${T("Não detone a nuvem.", "Do not detonate the cloud.")}</b> ${T("A explosão converte físico em fogo e exigiria Ignite/Detonator, investimento que não melhora o núcleo de caos/veneno.", "The explosion converts physical to fire and would require Ignite/Detonator investment that does not improve the chaos/poison core.")}</p><p class="ac-caveat">${T("Limite da auditoria: os dados públicos não informam a frequência interna de reaplicação da nuvem. Gas é recomendado pela cobertura e uptime; Poisonburst permanece disponível para comparar no seu personagem.", "Audit limit: public data does not state the cloud's internal reapplication frequency. Gas is recommended for coverage and uptime; Poisonburst remains available for comparison on your character.")}</p></div>` : "";
  return `<style>
    .ac-profiles{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:14px 0}.ac-profile{min-height:58px;border:1px solid var(--edge2);background:#090a10;color:var(--text);padding:9px 12px;text-align:left;cursor:pointer;font-family:var(--ui)}.ac-profile b,.ac-profile small{display:block}.ac-profile small{color:var(--mute);margin-top:3px}.ac-profile[aria-pressed=true]{border-color:#7292ca;background:linear-gradient(135deg,rgba(114,146,202,.2),rgba(127,215,216,.06));box-shadow:inset 0 -2px #7292ca}.ac-loadout{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:8px}.ac-skill{display:grid;grid-template-columns:auto 1fr;gap:9px;align-items:center;padding:9px;border:1px solid var(--edge);background:#090a10;cursor:pointer}.ac-skill input{position:absolute;opacity:0;pointer-events:none}.ac-skill-art{display:grid;place-items:center;width:38px;height:38px;border:1px solid var(--edge2);color:var(--faint)}.ac-skill-art img{width:36px;height:36px;object-fit:contain}.ac-skill b,.ac-skill small{display:block}.ac-skill small{font-family:var(--ui);font-size:.76rem;margin-top:2px}.ac-skill.have{border-color:#2f5a5b}.ac-skill.have small{color:#8fd8d9}.ac-skill.miss{border-color:rgba(224,102,79,.48)}.ac-skill.miss small{color:#ffb3a3}.ac-skill.future{opacity:.55;cursor:not-allowed}.ac-rotation{margin:0;padding-left:20px;display:grid;gap:7px}.ac-verdict{border-color:#405a85;background:linear-gradient(135deg,rgba(114,146,202,.1),transparent)}.ac-verdict p{margin:8px 0}.ac-caveat{color:var(--mute);font-size:.9rem}@media(max-width:620px){.ac-profiles{grid-template-columns:1fr}.ac-profile{min-height:48px}.ac-loadout{grid-template-columns:1fr 1fr}}@media(max-width:390px){.ac-loadout{grid-template-columns:1fr}}
  </style>
  <div class="sechead"><div><h2>${T("Skills: uma barra para cada trabalho", "Skills: one bar for each job")}</h2><p>${T("Escolha a fase e o objetivo. Marque as gems disponíveis aqui ou em Meu personagem; Agora e o painel lateral usam o mesmo estado.", "Choose the phase and goal. Tick available gems here or in My character; Now and the side panel use the same state.")}</p></div></div>
  ${phaseSel(sel.id, "skills")}
  ${current ? adaptBanner("skills") : ""}
  <div class="ac-profiles" role="group" aria-label="${T("Objetivo da barra", "Loadout goal")}">${profiles.map(([id, name, hint]) => `<button type="button" class="ac-profile" data-combat-profile="${id}" aria-pressed="${profile === id}"><b>${name}</b><small>${hint}</small></button>`).join("")}</div>
  <div class="panel frame"><h3>${T(`Barra essencial · ${ownedCount}/${required.length} disponíveis`, `Essential bar · ${ownedCount}/${required.length} available`)}</h3><div class="ac-loadout">${loadout}</div></div>
  <div class="grid g2" style="margin-top:16px"><div class="panel frame"><h3>${T("Rotação deste perfil", "Rotation for this profile")}</h3><ol class="ac-rotation">${(rotations[profile] || rotations.clear).map(x => `<li>${esc(x)}</li>`).join("")}</ol></div>${gasAudit || `<div class="panel frame"><h3>${T("Regra de troca", "Swap rule")}</h3><p>${profile === "clear" ? T("Fork e heralds servem à cobertura. Não sacrifique Concentrated Area da Toxic Growth: ela continua sendo seu botão contra raros e bosses.", "Fork and heralds serve coverage. Do not sacrifice Concentrated Area on Toxic Growth: it remains your rare and boss button.") : T("Concentrated Area fica sempre na Toxic Growth. Troque apenas o motor que aplica veneno nas pústulas: Gas para uptime, Poisonburst para simplicidade.", "Concentrated Area always stays on Toxic Growth. Only swap the engine that poisons the pustules: Gas for uptime, Poisonburst for simplicity.")}</p></div>`}</div>
  <div class="sechead" style="margin-top:28px"><div><h2 style="font-size:1.4rem">${T("Setup completo da fase", "Full phase setup")}</h2><p>${T("Abaixo ficam todas as skills, supports, reservas e alternativas. A barra essencial acima é o resumo jogável.", "Below are all skills, supports, reservations and alternatives. The essential bar above is the playable summary.")}</p></div></div>
  <div style="margin-top:14px">${gemGrid(sel, false, true)}</div>
  <div class="panel frame" style="margin-top:16px"><h3>${T("Prioridade de sockets", "Socket priority")}</h3><ol class="ac-rotation">${D.ui.socketPrio.map(x => `<li>${esc(x)}</li>`).join("")}</ol></div>`;
}

document.addEventListener("click", e => {
  const b = e.target.closest("[data-combat-profile]");
  if (!b) return;
  S.ch.combatProfile = b.dataset.combatProfile;
  S.ch.skillsConfigured = true;
  store.set("char", S.ch);
  render();
});

