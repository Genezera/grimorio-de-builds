/* Seletor de classe/ascendência (quadradinhos com a arte) + ordenação por ranking das builds da landing. Dados nos data-* de cada card (tools/landing_registry.py). */
(() => {
  const grid = document.querySelector('.build-grid'); if (!grid) return;
  const cards = [...grid.querySelectorAll('.build[data-asc]')]; if (!cards.length) return;
  const tiles = [...document.querySelectorAll('.cls-tile[data-asc]')], all = document.querySelector('.cls-tile[data-all]'), sort = document.getElementById('fSort'), out = document.getElementById('fCount');
  if (!tiles.length || !all) return;
  const KEY = 'grimorio:landing-classes', en = document.documentElement.lang === 'en', sel = new Set();
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify({ a: [...sel], s: sort ? sort.value : 'default' })); } catch (e) {} };
  const apply = () => {
    let n = 0;
    cards.forEach(c => {
      const ok = !sel.size || sel.has(c.dataset.asc);
      c.hidden = !ok; if (ok) n++;
      const r = sort ? sort.value : 'default';
      c.style.order = r === 'default' ? c.dataset.guide : (c.dataset['r' + r.charAt(0).toUpperCase() + r.slice(1)] ?? c.dataset.guide);
    });
    tiles.forEach(t => t.setAttribute('aria-pressed', sel.has(t.dataset.asc) ? 'true' : 'false'));
    all.setAttribute('aria-pressed', sel.size ? 'false' : 'true');
    if (out) out.textContent = en ? `${n} of ${cards.length} builds` : `${n} de ${cards.length} builds`;
    save();
  };
  tiles.forEach(t => t.addEventListener('click', () => { sel.has(t.dataset.asc) ? sel.delete(t.dataset.asc) : sel.add(t.dataset.asc); apply(); }));
  all.addEventListener('click', () => { sel.clear(); apply(); });
  if (sort) sort.addEventListener('change', apply);
  try {
    const s = JSON.parse(localStorage.getItem(KEY) || '{}');
    (s.a || []).forEach(a => { if (tiles.some(t => t.dataset.asc === a)) sel.add(a); });
    if (sort && s.s && [...sort.options].some(o => o.value === s.s)) sort.value = s.s;
  } catch (e) {}
  apply();
})();
