/* Mobile/tablet layout lint: text cut off (overflow/ellipsis/clipped by a parent), content outside the viewport,
   small touch targets, tiny fonts, squeezed text columns, distorted images and large empty gaps.
   Covers every tab of every build (PT phone sizes, EN tablet sizes), the landing and the challenges page.
   Run: NODE_PATH=... node tools/tests/mobile.cjs   (SIZES/PAGES env vars optional) */
const { chromium } = require('playwright');
const fs = require('node:fs'), path = require('node:path'), http = require('node:http');
const root = path.resolve(__dirname, '../..');
const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(new URL(req.url, 'http://x').pathname), file = path.resolve(root, '.' + rel + (rel.endsWith('/') ? 'index.html' : ''));
  if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
  fs.readFile(file, (err, data) => { if (err) { res.writeHead(404).end(); return; } res.setHeader('Content-Type', ({ '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.webp': 'image/webp' })[path.extname(file)] || 'application/octet-stream'); res.end(data); });
});
const SIZES = (process.env.SIZES || '360x780,390x844,412x915,844x390,768x1024,820x1180,1024x768,1180x820').split(',').map(s => s.split('x').map(Number));
const BUILDS = ['silverfist', 'oracle', 'tactician', 'infernalist', 'acolyte', 'pathfinder', 'smith', 'martial', 'shaman', 'legionnaire', 'whirling','twister','hyperspeed'];
const PAGES = (process.env.PAGES || BUILDS.flatMap(b => [b + '/index.html', b + '/en.html']).concat(['index.html', 'en.html', 'rites/index.html', 'rites/en.html']).join(',')).split(',');

function lint(scopeSel) {
  const scope = document.querySelector(scopeSel) || document.body, W = innerWidth, touch = W < 1024, out = [];
  const name = e => e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (typeof e.className === 'string' && e.className.trim() ? '.' + e.className.trim().split(/\s+/).slice(0, 2).join('.') : '') + ' "' + (e.textContent || e.value || e.alt || '').trim().replace(/\s+/g, ' ').slice(0, 34) + '"';
  const hiddenAnc = el => { for (let e = el; e && e !== document.documentElement; e = e.parentElement) { if (e.tagName === 'DETAILS' && !e.open && !el.closest('summary')) return true; const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity < .05 || e.hidden) return true; } return false; };
  const skip = el => el.closest('#poeScene,.scene,.void,canvas,svg,.sr-only,.sr,.skip,[aria-hidden="true"],.ttip,.guide-toast,.sb-shade,.tree-wrap,.treebox,#treeSvg,.tree,.asc-tree') || getComputedStyle(el).position === 'fixed';
  const scroller = el => { for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) { const cs = getComputedStyle(p); if (/(auto|scroll)/.test(cs.overflowX) && p.scrollWidth > p.clientWidth + 1) return p; } return null; };
  const ownText = el => [...el.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim().length > 1);
  const add = (kind, el, extra) => { const m = `${kind}: ${name(el)}${extra ? ' ' + extra : ''}`; if (!out.includes(m) && out.length < 40) out.push(m); };
  for (const el of scope.querySelectorAll('*')) {
    if (skip(el)) continue;
    const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) continue;
    const texts = ownText(el);
    const isCtl = el.matches('button,input,select,textarea,summary,[role="tab"],a.primary,a.guide-btn,.chk');
    if (!texts.length && !isCtl && !el.matches('img')) continue;
    if (hiddenAnc(el)) continue;
    const cs = getComputedStyle(el), sc = scroller(el);
    // A. text cut by its own box
    if (texts.length && /(hidden|clip)/.test(cs.overflowX) && el.scrollWidth > el.clientWidth + 2) add('CUT-X', el, `${el.scrollWidth}>${el.clientWidth}`);
    if (texts.length && /(hidden|clip)/.test(cs.overflowY) && !/-webkit-box/.test(cs.display) && el.scrollHeight > el.clientHeight + 3 && el.clientHeight > 0) add('CUT-Y', el, `${el.scrollHeight}>${el.clientHeight}`);
    if (texts.length && cs.textOverflow === 'ellipsis' && el.scrollWidth > el.clientWidth + 1) add('ELLIPSIS', el);
    // A2. text clipped by an ancestor with overflow hidden
    if (texts.length && !sc) {
      const range = document.createRange(); range.selectNodeContents(el); const tr = range.getBoundingClientRect();
      for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
        const pc = getComputedStyle(p); if (!/(hidden|clip)/.test(pc.overflowX + pc.overflowY)) continue;
        const pr = p.getBoundingClientRect();
        if (tr.right > pr.right + 3 || tr.left < pr.left - 3 || tr.bottom > pr.bottom + 3) { add('CLIPPED', el, `by ${name(p).slice(0, 40)}`); break; }
      }
    }
    // B. outside the viewport (not inside a horizontal scroller)
    if (!sc && (r.right > W + 2 || r.left < -2)) add('OFFSCREEN', el, `${Math.round(r.left)}..${Math.round(r.right)} of ${W}`);
    // C. touch target
    if (touch && isCtl && !el.matches('input[type=checkbox],input[type=radio],input[type=range],.hrail button') && (r.height < 30 || r.width < 30) && !el.closest('p,li')) add('TAP', el, `${Math.round(r.width)}x${Math.round(r.height)}`);
    // D. tiny font
    if (texts.length && parseFloat(cs.fontSize) < 10) add('FONT', el, cs.fontSize);
    // E. squeezed column: long text in a very narrow box
    const len = texts.reduce((a, n) => a + n.textContent.trim().length, 0);
    if (len > 40 && r.width < 90 && !sc && cs.writingMode === 'horizontal-tb') add('NARROW', el, `${Math.round(r.width)}px`);
    // F. distorted image
    if (el.matches('img') && el.naturalWidth > 8 && cs.objectFit === 'fill') { const a = (r.width / r.height) / (el.naturalWidth / el.naturalHeight); if (a > 1.15 || a < .87) add('IMG-RATIO', el, a.toFixed(2)); }
  }
  // G. big vertical gaps inside the scope (no visible content)
  const blocks = [...scope.querySelectorAll('*')].filter(e => (e.matches('svg,canvas,.build-art,.medal,.tree-wrap,.treebox') || (e.getBoundingClientRect().height > 60 && getComputedStyle(e).backgroundImage.includes('url(')) || (!skip(e) && (ownText(e).length || e.matches('img,button,input,select,table,.panel,.card')))) && !hiddenAnc(e)).map(e => e.getBoundingClientRect()).filter(r => r.height > 0 && r.width > 0).sort((a, b) => a.top - b.top);
  let bottom = blocks.length ? blocks[0].bottom : 0;
  for (const b of blocks) { if (b.top - bottom > 170) { out.push(`GAP: ${Math.round(b.top - bottom)}px empty at y=${Math.round(bottom + scrollY)}`); } bottom = Math.max(bottom, b.bottom); }
  return out;
}

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch({ headless: true, ...(process.env.BROWSER_CHANNEL ? { channel: process.env.BROWSER_CHANNEL } : {}) });
  const problems = []; let checks = 0;
  try {
    for (const [w, h] of SIZES) {
      const ctx = await browser.newContext({ viewport: { width: w, height: h }, reducedMotion: 'reduce', hasTouch: w < 1024, isMobile: w < 768, deviceScaleFactor: 1 });
      const page = await ctx.newPage();
      await page.route(/fonts\.(googleapis|gstatic)\.com/, r => r.abort());
      for (const file of PAGES) {
        await page.goto(`${base}/${file}`); await page.waitForTimeout(250);
        const isBuild = BUILDS.some(b => file.startsWith(b + '/'));
        const run = async (label, scope) => { const r = await page.evaluate(lint, scope); checks++; r.forEach(x => problems.push(`${w}x${h} ${file} ${label}: ${x}`)); };
        if (!isBuild) { await page.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true)); for (let y = 0; y < await page.evaluate(() => document.documentElement.scrollHeight); y += 500) { await page.evaluate(y => scrollTo(0, y), y); await page.waitForTimeout(30); } await page.waitForTimeout(400); await page.evaluate(() => scrollTo(0, 0)); await run('page', 'body'); continue; }
        for (const lv of [8, 70]) {
          await page.evaluate(lv => setLv(lv), lv);
          await run(`lv${lv} header`, '.console');
          for (const id of await page.evaluate(() => TABS.map(t => t[0]).concat(['craft']))) {
            await page.evaluate(id => guideGo(id), id); await page.waitForTimeout(60);
            await run(`lv${lv} #${id}`, '#v-' + id);
          }
        }
      }
      await ctx.close();
      console.log(`${w}x${h} done · problems so far: ${problems.length}`);
    }
  } finally { await browser.close(); server.close(); }
  fs.writeFileSync(path.join(__dirname, 'mobile-report.txt'), problems.join('\n') + '\n');
  console.log(JSON.stringify({ checks, problems: problems.filter(x => !/: GAP: /.test(x)).length, gapNotes: problems.filter(x => /: GAP: /.test(x)).length }, null, 1));
  console.log(problems.slice(0, 80).join('\n'));
  // GAP is informational (background art, fade-in sections and two-column layouts produce false positives); everything else fails the run
  process.exitCode = problems.some(x => !/: GAP: /.test(x)) ? 1 : 0;
})();
