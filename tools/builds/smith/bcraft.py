# -*- coding: utf-8 -*-
# Oficina de crafting da Smith of Kitava (executado dentro de bdata.py). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("shield", L("Escudo", "Shield"), "Shields_str", L("Armour altíssima: é o dano do Shield Wall, do Fortifying Cry e do Greatest Defence.", "Very high Armour: it's the damage of Shield Wall, Fortifying Cry and Greatest Defence."),
        L("Tower Shield de maior Armour base disponível; ilvl 75+ para % Armour e Armour flat no topo.", "The highest base-Armour Tower Shield available; ilvl 75+ for top % Armour and flat Armour."),
        L("% Armour + Armour flat + vida já fazem o escudo do endgame; resistência a fogo é bônus.", "% Armour + flat Armour + life already make an endgame shield; fire resistance is a bonus."),
        L("Block chance ocupa um prefixo que a Armour quer.", "Block chance takes a prefix that Armour wants."),
        ["increased Armour$", "to Armour$", "to maximum Life$", "to Fire Resistance", "Maximum Fire Resistance"], ["lockshield"]),
 K.item("mace", L("Maça", "Mace"), "One_Hand_Maces", L("+ nível de melee e % dano elemental de ataques (depois do Avatar of Fire).", "+ melee levels and % elemental attack damage (after Avatar of Fire)."),
        L("Maça de uma mão; até o Ato 4, duas. No endgame o Set 2 é Nebuloch (unique).", "One-handed mace; until Act 4, two. In endgame Set 2 is Nebuloch (unique)."),
        L("+3 melee + % dano elemental de ataques é o suficiente para os mapas.", "+3 melee + % elemental attack damage is enough for maps."),
        L("+ físico deixa de importar depois do Avatar of Fire (75% vira fogo, mas o % físico não escala o fogo).", "+ physical stops mattering after Avatar of Fire (75% becomes fire, but % physical doesn't scale fire)."),
        ["Level of all Melee Skills", "Elemental Damage with Attacks", "increased Attack Speed", "Adds .* Fire Damage$"], ["Nebuloch", "dual"]),
 K.item("body", "Body Armour", "Body_Armours_str", L("Body NORMAL de Armour alta: a ascendância dá os mods.", "High-Armour NORMAL body: the ascendancy provides the mods."),
        L("Ornate Plate (ou a base de maior Armour que você equipa) — tem que continuar Normal (branca) para o Smith's Masterwork.", "Ornate Plate (or the highest-Armour base you can wear) — it must stay Normal (white) for Smith's Masterwork."),
        L("Base alta + 20% de qualidade + sockets com runas.", "High base + 20% quality + sockets with runes."),
        L("Transmutation/Regal/Essence transformam em Magic/Rare e desligam o Smith's Masterwork.", "Transmutation/Regal/Essence turn it Magic/Rare and switch off Smith's Masterwork."), ["increased Armour$"], ["normalbody"]),
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_str", L("Vida, resistência a fogo e Chaos.", "Life, fire and Chaos resistance."), L("Base de Armour.", "Armour base."), L("Vida + fogo + Chaos.", "Life + fire + Chaos."), L("Constricting Command substitui no T10+.", "Constricting Command replaces it at T10+."), ["to maximum Life$", "to Fire Resistance", "Chaos Resistance"], ["Constricting Command", "Thrillsteel"]),
 K.item("gloves", L("Luvas", "Gloves"), "Gloves_str", L("Attack speed, + melee e vida.", "Attack speed, + melee and life."), L("Base de Armour; Runeforged Ornate Mitts no setup otimizado.", "Armour base; Runeforged Ornate Mitts in the optimized setup."), L("Attack speed + vida + resistência.", "Attack speed + life + resistance."), L("+2 melee nas luvas é caro: attack speed rende mais cedo.", "+2 melee on gloves is pricey: attack speed pays off earlier."), ["increased Attack Speed", "Level of all Melee Skills", "to maximum Life$"]),
 K.item("boots", L("Botas", "Boots"), "Boots_str", L("Movement Speed, vida e resistências.", "Movement Speed, life and resistances."), L("Base de Armour ilvl 82 para 35%.", "ilvl 82 Armour base for 35%."), L("30%+ MS e vida.", "30%+ MS and life."), L("Momentum na árvore remove a penalidade de Armour.", "Momentum on the tree removes the Armour movement penalty."), ["Movement Speed", "to maximum Life$"]),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("+ melee, vida, Força e Spirit.", "+ melee, life, Strength and Spirit."), L("Qualquer base; anoint Thaumaturgic Generator no endgame.", "Any base; Thaumaturgic Generator anoint in endgame."), L("+2/+3 melee + vida.", "+2/+3 melee + life."), L("O anoint precisa de Distilled Emotions: confira o custo.", "The anoint needs Distilled Emotions: check the cost."), ["Level of all Melee Skills", "to maximum Life$", "to Strength$", "to Spirit$"]),
 K.item("rings", L("Anéis", "Rings"), "Rings", L("Resistência a fogo (Coal Stoker), vida e Chaos.", "Fire resistance (Coal Stoker), life and Chaos."), L("Ruby Ring (implicit de fogo).", "Ruby Ring (fire implicit)."), L("Fogo + vida + Chaos.", "Fire + life + Chaos."), L("Breach Ring é o upgrade do endgame.", "Breach Ring is the endgame upgrade."), ["to Fire Resistance", "to maximum Life$", "Chaos Resistance"]),
 K.item("belt", L("Cinto", "Belt"), "Belts", L("Vida e resistências.", "Life and resistances."), L("Heavy/Plate Belt.", "Heavy/Plate Belt."), L("Vida + Chaos Res.", "Life + Chaos Res."), L("Charms: confira os slots do cinto.", "Charms: check the belt's slots."), ["to maximum Life$", "Chaos Resistance", "to Strength$"]),
 K.item("life-flask", L("Frasco de vida", "Life flask"), "Life_Flasks", L("Recuperação confiável (sem mana com Blood Magic).", "Reliable recovery (no mana with Blood Magic)."), L("Ultimate Life Flask.", "Ultimate Life Flask."), L("Recuperação alta.", "High recovery."), L("Purity of Fire com Herbalism II aumenta a cura do flask.", "Purity of Fire with Herbalism II increases flask healing."), ["Amount Recovered", "Instant"]),
 K.item("charms", "Charms", "Charms", L("Freeze, Stun e Slow.", "Freeze, Stun and Slow."), L("Thawing + Stone + Silver; For Utopia no T10+.", "Thawing + Stone + Silver; For Utopia at T10+."), L("Três gatilhos úteis.", "Three useful triggers."), L("Heatproofing já cobre ailments de dano.", "Heatproofing already covers damaging ailments."), ["Charges", "Duration"], ["For Utopia"]),
]

CK_DETAIL = {
 "shield": dict(
  base=L("Tower Shield ilvl 75+ com a maior Armour base que você equipa.", "ilvl 75+ Tower Shield with the highest base Armour you can wear."),
  targets=[[P, "(101–110)% increased Armour (T2 92–100%)", "75 (65)"], [P, "+(249–277) to Armour", 75], [P, "+(175–189) to maximum Life", 70], [X, "+(41–45)% to Fire Resistance", 82], [X, "+3% to Maximum Fire Resistance", 81], [DS, "Amanamu: Shield Skills fully Break Armour when they Heavy Stun · +1% all maximum Resistances", 65]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Greater Essence of Insulation", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Preserved Rib", "Omen of Abyssal Echoes", "Armourer's Scrap", "Artificer's Orb", "Divine Orb"],
  cheap=[K.trade("Shield (Armour) · Armour ≥ 800 · Life", "Nos primeiros mapas 800–900 de Armour bastam.", "For early maps 800–900 Armour is enough.")],
  value=[S(L("Armour no Magic", "Armour on the Magic item"), L("Base branca → Transmutation/Augmentation até % Armour ou Armour flat → Regal.", "White base → Transmutation/Augmentation until % Armour or flat Armour → Regal."), L("Na campanha, Abyss/Lightless Passage dão Gnawed Rib para gamblar Armour.", "In the campaign, Abyss/Lightless Passage give Gnawed Ribs to gamble Armour.")),
         K.side_exalt("p", "% Armour, Armour e vida", "% Armour, Armour and life"), K.side_exalt("s", "resistência a fogo", "fire resistance"), K.quality("Armourer's Scrap", "")],
  lux=[S(L("Três prefixos de defesa", "Three defence prefixes"), L("Base ilvl 75+; Greater/Perfect Exalted + Omen of Sinistral Exaltation até % Armour T1, Armour flat T1 e vida.", "ilvl 75+ base; Greater/Perfect Exalted + Omen of Sinistral Exaltation until T1 % Armour, T1 flat Armour and life."), ""),
       K.desecrate("Preserved Rib", "", "“Shield Skills fully Break Armour when they Heavy Stun” ou +1% em todas as resistências máximas", "“Shield Skills fully Break Armour when they Heavy Stun” or +1% to all maximum resistances"),
       K.runeforge("Tower Shield", "Verisium"), K.divine, K.quality("Armourer's Scrap", "Vaal Armourer's Infuser")]),
 "mace": dict(
  base=L("Maça de uma mão ilvl 81+ (Set 1). O Set 2 do endgame é Nebuloch.", "ilvl 81+ one-handed mace (Set 1). Endgame Set 2 is Nebuloch."),
  targets=[[X, "+4 to Level of all Melee Skills (T2 +3)", "81 (55)"], [P, "(87–100)% increased Elemental Damage with Attacks", 81], [X, "(26–28)% increased Attack Speed", 77], [P, "Adds (88–101) to (133–154) Fire Damage", 81], [DP, "Kurgal: Empowered Attacks deal (41–59)% increased Damage · Amanamu: Penetrate Fire Resistance", 65], [C, "Perfect Essence of Battle: +2 to Level of all Attack Skills", 72]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Greater Essence of Haste", "Greater Essence of Flames", "Exalted Orb", "Perfect Essence of Battle", "Preserved Jawbone", "Omen of the Blackblooded", "Omen of the Liege", "Omen of Abyssal Echoes", "Blacksmith's Whetstone"],
  cheap=[K.trade("One Hand Mace · +# to Level of all Melee Skills ≥ 3 · % increased Elemental Damage with Attacks", "", "")],
  value=[S(L("Melee ou elemental no Magic", "Melee or elemental on the Magic item"), L("Transmutation/Augmentation até + nível de melee (sufixo) ou % dano elemental de ataques (prefixo) → Regal.", "Transmutation/Augmentation until + melee levels (suffix) or % elemental attack damage (prefix) → Regal."), L("Garantido: Greater Essence of Haste (attack speed) ou Flames (fogo adicionado) no Magic.", "Guaranteed: Greater Essence of Haste (attack speed) or Flames (added fire) on the Magic item.")),
         K.side_exalt("s", "+ nível de melee e attack speed", "+ melee levels and attack speed"), K.side_exalt("p", "% dano elemental e fogo adicionado", "% elemental damage and added fire"), K.quality("Blacksmith's Whetstone", "")],
  lux=[K.desecrate("Preserved Jawbone", "Omen of the Blackblooded", "Empowered Attacks deal (41–59)% increased Damage (Kurgal)", "Empowered Attacks deal (41–59)% increased Damage (Kurgal)"),
       S(L("Perfect Essence of Battle", "Perfect Essence of Battle"), L("Num Rare, remove um mod aleatório e adiciona +2 to Level of all Attack Skills (ocupa o crafted).", "On a Rare, removes a random mod and adds +2 to Level of all Attack Skills (takes the crafted slot)."), ""), K.divine]),
 "body": dict(
  base=L("Ornate Plate Normal (ou a maior Armour base que você equipa).", "Normal Ornate Plate (or the highest base Armour you can wear)."),
  targets=[[L("Base", "Base"), L("Armour base alta · Normal", "High base Armour · Normal"), 1], [L("Qualidade", "Quality"), "+20% (Armourer's Scrap)", 1], [L("Runeforging", "Runeforging"), L("Runic Ward para Scouring Flame", "Runic Ward for Scouring Flame"), 55]],
  mats=["Armourer's Scrap", "Artificer's Orb", "Verisium", "Iron Rune", "Body Rune"],
  cheap=[S(L("Base Normal", "Normal base"), L("Pegue a base Normal de maior Armour que você equipa (drop ou vendor). Não use nenhuma orb de raridade nela.", "Take the highest-Armour Normal base you can wear (drop or vendor). Don't use any rarity orb on it."), L("Usou Transmutation sem querer: pegue outra base Normal.", "Used a Transmutation by accident: get another Normal base."))],
  value=[K.quality("Armourer's Scrap", ""), S(L("Runas nos sockets", "Runes in sockets"), L("Artificer's Orb e Iron Rune (% Armour) ou Body Rune (vida).", "Artificer's Orb and Iron Rune (% Armour) or Body Rune (life)."), "")],
  lux=[K.runeforge("Ornate Plate", "Verisium"), S(L("Scouring Flame com Runic Ward", "Scouring Flame with Runic Ward"), L("A versão Runeforged dá Runic Ward, que o Scouring Flame (Raise Shield) gasta.", "The Runeforged version grants Runic Ward, which Scouring Flame (Raise Shield) spends."), "")]),
 "helmet": dict(
  base=L("Capacete de Armour ilvl 81+.", "ilvl 81+ Armour helmet."),
  targets=[[P, "+(150–174) to maximum Life", 65], [X, "+(41–45)% to Fire Resistance", 82], [X, "Chaos Resistance", 68]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Greater Essence of Insulation", "Exalted Orb", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Helmet · Life ≥ 100 · Fire Resistance · Chaos Resistance", "", "")],
  value=[K.ess_start("Greater Essence of Insulation", "+31–35% resistência a fogo", "+31–35% fire resistance", "Capacete de Armour branco", "White Armour helmet"), K.side_exalt("p", "vida", "life"), K.side_exalt("s", "Chaos Resistance", "Chaos Resistance")],
  lux=[S("Constricting Command", L("Unique barato: Surrounded quase sempre + vida e regen.", "Cheap unique: Surrounded almost always + life and regen."), ""), K.divine]),
 "gloves": dict(
  base=L("Luvas de Armour ilvl 60+.", "ilvl 60+ Armour gloves."),
  targets=[[X, "(14–16)% increased Attack Speed", 60], [X, "+2 to Level of all Melee Skills", 41], [P, "+(120–149) to maximum Life", 60]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation", "Armourer's Scrap"],
  cheap=[K.trade("Gloves · Attack Speed ≥ 10 · Life", "", "")],
  value=[S(L("Attack speed no Magic", "Attack speed on the Magic item"), L("Transmutation/Augmentation até attack speed → Regal.", "Transmutation/Augmentation until attack speed → Regal."), ""), K.side_exalt("p", "vida", "life"), K.quality("Armourer's Scrap", "")],
  lux=[K.side_exalt("s", "+2 melee (depois do attack speed)", "+2 melee (after attack speed)"), K.runeforge("Ornate Mitts", "Verisium")]),
 "boots": dict(
  base=L("Botas de Armour ilvl 82 (35% MS).", "ilvl 82 Armour boots (35% MS)."),
  targets=[[P, "35% increased Movement Speed (T2 30%)", "82 (65)"], [P, "+(120–149) to maximum Life", 60], [X, "Chaos Resistance", 68]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Essence of Hysteria", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Boots · Movement Speed ≥ 25 · Life", "", "")],
  value=[S(L("Movimento no Magic", "Movement on the Magic item"), L("Base ilvl 82 → Transmutation/Augmentation até Movement Speed → Regal.", "ilvl 82 base → Transmutation/Augmentation until Movement Speed → Regal."), L("Garantido: Essence of Hysteria num Rare (30%).", "Guaranteed: Essence of Hysteria on a Rare (30%).")), K.side_exalt("p", "vida", "life"), K.side_exalt("s", "Chaos Resistance", "Chaos Resistance")],
  lux=[K.divine]),
 "amulet": dict(
  base=L("Qualquer amuleto; Jade/Crimson Amulet nas variantes do Lexd.", "Any amulet; Jade/Crimson Amulet in Lexd's variants."),
  targets=[[X, "+3 to Level of all Melee Skills", 75], [P, "+(120–149) to maximum Life", 60], [X, "+(31–33) to Strength", 74], [L("Anoint", "Anoint"), "Thaumaturgic Generator", 1]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation", "Distilled Emotions"],
  cheap=[K.trade("Amulet · +# to Level of all Melee Skills ≥ 2 · Life", "", "")],
  value=[S(L("Melee no Magic", "Melee on the Magic item"), L("Transmutation/Augmentation até + melee → Regal.", "Transmutation/Augmentation until + melee → Regal."), ""), K.side_exalt("p", "vida", "life")],
  lux=[S(L("Anoint Thaumaturgic Generator", "Thaumaturgic Generator anoint"), L("Instila o notable no amuleto com Distilled Emotions: fonte extra de Endurance Charge para o Nebuloch.", "Instil the notable into the amulet with Distilled Emotions: an extra Endurance Charge source for Nebuloch."), ""), K.divine]),
 "rings": dict(
  base=L("Ruby Ring.", "Ruby Ring."),
  targets=[[X, "+(41–45)% to Fire Resistance", 82], [X, "+(24–27)% to Chaos Resistance", 81], [P, "+(100–119) to maximum Life", 54]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Ruby Ring · Fire Resistance · Life", "", "")],
  value=[S(L("Resistências no Magic", "Resistances on the Magic item"), L("Transmutation/Augmentation até fogo ou Chaos → Regal.", "Transmutation/Augmentation until fire or Chaos → Regal."), ""), K.side_exalt("p", "vida", "life")],
  lux=[S("Breach Ring", L("Anel do endgame do Lexd.", "Lexd's endgame ring."), ""), K.divine]),
 "belt": dict(
  base=L("Heavy Belt.", "Heavy Belt."), targets=[[P, "+(150–174) to maximum Life", 65], [X, "Chaos Resistance", 68]], mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb"],
  cheap=[K.trade("Belt · Life ≥ 100 · Chaos Resistance", "", "")], value=[S(L("Vida no Magic", "Life on the Magic item"), L("Transmutation/Augmentation até vida → Regal.", "Transmutation/Augmentation until life → Regal."), ""), K.side_exalt("s", "resistências", "resistances")], lux=[K.divine]),
 "life-flask": dict(
  base="Ultimate Life Flask", targets=[[P, "(76–80)% increased Amount Recovered", 83]], mats=["Orb of Transmutation", "Orb of Augmentation", "Glassblower's Bauble"],
  cheap=[S(L("Transmutation + Augmentation", "Transmutation + Augmentation"), L("Recuperação alta.", "High recovery."), "")], value=[S(L("Qualidade", "Quality"), L("Glassblower's Bauble até 20%.", "Glassblower's Bauble up to 20%."), "")], lux=[S(L("Dois mods bons", "Two good mods"), L("Repita em bases brancas até prefixo e sufixo úteis.", "Repeat on white bases until both prefix and suffix are useful."), "")]),
 "charms": dict(
  base=L("Thawing, Stone e Silver Charm.", "Thawing, Stone and Silver Charm."), targets=[[P, "Charges / duration", 60]], mats=["Orb of Transmutation", "Orb of Augmentation"],
  cheap=[S(L("Charms normais", "Normal charms"), L("Freeze, Stun e Slow.", "Freeze, Stun and Slow."), "")], value=[S("For Utopia", L("Defende com 200% da Armour.", "Defend with 200% of Armour."), "")], lux=[S("The Fall of the Axe · Rite of Passage", L("Luxo do setup otimizado.", "Luxury of the optimized setup."), "")]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
