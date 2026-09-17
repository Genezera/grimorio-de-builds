/* One adaptive build companion, shared by both guides and languages. */
const buildNow = {
  tab: ['now','gear','skills'].includes(store.get('buildNowTab','now')) ? store.get('buildNowTab','now') : 'now',
  collapsed: store.get('buildNowCollapsed',false), open:false, returnFocus:null,
  wide:matchMedia('(min-width:1440px)'), inert:[], overflow:''
};
function buildNowImage(src){return src?`<span class="bn-art"><img src="${esc(src)}" alt="" loading="lazy"></span>`:'<span class="bn-art bn-empty" aria-hidden="true">◇</span>';}
function buildNowLink(tab,label){return `<button type="button" class="bn-link" data-bn-go="${tab}">${esc(label)} <span aria-hidden="true">↗</span></button>`;}
function buildNowContent(){
  const p=curPhase(),pa=adaptPhase(p),oracle=Object.hasOwn(VIEWS,'totem');
  if(buildNow.tab==='gear'){
    const items=setItems(p.id);
    return `<div class="bn-section-heading"><h3>${T('Equipamento da fase','Phase equipment')}</h3><p>${T('Plano recomendado, ajustado ao que você marcou. Não é uma leitura do inventário do jogo.','Recommended plan, adjusted to what you checked. This is not your in-game inventory.')}</p></div>
      <div class="bn-items">${items.map(i=>`<button type="button" class="bn-item ${i.u?'unique':''}" data-bn-go="gear">${buildNowImage(ic(i.ic))}<span class="bn-item-copy"><small>${esc(i.slot)}</small><b>${esc(i.n)}</b><span>${i.price!=null?esc(fmtPrice(i.price))+' · ':''}${T('Ver detalhes','View details')} ↗</span></span></button>`).join('')||`<p>${T('Consulte os itens de leveling para esta fase.','See levelling items for this phase.')}</p>`}</div>${buildNowLink('gear',T('Comparar todos os itens','Compare all items'))}${buildNowLink('craft',T('Abrir crafting','Open crafting'))}`;
  }
  if(buildNow.tab==='skills'){
    const gems=pa.gems.filter(g=>!(g.until&&S.lv>=g.until));
    return `<div class="bn-section-heading"><h3>${T('Sua barra de skills','Your skill bar')}</h3><p>${T('Skill primeiro, supports logo abaixo. Abra o guia para conferir requisitos e substituições.','Skill first, supports below. Open the guide for requirements and alternatives.')}</p></div><div class="bn-skills">${gems.map(g=>`<article class="bn-skill"><button type="button" class="bn-item" data-bn-go="skills">${buildNowImage(gemImg(g.skill))}<span class="bn-item-copy"><small>${esc(g.role||T('Skill da fase','Phase skill'))}</small><b>${esc(g.skill)}</b><span>${g.sp==='opt'?T('Só se sobrar Spirit','Only with spare Spirit'):g.sp==='free'?T('Sem reserva de Spirit','No Spirit reservation'):T('Ver como usar','See how to use')} ↗</span></span></button>${(g.sup||[]).length?`<ul class="bn-supports" aria-label="Supports">${g.sup.map(s=>`<li>${supImg(s)?`<img src="${esc(supImg(s))}" alt="" loading="lazy">`:''}<span>${esc(s)}</span></li>`).join('')}</ul>`:''}</article>`).join('')}</div>${buildNowLink('skills',T('Abrir guia de skills','Open skill guide'))}`;
  }
  const recs=charRecs().recs.filter(x=>x.lvl!=='ok').sort((a,b)=>({bad:0,warn:1,tip:2}[a.lvl]??3)-({bad:0,warn:1,tip:2}[b.lvl]??3)).slice(0,3);
  const milestones=msList.filter(m=>m.lv>=S.lv).slice(0,3);
  return `<div class="bn-focus"><span class="bn-eyebrow">${T('Seu foco nesta fase','Your focus this phase')}</span><h3>${esc(p.carry)}</h3><p>${T('As sugestões usam seu nível, fase e escolhas em Meu personagem.','Suggestions use your level, phase and choices in My character.')}</p>${buildNowLink('meu',T('Atualizar meu personagem','Update my character'))}</div>
    <div class="bn-section-heading"><h3>${T('O que fazer agora','What to do now')}</h3><p>${T('Resolva uma prioridade por vez.','Work through one priority at a time.')}</p></div>
    <div class="bn-priorities">${recs.map((r,i)=>`<button type="button" class="bn-priority ${r.lvl}" data-bn-go="${VIEWS[r.tab]?r.tab:'meu'}"><span class="bn-number" aria-hidden="true">0${i+1}</span><span><small>${r.lvl==='bad'?T('Resolver primeiro','Resolve first'):r.lvl==='warn'?T('Antes de avançar','Before moving on'):T('Próxima melhoria','Next improvement')}</small><b>${esc(r.t)}</b><span class="bn-priority-more">${T('Ver orientação','See guidance')} ↗</span></span></button>`).join('')||`<div class="bn-clear">✓ ${T('Nenhuma pendência pelas suas escolhas. Confira o próximo marco.','No pending issues from your choices. Check the next milestone.')}</div>`}</div>
    ${milestones.length?`<div class="bn-section-heading"><h3>${T('Próximos marcos','Next milestones')}</h3></div><div class="bn-milestones">${milestones.map(m=>`<label class="${S.done['ms:'+m.lv]?'completed':''}"><input type="checkbox" data-bn-check="ms:${m.lv}" ${S.done['ms:'+m.lv]?'checked':''}><span><small>${T('Nível','Level')} ${m.lv}</small><b>${esc(m.t)}</b></span></label>`).join('')}</div>`:''}
    <div class="bn-shortcuts">${buildNowLink('arvore',T('Próximas passivas','Next passives'))}${buildNowLink(oracle?'totem':'zoo',oracle?T('Totems e mana','Totems and mana'):T('Planejar Spirit','Plan Spirit'))}</div>`;
}
function renderSide(){
  const side=document.getElementById('side');if(!side)return;
  const collapsed=buildNow.wide.matches&&buildNow.collapsed;
  const p=curPhase(),body=side.querySelector('.bn-scroll'),y=body?.scrollTop||0;
  document.querySelector('.app').classList.toggle('side-min',collapsed);
  side.classList.toggle('bn-collapsed',collapsed);side.classList.toggle('drawer',buildNow.open&&!buildNow.wide.matches);
  side.setAttribute('aria-label',T('Seu build agora','Your build now'));
  const modal=buildNow.open&&!buildNow.wide.matches;
  side.setAttribute('role',modal?'dialog':'complementary');
  if(modal)side.setAttribute('aria-modal','true');else side.removeAttribute('aria-modal');
  side.innerHTML=collapsed?`<button class="bn-expand" type="button" data-bn-toggle aria-label="${T('Expandir Seu build agora','Expand Your build now')}"><span aria-hidden="true">◈</span><b>${S.lv}</b><span class="bn-vertical">${T('Seu build','Your build')}</span><span aria-hidden="true">‹</span></button>`:
    `<header class="bn-header"><div><span class="bn-eyebrow">${T('Companheiro de jornada','Journey companion')}</span><h2>${T('Seu build, agora','Your build, now')}</h2></div><button class="bn-close" type="button" data-bn-toggle aria-label="${buildNow.wide.matches?T('Recolher painel','Collapse panel'):T('Fechar painel','Close panel')}">${buildNow.wide.matches?'›':'×'}</button></header>
    <div class="bn-phase"><span class="bn-level"><small>${T('NÍVEL','LEVEL')}</small><b>${S.lv}</b></span><div><b>${esc(p.name)}</b><small>${S.mode==='cheap'?T('Rota econômica','Budget route'):T('Rota completa','Full route')} · ${esc(p.tag||'')}</small></div></div>
    <div class="bn-tabs" role="tablist" aria-label="${T('Resumo da build','Build summary')}">${[['now',T('Agora','Now')],['gear',T('Equipamento','Equipment')],['skills','Skills']].map(([id,title])=>`<button id="bn-tab-${id}" type="button" role="tab" aria-controls="bn-content" aria-selected="${buildNow.tab===id}" tabindex="${buildNow.tab===id?0:-1}" data-bn-tab="${id}">${title}</button>`).join('')}</div>
    <div class="bn-scroll" id="bn-content" role="tabpanel" aria-labelledby="bn-tab-${buildNow.tab}" tabindex="0"><div class="bn-content">${buildNowContent()}</div></div>
    <footer class="bn-footer"><span class="bn-live" aria-hidden="true"></span>${T('Acompanha as escolhas do seu personagem','Follows your character choices')}</footer>`;
  side.querySelector('.bn-scroll')?.scrollTo(0,y);
  const fab=document.getElementById('sbFab');
  fab.setAttribute('aria-expanded',String(modal));fab.setAttribute('aria-haspopup','dialog');
  fab.innerHTML=`<span class="bn-fab-icon" aria-hidden="true">◈</span><span>${T('Seu build','Your build')}<small>${T('Nível','Level')} ${S.lv}</small></span><span aria-hidden="true">↗</span>`;
}
function openDrawer(open){
  if(open&&buildNow.wide.matches){buildNow.collapsed=false;store.set('buildNowCollapsed',false);renderSide();return;}
  if(open===buildNow.open)return;
  buildNow.open=open;
  if(open){
    buildNow.returnFocus=document.activeElement;buildNow.overflow=document.body.style.overflow;document.body.style.overflow='hidden';
    buildNow.inert=[...document.querySelectorAll('.app > main,.app > .rail,#sbFab')].map(el=>[el,el.inert]);buildNow.inert.forEach(([el])=>el.inert=true);
  }else{
    document.body.style.overflow=buildNow.overflow;buildNow.inert.forEach(([el,was])=>el.inert=was);buildNow.inert=[];
  }
  document.documentElement.classList.toggle('bn-modal',open);
  document.getElementById('sbShade').hidden=!open;renderSide();
  if(open)document.querySelector('[data-bn-toggle]')?.focus();else buildNow.returnFocus?.focus({preventScroll:true});
}
document.addEventListener('click',e=>{
  if(e.target.closest('#sbFab'))return openDrawer(true);
  if(e.target.closest('#sbShade'))return openDrawer(false);
  if(e.target.closest('[data-bn-toggle]')){
    if(!buildNow.wide.matches)return openDrawer(false);
    buildNow.collapsed=!buildNow.collapsed;store.set('buildNowCollapsed',buildNow.collapsed);renderSide();document.querySelector('[data-bn-toggle]')?.focus();return;
  }
  const tab=e.target.closest('[data-bn-tab]');
  if(tab){buildNow.tab=tab.dataset.bnTab;store.set('buildNowTab',buildNow.tab);renderSide();document.querySelector('.bn-scroll').scrollTop=0;document.querySelector('#bn-tab-'+buildNow.tab).focus();return;}
  const go=e.target.closest('[data-bn-go]');
  if(go){if(buildNow.open)openDrawer(false);guideGo(go.dataset.bnGo);document.querySelector('#v-'+S.tab)?.focus({preventScroll:true});document.querySelector('#readingGuide')?.scrollIntoView({block:'start',behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'instant':'smooth'});}
});
document.addEventListener('change',e=>{
  const key=e.target.dataset.bnCheck;if(!key)return;
  S.done[key]=e.target.checked;store.set('done',S.done);render();
  document.querySelector(`[data-bn-check="${CSS.escape(key)}"]`)?.focus({preventScroll:true});
  guideToast(T('Progresso atualizado e salvo.','Progress updated and saved.'));
});
document.addEventListener('keydown',e=>{
  if(buildNow.open&&e.key==='Escape'){e.preventDefault();openDrawer(false);return;}
  if(e.target.matches('[data-bn-tab]')&&['ArrowRight','ArrowLeft','Home','End'].includes(e.key)){
    e.preventDefault();const tabs=[...document.querySelectorAll('[data-bn-tab]')],i=tabs.indexOf(e.target),n=e.key==='Home'?0:e.key==='End'?2:(i+(e.key==='ArrowRight'?1:2))%3;tabs[n].click();
  }
  if(buildNow.open&&e.key==='Tab'){
    const nodes=[...document.querySelectorAll('#side button,#side input,#side [tabindex="0"]')].filter(el=>el.getClientRects().length&&!el.disabled);
    const first=nodes[0],last=nodes.at(-1);
    if(e.shiftKey&&document.activeElement===first){e.preventDefault();last?.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first?.focus();}
  }
});
buildNow.wide.addEventListener('change',()=>{if(buildNow.open)openDrawer(false);renderSide();});
