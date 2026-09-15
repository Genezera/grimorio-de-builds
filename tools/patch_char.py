# Injeta a aba "Meu personagem" (char.js) no template.
t = open("app_template.html", encoding="utf-8").read()

def rep(old, new):
    global t
    assert old in t, "NOT FOUND: " + old[:80]
    t = t.replace(old, new, 1)

if "function vMeu" not in t:
    rep("const D = __DATA__;", 'const LANG = "__LANG__";\nconst D = __DATA__;')
    rep('<section class="view" id="v-agora"></section>', '<section class="view" id="v-agora"></section>\n    <section class="view" id="v-meu"></section>')
    rep('const TABS = [["agora","Agora"],', 'const TABS = [["agora","Agora"],["meu","Meu personagem"],')
    rep("const VIEWS = { meta: vMeta,", "const VIEWS = { meu: vMeu, meta: vMeta,")
    rep("/* ------------------------------------------------ events */", open("char.js", encoding="utf-8").read() + "\n/* ------------------------------------------------ events */")
    # painel lateral: recomendações no topo
    rep("""      ${sideSec("steps", "Próximos passos",""", """      ${(() => { const rr = charRecs().recs.filter(x => x.lvl !== "ok").slice(0, 4); if (S.sideOpen.recs === undefined) S.sideOpen.recs = true; return sideSec("recs", T("Para você agora", "For you now"), rr.length, (rr.length ? rr.map(x => `<div class="rec ${x.lvl} mini" data-gotab="${x.tab && x.tab !== "meu" ? x.tab : "meu"}"><span class="ri">${{ bad: "✖", warn: "!", tip: "➜", ok: "✔" }[x.lvl]}</span><div><b>${esc(x.t)}</b></div></div>`).join("") : `<span class="label">${T("Nada pendente pelo que você marcou.", "Nothing pending from what you ticked.")}</span>`) + `<button class="btn" type="button" data-gotab="meu">${T("Marcar o que eu tenho", "Tick what I have")}</button>`); })()}
      ${sideSec("steps", "Próximos passos",""")
    rep(".spnote{", """.charwrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:16px;align-items:start;margin-top:16px}
@media (max-width:1100px){.charwrap{grid-template-columns:1fr}}
.recs{position:sticky;top:12px;display:grid;gap:8px}
.rec{display:grid;grid-template-columns:28px 1fr;gap:10px;align-items:start;padding:9px 10px;border:1px solid var(--edge);background:#0f0c0a;cursor:pointer}
.rec .ri{display:grid;place-items:center;width:24px;height:24px;border-radius:50%;font-weight:900;font-family:var(--ui);font-size:.8rem}
.rec b{display:block;font-family:var(--ui);color:var(--text);font-size:.95rem;line-height:1.2}
.rec small{display:block;color:var(--mute);font-size:.84rem;margin-top:3px;line-height:1.3}
.rec.bad{border-color:rgba(224,102,79,.55)}.rec.bad .ri{background:#5a1d14;color:#ffb3a3}
.rec.warn{border-color:#7a6440}.rec.warn .ri{background:#4a3a1c;color:var(--gild-hi)}
.rec.tip{border-color:#2f5b6c}.rec.tip .ri{background:#15323d;color:#9fd2ff}
.rec.ok{opacity:.8}.rec.ok .ri{background:#15342a;color:#8fd9b8}
.rec.mini{padding:6px 8px;grid-template-columns:22px 1fr}.rec.mini .ri{width:20px;height:20px;font-size:.7rem}.rec.mini b{font-size:.84rem}
.chkgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:6px}
.chk{display:flex;align-items:center;gap:8px;padding:5px 8px;border:1px solid var(--edge);cursor:pointer;font-family:var(--ui);font-size:.88rem;color:var(--text)}
.chk:has(input:checked){border-color:#8a6a38;background:rgba(200,165,106,.08)}
.chk input{accent-color:#c8a56a}
.chk img{width:26px;height:26px;object-fit:contain}
.chk .px{margin-left:auto;font-family:var(--mono);font-size:.7rem;color:var(--gild)}
.petrow{display:grid;grid-template-columns:auto minmax(0,1.4fr) minmax(0,1fr) auto;gap:8px;align-items:center;margin-bottom:8px}
@media (max-width:600px){.petrow{grid-template-columns:1fr 1fr}}
.petrow .px{font-family:var(--mono);font-size:.76rem;color:var(--gild);white-space:nowrap}
.charstat{margin-top:6px}
.spnote{""")
open("app_template.html", "w", encoding="utf-8").write(t)
print("ok")
