# -*- coding: utf-8 -*-
# Painel "Joias" na aba Árvore e anel dourado nos jewel sockets do mapa — aplicado por kpatch.py sobre o template gerado (variável global t).
css = """
.nrow.ahead{opacity:.72} .nrow small{display:block;color:var(--mute);line-height:1.4;margin-top:2px} .nrow .rk{font-family:var(--ui);font-weight:800;font-size:.8rem;color:var(--gild-hi);min-width:1.2em;text-align:center}
.jw-note{margin:2px 0 8px;padding:0 6px;color:var(--mute);font-size:.86rem;line-height:1.4}
"""
marker = ".optnone{"
assert marker in t, "css marker"
t = t.replace(marker, css.strip("\n") + "\n" + marker, 1)

# 1) helper
anchor = "function vArvore() {"
assert anchor in t
helper = '''function jewelsPanel(pid) {
  const idx = id => TREE_ORDER.indexOf(id);
  const phaseName = id => (D.phases.find(p => p.id === id) || {}).name || "";
  return `<div class="plate">${T("Joias e jewel sockets", "Jewels and jewel sockets")}</div>
  <p class="jw-note">${T("Cada joia vai no socket indicado — anel dourado no mapa da árvore. Clique para centralizar.", "Each jewel goes in the socket shown — gold ring on the tree map. Click to centre it.")}</p>
  <div class="nlist">${A.jewels.map((j, i) => { const im = j.u ? uniqImg(j.n) : ""; const on = j.first && idx(j.first) <= idx(pid);
    return `<div class="nrow k3 ${on ? "" : "ahead"}" data-gotree="${j.node}">${im ? `<img src="${im}" alt="">` : `<img alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==">`}<div><b>${i + 1}. ${esc(j.n)} <span class="chip ${j.u ? "unique" : "rare"}" style="font-size:.7rem">${j.u ? "Unique" : "Rare"}</span></b>
      <small>${T("Socket perto de", "Socket near")} <span style="color:var(--text)">${esc(j.near || "?")}</span>${j.first ? ` · ${on ? T("já alocado nesta fase", "allocated in this phase") : T("aloque na fase", "allocate in phase")} ${on ? "" : esc(phaseName(j.first))}` : ""}${j.via ? ` · ${T("socket aberto pela joia", "socket opened by the jewel")} ${esc(j.via)}` : ""}${j.where === "s1" ? ` · Weapon Set I` : j.where === "s2" ? ` · Weapon Set II` : ""}</small>
      ${j.mods && j.mods.length ? `<small>${j.mods.map(esc).join(" · ")}</small>` : ""}${j.radius ? `<small>${T("Raio", "Radius")}: ${esc(j.radius)}${j.corrupted ? " · " + T("corrompida", "corrupted") : ""}</small>` : ""}</div></div>`; }).join("")}</div>`;
}
'''
t = t.replace(anchor, helper + anchor, 1)

# 2) painel dentro da aba (antes dos notables do meta)
old = "      ${A.metaNotables.length ? `<div class=\"divider\"></div><p class=\"label\""
assert old in t, "meta anchor"
new = "      ${A.jewels && A.jewels.length ? jewelsPanel(pid) : `<div class=\"divider\"></div><p class=\"jw-note\">${T(\"O guia de origem não define joias para esta build: use a joia que der vida, resistência ou o dano que você usa.\", \"The source guide doesn't define jewels for this build: use whatever gives life, resistances or the damage you use.\")}</p>`}\n" + old
t = t.replace(old, new, 1)

# 3) anel dourado no mapa
old = "    if (this.metaSet) {\n      for (const n of this.nodes) { if (!this.metaSet.has(n[0])) continue;"
assert old in t, "canvas anchor"
ring = """    if (typeof A !== "undefined" && A.jewels) {
      for (const j of A.jewels) { const i = this.idx.get(j.node); if (i == null) continue; const n = this.nodes[i]; const rad = Math.max(58, 6 / s) * 1.7;
        ctx.beginPath(); ctx.arc(n[1], n[2], rad, 0, Math.PI * 2); ctx.strokeStyle = "#E8C66A"; ctx.lineWidth = Math.max(3 / s, 20); ctx.shadowColor = "#E8C66A"; ctx.shadowBlur = 12 * r; ctx.stroke(); ctx.shadowBlur = 0; }
    }
"""
t = t.replace(old, ring + old, 1)

# 4) tooltip do socket mostra a joia que vai nele
old = 'el.innerHTML = `<div class="th">${esc(m[0])}</div><div class="st">${(m[1] || []).map(s => `<span>${esc(s)}</span>`).join("") || "<span>—</span>"}</div>`;'
assert old in t, "tooltip anchor"
new = ('const jw = (typeof A !== "undefined" && A.jewels || []).find(j => j.node === n[0]); const lines = jw ? [`${jw.n} · ${jw.u ? "Unique" : "Rare"}`, ...(jw.mods || [])] : (m[1] || []);\n'
       '    el.innerHTML = `<div class="th">${esc(m[0])}${jw ? " ◆" : ""}</div><div class="st">${lines.map(s => `<span>${esc(s)}</span>`).join("") || "<span>—</span>"}</div>`;')
t = t.replace(old, new, 1)
