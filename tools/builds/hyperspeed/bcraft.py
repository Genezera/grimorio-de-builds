# -*- coding: utf-8 -*-
# Oficina de crafting do Hyper Speed Monk (executado dentro de bdata.py: usa L, BOOK). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
# Enxuta de propósito: as peças em que vale gastar currency (capacete, corpo, luvas, botas e amuleto de Evasion/ES); anéis, cinto e charms são unique ou rare de troca.
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_dex_int", L("Energy Shield alto (450–500+), chance de crítico e resistências: cada 10 de ES no equipamento dá +0,1% de chance de crítico.", "High Energy Shield (450–500+), crit chance and resistances: every 10 ES on your gear gives +0.1% crit chance."),
        L("Base de Evasion/ES (Dex/Int), ilvl 80+ (Ancestral Tiara no guia do autor).", "Evasion/ES (Dex/Int) base, ilvl 80+ (Ancestral Tiara in the author's guide)."),
        L("ES acima de 450 + chance de crítico + duas resistências.", "ES above 450 + crit chance + two resistances."), L("Até o Waystones (80) o capacete pode ser vida e resistência.", "Until Waystones (80) the helmet can be life and resistance."),
        ["to maximum Energy Shield$", "increased Energy Shield$", "Critical Hit Chance", "Resistance"], []),
 K.item("body", L("Corpo", "Body Armour"), "Body_Armours_dex_int", L("Evasion máxima (a velocidade do Hollow Palm), ES para o crítico e a defesa, resistências.", "Maximum Evasion (Hollow Palm's speed), ES for crit and defence, resistances."),
        L("Base Dex/Int com muita Evasion, ilvl 65+ (Sleek Jacket no guia do autor).", "Dex/Int base with lots of Evasion, ilvl 65+ (Sleek Jacket in the author's guide)."),
        L("1400–1500 de Evasion e uns 500 de ES; resistências no cap.", "1400–1500 Evasion and about 500 ES; resistances capped."), L("Deflection Rating ou 'faster start of Energy Shield Recharge' por último.", "Deflection Rating or 'faster start of Energy Shield Recharge' last."),
        ["increased Evasion and Energy Shield", "to Evasion Rating$", "to maximum Energy Shield$", "Deflection Rating", "faster start of Energy Shield Recharge", "Resistance"], []),
 K.item("gloves", L("Luvas", "Gloves"), "Gloves_dex_int", L("Com o Way of the Stonefist viram Fists of Stone: dano adicionado alto, Evasion e velocidade.", "With Way of the Stonefist they become Fists of Stone: high added damage, Evasion and speed."),
        L("Base Dex/Int, ilvl 70+ (Opulent Gloves no guia do autor).", "Dex/Int base, ilvl 70+ (Opulent Gloves in the author's guide)."),
        L("DOIS danos adicionados de tier alto + Evasion flat.", "TWO high-tier added damage mods + flat Evasion."), L("Velocidade de cast com a vida cheia vira velocidade de ataque; Dexterity dá chance de projétil extra.", "Cast speed on Full Life becomes attack speed; Dexterity gives a chance for an extra projectile."),
        ["Adds .* Damage to Attacks", "to Evasion Rating$", "Cast Speed", "to Dexterity", "Level of all Melee"], []),
 K.item("boots", L("Botas", "Boots"), "Boots_dex_int", L("Deflection Rating primeiro, depois Evasion e ES altos e resistências; o movimento pesa pouco.", "Deflection Rating first, then high Evasion and ES and resistances; movement matters little."),
        L("Base Dex/Int, ilvl 80 (Sekhema Sandals ou Daggerfoot Shoes no guia do autor).", "Dex/Int base, ilvl 80 (Sekhema Sandals or Daggerfoot Shoes in the author's guide)."),
        L("Deflection + Evasion/ES + duas resistências.", "Deflection + Evasion/ES + two resistances."), L("Você se move com o Tempest Flurry: 35% de movimento só se sobrar mod.", "You move with Tempest Flurry: 35% movement only if you have a mod to spare."),
        ["Deflection Rating", "increased Evasion and Energy Shield", "Movement Speed", "Resistance"], []),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("+níveis de Melee (o maior ganho de dano da build) e defesas.", "+ Melee levels (the build's biggest damage gain) and defences."),
        L("Amber Amulet ou Absent Amulet (com Trinity), ilvl 50+.", "Amber Amulet or Absent Amulet (with Trinity), ilvl 50+."),
        L("+3 níveis de Melee (4 com o craft de Breach) + Evasion/ES.", "+3 Melee levels (4 with the Breach craft) + Evasion/ES."), L("Instill: Stimulants (com Lavianga's Spirits) ou Subterfuge Mask.", "Instill: Stimulants (with Lavianga's Spirits) or Subterfuge Mask."),
        ["Level of all Melee", "Critical Hit Chance", "Critical Damage Bonus", "increased Evasion", "maximum Energy Shield"], []),
]
CK_DETAIL = {
 "helmet": dict(
  base=L("Capacete Dex/Int ilvl 80+ (Ancestral Tiara).", "ilvl 80+ Dex/Int helmet (Ancestral Tiara)."),
  targets=[[P, "(92–100)% increased Evasion and Energy Shield", 65], [P, "+(79–94) to Evasion Rating / +(26–29) to maximum Energy Shield", 54], [X, "(30–34)% increased Critical Hit Chance", 58], [X, "+(41–45)% to Cold Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Armourer's Scrap"],
  cheap=[K.trade("Helmet (Evasion/ES) · Energy Shield ≥ 350 · Total Resistance ≥ 60")],
  value=[S(L("ES no Magic", "ES on the Magic item"), L("Base branca → Transmutation/Augmentation até Energy Shield → Regal.", "White base → Transmutation/Augmentation until Energy Shield → Regal."), ""), K.side_exalt("s", "chance de crítico e resistências", "crit chance and resistances")],
  lux=[K.divine]),
 "body": dict(
  base=L("Corpo Dex/Int ilvl 65+ (Sleek Jacket).", "ilvl 65+ Dex/Int body armour (Sleek Jacket)."),
  targets=[[P, "(101–110)% increased Evasion and Energy Shield", 75], [P, "+(142–161) to Evasion Rating / +(43–48) to maximum Energy Shield", 75], [X, "Gain Deflection Rating equal to (24–26)% of Evasion Rating", 81], [X, "+(41–45)% to Fire Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Armourer's Scrap"],
  cheap=[K.trade("Body Armour (Evasion/ES) · Evasion ≥ 1200 · Energy Shield ≥ 300")],
  value=[S(L("% Evasion/ES no Magic", "% Evasion/ES on the Magic item"), L("Base branca → Transmutation/Augmentation até % Evasion e ES → Regal.", "White base → Transmutation/Augmentation until % Evasion and ES → Regal."), ""), K.side_exalt("p", "Evasion e ES flat", "flat Evasion and ES"), K.side_exalt("s", "resistências e Deflection", "resistances and Deflection")],
  lux=[K.divine]),
 "gloves": dict(
  base=L("Luvas Dex/Int ilvl 70+ (Opulent Gloves).", "ilvl 70+ Dex/Int gloves (Opulent Gloves)."),
  targets=[[P, "Adds (21–24) to (32–37) Cold damage to Attacks", 75], [P, "Adds (1–4) to (60–71) Lightning damage to Attacks", 75], [X, "+(34–36) to Dexterity", 81]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Gloves (Evasion/ES) · Adds damage to Attacks (2 mods)")],
  value=[S(L("Dano adicionado primeiro", "Added damage first"), L("Transmutation/Augmentation até um dano adicionado → Regal → segundo dano.", "Transmutation/Augmentation until one added damage mod → Regal → the second damage."), ""), K.side_exalt("p", "dano adicionado e Evasion", "added damage and Evasion")],
  lux=[K.divine]),
 "boots": dict(
  base=L("Botas Dex/Int ilvl 80 (Sekhema Sandals / Daggerfoot Shoes).", "ilvl 80 Dex/Int boots (Sekhema Sandals / Daggerfoot Shoes)."),
  targets=[[X, "Gain Deflection Rating equal to (21–23)% of Evasion Rating", 66], [P, "(92–100)% increased Evasion and Energy Shield", 65], [X, "+(41–45)% to Fire Resistance", 82], [X, "+(41–45)% to Lightning Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Boots (Evasion/ES) · Deflection Rating · Total Resistance ≥ 60")],
  value=[S(L("Deflection no Magic", "Deflection on the Magic item"), L("Base branca → Transmutation/Augmentation até Deflection ou % Evasion/ES → Regal.", "White base → Transmutation/Augmentation until Deflection or % Evasion/ES → Regal."), ""), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.divine]),
 "amulet": dict(
  base=L("Absent Amulet / Amber Amulet ilvl 50+.", "Absent Amulet / Amber Amulet ilvl 50+."),
  targets=[[X, "+3 to Level of all Melee Skills (T2 +2)", "75 (41)"], [X, "(35–38)% increased Critical Hit Chance", 72], [X, "(35–39)% increased Critical Damage Bonus", 74], [P, "(45–50)% increased Evasion Rating", 77]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Greater Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Divine Orb"],
  cheap=[K.trade("Amulet · “+# to Level of all Melee Skills” · Evasion", "O maior ganho de dano da build.", "The build's biggest damage gain.")],
  value=[S(L("Crítico e Evasion no Magic", "Crit and Evasion on the Magic item"), L("Base branca → Transmutation/Augmentation até chance de crítico ou Evasion → Regal.", "White base → Transmutation/Augmentation until crit chance or Evasion → Regal."), ""), K.side_exalt("s", "+ níveis de Melee", "+ Melee levels")],
  lux=[K.divine]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
