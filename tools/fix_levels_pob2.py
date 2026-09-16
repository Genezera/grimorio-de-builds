# Segunda parte: remove números de nível herdados do poe.ninja nos textos e ajusta o que dependia do Effigy no 78.
s = open("timing.py", encoding="utf-8").read()
def rep(a, b):
    global s
    assert a in s, "NOT FOUND: " + a[:80]
    s = s.replace(a, b)
rep("Pelo guia do Mattjestic, traz as skills Azmerian Wolf e Discipline.", "Concede as skills Discipline e Azmerian Wolf.")
rep("Per Mattjestic's guide it grants the Azmerian Wolf and Discipline skills.", "Grants the Discipline and Azmerian Wolf skills.")
rep('''    pt = f"Nível {b}" if b else "Sem requisito de nível"
    en = f"Level {b}" if b else "No level requirement"''', '''    pt = f"Nível {b}" if b else "Requisito não confirmado — confira no item"
    en = f"Level {b}" if b else "Requirement not confirmed — check the item"''')
rep('add("item", "Spiteful Floret", (LV.get("Spiteful Floret") or {}).get("base") or 52,', 'add("item", "Spiteful Floret", (LV.get("Spiteful Floret") or {}).get("base") or 1,')
rep('("Pode colocar no weapon set 2 a partir do nível 52.", "Can go in weapon set 2 from level 52.")', '("Confira o requisito no item antes de comprar.", "Check the requirement on the item before buying.")')
rep('''        if d and d.get("base"):
            u["lvl"] = d["base"]; u["lvlSrc"] = d["src"]''', '''        if d and d.get("base"):
            u["lvl"] = d["base"]; u["lvlSrc"] = d["src"]
        else:
            u["lvl"] = None
        if u.get("rf"):
            import re as _re
            u["rf"] = _re.sub(r"\\s*\\(nv \\d+\\)", "", u["rf"])
    ''')
s = s.replace('''            u["rf"] = _re.sub(r"\\s*\\(nv \\d+\\)", "", u["rf"])
    ''', '''            u["rf"] = _re.sub(r"\\s*\\(nv \\d+\\)", "", u["rf"])''')
s += '''

def effigy_62(DATA):
    """O Sylvan's Effigy pede nível 62 (texto do item no jogo), não 78."""
    m = DATA["milestones"]
    m.pop(78, None)
    m[63] = "Sylvan's Effigy liberado (requer nível 62, ~1 div): tire o Rattling Sceptre, Skeletal Cleric vira o alvo do Pain Offering e ative mais beasts de aura conforme o Spirit."
    for b in DATA["buyOrder"]:
        if "Sylvan's Effigy" in b["item"]:
            b["phase"] = "Nv 62+"
    DATA["fixes"] = ["Sylvan's Effigy é um Stoic Sceptre e requer nível 62 (texto do item no jogo)." if "Sylvan's Effigy é Stoic Sceptre" in f else f for f in DATA["fixes"]]
'''
open("timing.py", "w", encoding="utf-8").write(s)

c = open("chober.py", encoding="utf-8").read()
if "timing.effigy_62(DATA)" not in c:
    c = c.replace("DATA.update(timing=timing.TIMING, timingCases=timing.TIMING_CASES)\n", "DATA.update(timing=timing.TIMING, timingCases=timing.TIMING_CASES)\ntiming.effigy_62(DATA)\n", 1)
open("chober.py", "w", encoding="utf-8").write(c)

for f in ("app_template.html", "char.js"):
    t = open(f, encoding="utf-8").read()
    t = t.replace("if (effigy && pets.length < 4 && lv >= 78)", "if (effigy && pets.length < 4 && lv >= 62)")
    t = t.replace('${lr ? ` · ${T("nível", "level")} ${lr.lvl}${lr.lvlRf ? "/" + lr.lvlRf : ""}` : ""}', '${lr ? ` · ${T("nível", "level")} ${lr.lvl}` : ""}')
    open(f, "w", encoding="utf-8").write(t)
print("ok")
