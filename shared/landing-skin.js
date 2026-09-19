/* Página inicial: cada cartão ganha a animação de assinatura da sua classe (shared/fx.js). */
(() => {
  if (!window.skFx) return;
  document.querySelectorAll('.build').forEach(card => {
    const key = [...card.classList].find(c => c !== 'build' && window.SK_FX[c]);
    const art = card.querySelector('.build-art'), medal = card.querySelector('.medal');
    if (!key || !art || !medal) return;
    const fx = window.skFx(window.SK_FX[key]);
    art.insertBefore(fx, art.firstChild);
    const fit = () => fx.style.setProperty('--m', medal.offsetWidth + 'px');
    fit();
    if (window.ResizeObserver) new ResizeObserver(fit).observe(medal);
  });
})();
