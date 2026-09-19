# -*- coding: utf-8 -*-
# Oficina de crafting do Whirling Glacial Bolt (executado dentro de bdata.py: usa L, BOOK). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
# Enxuta de propósito: as peças em que vale gastar currency (a besta e três peças de Armour); body, botas de leveling e cintos são unique.
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("crossbow", L("Besta", "Crossbow"), "Crossbows", L("Dano elemental adicionado, + níveis de Attack e velocidade: é o dano do Glacial Bolt.", "Added elemental damage, + Attack levels and speed: it's Glacial Bolt's damage."),
        L("Base branca do vendor; no endgame, Desolate Crossbow ilvl 82.", "White vendor base; in endgame, ilvl 82 Desolate Crossbow."),
        L("Pare com + níveis de Attack (ou dois dano adicionado fortes) e velocidade.", "Stop once you have + Attack levels (or two strong added damages) and speed."),
        L("Do 1 ao 75 a arma é a Rampart Raptor: não gaste currency em besta antes do 79.", "From 1 to 75 the weapon is the Rampart Raptor: don't spend currency on a crossbow before 79."),
        ["Adds .* Cold Damage$", "Adds .* Lightning Damage$", "Adds .* Fire Damage$", "Elemental Damage with Attacks", "increased Attack Speed", "increased Physical Damage$"], ["Rampart Raptor"]),
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_str", L("Vida, Armour e resistência a frio.", "Life, Armour and cold resistance."), L("Base de Armour (Força), ilvl 82.", "Armour (Strength) base, ilvl 82."),
        L("Vida + Armour + duas resistências.", "Life + Armour + two resistances."), L("Armour aplicada a dano elemental é sufixo e disputa com resistência.", "Armour applied to elemental damage is a suffix and competes with resistance."),
        ["to maximum Life$", "increased Armour$", "Armour also applies", "Cold Resistance", "Fire Resistance"], ["Thrillsteel"]),
 K.item("gloves", L("Luvas", "Gloves"), "Gloves_str", L("Vida, Armour e dano de frio adicionado.", "Life, Armour and added cold damage."), L("Base de Armour, ilvl 78+.", "Armour base, ilvl 78+."),
        L("Vida + Armour + resistência a caos.", "Life + Armour + chaos resistance."), L("NUNCA aceite 'chance de projétil extra': o autor diz que está bugado.", "NEVER accept 'chance for an extra projectile': the author says it's bugged."),
        ["to maximum Life$", "increased Armour$", "Adds .* Cold damage to Attacks", "Resistance"]),
 K.item("boots", L("Botas", "Boots"), "Boots_str", L("Movimento primeiro, depois vida e Armour aplicada a elemental.", "Movement first, then life and Armour applied to elemental."), L("Base de Armour ilvl 82 para 35%.", "ilvl 82 Armour base for 35%."),
        L("30%+ de movimento e vida.", "30%+ movement and life."), L("35% só existe em ilvl 82.", "35% only exists at ilvl 82."), ["Movement Speed", "to maximum Life$", "Armour also applies", "Resistance"], ["Wanderlust"]),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("Spirit para as reservas + nível de projétil.", "Spirit for the reservations + projectile level."), L("Absent Amulet ou base com Spirit, ilvl 75+.", "Absent Amulet or a Spirit base, ilvl 75+."),
        L("Spirit alto + vida; + nível de projéteis é luxo.", "High Spirit + life; + projectile levels are luxury."), L("A Trinity do PoB vem do Viper Heart (Spirit alto, caro): antes dele, pague as reservas com Morior Invictus.", "The PoB's Trinity comes from Viper Heart (high Spirit, expensive): before it, pay for the reservations with Morior Invictus."),
        ["to Spirit$", "Level of all Projectile", "increased Armour$", "maximum Life"], ["Viper Heart"]),
]
CK_DETAIL = {
 "crossbow": dict(
  base=L("Besta branca ilvl 82 (Desolate Crossbow no PoB).", "White ilvl 82 crossbow (Desolate Crossbow in the PoB)."),
  targets=[[P, "Adds (112–124) to (168–189) Cold Damage", 81], [P, "Adds (135–156) to (205–236) Fire Damage", 81], [P, "Adds (1–19) to (310–358) Lightning Damage", 81], [P, "(120–139)% increased Elemental Damage with Attacks", 81], [X, "(17–19)% increased Attack Speed", 37]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Perfect Essence of Battle", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Artificer's Orb", "Blacksmith's Whetstone"],
  cheap=[K.trade("Crossbow · “+# to Level of all Attack Skills” · Adds Cold/Fire/Lightning · Attack Speed", "No trade uma rare pronta costuma sair barata.", "On trade a finished rare is usually cheap.")],
  value=[S(L("Magic com um mod bom", "Magic with one good mod"), L("Base branca → Transmutation + Augmentation até dano elemental adicionado ou velocidade.", "White base → Transmutation + Augmentation until added elemental damage or speed."), ""),
         S(L("Rare com Regal", "Rare with Regal"), L("Regal Orb mantém os mods e adiciona um.", "A Regal Orb keeps the mods and adds one."), ""),
         K.side_exalt("p", "dano elemental adicionado", "added elemental damage"), K.side_exalt("s", "velocidade de ataque", "attack speed"), K.quality("Blacksmith's Whetstone", "")],
  lux=[S(L("Perfect Essence of Battle (se faltar nível)", "Perfect Essence of Battle (if levels are missing)"), L("Num Rare, remove um mod aleatório e adiciona +3 níveis de Attack. Ocupa o único mod crafted.", "On a Rare, removes a random modifier and adds +3 Attack levels. It takes the only crafted mod."), ""), K.divine]),
 "helmet": dict(
  base=L("Capacete de Armour (Força) ilvl 82.", "ilvl 82 Armour (Strength) helmet."),
  targets=[[P, "(92–100)% increased Armour", 65], [P, "+(150–174) to maximum Life", 65], [X, "+(41–45)% Cold Resistance", 82], [X, "+(38–43)% of Armour also applies to Elemental Damage", 66]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Armourer's Scrap"],
  cheap=[K.trade("Helmet (Armour) · Life ≥ 100 · Total Resistance ≥ 60")],
  value=[S(L("Vida e Armour no Magic", "Life and Armour on the Magic item"), L("Base branca → Transmutation/Augmentation até vida ou % Armour → Regal.", "White base → Transmutation/Augmentation until life or % Armour → Regal."), ""), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.divine]),
 "gloves": dict(
  base=L("Luvas de Armour ilvl 78+.", "ilvl 78+ Armour gloves."),
  targets=[[P, "+(120–149) to maximum Life", 60], [P, "(92–100)% increased Armour", 65], [P, "Adds (21–24) to (32–37) Cold damage to Attacks", 75], [X, "+(41–45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Gloves (Armour) · Life ≥ 80 · Adds Cold to Attacks")],
  value=[S(L("Vida primeiro", "Life first"), L("Transmutation/Augmentation até vida → Regal.", "Transmutation/Augmentation until life → Regal."), ""), K.side_exalt("p", "Armour e dano de frio adicionado", "Armour and added cold damage"), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.divine]),
 "boots": dict(
  base=L("Botas de Armour ilvl 82 (35% de movimento).", "ilvl 82 Armour boots (35% movement)."),
  targets=[[P, "35% increased Movement Speed (T2 30%)", "82 (65)"], [P, "+(120–149) to maximum Life", 60], [X, "+(41–45)% Resistance", 82], [X, "+(38–43)% of Armour also applies to Elemental Damage", 66]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Essence of Hysteria", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Boots (Armour) · Movement Speed ≥ 25 · Life ≥ 60")],
  value=[S(L("Movimento no Magic", "Movement on the Magic item"), L("Base branca ilvl 82 → Transmutation/Augmentation até Movement Speed → Regal.", "White ilvl 82 base → Transmutation/Augmentation until Movement Speed → Regal."), L("Garantido: Essence of Hysteria num Rare (30% MS).", "Guaranteed: Essence of Hysteria on a Rare (30% MS).")), K.side_exalt("s", "resistências e vida", "resistances and life")],
  lux=[K.divine]),
 "amulet": dict(
  base=L("Absent Amulet (implícito de Spirit) ilvl 75+.", "Absent Amulet (Spirit implicit) ilvl 75+."),
  targets=[[P, "+(47–50) to Spirit", 54], [X, "+3 to Level of all Projectile Skills (T2 +2)", "75 (41)"], [P, "(45–50)% increased Armour", 75]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Greater Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Divine Orb"],
  cheap=[K.trade("Amulet · “+# to Spirit” ≥ 40 · Life", "Spirit é o que paga as reservas.", "Spirit is what pays for the reservations.")],
  value=[S(L("Spirit no Magic", "Spirit on the Magic item"), L("Base branca → Transmutation/Augmentation até Spirit (prefixo) → Regal.", "White base → Transmutation/Augmentation until Spirit (prefix) → Regal."), ""), K.side_exalt("s", "+ nível de projéteis", "+ projectile levels")],
  lux=[K.divine]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
