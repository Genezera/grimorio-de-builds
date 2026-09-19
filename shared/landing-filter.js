/* Filtros por classe/ascendência/estilo/uso e ordenação por ranking das builds da landing (dados nos data-* de cada card, gerados por tools/landing_registry.py). */
(() => {
  const grid = document.querySelector('.build-grid'); if (!grid) return;
  const cards = [...grid.querySelectorAll('.build[data-class]')]; if (!cards.length) return;
  const $ = id => document.getElementById(id), f = { c: $('fClass'), a: $('fAsc'), t: $('fTag'), s: $('fSort'), m: $('fMeta') }, out = $('fCount');
  if (!f.c) return;
  const KEY = 'grimorio:landing-filter', en = document.documentElement.lang === 'en';
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify({ c: f.c.value, a: f.a.value, t: f.t.value, s: f.s.value, m: f.m.value })); } catch (e) {} };
  const apply = () => {
    let n = 0;
    cards.forEach(c => {
      const ok = (!f.c.value || c.dataset.class === f.c.value) && (!f.a.value || c.dataset.asc === f.a.value) && (!f.t.value || c.dataset.tags.split(' ').includes(f.t.value)) && (!f.m.value || c.dataset.meta === f.m.value);
      c.hidden = !ok; if (ok) n++;
      c.style.order = f.s.value === 'default' ? c.dataset.guide : (c.dataset['r' + f.s.value.charAt(0).toUpperCase() + f.s.value.slice(1)] ?? c.dataset.guide);
    });
    out.textContent = n === cards.length ? (en ? `${n} builds` : `${n} builds`) : (en ? `${n} of ${cards.length} builds` : `${n} de ${cards.length} builds`);
    save();
  };
  try { const s = JSON.parse(localStorage.getItem(KEY) || '{}'); ['c', 'a', 't', 's', 'm'].forEach(k => { if (s[k] != null && [...f[k].options].some(o => o.value === s[k])) f[k].value = s[k]; }); } catch (e) {}
  // ascendência só lista as da classe escolhida
  f.c.addEventListener('change', () => { const has = new Set(cards.filter(c => !f.c.value || c.dataset.class === f.c.value).map(c => c.dataset.asc)); [...f.a.options].forEach(o => { o.hidden = !!o.value && !has.has(o.value); }); if (f.a.value && !has.has(f.a.value)) f.a.value = ''; apply(); });
  Object.values(f).slice(1).forEach(el => el.addEventListener('change', apply));
  grid.style.display = grid.style.display || ''; apply();
})();
