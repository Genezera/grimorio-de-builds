/* SKIN v3 — comportamento da camada visual (shared/skin.css). Decorativo e defensivo: se algo não existir, não faz nada. */
(() => {
  const root = document.documentElement, build = root.dataset.build;
  if (!build) return;
  const en = /^en/i.test(root.lang || '');
  const T = (pt, eng) => (en ? eng : pt);
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1. navegação: poucas abas + "Mais" ---------- */
  const PRIMARY = ['agora', 'rota', 'mech', 'skills', 'gear', 'arvore', 'asc'];
  let more = null;
  function tabs() {
    const nav = $('#tabs'); if (!nav) return;
    let activeSec = null;
    $$('button', nav).forEach(b => {
      const id = (b.id || '').replace(/^tab-/, '');
      const sec = !PRIMARY.includes(id);
      b.classList.toggle('sk-sec', sec);
      if (sec && b.getAttribute('aria-selected') === 'true') activeSec = b;
    });
    if (!more) {
      more = document.createElement('button');
      more.id = 'skMore'; more.type = 'button'; more.setAttribute('aria-expanded', 'false'); more.setAttribute('aria-controls', 'tabs');
      more.addEventListener('click', () => {
        const open = !nav.classList.contains('sk-open');
        nav.classList.toggle('sk-open', open); more.setAttribute('aria-expanded', String(open));
        paintMore();
      });
      nav.insertAdjacentElement('afterend', more);
      nav.addEventListener('click', e => {           // escolher uma aba secundária fecha o menu
        const b = e.target.closest('button.sk-sec');
        if (b) setTimeout(() => { nav.classList.remove('sk-open'); more.setAttribute('aria-expanded', 'false'); paintMore(); }, 0);
      });
    }
    paintMore(activeSec);
  }
  function paintMore(sel) {
    const nav = $('#tabs'); if (!nav || !more) return;
    const act = sel || $$('button.sk-sec', nav).find(b => b.getAttribute('aria-selected') === 'true');
    const open = nav.classList.contains('sk-open');
    more.classList.toggle('has-active', !!act && !open);
    const name = act ? (act.childNodes[0] && act.childNodes[0].textContent.trim()) : '';
    more.textContent = open ? T('Menos ▴', 'Less ▴') : (act && name ? `${T('Mais', 'More')} · ${name} ▾` : `${T('Mais', 'More')} ▾`);
  }

  /* ---------- 2. assinatura da classe atrás do medalhão ---------- */
  function hero() {
    const row = $('.brand-row'), medal = $('.asc-medal'); if (!row || !medal || $('.skfx', row) || !window.skFx) return;
    const fx = window.skFx(window.SK_FX[build] || 'stars');
    row.insertBefore(fx, row.firstChild);
    const fit = () => fx.style.setProperty('--m', medal.offsetWidth + 'px');
    fit();
    if (window.ResizeObserver) new ResizeObserver(fit).observe(medal);
  }

  /* ---------- 3. aba Agora: o essencial primeiro, o resto dobrado ---------- */
  function polishAgora() {
    const v = $('#v-agora'); if (!v || !v.classList.contains('on') && v.offsetParent === null) return;
    const split = $('.nowcard .split', v);
    if (split && /≈\s*0\s*%/.test(split.textContent)) split.classList.add('sk-hide');   // build de uma skill só: a barra "seu dano / dano do outro" não diz nada
    const grids = $$(':scope > .grid.g2', v);
    const stop = $$(':scope > .sechead', v)[1];
    const early = grids.filter(g => !stop || (g.compareDocumentPosition(stop) & Node.DOCUMENT_POSITION_FOLLOWING));
    const fold = (g, label) => {
      const d = document.createElement('details'); d.className = 'sk-more';
      d.innerHTML = `<summary>${label}</summary><div class="sk-body"></div>`;
      g.replaceWith(d); $('.sk-body', d).appendChild(g);
    };
    if (early.length >= 3) {
      fold(early[0], T('Marcos desta fase e o que falta para a próxima', 'Phase milestones and what is left for the next one'));
      fold(early[2], T('Todos os uniques desta fase', 'Every unique for this phase'));
    }
  }

  /* ---------- ligações ---------- */
  function watch(sel, fn, opts) {
    const el = $(sel); if (!el) return;
    let raf = 0;
    new MutationObserver(() => { if (raf) return; raf = requestAnimationFrame(() => { raf = 0; fn(); }); }).observe(el, opts || { childList: true, subtree: true, attributes: true, attributeFilter: ['aria-selected', 'class'] });
    fn();
  }
  let booted = false;
  const boot = () => { if (booted || !$('#tabs')) return; booted = true; hero(); watch('#tabs', tabs); watch('#v-agora', polishAgora, { childList: true }); };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
  addEventListener('load', boot);
})();
