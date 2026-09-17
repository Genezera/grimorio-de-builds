# -*- coding: utf-8 -*-
# Oficina de crafting do Acolyte of Chayula (executado dentro de bdata.py). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("bow", L("Arco", "Bow"), "Bows", L("% físico, físico plano, + projéteis e flecha adicional.", "% physical, flat physical, + projectiles and additional arrow."), L("Splinterheart no leveling; Obliterator Bow nos mapas.", "Splinterheart while leveling; Obliterator Bow in maps."), L("Físico alto + um sufixo bom (projéteis ou flecha).", "High physical + one good suffix (projectiles or arrow)."), L("Dano elemental no arco não escala o veneno como o físico.", "Elemental damage on the bow doesn't scale poison like physical."), ["increased Physical Damage$", "Adds .* Physical Damage$", "Level of all Projectile", "additional Arrow"], ["Splinterheart"]),
 K.item("quiver", L("Aljava", "Quiver"), "Quivers", L("Dano plano (físico e raio), attack speed, bow damage.", "Flat damage (physical and lightning), attack speed, bow damage."), L("Toxic Quiver → Primed Quiver.", "Toxic Quiver → Primed Quiver."), L("Dois danos planos + attack speed.", "Two flat damage mods + attack speed."), L("O raio plano também ativa o Living Lightning da Repulsion.", "Flat lightning also triggers Repulsion's Living Lightning."), ["Adds .* Physical Damage", "Adds .* Lightning", "Attack Speed", "Damage with Bow"]),
 K.item("rings", L("Anéis", "Rings"), "Rings", L("Físico plano, resistências e remnant effect.", "Flat physical, resistances and remnant effect."), L("Blackheart no começo; rares depois.", "Blackheart early; rares later."), L("Físico plano + resistência.", "Flat physical + resistance."), L("Remnant effect só vem do desecrate do Amanamu.", "Remnant effect only comes from Amanamu's desecration."), ["Adds .* Physical Damage", "Resistance$"], ["Blackheart"]),
 K.item("gloves", L("Luvas", "Gloves"), "Gloves_dex", L("Físico e raio planos + attack speed.", "Flat physical and lightning + attack speed."), L("Luvas de Evasão.", "Evasion gloves."), L("Dois danos planos.", "Two flat damage mods."), L("Luvas 'Marksman' com + projéteis são raras e valem muito.", "'Marksman' gloves with + projectiles are rare and very valuable."), ["Adds .* Physical Damage", "Adds .* Lightning", "Attack Speed"]),
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_int", L("ES pura (Subterfuge Mask) e crítico no min-max.", "Pure ES (Subterfuge Mask) and crit for min-max."), L("Sorcerous/Ancestral Tiara.", "Sorcerous/Ancestral Tiara."), L("% ES alto + resistência.", "High % ES + resistance."), L("Capacete híbrido desliga a Subterfuge Mask.", "A hybrid helmet disables Subterfuge Mask."), ["increased Energy Shield$", "to maximum Life$", "Critical"]),
 K.item("body", "Body Armour", "Body_Armours_dex", L("Evasão alta + Spirit.", "High Evasion + Spirit."), L("Corsair Coat.", "Corsair Coat."), L("Spirit 50+ e % Evasão.", "50+ Spirit and % Evasion."), L("Sem Spirit no peito falta espaço para Ghost Dance/Blasphemy.", "Without chest Spirit there's no room for Ghost Dance/Blasphemy."), ["to Spirit$", "increased Evasion Rating$", "Deflection"]),
 K.item("boots", L("Botas", "Boots"), "Boots_dex_int", L("30% Movement Speed + Evasão/ES.", "30% Movement Speed + Evasion/ES."), L("Charmed Shoes.", "Charmed Shoes."), L("30% MS + resistência.", "30% MS + resistance."), L("Farrul's Rune of the Chase no socket.", "Farrul's Rune of the Chase in the socket."), ["Movement Speed", "Evasion and Energy Shield$", "Resistance$"]),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("Spirit, + projéteis, remnant effect; crítico no min-max.", "Spirit, + projectiles, remnant effect; crit for min-max."), L("Rare com Spirit → Absent Amulet (Eternal Rage).", "Rare with Spirit → Absent Amulet (Eternal Rage)."), L("Spirit + um mod de dano.", "Spirit + a damage mod."), L("Instill: Serrated Edges (barato) ou Dominion (Archon sem bloqueio).", "Instill: Serrated Edges (cheap) or Dominion (Archon without lockout)."), ["to Spirit$", "Level of all Projectile", "Critical Hit Chance$"]),
 K.item("belt", L("Cinto", "Belt"), "Belts", L("Vida, resistências e charm slots.", "Life, resistances and charm slots."), L("Long/Utility Belt.", "Long/Utility Belt."), L("Vida + duas resistências.", "Life + two resistances."), L("Mageblood/Headhunter só no min-max.", "Mageblood/Headhunter only for min-max."), ["to maximum Life$", "Resistance$"], ["Mageblood", "Headhunter"]),
 K.item("charms", "Charms", "Charms", L("Freeze, Slow e Rage.", "Freeze, Slow and Rage."), L("Thawing + Silver + Ruby.", "Thawing + Silver + Ruby."), L("Três gatilhos.", "Three triggers."), L("Rite of Passage (Cat) no min-max.", "Rite of Passage (Cat) for min-max."), ["Charges", "Duration"], ["Nascent Hope", "Ngamahu's Chosen", "The Fall of the Axe", "Rite of Passage"]),
]

CK_DETAIL = {
 "bow": dict(
  base=L("Obliterator Bow (78); ilvl 82 para o T1 de físico.", "Obliterator Bow (78); ilvl 82 for T1 physical."),
  targets=[[P, "(170–179)% increased Physical Damage (T2 155–169%)", "82 (75)"], [P, "Adds (26–39) to (44–66) Physical Damage", 75], [X, "+4 to Level of all Projectile Skills (T2 +3)", "81 (55)"], [X, "+(175–200)% Surpassing chance to fire an additional Arrow", 82], [X, "+(4.41–5)% to Critical Hit Chance", 73]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Greater Essence of Abrasion", "Omen of Dextral Exaltation", "Blacksmith's Whetstone", "Countess Seske's Rune of Archery", "Idol of Thruldana"],
  cheap=[K.trade("Splinterheart", "Unique barata; runeforge no nível 40 com Medved's Crest of the Circle.", "Cheap unique; runeforge at level 40 with Medved's Crest of the Circle.")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Obliterator Bow branco → Transmutation/Augmentation até % físico e físico plano → Regal.", "White Obliterator Bow → Transmutation/Augmentation until % physical and flat physical → Regal."), L("Não saiu: outra base (são baratas).", "Didn't hit: another base (they're cheap).")),
         K.side_exalt("s", "+ projéteis ou flecha adicional", "+ projectiles or additional arrow"), K.quality("Blacksmith's Whetstone", "")],
  lux=[S(L("Runas", "Runes"), L("Countess Seske's Rune of Archery (+1 flecha) e Idol of Thruldana (+1 limite de veneno).", "Countess Seske's Rune of Archery (+1 arrow) and Idol of Thruldana (+1 poison cap)."), ""), K.divine]),
 "quiver": dict(
  base="Primed Quiver", targets=[[P, "Adds (12–19) to (22–32) Physical Damage to Attacks", 75], [P, "Adds (1–4) to (60–71) Lightning damage to Attacks", 75], [P, "(51–59)% increased Damage with Bow Skills", 81], [X, "(14–16)% increased Attack Speed", 60]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation"],
  cheap=[K.trade("Quiver · Adds Physical Damage to Attacks · Adds Lightning Damage to Attacks", "", "")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Transmutation/Augmentation até dois danos planos → Regal.", "Transmutation/Augmentation until two flat damage mods → Regal."), ""), K.side_exalt("p", "dano plano / bow damage", "flat damage / bow damage")],
  lux=[K.side_exalt("s", "attack speed e crítico", "attack speed and crit"), K.divine]),
 "rings": dict(
  base=L("Ruby/Sapphire Ring (a resistência que faltar).", "Ruby/Sapphire Ring (whatever resistance you lack)."), targets=[[P, "Adds (12–19) to (22–32) Physical Damage to Attacks", 75], [X, "+(41–45)% Resistance", 82], [DP, L("Amanamu: % increased effect of Remnants", "Amanamu: % increased effect of Remnants"), 65]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Preserved Collarbone", "Omen of the Liege", "Omen of Sinistral Necromancy"],
  cheap=[K.trade("Blackheart", "", "")],
  value=[K.trade("Ring · Adds Physical Damage to Attacks · Resistances", "", ""), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.desecrate("Preserved Collarbone", "Omen of the Liege", "remnant effect (prefixo do Amanamu)", "remnant effect (Amanamu prefix)"), K.divine]),
 "gloves": dict(
  base=L("Luvas de Evasão.", "Evasion gloves."), targets=[[P, "Adds (12–19) to (22–32) Physical Damage to Attacks", 75], [P, "Adds (1–4) to (60–71) Lightning damage to Attacks", 75], [X, "(14–16)% increased Attack Speed", 60]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Gloves · Adds Physical Damage to Attacks · Adds Lightning Damage to Attacks", "", "")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Transmutation/Augmentation até dois danos planos → Regal.", "Transmutation/Augmentation until two flat damage mods → Regal."), ""), K.side_exalt("s", "attack speed", "attack speed")],
  lux=[S(L("Runas", "Runes"), L("Courtesan Mannan's Rune of Cruelty e Fenumus' Rune of Draining.", "Courtesan Mannan's Rune of Cruelty and Fenumus' Rune of Draining."), ""), K.divine]),
 "helmet": dict(
  base=L("Sorcerous/Ancestral Tiara (ES pura).", "Sorcerous/Ancestral Tiara (pure ES)."), targets=[[P, "(92–100)% increased Energy Shield", 65], [P, "+(150–174) to maximum Life", 65], [X, L("Critical Hit Chance (min-max)", "Critical Hit Chance (min-max)"), 60]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Cyclonic Alloy", "Rune of Reach", "Armourer's Scrap"],
  cheap=[K.trade("Helmet (ES) · Energy Shield · Life · Resistances", "", "")],
  value=[S(L("Defesa no Magic", "Defence on the Magic item"), L("Transmutation/Augmentation até % ES → Regal.", "Transmutation/Augmentation until % ES → Regal."), ""), K.alloy("Cyclonic Alloy", "uptime do Archon of Chayula", "Archon of Chayula uptime")],
  lux=[S("Rune of Reach", L("Mais remnant effect no socket.", "More remnant effect in the socket."), ""), K.divine]),
 "body": dict(
  base="Corsair Coat", targets=[[P, "+(57–61) to Spirit (T2 54–56)", "78 (65)"], [P, "(101–110)% increased Evasion Rating", 75]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Armourer's Scrap", "Craiceann's Rune of Warding"],
  cheap=[K.trade("Body Armour (Evasion) · to Spirit", "", "")],
  value=[S(L("Spirit no Magic", "Spirit on the Magic item"), L("Transmutation/Augmentation até Spirit → Regal.", "Transmutation/Augmentation until Spirit → Regal."), ""), K.side_exalt("p", "% Evasão", "% Evasion"), K.quality("Armourer's Scrap", "")],
  lux=[S("Craiceann's Rune of Warding", L("Com The Hollowkeeper: imune a curses.", "With The Hollowkeeper: curse immune."), ""), K.divine]),
 "boots": dict(
  base="Charmed Shoes", targets=[[P, "30% increased Movement Speed (T1 35%)", "65 (82)"], [P, L("% Evasion and Energy Shield", "% Evasion and Energy Shield"), 60]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Farrul's Rune of the Chase"],
  cheap=[K.trade("Boots · Movement Speed ≥ 25 · Resistances", "", "")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Transmutation/Augmentation até Movement Speed → Regal.", "Transmutation/Augmentation until Movement Speed → Regal."), ""), K.side_exalt("s", "resistências", "resistances")],
  lux=[S("Farrul's Rune of the Chase", L("Runa das botas do Goratha.", "Goratha's boots rune."), ""), K.divine]),
 "amulet": dict(
  base=L("Rare com Spirit → Absent Amulet.", "Rare with Spirit → Absent Amulet."), targets=[[P, "+(47–50) to Spirit", 54], [X, "+3 to Level of all Projectile Skills", 75], [DP, L("Amanamu: % increased effect of Remnants", "Amanamu: % increased effect of Remnants"), 65]],
  mats=["Chaos Orb", "Exalted Orb", "Omen of Dextral Exaltation", "Preserved Collarbone", "Omen of the Liege", "Distilled Emotions"],
  cheap=[K.trade("Amulet · to Spirit ≥ 35", "", "")],
  value=[K.side_exalt("s", "+ projéteis", "+ projectiles"), S(L("Instill", "Instill"), L("Serrated Edges para dano barato.", "Serrated Edges for cheap damage."), "")],
  lux=[K.desecrate("Preserved Collarbone", "Omen of the Liege", "remnant effect", "remnant effect"), S("Dominion", L("Instill oculto: Archon sem bloqueio.", "Hidden instill: Archon without lockout."), "")]),
 "belt": dict(
  base="Long Belt", targets=[[P, "+(150–174) to maximum Life", 65], [X, "+(41–45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb"],
  cheap=[K.trade("Belt · Life · Resistances", "", "")], value=[K.side_exalt("s", "resistências", "resistances")],
  lux=[S("Mageblood · Headhunter", L("Min-max.", "Min-max."), "")]),
 "charms": dict(
  base=L("Thawing, Silver e Ruby Charm.", "Thawing, Silver and Ruby Charm."), targets=[[P, "Charges / duration", 60]], mats=["Orb of Transmutation", "Orb of Augmentation"],
  cheap=[S(L("Charms normais", "Normal charms"), L("Freeze, Slow e fogo.", "Freeze, Slow and fire."), "")], value=[S("Nascent Hope · Ngamahu's Chosen", L("ES e Rage.", "ES and Rage."), "")],
  lux=[S("Rite of Passage · The Fall of the Axe", L("Min-max.", "Min-max."), "")]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
