# -*- coding: utf-8 -*-
# Oficina de crafting do Druid Shaman Archmage (executado dentro de bdata.py). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

MANA_FIRST = L("Regra da build: mana máxima primeiro. Mana é dano (Archmage) e vida (Mind Over Matter) no mesmo mod.",
               "The build's rule: maximum mana first. Mana is damage (Archmage) and life (Mind Over Matter) in the same mod.")
RUNES = L("Depois do Wisdom of the Maji, a runa também dá a linha 'Bonded' dela: encha todos os sockets.",
          "After Wisdom of the Maji the rune also grants its 'Bonded' line: fill every socket.")

CK_ITEMS = [
 K.item("staff", L("Cajado", "Staff"), "Staves", L("% dano de spell, +mana máxima, cast speed e + níveis de spell.", "% spell damage, +maximum mana, cast speed and + spell levels."), L("Chiming Staff (Sire of Shards) na campanha; Gelid Staff (Taryn's Shiver) para boss.", "Chiming Staff (Sire of Shards) in the campaign; Gelid Staff (Taryn's Shiver) for bosses."), L("Qualquer cajado Magic com % dano de spell já dobra seu dano no ato.", "Any magic staff with % spell damage already doubles your damage for that act."), L("As uniques baratas (Sire of Shards, Taryn's Shiver) batem quase qualquer rare até o endgame.", "The cheap uniques (Sire of Shards, Taryn's Shiver) beat almost any rare until endgame."), ["increased Spell Damage", "to maximum Mana$", "increased Cast Speed", "Level of all Spell"], ["Sire of Shards", "Taryn's Shiver", "Runeseeker's Call"]),
 K.item("focus", "Focus", "Foci", L("% ES (que vira mana), +mana máxima e crítico para spells.", "% ES (which becomes mana), +maximum mana and spell crit."), L("Sacred Focus (Rathpith Globe) no endgame.", "Sacred Focus (Rathpith Globe) in endgame."), L("% ES + mana.", "% ES + mana."), L("Com Eldritch Battery, ES no Focus é mana: não compare com 'defesa', compare com dano.", "With Eldritch Battery, focus ES is mana: don't compare it to 'defence', compare it to damage."), ["increased Energy Shield$", "to maximum Mana$", "Critical Hit Chance for Spell"], ["Rathpith Globe", "The Eternal Spark", "Threaded Light"]),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("+Spirit (prioridade), +mana máxima e + níveis de spell.", "+Spirit (priority), +maximum mana and + spell levels."), L("Rare com Spirit → Absent Amulet no endgame.", "Rare with Spirit → Absent Amulet in endgame."), L("+40 de Spirit ou mais.", "+40 Spirit or more."), L("Spirit no amuleto é o que faz Archmage e Cast on Critical rodarem juntos.", "Amulet Spirit is what lets Archmage and Cast on Critical run together."), ["to Spirit$", "to maximum Mana$", "Level of all Spell"], ["Stone of Lazhwar", "Astramentis", "The Everlasting Gaze"]),
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_int", L("% ES, +mana máxima e crítico para spells.", "% ES, +maximum mana and spell crit."), "Ancestral Tiara", L("% ES + mana; crítico no endgame.", "% ES + mana; crit in endgame."), L("Reservation Efficiency na Tiara ajuda a caber os dois buffs de 100 de Spirit.", "Reservation Efficiency on the Tiara helps fit both 100-Spirit buffs."), ["increased Energy Shield$", "to maximum Mana$", "Critical Hit Chance for Spell", "Resistance$"], ["Goldrim", "Indigon"]),
 K.item("body", "Body Armour", "Body_Armours_int", L("% ES, +mana máxima, +Spirit e resistências.", "% ES, +maximum mana, +Spirit and resistances."), L("Vile Robe (ES puro) ou Havoc Raiment (Cloak of Defiance).", "Vile Robe (pure ES) or Havoc Raiment (Cloak of Defiance)."), L("% ES + mana.", "% ES + mana."), L("Spirit no peito é a segunda maior fonte depois do amuleto.", "Chest Spirit is the second biggest source after the amulet."), ["increased Energy Shield$", "to maximum Mana$", "to Spirit$"], ["Ghostwrithe", "Cloak of Defiance", "Temporalis"]),
 K.item("gloves", L("Luvas", "Gloves"), "Gloves_int", L("+mana máxima, cast speed e + níveis de skills de projétil (Spark).", "+maximum mana, cast speed and + projectile skill levels (Spark)."), "Sirenscale Gloves", L("Mana + cast speed.", "Mana + cast speed."), L("'+ níveis de projétil' não afeta o Comet (não é projétil).", "'+ projectile levels' doesn't affect Comet (it isn't a projectile)."), ["to maximum Mana$", "increased Cast Speed", "Level of all Projectile"], ["Doedre's Tenure"]),
 K.item("boots", L("Botas", "Boots"), "Boots_int", L("Movement Speed, +mana máxima e resistências.", "Movement Speed, +maximum mana and resistances."), L("Sekhema Sandals / Wanderer Shoes.", "Sekhema Sandals / Wanderer Shoes."), L("30% MS + resistência.", "30% MS + resistance."), L("35% de MS só em ilvl 82.", "35% MS only at ilvl 82."), ["Movement Speed", "to maximum Mana$", "Resistance$"], ["Wanderlust"]),
 K.item("rings", L("Anéis", "Rings"), "Rings", L("+mana máxima, % mana máxima, eficiência de custo e resistências.", "+maximum mana, % maximum mana, cost efficiency and resistances."), L("Mnemonic Ring (mana) / Sapphire Ring.", "Mnemonic Ring (mana) / Sapphire Ring."), L("Mana plana + resistência.", "Flat mana + resistance."), L("Snakepit no anel DIREITO dá chain +1 nos projéteis de spell.", "Snakepit in the RIGHT ring grants +1 chain to spell projectiles."), ["to maximum Mana$", "increased maximum Mana", "Mana Cost Efficiency", "Resistances$"], ["Dream Fragments", "Snakepit", "Kalandra's Touch"]),
 K.item("belt", L("Cinto", "Belt"), "Belts", L("Vida, mana e resistências.", "Life, mana and resistances."), "Utility Belt", L("Vida + duas resistências.", "Life + two resistances."), L("Cada slot de charm VAZIO vale +40 de Spirit (Sacred Flow).", "Every EMPTY charm slot is worth +40 Spirit (Sacred Flow)."), ["to maximum Life$", "to maximum Mana$", "Resistance$"], ["Mageblood"]),
 K.item("flasks", "Flasks", "Flasks", L("Recuperação de mana — que com Mind Over Matter é cura.", "Mana recovery — which with Mind Over Matter is healing."), L("Transcendent Mana Flask / Ultimate Life Flask.", "Transcendent Mana Flask / Ultimate Life Flask."), L("Uhtred's Chalice + Lavianga's Spirits.", "Uhtred's Chalice + Lavianga's Spirits."), L("Sem flask de mana, um pack grande te mata: a mana é a sua vida.", "Without a mana flask a big pack kills you: mana is your life."), ["Recovery", "Charges"], ["Uhtred's Chalice", "Lavianga's Spirits", "Olroth's Resolve"]),
]

CK_DETAIL = {
 "staff": dict(
  base=L("Chiming Staff / Gelid Staff; na campanha, qualquer cajado Magic do vendor.", "Chiming Staff / Gelid Staff; in the campaign, any vendor magic staff."),
  targets=[[P, "(80-119)% increased Spell Damage", 65], [P, "+(80-118) to maximum Mana", 60], [X, "(15-20)% increased Cast Speed", 60], [X, "+1 to Level of all Spell Skills", 72]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Greater Iron Rune"],
  cheap=[K.trade("Sire of Shards", "Custa menos de 0,01 divine.", "It costs less than 0.01 divine."), K.trade("Staff · increased Spell Damage ≥ 80 · to maximum Mana", "", "")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Base Normal → Transmutation/Augmentation até % dano de spell ou mana → Regal.", "Normal base → Transmutation/Augmentation until % spell damage or mana → Regal."), L("Nada útil: próxima base (cajados são baratíssimos).", "Nothing useful: next base (staves are dirt cheap).")),
         K.side_exalt("p", "mana máxima", "maximum mana")],
  lux=[S("Runeseeker's Call", L("Aspiracional: só runas, com 200% do efeito delas.", "Aspirational: runes only, with 200% of their effect."), ""), K.divine]),
 "focus": dict(
  base=L("Sacred Focus (Rathpith Globe) ou Focus rare de ES.", "Sacred Focus (Rathpith Globe) or a rare ES focus."),
  targets=[[P, "(92-100)% increased Energy Shield", 65], [P, "+(80-118) to maximum Mana", 60], [X, "(30-35)% increased Critical Hit Chance for Spells", 72]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Armourer's Scrap"],
  cheap=[K.trade("Rathpith Globe", "", ""), K.trade("The Eternal Spark", "", "")],
  value=[S(L("ES no Magic", "ES on the magic item"), L("Transmutation/Augmentation até % ES → Regal.", "Transmutation/Augmentation until % ES → Regal."), ""), K.side_exalt("p", "mana máxima", "maximum mana")],
  lux=[K.quality("Armourer's Scrap", ""), K.divine]),
 "amulet": dict(
  base=L("Rare com Spirit → Absent Amulet.", "Rare with Spirit → Absent Amulet."),
  targets=[[P, "+(47-50) to Spirit", 54], [P, "+(80-118) to maximum Mana", 60], [X, "+(3-4) to Level of all Spell Skills", 75]],
  mats=["Chaos Orb", "Exalted Orb", "Omen of Dextral Exaltation", "Distilled Emotions"],
  cheap=[K.trade("Amulet · to Spirit ≥ 40", "", ""), K.trade("Stone of Lazhwar", "", "")],
  value=[K.side_exalt("s", "mana / cast speed", "mana / cast speed"), S(L("Instill", "Instill"), L("Zarokh's Gift (socket de jewel extra) no endgame.", "Zarokh's Gift (extra jewel socket) in endgame."), "")],
  lux=[K.divine]),
 "helmet": dict(
  base="Ancestral Tiara",
  targets=[[P, "(92-100)% increased Energy Shield", 65], [P, "+(120-143) to maximum Mana", 65], [X, "(30-35)% increased Critical Hit Chance", 72], [C, "Reservation Efficiency", 72]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Armourer's Scrap"],
  cheap=[K.trade("Helmet · increased Energy Shield · to maximum Mana", "", ""), K.trade("Goldrim", "", "")],
  value=[S(L("Defesa no Magic", "Defence on the magic item"), L("Transmutation/Augmentation até % ES → Regal.", "Transmutation/Augmentation until % ES → Regal."), ""), K.side_exalt("p", "mana máxima", "maximum mana")],
  lux=[K.divine]),
 "body": dict(
  base=L("Vile Robe (ES puro).", "Vile Robe (pure ES)."),
  targets=[[P, "(101-110)% increased Energy Shield", 75], [P, "+(120-150) to maximum Mana", 65], [P, "+(57-61) to Spirit", 78]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Greater Iron Rune", "Armourer's Scrap"],
  cheap=[K.trade("Cloak of Defiance", "", ""), K.trade("Ghostwrithe", "", "")],
  value=[S(L("Spirit no Magic", "Spirit on the magic item"), L("Transmutation/Augmentation até Spirit → Regal.", "Transmutation/Augmentation until Spirit → Regal."), ""), K.side_exalt("p", "% ES / mana", "% ES / mana")],
  lux=[S("Temporalis", L("Aspiracional: −2 s de cooldown (Blink quase infinito).", "Aspirational: −2 s cooldown (nearly infinite Blink)."), ""), K.divine]),
 "gloves": dict(
  base="Sirenscale Gloves",
  targets=[[P, "+(80-121) to maximum Mana", 60], [X, "(8-12)% increased Cast Speed", 60], [X, "+2 to Level of all Projectile Skills", 75]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb"],
  cheap=[K.trade("Gloves · to maximum Mana · increased Cast Speed", "", ""), K.trade("Doedre's Tenure", "", "")],
  value=[K.side_exalt("s", "cast speed", "cast speed")],
  lux=[K.divine]),
 "boots": dict(
  base=L("Sekhema Sandals / Wanderer Shoes.", "Sekhema Sandals / Wanderer Shoes."),
  targets=[[P, "35% increased Movement Speed (T2 30%)", "82 (65)"], [P, "+(80-118) to maximum Mana", 60], [X, "+(41-45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb"],
  cheap=[K.trade("Boots · Movement Speed ≥ 30 · to maximum Mana", "", ""), K.trade("Wanderlust", "", "")],
  value=[S(L("Magic → Regal", "Magic → Regal"), L("Transmutation/Augmentation até Movement Speed → Regal.", "Transmutation/Augmentation until Movement Speed → Regal."), ""), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.divine]),
 "rings": dict(
  base=L("Mnemonic Ring (mana) / Sapphire Ring.", "Mnemonic Ring (mana) / Sapphire Ring."),
  targets=[[P, "+(230-267) to maximum Mana", 75], [X, "(7-9)% increased maximum Mana", 72], [X, "(30-39)% increased Mana Cost Efficiency of Spells", 75], [X, "+(15-16)% to all Elemental Resistances", 68]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation"],
  cheap=[K.trade("Ring · to maximum Mana · Resistances", "", ""), K.trade("Dream Fragments", "", "")],
  value=[K.side_exalt("p", "mana máxima", "maximum mana"), K.side_exalt("s", "resistências / eficiência de custo", "resistances / cost efficiency")],
  lux=[S("Kalandra's Touch", L("Copia o anel oposto: combine com o melhor anel de mana.", "Copies the opposite ring: pair it with your best mana ring."), ""), K.divine]),
 "belt": dict(
  base="Utility Belt",
  targets=[[P, "+(150-174) to maximum Life", 65], [P, "+(80-118) to maximum Mana", 60], [X, "+(41-45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb"],
  cheap=[K.trade("Belt · to maximum Life · Resistances", "", "")],
  value=[K.side_exalt("s", "resistências", "resistances")],
  lux=[S("Mageblood", L("Aspiracional — e lembre: charm equipado é −40 de Spirit.", "Aspirational — and remember: an equipped charm is −40 Spirit."), "")]),
 "flasks": dict(
  base=L("Transcendent Mana Flask e Ultimate Life Flask.", "Transcendent Mana Flask and Ultimate Life Flask."),
  targets=[[P, "increased Amount Recovered", 60], [X, "increased Charges", 60]],
  mats=["Orb of Transmutation", "Orb of Augmentation"],
  cheap=[S(L("Flasks Magic", "Magic flasks"), L("Um de mana e um de vida, com 'increased Amount Recovered'.", "One mana and one life, with 'increased Amount Recovered'."), "")],
  value=[S("Uhtred's Chalice + Lavianga's Spirits", L("Recuperação que passa do máximo + efeito constante.", "Overflowing recovery + constant effect."), "")],
  lux=[S("Olroth's Resolve", L("Guard igual ao Runic Ward quando o efeito acaba.", "Guard equal to your Runic Ward when the effect ends."), "")]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
