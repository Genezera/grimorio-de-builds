/* FX v1 — cria o elemento .skfx (animação de assinatura) para uma "classe" de efeito. Usado por skin.js (builds) e landing.js (página inicial). */
window.skFx = kind => {
  const fx = document.createElement('span');
  fx.className = 'skfx fx-' + kind; fx.setAttribute('aria-hidden', 'true');
  if (kind === 'lightning') {
    fx.innerHTML = '<svg viewBox="0 0 100 100"><path d="M50 2 L43 -11 L53 -15 L45 -30"/><path d="M98 46 L112 39 L107 52 L124 46"/><path d="M50 98 L57 112 L47 116 L55 131"/><path d="M2 54 L-12 61 L-7 48 L-23 53"/></svg>';
  } else {
    const n = kind === 'void' ? 3 : kind === 'stars' ? 14 : kind === 'frost' ? 12 : 9;
    fx.innerHTML = Array.from({ length: n }, (_, i) => `<i style="--x:${(8 + (i * 83 / n + (i % 3) * 7)) % 92};--y:${(i * 37) % 90};--d:${((i * 0.53) % 3.6).toFixed(2)}s;--dx:${(i % 2 ? 1 : -1) * (8 + (i % 4) * 4)}px"></i>`).join('');
  }
  return fx;
};
window.SK_FX = { silverfist: 'spirit', oracle: 'stars', tactician: 'fire', infernalist: 'hell', acolyte: 'void', pathfinder: 'toxic', smith: 'forge', martial: 'lightning', shaman: 'lightning', legionnaire: 'lightning', whirling: 'frost', twister: 'lightning', hyperspeed: 'lightning',
                 sf: 'spirit', or: 'stars', ta: 'fire', in: 'hell', ac: 'void', pf: 'toxic', sk: 'forge', ma: 'lightning', sh: 'lightning', lg: 'lightning', gw: 'frost', tw: 'lightning', hs: 'lightning' };
