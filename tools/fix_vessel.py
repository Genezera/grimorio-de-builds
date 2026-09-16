# Spirit Vessel: um texto só, por fase, e sem números inventados.
# Dados do guia do Mattjestic (dl/matt.json, ids internos das gems):
#   "Giant's Blood Endgame" (variantes 13-15): Loyalty + Furious Slam (skill) + Arctic Howl (skill) + Rapid Attacks II + Rage III
#   "Endgame Mapping/Bossing" e setups 90+ (16-24): Loyalty + Devour (skill) + Oil Barrage (skill) + Salvo (SUPPORT) + Living Lightning II (SUPPORT)
import json
c = open("chober.py", encoding="utf-8").read()
def rep(a, b, count=1):
    global c
    assert a in c, "NOT FOUND: " + a[:70]
    c = c.replace(a, b, count)

# sockets do item: Spirit Vessel não é socket do body
rep('U("Body Armour", "Forgotten Warden", ["Fox Idol", "Spirit Vessel: Furious Slam + Arctic Howl"])', 'U("Body Armour", "Forgotten Warden", ["Fox Idol"])', 2)
rep('U("Body Armour", "Forgotten Warden", ["Fox Idol", "Spirit Vessel: Devour + Oil Barrage + Salvo + Living Lightning"])', 'U("Body Armour", "Forgotten Warden", ["Fox Idol", "Hawk Idol"])', 2)

# explicação dos supports
rep('"Furious Slam": "Skill de Bear socketada no Spirit Vessel: o Vessel vira urso e dá slams. Cada skill diferente socketada = +20% more dano do Vessel."',
    '"Furious Slam": "Gem de SKILL de Bear (não é support) que vai socketada no Spirit Vessel: o Vessel passa a usar esse ataque. Setup T15 do Mattjestic."')
rep('"Arctic Howl": "Skill de Werewolf socketada no Spirit Vessel: congela e dá dano de frio aos aliados."',
    '"Arctic Howl": "Gem de SKILL de Werewolf (não é support) socketada no Spirit Vessel. Setup T15 do Mattjestic, junto com Furious Slam."')
rep('"Devour": "Skill de Wyvern socketada no Spirit Vessel (versão endgame)."',
    '"Devour": "Gem de SKILL de Wyvern (não é support) socketada no Spirit Vessel. Setup de endgame (nível 90+) do Mattjestic."')
rep('"Oil Barrage": "Skill de Wyvern socketada no Spirit Vessel."',
    '"Oil Barrage": "Gem de SKILL de Wyvern (não é support) socketada no Spirit Vessel. Setup de endgame (nível 90+), junto com Devour."')
rep('"Salvo": "Skill socketada no Spirit Vessel."',
    '"Salvo": "SUPPORT (não é skill) usado no Spirit Vessel no setup de endgame do Mattjestic, junto com Devour e Oil Barrage."')
rep('"Living Lightning II": "Skill socketada no Spirit Vessel."',
    '"Living Lightning II": "SUPPORT (não é skill) usado no Spirit Vessel no setup de endgame do Mattjestic, junto com Devour e Oil Barrage."')

rep('G("Spirit Vessel", ["Loyalty", "Furious Slam", "Arctic Howl", "Rapid Attacks II", "Rage III"], "Companion grátis", "Vem do Forgotten Warden. Furious Slam (Bear) e Arctic Howl (Werewolf) socketados: +20% more dano por skill diferente."),',
    'G("Spirit Vessel", ["Loyalty", "Furious Slam", "Arctic Howl", "Rapid Attacks II", "Rage III"], "Companion do Forgotten Warden", "Vem do Forgotten Warden. USE ESTE até o nível 90: é o setup \\"Giant\'s Blood Endgame\\" do Mattjestic — 2 gems de skill (Furious Slam de Bear e Arctic Howl de Werewolf) + Loyalty, Rapid Attacks II e Rage III. No endgame (nível 90+) ele troca para Devour + Oil Barrage + Salvo + Living Lightning II."),')
rep('G("Spirit Vessel", ["Loyalty", "Devour", "Oil Barrage", "Salvo", "Living Lightning II"], "Companion grátis", "4 skills diferentes socketadas = +80% more dano do Vessel."),',
    'G("Spirit Vessel", ["Loyalty", "Devour", "Oil Barrage", "Salvo", "Living Lightning II"], "Companion do Forgotten Warden", "Setup de endgame (nível 90+) do Mattjestic, usado em todas as variantes dele de Endgame Mapping/Bossing: 2 gems de skill de Wyvern (Devour e Oil Barrage) + os supports Loyalty, Salvo e Living Lightning II. Antes do 90, use a versão com Furious Slam + Arctic Howl (fase T15)."),')
rep('80: "Forgotten Warden: Spirit Vessel com Furious Slam + Arctic Howl.",', '80: "Forgotten Warden: Spirit Vessel com Furious Slam + Arctic Howl (+ Loyalty, Rapid Attacks II, Rage III).",')
open("chober.py", "w", encoding="utf-8").write(c)

t = open("timing.py", encoding="utf-8").read()
a = '("Spirit Vessel: socket Furious Slam (Bear) + Arctic Howl (Werewolf).", "Spirit Vessel: socket Furious Slam (Bear) + Arctic Howl (Werewolf).")'
assert a in t
t = t.replace(a, '("Spirit Vessel até o nível 90: Loyalty + Furious Slam + Arctic Howl + Rapid Attacks II + Rage III. No endgame 90+: Loyalty + Devour + Oil Barrage + Salvo + Living Lightning II.", "Spirit Vessel until level 90: Loyalty + Furious Slam + Arctic Howl + Rapid Attacks II + Rage III. At endgame 90+: Loyalty + Devour + Oil Barrage + Salvo + Living Lightning II.")')
open("timing.py", "w", encoding="utf-8").write(t)

p = "i18n/en_extra.json"; d = json.load(open(p, encoding="utf-8"))
d.update({
 "Gem de SKILL de Bear (não é support) que vai socketada no Spirit Vessel: o Vessel passa a usar esse ataque. Setup T15 do Mattjestic.": "Bear SKILL gem (not a support) socketed into Spirit Vessel: the Vessel uses that attack. Mattjestic's T15 setup.",
 "Gem de SKILL de Werewolf (não é support) socketada no Spirit Vessel. Setup T15 do Mattjestic, junto com Furious Slam.": "Werewolf SKILL gem (not a support) socketed into Spirit Vessel. Mattjestic's T15 setup, together with Furious Slam.",
 "Gem de SKILL de Wyvern (não é support) socketada no Spirit Vessel. Setup de endgame (nível 90+) do Mattjestic.": "Wyvern SKILL gem (not a support) socketed into Spirit Vessel. Mattjestic's endgame setup (level 90+).",
 "Gem de SKILL de Wyvern (não é support) socketada no Spirit Vessel. Setup de endgame (nível 90+), junto com Devour.": "Wyvern SKILL gem (not a support) socketed into Spirit Vessel. Endgame setup (level 90+), together with Devour.",
 "SUPPORT (não é skill) usado no Spirit Vessel no setup de endgame do Mattjestic, junto com Devour e Oil Barrage.": "SUPPORT (not a skill) used on Spirit Vessel in Mattjestic's endgame setup, together with Devour and Oil Barrage.",
 "Companion do Forgotten Warden": "Forgotten Warden companion",
 "Vem do Forgotten Warden. USE ESTE até o nível 90: é o setup \"Giant's Blood Endgame\" do Mattjestic — 2 gems de skill (Furious Slam de Bear e Arctic Howl de Werewolf) + Loyalty, Rapid Attacks II e Rage III. No endgame (nível 90+) ele troca para Devour + Oil Barrage + Salvo + Living Lightning II.": "Comes from Forgotten Warden. USE THIS until level 90: it's Mattjestic's \"Giant's Blood Endgame\" setup — 2 skill gems (Bear's Furious Slam and Werewolf's Arctic Howl) + Loyalty, Rapid Attacks II and Rage III. At endgame (level 90+) it switches to Devour + Oil Barrage + Salvo + Living Lightning II.",
 "Setup de endgame (nível 90+) do Mattjestic, usado em todas as variantes dele de Endgame Mapping/Bossing: 2 gems de skill de Wyvern (Devour e Oil Barrage) + os supports Loyalty, Salvo e Living Lightning II. Antes do 90, use a versão com Furious Slam + Arctic Howl (fase T15).": "Mattjestic's endgame setup (level 90+), used in all his Endgame Mapping/Bossing variants: 2 Wyvern skill gems (Devour and Oil Barrage) + the supports Loyalty, Salvo and Living Lightning II. Before 90, use the Furious Slam + Arctic Howl version (T15 phase).",
 "Forgotten Warden: Spirit Vessel com Furious Slam + Arctic Howl (+ Loyalty, Rapid Attacks II, Rage III).": "Forgotten Warden: Spirit Vessel with Furious Slam + Arctic Howl (+ Loyalty, Rapid Attacks II, Rage III).",
})
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=0)

# adapt: o Spirit Vessel adicionado segue o nível (T15 antes do 90, endgame depois)
for f in ("adapt.js", "app_template.html"):
    s = open(f, encoding="utf-8").read()
    a = '    const sv = pick(t15, /^Spirit Vessel/);'
    assert a in s, f
    s = s.replace(a, '    const sv = pick(S.lv >= 90 ? phaseById("mm") : t15, /^Spirit Vessel/);')
    open(f, "w", encoding="utf-8").write(s)
print("ok")
