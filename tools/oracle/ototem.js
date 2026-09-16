/* ------------------------------------------------ totems & mana (Oracle) */
S.sp = { total: 0, zoo: [] };
function spCalc() {
  const tc = totemCalc(); const total = tc.spirit || 0;
  S.sp.total = total;
  return { used: tc.used, free: total - tc.used, pct: total ? tc.used / total : 0, rows: [] };
}

const WARD = { "Grim Pillars": [15, 81], "Bitter Dead": [11, 59], "Repulsion": [15, 116] };
function vTotem() {
  const c = S.ch, tc = totemCalc();
  const mana = +c.mana || 0;
  const chk = (k, label, hint) => `<div class="toggle"><span class="ui">${label}${hint ? `<br><small style="color:var(--faint);font-family:var(--body)">${hint}</small>` : ""}</span><label class="switch"><input type="checkbox" data-own="${k}" ${own(k) ? "checked" : ""} aria-label="${esc(label)}"><i></i></label></div>`;
  const R = 62, Lc = 2 * Math.PI * R, pct = tc.spirit ? Math.min(1, tc.used / tc.spirit) : 0;
  const need = n => Math.ceil(n * tc.perR + tc.otherSum);
  const st = !tc.ab ? ["warn", T("Sem Ancestral Bond o Spell Totem pede 3 charges por totem. Marque Ancestral Bond para simular.", "Without Ancestral Bond Spell Totem needs 3 charges per totem. Tick Ancestral Bond to simulate.")] : !tc.spirit ? ["warn", T("Digite seu Spirit máximo.", "Enter your max Spirit.")] : tc.fit >= 3 ? ["ok", T(`${tc.fit} totems cabem · sobram ${tc.left} Spirit.`, `${tc.fit} totems fit · ${tc.left} Spirit left.`)] : ["bad", T(`Só ${tc.fit} totem(s). Faltam ${need(3) - tc.spirit} Spirit para 3.`, `Only ${tc.fit} totem(s). ${need(3) - tc.spirit} Spirit short of 3.`)];
  const manaRows = Object.entries(D.totemMana).map(([lv, m]) => `<tr><td class="num">${lv}</td><td class="num">${m}</td><td>${lv >= 14 ? 2 : 1}</td></tr>`).join("");
  return `<div class="sechead"><div><h2>${T("Totems & Mana", "Totems & Mana")}</h2><p>${T("Quantos Spell Totems cabem no seu Spirit, quanto de mana a build precisa e o craft do amuleto de Archmage. Os números vêm dos dados do jogo (Path of Building): cada totem reserva 75 Spirit com Ancestral Bond, 1 totem base até a gem nível 13 e 2 a partir do 14.", "How many Spell Totems fit your Spirit, how much mana the build needs and the Archmage amulet craft. Numbers come from game data (Path of Building): each totem reserves 75 Spirit with Ancestral Bond, 1 base totem up to gem level 13 and 2 from level 14.")}</p></div></div>
  <div class="spirit">
    <div class="panel frame">
      <div class="grid g2" style="gap:10px">
        <label class="field"><span>${T("Spirit máximo", "Max Spirit")}</span><input type="number" min="0" data-ch="spirit" value="${esc(c.spirit)}"></label>
        <label class="field"><span>${T("Nível da gem Spell Totem", "Spell Totem gem level")}</span><input type="number" min="1" max="40" data-ch="gemLv" value="${esc(c.gemLv)}" placeholder="${S.lv >= 58 ? 14 : 1}"></label>
        <label class="field"><span>${T("Spirit do Malice (se usa)", "Malice Spirit (if used)")}</span><input type="number" min="0" data-ch="malice" value="${esc(c.malice)}"></label>
        <label class="field"><span>${T("Mana máxima", "Max mana")}</span><input type="number" min="0" data-ch="mana" value="${esc(c.mana)}"></label>
      </div>
      <div style="margin-top:10px;display:grid;gap:4px">
        ${chk("ab", "Ancestral Bond", T("dobra o limite · 75 Spirit por totem", "doubles the limit · 75 Spirit per totem"))}
        ${chk("ei", "Efficient Inscriptions", T("+20% eficiência: 63 por totem", "+20% efficiency: 63 per totem"))}
        ${chk("hw", "Unnamed Heartwood", T("+1 totem", "+1 totem"))}
        ${chk("Soul Mantle", "Soul Mantle", T("+1 totem e +75 Spirit (inclua esse Spirit no campo acima)", "+1 totem and +75 Spirit (include that Spirit in the field above)"))}
        ${chk("remnants", "Mana Remnants", "30 Spirit")}${chk("archmage", "Archmage", "100 Spirit")}${chk("swarm", "Ravenous Swarm", T("30 Spirit (leveling)", "30 Spirit (leveling)"))}${chk("malice", "Malice", T("usa o valor digitado", "uses the value typed"))}
      </div>
    </div>
    <div class="panel frame" style="display:grid;gap:12px;align-content:start">
      <div class="gauge"><svg viewBox="0 0 160 160" aria-hidden="true"><circle cx="80" cy="80" r="${R}" fill="none" stroke="#1f2436" stroke-width="16"/><circle cx="80" cy="80" r="${R}" fill="none" stroke="${st[0] === "bad" ? "var(--danger)" : st[0] === "warn" ? "var(--gild)" : "var(--wisp)"}" stroke-width="16" stroke-dasharray="${Lc}" stroke-dashoffset="${Lc * (1 - pct)}" transform="rotate(-90 80 80)"/></svg><div><b>${tc.ab ? tc.fit : 0}</b><small>${T("totems", "totems")}</small></div></div>
      <div class="rec ${st[0]}"><span class="ri">${{ ok: "✔", warn: "!", bad: "✖" }[st[0]]}</span><div><b>${esc(st[1])}</b><small>${T(`Limite: (${tc.base} base${tc.hw ? " + 1 Heartwood" : ""}${tc.soul ? " + 1 Soul Mantle" : ""}) × ${tc.ab ? 2 : 1} = ${tc.limit} · por totem: ${tc.perR} · outras reservas: ${tc.otherSum}`, `Limit: (${tc.base} base${tc.hw ? " + 1 Heartwood" : ""}${tc.soul ? " + 1 Soul Mantle" : ""}) × ${tc.ab ? 2 : 1} = ${tc.limit} · per totem: ${tc.perR} · other reservations: ${tc.otherSum}`)}</small></div></div>
      <div class="tablewrap"><table><thead><tr><th>${T("Totems", "Totems")}</th><th>${T("Spirit necessário", "Spirit needed")}</th><th></th></tr></thead><tbody>${[1, 2, 3, 4, 5, 6].filter(n => n <= Math.max(4, tc.limit)).map(n => `<tr><td class="num">${n}</td><td class="num">${need(n)}</td><td>${n > tc.limit ? `<span class="chip">${T("acima do limite", "above limit")}</span>` : tc.spirit && tc.spirit >= need(n) ? `<span class="chip wisp">${T("cabe", "fits")}</span>` : ""}</td></tr>`).join("")}</tbody></table></div>
      <p style="margin:0;color:var(--faint);font-size:.86rem">${T("Guia do Lowepe: 3 totems + Mana Remnants = 210 Spirit com Efficient Inscriptions, 255 sem. Nos bosses dá para desligar o Mana Remnants para caber mais um totem. O arredondamento exato da reserva pode variar 1 ponto: confira no painel de skills.", "Lowepe's guide: 3 totems + Mana Remnants = 210 Spirit with Efficient Inscriptions, 255 without. On bosses you can turn off Mana Remnants to fit one more totem. Exact reservation rounding may vary by 1 point: check the skills panel.")}</p>
    </div>
  </div>
  <div class="grid g2" style="margin-top:16px">
    <div class="panel frame"><h3>${T("Mana", "Mana")}</h3>
      <ul class="clean gold">
        <li>${mana ? T(`Zenith I/II só dão dano acima de 90% da mana: mantenha ≥ ${Math.round(mana * .9)} de ${mana}.`, `Zenith I/II only grant damage above 90% mana: keep ≥ ${Math.round(mana * .9)} of ${mana}.`) : T("Zenith I/II só dão dano acima de 90% da mana máxima.", "Zenith I/II only grant damage above 90% of maximum mana.")}</li>
        <li>${T("Com Ancestral Bond você paga a mana do Spell Totem, não dos spells que ele lança.", "With Ancestral Bond you pay Spell Totem's mana, not the spells it casts.")}</li>
        <li>${T("Archmage: spells não canalizados custam mana extra e causam dano de raio extra baseado na mana máxima (100 Spirit).", "Archmage: non-channelled spells cost extra mana and deal extra lightning damage based on maximum mana (100 Spirit).")}</li>
        <li>${T("Mind Over Matter: todo dano sai da mana antes da vida (50% less recuperação de mana). Só com mana bem acima da vida.", "Mind Over Matter: all damage from mana before life (50% less mana recovery). Only with mana well above life.")}</li>
        <li>${T("Mana Tempest drena mana: use por último, no boss.", "Mana Tempest drains mana: use it last, on the boss.")}</li>
      </ul>
      <div class="tablewrap"><table><thead><tr><th>${T("Nível da gem", "Gem level")}</th><th>${T("Mana do Spell Totem", "Spell Totem mana")}</th><th>${T("Totems base", "Base totems")}</th></tr></thead><tbody>${manaRows}</tbody></table></div>
    </div>
    <div class="panel frame"><h3>${T("Runic Ward (Grim Pillars)", "Runic Ward (Grim Pillars)")}</h3>
      <p style="margin:0 0 8px;color:var(--mute)">${T("Grim Pillars, Bitter Dead e Repulsion gastam Runic Ward, não mana. O Runic Ward vem de itens Runeforged/Runemastered. Custo por uso (gem nível 1 → 20):", "Grim Pillars, Bitter Dead and Repulsion spend Runic Ward, not mana. Runic Ward comes from Runeforged/Runemastered items. Cost per use (gem level 1 → 20):")}</p>
      <ul class="clean">${Object.entries(WARD).map(([n, [a, b]]) => `<li><span><b class="ui">${esc(n)}</b> · ${a} → ${b} Runic Ward</span></li>`).join("")}</ul>
      <p style="margin:10px 0 0;color:var(--faint);font-size:.86rem">${T("No 0.5.5, Remnants e Expedition só aparecem a partir do Ato 4: antes não tem como conseguir Grim Pillars.", "In 0.5.5, Remnants and Expedition only appear from Act 4: before that there's no way to get Grim Pillars.")}</p>
    </div>
  </div>
  <div class="panel frame" style="margin-top:16px"><h3>${T("Craft do amuleto de Archmage (Lowepe)", "Archmage amulet craft (Lowepe)")}</h3>
    <p style="margin:0 0 10px;color:var(--danger)">${T("Pode ficar muito caro: não comece com menos de 100 div.", "Can get very expensive: don't start with under 100 div.")}</p>
    <div class="checklist">${D.craft.map((s, i) => `<label class="check ${S.done["craft:" + i] ? "done" : ""}"><input type="checkbox" data-key="craft:${i}" ${S.done["craft:" + i] ? "checked" : ""}><span><b class="ui">${i + 1}.</b> ${esc(s)}</span></label>`).join("")}</div>
  </div>`;
}
document.addEventListener("change", e => { const t = e.target; if (t.dataset && t.dataset.own !== undefined && t.closest && t.closest("#v-totem")) { S.ch.own[t.dataset.own] = t.checked; saveCh(); } });
/* quando usar: status pelo que você marcou */
const TIMING_KEY = { "Sceptre com 130+ Spirit": "sceptre", "Sceptre with 130+ Spirit": "sceptre", "Wand com +Lightning/All Spells": "wand", "Wand with +Lightning/All Spells": "wand", "Dueling Wand": "dueling", "Peças Runeforged (Runic Ward)": "runeforged", "Runeforged pieces (Runic Ward)": "runeforged", "Amuleto de Archmage": "archamu", "Archmage amulet": "archamu", "Grim Pillars": "grim", "Bitter Dead": "bitter", "Archmage": "archmage", "Mana Tempest": "tempest", "Unnamed Heartwood": "hw", "Forced Outcome": "fo", "Harmony Within": "hwi", "Ancestral Bond": "ab", "Efficient Inscriptions": "ei", "Mind Over Matter": "mom" };
