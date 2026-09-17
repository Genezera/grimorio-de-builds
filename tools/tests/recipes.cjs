/* Recipe ordering: no ordinary crafting step may follow optional corruption. */
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
let checked=0;
for(const lang of ['pt','en']){
  const ctx={window:{},T:(pt,en)=>lang==='pt'?pt:en};vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(path.join(__dirname,'../../shared/craft-detail.js'),'utf8'),ctx);
  for(const oracle of [false,true])for(const [item,recipe] of Object.entries(ctx.window.craftDetail(oracle))){
    for(const route of ['cheap','value','lux']){
      const steps=recipe[route];assert.ok(steps?.length,`${item} ${route}`);
      const corrupt=steps.findIndex(s=>/considere Vaal|consider Vaal/.test(s.d));
      if(corrupt>=0)assert.equal(corrupt,steps.length-1,`${lang} ${oracle} ${item} ${route}: crafting follows corruption`);
      checked++;
    }
  }
}
console.log(`${checked} localized recipe routes: final corruption ordering OK`);
