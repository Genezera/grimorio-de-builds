/* Navigation, local search and accessible reading tools shared by both builds. */
const GUIDE_ORACLE = Object.prototype.hasOwnProperty.call(VIEWS, 'totem');
const GUIDE_GROUPS = [
  [T('Sua jornada','Your journey'), ['agora','meu','quando','rota','quests']],
  [T('Monte a build','Build setup'), ['skills','gear','craft','uniques','arvore','asc']],
  [T('Domine a build','Master the build'), ['totem','mech','caca','zoo','meta','tricks','atlas']],
  [T('Ajuda & fontes','Help & sources'), ['diag','fontes']]
];
const GUIDE_HINTS = {
  agora: [T('Seu próximo passo','Your next step'), T('Ajuste o nível e a etapa acima. Resolva o objetivo desta fase antes de comprar a próxima peça de endgame.','Set your level and stage above. Complete this stage’s objective before buying the next endgame item.'),'meu'],
  meu: [T('Comece pelo personagem real','Start with your actual character'),T('Marque apenas o que você já tem e informe seu Spirit. As recomendações e os equipamentos passam a refletir essas escolhas.','Only tick what you actually own and enter your Spirit. Recommendations and gear will reflect these choices.'),'agora'],
  quando: [T('Poder equipar ≠ estar pronto','Equippable ≠ ready'),T('Compare o requisito do item com o momento da troca. Confira também a ascendência, as passivas e o Spirit necessários.','Compare the item requirement with the swap timing. Check the required ascendancy, passives and Spirit too.'),'gear'],
  rota: [T('Avance uma etapa por vez','One stage at a time'),T('Use a rota para planejar os próximos níveis. A etapa escolhida manualmente prevalece sobre a faixa automática de nível.','Use the route to plan your next levels. A manually selected stage overrides the automatic level range.'),'quests'],
  quests: [T('Poder permanente primeiro','Permanent power first'),T('Marque as recompensas já coletadas. Pontos de passiva e Spirit de quests podem resolver uma troca sem gastar currency.','Tick rewards you have already collected. Quest passives and Spirit may enable a swap without spending currency.'),'arvore'],
  skills: [T('Entenda cada encaixe','Understand each socket'),T('Escolha a fase, confira a função da skill e abra a explicação dos supports. Só ative reservas que cabem no seu Spirit.','Choose your stage, check each skill’s role and open the support explanation. Only enable reservations that fit your Spirit.'), GUIDE_ORACLE ? 'totem' : 'zoo'],
  gear: [T('Prioridade antes de perfeição','Priorities before perfection'),T('Compare os itens da fase com o que você já possui. Abra Crafting para escolher a base, os mods e um ponto de parada.','Compare stage gear with what you already own. Open Crafting to choose a base, modifiers and a stopping point.'),'craft'],
  craft: [T('Planeje antes de gastar','Plan before spending'),T('Escolha o equipamento e a rota. O nível do item libera mods; o nível do personagem define quando você pode equipá-lo.','Choose an item and a route. Item level unlocks modifiers; character level determines when you can equip it.'),'gear'],
  uniques: [T('Compre a função certa','Buy the right function'),T('Verifique a variante, os rolls e o requisito. O preço exibido é uma referência de pesquisa; confira a oferta na sua liga.','Check the variant, rolls and requirements. Displayed prices are research references; check listings in your league.'),'quando'],
  arvore: [T('Siga a ordem, confira os pontos','Follow the order, check your points'),T('Selecione a etapa e compare os pontos disponíveis. Use o zoom e o ajuste de enquadramento para localizar a próxima passiva.','Select your stage and check available points. Use zoom and fit controls to locate the next passive.'),'asc'],
  asc: [T('Planeje as dependências','Plan dependencies'),T('Pegue os notables na ordem do guia. Uma mudança de ascendência pode exigir ajustar armas, reservas ou skills antes da troca.','Take notables in the guide’s order. An ascendancy change may require adjusting weapons, reservations or skills first.'),'meu'],
  totem: [T('Spirit, mana e Runic Ward','Spirit, mana and Runic Ward'),T('São recursos diferentes. Confira quantos totems cabem e se as armaduras sustentam as skills de Runic Ward antes de ativar o setup.','These are different resources. Check totem capacity and whether your armour supports Runic Ward skills before enabling the setup.'),'craft'],
  mech: [T('Entenda a mecânica','Understand the mechanic'),(D.ui&&D.ui.mechHint)||T('Leia como a build causa dano e se defende, depois planeje o Spirit das skills persistentes.','Read how the build deals damage and defends, then plan the Spirit of your persistent skills.'),'skills'],
  caca: [T('Capture o tipo, depois busque o roll','Capture the type, then hunt the roll'),T('Filtre o beast pelo objetivo. Área correta não garante Haste: confira os modificadores antes de concluir a captura.','Filter beasts by your goal. The right area does not guarantee Haste: check modifiers before completing the capture.'),'zoo'],
  zoo: [T('Monte o zoo que cabe','Build a zoo that fits'),T('Informe o Spirit total e a eficiência real. Priorize o companion principal; acrescente auras depois de conferir o saldo.','Enter your actual Spirit and efficiency. Prioritise the main companion; add auras after checking the remaining budget.'),'meu'],
  meta: [T('Otimize o que já funciona','Optimise a working setup'),T('Resolva primeiro as dependências básicas. Compare cada upgrade com a melhoria mais barata que ainda falta no personagem.','Resolve core dependencies first. Compare each upgrade against the cheapest improvement still missing on your character.'),'craft'],
  tricks: [T('Uma melhoria por teste','One change per test'),T('Escolha um tema e aplique uma mudança de cada vez. Assim fica claro o que melhorou o dano, a defesa ou o conforto.','Pick a topic and apply one change at a time. This makes damage, defence and comfort improvements easier to measure.'),'diag'],
  atlas: [T('Mapeie com consistência','Map consistently'),T('Ajuste dificuldade e mecânicas ao seu equipamento. Se os mapas travarem, use o diagnóstico antes de aumentar o investimento.','Match difficulty and mechanics to your equipment. If mapping stalls, use troubleshooting before increasing investment.'),'diag'],
  diag: [T('Do sintoma à causa','From symptom to cause'),T('Procure o problema que está acontecendo agora. Confira skills, reservas e requisitos antes de tentar resolver tudo com uma compra.','Find the problem happening now. Check skills, reservations and requirements before trying to solve it with a purchase.'),'meu'],
  fontes: [T('Saiba de onde vem cada decisão','Know where each decision comes from'),T('As builds seguem seus autores; mecânicas e dados usam fontes separadas. O patch-alvo é 0.5.5 e a revisão de crafting é de 16/09/2026.','Builds follow their authors; mechanics and data use separate sources. The target patch is 0.5.5 and crafting was reviewed on 2026-09-16.'),'craft']
};
TABS.splice(TABS.findIndex(x => x[0] === 'gear') + 1, 0, ['craft', 'Crafting']);
VIEWS.craft = vCraft;
const guideOriginalRender = renderTab;
renderTab = function(id) {
  if (!VIEWS[id]) id = S.tab = 'agora';
  guideOriginalRender(id);
  document.querySelectorAll('#v-' + id + ' img').forEach(img => { img.loading = 'lazy'; img.decoding = 'async'; });
  if (id === 'craft') mountCraft();
  const hint = GUIDE_HINTS[id];
  if (hint) $('#readingGuide').innerHTML = `<p><b>${hint[0]}</b>${hint[1]}</p><a href="#${hint[2]}" data-guide-go="${hint[2]}">${esc(TABS.find(x=>x[0]===hint[2])?.[1] || '')} →</a>`;
  if (id === 'fontes') $('#v-fontes').insertAdjacentHTML('afterbegin', `<div class="craft-note">${T('Notas oficiais do patch-alvo:','Official target patch notes:')} <a href="https://www.pathofexile.com/forum/view-thread/4000864" target="_blank" rel="noopener">0.5.5</a> · <a href="https://www.pathofexile.com/forum/view-thread/4004106" target="_blank" rel="noopener">0.5.5b</a>. ${T('Veja as fontes de cada método na aba Crafting. Os caches antigos de preço não registram a liga nem a hora de coleta.','See each method’s sources in Crafting. Older price caches do not record the league or collection time.')}</div>`);
};
function guideGroup(id) { return GUIDE_GROUPS.findIndex(g=>g[1].includes(id)); }
function guideGo(id, push = true) {
  if (!VIEWS[id]) return;
  if (push && location.hash !== '#' + id) history.pushState(null, '', '#' + id);
  S.tab = id; store.set('tab', id); showTab();
}
function buildTabs() {
  const requested = location.hash.slice(1);
  if (VIEWS[requested]) S.tab = requested;
  if (!VIEWS[S.tab]) S.tab = 'agora';
  $('#tabs').setAttribute('aria-label', T('Seções do guia','Guide sections'));
  $('#tabs').innerHTML = TABS.map(([id,l]) => `<button id="tab-${id}" role="tab" type="button" data-tab="${id}" aria-controls="v-${id}" aria-selected="${S.tab === id}" tabindex="${S.tab===id?0:-1}">${esc(l)}${id==='quests'?'<span class="count" id="qcount"></span>':''}</button>`).join('');
  $('#tabs').onclick = e => { const b=e.target.closest('[data-tab]'); if (b) guideGo(b.dataset.tab); };
  $('#tabs').onkeydown = e => {
    const list=[...$('#tabs').querySelectorAll('button:not([hidden])')], i=list.indexOf(document.activeElement);
    let next;
    if(e.key==='ArrowRight') next=(i+1)%list.length;
    if(e.key==='ArrowLeft') next=(i-1+list.length)%list.length;
    if(e.key==='Home') next=0;
    if(e.key==='End') next=list.length-1;
    if(next!==undefined){e.preventDefault();guideGo(list[next].dataset.tab);list[next].focus();}
  };
  $('#navGroups').innerHTML=GUIDE_GROUPS.map(([label],i)=>`<button type="button" data-group="${i}" aria-pressed="false">${label}</button>`).join('');
  $('#navGroups').onclick=e=>{const b=e.target.closest('[data-group]');if(b){const g=GUIDE_GROUPS[+b.dataset.group];guideGo(g[1].find(id=>VIEWS[id]));}};
  document.querySelectorAll('section.view').forEach(el=>{el.setAttribute('role','tabpanel');el.setAttribute('aria-labelledby','tab-'+el.id.slice(2));el.tabIndex=0;});
  $('#guideTools').innerHTML=`<div class="guide-search"><label class="sr-only" for="guideSearch">${T('Buscar no guia','Search the guide')}</label><input id="guideSearch" type="search" placeholder="${T('Buscar item, skill ou dúvida…','Search items, skills or questions…')}" autocomplete="off" aria-controls="guideResults" aria-expanded="false"></div><div class="guide-tools-actions"><button type="button" id="guidePrint" title="${T('Imprimir a seção aberta','Print the open section')}">${T('Imprimir','Print')}</button><button type="button" id="guideLink" title="${T('Copiar link desta seção','Copy this section’s link')}">${T('Link','Link')}</button></div><div class="search-results" id="guideResults" hidden></div>`;
  $('#guideSearch').addEventListener('input',guideSearch);
  $('#guideSearch').addEventListener('keydown',e=>{if(e.key==='ArrowDown'){$('#guideResults button')?.focus();e.preventDefault();}});
  $('#guidePrint').onclick=()=>window.print();
  $('#guideLink').onclick=()=>guideCopy(location.href,T('Link copiado.','Link copied.'));
  document.body.insertAdjacentHTML('afterbegin',`<a class="guide-skip" href="#readingGuide">${T('Pular para o conteúdo','Skip to content')}</a>`);
}
function showTab() {
  if (!VIEWS[S.tab]) S.tab='agora';
  const group=guideGroup(S.tab);
  document.querySelectorAll('#tabs button').forEach(b=>{const active=b.dataset.tab===S.tab;b.setAttribute('aria-selected',active);b.tabIndex=active?0:-1;b.hidden=guideGroup(b.dataset.tab)!==group;});
  document.querySelectorAll('#navGroups button').forEach(b=>b.setAttribute('aria-pressed',+b.dataset.group===group));
  document.querySelectorAll('section.view').forEach(el=>{const active=el.id==='v-'+S.tab;el.classList.toggle('on',active);el.hidden=!active;});
  if(location.hash!== '#'+S.tab) history.replaceState(null,'','#'+S.tab);
  document.querySelectorAll('.langsw a').forEach(a=>{a.href=a.getAttribute('href').split('#')[0]+'#'+S.tab;});
  renderTab(S.tab);
}
const guidePlain=value=>String(value).replace(/<[^>]*>/g,' ').replace(/\s+/g,' ').trim();
const guideNorm=value=>guidePlain(value).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
function guideStrings(value, result=[]) {
  if(typeof value==='string' && value.length>3 && !/^(https?:|data:)/.test(value)) result.push(guidePlain(value));
  else if(Array.isArray(value)) value.forEach(v=>guideStrings(v,result));
  else if(value && typeof value==='object') Object.entries(value).forEach(([k,v])=>{if(!['ic','icon','img','url','id'].includes(k)) guideStrings(v,result);});
  return result;
}
let guideIndex;
function guideSearch() {
  const q=guideNorm($('#guideSearch').value), box=$('#guideResults');
  box.hidden=q.length<2;$('#guideSearch').setAttribute('aria-expanded',!box.hidden);
  if(box.hidden) return;
  if(!guideIndex){
    const sources={agora:D.phases,meu:GUIDE_HINTS.meu,quando:D.timing,rota:D.phases,quests:D.quests,skills:D.phases.map(p=>p.gems),gear:[D.gear,A.sets],craft:craftRecipes(),uniques:D.uniques,arvore:D.keyPassives,asc:D.asc,totem:[D.totem,D.craft,D.phases],mech:D.mech,caca:D.hunt,zoo:D.beasts,meta:[D.meta,D.optimizations],tricks:D.tricks,atlas:D.atlas,diag:D.fixes,fontes:D.sources};
    guideIndex=TABS.map(([id,label])=>({id,label,text:guideStrings([label,GUIDE_HINTS[id],sources[id]])}));
  }
  const hits=guideIndex.map(row=>({...row,matches:row.text.filter(s=>guideNorm(s).includes(q))})).filter(row=>row.matches.length);
  box.innerHTML=`<p class="search-status" role="status">${hits.length} ${T('seções encontradas','sections found')}</p>`+hits.map(row=>`<button type="button" data-search-go="${row.id}"><b>${esc(row.label)}</b><small>${esc(row.matches[0].slice(0,170))}${row.matches[0].length>170?'…':''}</small></button>`).join('')+(!hits.length?`<p>${T('Tente o nome em inglês do item ou termos como Spirit, mana e resistências.','Try the English item name or terms such as Spirit, mana and resistances.')}</p>`:'');
}
function guideToast(message){document.querySelector('.guide-toast')?.remove();const el=document.createElement('div');el.className='guide-toast';el.role='status';el.textContent=message;document.body.append(el);setTimeout(()=>el.remove(),3500);}
async function guideCopy(text,message){try{await navigator.clipboard.writeText(text);guideToast(message);}catch{const el=document.createElement('textarea');el.value=text;el.style.position='fixed';el.style.opacity='0';document.body.append(el);el.select();const ok=document.execCommand('copy');el.remove();guideToast(ok?message:T('Não foi possível copiar. Use a barra de endereço ou selecione o texto.','Copy failed. Use the address bar or select the text.'));}}
document.addEventListener('click',e=>{
  if(e.target.closest('a[data-gotab],a[data-gotree]'))e.preventDefault();
  const target=e.target.closest('[data-guide-go],[data-search-go]');
  if(target){e.preventDefault();guideGo(target.dataset.guideGo||target.dataset.searchGo);$('#guideResults').hidden=true;$('#guideSearch').setAttribute('aria-expanded','false');$('#v-'+S.tab).focus({preventScroll:true});$('#readingGuide').scrollIntoView({block:'start',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});}
  else if(!e.target.closest('#guideTools')){$('#guideResults').hidden=true;$('#guideSearch').setAttribute('aria-expanded','false');}
});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){$('#guideResults').hidden=true;$('#guideSearch').setAttribute('aria-expanded','false');if(document.activeElement.closest('#guideResults'))$('#guideSearch').focus();}if((e.ctrlKey||e.metaKey)&&e.key==='k'){e.preventDefault();$('#guideSearch').focus();}});
addEventListener('popstate',()=>{const id=location.hash.slice(1);if(VIEWS[id])guideGo(id,false);});
addEventListener('hashchange',()=>{const id=location.hash.slice(1);if(VIEWS[id]&&S.tab!==id)guideGo(id,false);});
