# Patch do template: árvore por nível, barra de skills por Spirit, sockets nos itens.
t = open("app_template.html", encoding="utf-8").read()

def rep(old, new, count=1):
    global t
    assert old in t, "NOT FOUND: " + old[:90]
    t = t.replace(old, new, count)

# ---------------------------------------------------------------- CSS
rep(".gem .role{font-size:.9rem;color:var(--mute)}", """.gem .role{font-size:.9rem;color:var(--mute)}
.spc{display:inline-block;margin-top:5px;padding:2px 8px;font-family:var(--ui);font-size:.76rem;font-weight:700;border:1px solid var(--edge2);color:var(--mute)}
.spc.core{border-color:#8a6a38;color:var(--gild-hi);background:rgba(200,165,106,.1)}
.spc.free{border-color:#2f5b4c;color:#8fd9b8}
.spc.opt{border-style:dashed;color:var(--faint)}
.gem.optional{opacity:.78;border-style:dashed}
.gem.optional:hover{opacity:1}
.spgroup{display:flex;align-items:baseline;gap:10px;margin:22px 0 10px;font-family:var(--ui);font-weight:700;color:var(--gild-hi);font-size:1.02rem}
.spgroup:first-child{margin-top:0}
.spgroup small{font-weight:400;color:var(--mute);font-family:var(--body);font-size:.88rem}
.spnote{padding:12px 14px;margin-bottom:16px;border-color:#8a6a38;display:grid;grid-template-columns:auto 1fr;gap:12px;align-items:start;background:linear-gradient(90deg,rgba(200,165,106,.1),transparent)}
.spnote b{font-family:var(--display);color:var(--gild-hi);font-size:1rem}
.spnote p{margin:0;color:var(--text)}
.runes .sock-list{display:grid;gap:3px;margin-top:3px}
.runes .sock-list span::before{content:"◇ ";color:var(--gild)}
.nextpts{display:grid;gap:4px;padding:6px}
.nextpts li{display:grid;grid-template-columns:26px 1fr;gap:8px;align-items:center;cursor:pointer;padding:3px 4px}
.nextpts li:hover{background:rgba(143,208,255,.08)}
.nextpts .no{display:grid;place-items:center;width:22px;height:22px;border:1px solid #6fb2e6;color:#9fd2ff;font-family:var(--mono);font-size:.72rem;border-radius:50%}
.nextpts .nb{font-family:var(--ui);color:var(--text);font-size:.9rem;line-height:1.15}
.nextpts .nb small{display:block;color:var(--mute);font-size:.76rem}
.nextpts .nb.big{color:#9fd2ff;font-weight:700}
.ptsrow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;padding:8px 10px;border-top:1px solid var(--edge)}
.ptsrow input{width:74px}
.ptsrow .btn{padding:4px 10px}
""")

# ---------------------------------------------------------------- estado da árvore por nível
rep("function gemDiff(phase) {", """const questPts = lv => { let q = 0; for (const [l, p] of A.quest || []) if (lv >= l) q = p; return q; };
const autoPts = lv => Math.max(0, lv - 1 + questPts(lv));
const ptsAt = lv => (S.ptsOv != null && S.ptsOvLv === lv) ? S.ptsOv : autoPts(lv);
const nodeName = id => ((A.tree.meta[id] || [])[0]) || String(id);
function treeState(pid, lvBased) {
  const O = A.order[pid]; const i = TREE_ORDER.indexOf(pid);
  const pts = lvBased ? ptsAt(S.lv) : O.n;
  const m = O.o.slice(0, Math.min(pts, O.o.length));
  const next = lvBased ? O.o.slice(m.length, m.length + 8) : [];
  const prevIds = i > 0 ? new Set(A.alloc[TREE_ORDER[i - 1]].m) : null;
  const phaseSet = new Set(A.alloc[pid].m);
  const mk = id => { const mm = A.tree.meta[id] || []; return { id, n: mm[0] || id, s: mm[1] || [], k: A.nodeKind[id] || 0, ic: A.passiveIcon[id], new: prevIds ? !prevIds.has(id) : true, ahead: !phaseSet.has(id) }; };
  return { m, next, pts, phaseN: O.n, extra: Math.max(0, pts - O.o.length), notables: m.filter(id => A.nodeKind[id]).map(mk), nextList: next.map(mk), prevIds };
}
function gemDiff(phase) {""")

# ---------------------------------------------------------------- gem card: chip de Spirit
rep("""  return `<article class="gem frame ${carry ? "carry" : ""}">""", """  const spTxt = g.sp === "core" ? `Spirit #${g.pr}${g.cost ? " · " + esc(g.cost) : ""}` : g.sp === "opt" ? `Só se sobrar Spirit${g.cost ? " · " + esc(g.cost) : ""}` : g.sp === "free" ? (g.cost && g.cost !== "Sem Spirit" ? `Sem Spirit · ${esc(g.cost)}` : "Sem Spirit") : "";
  return `<article class="gem frame ${carry ? "carry" : ""} ${g.sp === "opt" ? "optional" : ""}">""")
rep("""<div class="role">${esc(g.role)}${g.set && g.set !== "—" ? " · " + esc(g.set) : ""}</div></div></div>""",
    """<div class="role">${esc(g.role)}${g.set && g.set !== "—" ? " · " + esc(g.set) : ""}</div>${spTxt ? `<span class="spc ${g.sp}">${spTxt}</span>` : ""}</div></div>""")

# ---------------------------------------------------------------- gem grid agrupada por Spirit
rep("""  const mainHtml = `<div class="gems stagger">${main.map(g => gemCard(g, gemDiff(p), detailed)).join("")}</div>`;""",
    """  const df = gemDiff(p); const cards = list => `<div class="gems stagger">${list.map(g => gemCard(g, df, detailed)).join("")}</div>`;
  let mainHtml = cards(main);
  if (main.some(g => g.sp)) {
    const core = main.filter(g => g.sp === "core").sort((a, b) => a.pr - b.pr), rest = main.filter(g => !g.sp);
    const free = main.filter(g => g.sp === "free"), opt = main.filter(g => g.sp === "opt").sort((a, b) => a.pr - b.pr);
    const res = [...core, ...rest];
    mainHtml = `${p.spiritNote ? `<div class="spnote frame"><b>Spirit</b><p>${esc(p.spiritNote)}</p></div>` : ""}` +
      (res.length ? `<div class="spgroup">1 · Reservam Spirit <small>${core.length ? "ative nesta ordem; se o Spirit ficar negativo, desligue o último" : "companions e auras"}</small></div>${cards(res)}` : "") +
      (free.length ? `<div class="spgroup">2 · Não reservam Spirit <small>use sempre</small></div>${cards(free)}` : "") +
      (opt.length ? `<div class="spgroup">3 · Só se sobrar Spirit <small>entram depois, quando você ganhar mais Spirit</small></div>${cards(opt)}` : "");
  }""")

# ---------------------------------------------------------------- item card: sockets
rep("""    ${it.r && it.r.length ? `<div class="runes">Sockets / versão: ${it.r.map(esc).join(" · ")}</div>` : ""}""",
    """    ${it.r && it.r.length ? `<div class="runes"><b>${it.rs ? "Sockets (do guia)" : "Sockets (sugestão)"}</b><div class="sock-list">${it.r.map(x => `<span>${esc(x)}</span>`).join("")}</div>${it.rs ? "" : '<small style="color:var(--faint)">Sem socket? Artificer\\'s Orb adiciona um.</small>'}</div>` : ""}""")

# ---------------------------------------------------------------- painel lateral
rep("""  const nt = A.notables[p.id];
  const prog""", """  const nt = A.notables[p.id]; const ts = treeState(p.id, true);
  const prog""")
rep("""  const gems = p.gems.filter(g => !(g.until && S.lv >= g.until));""",
    """  const rank = g => g.sp === "core" ? g.pr : g.sp === "free" ? 50 : g.sp === "opt" ? 100 + g.pr : 40;
  const gems = p.gems.filter(g => !(g.until && S.lv >= g.until)).slice().sort((a, b) => rank(a) - rank(b));""")
rep("""  const newN = nt.list.filter(n => n.new && n.k !== 3);
  const phaseIdx""", """  const newN = ts.notables.filter(n => n.new && n.k !== 3);
  const phaseIdx""")
rep("""<small class="label" style="font-size:.7rem">${esc(g.role)}</small>""",
    """<small class="label" style="font-size:.7rem">${g.sp === "core" ? `Spirit #${g.pr} · ` : g.sp === "opt" ? "Se sobrar Spirit · " : g.sp === "free" ? "Sem Spirit · " : ""}${esc(g.role)}</small>""")
rep("""      ${sideSec("tree", "Passivas", `${nt.count} pontos`, `""",
    """      ${sideSec("tree", "Passivas", `${ts.m.length} pontos`, `
        ${ts.nextList.length ? `<span class="label">Próximos pontos</span><ol class="nextpts" style="margin:0;padding:0;list-style:none">${ts.nextList.slice(0, 4).map((n, k) => `<li data-gotree="${n.id}"><span class="no">${k + 1}</span><span class="nb ${n.k ? "big" : ""}">${esc(n.n)}</span></li>`).join("")}</ol>` : ""}""")

# ---------------------------------------------------------------- agora
rep("""  const newN = A.notables[p.id].list.filter(n => n.new && n.k !== 3);""",
    """  const newN = treeState(p.id, true).notables.filter(n => n.new && n.k !== 3);""")

# ---------------------------------------------------------------- TreeView: próximos pontos
rep("""  setAlloc(sets, prevIds) {""", """  setNext(ids) { this.next = ids || []; this.nextSet = new Set(this.next); this.draw(); }
  setAlloc(sets, prevIds) {""")
rep("""    if (this.hover) {
      const [id, x, y, k] = this.hover;""", """    if (this.next && this.next.length) {
      for (const e of this.edges) {
        const na = this.nextSet.has(e.a), nb = this.nextSet.has(e.b);
        if ((na && (nb || this.alloc.has(e.b))) || (nb && this.alloc.has(e.a))) { ctx.setLineDash([60, 40]); ctx.strokeStyle = "#8fd0ff"; ctx.lineWidth = Math.max(2.4 / s, 16); ctx.stroke(e.p); ctx.setLineDash([]); }
      }
      this.next.forEach((id, k) => { const n = this.nodes[this.idx.get(id)]; if (!n) return; const rad = Math.max(n[3] === 2 ? 80 : n[3] ? 52 : 30, 5 / s) * 1.25;
        ctx.beginPath(); ctx.arc(n[1], n[2], rad, 0, Math.PI * 2); ctx.fillStyle = "rgba(20,40,60,.9)"; ctx.fill(); ctx.strokeStyle = "#8fd0ff"; ctx.lineWidth = Math.max(2 / s, 12); ctx.stroke();
        ctx.save(); ctx.setTransform(r, 0, 0, r, 0, 0); ctx.font = "700 12px 'IBM Plex Mono', monospace"; ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillStyle = "#cfe9ff";
        ctx.fillText(String(k + 1), n[1] * s + this.ox, n[2] * s + this.oy); ctx.restore(); });
    }
    if (this.hover) {
      const [id, x, y, k] = this.hover;""")

# ---------------------------------------------------------------- aba árvore
rep("""  const nt = A.notables[pid]; const name = pid === "uber" ? "Bossing (endgame)" : D.phases.find(p => p.id === pid).name;""",
    """  const nt = A.notables[pid]; const name = pid === "uber" ? "Bossing (endgame)" : D.phases.find(p => p.id === pid).name;
  const lvBased = pid === phaseOf(S.lv).id; const ts = treeState(pid, lvBased);""")
rep("""        <span class="chip gold" style="margin-left:auto">${nt.count} principais${nt.s1 ? ` · ${nt.s1} Set I · ${nt.s2} Set II` : ""}</span>
      </div>""", """        <span class="chip gold" style="margin-left:auto">${lvBased ? `Nível ${S.lv}: ${ts.m.length} pontos` : `Fase completa: ${ts.m.length} pontos`}</span>
      </div>
      ${lvBased ? `<div class="ptsrow"><span class="label">Pontos que você tem</span><input type="number" min="0" max="140" id="ptsIn" value="${ts.pts}" aria-label="Pontos de passiva"><button class="btn" type="button" id="ptsAuto">Automático (${autoPts(S.lv)})</button><small style="color:var(--mute)">Automático = nível − 1 + pontos de quest (≈). Se no jogo for diferente, digite o seu número.</small></div>` : `<div class="ptsrow"><small style="color:var(--mute)">Mostrando a fase inteira. Selecione a sua fase atual para ver os pontos do seu nível e os próximos.</small></div>`}""")
rep("""<span><i style="background:transparent;border:2px solid #7FD8B0"></i>Novo nesta fase</span></div>""",
    """<span><i style="background:transparent;border:2px solid #7FD8B0"></i>Novo nesta fase</span>${lvBased ? '<span><i style="background:transparent;border:2px dashed #8fd0ff"></i>Próximos pontos (numerados)</span>' : ""}</div>""")
rep("""      <div class="plate">Notables · ${esc(name)}</div>
      <div class="nlist">${nt.list.filter(n => n.k !== 3).map(n => `<div class="nrow k${n.k} ${n.new ? "new" : ""}" data-gotree="${n.id}"><img src="${ic(n.ic) || ""}" alt=""><div><b>${esc(n.n)} ${n.pass ? '<span class="chip" style="font-size:.7rem">só passagem</span>' : ""}${n.new ? '<span class="chip wisp" style="font-size:.7rem">novo</span>' : ""}${n.set !== "m" ? ` <span class="chip ${n.set}" style="font-size:.7rem">${n.set === "s1" ? "Set I" : "Set II"}</span>` : ""}</b><small>${esc(n.s.join(" · "))}</small></div></div>`).join("")}""",
    """      ${ts.nextList.length ? `<div class="plate">Próximos pontos</div><ol class="nextpts" style="margin:0;list-style:none">${ts.nextList.map((n, k) => `<li data-gotree="${n.id}"><span class="no">${k + 1}</span><span class="nb ${n.k ? "big" : ""}">${esc(n.n)}<small>${esc((n.s || []).join(" · ").slice(0, 90))}</small></span></li>`).join("")}</ol>` : ""}
      ${ts.extra ? `<p style="padding:6px 10px;color:var(--gild-hi);margin:0">Você tem ${ts.extra} ponto(s) além do caminho completo do guia: coloque em vida, Spirit ou resistência perto do caminho.</p>` : ""}
      <div class="plate">Notables · ${esc(name)}${lvBased ? ` (nível ${S.lv})` : ""}</div>
      <div class="nlist">${ts.notables.filter(n => n.k !== 3).map(n => `<div class="nrow k${n.k} ${n.new ? "new" : ""}" data-gotree="${n.id}"><img src="${ic(n.ic) || ""}" alt=""><div><b>${esc(n.n)} ${n.new ? '<span class="chip wisp" style="font-size:.7rem">novo</span>' : ""}${n.ahead ? '<span class="chip bear" style="font-size:.7rem">da próxima fase</span>' : ""}</b><small>${esc(n.s.join(" · "))}</small></div></div>`).join("")}""")
rep("""${nt.list.find(x => x.id === n.id) ? ' <span class="chip gold" style="font-size:.7rem">no guia</span>' : ""}""",
    """${ts.m.includes(n.id) ? ' <span class="chip gold" style="font-size:.7rem">no guia</span>' : ""}""")
rep("""  const al = A.alloc[pid]; TV.setAlloc(al, i > 0 ? prevIds : null);
  requestAnimationFrame(() => TV.fit([...al.m, ...al.s1, ...al.s2]));""",
    """  const al = A.alloc[pid]; const ts = treeState(pid, pid === phaseOf(S.lv).id);
  TV.setAlloc({ m: ts.m, s1: al.s1, s2: al.s2 }, i > 0 ? prevIds : null); TV.setNext(ts.next); TV.fitIds = [...ts.m, ...ts.next];
  requestAnimationFrame(() => TV.fit(TV.fitIds));""")
rep("""else if (a === "fit") TV.fit([...al.m, ...al.s1, ...al.s2]);""", """else if (a === "fit") TV.fit(TV.fitIds || al.m);""")

# ---------------------------------------------------------------- input de pontos
rep("""  if (t.id === "addRow")""", """  if (t.id === "ptsAuto") { S.ptsOv = null; render(); return; }
  if (t.id === "addRow")""")
open("app_template.html", "w", encoding="utf-8").write(t)
print("patched")
