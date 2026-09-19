# -*- coding: utf-8 -*-
# Oficina de crafting do Tornado da Lança (executado dentro de bdata.py: usa L, BOOK). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
# Enxuta de propósito: as peças em que vale gastar currency (a besta e três peças de Armour); body, botas de leveling e cintos são unique.
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("spear", L("Spear", "Spear"), "Spears", L("Dano elemental adicionado e velocidade: é o dano do Twister e da Whirling Slash.", "Added elemental damage and speed: it's the damage of Twister and Whirling Slash."),
        L("Base branca do vendor; no endgame, Soaring Spear ilvl 82 (Set 1) e Akoyan Spear (Set 2).", "White vendor base; in endgame, ilvl 82 Soaring Spear (Set 1) and Akoyan Spear (Set 2)."),
        L("Pare com dano elemental adicionado alto (fogo, frio ou raio) e velocidade de ataque.", "Stop once you have high added elemental damage (fire, cold or lightning) and attack speed."),
        L("Do 16 ao ~60 a Skysliver dispensa craft: não gaste currency em spear antes do 70.", "From 16 to ~60 Skysliver needs no craft: don't spend currency on a spear before 70."),
        ["Adds .* Cold Damage$", "Adds .* Lightning Damage$", "Adds .* Fire Damage$", "Elemental Damage with Attacks", "increased Attack Speed", "Critical Hit Chance", "Critical Damage Bonus"], ["Skysliver"]),
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_dex_int", L("Vida, Evasion/ES e resistências.", "Life, Evasion/ES and resistances."), L("Base de Evasion/ES (Dex/Int), ilvl 80+ (Ancestral Tiara no PoB).", "Evasion/ES (Dex/Int) base, ilvl 80+ (Ancestral Tiara in the PoB)."),
        L("Vida + Evasion/ES + duas resistências.", "Life + Evasion/ES + two resistances."), L("Do 1 ao 26 o capacete é Str: use o do vendor e a Thrillsteel no 27.", "From 1 to 26 the helmet is Str: use a vendor one and Thrillsteel at 27."),
        ["to maximum Life$", "increased Evasion and Energy Shield", "Deflection Rating", "Resistance"], ["Thrillsteel"]),
 K.item("gloves", L("Luvas", "Gloves"), "Gloves_dex_int", L("Vida, Evasion/ES e dano adicionado a ataques.", "Life, Evasion/ES and added attack damage."), L("Base Dex/Int, ilvl 78+ (Secured Wraps no PoB).", "Dex/Int base, ilvl 78+ (Secured Wraps in the PoB)."),
        L("Vida + Evasion/ES + resistência a caos.", "Life + Evasion/ES + chaos resistance."), L("NUNCA aceite 'chance de projétil extra': está bugada.", "NEVER accept 'chance for an extra projectile': it's bugged."),
        ["to maximum Life$", "increased Evasion and Energy Shield", "Adds .* Damage to Attacks", "Resistance"]),
 K.item("boots", L("Botas", "Boots"), "Boots_dex_int", L("Movimento primeiro, depois vida e Evasion/ES.", "Movement first, then life and Evasion/ES."), L("Base Dex/Int ilvl 82 para 35% (Daggerfoot Shoes no PoB).", "ilvl 82 Dex/Int base for 35% (Daggerfoot Shoes in the PoB)."),
        L("30%+ de movimento e vida.", "30%+ movement and life."), L("35% só existe em ilvl 82.", "35% only exists at ilvl 82."), ["Movement Speed", "to maximum Life$", "increased Evasion and Energy Shield", "Resistance"], ["Wanderlust"]),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("Spirit para as reservas + nível de projétil.", "Spirit for the reservations + projectile level."), L("Absent Amulet (implícito de Spirit) ilvl 75+.", "Absent Amulet (Spirit implicit) ilvl 75+."),
        L("Spirit alto + vida; +3 de projétil é o sonho.", "High Spirit + life; +3 projectile is the dream."), L("Gale Gorget no PoB: +3 de projétil, +50 de Spirit e Cast on Critical de brinde.", "Gale Gorget in the PoB: +3 projectile, +50 Spirit and a free Cast on Critical."),
        ["to Spirit$", "Level of all Projectile", "increased Armour", "maximum Life"], []),
]
CK_DETAIL = {
 "spear": dict(
  base=L("Spear branca ilvl 82 (Soaring Spear no PoB).", "White ilvl 82 spear (Soaring Spear in the PoB)."),
  targets=[[P, "Adds (88–101) to (133–154) Fire Damage", 81], [P, "Adds (72–81) to (110–123) Cold Damage", 81], [P, "Adds (1–12) to (202–234) Lightning Damage", 81], [P, "(87–100)% increased Elemental Damage with Attacks", 81], [X, "(26–28)% increased Attack Speed", 77], [X, "+(4.41–5)% to Critical Hit Chance", 73]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Artificer's Orb", "Blacksmith's Whetstone"],
  cheap=[K.trade("Spear · Adds Cold/Fire/Lightning · Attack Speed", "No trade uma rare pronta costuma sair barata.", "On trade a finished rare is usually cheap.")],
  value=[S(L("Magic com um mod bom", "Magic with one good mod"), L("Base branca → Transmutation + Augmentation até dano elemental adicionado ou velocidade.", "White base → Transmutation + Augmentation until added elemental damage or speed."), ""),
         S(L("Rare com Regal", "Rare with Regal"), L("Regal Orb mantém os mods e adiciona um.", "A Regal Orb keeps the mods and adds one."), ""),
         K.side_exalt("p", "dano elemental adicionado", "added elemental damage"), K.side_exalt("s", "velocidade de ataque", "attack speed"), K.quality("Blacksmith's Whetstone", "")],
  lux=[K.divine]),
 "helmet": dict(
  base=L("Capacete Dex/Int ilvl 80+ (Ancestral Tiara).", "ilvl 80+ Dex/Int helmet (Ancestral Tiara)."),
  targets=[[P, "+(150–174) to maximum Life", 65], [P, "(92–100)% increased Evasion and Energy Shield", 65], [X, "+(41–45)% to Cold Resistance", 82], [X, "+(41–45)% to Lightning Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Armourer's Scrap"],
  cheap=[K.trade("Helmet (Evasion/ES) · Life ≥ 100 · Total Resistance ≥ 60")],
  value=[S(L("Vida e Evasion/ES no Magic", "Life and Evasion/ES on the Magic item"), L("Base branca → Transmutation/Augmentation até vida ou % Evasion/ES → Regal.", "White base → Transmutation/Augmentation until life or % Evasion/ES → Regal."), ""), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.divine]),
 "gloves": dict(
  base=L("Luvas Dex/Int ilvl 78+ (Secured Wraps).", "ilvl 78+ Dex/Int gloves (Secured Wraps)."),
  targets=[[P, "+(120–149) to maximum Life", 60], [P, "(92–100)% increased Evasion and Energy Shield", 65], [P, "Adds (21–24) to (32–37) Cold damage to Attacks", 75], [X, "+(41–45)% to Fire Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Gloves (Evasion/ES) · Life ≥ 80 · Adds damage to Attacks")],
  value=[S(L("Vida primeiro", "Life first"), L("Transmutation/Augmentation até vida → Regal.", "Transmutation/Augmentation until life → Regal."), ""), K.side_exalt("p", "Evasion/ES e dano adicionado", "Evasion/ES and added damage"), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.divine]),
 "boots": dict(
  base=L("Botas Dex/Int ilvl 82 (35% de movimento).", "ilvl 82 Dex/Int boots (35% movement)."),
  targets=[[P, "35% increased Movement Speed", 82], [P, "+(120–149) to maximum Life", 60], [X, "+(41–45)% to Fire Resistance", 82], [X, "+(41–45)% to Cold Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Essence of Hysteria", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Boots (Evasion/ES) · Movement Speed ≥ 25 · Life ≥ 60")],
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
