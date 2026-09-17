# -*- coding: utf-8 -*-
# Oficina de crafting da Infernalist (executado dentro de bdata.py). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("staff", L("Cajado (leveling e staff barato)", "Staff (leveling and cheap staff)"), "Staves", L("+ nível de spells, dano como extra, cast speed — o staff 'giga' do Ignatius.", "+ spell levels, damage as extra, cast speed — Ignatius's 'giga' staff."), L("Qualquer staff de Inteligência; ilvl 81+ para os tiers do topo.", "Any Intelligence staff; ilvl 81+ for top tiers."), L("6 stats fortes + Perfect Essence of Sorcery (+5 spells).", "6 strong stats + Perfect Essence of Sorcery (+5 spells)."), L("A essence remove um mod aleatório: não arrisque o cast speed (veja a receita).", "The essence removes a random mod: don't risk the cast speed (see the recipe)."), ["Level of all Spell Skills", "as Extra", "increased Cast Speed", "increased Lightning Damage$"], ["Earthbound"]),
 K.item("wand", L("Dueling Wand + foco", "Dueling Wand + focus"), "Wands", L("Spellslinger (nível 65) com + spells, spell damage e crítico.", "Spellslinger (level 65) with + spells, spell damage and crit."), L("Dueling Wand; Tasalian/Runed Focus na outra mão.", "Dueling Wand; Tasalian/Runed Focus in the off-hand."), L("+ spells e dois mods de dano.", "+ spells and two damage mods."), L("Mana na wand só atrapalha o Pyromantic Pact.", "Mana on the wand only hurts Pyromantic Pact."), ["Level of all Spell Skills", "increased Spell Damage", "Critical Hit Chance for Spells", "increased Cast Speed"]),
 K.item("focus", L("Foco", "Focus"), "Foci", L("Spell damage, + spells e ES.", "Spell damage, + spells and ES."), L("Tasalian Focus → Runed Focus.", "Tasalian Focus → Runed Focus."), L("+2 spells e spell damage.", "+2 spells and spell damage."), L("Evite o prefixo híbrido de mana.", "Avoid the hybrid mana prefix."), ["Level of all Spell Skills", "increased Spell Damage$", "maximum Energy Shield$"]),
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_int", L("ES, vida e resistências.", "ES, life and resistances."), L("Ancestral/Sorcerous Tiara → Kamasan Tiara com anoint.", "Ancestral/Sorcerous Tiara → anointed Kamasan Tiara."), L("ES + vida + duas resistências.", "ES + life + two resistances."), L("O prefixo híbrido de mana (Angel's) é ruim aqui.", "The hybrid mana prefix (Angel's) is bad here."), ["increased Energy Shield$", "to maximum Life$", "Fire Resistance"]),
 K.item("gloves", L("Luvas", "Gloves"), "Gloves_int", L("Dano crítico, ES e resistências.", "Crit damage, ES and resistances."), L("Maligaro's Virtuosity no começo; rare de ES depois.", "Maligaro's Virtuosity early; rare ES gloves later."), L("ES + resistência + dano crítico.", "ES + resistance + crit damage."), L("Sem mana.", "No mana."), ["maximum Energy Shield$", "Critical Damage Bonus", "Resistance$"], ["Maligaro's Virtuosity"]),
 K.item("boots", L("Botas", "Boots"), "Boots_int", L("Movement Speed + ES + resistências.", "Movement Speed + ES + resistances."), L("Lattice/Dunerunner Sandals.", "Lattice/Dunerunner Sandals."), L("30% Movement Speed + duas resistências.", "30% Movement Speed + two resistances."), L("Não compre bota sem Movement Speed.", "Don't buy boots without Movement Speed."), ["Movement Speed", "maximum Energy Shield$", "Resistance$"], ["Decree of Flight"]),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("Recoup como vida, + spells e Spirit.", "Recoup as life, + spells and Spirit."), L("Solar Amulet (Spirit) → rare com recoup.", "Solar Amulet (Spirit) → rare with recoup."), L("Recoup + um mod de dano ou Spirit.", "Recoup + a damage or Spirit mod."), L("O recoup como MANA (of Zen) não serve: queremos como vida.", "Recoup as MANA (of Zen) doesn't work: we want it as life."), ["Recouped as Life", "Level of all Spell Skills", "to Spirit$"], ["Choir of the Storm"]),
 K.item("rings", L("Anéis", "Rings"), "Rings", L("Resistências e cast speed.", "Resistances and cast speed."), L("Prismatic Ring → Snakepit (esquerdo).", "Prismatic Ring → Snakepit (left)."), L("Resistências + cast speed.", "Resistances + cast speed."), L("O Snakepit só funciona no anel esquerdo.", "Snakepit only works in the left ring slot."), ["all Elemental Resistances", "increased Cast Speed", "Resistance$"], ["Snakepit"]),
 K.item("belt", L("Cinto", "Belt"), "Belts", L("Recoup de fogo (Perfect Essence of Insulation) + vida.", "Fire recoup (Perfect Essence of Insulation) + life."), "Heavy Belt", L("Recoup de fogo + vida + resistências.", "Fire recoup + life + resistances."), L("Sem o recoup do cinto o Pyromantic Pact fica perigoso.", "Without belt recoup Pyromantic Pact is dangerous."), ["to maximum Life$", "Fire Resistance$"], ["Coward's Legacy", "Mageblood"]),
 K.item("flask", L("Frascos", "Flasks"), "Life_Flasks", L("Vida no leveling; Blood of the Warrior no endgame.", "Life while leveling; Blood of the Warrior in endgame."), "Ultimate Life Flask", L("Recuperação alta.", "High recovery."), L("Com Pyromantic Pact o flask de mana é inútil.", "With Pyromantic Pact the mana flask is useless."), ["Amount Recovered"], ["Blood of the Warrior"]),
 K.item("charms", "Charms", "Charms", L("Freeze e Ignite (você se incendeia de propósito).", "Freeze and Ignite (you set yourself on fire on purpose)."), L("Thawing + Dousing + Golden.", "Thawing + Dousing + Golden."), L("Três gatilhos.", "Three triggers."), L("Beira's Anguish cedo; Rite of Passage/For Utopia no luxo.", "Beira's Anguish early; Rite of Passage/For Utopia for luxury."), ["Charges", "Duration"], ["Beira's Anguish"]),
]

CK_DETAIL = {
 "staff": dict(
  base=L("Staff de Inteligência; ilvl 81+ para os tiers do topo.", "Intelligence staff; ilvl 81+ for top tiers."),
  targets=[[C, "Perfect Essence of Sorcery: +5 to Level of all Spell Skills", 72], [X, "+(5–6) to Level of all Spell Skills (T2 +4)", "78 (55)"], [P, "Gain (55–60)% of Damage as Extra Lightning Damage", 80], [X, "(50–52)% increased Cast Speed", 80], [P, "(209–238)% increased Lightning Damage", 81]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Perfect Essence of Sorcery", "Omen of Dextral Crystallisation", "Arcanist's Etcher"],
  cheap=[S(L("Leveling", "Leveling"), L("Staff branco do vendor → Transmutation/Augmentation até + spells ou dano de raio. Vendors renovam a cada nível: olhe sempre.", "White vendor staff → Transmutation/Augmentation until + spells or lightning damage. Vendors refresh every level: always check."), "")],
  value=[K.trade("Staff · Gain % of Damage as Extra · increased Cast Speed · increased Spell Damage", "Compre um de 6 stats forte por 1–2 Exalted (dano como extra, spell damage, cast speed, raio).", "Buy a strong 6-stat one for 1–2 Exalted (damage as extra, spell damage, cast speed, lightning)."),
         S(L("Perfect Essence of Sorcery", "Perfect Essence of Sorcery"), L("A essence troca um mod aleatório por +5 spells (sufixo). Com Omen of Dextral Crystallisation ela remove só um sufixo: bom se os sufixos forem lixo; se o único sufixo bom for o cast speed, use sem omen e aceite o risco num staff de 1–2 Exalted.", "The essence swaps a random mod for +5 spells (suffix). With Omen of Dextral Crystallisation it only removes a suffix: good if the suffixes are junk; if cast speed is the only good suffix, go without the omen and accept the risk on a 1–2 Exalted staff."), L("Removeu o cast speed: compre outro staff, é barato.", "It removed cast speed: buy another staff, it's cheap.")),
         K.quality("Arcanist's Etcher", "")],
  lux=[S(L("Set 2: Chiming Staff", "Set 2: Chiming Staff"), L("Um Chiming Staff barato no Weapon Set 2 só para o Sigil of Power.", "A cheap Chiming Staff on Weapon Set 2 just for Sigil of Power."), ""), S("Earthbound", L("No setup CoA o Earthbound fica no Set 2 para o snapshot do Pinnacle of Power.", "In the CoA setup Earthbound sits on Set 2 for the Pinnacle of Power snapshot."), "")]),
 "wand": dict(
  base=L("Dueling Wand (nível 65).", "Dueling Wand (level 65)."),
  targets=[[C, "Perfect Essence of Sorcery: +3 to Level of all Spell Skills", 72], [X, "+4 to Level of all Spell Skills (T2 +3)", "78 (55)"], [P, "(105–119)% increased Spell Damage", 80], [X, "(33–35)% increased Cast Speed", 80], [X, "(60–73)% increased Critical Hit Chance for Spells", 76]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Perfect Essence of Sorcery", "Arcanist's Etcher"],
  cheap=[K.trade("Dueling Wand · +# to Level of all Spell Skills", "O Ignatius: espere uma BOA; antes disso o staff + essence rende mais.", "Ignatius: wait for a GOOD one; before that the staff + essence is better.")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Dueling Wand branca → Transmutation/Augmentation até + spells e spell damage → Regal.", "White Dueling Wand → Transmutation/Augmentation until + spells and spell damage → Regal."), ""), K.side_exalt("s", "crítico e cast speed", "crit and cast speed")],
  lux=[K.side_exalt("p", "spell damage T1", "T1 spell damage"), K.divine]),
 "focus": dict(
  base=L("Tasalian Focus → Runed Focus.", "Tasalian Focus → Runed Focus."),
  targets=[[X, "+2 to Level of all Spell Skills", 41], [P, "(75–89)% increased Spell Damage", 60], [P, "+(81–90) to maximum Energy Shield", 70], [X, "(54–59)% increased Critical Hit Chance for Spells", 59]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Focus · +# to Level of all Spell Skills · increased Spell Damage", "", "")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Transmutation/Augmentation até + spells e spell damage → Regal.", "Transmutation/Augmentation until + spells and spell damage → Regal."), ""), K.side_exalt("s", "crítico de spell", "spell crit")],
  lux=[K.side_exalt("p", "ES", "ES"), K.divine]),
 "helmet": dict(
  base=L("Ancestral/Sorcerous Tiara → Kamasan Tiara.", "Ancestral/Sorcerous Tiara → Kamasan Tiara."),
  targets=[[P, "(92–100)% increased Energy Shield", 65], [P, "+(150–174) to maximum Life", 65], [X, "+(41–45)% to Fire Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Armourer's Scrap", "Distilled Emotions"],
  cheap=[K.trade("Helmet (ES) · Energy Shield · Life · Resistances", "", "")],
  value=[S(L("Defesa no Magic", "Defence on the Magic item"), L("Transmutation/Augmentation até % ES ou vida → Regal.", "Transmutation/Augmentation until % ES or life → Regal."), ""), K.side_exalt("s", "resistências", "resistances"), K.quality("Armourer's Scrap", "")],
  lux=[S(L("Kamasan Tiara com anoint", "Anointed Kamasan Tiara"), L("A versão cara usa Kamasan Tiara com anoint (Distilled Emotions) e Soul Cores.", "The expensive version uses an anointed Kamasan Tiara (Distilled Emotions) and Soul Cores."), ""), K.divine]),
 "gloves": dict(
  base=L("Luvas de Inteligência; Maligaro's Virtuosity no começo.", "Intelligence gloves; Maligaro's Virtuosity early."),
  targets=[[P, "+(48–60) to maximum Energy Shield", 54], [P, "(39–42)% increased Energy Shield + (42–49) to maximum Life", 78], [X, "(30–34)% increased Critical Damage Bonus", 59]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation", "Armourer's Scrap"],
  cheap=[K.trade("Maligaro's Virtuosity", "Unique barata no poe.ninja.", "Cheap unique on poe.ninja.")],
  value=[S(L("Rare de ES", "Rare ES gloves"), L("Transmutation/Augmentation até ES → Regal → Exalted com Omen de sufixo para dano crítico/resist.", "Transmutation/Augmentation until ES → Regal → suffix-Omen Exalted for crit damage/resist."), ""), K.quality("Armourer's Scrap", "")],
  lux=[K.runeforge("Sirenscale Gloves", "Verisium"), K.divine]),
 "boots": dict(
  base="Lattice/Dunerunner Sandals", targets=[[P, "30% increased Movement Speed (T1 35%)", "65 (82)"], [P, "+(48–60) to maximum Energy Shield", 54], [X, "+(41–45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Boots · Movement Speed ≥ 25 · Resistances", "", "")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Sandals brancas → Transmutation/Augmentation até Movement Speed → Regal.", "White sandals → Transmutation/Augmentation until Movement Speed → Regal."), ""), K.side_exalt("s", "resistências", "resistances")],
  lux=[S("Decree of Flight", L("Setup CoA: dodge mais rápido e Guard no dodge.", "CoA setup: faster dodge and Guard on dodge."), ""), K.divine]),
 "amulet": dict(
  base=L("Solar Amulet (Spirit) ou Lapis/Gold.", "Solar Amulet (Spirit) or Lapis/Gold."),
  targets=[[X, "(22–24)% of Damage taken Recouped as Life", 79], [X, "+3 to Level of all Spell Skills", 75], [P, "+(47–50) to Spirit", 54]],
  mats=["Chaos Orb", "Orb of Annulment", "Exalted Orb", "Omen of Dextral Exaltation", "Omen of Dextral Erasure"],
  cheap=[K.trade("Amulet · % of Damage taken Recouped as Life", "Filtre SEM mana.", "Filter out mana.")],
  value=[S(L("Recoup no sufixo", "Recoup on the suffix"), L("Amuleto com um bom prefixo (Spirit/ES) → Exalted com Omen de sufixo até o recoup como vida.", "Amulet with a good prefix (Spirit/ES) → suffix-Omen Exalted until recoup as life."), L("Veio mana/lixo: Omen of Dextral Erasure + Annulment e tente de novo.", "Rolled mana/junk: Omen of Dextral Erasure + Annulment and try again."))],
  lux=[K.side_exalt("s", "+3 spells", "+3 spells"), K.divine]),
 "rings": dict(
  base=L("Prismatic Ring → Snakepit.", "Prismatic Ring → Snakepit."), targets=[[X, "+(15–16)% to all Elemental Resistances", 68], [X, "(22–24)% increased Cast Speed", 60]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Ring · Resistances · increased Cast Speed", "", "")], value=[K.side_exalt("s", "resistências e cast speed", "resistances and cast speed")],
  lux=[S("Snakepit", L("Anel ESQUERDO para a versão Low Life.", "LEFT ring for the Low Life version."), "")]),
 "belt": dict(
  base="Heavy Belt", targets=[[C, "Perfect Essence of Insulation: (26–30)% of Fire Damage taken Recouped as Life", 72], [P, "+(150–174) to maximum Life", 65]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Perfect Essence of Insulation"],
  cheap=[K.trade("Belt · Life · Resistances", "", "")],
  value=[S(L("Perfect Essence of Insulation", "Perfect Essence of Insulation"), L("Num cinto rare com vida, a Perfect Essence of Insulation troca um mod aleatório por 26–30% do dano de FOGO recuperado como vida — exatamente o dano do Pyromantic Pact e do Grinning Immolation.", "On a rare belt with life, Perfect Essence of Insulation swaps a random mod for 26–30% of FIRE damage recouped as life — exactly the damage from Pyromantic Pact and Grinning Immolation."), L("Levou a vida: Exalted de novo.", "It removed the life: Exalted again."))],
  lux=[S("Coward's Legacy · Mageblood", L("Low Life e CoA.", "Low Life and CoA."), "")]),
 "flask": dict(
  base="Ultimate Life Flask", targets=[[P, "(76–80)% increased Amount Recovered", 83]], mats=["Orb of Transmutation", "Orb of Augmentation", "Glassblower's Bauble"],
  cheap=[S(L("Leveling", "Leveling"), L("Transmutation/Augmentation: recuperação alta.", "Transmutation/Augmentation: high recovery."), "")],
  value=[S("Blood of the Warrior", L("Recoup durante o efeito, sem sair com a vida cheia.", "Recoup during the effect, not removed at full life."), "")],
  lux=[S(L("Qualidade", "Quality"), L("Glassblower's Bauble até 20%.", "Glassblower's Bauble up to 20%."), "")]),
 "charms": dict(
  base=L("Thawing, Dousing e Golden Charm.", "Thawing, Dousing and Golden Charm."), targets=[[P, "Charges / duration", 60]], mats=["Orb of Transmutation", "Orb of Augmentation"],
  cheap=[S(L("Charms normais", "Normal charms"), L("Freeze e Ignite.", "Freeze and Ignite."), "")], value=[S("Beira's Anguish", L("Chão em chamas que ignita.", "Burning ground that ignites."), "")],
  lux=[S("Rite of Passage · For Utopia", L("Setup CoA.", "CoA setup."), "")]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
