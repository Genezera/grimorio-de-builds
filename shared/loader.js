/* Instant navigation + entry loading screen. Loaded in <head>; decorative only, never blocks input.
   - Links inside the site are prerendered in the background (Speculation Rules): the click just swaps in the already-rendered page,
     with a native crossfade (@view-transition in loader.css). No curtain, no reload feel.
   - The loading screen covers every real page load (skipped only for prerendered pages and back/forward cache).
   - Lite mode (phones, touch tablets, weak devices): no prerender, blur, particles or infinite animations. */
(() => {
  const root = document.documentElement;
  const qs = new URLSearchParams(location.search);
  const src = document.currentScript && document.currentScript.src;
  const siteBase = src ? new URL('../', src) : new URL('./', location.href);   // .../trilha-silverfist/
  const art = new URL('shared/art/', siteBase).href;

  /* ---- modo leve: celular, tablet touch e aparelhos fracos (sem blur, partículas nem animações infinitas; ver loader.css) */
  const mem = navigator.deviceMemory || 8, cores = navigator.hardwareConcurrency || 8, saveData = !!(navigator.connection && navigator.connection.saveData);
  const lite = qs.has('lite') || (!qs.has('full') && (matchMedia('(pointer: coarse)').matches || innerWidth < 900 || mem <= 4 || cores <= 4 || saveData));
  if (lite) root.classList.add('lite');

  /* ---- prerender every page of the site on hover/touch (Chrome/Edge); from inside a build, the home page eagerly */
  if (!navigator.webdriver && HTMLScriptElement.supports && HTMLScriptElement.supports('speculationrules')) {
    const site = { and: [{ href_matches: siteBase.pathname + '*' }, { not: { selector_matches: '[target=_blank], [download]' } }, { not: { href_matches: location.pathname } }] };
    // no modo leve só baixa o HTML ao tocar (pré-renderizar páginas pesadas em segundo plano deixaria o celular lento)
    const rules = lite ? { prefetch: [{ source: 'document', where: site, eagerness: 'conservative' }] }
                       : { prerender: [{ source: 'document', where: site, eagerness: 'moderate' }], prefetch: [{ source: 'document', where: site, eagerness: 'conservative' }] };
    const inSubfolder = location.pathname.replace(/[^/]*$/, '') !== siteBase.pathname;
    if (inSubfolder && !lite) rules.prerender.push({ source: 'list', urls: [new URL(/en\.html$/.test(location.pathname) ? 'en.html' : 'index.html', siteBase).href], eagerness: 'eager' });
    const s = document.createElement('script'); s.type = 'speculationrules'; s.textContent = JSON.stringify(rules);
    document.head.appendChild(s);
  }

  if (navigator.webdriver && !qs.has('loader')) return;             // automated tests: no overlay
  if (document.prerendering) return;                                // prerendered page: it is shown already rendered
  let internal = false;
  try { internal = !!document.referrer && new URL(document.referrer).origin === location.origin; } catch (e) {}
  const nav = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
  if (nav && nav.type === 'back_forward' && !qs.has('loader')) return;   // voltar/avançar: a página vem pronta do cache

  const BUILDS = {
    silverfist: ['sf', 'Mighty Silverfist', 'Huntress · Spirit Walker'], oracle: ['or', 'Oracle Spell Totem', 'Druid · Oracle'],
    tactician: ['ta', 'Tactician Pin2Win', 'Mercenary · Tactician'], infernalist: ['in', 'Infernalist Comet', 'Witch · Infernalist'],
    acolyte: ['ac', 'Poisonburst Archon', 'Monk · Acolyte of Chayula'], pathfinder: ['pf', 'Pathfinder Decompose', 'Ranger · Pathfinder'],
    smith: ['sk', 'Smith of Kitava', 'Warrior · Smith of Kitava'], martial: ['ma', 'Oil Barrage Teleport', 'Monk · Martial Artist'],
  };
  const PAL = { silverfist: ['#07080a', '#5fe3c1', '#c3a066', '#ecd6a3'], oracle: ['#06060c', '#a58dff', '#b7bfd9', '#eef1fb'], tactician: ['#08080a', '#ff8a3d', '#c9a46a', '#f0dcb0'],
    infernalist: ['#0a0505', '#ff5b1f', '#d9a36b', '#f6d8b0'], acolyte: ['#07050b', '#b35cff', '#c3b2e6', '#efe7ff'], pathfinder: ['#060906', '#7fd957', '#cdbb7c', '#f0e3b4'],
    smith: ['#09070a', '#ff6a13', '#d08a47', '#f5cf9f'], martial: ['#05070b', '#4cc3ff', '#e0b25c', '#f7deaa'], home: ['#07070a', '#c3a066', '#c3a066', '#ecd6a3'], rites: ['#07050c', '#9b6bff', '#f1b35c', '#ffd894'] };
  const en = /(^|\/)en\.html$/.test(location.pathname);
  const dir = location.pathname.split('/').filter(Boolean).slice(-2, -1)[0] || '';
  const key = BUILDS[dir] ? dir : dir === 'rites' ? 'rites' : 'home';
  const [p, name, sub] = BUILDS[key] || (key === 'rites' ? ['', en ? 'Challenge Grimoire' : 'Grimório das Challenges', 'Forbidden Rites · 0.5.5'] : ['', en ? 'Build Grimoire' : 'Grimório de Builds', 'Path of Exile 2 · Forbidden Rites']);
  const c = PAL[key];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.style.setProperty('--pl-ground', c[0]); root.style.setProperty('--pl-acc', c[1]);
  root.classList.add('ld');                                          // plain cover before first paint

  const discSize = () => Math.ceil(2 * Math.hypot(innerWidth / 2, innerHeight * .54) + 4) + 'px';
  const esc = s => String(s).replace(/[&<>"]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[ch]);
  const born = performance.now(), minShow = reduce ? 0 : internal ? 350 : 900;   // dentro do site: só cobre o carregamento
  let el = null, done = false;
  const progress = v => { if (el) el.style.setProperty('--pl-p', v); };
  const mount = () => {
    if (el || done) return;
    el = document.createElement('div');
    el.className = 'poe-loader'; el.setAttribute('aria-hidden', 'true');
    [['--pl-ground', c[0]], ['--pl-acc', c[1]], ['--pl-gold', c[2]], ['--pl-hi', c[3]], ['--pl-d', discSize()]].forEach(([k, v]) => el.style.setProperty(k, v));
    if (p) el.style.setProperty('--pl-bg', `url("${art}${p}-asc-bg.webp")`);
    el.innerHTML = `<div class="pl-disc"></div><div class="pl-stage">
      <div class="pl-medal"><span class="pl-ring r1"></span><span class="pl-ring r2"></span><span class="pl-ring r3"></span>
        <span class="pl-spark s1"></span><span class="pl-spark s2"></span><span class="pl-spark s3"></span>
        <span class="pl-art">${p ? `<img src="${art}${p}-asc-sm.webp" alt="" decoding="async">` : '<span class="pl-glyph">◇</span>'}</span></div>
      <div class="pl-name">${esc(name)}</div><div class="pl-sub">${esc(sub)}</div><div class="pl-bar"><i></i></div></div>`;
    const im = el.querySelector('img');
    if (im) { const ok = () => im.classList.add('ok'); if (im.complete && im.naturalWidth) ok(); else { im.addEventListener('load', ok, { once: true }); im.addEventListener('error', ok, { once: true }); } }
    document.body.prepend(el);
    root.classList.remove('ld');
    requestAnimationFrame(() => requestAnimationFrame(() => el && el.classList.add('on')));
    progress(document.readyState === 'complete' ? 1 : document.readyState === 'interactive' ? .62 : .3);
  };
  const finish = () => {
    if (done) return; done = true;
    if (!el) { root.classList.remove('ld'); return; }
    progress(1);
    // revela só com fontes prontas e a renderização inicial da página já feita (o trabalho pesado acontece atrás da tela)
    const fonts = document.fonts && document.fonts.ready ? Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 1200))]) : Promise.resolve();
    const idle = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => (window.requestIdleCallback ? requestIdleCallback(r, { timeout: 400 }) : setTimeout(r, 80)))));
    fonts.then(idle).then(() => setTimeout(() => {
      if (!el) return;
      el.classList.add('out');
      setTimeout(() => { if (el) { el.remove(); el = null; } }, reduce ? 220 : 850);
    }, Math.max(0, minShow - (performance.now() - born))));
  };
  if (document.body) mount();
  else {
    const mo = new MutationObserver(() => { if (document.body) { mo.disconnect(); mount(); } });
    mo.observe(root, { childList: true });
    document.addEventListener('DOMContentLoaded', () => { mo.disconnect(); mount(); }, { once: true });
  }
  document.addEventListener('DOMContentLoaded', () => progress(.62), { once: true });
  if (document.readyState === 'complete') setTimeout(finish, 0); else addEventListener('load', finish, { once: true });
  setTimeout(finish, 5000);
  addEventListener('resize', () => el && el.style.setProperty('--pl-d', discSize()), { passive: true });
})();
