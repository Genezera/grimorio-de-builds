# -*- coding: utf-8 -*-
# Oficina de crafting do Martial Artist Oil Barrage (executado dentro de bdata.py). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("talisman", "Talisman", "Talismans", L("Fogo, frio e raio planos, % elemental com ataques, crítico e + níveis.", "Flat fire, cold and lightning, % elemental attack damage, crit and + levels."), L("Spiny Talisman (crítico base alto).", "Spiny Talisman (high base crit)."), L("300+ EDPS para a troca; 490+ com 15% de crítico no endgame.", "300+ EDPS for the swap; 490+ with 15% crit in endgame."), L("'+ nível de skills Melee' não afeta o Oil Barrage (é projétil): o nível vem da Perfect Essence of Battle (+3 ataques).", "'+ Melee skill levels' doesn't affect Oil Barrage (it's a projectile): levels come from Perfect Essence of Battle (+3 attacks)."), ["Adds .* (Fire|Cold|Lightning) Damage$", "Elemental Damage with Attacks", "Critical Hit Chance", "Attack Speed"]),
 K.item("gloves", L("Luvas (Fists of Stone)", "Gloves (Fists of Stone)"), "Gloves_dex_int", L("Dano crítico, attack speed, dano plano e defesa — o Way of the Stonefist transforma cada um.", "Crit damage, attack speed, flat damage and defence — Way of the Stonefist transforms each one."), L("Qualquer base: a ascendência troca por Fists of Stone.", "Any base: the ascendancy turns it into Fists of Stone."), L("Dano crítico + attack speed.", "Crit damage + attack speed."), L("Sem Runeforge na Verisium Anvil não há Runic Ward para a Refutation.", "Without Runeforging at the Verisium Anvil there's no Runic Ward for Refutation."), ["Critical Damage Bonus", "Attack Speed", "Adds .* damage to Attacks", "Evasion and Energy Shield$"]),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("Spirit, + projéteis, crítico e ES.", "Spirit, + projectiles, crit and ES."), L("Rare com Spirit → Absent Amulet.", "Rare with Spirit → Absent Amulet."), L("+47–50 Spirit + um mod de dano.", "+47–50 Spirit + a damage mod."), L("Instill Thaumaturgic Generator (carga aleatória periódica).", "Thaumaturgic Generator instill (periodic random charge)."), ["to Spirit$", "Level of all Projectile", "Critical Hit Chance$"]),
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_int", L("ES alto e vida.", "High ES and life."), "Ancestral Tiara", L("% ES + ES plano.", "% ES + flat ES."), L("Myris Uxor e Alpha's Howl costumam ser melhores até o endgame.", "Myris Uxor and Alpha's Howl are usually better until endgame."), ["increased Energy Shield$", "to maximum Energy Shield$", "to maximum Life$"], ["Myris Uxor", "Alpha's Howl"]),
 K.item("body", "Body Armour", "Body_Armours_dex_int", L("Evasão/ES e Spirit.", "Evasion/ES and Spirit."), L("Forgotten Warden; Sleek Jacket com Spirit para a versão de mapa.", "Forgotten Warden; Sleek Jacket with Spirit for the mapping version."), L("% Evasão/ES + Spirit.", "% Evasion/ES + Spirit."), L("Spirit no peito libera Wind Dancer/Ghost Dance junto do Cast on Critical.", "Chest Spirit fits Wind Dancer/Ghost Dance alongside Cast on Critical."), ["to Spirit$", "Evasion and Energy Shield$"], ["Forgotten Warden"]),
 K.item("boots", L("Botas", "Boots"), "Boots_dex_int", L("35% Movement Speed, Evasão e resistências.", "35% Movement Speed, Evasion and resistances."), L("Drakeskin Boots / Wanderer Shoes.", "Drakeskin Boots / Wanderer Shoes."), L("30% MS + resistência.", "30% MS + resistance."), L("35% só em ilvl 82.", "35% only at ilvl 82."), ["Movement Speed", "Evasion and Energy Shield$", "Resistance$"]),
 K.item("rings", L("Anéis", "Rings"), "Rings", L("Dano plano em ataques, raridade e resistências.", "Flat attack damage, rarity and resistances."), L("Gold Ring (raridade implícita).", "Gold Ring (implicit rarity)."), L("Raio/físico plano + resistência.", "Flat lightning/physical + resistance."), L("Kalandra's Touch copia o outro anel: só vale com um anel muito bom.", "Kalandra's Touch copies the other ring: only worth it with a great ring."), ["Adds .* damage to Attacks", "Rarity", "Resistances$"], ["Kalandra's Touch"]),
 K.item("belt", L("Cinto", "Belt"), "Belts", L("Vida e resistências.", "Life and resistances."), "Utility Belt", L("Vida + duas resistências.", "Life + two resistances."), L("Ingenuity e Headhunter são as opções do planner.", "Ingenuity and Headhunter are the planner's options."), ["to maximum Life$", "Resistance$"], ["Ingenuity", "Headhunter"]),
 K.item("charms", "Charms", "Charms", L("Freeze, Stun e Power Charge.", "Freeze, Stun and Power Charge."), L("Thawing + Stone + Golden.", "Thawing + Stone + Golden."), L("Três gatilhos úteis.", "Three useful triggers."), L("Rite of Passage no Aspirational.", "Rite of Passage in Aspirational."), ["Charges", "Duration"], ["Nascent Hope", "Breath of the Mountains", "Rite of Passage"]),
]

CK_DETAIL = {
 "talisman": dict(
  base=L("Spiny Talisman; ilvl 81 para os T1 de dano plano.", "Spiny Talisman; ilvl 81 for T1 flat damage."),
  targets=[[P, "Adds (135–156) to (205–236) Fire Damage (T2 102–130 / 155–198)", "81 (75)"], [P, "Adds (112–124) to (168–189) Cold Damage", "81 (75)"], [P, "Adds (1–19) to (310–358) Lightning Damage", "81 (75)"],
           [X, "+(4.41–5)% to Critical Hit Chance", 73], [X, "(26–28)% increased Attack Speed", 77], [C, "Perfect Essence of Battle: +3 to Level of all Attack Skills", 72]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Perfect Essence of Battle", "Omen of Sinistral Exaltation", "Artificer's Orb", "Greater Iron Rune"],
  cheap=[K.trade("Talisman · Elemental DPS ≥ 300", "Ordene por EDPS; o site soma as runas.", "Sort by EDPS; the site includes runes.")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Base Normal → Transmutation/Augmentation até um dano elemental plano → Regal.", "Normal base → Transmutation/Augmentation until a flat elemental damage mod → Regal."), L("Nada de dano: próxima base (identifique todo Talisman rare).", "No damage: next base (identify every rare Talisman).")),
         K.side_exalt("p", "mais um dano elemental plano", "another flat elemental damage mod"),
         S("Perfect Essence of Battle", L("Com o item acima de 300 EDPS: +3 nível de todas as skills de ataque (inclui Oil Barrage).", "Once the item is above 300 EDPS: +3 to Level of all Attack Skills (includes Oil Barrage)."), L("Ocupa o mod crafted: sem Alloy depois.", "Takes the crafted mod: no Alloy afterwards."))],
  lux=[K.quality("Blacksmith's Whetstone", ""), K.divine]),
 "gloves": dict(
  base=L("Qualquer luva de Evasão/ES (vira Fists of Stone).", "Any Evasion/ES gloves (become Fists of Stone)."),
  targets=[[X, "(30–34)% increased Critical Damage Bonus", 59], [X, "(14–16)% increased Attack Speed", 60], [P, "Adds (1–4) to (60–71) Lightning damage to Attacks", 75], [P, "(92–100)% increased Evasion and Energy Shield", 65]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Gloves · Critical Damage Bonus · Attack Speed", "", "")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Transmutation/Augmentation até dano crítico ou attack speed → Regal.", "Transmutation/Augmentation until crit damage or attack speed → Regal."), ""), K.side_exalt("s", "attack speed / dano crítico", "attack speed / crit damage")],
  lux=[K.runeforge("Fists of Stone", "Verisium"), K.divine]),
 "amulet": dict(
  base=L("Rare com Spirit → Absent Amulet.", "Rare with Spirit → Absent Amulet."),
  targets=[[P, "+(47–50) to Spirit", 54], [X, "+3 to Level of all Projectile Skills", 75], [X, "(35–38)% increased Critical Hit Chance", 72]],
  mats=["Chaos Orb", "Exalted Orb", "Omen of Dextral Exaltation", "Distilled Emotions"],
  cheap=[K.trade("Amulet · to Spirit ≥ 40", "", "")],
  value=[K.side_exalt("s", "+ projéteis ou crítico", "+ projectiles or crit"), S(L("Instill", "Instill"), L("Thaumaturgic Generator: carga aleatória periódica.", "Thaumaturgic Generator: periodic random charge."), "")],
  lux=[S("Zarokh's Gift", L("Instill do Aspirational: socket de jewel extra (e Thaumaturgic Generator vai para o capacete).", "Aspirational instill: extra jewel socket (and Thaumaturgic Generator moves to the helmet)."), ""), K.divine]),
 "helmet": dict(
  base="Ancestral Tiara", targets=[[P, "(92–100)% increased Energy Shield", 65], [P, "+(61–73) to maximum Energy Shield", 60], [P, "+(150–174) to maximum Life", 65]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Raven-Touched Shard", "Armourer's Scrap"],
  cheap=[K.trade("Myris Uxor", "", ""), K.trade("Alpha's Howl", "", "")],
  value=[S(L("Defesa no Magic", "Defence on the Magic item"), L("Transmutation/Augmentation até % ES → Regal.", "Transmutation/Augmentation until % ES → Regal."), ""), K.side_exalt("p", "ES plano / vida", "flat ES / life")],
  lux=[S("Raven-Touched Shard", L("Augment do Aspirational.", "Aspirational augment."), ""), K.divine]),
 "body": dict(
  base=L("Forgotten Warden · Sleek Jacket", "Forgotten Warden · Sleek Jacket"), targets=[[P, "+(57–61) to Spirit (T2 54–56)", "78 (65)"], [P, "(101–110)% increased Evasion and Energy Shield", 75]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Armourer's Scrap", "Greater Iron Rune"],
  cheap=[K.trade("Forgotten Warden", "", "")],
  value=[S(L("Spirit no Magic", "Spirit on the Magic item"), L("Sleek Jacket: Transmutation/Augmentation até Spirit → Regal.", "Sleek Jacket: Transmutation/Augmentation until Spirit → Regal."), ""), K.side_exalt("p", "% Evasão/ES", "% Evasion/ES")],
  lux=[K.quality("Armourer's Scrap", ""), K.divine]),
 "boots": dict(
  base="Drakeskin Boots", targets=[[P, "35% increased Movement Speed (T2 30%)", "82 (65)"], [P, "(92–100)% increased Evasion and Energy Shield", 65], [X, "+(41–45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Farrul's Rune of the Chase"],
  cheap=[K.trade("Boots · Movement Speed ≥ 30 · Resistances", "", "")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Transmutation/Augmentation até Movement Speed → Regal.", "Transmutation/Augmentation until Movement Speed → Regal."), ""), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.divine]),
 "rings": dict(
  base="Gold Ring", targets=[[P, "Adds (1–4) to (60–71) Lightning damage to Attacks", 75], [P, "Adds (12–19) to (22–32) Physical Damage to Attacks", 75], [X, "+(15–16)% to all Elemental Resistances", 68]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation"],
  cheap=[K.trade("Ring · Adds Lightning Damage to Attacks · Resistances", "", "")],
  value=[K.side_exalt("p", "dano plano", "flat damage"), K.side_exalt("s", "resistências / raridade", "resistances / rarity")],
  lux=[S("Kalandra's Touch", L("Copia o anel oposto: combine com o melhor anel.", "Copies the opposite ring: pair it with your best ring."), ""), K.divine]),
 "belt": dict(
  base="Utility Belt", targets=[[P, "+(150–174) to maximum Life", 65], [X, "+(41–45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb"],
  cheap=[K.trade("Ingenuity", "", "")], value=[K.side_exalt("s", "resistências", "resistances")],
  lux=[S("Headhunter", L("Aspirational.", "Aspirational."), "")]),
 "charms": dict(
  base=L("Thawing, Stone e Golden Charm.", "Thawing, Stone and Golden Charm."), targets=[[P, "Charges / duration", 60]], mats=["Orb of Transmutation", "Orb of Augmentation"],
  cheap=[S(L("Charms normais", "Normal charms"), L("Freeze, Stun e rare/unique.", "Freeze, Stun and rare/unique."), "")], value=[S("Nascent Hope · Breath of the Mountains", L("ES e Power Charge.", "ES and Power Charge."), "")],
  lux=[S("Rite of Passage", L("Stag > Cat > Wolf.", "Stag > Cat > Wolf."), "")]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
