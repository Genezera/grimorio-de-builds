/* Loading screen + smooth transitions between pages/builds. Loaded in <head>; purely decorative and never blocks input. */
(() => {
  const root = document.documentElement;
  const qs = new URLSearchParams(location.search);
  if (navigator.webdriver && !qs.has('loader')) return;          // automated tests: no overlay
  const src = document.currentScript && document.currentScript.src;
  const art = src ? new URL('art/', src).href : 'shared/art/';
  const BUILDS = {
    silverfist: ['sf', 'Mighty Silverfist', 'Huntress · Spirit Walker'], oracle: ['or', 'Oracle Spell Totem', 'Druid · Oracle'],
    tactician: ['ta', 'Tactician Pin2Win', 'Mercenary · Tactician'], infernalist: ['in', 'Infernalist Comet', 'Witch · Infernalist'],
    acolyte: ['ac', 'Poisonburst Archon', 'Monk · Acolyte of Chayula'], pathfinder: ['pf', 'Pathfinder Decompose', 'Ranger · Pathfinder'],
    smith: ['sk', 'Smith of Kitava', 'Warrior · Smith of Kitava'], martial: ['ma', 'Oil Barrage Teleport', 'Monk · Martial Artist'],
  };
  const PAL = {"silverfist":["#07080a","#5fe3c1","#c3a066","#ecd6a3"],"oracle":["#06060c","#a58dff","#b7bfd9","#eef1fb"],"tactician":["#08080a","#ff8a3d","#c9a46a","#f0dcb0"],"infernalist":["#0a0505","#ff5b1f","#d9a36b","#f6d8b0"],"acolyte":["#07050b","#b35cff","#c3b2e6","#efe7ff"],"pathfinder":["#060906","#7fd957","#cdbb7c","#f0e3b4"],"smith":["#09070a","#ff6a13","#d08a47","#f5cf9f"],"martial":["#05070b","#4cc3ff","#e0b25c","#f7deaa"],"home":["#07070a","#c3a066","#c3a066","#ecd6a3"],"rites":["#07050c","#9b6bff","#f1b35c","#ffd894"]};   // [fundo, acento, ouro, ouro claro] — cortina sempre na paleta do destino
  const en = /(^|\/)en\.html$/.test(location.pathname);
  const HOME = ['', en ? 'Build Grimoire' : 'Grimório de Builds', 'Path of Exile 2 · Forbidden Rites'];
  const RITES = ['', en ? 'Challenge Grimoire' : 'Grimório das Challenges', 'Forbidden Rites · 0.5.5'];
  const infoFor = path => {
    const seg = path.split('/').filter(Boolean);
    const dir = seg.length > 1 ? seg[seg.length - 2] : '';
    if (BUILDS[dir]) return [dir, ...BUILDS[dir]];
    if (dir === 'rites') return ['rites', ...RITES];
    return ['home', ...HOME];
  };
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let fromNav = false;
  try { const t = +sessionStorage.getItem('poeNav'); fromNav = t && Date.now() - t < 8000; sessionStorage.removeItem('poeNav'); } catch (e) {}
  let firstVisit = true;
  try { firstVisit = !sessionStorage.getItem('poeSeen'); sessionStorage.setItem('poeSeen', '1'); } catch (e) {}
  { const c = PAL[infoFor(location.pathname)[0]] || PAL.home; root.style.setProperty('--pl-ground', c[0]); root.style.setProperty('--pl-acc', c[1]); }
  root.classList.add('ld');                                        // plain cover before first paint

  const discSize = () => Math.ceil(2 * Math.hypot(innerWidth / 2, innerHeight * .54) + 4) + 'px';   // cobre até o canto mais distante do centro da íris
  addEventListener('resize', () => document.querySelectorAll('.poe-loader').forEach(n => n.style.setProperty('--pl-d', discSize())), { passive: true });
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
  function overlay(info, mode) {
    const [key, p, name, sub] = info;
    const el = document.createElement('div');
    el.className = 'poe-loader ' + mode; el.setAttribute('aria-hidden', 'true'); el.dataset.key = key;
    el.style.setProperty('--pl-d', discSize());
    el.style.setProperty('--pl-t', -(Date.now() % 1e6) / 1000 + 's');
    const c = PAL[key] || PAL.home;
    [['--pl-ground', c[0]], ['--pl-acc', c[1]], ['--pl-gold', c[2]], ['--pl-hi', c[3]]].forEach(([k, v]) => el.style.setProperty(k, v));   // fase das animações pelo relógio: continua igual na página seguinte
    const img = p ? `<img src="${art}${p}-asc-sm.webp" alt="" decoding="async">` : '<span class="pl-glyph">◇</span>';
    el.innerHTML = `<div class="pl-disc"></div><div class="pl-stage">
      <div class="pl-medal"><span class="pl-ring r1"></span><span class="pl-ring r2"></span><span class="pl-ring r3"></span>
        <span class="pl-spark s1"></span><span class="pl-spark s2"></span><span class="pl-spark s3"></span><span class="pl-art">${img}</span></div>
      <div class="pl-name">${esc(name)}</div><div class="pl-sub">${esc(sub)}</div>
      <div class="pl-bar"><i></i></div></div>`;
    if (p) el.style.setProperty('--pl-bg', `url("${art}${p}-asc-bg.webp")`);
    const im = el.querySelector('.pl-art img');
    if (im) { const ok = () => im.classList.add('ok'); if (im.complete && im.naturalWidth) ok(); else { im.addEventListener('load', ok, { once: true }); im.addEventListener('error', ok, { once: true }); } }
    return el;
  }

  /* ---- entering this page */
  const here = infoFor(location.pathname);
  const born = performance.now();
  const minShow = reduce ? 0 : fromNav ? 420 : firstVisit ? 1150 : 650;
  let el = null, done = false;
  const mount = () => {
    if (el || done) return;
    el = overlay(here, fromNav ? 'enter nav on' : 'enter');
    document.body.prepend(el);
    root.classList.remove('ld');
    if (!fromNav) requestAnimationFrame(() => requestAnimationFrame(() => el && el.classList.add('on')));
    progress(document.readyState === 'complete' ? 1 : document.readyState === 'interactive' ? .62 : .3);
  };
  const progress = v => { if (el) el.style.setProperty('--pl-p', v); };
  const finish = () => {
    if (done) return; done = true;
    if (!el) { root.classList.remove('ld'); return; }
    progress(1);
    const fonts = document.fonts && document.fonts.ready ? Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 1200))]) : Promise.resolve();
    const idle = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => (window.requestIdleCallback ? requestIdleCallback(r, { timeout: 300 }) : setTimeout(r, 60)))));
    fonts.then(idle).then(() => {
      const wait = Math.max(0, minShow - (performance.now() - born));
      setTimeout(() => {
        if (!el) return;
        el.classList.add('out');
        setTimeout(() => { if (el) { el.remove(); el = null; } }, reduce ? 220 : 850);
      }, wait);
    });
  };
  // monta assim que o <body> existir (antes dos scripts pesados da página terminarem de baixar)
  if (document.body) mount();
  else {
    const mo = new MutationObserver(() => { if (document.body) { mo.disconnect(); mount(); } });
    mo.observe(root, { childList: true });
    document.addEventListener('DOMContentLoaded', () => { mo.disconnect(); mount(); }, { once: true });
  }
  document.addEventListener('DOMContentLoaded', () => progress(.62), { once: true });
  if (document.readyState === 'complete') setTimeout(finish, 0); else addEventListener('load', finish, { once: true });
  setTimeout(finish, 5000);                                         // never hang on a slow image/font
  addEventListener('pageshow', e => {
    if (!e.persisted) return;
    root.classList.remove('ld');
    document.querySelectorAll('.poe-loader').forEach(n => { n.classList.add('out'); setTimeout(() => n.remove(), 900); });
  });

  /* ---- leaving to another page of the site */
  document.addEventListener('click', e => {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    const a = e.target.closest && e.target.closest('a[href]');
    if (!a || (a.target && a.target !== '_self') || a.hasAttribute('download')) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || !/(\.html|\/)$/.test(url.pathname)) return;
    if (url.pathname === location.pathname && url.search === location.search) return;   // same page / hash
    e.preventDefault();
    try { sessionStorage.setItem('poeNav', String(Date.now())); } catch (err) {}
    if (reduce) { location.href = url.href; return; }
    document.querySelectorAll('.poe-loader').forEach(n => n.remove());
    const leave = overlay(infoFor(url.pathname), 'leave');
    document.body.appendChild(leave);
    requestAnimationFrame(() => requestAnimationFrame(() => { leave.classList.add('on'); leave.style.setProperty('--pl-p', .3); }));
    setTimeout(() => { location.href = url.href; }, 560);
  }, true);
})();
