/* A deliberately opt-in published-weight model; no catalyst or reveal claims. */
function craftWeightExplorer(){
  const r=craftRecipes().find(x=>x.id===S.craft.item),magic=/Flasks|Charms/.test(r.page);
  if(magic)return `<div class="craft-note">${T('Selecione um equipamento Rare para explorar pesos de Exalted. Para frascos e charms, informe uma hipótese no simulador abaixo.','Select Rare equipment to explore Exalted weights. For flasks and charms, enter an assumption in the simulator below.')}</div>`;
  const targets=craftTargets(r),families=[...new Set((CF.pools[r.page]||[]).filter(m=>m.kind==='normal').map(m=>m.family))].sort();
  return `<details class="panel frame" style="margin-bottom:20px" id="weightExplorer"><summary>${T('Não sabe a chance? Explore os pesos publicados','Unsure of the probability? Explore published weights')} · ${esc(r.name)}</summary><p class="craft-lead">${T('Modelo condicional para adicionar um mod Rare à classe selecionada. Inclui pesos 1, mas o significado desses pesos não foi validado. Não simula remoção por Chaos, catalysts, Genesis, Desecration nem exceções de bases especiais.','Conditional model for adding one Rare modifier to the selected class. Includes weight-1 entries, whose meaning has not been validated. Does not simulate Chaos removal, catalysts, Genesis, Desecration or special-base exceptions.')}</p>
  <div class="calc-form"><label>${T('Mod alvo exato','Exact target modifier')}<select id="cw-target">${targets.map((m,i)=>`<option value="${i}">${esc(m.text)} · ilvl ${m.level}</option>`).join('')}</select></label><label>ilvl<input id="cw-ilvl" type="number" min="1" max="100" step="1" value="${S.craft.ilvl}"></label>
  <label>${T('Currency de adição','Adding currency')}<select id="cw-floor"><option value="0">Exalted Orb</option><option value="35">Greater Exalted Orb</option><option value="50">Perfect Exalted Orb</option></select></label><label>${T('Lado forçado por omen','Side forced by omen')}<select id="cw-side"><option value="">${T('Nenhum','None')}</option><option value="Prefix">Sinistral · ${T('prefixo','prefix')}</option><option value="Suffix">Dextral · ${T('sufixo','suffix')}</option></select></label>
  <label>${T('Prefixos livres','Open prefixes')}<input id="cw-prefix" type="number" min="0" max="3" step="1" value="1"></label><label>${T('Sufixos livres','Open suffixes')}<input id="cw-suffix" type="number" min="0" max="3" step="1" value="1"></label>
  <label style="grid-column:1/-1">${T('Famílias já no item (Ctrl/Cmd para múltiplas)','Families already on the item (Ctrl/Cmd for multiple)')}<select id="cw-blocked" multiple size="4">${families.map(f=>`<option>${esc(f)}</option>`).join('')}</select></label></div>
  <label class="craft-note" style="display:flex;gap:12px;align-items:start"><input type="checkbox" id="cw-consent" style="margin-top:6px;accent-color:var(--gild)"><span>${T('Simular como se os pesos publicados fossem corretos e o pool completo para a minha base. Entendo que o número é uma hipótese, não uma chance validada do jogo.','Simulate as if the published weights were correct and the pool complete for my base. I understand the number is an assumption, not a validated in-game probability.')}</span></label><div id="weightResult" aria-live="polite"></div></details>`;
}
function craftPublishedChance(rows,{ilvl,floor,side,prefix,suffix,blocked,target}){
  if(!Number.isInteger(ilvl)||ilvl<1||ilvl>100||![prefix,suffix].every(n=>Number.isInteger(n)&&n>=0&&n<=3))return null;
  const sides=[...(prefix>0?['Prefix']:[]),...(suffix>0?['Suffix']:[])].filter(s=>!side||s===side);
  const pool=rows.filter(m=>m.kind==='normal'&&m.weight>0&&m.level<=ilvl&&m.level>=floor&&sides.includes(m.gen)&&!blocked.includes(m.family));
  const total=pool.reduce((n,m)=>n+m.weight,0),hit=pool.filter(m=>m.name===target?.name&&m.text===target?.text&&m.level===target?.level&&m.gen===target?.gen).reduce((n,m)=>n+m.weight,0);
  return {p:total?hit/total:0,total,hit,entries:pool.length,unknown:pool.filter(m=>m.weight===1).length};
}
let craftLastWeight=null;
function craftUpdateWeights(){
  const box=$('#weightResult');if(!box)return;
  craftLastWeight=null;
  if(!$('#cw-consent').checked){box.innerHTML=`<p class="craft-lead">${T('Escolha o alvo e descreva os espaços e famílias do item. Ative a hipótese acima para calcular.','Choose a target and describe the item’s slots and families. Enable the assumption above to calculate.')}</p>`;return;}
  const r=craftRecipes().find(x=>x.id===S.craft.item),targets=craftTargets(r),result=craftPublishedChance(CF.pools[r.page],{ilvl:Number($('#cw-ilvl').value),floor:Number($('#cw-floor').value),side:$('#cw-side').value,prefix:Number($('#cw-prefix').value),suffix:Number($('#cw-suffix').value),blocked:[...$('#cw-blocked').selectedOptions].map(o=>o.value),target:targets[Number($('#cw-target').value)]});
  if(!result){box.textContent=T('Use ilvl inteiro de 1 a 100 e espaços livres inteiros de 0 a 3.','Use integer item level from 1 to 100 and integer open slots from 0 to 3.');return;}
  const percent=(result.p*100).toLocaleString(LANG==='pt'?'pt-BR':'en-US',{maximumFractionDigits:5});
  craftLastWeight=result.p;
  box.innerHTML=`<div class="craft-note"><b>${T('Chance no modelo','Model probability')}: ${percent}%</b><br>${result.hit} / ${result.total} ${T('de peso elegível','eligible weight')} · ${result.entries} ${T('linhas','rows')} · ${result.unknown} ${T('linhas com peso 1 não validado','rows with unvalidated weight 1')}. ${result.p===0?T('O alvo não está disponível neste estado do modelo.','The target is unavailable in this model state.'):''}</div>${result.p>0?`<button class="guide-btn" type="button" data-use-weight>${T('Usar esta hipótese no simulador','Use this assumption in the simulator')} ↓</button>`:''}`;
}
document.addEventListener('change',e=>{if(e.target.id.startsWith('cw-'))craftUpdateWeights();});
document.addEventListener('click',e=>{if(e.target.closest('[data-use-weight]')&&craftLastWeight>0){craftCalc.p=String(craftLastWeight*100);store.set('craftCalc',craftCalc);$('#cc-p').value=craftCalc.p;craftUpdateCalculator();$('#cc-p').focus();}});
