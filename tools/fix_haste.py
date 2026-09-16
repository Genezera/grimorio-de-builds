# Corrige o exagero "crabs rolam Haste com facilidade": o guia do Mattjestic só diz que crabs são onde é mais fácil achar TODAS as auras T1,
# e manda farmar essences de crab no Whakapanu Island até aparecer Haste (é sorte).
import json

OLD_REC_PT = "Haste é a melhor aura. Quill Crab / Coconut Crab (Ato 4, Whakapanu Island) rolam Haste com facilidade."
OLD_REC_EN = "Haste is the best aura. Quill Crab / Coconut Crab (Act 4, Whakapanu Island) roll Haste easily."
NEW_REC_PT = "Haste é a melhor aura, mas é sorte. Rota do Mattjestic: Ato 4, Whakapanu Island, essences de crab na praia (Quill/Coconut Crab) — repita até aparecer Haste. Antlion Charger e Diretusk Boar (Ato 3) também podem rolar Haste; Quadrilla, Swarming Wisp, Crag Leaper e Hyena Demon NÃO rolam."
NEW_REC_EN = "Haste is the best aura, but it's luck. Mattjestic's route: Act 4, Whakapanu Island, crab essences on the beach (Quill/Coconut Crab) — repeat until Haste shows up. Antlion Charger and Diretusk Boar (Act 3) can also roll Haste; Quadrilla, Swarming Wisp, Crag Leaper and Hyena Demon can NOT."
for f in ("app_template.html", "char.js"):
    s = open(f, encoding="utf-8").read()
    assert OLD_REC_PT in s and OLD_REC_EN in s, f
    s = s.replace(OLD_REC_PT, NEW_REC_PT).replace(OLD_REC_EN, NEW_REC_EN)
    open(f, "w", encoding="utf-8").write(s)

c = open("chober.py", encoding="utf-8").read()
c = c.replace('"mods": "Haste Aura (o mais fácil de achar)"', '"mods": "Qualquer aura T1, inclusive Haste (sorte: farme essences de crab)"')
c = c.replace('"body": "Beasts com a tag very_fast_movement (ex.: Crag Leaper) nunca rolam Haste Aura. Procure Haste em crabs."',
              '"body": "Beasts com a tag very_fast_movement (ex.: Crag Leaper) nunca rolam Haste Aura. Pelo guia do Mattjestic, Quadrilla, Swarming Wisp e Hyena Demon também não. Para Haste, farme essences de crab no Whakapanu Island (Ato 4) — crabs são onde é mais fácil achar todas as auras T1, mas Haste continua sendo sorte e pode levar várias tentativas."')
open("chober.py", "w", encoding="utf-8").write(c)

p = "i18n/en_extra.json"; d = json.load(open(p, encoding="utf-8"))
d["Qualquer aura T1, inclusive Haste (sorte: farme essences de crab)"] = "Any T1 aura, including Haste (luck: farm crab essences)"
d["Beasts com a tag very_fast_movement (ex.: Crag Leaper) nunca rolam Haste Aura. Pelo guia do Mattjestic, Quadrilla, Swarming Wisp e Hyena Demon também não. Para Haste, farme essences de crab no Whakapanu Island (Ato 4) — crabs são onde é mais fácil achar todas as auras T1, mas Haste continua sendo sorte e pode levar várias tentativas."] = \
    "Beasts with the very_fast_movement tag (e.g. Crag Leaper) never roll Haste Aura. Per Mattjestic's guide, Quadrilla, Swarming Wisp and Hyena Demon don't either. For Haste, farm crab essences on Whakapanu Island (Act 4) — crabs are the easiest place to find all T1 auras, but Haste is still luck and can take many attempts."
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=0)

# spirit_tiers / timing: textos que dizem que crabs "rolam Haste"
for f in ("spirit_tiers.py", "timing.py"):
    s = open(f, encoding="utf-8").read()
    s = s.replace("Quill Crab e Coconut Crab aparecem no Whakapanu Island (Ato 4).", "Quill Crab e Coconut Crab aparecem no Whakapanu Island (Ato 4); Haste neles é sorte.")
    open(f, "w", encoding="utf-8").write(s)
print("ok")
