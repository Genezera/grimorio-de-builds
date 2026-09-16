/* Forbidden Rites challenge grimoire — rendering, progress, omen planner, motion. */
(() => {
  const D = window.RITES, U = window.RT, LANG = document.documentElement.lang.startsWith('pt') ? 'pt' : 'en';
  const ART = '../shared/art/rites/';
  const img = n => `${ART}${n}.webp`;
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fmt = (n, d = 2) => Number(n).toLocaleString(LANG === 'pt' ? 'pt-BR' : 'en-US', { maximumFractionDigits: d });

  /* ---------- storage */
  const KEY = 'rites1:';
  const load = (k, def) => { try { const v = localStorage.getItem(KEY + k); return v == null ? def : JSON.parse(v); } catch { return def; } };
  const save = (k, v) => { try { localStorage.setItem(KEY + k, JSON.stringify(v)); } catch { /* private mode */ } };
  const S = { done: load('done', {}), level: load('level', 1), reliq: load('reliq', 0), trees: load('trees', { ritual: 0, delirium: 0, abyss: 0 }), hc: load('hc', false), nolow: load('nolow', false) };
  const on = k => !!S.done[k];

  /* ---------- progress per challenge */
  const CH = Object.fromEntries(D.challenges.map(c => [c.id, c]));
  function progress(id) {
    switch (id) {
      case 'riteseeker': return D.rites.filter(r => r.bosses.every((b, i) => on(`rite:${r.id}:${i}`))).length;
      case 'hunter': return D.rares.filter((r, i) => on(`rare:${i}`)).length;
      case 'ascendant': return D.trials.filter(t => on(`trial:${t.id}`)).length;
      case 'master': return Math.min(90, +S.level || 0);
      case 'reliquarian': return Math.min(50, +S.reliq || 0);
      case 'nameless': return D.omens.filter(o => on(`omen:${o.name}`)).length;
      case 'cartographer': return D.trees.filter(t => (+S.trees[t.id] || 0) >= t.max).length;
      case 'vanquisher': return D.bosses.filter(b => on(`boss:${b.id}`)).length;
    }
    return 0;
  }
  const complete = id => progress(id) >= CH[id].goal;
  const totalDone = () => D.challenges.filter(c => complete(c.id)).length;

  /* ---------- small pieces */
  const ring = (p, size = 44, label = '') => {
    const r = size / 2 - 4, c = 2 * Math.PI * r, v = Math.max(0, Math.min(1, p));
    return `<svg class="ring" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" aria-hidden="true"><circle cx="${size / 2}" cy="${size / 2}" r="${r}" class="rt"/><circle cx="${size / 2}" cy="${size / 2}" r="${r}" class="rv" stroke-dasharray="${(c * v).toFixed(1)} ${c.toFixed(1)}" transform="rotate(-90 ${size / 2} ${size / 2})"/>${label ? `<text x="50%" y="54%" text-anchor="middle" dominant-baseline="middle">${label}</text>` : ''}</svg>`;
  };
  const chk = (key, label, extra = '') => `<label class="chk ${on(key) ? 'on' : ''}"><input type="checkbox" data-k="${esc(key)}" ${on(key) ? 'checked' : ''}><span class="gem" aria-hidden="true"></span><span class="lbl">${label}</span>${extra}</label>`;
  const icon = (n, cls = '') => `<img class="ico ${cls}" src="${img(n)}" alt="" loading="lazy" decoding="async">`;

  /* ---------- hero + rewards */
  function hero() {
    const n = totalDone(), end = new Date(D.leagueEnd), days = Math.ceil((end - Date.now()) / 864e5);
    return `<section class="hero" id="top">
      <div class="hero-copy">
        <p class="kicker"><span class="dia"></span>${esc(U.kicker)}</p>
        <h1><span class="h1a">${esc(U.h1a)}</span> <span class="h1b">${esc(U.h1b)}</span></h1>
        <p class="sub">${esc(U.sub)}</p>
        <p class="lead">${esc(U.lead)}</p>
        <div class="cta"><a class="btn primary" href="#riteseeker">${esc(U.start)} <span aria-hidden="true">→</span></a><a class="btn" href="#rewards">${esc(U.rewards)}</a></div>
        <p class="ends">${days > 0 ? `${esc(U.ends)} <b>${days}</b> ${esc(U.days)}` : esc(U.ended)} · <span class="saved">${esc(U.saved)}</span></p>
      </div>
      <div class="hero-sigil" aria-hidden="true">
        <svg class="circle c1" viewBox="0 0 400 400"><circle cx="200" cy="200" r="190"/><circle cx="200" cy="200" r="160"/><g>${Array.from({ length: 24 }, (_, i) => `<line x1="200" y1="14" x2="200" y2="${i % 3 ? 30 : 42}" transform="rotate(${i * 15} 200 200)"/>`).join('')}</g><polygon points="200,40 339,280 61,280"/><polygon points="200,360 61,120 339,120"/></svg>
        <img class="totem" src="${img('totem')}" alt="" decoding="async">
        <div class="count">${ring(n / 8, 132, '')}<b>${n}<small>/8</small></b><span>${esc(U.progress)}</span></div>
      </div>
    </section>
    <section class="rewards frame" id="rewards" aria-labelledby="rw-h">
      <h2 id="rw-h">${esc(U.rewards)}</h2>
      <ol class="track">${Array.from({ length: 8 }, (_, i) => { const k = i + 1, rw = D.rewards.find(r => r.n === k), got = n >= k; return `<li class="${got ? 'got' : ''} ${rw ? 'big' : ''}"><span class="step"><i>${k}</i></span>${rw ? `<figure>${icon(rw.img)}<figcaption><b>${esc(rw.name)}</b><small>${esc(rw.d)}</small><em>${got ? esc(U.unlocked) : `${esc(U.rewardAt)} ${k}`}</em></figcaption></figure>` : `<span class="piece" title="Totem">✦</span>`}</li>`; }).join('')}</ol>
      <p class="note">${esc(U.totem)}</p>
    </section>
    <section class="order frame"><h2>${esc(U.order)}</h2><ol>${U.orderSteps.map(s => `<li>${esc(s)}</li>`).join('')}</ol></section>`;
  }

  /* ---------- nav */
  const nav = () => `<nav class="chnav" id="challenges" aria-label="${esc(U.nav)}"><div class="chnav-in">${D.challenges.map(c => { const p = progress(c.id) / c.goal; return `<a href="#${c.id}" data-nav="${c.id}" class="${complete(c.id) ? 'ok' : ''}">${ring(p, 30)}<span>${esc(c.name.replace('The ', ''))}</span></a>`; }).join('')}</div></nav>`;

  /* ---------- tools per challenge */
  function tool(c) {
    switch (c.kind) {
      case 'rites': return `<div class="rites">${D.rites.map(r => { const all = r.bosses.every((b, i) => on(`rite:${r.id}:${i}`)); return `<details class="rite ${all ? 'ok' : ''}" ${all ? '' : ''}><summary><span class="act">${esc(r.act)}</span><b>${esc(r.name)}</b><span class="mini">${r.bosses.filter((b, i) => on(`rite:${r.id}:${i}`)).length}/${r.bosses.length}</span></summary>
        <button type="button" class="btn sm" data-rite="${r.id}">${esc(U.allRite)}</button>
        <div class="tbl"><table><thead><tr><th></th><th>${esc(U.boss)}</th><th>${esc(U.area)}</th><th>${esc(U.reward)}</th></tr></thead><tbody>${r.bosses.map((b, i) => `<tr class="${on(`rite:${r.id}:${i}`) ? 'on' : ''}"><td>${chk(`rite:${r.id}:${i}`, '<span class="sr">✓</span>')}</td><td data-l="${esc(U.boss)}"><b>${esc(b[0])}</b></td><td data-l="${esc(U.area)}">${esc(b[1])}</td><td data-l="${esc(U.reward)}">${esc(b[2])}</td></tr>`).join('')}</tbody></table></div></details>`; }).join('')}</div>`;
      case 'rares': {
        const acts = [...new Set(D.rares.map(r => r.act))];
        return `<div class="rares">${acts.map(a => `<div class="actgroup"><h4>${esc(a)}</h4>${D.rares.map((r, i) => r.act !== a ? '' : `<div class="rare ${on(`rare:${i}`) ? 'on' : ''}">${chk(`rare:${i}`, `<b>${esc(r.name)}</b><small>${esc(r.area)}${r.poi && r.poi !== '—' ? ` · ${esc(r.poi)}` : ''}</small>`)}</div>`).join('')}</div>`).join('')}</div>`;
      }
      case 'trials': return `<div class="trials">${D.trials.map(t => `<div class="trial ${on(`trial:${t.id}`) ? 'on' : ''}">${icon(t.img, 'big')}<div>${chk(`trial:${t.id}`, `<b>${esc(t.name)}</b> <span class="pts">+${t.pts} ${esc(U.trialPts)}</span>`)}<p>${esc(t.how)}</p></div></div>`).join('')}</div>
        <details class="chaos"><summary>${icon('tile-chaos', 'banner')}<b>${esc(U.chaos)}</b></summary><ul>${D.chaos055.map(x => `<li>${esc(x)}</li>`).join('')}</ul></details>`;
      case 'level': return `<div class="numtool"><label>${esc(U.level)} <input type="number" min="1" max="100" data-num="level" value="${esc(S.level)}"></label><div class="bar"><i style="width:${Math.min(100, S.level / 90 * 100)}%"></i></div><span>${Math.min(S.level, 90)}/90</span></div>`;
      case 'counter': return `<div class="numtool"><button type="button" class="btn sm" data-step="reliq:-1" aria-label="−1">−</button><label>${esc(U.count)} <input type="number" min="0" max="999" data-num="reliq" value="${esc(S.reliq)}"></label><button type="button" class="btn sm" data-step="reliq:1" aria-label="+1">+</button><div class="bar"><i style="width:${Math.min(100, S.reliq / 50 * 100)}%"></i></div><span>${Math.min(S.reliq, 50)}/50</span></div>`;
      case 'omens': return omenPlanner();
      case 'trees': return `<div class="trees">${D.trees.map(t => { const v = +S.trees[t.id] || 0; return `<div class="tree ${v >= t.max ? 'on' : ''}">${icon(t.img, 'big')}<div><b>${esc(t.name)}</b><small>${esc(t.where)}</small><div class="numtool slim"><button type="button" class="btn sm" data-step="tree:${t.id}:-1" aria-label="−1">−</button><input type="number" min="0" max="${t.max}" data-tree="${t.id}" value="${v}" aria-label="${esc(t.name)} ${esc(U.points)}"><button type="button" class="btn sm" data-step="tree:${t.id}:1" aria-label="+1">+</button><span>/${t.max}</span></div><div class="bar"><i style="width:${v / t.max * 100}%"></i></div></div></div>`; }).join('')}</div>`;
      case 'bosses': return `<div class="bosses">${D.bosses.map(b => `<article class="boss ${on(`boss:${b.id}`) ? 'on' : ''}"><header>${icon(b.img, 'big')}<div><span class="mech">${esc(b.mech)}</span>${chk(`boss:${b.id}`, `<b>${esc(b.name)}</b>`)}</div></header>
        <div class="keys"><figure>${icon(b.key)}<figcaption>${esc(U.key)}</figcaption></figure><figure>${icon(b.drop)}<figcaption>${esc(U.drop)}</figcaption></figure></div>
        <h5>${esc(U.unlock)}</h5><ol>${b.steps.map(s => `<li>${esc(s)}</li>`).join('')}</ol><p class="tip">${esc(b.tip)}</p></article>`).join('')}</div>`;
    }
    return '';
  }

  function omenRows() {
    return D.omens.map(o => ({ ...o, total: (o.price || 0) + (o.trigPrice || 0), used: on(`omen:${o.name}`), blocked: (S.hc && o.risk === 'death') || (S.nolow && o.risk === 'risk') }));
  }
  function omenPlanner() {
    const rows = omenRows(), used = rows.filter(r => r.used).length, need = Math.max(0, 18 - used);
    const plan = rows.filter(r => !r.used && !r.blocked).sort((a, b) => a.total - b.total).slice(0, need);
    const planSet = new Set(plan.map(p => p.name)), cost = plan.reduce((a, r) => a + r.total, 0);
    const sorted = [...rows].sort((a, b) => (b.used - a.used) || (planSet.has(b.name) - planSet.has(a.name)) || (a.total - b.total));
    return `<div class="planner">
      <div class="plan-head"><div class="plan-sum">${ring(used / 18, 56, `${used}`)}<div><b>${esc(U.plan)}</b><span>${esc(U.planLeft)} <b>${need}</b> · ${esc(U.planCost)}: <b>≈ ${fmt(cost, 2)} div</b></span></div></div>
      <div class="toggles"><label class="sw"><input type="checkbox" data-flag="hc" ${S.hc ? 'checked' : ''}><i></i>${esc(U.hc)}</label><label class="sw"><input type="checkbox" data-flag="nolow" ${S.nolow ? 'checked' : ''}><i></i>${esc(U.nolow)}</label></div></div>
      <div class="tbl"><table class="omens"><thead><tr><th>${esc(U.used)}</th><th>${esc(U.omen)}</th><th>${esc(U.trigger)}</th><th title="${esc(U.total)}">${esc(U.cost)}</th></tr></thead><tbody>
      ${sorted.map(r => `<tr class="${r.used ? 'on' : ''} ${planSet.has(r.name) ? 'plan' : ''} ${r.blocked ? 'blocked' : ''}"><td>${chk(`omen:${r.name}`, '<span class="sr">✓</span>')}</td><td data-l="${esc(U.omen)}"><span class="om">${icon(r.img)}<b>${esc(r.name)}</b></span>${r.risk === 'death' ? '<em class="warn">☠</em>' : r.risk === 'risk' ? '<em class="warn">♥</em>' : ''}</td><td data-l="${esc(U.trigger)}">${esc(r.how)}${r.trig ? `<small> + ${esc(r.trig)}</small>` : ''}</td><td data-l="${esc(U.cost)}" class="num">${r.price == null ? '—' : `${fmt(r.total, r.total < .1 ? 3 : 2)} div`}</td></tr>`).join('')}
      </tbody></table></div>
      <p class="note">${esc(U.exch)} ${esc(D.reviewed)} · ${esc(U.total)}.</p></div>`;
  }

  /* ---------- challenge section */
  function section(c, i) {
    const p = progress(c.id), pct = p / c.goal, ok = complete(c.id);
    return `<section class="ch frame ${ok ? 'complete' : ''}" id="${c.id}" aria-labelledby="h-${c.id}" style="--i:${i}">
      <div class="ch-art" style="--art:url('${img(c.art)}')"><span class="num">${String(i + 1).padStart(2, '0')}</span></div>
      <header class="ch-head">${icon(c.icon, 'sigil')}<div class="ch-title"><h2 id="h-${c.id}">${esc(c.name)}</h2><p class="req"><span>${esc(U.req)}:</span> “${esc(c.req)}”</p><p class="reqpt">${esc(c.reqpt)}</p>
        <div class="chips"><span class="chip">${esc(U.phase)}: ${esc(c.phase)}</span><span class="chip">${esc(U.effort)}: ${esc(c.effort)}</span>${ok ? `<span class="chip ok">✓ ${esc(U.done)}</span>` : ''}</div></div>
        <div class="ch-prog">${ring(pct, 76, `${p}`)}<small>${esc(U.of)} ${c.goal}</small></div></header>
      <div class="ch-body">
        <div class="col steps"><h3>${esc(U.how)}</h3><ol>${c.steps.map(s => `<li>${esc(s)}</li>`).join('')}</ol><h3 class="t2">${esc(U.tips)}</h3><ul class="tips">${c.tips.map(s => `<li>${esc(s)}</li>`).join('')}</ul></div>
        <div class="col tool"><h3>${esc(U.where)}</h3>${tool(c)}</div>
      </div></section>`;
  }

  const mechanics = () => `<section class="mechs" id="mechanics"><h2>${esc(U.mech)}</h2><p class="lead2">${esc(U.mechLead)}</p><div class="mgrid">${D.mechanics.map(m => `<article class="mech frame"><img src="${img(m.img)}" alt="" loading="lazy"><div><h3>${esc(m.t)}</h3><p>${esc(m.d)}</p></div></article>`).join('')}</div>
    <div class="items">${['sacred-bloom', 'ritual-tablet', 'jiquani-core', 'atziri-core', 'expedition-tablet'].map(n => `<figure>${icon(n)}<figcaption>${esc({ 'sacred-bloom': 'Sacred Bloom', 'ritual-tablet': 'Ritual Tablet', 'jiquani-core': "Jiquani's Soul Core", 'atziri-core': "Atziri's Soul Core", 'expedition-tablet': 'Expedition Tablet' }[n])}</figcaption></figure>`).join('')}</div></section>`;

  const footer = () => `<footer class="foot"><h2>${esc(U.sources)}</h2><ul>${D.sources.map(s => `<li><a href="${esc(s[1])}" target="_blank" rel="noopener">${esc(s[0])} ↗</a></li>`).join('')}</ul><p>${esc(U.reviewed)} ${esc(D.reviewed)} · ${esc(U.fan)}</p><button type="button" class="btn sm ghost" data-reset>${esc(U.reset)}</button></footer>`;

  /* ---------- render + events */
  const app = document.getElementById('app');
  let first = true;
  function render(keepFocus) {
    const openRites = new Set([...document.querySelectorAll('details.rite[open]')].map(d => d.querySelector('[data-rite]')?.dataset.rite));
    const chaosOpen = document.querySelector('details.chaos')?.open;
    const y = scrollY, active = document.activeElement, sel = active && (active.dataset.k ? `[data-k="${CSS.escape(active.dataset.k)}"]` : active.dataset.num ? `[data-num="${active.dataset.num}"]` : active.dataset.tree ? `[data-tree="${active.dataset.tree}"]` : active.dataset.flag ? `[data-flag="${active.dataset.flag}"]` : active.dataset.step ? `[data-step="${CSS.escape(active.dataset.step)}"]` : active.dataset.rite ? `[data-rite="${active.dataset.rite}"]` : null);
    app.innerHTML = hero() + nav() + `<div class="chlist">${D.challenges.map(section).join('')}</div>` + mechanics() + footer();
    document.querySelectorAll('details.rite').forEach(d => { if (openRites.has(d.querySelector('[data-rite]')?.dataset.rite)) d.open = true; });
    if (chaosOpen) document.querySelector('details.chaos').open = true;
    if (!first) { scrollTo(0, y); if (keepFocus && sel) document.querySelector(sel)?.focus({ preventScroll: true }); }
    first = false; observe();
  }
  app.addEventListener('change', e => {
    const t = e.target;
    if (t.dataset.k) { S.done[t.dataset.k] = t.checked; if (!t.checked) delete S.done[t.dataset.k]; save('done', S.done); burst(t); return render(true); }
    if (t.dataset.flag) { S[t.dataset.flag] = t.checked; save(t.dataset.flag, t.checked); return render(true); }
    if (t.dataset.num) { const v = Math.max(+t.min || 0, Math.min(+t.max || 999, Math.round(+t.value || 0))); S[t.dataset.num] = v; save(t.dataset.num, v); return render(true); }
    if (t.dataset.tree) { const tr = D.trees.find(x => x.id === t.dataset.tree); S.trees[tr.id] = Math.max(0, Math.min(tr.max, Math.round(+t.value || 0))); save('trees', S.trees); return render(true); }
  });
  app.addEventListener('click', e => {
    const b = e.target.closest('[data-step],[data-rite],[data-reset]'); if (!b) return;
    if (b.dataset.reset !== undefined) { if (confirm(U.resetq)) { ['done', 'level', 'reliq', 'trees', 'hc', 'nolow'].forEach(k => { try { localStorage.removeItem(KEY + k); } catch { } }); Object.assign(S, { done: {}, level: 1, reliq: 0, trees: { ritual: 0, delirium: 0, abyss: 0 }, hc: false, nolow: false }); render(); } return; }
    if (b.dataset.rite) { const r = D.rites.find(x => x.id === b.dataset.rite), all = r.bosses.every((x, i) => on(`rite:${r.id}:${i}`)); r.bosses.forEach((x, i) => { if (all) delete S.done[`rite:${r.id}:${i}`]; else S.done[`rite:${r.id}:${i}`] = true; }); save('done', S.done); burst(b); return render(true); }
    const [k, a, c] = b.dataset.step.split(':');
    if (k === 'reliq') { S.reliq = Math.max(0, Math.min(999, (+S.reliq || 0) + +a)); save('reliq', S.reliq); }
    if (k === 'tree') { const tr = D.trees.find(x => x.id === a); S.trees[a] = Math.max(0, Math.min(tr.max, (+S.trees[a] || 0) + +c)); save('trees', S.trees); }
    render(true);
  });

  /* ---------- motion: reveal, active nav, spark burst, embers */
  let io, navIo;
  function observe() {
    if (!('IntersectionObserver' in window)) return;
    if (!reduce) {
      io?.disconnect();
      io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }), { rootMargin: '0px 0px -8% 0px' });
      document.querySelectorAll('.ch,.mech,.rewards,.order').forEach(el => { if (el.getBoundingClientRect().top > innerHeight * .9) { el.classList.add('rv'); io.observe(el); } });
    }
    navIo?.disconnect();
    navIo = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { document.querySelectorAll('[data-nav]').forEach(a => a.classList.toggle('cur', a.dataset.nav === en.target.id)); const cur = document.querySelector(`[data-nav="${en.target.id}"]`); cur?.parentElement.scrollTo({ left: cur.offsetLeft - 40, behavior: reduce ? 'auto' : 'smooth' }); } }), { rootMargin: '-40% 0px -55% 0px' });
    document.querySelectorAll('.ch').forEach(s => navIo.observe(s));
  }
  function burst(el) {
    if (reduce || !el?.getBoundingClientRect) return;
    const r = el.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
    for (let i = 0; i < 10; i++) {
      const s = document.createElement('i'); s.className = 'spark'; const a = Math.PI * 2 * i / 10, d = 18 + Math.random() * 22;
      s.style.cssText = `left:${x}px;top:${y}px;--dx:${Math.cos(a) * d}px;--dy:${Math.sin(a) * d}px`;
      document.body.append(s); setTimeout(() => s.remove(), 700);
    }
  }
  function embers() {
    const cv = document.getElementById('embers'); if (!cv || reduce) return;
    const ctx = cv.getContext('2d'); let W, H, P = [], L = [], run = true;
    const size = () => { const d = Math.min(2, devicePixelRatio || 1); W = innerWidth; H = innerHeight; cv.width = W * d; cv.height = H * d; ctx.setTransform(d, 0, 0, d, 0, 0); const n = Math.round(Math.min(70, W * H / 24000)); while (P.length < n) P.push(mk(true)); P.length = n; while (L.length < 5) L.push(loc()); };
    const cols = [[155, 107, 255], [201, 173, 255], [241, 179, 92], [184, 50, 63]];
    const mk = f => ({ x: Math.random() * W, y: f ? Math.random() * H : H + 10, r: .6 + Math.random() * 2.2, vy: -(.15 + Math.random() * .5), ph: Math.random() * 6, a: .25 + Math.random() * .6, c: cols[Math.random() < .62 ? 0 : Math.random() < .55 ? 1 : Math.random() < .7 ? 2 : 3] });
    const loc = () => ({ x: -40 - Math.random() * W, y: Math.random() * H * .8, v: .6 + Math.random() * 1.4, w: Math.random() * 6, s: .6 + Math.random() * .7 });
    size(); addEventListener('resize', size, { passive: true });
    document.addEventListener('visibilitychange', () => { run = !document.hidden; if (run) requestAnimationFrame(t); });
    function t() {
      if (!run) return;
      ctx.clearRect(0, 0, W, H); ctx.globalCompositeOperation = 'lighter';
      for (const p of P) { p.ph += .012; p.y += p.vy; p.x += Math.sin(p.ph) * .35; if (p.y < -12) Object.assign(p, mk(false)); const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 6); g.addColorStop(0, `rgba(${p.c},${p.a})`); g.addColorStop(1, `rgba(${p.c},0)`); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p.x, p.y, p.r * 6, 0, 6.29); ctx.fill(); }
      ctx.globalCompositeOperation = 'source-over'; ctx.fillStyle = 'rgba(6,4,10,.75)';
      for (const l of L) { l.x += l.v * 1.6; l.w += .35; const fy = l.y + Math.sin(l.w * .3) * 6; if (l.x > W + 60) Object.assign(l, loc(), { x: -40 }); ctx.save(); ctx.translate(l.x, fy); ctx.scale(l.s, l.s); ctx.beginPath(); ctx.ellipse(0, 0, 5, 1.6, 0, 0, 6.29); ctx.fill(); const f = Math.sin(l.w) * 3; ctx.beginPath(); ctx.ellipse(-1, -2 - f * .3, 4, 1.1, -.5, 0, 6.29); ctx.ellipse(-1, 2 + f * .3, 4, 1.1, .5, 0, 6.29); ctx.fill(); ctx.restore(); }
      requestAnimationFrame(t);
    }
    requestAnimationFrame(t);
    if (matchMedia('(pointer:fine)').matches) addEventListener('pointermove', e => { const bg = document.querySelector('.totem-bg'); if (bg) bg.style.transform = `translate3d(${(e.clientX / W - .5) * -20}px,${(e.clientY / H - .5) * -14}px,0)`; }, { passive: true });
  }

  render();
  embers();
  if (location.hash) requestAnimationFrame(() => document.querySelector(location.hash)?.scrollIntoView());
})();
