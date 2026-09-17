/* ------------------------------------------------ aba da mecânica da build (kit) */
S.sp = { total: 0, zoo: [] };
function spCalc() {
  const tc = buffCalc(); S.sp.total = tc.spirit || 0;
  return { used: tc.used, free: tc.free, pct: tc.pct, rows: tc.rows };
}
S.mechCount = store.get("mechCount", {});
function mechSection(sec) {
  const h = sec.h ? `<h3>${esc(sec.h)}</h3>` : "";
  const p = sec.p ? `<p style="margin:0 0 12px;color:var(--mute)">${esc(sec.p)}</p>` : "";
  if (sec.type === "cards") return `<div class="grid g2 stagger" style="margin-top:16px">${sec.cards.map(([t, b]) => `<div class="panel frame"><h3>${esc(t)}</h3><p style="margin:0">${esc(b)}</p></div>`).join("")}</div>`;
  if (sec.type === "steps") return `<div class="panel frame" style="margin-top:16px">${h}${p}<ol style="margin:0;padding-left:20px;display:grid;gap:8px">${sec.steps.map(([t, b]) => `<li><b class="ui" style="color:var(--gild-hi)">${esc(t)}</b>${b ? ` — ${esc(b)}` : ""}</li>`).join("")}</ol></div>`;
  if (sec.type === "table") return `<div class="panel frame" style="margin-top:16px">${h}${p}<div class="tablewrap"><table><thead><tr>${sec.cols.map(c => `<th>${esc(c)}</th>`).join("")}</tr></thead><tbody>${sec.rows.map(r => `<tr>${r.map((c, i) => `<td${i === 0 ? ' class="num"' : ""}>${esc(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div></div>`;
  if (sec.type === "rotation") return `<div class="grid g2 stagger" style="margin-top:16px">${sec.blocks.map(([t, steps]) => `<div class="panel frame"><h3>${esc(t)}</h3><ol style="margin:0;padding-left:20px;display:grid;gap:6px">${steps.map(s => `<li>${esc(s)}</li>`).join("")}</ol></div>`).join("")}</div>`;
  if (sec.type === "timeline") return `<div class="panel frame" style="margin-top:16px">${h}${p}<ol class="clean" style="display:grid;gap:10px;list-style:none;padding:0;margin:0">${sec.items.map(it => { const on = S.lv >= it.lv; const next = !on && sec.items.find(x => S.lv < x.lv) === it; return `<li style="display:grid;grid-template-columns:auto 1fr;gap:12px;align-items:start;opacity:${on || next ? 1 : .6}"><span class="chip ${on ? "gold" : next ? "wisp" : ""}">${T("Nv", "Lv")} ${it.lv}</span><div><b class="ui">${esc(it.t)}</b>${next ? ` <span class="chip wisp">${T("próximo", "next")}</span>` : ""}<br><span style="color:var(--mute)">${esc(it.d)}</span></div></li>`; }).join("")}</ol></div>`;
  if (sec.type === "counter") {
    const picked = sec.items.filter(([k]) => S.mechCount[k]).length, val = Math.min(sec.cap || 1e9, picked * sec.per);
    return `<div class="panel frame" style="margin-top:16px">${h}${p}<div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px">${sec.items.map(([k, label]) => { const im = gemImg(label) || supImg(label); return `<label class="chk"><input type="checkbox" data-mcount="${esc(k)}" ${S.mechCount[k] ? "checked" : ""}><span>${im ? `<img src="${im}" alt="">` : ""}${esc(label)}</span></label>`; }).join("")}</div>
      <div class="rec ${picked ? "ok" : "tip"}"><span class="ri">${picked ? "✔" : "➜"}</span><div><b>${esc(sec.result.replace("{n}", picked).replace("{v}", val))}</b><small>${esc(sec.text || "")}</small></div></div></div>`;
  }
  if (sec.type === "spirit") {
    const tc = buffCalc(), R = 62, Lc = 2 * Math.PI * R, pct = tc.spirit ? Math.min(1, tc.used / tc.spirit) : 0;
    const st = !tc.spirit ? ["warn", T("Informe seu Spirit máximo", "Enter your max Spirit")] : tc.free < 0 ? ["bad", T(`Faltam ${-tc.free} de Spirit`, `${-tc.free} Spirit short`)] : ["ok", T(`Cabe tudo: sobram ${tc.free}`, `Everything fits: ${tc.free} left`)];
    return `<div class="spirit" style="margin-top:16px"><div class="panel frame">${h}${p}
      <label class="field"><span>${T("Spirit máximo", "Max Spirit")}</span><input type="number" min="0" data-ch="spirit" value="${esc(S.ch.spirit)}"></label>
      <div style="margin-top:10px;display:grid;gap:4px">
        ${CHAR.halve ? `<label class="chk"><input type="checkbox" data-own="${esc(CHAR.halve)}" ${own(CHAR.halve) ? "checked" : ""}><span>${esc(CHAR.halveLabel || CHAR.halve)}</span></label>` : ""}
        ${(CHAR.buffs || []).map(b => { const im = gemImg(b.name); return `<label class="chk"><input type="checkbox" data-own="${esc(b.key)}" ${own(b.key) ? "checked" : ""}><span>${im ? `<img src="${im}" alt="">` : ""}${esc(b.name)} · ${Math.ceil(b.cost * tc.mult)} Spirit${b.note ? ` <small style="color:var(--faint)">${esc(b.note)}</small>` : ""}</span></label>`; }).join("")}
      </div></div>
      <div class="panel frame" style="display:grid;gap:12px;align-content:start">
        <div class="gauge"><svg viewBox="0 0 160 160" aria-hidden="true"><circle cx="80" cy="80" r="${R}" fill="none" stroke="var(--edge)" stroke-width="16"/><circle cx="80" cy="80" r="${R}" fill="none" stroke="${tc.free < 0 ? "var(--accent2)" : "var(--accent)"}" stroke-width="16" stroke-dasharray="${(Lc * pct).toFixed(1)} ${Lc.toFixed(1)}" transform="rotate(-90 80 80)" stroke-linecap="round"/></svg><div><b>${tc.used}</b><small>/ ${tc.spirit || "—"} Spirit</small></div></div>
        <div class="rec ${st[0]}"><span class="ri">${{ ok: "✔", warn: "!", bad: "✖" }[st[0]]}</span><div><b>${esc(st[1])}</b><small>${esc(sec.note || "")}</small></div></div>
      </div></div>`;
  }
  return "";
}
function vMech() {
  const M = D.mech || { title: "", intro: "", sections: [] };
  return `<div class="sechead"><div><h2>${esc(M.title)}</h2><p>${esc(M.intro)}</p></div></div>${M.sections.map(mechSection).join("")}`;
}
document.addEventListener("change", e => { const t = e.target; if (t.dataset && t.dataset.mcount !== undefined) { S.mechCount[t.dataset.mcount] = t.checked; store.set("mechCount", S.mechCount); render(); } });
/* quando usar: status pelo que você marcou */
const TIMING_KEY = D.timingKey || {};
