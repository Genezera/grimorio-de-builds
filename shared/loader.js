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
  root.classList.add('ld');                                        // plain cover before first paint

  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
  function overlay(info, mode) {
    const [key, p, name, sub] = info;
    const el = document.createElement('div');
    el.className = 'poe-loader ' + mode; el.setAttribute('aria-hidden', 'true'); el.dataset.key = key;
    const img = p ? `<img src="${art}${p}-asc-sm.webp" alt="" decoding="async">` : '<span class="pl-glyph">◇</span>';
    el.innerHTML = `<div class="pl-veil"></div><div class="pl-stage">
      <div class="pl-medal"><span class="pl-ring r1"></span><span class="pl-ring r2"></span><span class="pl-ring r3"></span>
        <span class="pl-spark s1"></span><span class="pl-spark s2"></span><span class="pl-spark s3"></span><span class="pl-art">${img}</span></div>
      <div class="pl-name">${esc(name)}</div><div class="pl-sub">${esc(sub)}</div>
      <div class="pl-bar"><i></i></div></div>`;
    if (p) el.style.setProperty('--pl-bg', `url("${art}${p}-asc-bg.webp")`);
    return el;
  }

  /* ---- entering this page */
  const here = infoFor(location.pathname);
  const born = performance.now();
  const minShow = reduce ? 0 : fromNav ? 420 : firstVisit ? 1150 : 650;
  let el = null, done = false;
  const mount = () => {
    if (el || done) return;
    el = overlay(here, fromNav ? 'enter nav' : 'enter');
    document.body.prepend(el);
    root.classList.remove('ld');
    requestAnimationFrame(() => el.classList.add('on'));
    progress(document.readyState === 'complete' ? 1 : document.readyState === 'interactive' ? .62 : .3);
  };
  const progress = v => { if (el) el.style.setProperty('--pl-p', v); };
  const finish = () => {
    if (done) return; done = true;
    if (!el) { root.classList.remove('ld'); return; }
    progress(1);
    const wait = Math.max(0, minShow - (performance.now() - born));
    setTimeout(() => {
      root.classList.add('pl-reveal');
      el.classList.add('out');
      setTimeout(() => { el.remove(); el = null; root.classList.remove('pl-reveal'); }, reduce ? 200 : 900);
    }, wait);
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
  addEventListener('pageshow', e => { if (e.persisted) { document.querySelectorAll('.poe-loader').forEach(n => n.remove()); root.classList.remove('ld', 'pl-reveal'); } });

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
    requestAnimationFrame(() => requestAnimationFrame(() => leave.classList.add('on')));
    setTimeout(() => { location.href = url.href; }, 520);
  }, true);
})();
