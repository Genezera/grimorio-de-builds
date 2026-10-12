/* Runes of Aldur — bilingual challenge tracker. Game objectives: PoE2DB. */
(() => {
  const pt = document.documentElement.lang === 'pt-BR';
  const L = (a, b) => pt ? a : b;
  const esc = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const KEY = 'aldur1:progress';
  let state = {};
  try { state = JSON.parse(localStorage.getItem(KEY)) || {}; } catch { state = {}; }
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch {} };
  const on = key => !!state[key];
  const num = (key, max) => Math.max(0, Math.min(max, Number(state[key]) || 0));

  const challenges = [
    {id:'runeseeker', glyph:'ᚱ', phase:L('CAMPANHA','CAMPAIGN'), name:'The Runeseeker', title:L('Decifre o Remnant','Read the Remnant'), desc:L('Inscreva do seu Tome sequências com estes comprimentos em Runic Remnants. Cada comprimento conta uma vez.','Inscribe sequences of these lengths from your Tome at Runic Remnants. Each length counts once.'), items:['2 Runes','3 Runes','4 Runes','5 Runes','6 Runes','7+ Runes'], tip:L('Remnants com mais espaços são raros. Guarde a sequência longa para quando encontrar um com pelo menos sete slots.','Remnants with many slots are rare. Save the long sequence for one with at least seven slots.')},
    {id:'hunter', glyph:'ᛉ', phase:L('CAMPANHA','CAMPAIGN'), name:'The Hunter', title:L('Seis caçadas opcionais','Six optional hunts'), desc:L('Derrote estes chefes opcionais ao atravessar a campanha.','Defeat these optional bosses as you travel through the campaign.'), items:['The Crowbell','Kabala, Constrictor Queen','Blackjaw, the Remnant','Great White One','Akthi, the Final Sting','Anundr, the Sandworm'], tip:L('Marque cada chefe no momento da luta para evitar voltar às áreas depois.','Tick each boss after the fight so you do not have to revisit areas later.')},
    {id:'ascendant', glyph:'ᛟ', phase:L('PROVAS','TRIALS'), name:'The Ascendant', title:L('Oito pontos de Ascendência','Eight Ascendancy points'), desc:L('Complete as quatro provas. Cada uma concede dois pontos.','Complete all four trials. Each grants two points.'), items:[L('Primeira prova','First Trial'),L('Segunda prova','Second Trial'),L('Terceira prova','Third Trial'),L('Prova final','Final Trial')], tip:L('O desafio conclui quando os oito pontos forem obtidos.','The challenge completes when all eight points have been earned.')},
    {id:'master', glyph:'ᛗ', phase:L('PERSONAGEM','CHARACTER'), name:'The Master', title:L('Alcance o nível 90','Reach level 90'), desc:L('Acompanhe seu nível atual. A barra conclui ao chegar ao 90.','Track your current level. The bar completes at level 90.'), number:{key:'level', max:100, goal:90, label:L('Nível atual','Current level')}, tip:L('Este é um objetivo de progressão longa. Continue mapeando enquanto avança nas demais challenges.','This is a long progression goal. Keep mapping while completing the other challenges.')},
    {id:'reliquarian', glyph:'ᚹ', phase:L('ITENS','ITEMS'), name:'The Reliquarian', title:L('Identifique 50 uniques','Identify 50 uniques'), desc:L('Conte os itens únicos que você identificou na liga.','Count the unique items you identified in the league.'), number:{key:'uniques', max:50, goal:50, label:L('Uniques identificados','Uniques identified')}, tip:L('O contador aqui é manual e fica salvo apenas neste navegador.','This counter is manual and saved only in this browser.')},
    {id:'artisan', glyph:'ᚷ', phase:L('CRAFTING','CRAFTING'), name:'The Artisan', title:L('Forje com Verisium','Forge with Verisium'), desc:L('Crie um item usando cada um dos 14 ingredientes listados.','Craft an item using each of the 14 listed ingredients.'), items:['Verisium','Runic Alloy','Adaptive Alloy','Protective Alloy','Expansive Alloy','Swift Alloy','Any Kalguuran Crest','Exceptional Verisium','Cyclonic Alloy','Prismatic Alloy','Mystic Alloy','Sovereign Alloy','Celestial Alloy','Any Flux'], tip:L('O requisito é usar cada ingrediente ao craftar um item, não apenas encontrá-lo.','You must use each ingredient to craft an item; finding it alone does not count.')},
    {id:'cartographer', glyph:'ᛇ', phase:L('ATLAS','ATLAS'), name:'The Cartographer', title:L('Complete a árvore principal','Complete the main tree'), desc:L('Aloque completamente a árvore passiva principal do Atlas.','Fully allocate the main Atlas Passive Tree.'), items:[L('Árvore principal completamente alocada','Main Atlas tree fully allocated')], tip:L('Confira a conclusão dentro do jogo. A contagem de pontos exibida em fontes da comunidade diverge; este checklist acompanha o requisito oficial sem fixar um número.','Check completion in game. Community sources disagree on the point count, so this checklist follows the objective without fixing a number.')},
    {id:'vanquisher', glyph:'ᛏ', phase:'ENDGAME', name:'The Vanquisher', title:L('Vença os três pinnacles','Defeat the three pinnacles'), desc:L('Derrote cada chefe do endgame, incluindo o Vessel of Kulemak em força máxima.','Defeat each endgame boss, including Vessel of Kulemak at full strength.'), items:['Vessel of Kulemak — '+L('força máxima','full strength'),'The Bodach','Tangmazu'], tip:L('Verifique a condição “full strength” antes de marcar Vessel of Kulemak.','Check the “full strength” condition before ticking Vessel of Kulemak.')}
  ];
  const hunterAreas = [
    ['Hunting Grounds',L('Ato 1','Act 1')],
    ['Keth',L('Ato 2','Act 2')],
    ["Jiquani’s Machinarium",L('Ato 3','Act 3')],
    ['Whakapanu Island',L('Ato 4','Act 4')],
    ['The Khari Crossing',L('Interlúdio 2','Interlude 2')],
    ['The Khari Crossing',L('Interlúdio 2','Interlude 2')]
  ];
  const ART = '../shared/art/aldur/';
  const visuals = {
    runeseeker:['hero.jpg','remnant.webp'], hunter:['scene-5.jpg','rune.webp'],
    ascendant:['mechanic.jpg','ward.webp'], master:['scene-7.jpg','rune.webp'],
    reliquarian:['mechanic.jpg','crest.webp'], artisan:['mechanic.jpg','anvil.webp'],
    cartographer:['scene-7.jpg','remnant.webp'], vanquisher:['scene-5.jpg','ward.webp']
  };
  const steps = {
    runeseeker: L(['Encontre um Runic Remnant durante a campanha ou nos mapas.','Confira quantos espaços de runa ele oferece antes de inscrever.','Use seu Tome e complete uma inscrição de cada comprimento pedido.'],['Find a Runic Remnant in the campaign or maps.','Check its rune slots before inscribing.','Use your Tome to complete an inscription of each required length.']),
    hunter: L(['Siga a campanha e procure os chefes opcionais nas áreas indicadas.','Os dois últimos estão em The Khari Crossing no Interlúdio 2.','Marque cada chefe depois da vitória.'],['Follow the campaign and find the optional bosses in the listed areas.','The final two are in The Khari Crossing in Interlude 2.','Tick each boss after defeating it.']),
    ascendant: L(['Faça a primeira e a segunda prova durante a campanha.','Volte às provas de nível mais alto para obter os pontos restantes.','Confirme que recebeu todos os oito pontos de Ascendência.'],['Complete the first two trials during the campaign.','Return to higher-level trials for the remaining points.','Confirm that you have earned all eight Ascendancy points.']),
    master: L(['Atualize seu nível no campo ao lado.','Continue a progressão nos mapas e no Atlas.','O objetivo conclui quando você alcançar o nível 90.'],['Update your level in the field beside this guide.','Continue progressing through maps and the Atlas.','The objective completes when you reach level 90.']),
    reliquarian: L(['Separe uniques que ainda não foram identificados.','Identifique cada item e some no contador.','Complete a contagem de 50 itens identificados.'],['Keep unique items that are still unidentified.','Identify each item and add it to the counter.','Reach a total of 50 identified items.']),
    artisan: L(['Use um ingrediente de Verisium ao criar um item.','Repita com cada Alloy, Crest, Verisium e Flux da lista.','Marque apenas ingredientes efetivamente usados em um craft.'],['Use a Verisium ingredient when crafting an item.','Repeat with every Alloy, Crest, Verisium and Flux in the list.','Tick only ingredients you have actually used in a craft.']),
    cartographer: L(['Avance pela árvore passiva principal do Atlas.','Aloque todos os pontos exigidos nela.','Confirme no jogo que a árvore principal está completa.'],['Progress through the main Atlas Passive Tree.','Allocate all the points it requires.','Confirm in game that the main tree is complete.']),
    vanquisher: L(['Prepare a build para os encontros pinnacle.','Derrote The Bodach e Tangmazu.','Derrote Vessel of Kulemak em força máxima.'],['Prepare your build for pinnacle encounters.','Defeat The Bodach and Tangmazu.','Defeat Vessel of Kulemak at full strength.'])
  };

  function progress(c) {
    if (c.number) return {value:Math.min(c.number.goal,num(c.number.key,c.number.max)), goal:c.number.goal};
    return {value:c.items.filter((_,i)=>on(c.id+':'+i)).length, goal:c.items.length};
  }
  const done = c => { const p=progress(c); return p.value>=p.goal; };
  const total = () => challenges.filter(done).length;
  const ring = (fraction, size = 44) => {
    const r = size / 2 - 4, length = 2 * Math.PI * r;
    return `<svg class="ring" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" aria-hidden="true"><circle cx="${size/2}" cy="${size/2}" r="${r}" class="rt"/><circle cx="${size/2}" cy="${size/2}" r="${r}" class="rv" stroke-dasharray="${(length*Math.max(0,Math.min(1,fraction))).toFixed(1)} ${length.toFixed(1)}" transform="rotate(-90 ${size/2} ${size/2})"/></svg>`;
  };
  const icon = (name, cls = '') => `<img class="ico ${cls}" src="${ART}${name}" alt="" loading="lazy" decoding="async">`;

  function checklist(c) {
    if (c.number) {
      const v = num(c.number.key, c.number.max);
      return `<div class="aldur-number"><label for="num-${c.id}">${esc(c.number.label)}</label><div class="aldur-number-controls"><button class="btn sm" type="button" data-step="${c.number.key}:-1" aria-label="${esc(L('Diminuir','Decrease'))}">−</button><input id="num-${c.id}" type="number" inputmode="numeric" min="0" max="${c.number.max}" value="${v}" data-num="${c.number.key}"><button class="btn sm" type="button" data-step="${c.number.key}:1" aria-label="${esc(L('Aumentar','Increase'))}">+</button><b>/ ${c.number.goal}</b></div></div>`;
    }
    return `<div class="aldur-checks">${c.items.map((item,i) => {
      const key = `${c.id}:${i}`;
      const itemIcon = c.id === 'runeseeker' ? 'rune.webp' : c.id === 'artisan' ? (i===0 || i===7 ? 'verisium.webp' : i===6 ? 'crest.webp' : i===13 ? 'ward.webp' : 'alloy.webp') : null;
      return `<label class="chk aldur-check ${on(key)?'on':''}"><input type="checkbox" data-check="${key}" ${on(key)?'checked':''}><span class="gem" aria-hidden="true"></span>${itemIcon?icon(itemIcon,'ingredient'):''}<span class="lbl"><b>${esc(item)}</b>${c.id==='hunter'?`<small>${esc(hunterAreas[i].join(' · '))}</small>`:''}</span></label>`;
    }).join('')}</div>`;
  }

  function hero() {
    const n = total();
    const rewards = [[2,'reward-boots.webp',L('Botas','Boots')],[4,'reward-gloves.webp',L('Luvas','Gloves')],[6,'reward-body.webp',L('Armadura','Body Armour')],[8,'reward-helmet.webp',L('Elmo','Helmet')]];
    return `<section class="hero" id="top"><div class="hero-copy">
      <p class="kicker"><span class="dia"></span>${esc(L('Path of Exile 2 · 0.5 · Runes of Aldur','Path of Exile 2 · 0.5 · Runes of Aldur'))}</p>
      <h1><span class="h1a">RUNES OF</span><span class="h1b">ALDUR</span></h1>
      <p class="sub">${esc(L('O grimório das 8 challenges','The grimoire of 8 challenges'))}</p>
      <p class="lead">${esc(L('Inscribe runas, forje com Verisium e avance da campanha aos chefes do Atlas. Cada objetivo explicado, com seu progresso salvo neste navegador.','Inscribe runes, forge with Verisium and progress from the campaign to the Atlas bosses. Every objective explained, with progress saved in this browser.'))}</p>
      <div class="cta"><a class="btn primary" href="#runeseeker">${esc(L('Começar pela campanha','Start with the campaign'))} <span aria-hidden="true">→</span></a><a class="btn" href="#rewards">${esc(L('Recompensas da liga','League rewards'))}</a></div>
      <p class="ends">${esc(L('Progresso salvo neste navegador','Progress saved in this browser'))}</p>
      </div><div class="hero-sigil" aria-hidden="true"><svg class="circle c1" viewBox="0 0 400 400"><circle cx="200" cy="200" r="190"/><circle cx="200" cy="200" r="160"/><g>${Array.from({length:24},(_,i)=>`<line x1="200" y1="14" x2="200" y2="${i%3?30:42}" transform="rotate(${i*15} 200 200)"/>`).join('')}</g><polygon points="200,40 339,280 61,280"/><polygon points="200,360 61,120 339,120"/></svg><img class="totem" src="${ART}hero.jpg" alt="" decoding="async"><div class="count">${ring(n/8,132)}<b>${n}<small>/8</small></b><span>${esc(L('challenges concluídas','challenges completed'))}</span></div></div></section>
      <section class="rewards frame" id="rewards"><h2>${esc(L('Recompensas da liga','League rewards'))}</h2><ol class="track">${Array.from({length:8},(_,i)=>{const k=i+1,rw=rewards.find(x=>x[0]===k),earned=n>=k;return `<li class="${earned?'got':''} ${rw?'big':''}"><span class="step"><i>${k}</i></span>${rw?`<figure>${icon(rw[1])}<figcaption><b>Knight of Aldur</b><small>${esc(rw[2])}</small><em>${earned?esc(L('desbloqueada','unlocked')):`${esc(L('com','at'))} ${k}`}</em></figcaption></figure>`:`<span class="piece" aria-label="${esc(L('Peça do totem','Totem piece'))}">✦</span>`}</li>`}).join('')}</ol><p class="note">${esc(L('Cada challenge concluída também acrescenta uma peça ao Totem de Aldur do seu esconderijo.','Every completed challenge also adds a piece to your Aldur hideout totem.'))}</p></section>
      <section class="order frame"><h2>${esc(L('Ordem recomendada','Recommended order'))}</h2><ol><li>${esc(L('Campanha: Runeseeker, Hunter e primeiras provas.','Campaign: Runeseeker, Hunter and the first trials.'))}</li><li>${esc(L('Primeiros mapas: identificar uniques e forjar com Verisium.','Early maps: identify uniques and craft with Verisium.'))}</li><li>${esc(L('Atlas: completar a árvore principal, as provas e o nível 90.','Atlas: complete the main tree, trials and level 90.'))}</li><li>${esc(L('Endgame: enfrentar os três chefes pinnacle.','Endgame: defeat all three pinnacle bosses.'))}</li></ol></section>`;
  }

  function challenge(c,i) {
    const p=progress(c), complete=done(c), [banner,emblem]=visuals[c.id];
    return `<section class="ch frame ${complete?'complete':''}" id="${c.id}" aria-labelledby="title-${c.id}"><div class="ch-art" data-glyph="${esc(c.glyph)}" style="--art:url('${ART}${banner}')"><span class="num" aria-hidden="true">${String(i+1).padStart(2,'0')}</span></div>
      <header class="ch-head">${icon(emblem,'sigil')}<div class="ch-title"><h2 id="title-${c.id}">${esc(c.name)}</h2><p class="req"><span>${esc(L('Objetivo','Objective'))}:</span> ${esc(c.title)}</p><p class="reqpt">${esc(c.desc)}</p><div class="chips"><span class="chip">${esc(c.phase)}</span>${complete?`<span class="chip ok">✓ ${esc(L('Concluída','Completed'))}</span>`:''}</div></div><div class="ch-prog">${ring(p.value/p.goal,76)}<strong>${p.value}/${p.goal}</strong></div></header>
      <div class="ch-body"><div class="col steps"><h3>${esc(L('Como fazer','How to complete'))}</h3><ol>${steps[c.id].map(s=>`<li>${esc(s)}</li>`).join('')}</ol><h3 class="t2">${esc(L('Dica','Tip'))}</h3><ul class="tips"><li>${esc(c.tip)}</li></ul></div><div class="col tool"><h3>${esc(L('Acompanhe aqui','Track it here'))}</h3>${checklist(c)}</div></div></section>`;
  }

  function render(focusSelector) {
    const app=document.getElementById('app'), had=!!app.firstElementChild, y=scrollY;
    app.innerHTML=hero()+`<nav class="chnav" id="challenges" aria-label="${esc(L('Challenges','Challenges'))}"><div class="chnav-in">${challenges.map(c=>`<a href="#${c.id}" class="${done(c)?'ok':''}">${ring(progress(c).value/progress(c).goal,30)}<span>${esc(c.name.replace('The ',''))}</span></a>`).join('')}</div></nav><div class="chlist">${challenges.map(challenge).join('')}</div>
      <section class="mechs" id="mechanics"><h2>${esc(L('Mecânicas da liga','League mechanics'))}</h2><p class="lead2">${esc(L('Runic Remnants, Verisium e os chefes que acompanham a jornada.','Runic Remnants, Verisium and the bosses along the journey.'))}</p><div class="mgrid">${[['hero.jpg','Runic Remnants',L('Inscribe sequências no remnant e enfrente os inimigos invocados.','Inscribe sequences at a remnant and face summoned enemies.')],['mechanic.jpg','Verisium',L('Use os ingredientes da liga para criar itens e avançar no desafio The Artisan.','Use league ingredients to craft items and advance The Artisan.')],['scene-5.jpg',L('Chefes','Bosses'),L('Da campanha aos encontros pinnacle do Atlas.','From the campaign to Atlas pinnacle encounters.')]].map(m=>`<article class="mech frame"><img src="${ART+m[0]}" alt="" loading="lazy"><div><h3>${esc(m[1])}</h3><p>${esc(m[2])}</p></div></article>`).join('')}</div></section>
      <footer class="foot"><h2>${esc(L('Fontes','Sources'))}</h2><ul><li><a href="https://poe2db.tw/us/Runes_of_Aldur_challenges" target="_blank" rel="noopener noreferrer">PoE2DB ↗</a></li><li><a href="https://www.pathofexile.com/forum/view-thread/3932540" target="_blank" rel="noopener noreferrer">Path of Exile ↗</a></li></ul><p>${esc(L('Projeto de fã, sem vínculo com a Grinding Gear Games. Arte e ícones © Grinding Gear Games.','Fan project, not affiliated with Grinding Gear Games. Art and icons © Grinding Gear Games.'))}</p><button type="button" class="btn sm ghost" id="reset">${esc(L('Zerar progresso','Reset progress'))}</button></footer>`;
    app.querySelector('#reset').addEventListener('click',()=>{if(confirm(L('Apagar o progresso de Runes of Aldur neste navegador?','Erase Runes of Aldur progress in this browser?'))){state={};save();render();}});
    if(had){scrollTo(0,y);if(focusSelector)document.querySelector(focusSelector)?.focus({preventScroll:true});}
    observe();
  }

  document.addEventListener('change',e=>{const t=e.target;if(t.matches('[data-check]')){state[t.dataset.check]=t.checked;save();burst(t);render(`[data-check="${CSS.escape(t.dataset.check)}"]`);}if(t.matches('[data-num]')){const c=challenges.find(x=>x.number?.key===t.dataset.num);state[t.dataset.num]=Math.max(0,Math.min(c.number.max,parseInt(t.value,10)||0));save();render(`[data-num="${t.dataset.num}"]`);}});
  document.addEventListener('click',e=>{const t=e.target.closest('[data-step]');if(!t)return;const [key,step]=t.dataset.step.split(':');const c=challenges.find(x=>x.number?.key===key);state[key]=Math.max(0,Math.min(c.number.max,num(key,c.number.max)+Number(step)));save();render(`[data-step="${t.dataset.step}"]`);});
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function burst(el){if(reduce)return;const r=el.getBoundingClientRect();for(let i=0;i<8;i++){const s=document.createElement('span');s.className='spark';s.style.left=(r.left+r.width/2)+'px';s.style.top=(r.top+r.height/2)+'px';const a=i*Math.PI/4;s.style.setProperty('--dx',Math.cos(a)*(20+i*2)+'px');s.style.setProperty('--dy',Math.sin(a)*(20+i*2)+'px');document.body.append(s);setTimeout(()=>s.remove(),750);}}
  let io;
  function observe(){if(reduce||!('IntersectionObserver' in window))return;io?.disconnect();io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}}),{rootMargin:'0px 0px -8% 0px'});document.querySelectorAll('.ch,.mech,.rewards,.order').forEach(el=>{if(el.getBoundingClientRect().top>innerHeight*.9){el.classList.add('rv');io.observe(el);}});}
  function embers(){const canvas=document.getElementById('embers');if(!canvas||reduce)return;const ctx=canvas.getContext('2d');let w,h,particles=[];function size(){w=innerWidth;h=innerHeight;const d=Math.min(2,devicePixelRatio||1);canvas.width=w*d;canvas.height=h*d;ctx.setTransform(d,0,0,d,0,0);particles=Array.from({length:Math.min(55,Math.round(w*h/24000))},()=>({x:Math.random()*w,y:Math.random()*h,r:.7+Math.random()*2,s:.12+Math.random()*.4,a:Math.random()*6}));}size();addEventListener('resize',size,{passive:true});function draw(){if(!document.hidden){ctx.clearRect(0,0,w,h);for(const p of particles){p.y-=p.s;p.x+=Math.sin(p.a+=.01)*.25;if(p.y<0)p.y=h;ctx.fillStyle=`rgba(107,218,205,${.17+.25*Math.sin(p.a)})`;ctx.shadowColor='#6bdacd';ctx.shadowBlur=14;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill();}}requestAnimationFrame(draw);}draw();}
  render();embers();if(location.hash)requestAnimationFrame(()=>document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView());
})();
