# -*- coding: utf-8 -*-
# Aba Itens com ranking de opções por nível (uniques ou rares) — aplicado por kpatch.py sobre o template gerado (variável global t) quando GEAR tem "opts".

# 1) CSS
css = """
.opts{list-style:none;margin:2px 0 0;padding:0;display:grid;gap:8px}
.opt{display:grid;grid-template-columns:auto 34px minmax(0,1fr);gap:4px 10px;align-items:center;padding:9px 10px;border:1px solid var(--edge2);border-radius:10px;background:rgba(255,255,255,.02)}
.opt.best{border-color:rgba(114,146,202,.65);background:rgba(114,146,202,.10)}
.opt .rk{font-family:var(--ui);font-weight:800;font-size:.8rem;color:var(--mute)} .opt.best .rk{color:var(--gild-hi)}
.opt img,.opt .noimg{width:34px;height:34px;object-fit:contain}
.opt b{display:block;font-size:.95rem;line-height:1.25}
.opt small{display:block;color:var(--mute);line-height:1.4;margin-top:2px;font-size:.84rem}
.opt .ochips{grid-column:2 / -1;display:flex;gap:6px;align-items:center;flex-wrap:wrap}
.opt .ochips i{font-style:normal;color:var(--mute);font-size:.8rem}
.chip.rare{color:#e6c979;border-color:rgba(230,201,121,.4);background:rgba(230,201,121,.08)}
.chip.cost-free{color:#86efac;border-color:rgba(134,239,172,.4)} .chip.cost-cheap{color:var(--wisp);border-color:rgba(127,215,216,.35)}
.chip.cost-value{color:#e6c979;border-color:rgba(230,201,121,.4)} .chip.cost-lux{color:#d8a4ff;border-color:rgba(216,164,255,.45)}
.optnext{margin:2px 0 0;color:var(--mute);font-size:.86rem;line-height:1.4} .optnext b{color:var(--text)}
.tier.locked{opacity:.55} .tier .lk{color:var(--mute);font-size:.8rem;margin-left:6px;white-space:nowrap}
.optnone{color:var(--mute);font-size:.88rem;margin:2px 0 0}
.slot .lvnote{font-family:var(--ui);font-size:.8rem;color:var(--mute);margin:0}
"""
marker = ".slot{padding:14px;display:grid;gap:9px;align-content:start}"
assert marker in t
t = t.replace(marker, marker + css, 1)

# 2) helpers, junto de modeList
old = 'const modeList = p => S.mode === "cheap" ? p.cheap : p.full;'
new = old + """
const COSTN = { free: ["Grátis", "Free"], cheap: ["Barato", "Cheap"], value: ["Valor", "Value"], lux: ["Luxo", "Luxury"] };
const optOk = o => S.mode === "cheap" ? (o.c === "free" || o.c === "cheap") : true;
function gearRank(g, lv) {
  const list = (g.opts || []).filter(o => o.lv <= lv && optOk(o)).sort((a, b) => b.s - a.s || b.lv - a.lv);
  const best = list[0];
  const next = (g.opts || []).filter(o => o.lv > lv && optOk(o) && (!best || o.s > best.s)).sort((a, b) => a.lv - b.lv || b.s - a.s)[0];
  return { list, next };
}
function optRow(o, i) {
  const im = o.k === "u" ? uniqImg(o.n) : "";
  const c = COSTN[o.c] || COSTN.free;
  return `<li class="opt ${i === 0 ? "best" : ""}"><span class="rk">#${i + 1}</span>${im ? `<img src="${im}" alt="">` : `<span class="noimg"></span>`}<div><b>${esc(o.n)}</b><small>${esc(o.w)}</small></div>
    <span class="ochips"><span class="chip ${o.k === "u" ? "unique" : "rare"}">${o.k === "u" ? "Unique" : "Rare"}</span><span class="chip cost-${o.c}">${T(c[0], c[1])}${o.p != null && o.p >= .01 ? ` · ~${o.p} div` : ""}</span><i>${T("Nv", "Lv")} ${o.lv}</i></span></li>`;
}
function tierLock(text, lv) {                       // linha fixa (Barato/Valor/Completo) que só cita uniques de nível acima do seu: mostra o nível em vez de esconder
  const names = uniquesIn(text); if (!names.length) return 0;
  const lvs = names.map(n => (D.uniques.find(u => u.n === n) || {}).lvl);
  if (lvs.some(x => !x)) return 0;
  const min = Math.min(...lvs); return min > lv ? min : 0;
}
function tierRows(g, lv, tiers) {
  const row = (k, label, text) => { const lock = tierLock(text, lv); return `<div class="tier ${k} ${tiers.includes(k) ? "on" : ""} ${lock ? "locked" : ""}"><span class="k">${label}</span><span>${esc(text)}${lock ? ` <span class="lk">🔒 ${T("a partir do nível", "from level")} ${lock}</span>` : ""}</span></div>`; };
  return row("cheap", "Barato", g.cheap) + row("value", "Valor", g.value) + row("full", "Completo", g.full);
}
function optsBlock(g, lv) {
  const { list, next } = gearRank(g, lv);
  const top = list.slice(0, 4);
  return `<p class="lvnote">${T(`Melhores para o nível ${lv} · modo ${S.mode === "cheap" ? "barato" : "completo"} (ranking do guia)`, `Best for level ${lv} · ${S.mode === "cheap" ? "budget" : "full"} mode (guide ranking)`)}</p>
    ${top.length ? `<ol class="opts">${top.map(optRow).join("")}</ol>` : `<p class="optnone">${T("Nada deste slot nesse nível: use o que cair.", "Nothing for this slot at that level: use what drops.")}</p>`}
    ${next ? `<p class="optnext">${T("Próximo upgrade", "Next upgrade")} · ${T("Nv", "Lv")} ${next.lv}: <b>${esc(next.n)}</b></p>` : ""}`;
}"""
assert old in t
t = t.replace(old, new, 1)

# 3) card do slot: ranking no lugar das três linhas fixas quando o slot tem opções
old_t = """    <div class="tier cheap ${tiers.includes("cheap") ? "on" : ""}"><span class="k">Barato</span><span>${esc(g.cheap)}</span></div>
    <div class="tier value ${tiers.includes("value") ? "on" : ""}"><span class="k">Valor</span><span>${esc(g.value)}</span></div>
    <div class="tier full ${tiers.includes("full") ? "on" : ""}"><span class="k">Completo</span><span>${esc(g.full)}</span></div>"""
new_t = """    ${g.opts ? optsBlock(g, lvView) : tierRows(g, lvView, tiers)}"""
assert old_t in t
t = t.replace(old_t, new_t, 1)
old_u = "const u = uniquesIn(g.cheap + g.value + g.full);"
assert old_u in t
t = t.replace(old_u, "const u = g.opts ? [...new Set(g.opts.filter(o => o.k === \"u\" && A.uniqIcon[o.n]).map(o => o.n))].slice(0, 6) : uniquesIn(g.cheap + g.value + g.full);", 1)
old_v = "  const tiers = S.mode === \"cheap\" ? [\"cheap\"] : [\"value\", \"full\"];\n  return `<div class=\"sechead\"><div><h2>Itens</h2>"
assert old_v in t
t = t.replace(old_v, "  const tiers = S.mode === \"cheap\" ? [\"cheap\"] : [\"value\", \"full\"];\n  const lvView = S.gearPhase ? sel.lv[1] : S.lv;\n  return `<div class=\"sechead\"><div><h2>Itens</h2>", 1)
t = t.replace("<p>Primeiro, o set completo da fase escolhida. Depois, cada slot do barato ao completo.</p>", "<p>Cada slot mostra as melhores opções para o seu nível — uniques ou rares — em ordem de encaixe na build. Troque Barato/Completo no topo para ver as opções acessíveis ou todas.</p>", 1)
t = t.replace("<h2 style=\"font-size:1.4rem\">Slot a slot · do barato ao completo</h2>", "<h2 style=\"font-size:1.4rem\">Slot a slot · ranking para o seu nível</h2>", 1)

# 4) aba Agora: 'Compre / use' = melhor opção de cada slot para o nível atual
old_a = """<ul class="clean ${S.mode === "full" ? "gold" : ""}">${modeList(p).map(x => { const u = uniquesIn(x); return `<li><span>${esc(x)}${u.length ? `<span style="display:inline-flex;gap:4px;margin-left:6px;vertical-align:middle">${u.map(n => `<img src="${uniqImg(n)}" alt="${esc(n)}" title="${esc(n)}" style="width:26px;height:26px;object-fit:contain">`).join("")}</span>` : ""}</span></li>`; }).join("")}</ul>"""
assert old_a in t
new_a = """${D.gear.some(g => g.opts) ? `<ul class="clean ${S.mode === "full" ? "gold" : ""}">${D.gear.filter(g => g.opts).map(g => { const o = gearRank(g, S.lv).list[0]; if (!o) return ""; const im = o.k === "u" ? uniqImg(o.n) : ""; return `<li><span><small style="color:var(--mute)">${esc(g.slot)}</small> · ${esc(o.n)}${im ? `<img src="${im}" alt="" style="width:26px;height:26px;object-fit:contain;margin-left:6px;vertical-align:middle">` : ""} <span class="chip ${o.k === "u" ? "unique" : "rare"}" style="margin-left:4px">${o.k === "u" ? "Unique" : "Rare"}</span></span></li>`; }).join("")}</ul>
      <p class="optnext" style="margin-top:8px">${T("O melhor de cada slot para o nível " + S.lv + ". Veja as alternativas na aba Itens.", "The best for each slot at level " + S.lv + ". See the alternatives in the Items tab.")}</p>"""
new_a = new_a + "` : `" + old_a + "`}"          # builds sem opções por slot mantêm a lista antiga
t = t.replace(old_a, new_a, 1)

