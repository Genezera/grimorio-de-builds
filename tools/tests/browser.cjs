/* Run with Node and Playwright. Uses an ephemeral local HTTP server, no build network. */
const { chromium } = require('playwright');
const fs=require('node:fs'), path=require('node:path'), http=require('node:http'), assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../..');
const server=http.createServer((req,res)=>{
  const rel=decodeURIComponent(new URL(req.url,'http://localhost').pathname),file=path.resolve(root,'.'+rel+(rel.endsWith('/')?'index.html':''));
  if(!file.startsWith(root+path.sep)){res.writeHead(403).end();return;}
  fs.readFile(file,(err,data)=>{if(err){res.writeHead(404).end();return;}res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript'})[path.extname(file)]||'application/octet-stream');res.end(data);});
});
(async()=>{
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=`http://127.0.0.1:${server.address().port}`,browser=await chromium.launch({headless:true,...(process.env.BROWSER_CHANNEL?{channel:process.env.BROWSER_CHANNEL}:{})});
  let pages=0,tabs=0,recipes=0;const errors=[],overflow=[];
  try{
    for(const width of [1366,1024,768,390]){
      const context=await browser.newContext({viewport:{width,height:1000},reducedMotion:'reduce'}),page=await context.newPage();
      page.on('pageerror',e=>errors.push(page.url()+': '+e.message));
      page.on('response',r=>{if(r.url().startsWith(base+'/')&&r.status()>=400)errors.push(`${r.status()} ${r.url()}`);});
      await page.route('https://fonts.googleapis.com/**',route=>route.abort());
      await page.route('https://fonts.gstatic.com/**',route=>route.abort());
      for(const file of ['index.html','en.html',...['silverfist','oracle','tactician','infernalist','acolyte','pathfinder','smith','martial'].flatMap(b=>[b+'/index.html',b+'/en.html'])]){
        await page.goto(base+'/'+file);await page.waitForLoadState('domcontentloaded');pages++;
        if(!file.includes('/')){
          assert.equal(await page.locator('.build').count(),8);
          assert.equal(await page.locator('.primary').count(),8);
        }else{
          assert.equal(await page.locator('#navGroups button').count(),4);
          const ids=await page.locator('#tabs button').evaluateAll(xs=>xs.map(x=>x.dataset.tab));
          for(const id of ids){
            const group=await page.evaluate(id=>guideGroup(id),id);
            await page.locator(`[data-group="${group}"]`).click();await page.locator(`[data-tab="${id}"]`).click();
            assert.equal(await page.locator(`#v-${id}`).isVisible(),true,file+' '+id);
            assert.ok((await page.locator(`#v-${id}`).innerText()).length>30,file+' empty '+id);
            if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2))overflow.push(`${width} ${file} #${id}`);
            tabs++;
          }
          // Search really returns content matches, including accent-independent queries.
          await page.locator('#guideSearch').fill('Spirit');
          assert.ok(await page.locator('[data-search-go]').count()>0);
          await page.locator('[data-search-go]').first().click();
          assert.equal(await page.locator('#guideResults').isVisible(),false);
          await page.locator('#guideSearch').fill('zzzzzznonsense');
          assert.equal(await page.locator('[data-search-go]').count(),0);
          await page.keyboard.press('Escape');
          await page.locator('[data-group="1"]').click();await page.locator('[data-tab="craft"]').click();
          await page.locator('[data-cview="recipes"]').click();
          for(const id of await page.locator('[data-citem]').evaluateAll(xs=>xs.map(x=>x.dataset.citem))){
            await page.locator(`[data-citem="${id}"]`).click();
            for(const route of ['cheap','value','lux']){await page.locator('#craftRoute').selectOption(route);assert.ok(await page.locator('.craft-step').count()>=3);recipes++;}
          }
          await page.locator('[data-citem="amulet"]').click();
          await page.locator('#craftIlvl').fill('1');await page.locator('#craftIlvl').press('Tab');
          assert.ok(await page.locator('.craft-mods tr.locked').count()>0);
          await page.locator('#craftIlvl').fill('82');await page.locator('#craftIlvl').press('Tab');
          await page.locator('[data-cstep]').first().check();await page.reload();
          assert.equal(await page.locator('[data-cstep]').first().isChecked(),true);
          await page.locator('[data-cview="basics"]').click();assert.equal(await page.locator('.craft-glossary article').count(),12);
          await page.locator('[data-cview="calculator"]').click();
          await page.locator('#weightExplorer summary').click();
          assert.equal(await page.locator('[data-use-weight]').count(),0);
          await page.locator('#cw-consent').check();
          assert.equal(await page.locator('[data-use-weight]').count(),1);
          await page.locator('[data-use-weight]').click();
          assert.ok(Number(await page.locator('#cc-p').inputValue())>0);
          await page.locator('#cw-prefix').fill('0');await page.locator('#cw-prefix').press('Tab');await page.locator('#cw-suffix').fill('0');await page.locator('#cw-suffix').press('Tab');
          assert.equal(await page.locator('[data-use-weight]').count(),0,file+' weight after prefix 0');
          const model=await page.evaluate(()=>craftPublishedChance([
            {kind:'normal',name:'a',text:'mana',level:75,gen:'Prefix',family:'mana',weight:1},
            {kind:'normal',name:'b',text:'life',level:75,gen:'Prefix',family:'life',weight:9}
          ],{ilvl:80,floor:50,side:'Prefix',prefix:1,suffix:0,blocked:[],target:{name:'a',text:'mana',level:75,gen:'Prefix'}}));
          assert.equal(model.p,.1);assert.equal(model.unknown,1);
          for(const [k,v] of Object.entries({p:'5',cost:'2',budget:'100',base:'0'}))await page.locator('#cc-'+k).fill(v);
          const result=await page.evaluate(()=>craftStatistics({p:.05,cost:2,budget:100,base:0}));
          assert.equal(result.meanCost,40);assert.equal(result.n90,45);assert.ok(Math.abs(result.success-.9230550247)<1e-9);
          assert.equal(await page.evaluate(()=>craftStatistics({p:0,cost:2,budget:100})),null);
          assert.equal(await page.evaluate(()=>craftStatistics({p:1,cost:2,budget:1}).success),0);
          assert.equal(await page.evaluate(()=>craftStatistics({p:1,cost:2,budget:2}).success),1);
          assert.equal(await page.evaluate(()=>craftStatistics({p:.5,cost:2,budget:1,base:5}).attempts),0);
          await page.locator('#cc-p').fill('0');assert.equal(await page.locator('.calc-results').count(),0);
          await page.locator('[data-cview="recipes"]').click();
          // Roving tab index and arrow navigation.
          await page.locator('[data-tab="craft"]').focus();await page.keyboard.press('ArrowRight');
          assert.equal(await page.locator('#tabs [role="tab"][aria-selected="true"]').count(),1);
          await page.locator('[data-tab="craft"]').click();
        }
        if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2))overflow.push(`${width} ${file}`);
        if(process.env.SCREENSHOT_DIR){fs.mkdirSync(process.env.SCREENSHOT_DIR,{recursive:true});await page.screenshot({path:path.join(process.env.SCREENSHOT_DIR,`${file.replace('/','-')}-${width}.png`),fullPage:false});}
      }
      // Language switch preserves deep link and build-specific crafting progress.
      await page.goto(base+'/oracle/index.html#craft');await page.locator('[data-cview="recipes"]').click();await page.locator('[data-cstep]').first().check();
      await page.locator('.langsw a[hreflang="en"]').click();
      assert.equal(new URL(page.url()).hash,'#craft');assert.equal(await page.locator('[data-cstep]').first().isChecked(),true);
      await page.goto(base+'/oracle/index.html#missing-tab');assert.equal(await page.locator('.view.on').count(),1);
      await context.close();
    }
    // Challenge progress and planner costs are independent of the build guides.
    for(const lang of ['pt','en']){
      const context=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'reduce'});
      const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
      await page.goto(base+'/rites/'+(lang==='pt'?'index.html':'en.html'));pages++;
      assert.equal(await page.locator('.chlist > section').count(),8);
      await page.locator('details.rite').first().locator('summary').click();
      await page.locator('[data-rite]').first().click();
      assert.equal(await page.locator('details.rite.ok').count(),1);
      await page.locator('[data-num="level"]').fill('90');await page.locator('[data-num="level"]').press('Tab');
      assert.equal(await page.locator('#master.complete').count(),1);
      await page.reload();assert.equal(await page.locator('#master.complete').count(),1);
      await page.locator('.lang a').filter({hasText:lang==='pt'?'EN':'PT'}).click();
      assert.equal(await page.locator('#master.complete').count(),1);
      // Missing omen OR activation currency must never count as free.
      await page.evaluate(()=>{RITES.omens.forEach(o=>o.price=null);document.querySelector('[data-flag="hc"]').click();});
      assert.equal(await page.locator('.omens tr.plan').count(),0);
      assert.equal(await page.locator('.plan-head [role="status"]').count(),1);
      assert.ok((await page.locator('.omens td.num').allTextContents()).every(t=>t==='—'));
      await page.evaluate(()=>{RITES.omens.forEach(o=>{o.price=1;o.trigPrice=o.trig?null:0;});document.querySelector('[data-flag="nolow"]').click();});
      assert.equal(await page.locator('.omens tr.plan small').count(),0);
      if(process.env.SCREENSHOT_DIR)await page.screenshot({path:path.join(process.env.SCREENSHOT_DIR,`rites-${lang}-390.png`),fullPage:false});
      await context.close();
    }
    for(const width of [320,1920]){
      const page=await browser.newPage({viewport:{width,height:1000},reducedMotion:'reduce'});
      page.on('pageerror',e=>errors.push(e.message));
      for(const build of ['silverfist','oracle','tactician','infernalist','acolyte','pathfinder','smith','martial']){
        await page.goto(base+'/'+build+'/en.html');await page.evaluate(()=>setLv(95));pages++;
        for(const id of await page.evaluate(()=>TABS.map(x=>x[0]))){
          await page.evaluate(id=>guideGo(id),id);
          if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2))overflow.push(`${width} ${build} #${id}`);
          tabs++;
        }
        if(build==='oracle')assert.equal(await page.evaluate(()=>qStatus(D.timing.find(x=>x.n==='Archmage amulet')).t),'Check the requirement on the item');
      }
      await page.close();
    }
    assert.deepEqual(errors,[],'Browser runtime errors');assert.deepEqual(overflow,[],'Horizontal page overflow');
    console.log(JSON.stringify({pages,tabViews:tabs,recipeRoutes:recipes,runtimeErrors:errors.length,horizontalOverflow:overflow.length,checks:'search, deep links, keyboard, persistence, PT/EN, ilvl, weight opt-in, blocked slots, calculator boundaries, level 95 at 320px/1920px'},null,2));
  }finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
})().catch(error=>{console.error(error);process.exitCode=1;server.close();});
