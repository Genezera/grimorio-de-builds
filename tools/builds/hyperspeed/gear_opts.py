# -*- coding: utf-8 -*-
# Opções por slot com nível mínimo, custo e nota de encaixe na build (executado dentro de bdata.py: usa L e common.ECO).
# Nível = requisito da base do item (RePoE); preço = poe.ninja (Divines); mods = poe.ninja. A nota (s) é o meu julgamento de encaixe para o Monk Hollow Palm
# (Evasion para a velocidade, Energy Shield para o crítico e a defesa, dano adicionado, +níveis de Melee) — não é um número do jogo. Barato = Grátis + Barato; Completo = todos.
# Custo: free < 0,05 Div · cheap < 1 · value < 30 · lux (ou item do guia do autor sem preço).
import common as _c, glob as _g, json as _j, os as _os, re as _re

# nível exigido do unique = o que o poe.ninja mostra no item (levelRequired); o menor entre as variantes (Tense/Runeforged/Runemastered...). 0 vira 1.
_REQ = {}
for _f in _g.glob(_os.path.join(_os.path.dirname(_c.__file__), "..", "dl", "eco_Unique*.json")):
    for _l in _j.load(open(_f, encoding="utf-8"))["lines"]:
        if _l.get("levelRequired") not in (None, ""):
            _REQ.setdefault(_l["name"], set()).add(int(_l["levelRequired"]))


def O(n, kind, lv, s, why, cost=None, tip=None):
    """n = nome (unique) ou descrição (rare); kind 'u'|'r'; lv = nível mínimo; s = nota de encaixe 0-100; why = (pt, en)."""
    price = None
    if kind == "u":
        e = _c.ECO.get(n) or {}
        price = e.get("price")
        if n in _REQ:
            lv = max(1, min(_REQ[n]))
            why = tuple(_re.sub(r"\s*\((?:([^()]*?), )?(?:nível|level) \d+\)", lambda m: f" ({m.group(1)})" if m.group(1) else "", w) for w in why)
        cost = cost or ("free" if price is not None and price < .05 else "cheap" if price is not None and price < 1 else "value" if price is not None and price < 30 else "lux")
    return dict(n=n, k=kind, lv=lv, c=cost or "free", s=s, p=round(price, 3) if price is not None else None, w=L(*why), tip=tip)


GEAR_OPTS = {
 "set1": [
  O(L("Spear branca do vendor (Hardwood Spear)", "White vendor spear (Hardwood Spear)"), "r", 1, 40, ("Vem da Huntress (stash): as duas skills do começo exigem spear. Vale até o Ironhead Spear.", "Comes from the Huntress (stash): the early skills need a spear. Good until the Ironhead Spear.")),
  O(L("Ironhead Spear com dano adicionado", "Ironhead Spear with added damage"), "r", 5, 55, ("Base de nível 5 (Adds 1 to 4 Physical Damage). Não gaste currency: a spear só serve até o 22.", "Level 5 base (Adds 1 to 4 Physical Damage). Don't spend currency: the spear only lasts until 22.")),
  O(L("Sem arma (Hollow Palm Technique)", "No weapon (Hollow Palm Technique)"), "r", 23, 90, ("Do 23 em diante o Set 1 fica VAZIO: com o Hollow Palm Technique alocado as skills de cajado funcionam sem arma e a velocidade vem da Evasion.", "From 23 on Set 1 stays EMPTY: with Hollow Palm Technique allocated the quarterstaff skills work without a weapon and speed comes from Evasion.")),
 ],
 "set2": [
  O(L("Sinister Quarterstaff rare com crítico e dano elemental", "Rare Sinister Quarterstaff with crit and elemental damage"), "r", 67, 90, ("A arma do Set 2 do autor (base nível 67): +3,62% de chance de crítico, dano adicionado de fogo, raio e frio, +22% de dano crítico e +5 de nível de Melee. Só o Falling Thunder usa.", "The author's Set 2 weapon (level 67 base): +3.62% crit chance, added fire, lightning and cold damage, +22% crit damage and +5 Melee levels. Only Falling Thunder uses it.")),
 ],
 "helmet": [
  O(L("Capacete rare com vida e resistências", "Rare helmet with life and resistances"), "r", 1, 50, ("Vida e resistências que faltarem: a build ainda é de vida até o corte Waystones.", "Life and whatever resistances you're missing: the build is still a life build until the Waystones cut.")),
  O(L("Coral Circlet (o do autor no 23+)", "Coral Circlet (the author's at 23+)"), "r", 23, 68, ("Vida e Energy Shield (+30 vida, +42 ES). É o capacete da variante 23+ do autor.", "Life and Energy Shield (+30 life, +42 ES). It's the helmet of the author's 23+ variant.")),
  O(L("Ancestral Tiara rare com ~500 de ES", "Rare Ancestral Tiara with ~500 ES"), "r", 80, 90, ("A base do autor (nível 80): o mais importante é o Energy Shield (450+, de preferência 500+), depois chance de crítico e resistências.", "The author's base (level 80): the most important stat is Energy Shield (450+, ideally 500+), then crit chance and resistances.")),
  O(L("Kamasan Tiara rare (Final Endgame)", "Rare Kamasan Tiara (Final Endgame)"), "r", 75, 92, ("O capacete da Final Endgame (base nível 75): +73 de ES, +37 de mana e resistências.", "The Final Endgame helmet (level 75 base): +73 ES, +37 mana and resistances."), cost="value"),
 ],
 "body": [
  O(L("Corpo rare de Evasion com vida e resistências", "Rare Evasion body armour with life and resistances"), "r", 1, 50, ("Evasion primeiro: a velocidade do Hollow Palm vem dela (1% a cada 75). Suba a base com o nível.", "Evasion first: Hollow Palm's speed comes from it (1% per 75). Raise the base with your level.")),
  O(L("Strider Vest rare com vida e Evasion", "Rare Strider Vest with life and Evasion"), "r", 52, 70, ("O corpo do autor na campanha (base nível 52): +40 de vida e 33% de Evasion. Mantém a build de vida até o corte Waystones.", "The author's campaign body armour (level 52 base): +40 life and 33% Evasion. Keeps the build on life until the Waystones cut.")),
  O(L("Sleek Jacket rare com 1400+ Evasion e ~500 de ES", "Rare Sleek Jacket with 1400+ Evasion and ~500 ES"), "r", 65, 92, ("O corpo do plano de ES (base nível 65): 1400–1500 de Evasion e uns 500 de ES para não derrubar o crítico. Resistências no cap e Deflection ou 'faster start of ES Recharge' por último.", "The ES plan's body armour (level 65 base): 1400–1500 Evasion and about 500 ES so it doesn't drag down crit. Resistances capped and Deflection or 'faster start of ES Recharge' last."), cost="value"),
 ],
 "gloves": [
  O(L("Luvas rare com vida e Evasion", "Rare gloves with life and Evasion"), "r", 1, 50, ("Vida primeiro; procure dano adicionado se puder.", "Life first; look for added damage if you can.")),
  O(L("Hunting Bracers com +2 de nível de Melee", "Hunting Bracers with +2 Melee levels"), "r", 45, 72, ("A base de nível 45 do autor: +2 níveis de Melee (Act 3-6) ou +20 de vida.", "The author's level 45 base: +2 Melee levels (Act 3-6) or +20 life.")),
  O(L("Opulent Gloves rare com dano adicionado e +2 de Melee", "Rare Opulent Gloves with added damage and +2 Melee"), "r", 70, 86, ("A base do plano Waystones (nível 70): dano de raio e físico adicionados, vida, Dexterity, ES e +2 de nível de Melee.", "The Waystones plan's base (level 70): added lightning and physical damage, life, Dexterity, ES and +2 Melee levels.")),
  O(L("Luvas rare para o Way of the Stonefist", "Rare gloves for Way of the Stonefist"), "r", 80, 92, ("O ideal do autor: DOIS danos adicionados de tier alto (fogo, raio, frio ou físico), Evasion flat T1 (ou híbrida), velocidade de cast com a vida cheia (vira velocidade de ataque) e Dexterity (chance de projétil extra).", "The author's ideal: TWO high-tier added damage mods (fire, lightning, cold or physical), T1 flat Evasion (or hybrid), cast speed on Full Life (becomes attack speed) and Dexterity (a chance for an extra projectile)."), cost="value"),
 ],
 "boots": [
  O(L("Botas rare com movimento e vida", "Rare boots with movement and life"), "r", 1, 40, ("Qualquer base com movimento e vida até o Wrapped Sandals (11).", "Any base with movement and life until Wrapped Sandals (11).")),
  O("Wrapped Sandals", "r", 11, 45, ("Base de nível 11 com 10% de movimento: as botas do começo do autor.", "Level 11 base with 10% movement: the author's early boots.")),
  O("Bound Boots", "r", 45, 68, ("Base de nível 45 (Evasion alta) com 10% de movimento: as botas da campanha do autor.", "Level 45 base (high Evasion) with 10% movement: the author's campaign boots.")),
  O(L("Sekhema Sandals rare com ES", "Rare Sekhema Sandals with ES"), "r", 80, 84, ("A base do plano Waystones (nível 80): 68% de ES aumentado, resistências e 30% de movimento.", "The Waystones plan's base (level 80): 68% increased ES, resistances and 30% movement."), cost="value"),
  O(L("Daggerfoot Shoes rare com Deflection", "Rare Daggerfoot Shoes with Deflection"), "r", 80, 92, ("O ideal do autor: Deflection Rating primeiro, Evasion e ES altos (a velocidade do Hollow Palm), 35% de movimento por último (você se move com o Tempest Flurry).", "The author's ideal: Deflection Rating first, high Evasion and ES (Hollow Palm's speed), 35% movement last (you move with Tempest Flurry)."), cost="value"),
 ],
 "amulet": [
  O(L("Azure Amulet com vida", "Azure Amulet with life"), "r", 1, 45, ("Base de nível 1 com +20 de vida: o amuleto do começo do autor.", "Level 1 base with +20 life: the author's early amulet.")),
  O(L("Bloodstone Amulet com +2 de Melee", "Bloodstone Amulet with +2 Melee"), "r", 18, 66, ("+2 níveis de Melee (nível 18): já sobe o dano da campanha.", "+2 Melee levels (level 18): raises campaign damage already.")),
  O(L("Amber Amulet com +3 de Melee e crítico", "Amber Amulet with +3 Melee and crit"), "r", 8, 78, ("A base do plano Waystones: +3 níveis de Melee, 35% de chance de crítico, 35% de dano crítico e Evasion.", "The Waystones plan's base: +3 Melee levels, 35% crit chance, 35% crit damage and Evasion.")),
  O(L("Absent Amulet com +4 de Melee e Trinity", "Absent Amulet with +4 Melee and Trinity"), "r", 50, 94, ("O do autor (nível 50): +3 de Melee (+4 com o craft de Breach), Trinity de brinde, ES e Evasion. Instill: Stimulants (velocidade de ataque com o Lavianga's Spirits) ou Subterfuge Mask.", "The author's (level 50): +3 Melee (+4 with the Breach craft), Trinity for free, ES and Evasion. Instill: Stimulants (attack speed with Lavianga's Spirits) or Subterfuge Mask."), cost="value"),
 ],
 "rings": [
  O("Iron Ring", "r", 1, 55, ("Base de nível 1: procure dano adicionado (o autor manda tirar cedo, é o que sobe o DPS da spear).", "Level 1 base: look for added damage (the author says get it early: it's what raises the spear's DPS).")),
  O(L("Sapphire/Ruby Ring com dano adicionado e resistências", "Sapphire/Ruby Ring with added damage and resistances"), "r", 12, 66, ("Bases de nível 8 e 12 da campanha do autor: dano de raio adicionado e resistências.", "The author's campaign level 8 and 12 bases: added lightning damage and resistances.")),
  O(L("Breach Ring rare com dano adicionado e leech", "Rare Breach Ring with added damage and leech"), "r", 40, 90, ("Base de nível 40: dano adicionado de fogo, frio e raio, resistências e UM anel com Leech Physical Damage as Mana (o autor exige em um deles).", "Level 40 base: added fire, cold and lightning damage, resistances and ONE ring with Leech Physical Damage as Mana (the author requires it on one)."), cost="value"),
  O("Kalandra's Touch", "u", 1, 92, ("Reflete o anel do lado oposto: só vale com um anel já muito bom. ~33 Divines.", "Reflects the opposite ring: only worth it with an already very good ring. ~33 Divines."), cost="lux"),
 ],
 "belt": [
  O("Rawhide Belt", "r", 1, 45, ("Base de nível 1 com resistências: o cinto da campanha do autor.", "Level 1 base with resistances: the author's campaign belt.")),
  O("Shavronne's Satchel", "u", 62, 88, ("A vida dos flasks também vale para o ES e mais cargas ganhas (com 21–30% menos velocidade de recuperação). Use com um Life Flask de recuperação INSTANTÂNEA. Fine Belt, nível 62.", "Flask life recovery also applies to ES and more charges gained (with 21–30% reduced recovery rate). Use with an INSTANT-recovery Life Flask. Fine Belt, level 62.")),
  O("Mageblood", "u", 55, 100, ("O cinto da Final Endgame (luxo, ~570 Divines): Silver, Stibnite, Jade e Sulphur; de preferência um duplicado.", "The Final Endgame belt (luxury, ~570 Divines): Silver, Stibnite, Jade and Sulphur; ideally one duplicate."), cost="lux"),
 ],
}
GEAR_OPTS["charms"] = [
  O("Sapphire Charm", "r", 5, 45, ("Charm mágico do começo do autor (nível 5). O slot de charm vem da quest do Medallion.", "The author's early magic charm (level 5). The charm slot comes from the Medallion quest.")),
  O("Ngamahu's Chosen", "u", 5, 80, ("Ao usar dá o máximo de Rage: alimenta o Rage III. Ruby Charm, quase de graça.", "On use grants maximum Rage: feeds Rage III. Ruby Charm, nearly free.")),
  O("The Fall of the Axe", "u", 10, 74, ("Onslaught durante o efeito quando você sofre Slow.", "Onslaught during the effect when you're Slowed.")),
  O("Nascent Hope", "u", 12, 78, ("O ES começa a recarregar ao usar (contra Freeze): útil com CI.", "ES Recharge starts on use (against Freeze): useful with CI.")),
  O("Rite of Passage", "u", 50, 92, ("Possessão por espíritos animais ao usar. Luxo (~15 Divines).", "Possession by animal spirits on use. Luxury (~15 Divines)."), cost="value"),
]
GEAR_OPTS["flasks"] = [
  O("Lesser Life Flask", "r", 1, 40, ("Base de vida do começo: use a melhor que cair.", "Early life base: use the best that drops.")),
  O("Giant Life Flask", "r", 23, 58, ("Base de nível 23 (a do autor no 23+).", "Level 23 base (the author's at 23+).")),
  O("Ultimate Life Flask", "r", 60, 84, ("A base do autor no endgame (nível 60): com 28% de recuperação INSTANTÂNEA e 33% de cargas, e o Shavronne's Satchel, devolve ES.", "The author's endgame base (level 60): with 28% INSTANT recovery and 33% increased charges, and Shavronne's Satchel, it gives ES back.")),
  O("Lavianga's Spirits", "u", 49, 88, ("Flask de mana que não se usa: o efeito fica sempre ativo (~0,1 Divine). O autor liga o instill Stimulants do amuleto a ele.", "A mana flask you don't use: its effect is always on (~0.1 Divine). The author pairs the amulet's Stimulants instill with it.")),
]
SLOT_OPTS = ["set1", "set2", "helmet", "body", "gloves", "boots", "amulet", "rings", "belt", "charms", "flasks"]
