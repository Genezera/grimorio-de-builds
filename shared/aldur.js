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
  function checklist(c) {
    if (c.number) {
      const v=num(c.number.key,c.number.max);
      return `<div class="number-tool"><label for="num-${c.id}">${esc(c.number.label)}</label><div class="number-controls"><button type="button" data-step="${c.number.key}:-1" aria-label="${esc(L('Diminuir','Decrease'))}">−</button><input id="num-${c.id}" type="number" inputmode="numeric" min="0" max="${c.number.max}" value="${v}" data-num="${c.number.key}"><button type="button" data-step="${c.number.key}:1" aria-label="${esc(L('Aumentar','Increase'))}">+</button><span>/ ${c.number.goal}</span></div></div>`;
    }
    return `<div class="check-grid">${c.items.map((item,i)=>{
      const itemIcon=c.id==='runeseeker'?'rune.webp':c.id==='artisan'?(i===0||i===7?'verisium.webp':i===6?'crest.webp':i===13?'ward.webp':'alloy.webp'):null;
      return `<label class="check ${on(c.id+':'+i)?'checked':''}"><input type="checkbox" data-check="${c.id}:${i}" ${on(c.id+':'+i)?'checked':''}><span class="check-mark" aria-hidden="true">✦</span>${itemIcon?`<img class="check-item-icon" src="${ART+itemIcon}" alt="" loading="lazy">`:''}<span>${esc(item)}${c.id==='hunter'?`<small>${esc(hunterAreas[i].join(' · '))}</small>`:''}</span></label>`;
    }).join('')}</div>`;
  }
  function card(c,i) {
    const p=progress(c), completed=done(c);
    const [banner,icon]=visuals[c.id];
    return `<article class="challenge ${completed?'complete':''}" id="${c.id}" aria-labelledby="title-${c.id}">
      <div class="challenge-banner"><img src="${ART+banner}" alt="" loading="lazy" decoding="async"><span class="banner-number">${String(i+1).padStart(2,'0')}</span></div>
      <div class="challenge-inner"><header class="challenge-header"><div class="challenge-emblem"><img src="${ART+icon}" alt="" loading="lazy"></div><div class="challenge-heading"><p class="true-name">${esc(c.name)} <span>· ${esc(c.phase)}</span></p><h3 id="title-${c.id}">${esc(c.title)}</h3><p class="description">${esc(c.desc)}</p></div><div class="challenge-count"><b>${p.value}<small>/${p.goal}</small></b><span>${completed?esc(L('CONCLUÍDO','COMPLETE')):esc(L('PROGRESSO','PROGRESS'))}</span></div></header>
      <div class="meter" role="progressbar" aria-valuenow="${p.value}" aria-valuemin="0" aria-valuemax="${p.goal}" aria-label="${esc(c.name)}"><span style="width:${p.value/p.goal*100}%"></span></div>
      <div class="challenge-body"><div class="guide-column"><h4>${esc(L('Como fazer','How to complete'))}</h4><ol>${steps[c.id].map(s=>`<li>${esc(s)}</li>`).join('')}</ol><p class="tip"><span aria-hidden="true">✦</span>${esc(c.tip)}</p></div><div class="tool-column"><h4>${esc(L('Acompanhe aqui','Track it here'))}</h4>${checklist(c)}</div></div></div></article>`;
  }
  function render(focusSelector) {
    const n=total();
    const app=document.getElementById('app'), wasRendered=!!app.firstElementChild, y=scrollY;
    document.getElementById('app').innerHTML=`<section class="hero" id="top"><div class="hero-copy"><p class="eyebrow"><span class="line"></span> PATH OF EXILE 2 <span class="dot">✦</span> ${esc(L('LIGA 0.5','0.5 LEAGUE'))}</p><h1>Runes <em>of</em><br><span>Aldur</span></h1><p class="hero-sub">${esc(L('O grimório das oito challenges','The grimoire of eight challenges'))}</p><p class="hero-description">${esc(L('Inscribe runas, forje com Verisium e avance da campanha aos chefes do Atlas. Cada objetivo explicado, com seu progresso salvo neste navegador.','Inscribe runes, forge with Verisium and progress from the campaign to the Atlas bosses. Every objective explained, with progress saved in this browser.'))}</p><div class="hero-actions"><a class="button primary" href="#runeseeker">${esc(L('Começar pelas runas','Start with runes'))} <span>→</span></a><a class="button secondary" href="#challenges">${esc(L('Ver as 8 challenges','See all 8 challenges'))}</a></div><p class="hero-foot">✦ ${esc(L('Seu progresso fica neste navegador','Your progress stays in this browser'))}</p></div><div class="hero-art" aria-hidden="true"><img class="hero-game" src="${ART}hero.jpg" alt=""><div class="hero-art-glow"></div><img class="hero-totem" src="${ART}totem.webp" alt=""><span class="hero-rune">ᚱ · ᚢ · ᚾ · ᛖ · ᛋ</span></div></section>
    <section class="overview" id="rewards" aria-label="${esc(L('Seu progresso','Your progress'))}"><div class="overview-lead"><span class="section-label">${esc(L('SUA JORNADA','YOUR JOURNEY'))}</span><strong>${n}<small>/8</small></strong><span>${esc(L('challenges concluídas','challenges complete'))}</span><img src="${ART}remnant.webp" alt=""></div><div class="reward-track"><div class="reward-head"><h2>${esc(L('Recompensas da liga','League rewards'))}</h2><p>Knight of Aldur Armour Set</p></div><div class="milestones">${[[2,'reward-boots.webp',L('Botas','Boots')],[4,'reward-gloves.webp',L('Luvas','Gloves')],[6,'reward-body.webp',L('Armadura','Body Armour')],[8,'reward-helmet.webp',L('Elmo','Helmet')]].map(([v,img,name])=>`<div class="milestone ${n>=v?'earned':''}"><span class="milestone-icon"><img src="${ART+img}" alt="" loading="lazy"></span><b>${v}/8</b><small>${esc(name)}</small></div>`).join('')}</div><p class="reward-note"><img src="${ART}totem.webp" alt="">${esc(L('Cada challenge também acrescenta uma peça ao Totem de Aldur no esconderijo.','Each challenge also adds a piece to the Aldur hideout totem.'))}</p></div></section>
    <section class="route" id="route"><div class="section-intro"><span class="section-label">${esc(L('ORDEM SUGERIDA','SUGGESTED ORDER'))}</span><h2>${esc(L('Da campanha ao Atlas','From campaign to Atlas'))}</h2></div><div class="route-steps"><div><img src="${ART}hero.jpg" alt="" loading="lazy"><span>01</span><b>${esc(L('Campanha','Campaign'))}</b><p>${esc(L('Inscribe sequências, derrote os chefes opcionais e faça as primeiras provas.','Inscribe rune sequences, defeat optional bosses and complete the first trials.'))}</p></div><div><img src="${ART}mechanic.jpg" alt="" loading="lazy"><span>02</span><b>${esc(L('Forja e mapas','Forge and maps'))}</b><p>${esc(L('Identifique uniques, use Verisium e avance pela árvore principal.','Identify uniques, use Verisium and advance through the main Atlas tree.'))}</p></div><div><img src="${ART}scene-5.jpg" alt="" loading="lazy"><span>03</span><b>Endgame</b><p>${esc(L('Chegue ao nível 90, finalize as provas e vença os pinnacles.','Reach level 90, finish the trials and defeat the pinnacles.'))}</p></div></div></section>
    <section class="challenge-section" id="challenges"><div class="section-intro"><span class="section-label">${esc(L('OITO MARCAS NO TOTEM','EIGHT MARKS ON THE TOTEM'))}</span><h2>${esc(L('Seu códice de desafios','Your challenge codex'))}</h2><p>${esc(L('Marque as etapas conforme concluir no jogo. As alterações são salvas automaticamente neste navegador.','Tick each step as you complete it in game. Changes save automatically in this browser.'))}</p></div><nav class="challenge-nav" aria-label="${esc(L('Navegar pelos desafios','Browse challenges'))}">${challenges.map((c,i)=>`<a href="#${c.id}" class="${done(c)?'complete':''}"><span>${String(i+1).padStart(2,'0')}</span>${esc(c.name.replace('The ',''))}</a>`).join('')}</nav><div class="challenge-grid">${challenges.map(card).join('')}</div></section>
    <footer class="footer"><div><span class="section-label">GRIMÓRIO DE BUILDS</span><p>${esc(L('Projeto de fã, sem vínculo com a Grinding Gear Games. Arte do jogo © Grinding Gear Games.','Fan project, not affiliated with Grinding Gear Games. Game art © Grinding Gear Games.'))}</p><p>${esc(L('Objetivos consultados em 12/10/2026. Confirme a conclusão no jogo.','Objectives checked on 2026-10-12. Confirm completion in game.'))}</p></div><div class="footer-links"><a href="https://poe2db.tw/us/Runes_of_Aldur_challenges" target="_blank" rel="noopener noreferrer">${esc(L('Fonte dos objetivos','Objective source'))} ↗</a><a href="https://www.pathofexile.com/forum/view-thread/3932540" target="_blank" rel="noopener noreferrer">${esc(L('Notas oficiais 0.5','Official 0.5 notes'))} ↗</a><button type="button" id="reset">${esc(L('Zerar meu progresso','Reset my progress'))}</button></div></footer>`;
    document.getElementById('reset').addEventListener('click',()=>{if(confirm(L('Apagar o progresso de Runes of Aldur neste navegador?','Erase Runes of Aldur progress in this browser?'))){state={};save();render();}});
    if(wasRendered){scrollTo(0,y);if(focusSelector)document.querySelector(focusSelector)?.focus({preventScroll:true});}
  }
  document.addEventListener('change',e=>{
    const t=e.target;
    if(t.matches('[data-check]')) {state[t.dataset.check]=t.checked; save(); burst(t);render(`[data-check="${CSS.escape(t.dataset.check)}"]`);}
    if(t.matches('[data-num]')) {const c=challenges.find(x=>x.number?.key===t.dataset.num);state[t.dataset.num]=Math.max(0,Math.min(c.number.max,parseInt(t.value,10)||0));save();render(`[data-num="${t.dataset.num}"]`);}
  });
  document.addEventListener('click',e=>{
    const t=e.target.closest('[data-step]');if(!t)return;
    const [key,step]=t.dataset.step.split(':');const c=challenges.find(x=>x.number?.key===key);state[key]=Math.max(0,Math.min(c.number.max,num(key,c.number.max)+Number(step)));save();render(`[data-step="${t.dataset.step}"]`);
  });
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function burst(el){
    if(reduce)return;const r=el.getBoundingClientRect();
    for(let i=0;i<8;i++){const s=document.createElement('span');s.className='rune-spark';s.style.left=(r.left+r.width/2)+'px';s.style.top=(r.top+r.height/2)+'px';const a=i*Math.PI/4;s.style.setProperty('--dx',Math.cos(a)*(20+i*2)+'px');s.style.setProperty('--dy',Math.sin(a)*(20+i*2)+'px');document.body.append(s);setTimeout(()=>s.remove(),750);}
  }
  function embers(){
    const canvas=document.getElementById('embers');if(!canvas||reduce)return;const ctx=canvas.getContext('2d');let w,h,particles=[];
    function size(){w=innerWidth;h=innerHeight;const d=Math.min(2,devicePixelRatio||1);canvas.width=w*d;canvas.height=h*d;ctx.setTransform(d,0,0,d,0,0);particles=Array.from({length:Math.min(48,Math.round(w*h/28000))},()=>({x:Math.random()*w,y:Math.random()*h,r:.5+Math.random()*1.8,s:.12+Math.random()*.35,a:Math.random()*6}));}
    size();addEventListener('resize',size,{passive:true});
    function draw(){if(!document.hidden){ctx.clearRect(0,0,w,h);for(const p of particles){p.y-=p.s;p.x+=Math.sin(p.a+=.01)*.25;if(p.y<0)p.y=h;const alpha=.2+.2*Math.sin(p.a);ctx.fillStyle=`rgba(107,218,205,${alpha})`;ctx.shadowColor='#6bdacd';ctx.shadowBlur=12;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill();}}requestAnimationFrame(draw);}draw();
  }
  render();
  embers();
  if (location.hash) requestAnimationFrame(() => document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView());
})();
