/* Layout audit: finds visible UI atoms (buttons, fields, labels, text) that cover each other,
   plus horizontal page overflow, on every tab of both builds, the landing and the challenges page,
   at many viewport sizes. Run: NODE_PATH=... node tools/tests/overlap.cjs  (serves the repo itself). */
const { chromium } = require('playwright');
const fs = require('node:fs'), path = require('node:path'), http = require('node:http');
const root = path.resolve(__dirname, '../..');
const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(new URL(req.url, 'http://x').pathname), file = path.resolve(root, '.' + rel + (rel.endsWith('/') ? 'index.html' : ''));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  fs.readFile(file, (err, data) => { if (err) { res.writeHead(404).end(); return; } res.setHeader('Content-Type', ({ '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.webp': 'image/webp' })[path.extname(file)] || 'application/octet-stream'); res.end(data); });
});
const SIZES = (process.env.SIZES || '320x640,375x812,414x896,844x390,768x1024,1024x768,1280x800,1440x900,1920x1080,2560x1440').split(',').map(s => s.split('x').map(Number));

/* runs inside the page */
function audit(scopeSel) {
  const scope = document.querySelector(scopeSel) || document.body;
  const interactive = 'button,a,input,select,textarea,summary,label,.chip,.pill,.tbtn';
  const vis = el => { for (let e = el; e && e !== document.documentElement; e = e.parentElement) { if (e.tagName === 'DETAILS' && !e.open && !el.closest('summary')) return false; const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity < .05 || e.hidden) return false; } return true; };
  const skip = el => el.closest('#poeScene,.void,.scene,.ttip,.guide-toast,.spark,canvas,svg,.sr-only,.sr,[aria-hidden="true"]') || getComputedStyle(el).position === 'fixed' || el.closest('.sb-fab,.sb-shade');
  const clips = el => { const out = []; for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) { const cs = getComputedStyle(p); if (cs.overflowX !== 'visible' || cs.overflowY !== 'visible') out.push(p.getBoundingClientRect()); } return out; };
  const clipRects = el => {
    // inline elements that wrap produce one rect per line; measure lines, not the bounding box
    const cs = getComputedStyle(el), raw = cs.display === 'inline' ? [...el.getClientRects()] : [el.getBoundingClientRect()], cl = clips(el);
    return raw.map(r => cl.reduce((b, q) => ({ l: Math.max(b.l, q.left), t: Math.max(b.t, q.top), r: Math.min(b.r, q.right), b: Math.min(b.b, q.bottom) }), { l: r.left, t: r.top, r: r.right, b: r.bottom })).filter(b => b.r - b.l >= 3 && b.b - b.t >= 3);
  };
  const atoms = [];
  for (const el of scope.querySelectorAll('*')) {
    if (skip(el)) continue;
    const isInt = el.matches(interactive);
    const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1);
    if (!isInt && !hasText && !el.matches('img')) continue;
    if (el.matches('img') && !el.closest('button,a,.tt,.gem,.gicon,.slot,.item')) continue;
    const rects = clipRects(el); if (!rects.length) continue;
    if (!vis(el)) continue;
    rects.forEach(box => atoms.push({ el, box }));
  }
  atoms.sort((a, b) => a.box.t - b.box.t);
  const hits = [];
  for (let i = 0; i < atoms.length; i++) {
    const A = atoms[i];
    for (let j = i + 1; j < atoms.length && atoms[j].box.t < A.box.b; j++) {
      const B = atoms[j];
      if (A.el === B.el || A.el.contains(B.el) || B.el.contains(A.el)) continue;
      // text atoms inside the same interactive parent are fine (e.g. <b> and <small> in a button)
      const pa = A.el.closest(interactive), pb = B.el.closest(interactive); if (pa && pa === pb) continue;
      const w = Math.min(A.box.r, B.box.r) - Math.max(A.box.l, B.box.l), h = Math.min(A.box.b, B.box.b) - Math.max(A.box.t, B.box.t);
      if (w <= 2 || h <= 2) continue;
      const area = w * h, small = Math.min((A.box.r - A.box.l) * (A.box.b - A.box.t), (B.box.r - B.box.l) * (B.box.b - B.box.t));
      if (area < 40 || area / small < .25) continue;
      const name = e => (e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).slice(0, 2).join('.') : '') + ' "' + (e.textContent || e.value || e.alt || '').trim().slice(0, 28) + '"');
      const msg = `${name(A.el)} ⟷ ${name(B.el)} (${Math.round(area)}px²)`; if (!hits.includes(msg)) hits.push(msg);
      if (hits.length > 12) return { hits, overflow: document.documentElement.scrollWidth - innerWidth };
    }
  }
  return { hits, overflow: document.documentElement.scrollWidth - innerWidth };
}

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch({ headless: true, ...(process.env.BROWSER_CHANNEL ? { channel: process.env.BROWSER_CHANNEL } : {}) });
  const problems = []; let checks = 0;
  const pages = (process.env.PAGES || ['silverfist','oracle','tactician','infernalist','acolyte','pathfinder','smith'].flatMap(b => [b + '/index.html', b + '/en.html']).concat(['index.html', 'en.html', 'rites/index.html', 'rites/en.html']).join(',')).split(',');
  try {
    for (const [w, h] of SIZES) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h }, reducedMotion: 'reduce', hasTouch: w < 1024 });
      const page = await ctx.newPage();
      await page.route(/fonts\.(googleapis|gstatic)\.com/, r => r.abort());
      for (const file of pages) {
        await page.goto(`${base}/${file}`); await page.waitForTimeout(250);
        const isBuild = /silverfist|oracle|tactician|infernalist|acolyte|pathfinder|smith/.test(file);
        const run = async (label, scope) => {
          await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(60);
          const r = await page.evaluate(audit, scope); checks++;
          if (r.overflow > 1) problems.push(`${w}x${h} ${file} ${label}: page overflow ${r.overflow}px`);
          r.hits.forEach(x => problems.push(`${w}x${h} ${file} ${label}: ${x}`));
        };
        if (!isBuild) { await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true)); await run('page', 'body'); continue; }
        await page.evaluate(() => setLv(52));
        await run('header', '.console');
        const tabs = await page.evaluate(() => TABS.map(t => t[0]));
        for (const id of tabs) {
          await page.evaluate(id => guideGo(id), id); await page.waitForTimeout(90);
          await run('#' + id, '#v-' + id);
          if (id === 'tree' || id === 'arvore') { await page.evaluate(() => { const b = document.querySelector('[data-tz="labels"]'); b && b.click(); }); await run('#arvore+labels', '#v-arvore'); }
          if (id === 'craft') for (const v of ['basics', 'calculator']) { await page.evaluate(v => { S.craft.view = v; renderTab('craft'); }, v); await run('#craft:' + v, '#v-craft'); }
        }
        await run('navigator', '#navigator');
      }
      await ctx.close();
      console.log(`${w}x${h} done · problems so far: ${problems.length}`);
    }
  } finally { await browser.close(); server.close(); }
  fs.writeFileSync(path.join(__dirname, 'overlap-report.txt'), problems.join('\n') + '\n');
  console.log(JSON.stringify({ checks, problems: problems.length }, null, 1));
  console.log(problems.slice(0, 60).join('\n'));
  process.exitCode = problems.length ? 1 : 0;
})();
