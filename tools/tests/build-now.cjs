const {chromium}=require('playwright');
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../..');
const server=http.createServer((req,res)=>{const file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://local').pathname));if(!file.startsWith(root+path.sep))return res.writeHead(403).end();fs.readFile(file,(err,data)=>{if(err)return res.writeHead(404).end();res.setHeader('Content-Type',({'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css'})[path.extname(file)]||'application/octet-stream');res.end(data);});});
const openFab=async page=>{await page.evaluate(()=>{const c=document.querySelector('.console');scrollTo(0,c?c.getBoundingClientRect().bottom+scrollY+40:0);dispatchEvent(new Event('scroll'));});await page.waitForFunction(()=>!document.getElementById('sbFab').classList.contains('sb-fab-away'));await page.locator('#sbFab').click();};
(async()=>{
 await new Promise(r=>server.listen(0,'127.0.0.1',r));
 const base=`http://127.0.0.1:${server.address().port}`,errors=[];
 const browser=await chromium.launch({headless:true,...(process.env.BROWSER_CHANNEL?{channel:process.env.BROWSER_CHANNEL}:{})});let checks=0;
 try{
  const sizes=(process.env.SIZES||'320x568,375x812,540x720,768x1024,1024x768,844x390,1439x900,1440x900,1920x1080,2560x1440').split(',').map(v=>v.split('x').map(Number));
  for(const [width,height] of sizes){
   const context=await browser.newContext({viewport:{width,height},reducedMotion:'reduce'}),page=await context.newPage();
   page.on('pageerror',e=>errors.push(e.message));await page.route(/fonts\.(googleapis|gstatic)\.com/,r=>r.abort());
   for(const file of ['silverfist','oracle','tactician','infernalist','acolyte','pathfinder','smith','martial','shaman','legionnaire','whirling','twister'].flatMap(b=>[b+'/index.html',b+'/en.html'])){
    await page.goto(base+'/'+file);await page.evaluate(()=>{buildNow.collapsed=false;renderSide();});
    if(width<1440){await openFab(page);assert.equal(await page.locator('#side').getAttribute('aria-modal'),'true');assert.ok(await page.locator('main').evaluate(el=>el.inert));}
    for(const level of [1,35,70,95]){
     await page.evaluate(lv=>{S.mode=lv<50?'cheap':'full';setLv(lv);},level);
     for(const tab of ['now','gear','skills']){
      await page.locator(`[data-bn-tab="${tab}"]`).click();
      assert.ok((await page.locator('#bn-content').innerText()).length>50);
      const issues=await page.evaluate(()=>{
       const out=[],side=document.getElementById('side'),r=side.getBoundingClientRect();
       if(r.left<-.5||r.right>innerWidth+.5||r.bottom>innerHeight+1)out.push('panel outside viewport');
       for(const el of side.querySelectorAll('.bn-scroll,.bn-item,.bn-priority,.bn-supports,.bn-phase,.bn-tabs'))if(el.scrollWidth>el.clientWidth+1)out.push(el.className+' overflows');
       if(document.documentElement.scrollWidth>innerWidth+1)out.push('page overflows');
       const scroll=side.querySelector('.bn-scroll');if(scroll.clientHeight<80)out.push('scroll area too short');
       scroll.scrollTop=scroll.scrollHeight;
       const last=scroll.querySelector('.bn-content').lastElementChild.getBoundingClientRect();if(last.bottom>scroll.getBoundingClientRect().bottom+1)out.push('last action cannot be reached');
       return out;
      });assert.deepEqual(issues,[],`${file} ${width} ${level} ${tab}`);checks++;
     }
    }
    await page.locator('[data-bn-tab="now"]').click();await page.keyboard.press('ArrowRight');assert.equal(await page.locator('#bn-tab-gear').getAttribute('aria-selected'),'true');
    if(process.env.SCREENSHOT_DIR&&['silverfist/index.html','oracle/index.html'].includes(file)&&[375,768,1440].includes(width)){
     fs.mkdirSync(process.env.SCREENSHOT_DIR,{recursive:true});await page.locator('.bn-scroll').evaluate(el=>el.scrollTop=0);await page.locator('#side').screenshot({path:path.join(process.env.SCREENSHOT_DIR,`${file.split('/')[0]}-${width}-gear.png`)});
     await page.locator('[data-bn-tab="now"]').click();await page.locator('#side').screenshot({path:path.join(process.env.SCREENSHOT_DIR,`${file.split('/')[0]}-${width}-now.png`)});
    }
    if(width<1440){
     await page.locator('[data-bn-toggle]').focus();await page.keyboard.press('Shift+Tab');assert.ok(await page.evaluate(()=>document.activeElement.closest('#side')!==null));
     await page.keyboard.press('Escape');assert.equal(await page.locator('#sbFab').getAttribute('aria-expanded'),'false');assert.equal(await page.locator('main').evaluate(el=>el.inert),false);assert.equal(await page.locator('#sbFab').evaluate(el=>el===document.activeElement),true);
     await openFab(page);await page.locator('[data-bn-tab="gear"]').click();await page.locator('[data-bn-go="gear"]').last().click();assert.equal(await page.locator('#v-gear').isVisible(),true);assert.equal(await page.locator('#side').isVisible(),false);
    }else{await page.locator('[data-bn-toggle]').click();assert.equal(await page.locator('.bn-expand').count(),1);await page.locator('[data-bn-toggle]').click();assert.equal(await page.locator('.bn-tabs').count(),1);}
   }
   await context.close();console.log(`${width}x${height}: passed`);
  }
  // Open mobile -> resize desktop -> resize mobile must not leave a modal lock.
  const page=await browser.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});page.on('pageerror',e=>errors.push(e.message));
  await page.goto(base+'/oracle/index.html');await openFab(page);await page.setViewportSize({width:1500,height:900});await page.waitForFunction(()=>!buildNow.open);assert.equal(await page.locator('main').evaluate(el=>el.inert),false);
  await page.setViewportSize({width:390,height:844});await openFab(page);await page.locator('[data-bn-tab="skills"]').click();await page.keyboard.press('Escape');await page.reload();await openFab(page);assert.equal(await page.locator('#bn-tab-skills').getAttribute('aria-selected'),'true');
  await page.evaluate(()=>setLv(1));await page.locator('[data-bn-tab="now"]').click();
  const milestone=page.locator('[data-bn-check]').first(),key=await milestone.getAttribute('data-bn-check');await milestone.check();
  await page.reload();assert.equal(await page.evaluate(k=>S.done[k],key),true);
  await page.emulateMedia({reducedMotion:'no-preference'});await openFab(page);
  assert.equal(await page.locator('#side').evaluate(el=>getComputedStyle(el).animationName),'bn-enter');
  await page.emulateMedia({reducedMotion:'reduce'});assert.equal(await page.locator('#side').evaluate(el=>getComputedStyle(el).animationName),'none');
  await page.close();assert.deepEqual(errors,[]);console.log(JSON.stringify({panelStates:checks,runtimeErrors:errors.length}));
 }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);process.exitCode=1;server.close();});
