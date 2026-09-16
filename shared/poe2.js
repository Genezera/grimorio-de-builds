/* PoE2 theme motion: page-aware ascendancy scenery, particles, trail, nav ink, reveals.
   Everything here is decorative; the guide works without it. */
(() => {
  const root = document.documentElement;
  const build = root.dataset.build === 'oracle' ? 'oracle' : 'silverfist';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const coarse = matchMedia('(pointer: coarse)');
  const artBase = new URL('art/', document.currentScript.src).href;
  const P = build === 'oracle' ? 'or' : 'sf';
  const art = n => `${artBase}${P}-${n}.webp`;
  const $$ = s => [...document.querySelectorAll(s)];

  /* ---------- scenery: each group of tabs has its own art and framing; each tab nudges it */
  const SCENES = [
    { img: 'asc-bg',   x: 64, y: 44, s: 1.00, r: 0,  o: .62 },  // Sua jornada — ascendancy
    { img: 'class-bg', x: 70, y: 52, s: 1.08, r: -4, o: .55 },  // Monte a build — base class
    { img: 'asc-bg',   x: 72, y: 58, s: 1.34, r: 6,  o: .64 },  // Domine a build — ascendancy close-up
    { img: 'class-bg', x: 60, y: 36, s: .92,  r: 3,  o: .42 },  // Ajuda — base class, calm
  ];
  const hash = s => [...s].reduce((h, c) => (h * 31 + c.charCodeAt(0)) >>> 0, 7);
  const scene = document.createElement('div');
  scene.id = 'poeScene'; scene.setAttribute('aria-hidden', 'true');
  scene.innerHTML = '<div class="layer"><div class="art"></div></div><div class="layer"><div class="art"></div></div><div class="tint"></div><canvas id="poeMotes"></canvas><div class="veil"></div><div class="grain"></div>';
  document.body.prepend(scene);
  const layers = [...scene.querySelectorAll('.layer')];
  let front = 0, curImg = '';
  function paintScene(tab) {
    const g = typeof guideGroup === 'function' ? Math.max(0, guideGroup(tab)) : 0;
    const sc = SCENES[g] || SCENES[0], h = hash(tab || 'agora');
    const dx = (h % 9) - 4, dy = ((h >> 4) % 7) - 3, dk = ((h >> 8) % 7) / 100, dr = ((h >> 12) % 5) - 2;
    const img = art(sc.img);
    const vars = { '--sx': `${sc.x + dx}%`, '--sy': `${sc.y + dy}%`, '--sk': (sc.s + dk).toFixed(3), '--sr': `${sc.r + dr}deg`, '--so': sc.o };
    if (img !== curImg) {                       // crossfade to the other layer
      front = 1 - front; curImg = img;
      const el = layers[front].firstChild;
      el.style.setProperty('--img', `url("${img}")`);
      Object.entries(vars).forEach(([k, v]) => el.style.setProperty(k, v));
      layers[front].classList.add('on'); layers[1 - front].classList.remove('on');
    } else {                                    // same art: glide to the new framing
      const el = layers[front].firstChild;
      Object.entries(vars).forEach(([k, v]) => el.style.setProperty(k, v));
    }
  }
  if (!reduce.matches && !coarse.matches) {    // gentle parallax on desktop pointers
    let raf = 0;
    addEventListener('pointermove', e => {
      if (raf) return;
      raf = requestAnimationFrame(() => {
        raf = 0;
        const x = (e.clientX / innerWidth - .5) * -18, y = (e.clientY / innerHeight - .5) * -12;
        layers.forEach(l => { l.style.transform = `translate3d(${x}px,${y}px,0)`; });
      });
    }, { passive: true });
  }

  /* ---------- particles: spirit wisps (Spirit Walker) / fate motes & stars (Oracle) */
  function motes() {
    const cv = document.getElementById('poeMotes'); if (!cv || reduce.matches) return;
    const ctx = cv.getContext('2d'); let W, H, dpr, parts = [], running = true;
    const css = n => getComputedStyle(root).getPropertyValue(n).trim();
    const rgb = hex => { const v = parseInt(hex.replace('#', ''), 16); return [(v >> 16) & 255, (v >> 8) & 255, v & 255]; };
    const cols = [rgb(css('--accent')), rgb(css('--accent2')), rgb(css('--gild-hi')), rgb(css('--wisp'))];
    const count = () => Math.round(Math.min(70, Math.max(18, innerWidth * innerHeight / (coarse.matches ? 42000 : 26000))));
    const spawn = fresh => {
      const oracle = build === 'oracle', pick = Math.random();
      const c = oracle ? (pick < .5 ? cols[0] : pick < .72 ? cols[3] : pick < .9 ? cols[2] : cols[1]) : (pick < .72 ? cols[0] : pick < .88 ? cols[2] : cols[1]);
      return { x: Math.random() * W, y: fresh ? Math.random() * H : H + 20, r: (oracle ? .6 : 1) + Math.random() * (oracle ? 1.8 : 2.4),
        vy: oracle ? -(.04 + Math.random() * .12) : -(.18 + Math.random() * .45), vx: (Math.random() - .5) * .12,
        ph: Math.random() * 6.28, sp: .004 + Math.random() * .01, a: .25 + Math.random() * .55, c, tw: oracle && Math.random() < .35 };
    };
    const size = () => { dpr = Math.min(2, devicePixelRatio || 1); W = innerWidth; H = innerHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); const n = count(); while (parts.length < n) parts.push(spawn(true)); parts.length = n; };
    size(); addEventListener('resize', size, { passive: true });
    document.addEventListener('visibilitychange', () => { running = !document.hidden; if (running) requestAnimationFrame(tick); });
    let t = 0;
    function tick() {
      if (!running) return;
      t++; ctx.clearRect(0, 0, W, H); ctx.globalCompositeOperation = 'lighter';
      for (const p of parts) {
        p.ph += p.sp; p.y += p.vy; p.x += p.vx + Math.sin(p.ph) * (build === 'oracle' ? .08 : .35);
        if (p.y < -30 || p.x < -30 || p.x > W + 30) Object.assign(p, spawn(false));
        const a = p.a * (p.tw ? .45 + .55 * Math.abs(Math.sin(p.ph * 3)) : 1) * Math.min(1, (H - p.y) / 160);
        const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 7);
        g.addColorStop(0, `rgba(${p.c},${a})`); g.addColorStop(.25, `rgba(${p.c},${a * .35})`); g.addColorStop(1, `rgba(${p.c},0)`);
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p.x, p.y, p.r * 7, 0, 6.283); ctx.fill();
        if (p.tw) { ctx.fillStyle = `rgba(255,255,255,${a * .8})`; ctx.fillRect(p.x - .5, p.y - .5, 1, 1); }
      }
      requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  /* ---------- hero medallion with the ascendancy art */
  function medal() {
    const h1 = document.querySelector('.brand h1'); if (!h1 || document.querySelector('.asc-medal')) return;
    const row = document.createElement('div'); row.className = 'brand-row';
    const b = document.createElement('button'); b.type = 'button'; b.className = 'asc-medal';
    const name = build === 'oracle' ? 'Oracle' : 'Spirit Walker';
    b.setAttribute('aria-label', (typeof T === 'function' ? T('Abrir Ascendência: ', 'Open Ascendancy: ') : '') + name);
    b.innerHTML = `<span class="glow"></span><img src="${art('asc')}" alt="" width="148" height="148" decoding="async"><span class="cap">${name}</span>`;
    b.addEventListener('click', () => typeof guideGo === 'function' && guideGo('asc'));
    if (!reduce.matches && !coarse.matches) {
      b.addEventListener('pointermove', e => { const r = b.getBoundingClientRect(); const x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; b.style.transform = `perspective(500px) rotateY(${x * 18}deg) rotateX(${-y * 18}deg) scale(1.04)`; });
      b.addEventListener('pointerleave', () => { b.style.transform = ''; });
    }
    h1.before(row); row.append(b, h1);
    root.style.setProperty('--craft-art', `url("${art('class')}")`);
  }

  /* ---------- trail: level label on the rail + horizontal trail for tablet/phone */
  let hrail;
  function trails() {
    const you = document.getElementById('you');
    if (you && !you.querySelector('.you-lv')) you.insertAdjacentHTML('beforeend', '<i class="you-lv"></i>');
    const where = document.querySelector('.where');
    if (where && typeof D !== 'undefined' && !hrail) {
      hrail = document.createElement('div'); hrail.className = 'hrail'; hrail.setAttribute('role', 'group');
      hrail.setAttribute('aria-label', typeof T === 'function' ? T('Trilha de níveis', 'Level trail') : 'Level trail');
      hrail.innerHTML = '<div class="hs"></div><div class="hf"></div>' + D.phases.map((p, i) => `<button type="button" data-hi="${i}" style="left:${((p.lv[0] - 1) / 99 * 100).toFixed(2)}%" title="${p.lv[0]} · ${String(p.name).replace(/"/g, '&quot;')}" aria-label="${String(p.name).replace(/"/g, '&quot;')} · ${p.lv[0]}"></button>`).join('') + '<div class="hy"></div>';
      hrail.addEventListener('click', e => { const b = e.target.closest('[data-hi]'); if (b && typeof setLv === 'function') setLv(D.phases[+b.dataset.hi].lv[0]); });
      where.prepend(hrail);
    }
  }
  let lastLv = null;
  function paintTrails() {
    if (typeof S === 'undefined') return;
    const pct = ((S.lv - 1) / 99 * 100);
    const lab = document.querySelector('#you .you-lv'); if (lab) lab.textContent = S.lv;
    if (hrail) {
      hrail.querySelector('.hf').style.width = pct + '%';
      hrail.querySelector('.hy').style.left = pct + '%';
      const cur = typeof curPhase === 'function' ? curPhase() : null;
      hrail.querySelectorAll('[data-hi]').forEach(b => { const p = D.phases[+b.dataset.hi]; b.classList.toggle('cur', p === cur); b.classList.toggle('done', p.lv[1] < S.lv); });
    }
    if (lastLv !== null && lastLv !== S.lv && !reduce.matches) {
      const orb = document.querySelector('.orbLv'); if (orb) { orb.classList.remove('bump'); void orb.offsetWidth; orb.classList.add('bump'); }
    }
    lastLv = S.lv;
  }

  /* ---------- navigator: sliding ink under the active group, active tab kept in view, stuck shadow */
  let ink;
  function paintNav() {
    const groups = document.getElementById('navGroups'); if (!groups) return;
    if (!ink) { ink = document.createElement('span'); ink.className = 'ng-ink'; groups.append(ink); }
    const on = groups.querySelector('[aria-pressed="true"]');
    if (on) { ink.style.left = on.offsetLeft + 'px'; ink.style.width = on.offsetWidth + 'px'; }
    const tab = document.querySelector('#tabs [aria-selected="true"]'), bar = document.getElementById('tabs');
    if (tab && bar && bar.scrollWidth > bar.clientWidth) bar.scrollTo({ left: tab.offsetLeft - bar.clientWidth / 2 + tab.offsetWidth / 2, behavior: reduce.matches ? 'auto' : 'smooth' });
  }
  function stuck() {
    const nav = document.getElementById('navigator'); if (!nav || !('IntersectionObserver' in window)) return;
    const sentinel = document.createElement('div'); sentinel.style.cssText = 'height:1px;margin-bottom:-1px';
    nav.before(sentinel);
    new IntersectionObserver(([e]) => nav.classList.toggle('stuck', !e.isIntersecting)).observe(sentinel);
  }

  /* ---------- scroll reveal for cards rendered below the fold */
  let io;
  const REVEAL = '.frame,.tt,.gem,.qcard,.slot,.ucard,.craft-step,.craft-glossary article,.tablewrap,details.acc';
  function reveal(scope) {
    if (reduce.matches || !('IntersectionObserver' in window)) return;
    root.classList.add('js-reveal');
    io = io || new IntersectionObserver(entries => entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -6% 0px', threshold: .04 });
    const vh = innerHeight;
    scope.querySelectorAll(REVEAL).forEach((el, i) => {
      if (el.closest('.rv') || el.getBoundingClientRect().top < vh * .92) return;   // already visible: no flash
      el.classList.add('rv'); el.style.transitionDelay = `${Math.min(i % 6, 5) * 45}ms`; io.observe(el);
    });
  }

  /* ---------- wire into the guide */
  function afterRender(id) {
    paintScene(id); paintNav(); paintTrails();
    const view = document.getElementById('v-' + id); if (view) reveal(view);
  }
  function boot() {
    medal(); trails(); stuck();
    if (typeof renderTab === 'function') {
      const orig = renderTab;
      renderTab = function (id) { orig(id); try { afterRender(S.tab); } catch (e) { /* decorative only */ } };
    }
    if (typeof paintRail === 'function') {
      const origRail = paintRail;
      paintRail = function () { origRail(); try { paintTrails(); } catch (e) {} };
    }
    addEventListener('resize', () => paintNav(), { passive: true });
    afterRender(typeof S !== 'undefined' ? S.tab : 'agora');
    motes();
  }
  boot();
})();
