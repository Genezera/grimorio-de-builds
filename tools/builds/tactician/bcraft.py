# -*- coding: utf-8 -*-
# Oficina de crafting do Tactician (executado dentro de bdata.py: usa L, BOOK). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("crossbow", L("Crossbow", "Crossbow"), "Crossbows", L("+ nível de projéteis, dano físico e dano adicionado: é 70% do dano da build.", "+ projectile levels, physical damage and added damage: it's 70% of the build's damage."),
        L("Suba de base a cada salto: 16 (Ato 2), 33 (Ato 3), Cannonade 59, Trarthan Cannon 65 (só granadas), Siege Crossbow 79.", "Move bases at each jump: 16 (Act 2), 33 (Act 3), Cannonade 59, Trarthan Cannon 65 (grenades only), Siege Crossbow 79."),
        L("Pare quando tiver + nível de projéteis e dois mods de dano fortes; o resto é luxo.", "Stop once you have + projectile levels and two strong damage mods; the rest is luxury."),
        L("Trarthan Cannon não carrega virotes: o Explosive Shot precisa de outra crossbow no Weapon Set 2.", "The Trarthan Cannon can't load bolts: Explosive Shot needs another crossbow in Weapon Set 2."),
        ["increased Physical Damage$", "Adds .* Physical Damage$", "Adds .* Lightning Damage$", "Level of all Projectile", "increased Attack Speed", "Mana per enemy killed"], ["siege", "trarthan", "cannonade"]),
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_str", L("Vida, Armour e resistências.", "Life, Armour and resistances."), L("Base de Armour (Força). No endgame, Armour vira Deflection com Polish That Gear.", "Armour (Strength) base. In endgame, Armour becomes Deflection with Polish That Gear."),
        L("Vida + duas resistências + % Armour applies to Elemental já resolvem.", "Life + two resistances + % Armour applies to Elemental already do the job."), L("Não troque vida por dano no capacete.", "Don't trade life for damage on the helmet."),
        ["to maximum Life$", "increased Armour$", "to Fire Resistance", "Armour also applies to Elemental"], ["Constricting Command"]),
 K.item("body", "Body Armour", "Body_Armours_str", L("Vida, Armour e regeneração para o Berserk.", "Life, Armour and regeneration for Berserk."), L("Base com implicit de Life Regeneration (o BlazeworksTV usa Ornate Plate no T15).", "A base with a Life Regeneration implicit (BlazeworksTV uses Ornate Plate at T15)."),
        L("Vida alta + Armour + uma resistência. Regen ajuda muito com Berserk.", "High life + Armour + one resistance. Regen helps a lot with Berserk."), L("Essence of Hysteria no body dá Thorns, não Movement Speed.", "Essence of Hysteria on body armour gives Thorns, not Movement Speed."),
        ["to maximum Life$", "increased Armour$", "Life Regeneration per second", "Armour also applies to Elemental"]),
 K.item("gloves", L("Luvas", "Gloves"), "Gloves_str", L("Dano adicionado (raio para Shock), vida e Mana on Kill.", "Added damage (lightning for Shock), life and Mana on Kill."), L("Base de Armour; dano adicionado a ataques é prefixo.", "Armour base; added attack damage is a prefix."),
        L("Um dano adicionado + vida + Mana on Kill.", "One added damage + life + Mana on Kill."), L("Mana on Kill é sufixo e disputa com resistências.", "Mana on Kill is a suffix and competes with resistances."),
        ["Adds .* Lightning damage to Attacks", "Adds .* Physical Damage to Attacks", "to maximum Life$", "Mana per enemy killed"]),
 K.item("boots", L("Botas", "Boots"), "Boots_str", L("Movement Speed primeiro, depois vida e resistências.", "Movement Speed first, then life and resistances."), L("Base de Armour ilvl 82 para 35%.", "ilvl 82 Armour base for 35%."),
        L("30%+ de MS e vida.", "30%+ MS and life."), L("35% só existe em ilvl 82.", "35% only exists at ilvl 82."), ["Movement Speed", "to maximum Life$"]),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("Spirit para Berserk + nível de projéteis.", "Spirit for Berserk + projectile levels."), L("Solar Amulet (implicit de Spirit) é a base do endgame.", "Solar Amulet (Spirit implicit) is the endgame base."),
        L("Spirit alto + vida. + nível de projéteis é luxo se a mana aguentar.", "High Spirit + life. + projectile levels is luxury if mana holds."), L("+ nível de projéteis aumenta o custo de mana das granadas.", "+ projectile levels raises grenade mana cost."),
        ["to Spirit$", "Level of all Projectile", "to maximum Life$"], ["spamu"]),
 K.item("rings", L("Anéis", "Rings"), "Rings", L("Dano adicionado a ataques e resistências.", "Added attack damage and resistances."), L("Qualquer base; Topaz/Ruby cobrem resistência pelo implicit.", "Any base; Topaz/Ruby cover resistance via implicit."),
        L("Um dano adicionado + vida + resistência.", "One added damage + life + resistance."), L("Raio adicionado é o mais forte (Shock).", "Added lightning is strongest (Shock)."),
        ["Adds .* Lightning damage to Attacks", "Adds .* Fire damage to Attacks", "to maximum Life$", "to all Elemental Resistances"]),
 K.item("belt", L("Cinto", "Belt"), "Belts", L("Vida, resistências, Força e Armour.", "Life, resistances, Strength and Armour."), L("Heavy/Plate Belt.", "Heavy/Plate Belt."), L("Vida + duas resistências.", "Life + two resistances."), L("Mageblood é luxo: só depois da crossbow.", "Mageblood is luxury: only after the crossbow."),
        ["to maximum Life$", "to Strength$", "to Armour$"], ["Mageblood"]),
 K.item("life-flask", L("Frasco de vida", "Life flask"), "Life_Flasks", L("Recuperação confiável.", "Reliable recovery."), L("Ultimate Life Flask.", "Ultimate Life Flask."), L("Recuperação alta + instant parcial.", "High recovery + partial instant."), L("Não gaste Exalted em flask.", "Don't spend Exalted on flasks."), ["Amount Recovered", "Instant"]),
 K.item("mana-flask", L("Frasco de mana", "Mana flask"), "Mana_Flasks", L("Mana no boss antes das joias.", "Mana on bosses before the jewels."), L("Ultimate Mana Flask.", "Ultimate Mana Flask."), L("Recuperação alta.", "High recovery."), L("Com joias de mana ele vira reserva.", "With mana jewels it becomes a backup."), ["Amount Recovered"]),
 K.item("charms", "Charms", "Charms", L("Cobrir freeze, ignite e bleed.", "Cover freeze, ignite and bleed."), L("Thawing + Dousing + Staunching; Beira's Anguish e Sanguis Heroum no endgame.", "Thawing + Dousing + Staunching; Beira's Anguish and Sanguis Heroum in endgame."), L("Três charms que disparam sozinhos.", "Three charms that trigger on their own."), L("Charm sem gatilho útil ocupa slot à toa.", "A charm without a useful trigger wastes a slot."), ["Charges", "Duration"], ["Beira's Anguish", "Sanguis Heroum"]),
]

CK_DETAIL = {
 "crossbow": dict(
  base=L("Crossbow branca do vendor em cada salto; no endgame Siege Crossbow ilvl 81+ (Trarthan Cannon só granadas).", "White vendor crossbow at each jump; in endgame an ilvl 81+ Siege Crossbow (Trarthan Cannon grenades only)."),
  targets=[[P, "(170–179)% increased Physical Damage (T2 155–169%)", "82 (75)"], [P, "Adds (37–55) to (63–94) Physical Damage", 75], [P, "Adds (1–19) to (310–358) Lightning Damage", 81], [X, "+5 to Level of all Projectile Skills (T2 +4)", "81 (55)"], [X, "(17–19)% increased Attack Speed", 37], [X, "Gain (36–45) Mana per enemy killed", 78], [DP, "Amanamu: Grenade Skills have +1 Cooldown Uses · (101–121)% increased Grenade Damage", 65], [C, "Perfect Essence of Battle: +3 to Level of all Attack Skills", 72]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Greater Essence of Abrasion", "Greater Essence of Electricity", "Exalted Orb", "Perfect Essence of Battle", "Gnawed Jawbone", "Preserved Jawbone", "Omen of the Liege", "Omen of Abyssal Echoes", "Artificer's Orb", "Blacksmith's Whetstone", "Vaal Orb"],
  cheap=[K.trade("Crossbow · “+# to Level of all Projectile Skills” ≥ 3 · “% increased Physical Damage” ≥ 100 / Adds Physical/Lightning", "Na campanha (SSF) o BlazeworksTV crafta; no trade, uma rare pronta costuma sair barata.", "In the campaign (SSF) BlazeworksTV crafts it; on trade a finished rare is usually cheap.")],
  value=[S(L("Guarde a currency do ato", "Save the act's currency"), L("Até a próxima base, só Transmutation e Augmentation na arma. Regal, Alchemy e Exalted ficam para o salto (16, 33, 59).", "Until the next base, only Transmutation and Augmentation on the weapon. Regal, Alchemy and Exalted wait for the jump (16, 33, 59)."), ""),
         S(L("Magic com um mod bom", "Magic with one good mod"), L("Base branca do vendor → Transmutation + Augmentation. Continue só se saiu + nível de projéteis, % físico, dano adicionado ou attack speed.", "White vendor base → Transmutation + Augmentation. Only continue if you got + projectile levels, % physical, added damage or attack speed."), L("Não saiu nada útil: compre outra base branca (é mais barato que Annulment).", "Nothing useful: buy another white base (cheaper than Annulment).")),
         S(L("Rare: Regal ou Essence", "Rare: Regal or Essence"), L("Regal Orb mantém os mods e adiciona um. Greater Essence of Abrasion (físico) ou Electricity (raio) transforma o Magic em Rare com o dano garantido.", "Regal Orb keeps the mods and adds one. Greater Essence of Abrasion (physical) or Electricity (lightning) turns the Magic item Rare with guaranteed damage."), ""),
         K.side_exalt("s", "+ nível de projéteis ou attack speed", "+ projectile levels or attack speed"),
         K.desecrate("Gnawed Jawbone", "", "um mod de granada (Amanamu) se oferecido", "a grenade mod (Amanamu) if offered"),
         K.quality("Blacksmith's Whetstone", "")],
  lux=[S(L("Siege Crossbow ilvl 81+", "ilvl 81+ Siege Crossbow"), L("Base branca ilvl 81+ para liberar +5 nível de projéteis e raio T1. Mesma abertura: Transmutation/Augmentation → Essence of Electricity ou Abrasion.", "White ilvl 81+ base to unlock +5 projectile levels and T1 lightning. Same opening: Transmutation/Augmentation → Essence of Electricity or Abrasion."), ""),
       K.side_exalt("p", "% físico e dano adicionado", "% physical and added damage"),
       K.desecrate("Preserved Jawbone", "Omen of the Liege", "Grenade Skills have +1 Cooldown Uses ou (101–121)% increased Grenade Damage", "Grenade Skills have +1 Cooldown Uses or (101–121)% increased Grenade Damage"),
       S(L("Perfect Essence of Battle (se faltar nível)", "Perfect Essence of Battle (if levels are missing)"), L("Num Rare, remove um mod aleatório e adiciona +3 to Level of all Attack Skills. Ocupa o único mod crafted do item.", "On a Rare, removes a random mod and adds +3 to Level of all Attack Skills. Takes the item's only crafted mod."), L("Levou um prefixo de dano: complete com Exalted + Omen of Sinistral Exaltation.", "It removed a damage prefix: refill with Exalted + Omen of Sinistral Exaltation.")),
       K.divine, K.quality("Blacksmith's Whetstone", "Vaal Orb")]),
 "helmet": dict(
  base=L("Capacete de Armour (Força) ilvl 82.", "ilvl 82 Armour (Strength) helmet."),
  targets=[[P, "+(150–174) to maximum Life", 65], [P, "(92–100)% increased Armour", 65], [P, "(39–42)% increased Armour / +(42–49) to maximum Life", 78], [X, "+(41–45)% Fire/Cold/Lightning Resistance", 82], [X, "+(38–43)% of Armour also applies to Elemental Damage", 66]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Greater Essence of Insulation", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Armourer's Scrap"],
  cheap=[K.trade("Helmet (Armour) · Life ≥ 100 · Total Resistance ≥ 60")],
  value=[K.ess_start("Greater Essence of Insulation", "+31–35% resistência a fogo", "+31–35% fire resistance", "Capacete de Armour branco", "White Armour helmet"), K.side_exalt("p", "vida e % Armour", "life and % Armour"), K.side_exalt("s", "resistências e Armour applies to Elemental", "resistances and Armour applies to Elemental"), K.quality("Armourer's Scrap", "")],
  lux=[S(L("Constricting Command", "Constricting Command"), L("Unique barato do setup aspiracional: vida, atributos e regeneração. Compare com um rare de vida + duas resistências.", "Cheap unique from the aspirational setup: life, attributes and regeneration. Compare with a life + two resistances rare."), ""), K.divine]),
 "body": dict(
  base=L("Ornate Plate ou outra base de Armour com implicit de Life Regeneration.", "Ornate Plate or another Armour base with a Life Regeneration implicit."),
  targets=[[P, "+(200–214) to maximum Life", 80], [P, "(101–110)% increased Armour", 75], [X, "(33.1–36) Life Regeneration per second", 81], [X, "+(44–50)% of Armour also applies to Elemental Damage", 81], [DS, "Amanamu: (6–12)% increased Spirit Reservation Efficiency", 65], [C, "Perfect Essence of the Body: (8–10)% increased maximum Life", 72]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Perfect Essence of the Body", "Preserved Rib", "Omen of Abyssal Echoes", "Armourer's Scrap"],
  cheap=[K.trade("Body (Armour) · Life ≥ 150 · Resistance ≥ 30", "Qualquer body de vida serve até o Berserk.", "Any life body works until Berserk.")],
  value=[S(L("Vida e Armour no Magic", "Life and Armour on the Magic item"), L("Base branca → Transmutation/Augmentation até vida ou % Armour → Regal.", "White base → Transmutation/Augmentation until life or % Armour → Regal."), ""), K.side_exalt("s", "Life Regeneration e resistências", "Life Regeneration and resistances"), K.quality("Armourer's Scrap", "")],
  lux=[S(L("Perfect Essence of the Body", "Perfect Essence of the Body"), L("Num Rare de vida + Armour, remove um mod aleatório e adiciona 8–10% de vida máxima.", "On a life + Armour Rare, removes a random mod and adds 8–10% maximum life."), ""), K.desecrate("Preserved Rib", "", "Spirit Reservation Efficiency (Amanamu)", "Spirit Reservation Efficiency (Amanamu)"), K.divine, K.quality("Armourer's Scrap", "Vaal Armourer's Infuser")]),
 "gloves": dict(
  base=L("Luvas de Armour ilvl 75+.", "ilvl 75+ Armour gloves."),
  targets=[[P, "Adds (1–4) to (60–71) Lightning damage to Attacks", 75], [P, "Adds (12–19) to (22–32) Physical Damage to Attacks", 75], [P, "+(120–149) to maximum Life", 60], [X, "Gain (36–45) Mana per enemy killed", 78], [X, "+(41–45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Armourer's Scrap"],
  cheap=[K.trade("Gloves · Adds Lightning/Physical to Attacks · Life ≥ 80")],
  value=[S(L("Dano adicionado primeiro", "Added damage first"), L("Transmutation/Augmentation até dano adicionado → Regal.", "Transmutation/Augmentation until added damage → Regal."), ""), K.side_exalt("p", "vida", "life"), K.side_exalt("s", "Mana on Kill e resistência", "Mana on Kill and resistance"), K.quality("Armourer's Scrap", "")],
  lux=[K.side_exalt("p", "raio adicionado T1 + vida", "T1 added lightning + life"), K.divine]),
 "boots": dict(
  base=L("Botas de Armour ilvl 82 (35% MS).", "ilvl 82 Armour boots (35% MS)."),
  targets=[[P, "35% increased Movement Speed (T2 30%)", "82 (65)"], [P, "+(120–149) to maximum Life", 60], [X, "+(41–45)% Resistance", 82], [DS, "Ulaman: +(13–17)% Lightning and Chaos Resistances", 65]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Essence of Hysteria", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Preserved Rib", "Armourer's Scrap"],
  cheap=[K.trade("Boots · Movement Speed ≥ 25 · Life ≥ 60")],
  value=[S(L("Movimento no Magic", "Movement on the Magic item"), L("Base branca ilvl 82 → Transmutation/Augmentation até Movement Speed → Regal.", "White ilvl 82 base → Transmutation/Augmentation until Movement Speed → Regal."), L("Garantido: Essence of Hysteria num Rare (30% MS, ocupa o crafted).", "Guaranteed: Essence of Hysteria on a Rare (30% MS, uses the crafted slot).")), K.side_exalt("p", "vida", "life"), K.side_exalt("s", "resistências", "resistances"), K.quality("Armourer's Scrap", "")],
  lux=[K.desecrate("Preserved Rib", "", "resistência híbrida com Chaos", "a hybrid Chaos resistance"), K.divine]),
 "amulet": dict(
  base=L("Solar Amulet (implicit de Spirit).", "Solar Amulet (Spirit implicit)."),
  targets=[[P, "+(47–50) to Spirit", 54], [X, "+3 to Level of all Projectile Skills (T2 +2)", "75 (41)"], [P, "+(120–149) to maximum Life", 60], [C, "Sovereign Alloy: (20–30)% Explicit Resistance magnitudes", 65]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Greater Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Sovereign Alloy", "Divine Orb"],
  cheap=[K.trade("Solar Amulet · “+# to Spirit” ≥ 40 · Life", "Spirit é o que libera o Berserk.", "Spirit is what unlocks Berserk.")],
  value=[S(L("Spirit no Magic", "Spirit on the Magic item"), L("Solar Amulet branco → Transmutation/Augmentation até Spirit (prefixo) → Regal.", "White Solar Amulet → Transmutation/Augmentation until Spirit (prefix) → Regal."), ""), K.side_exalt("s", "+ nível de projéteis", "+ projectile levels"), K.side_exalt("p", "vida", "life")],
  lux=[S(L("Spirit T1 + projéteis +3", "T1 Spirit + projectile +3"), L("Base ilvl 75+. Greater/Perfect Exalted com Omen de lado para chegar em 47–50 Spirit e +3 projéteis.", "ilvl 75+ base. Greater/Perfect Exalted with a side Omen to reach 47–50 Spirit and +3 projectile levels."), ""), K.alloy("Sovereign Alloy", "(20–30)% de magnitude nas resistências explícitas", "(20–30)% explicit resistance magnitude"), K.divine]),
 "rings": dict(
  base=L("Topaz/Ruby Ring (implicit de resistência).", "Topaz/Ruby Ring (resistance implicit)."),
  targets=[[P, "Adds (1–4) to (60–71) Lightning damage to Attacks", 75], [P, "Adds (25–29) to (37–45) Fire damage to Attacks", 75], [P, "+(100–119) to maximum Life", 54], [X, "+(15–16)% to all Elemental Resistances", 68]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Preserved Collarbone"],
  cheap=[K.trade("Ring · Adds Lightning/Fire to Attacks · Resistance")],
  value=[S(L("Dano adicionado no Magic", "Added damage on the Magic item"), L("Transmutation/Augmentation até dano adicionado → Regal.", "Transmutation/Augmentation until added damage → Regal."), ""), K.side_exalt("s", "resistências", "resistances"), K.side_exalt("p", "vida", "life")],
  lux=[K.desecrate("Preserved Collarbone", "", "um mod de ataque/resistência útil", "a useful attack/resistance mod"), K.divine]),
 "belt": dict(
  base=L("Heavy Belt (Força) ou Plate Belt (Armour).", "Heavy Belt (Strength) or Plate Belt (Armour)."),
  targets=[[P, "+(150–174) to maximum Life", 65], [P, "+(312–351) to Armour", 80], [X, "+(34–36) to Strength", 81], [X, "+(41–45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Belt · Life ≥ 100 · Total Resistance ≥ 50")],
  value=[S(L("Vida no Magic", "Life on the Magic item"), L("Transmutation/Augmentation até vida → Regal.", "Transmutation/Augmentation until life → Regal."), ""), K.side_exalt("s", "resistências e Força", "resistances and Strength")],
  lux=[S("Mageblood", L("Legados de flask permanentes. Só depois da Siege Crossbow e do amuleto de Spirit.", "Permanent flask legacies. Only after the Siege Crossbow and the Spirit amulet."), ""), K.divine]),
 "life-flask": dict(
  base=L("Ultimate Life Flask ilvl 83.", "ilvl 83 Ultimate Life Flask."), targets=[[P, "(76–80)% increased Amount Recovered", 83], [X, "Charges / duration", 60]], mats=["Orb of Transmutation", "Orb of Augmentation", "Glassblower's Bauble"],
  cheap=[S(L("Transmutation + Augmentation", "Transmutation + Augmentation"), L("Flask branco → Transmutation/Augmentation até recuperação alta.", "White flask → Transmutation/Augmentation until high recovery."), "")], value=[S(L("Qualidade", "Quality"), L("Glassblower's Bauble até 20%.", "Glassblower's Bauble up to 20%."), "")], lux=[S(L("Dois mods bons", "Two good mods"), L("Repita Transmutation em bases brancas até prefixo e sufixo úteis.", "Repeat Transmutation on white bases until both prefix and suffix are useful."), "")]),
 "mana-flask": dict(
  base=L("Ultimate Mana Flask.", "Ultimate Mana Flask."), targets=[[P, "(76–80)% increased Amount Recovered", 83]], mats=["Orb of Transmutation", "Orb of Augmentation", "Glassblower's Bauble"],
  cheap=[S(L("Transmutation + Augmentation", "Transmutation + Augmentation"), L("Recuperação alta basta.", "High recovery is enough."), "")], value=[S(L("Qualidade", "Quality"), L("Glassblower's Bauble até 20%.", "Glassblower's Bauble up to 20%."), "")], lux=[S(L("Troque por joias de mana", "Swap for mana jewels"), L("Com joias Ruby/Sapphire de mana o flask vira reserva.", "With Ruby/Sapphire mana jewels the flask becomes a backup."), "")]),
 "charms": dict(
  base=L("Thawing, Dousing e Staunching Charm.", "Thawing, Dousing and Staunching Charm."), targets=[[P, "Charges / duration", 60]], mats=["Orb of Transmutation", "Orb of Augmentation"],
  cheap=[S(L("Charms normais", "Normal charms"), L("Um de cada tipo de ailment perigoso.", "One for each dangerous ailment."), "")], value=[S("Beira's Anguish + Sanguis Heroum", L("Ambos custam quase nada no poe.ninja.", "Both cost almost nothing on poe.ninja."), "")], lux=[S("The Fall of the Axe · Rite of Passage", L("Onslaught e espíritos animais: luxo do setup máximo.", "Onslaught and animal spirits: max-setup luxury."), "")]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
