# Troca a fonte de níveis exigidos (poe.ninja -> Path of Building) e corrige os textos que dependiam do número errado.
s = open("timing.py", encoding="utf-8").read()

start = s.index("def _levels():"); end = s.index("LV = _levels()")
NEW_LEVELS = r'''def _levels():
    """Nível exigido por unique, do Path of Building (PoE2): linha 'Requires Level' do unique ou, sem ela, o requisito do tipo base.
    (O campo levelRequired do poe.ninja NÃO é confiável: dizia 78 para o Sylvan's Effigy, que no jogo pede 62.)"""
    import re
    bases = {}
    for f in glob.glob("dl/pob/pob_*.lua"):
        for m in re.finditer(r'itemBases\["([^"]+)"\] = \{(.*?)\n\}', open(f, encoding="utf-8").read(), re.S):
            r = re.search(r"req = \{[^}]*level = (\d+)", m.group(2)); bases[m.group(1)] = int(r.group(1)) if r else 1
    out = {}
    for f in glob.glob("dl/pob/pobu_*.lua"):
        for blk in re.findall(r"\[\[(.*?)\]\]", open(f, encoding="utf-8").read(), re.S):
            lines = [l.strip() for l in blk.strip().splitlines() if l.strip()]
            if len(lines) < 2: continue
            name, base = lines[0], lines[1]
            rq = next((int(re.search(r"\d+", l).group()) for l in lines if l.startswith("Requires Level")), None)
            if name not in out:
                out[name] = {"base": rq or bases.get(base), "src": "unique" if rq else "base", "type": base}
    return out

'''
s = s[:start] + NEW_LEVELS + s[end:]

def rep(a, b):
    global s
    assert a in s, "NOT FOUND: " + a[:80]
    s = s.replace(a, b)

rep('''    d = LV.get(name, {})
    b, r = d.get("base"), d.get("rf")
    pt = f"Nível {b}" if b else "Sem requisito de nível"
    en = f"Level {b}" if b else "No level requirement"
    if r and r != b:
        pt += f" · Runeforged/Runemastered: nível {r}"; en += f" · Runeforged/Runemastered: level {r}"''',
'''    d = LV.get(name, {})
    b = d.get("base")
    pt = f"Nível {b}" if b else "Sem requisito de nível"
    en = f"Level {b}" if b else "No level requirement"
    if b and d.get("src") == "base":
        pt += " (do tipo base — confira no item)"; en += " (from the base type — check the item)"''')

rep('''(LV.get("Sylvan's Effigy") or {}).get("base") or 78''', '''(LV.get("Sylvan's Effigy") or {}).get("base") or 62''')
rep('''("Nível 78, na fase T15+. Substitui o Rattling Sceptre.", "Level 78, in the T15+ phase. Replaces the Rattling Sceptre.")''',
    '''("A partir do nível 62 (requisito do item). Entra assim que você conseguir — normalmente no início do Atlas. Substitui o Rattling Sceptre.", "From level 62 (item requirement). Put it on as soon as you get it — usually early Atlas. Replaces the Rattling Sceptre.")''')

i = s.index('("Conseguiu antes do nível 78?'); j = s.index('    [("Tire o Rattling Sceptre')
s = s[:i] + '''("Conseguiu antes do nível 62? Guarde até o 62. Já está no 62+? Equipe agora. Antes de trocar, deixe prontos: (1) beasts de aura de tipos diferentes capturados — Haste (Quill/Coconut Crab) e Physical (Swarming Wisp / Plague Swarm); (2) Primate Idol + Rabbit Idol para os sockets; (3) um Skeletal Cleric para ser o alvo do Pain Offering, porque a gem Skeletal Warrior sai junto com o Rattling Sceptre.",
     "Got it before level 62? Keep it until 62. Already 62+? Equip it now. Before swapping, have ready: (1) captured aura beasts of different types — Haste (Quill/Coconut Crab) and Physical (Swarming Wisp / Plague Swarm); (2) Primate Idol + Rabbit Idol for the sockets; (3) a Skeletal Cleric to be the Pain Offering target, because the Skeletal Warrior gem leaves with the Rattling Sceptre."),
    ("Ainda não tem? A rota continua funcionando com Rattling Sceptre e 2 companions. O Effigy é o maior upgrade de Spirit e de companions: priorize antes de Idolatry e de itens de luxo.",
     "Don't have it yet? The route still works with Rattling Sceptre and 2 companions. The Effigy is the biggest Spirit and companion upgrade: prioritize it over Idolatry and luxury items."),
''' + s[j:]

rep(' Atenção: a versão Runeforged pede nível 55; a normal pede 33.', '')
rep(' Note: the Runeforged version needs level 55; the normal one needs 33.', '')
rep('("Ato 3–4 até o nível 78.", "Acts 3–4 until level 78.")', '("Ato 3 até trocar pela Forgotten Warden.", "Act 3 until you swap to Forgotten Warden.")')
rep('''("Ao trocar pela Forgotten Warden (nível 78), você perde +100 Spirit: faça a troca junto com o Sylvan's Effigy (increased Spirit) e confira o painel.", "When swapping to Forgotten Warden (level 78) you lose +100 Spirit: do it together with Sylvan's Effigy (increased Spirit) and check the panel.")''',
    '''("Ao trocar pela Forgotten Warden você perde +100 Spirit: faça a troca depois do Sylvan's Effigy (increased Spirit) e confira o painel.", "When swapping to Forgotten Warden you lose +100 Spirit: do it after Sylvan's Effigy (increased Spirit) and check the panel.")''')
rep('''(LV.get("Forgotten Warden") or {}).get("base") or 78''', '''(LV.get("Forgotten Warden") or {}).get("base") or 70''')
rep('''("Nível 78, junto com o Sylvan's Effigy.", "Level 78, together with Sylvan's Effigy.")''',
    '''("Depois do Sylvan's Effigy, quando o requisito do item permitir.", "After Sylvan's Effigy, once the item's requirement allows.")''')
rep('Pelo guia, dá o Spirit Vessel.', 'Concede a skill Spirit Vessel.')
rep('Per the guide it grants Spirit Vessel.', 'Grants the Spirit Vessel skill.')
rep('''("Antes do 78 não dá para equipar: guarde e siga com Enfolding Dawn.", "Before level 78 you can't equip it: keep it and stay on Enfolding Dawn.")''',
    '''("Se o requisito do item for maior que o seu nível, guarde e siga com Enfolding Dawn.", "If the item's requirement is above your level, keep it and stay on Enfolding Dawn.")''')
rep('add("skill", "Azmerian Wolf", 78,', 'add("skill", "Azmerian Wolf", 62,')
rep('("Junto com o Effigy (nível 78).", "Together with the Effigy (level 78).")', '("Junto com o Effigy (nível 62).", "Together with the Effigy (level 62).")')
rep(' (e o da versão Runeforged, que costuma ser maior)', '')
rep(" (and the Runeforged version's, usually higher)", '')

i = s.index(' (("Comprei a versão Runeforged'); j = s.index(" ((\"Tenho o Effigy mas não tenho Giant")
s = s[:i] + s[j:]

i = s.index('  ("Normal. Selecione'); j = s.index(' (("Consegui um item antes do nível exigido"')
s = s[:i] + '''  ("Normal. Selecione 'Início do Atlas' em 'Onde você está' no topo: o guia passa a mostrar a fase do Atlas, e a árvore continua usando os pontos do seu nível. Já dá para usar: The Catha's Balance (3º Trial em área 60+), Chober Chaber, The Vertex, Evergrasping Ring e o Sylvan's Effigy (nível 62). Se tiver o Effigy, siga o cartão dele: tire o Rattling Sceptre, use Skeletal Cleric no Pain Offering e ative mais beasts de aura conforme o Spirit.",
   "Normal. Pick 'Early Atlas' in 'Where are you' at the top: the guide switches to the Atlas phase and the tree keeps using your level's points. Already usable: The Catha's Balance (3rd Trial in area 60+), Chober Chaber, The Vertex, Evergrasping Ring and Sylvan's Effigy (level 62). If you have the Effigy, follow its card: remove the Rattling Sceptre, use Skeletal Cleric for Pain Offering and activate more aura beasts as Spirit allows.")),
''' + s[j:]

rep('''def unique_levels(UNIQUES):
    """Corrige o nível exigido dos uniques com o dado real do item."""
    for u in UNIQUES:
        d = LV.get(u["n"])
        if d and d.get("base"):
            u["lvl"] = d["base"]
            if d.get("rf") and d["rf"] != d["base"]:
                u["lvlRf"] = d["rf"]''',
'''def unique_levels(UNIQUES):
    """Nível exigido dos uniques pelo Path of Building (ver _levels)."""
    for u in UNIQUES:
        u.pop("lvlRf", None)
        d = LV.get(u["n"])
        if d and d.get("base"):
            u["lvl"] = d["base"]; u["lvlSrc"] = d["src"]''')
open("timing.py", "w", encoding="utf-8").write(s)
print("ok")
