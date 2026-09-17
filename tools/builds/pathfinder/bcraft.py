# -*- coding: utf-8 -*-
# Oficina de crafting do Pathfinder (executado dentro de bdata.py). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("bow", L("Arco (leveling)", "Bow (leveling)"), "Bows", L("% físico, físico adicionado e + nível de projéteis até o 57.", "% physical, added physical and + projectile levels until 57."), L("Arco branco do vendor ou drop; Artillery Bow no fim da campanha.", "White vendor or dropped bow; Artillery Bow at the end of the campaign."), L("Dois mods de físico + projéteis bastam.", "Two physical mods + projectiles are enough."), L("Elemental não aumenta veneno.", "Elemental doesn't raise poison."), ["increased Physical Damage$", "Adds .* Physical Damage$", "Level of all Projectile", "increased Attack Speed"]),
 K.item("quiver", L("Aljava (leveling)", "Quiver (leveling)"), "Quivers", L("Físico adicionado a ataques.", "Added physical to attacks."), L("Toxic Quiver no fim da campanha.", "Toxic Quiver at the end of the campaign."), L("Um físico adicionado.", "One added physical."), L("Tenha aljava nos dois sets.", "Keep a quiver on both sets."), ["Adds .* Physical Damage", "Level of all Projectile"]),
 K.item("mace", L("Maça do Set 1 (58+)", "Set 1 mace (58+)"), "One_Hand_Maces", L("Dano extra físico e dano contra Fully Broken Armour (Corrosion quebra).", "Extra physical damage and damage against Fully Broken Armour (Corrosion breaks it)."), L("Brigand Mace ou qualquer maça de uma mão com pouca Força e 2 sockets.", "Brigand Mace or any low-Strength one-handed mace with 2 sockets."), L("Perfect Essence of Abrasion + o mod de Fully Broken Armour.", "Perfect Essence of Abrasion + the Fully Broken Armour mod."), L("A essence pode sair se o desecrate remover: repita.", "The essence may go if the desecrate removes it: repeat."), ["Damage against Enemies with Fully Broken Armour"]),
 K.item("sceptre", L("Sceptres (os dois sets)", "Sceptres (both sets)"), "Sceptres", L("Spirit acima de tudo; + nível e vida de minions no Set 2.", "Spirit above all; + minion levels and life on Set 2."), L("Stoic Sceptre.", "Stoic Sceptre."), L("% increased Spirit alto + um mod útil.", "High % increased Spirit + one useful mod."), L("Sem sceptre no Set 2 você não invoca o suficiente.", "Without a sceptre on Set 2 you can't summon enough."), ["increased Spirit$", "Level of all Minion Skills", "Minions have .* increased maximum Life"], ["sceptres"]),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("+3 nível de minions ou 45+ Spirit.", "+3 minion levels or 45+ Spirit."), L("Solar Amulet → Astramentis → amuleto fracturado.", "Solar Amulet → Astramentis → fractured amulet."), L("Spirit ou +minions com vida/resist.", "Spirit or + minions with life/resist."), L("O +3 minions não pode ser fracturado junto com qualidade alta: fracture o Spirit.", "+3 minions can't be fractured alongside high quality: fracture Spirit instead."), ["Level of all Minion Skills", "to Spirit$"], ["Astramentis"]),
 K.item("body", "Body Armour", "Body_Armours_dex_int", L("ES e Evasion com resistências.", "ES and Evasion with resistances."), L("Rambler Jacket → Sacrificial Regalia.", "Rambler Jacket → Sacrificial Regalia."), L("ES/Evasion + duas resistências.", "ES/Evasion + two resistances."), L("Chaos Resistance não é prioridade.", "Chaos Resistance isn't a priority."), ["increased Evasion and Energy Shield$", "to maximum Energy Shield$", "to maximum Life$"]),
 K.item("boots", L("Botas", "Boots"), "Boots_dex_int", L("Corpsewade: nível e sockets.", "Corpsewade: level and sockets."), L("Corpsewade (unique).", "Corpsewade (unique)."), L("Nível alto + sockets.", "High level + sockets."), L("Corromper pode estragar: compre uma de 2 sockets não corrompida para tentar.", "Corrupting can brick it: buy an uncorrupted 2-socket one to try."), ["Movement Speed"], ["Corpsewade"]),
 K.item("rings", L("Anéis", "Rings"), "Rings", L("Resistências e veneno.", "Resistances and poison."), L("Prismatic Ring → Unset Ring com runas.", "Prismatic Ring → Unset Ring with runes."), L("Resistências.", "Resistances."), L("Unset Ring tem socket para runas.", "Unset Ring has a socket for runes."), ["to all Elemental Resistances", "Resistance"]),
 K.item("belt", L("Cinto", "Belt"), "Belts", L("Vida/resists; Shavronne's Satchel no endgame.", "Life/resists; Shavronne's Satchel in endgame."), L("Heavy Belt.", "Heavy Belt."), L("Resistências.", "Resistances."), L("Mageblood só no Uber.", "Mageblood only in Uber."), ["to maximum Life$", "Resistance"], ["Shavronne's Satchel", "Mageblood"]),
 K.item("life-flask", L("Frasco de vida", "Life flask"), "Life_Flasks", L("Regen constante com Enduring Elixirs.", "Constant regen with Enduring Elixirs."), "Ultimate Life Flask", L("Recuperação alta.", "High recovery."), L("Com Shavronne's Satchel também cura ES.", "With Shavronne's Satchel it also heals ES."), ["Amount Recovered"]),
 K.item("charms", "Charms", "Charms", L("Freeze, Stun e Ignite.", "Freeze, Stun and Ignite."), L("Thawing + Stone + Dousing.", "Thawing + Stone + Dousing."), L("Três gatilhos.", "Three triggers."), L("For Utopia no Uber.", "For Utopia in Uber."), ["Charges", "Duration"], ["For Utopia"]),
]

CK_DETAIL = {
 "bow": dict(
  base=L("Arco branco; ilvl 81+ para os tiers do topo.", "White bow; ilvl 81+ for top tiers."),
  targets=[[P, "(170–179)% increased Physical Damage", 82], [P, "Adds (26–39) to (44–66) Physical Damage", 75], [X, "+4 to Level of all Projectile Skills (T2 +3)", "81 (55)"], [X, "(17–19)% increased Attack Speed", 37]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Greater Essence of Abrasion", "Exalted Orb", "Blacksmith's Whetstone", "Artificer's Orb", "Iron Rune"],
  cheap=[S(L("Transmutation + Augmentation", "Transmutation + Augmentation"), L("Arcos brancos do vendor: Transmutation/Augmentation até % físico ou físico adicionado.", "White vendor bows: Transmutation/Augmentation until % physical or added physical."), L("Não saiu: outra base branca (vendors renovam a cada nível).", "Didn't hit: another white base (vendors refresh every level)."))],
  value=[S(L("Regal só com stats bons", "Regal only with good stats"), L("Regal/Exalted apenas em arcos que já têm vários stats prioritários.", "Regal/Exalted only on bows that already have several priority stats."), ""), K.quality("Blacksmith's Whetstone", "")],
  lux=[K.side_exalt("s", "+ nível de projéteis e attack speed", "+ projectile levels and attack speed"), K.divine]),
 "quiver": dict(
  base=L("Aljava branca; Toxic Quiver no fim da campanha.", "White quiver; Toxic Quiver at the end of the campaign."),
  targets=[[P, "Adds (12–19) to (22–32) Physical Damage to Attacks", 75], [X, "+1 to Level of all Projectile Skills", 5]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb"],
  cheap=[S(L("Físico adicionado", "Added physical"), L("Transmutation/Augmentation até físico adicionado.", "Transmutation/Augmentation until added physical."), "")],
  value=[S(L("Regal", "Regal"), L("Regal se já tiver físico + projéteis.", "Regal if it already has physical + projectiles."), "")],
  lux=[S(L("Aljava nos dois sets", "Quiver on both sets"), L("Uma aljava barata no Set 2 para o Stormcaller.", "A cheap quiver on Set 2 for Stormcaller."), "")]),
 "mace": dict(
  base=L("Maça de uma mão com 2 sockets e pouca Força.", "One-handed mace with 2 sockets and low Strength."),
  targets=[[C, "Perfect Essence of Abrasion: Gain (15–20)% of Damage as Extra Physical", 72], [DP, "Amanamu: (41–59)% increased Damage against Enemies with Fully Broken Armour", 65]],
  mats=["Perfect Essence of Abrasion", "Exalted Orb", "Preserved Jawbone", "Omen of Sinistral Necromancy", "Omen of the Liege", "Omen of Abyssal Echoes", "Omen of Light", "Orb of Annulment"],
  cheap=[K.trade("One Hand Mace · 2 sockets · low Strength requirement", "Para começar qualquer maça serve: o Set 1 é de auras.", "To start any mace works: Set 1 is for auras.")],
  value=[S(L("Perfect Essence of Abrasion", "Perfect Essence of Abrasion"), L("Numa maça de 6 mods (complete com Exalted), a essence remove um mod aleatório e adiciona 15–20% do dano como físico extra.", "On a 6-mod mace (fill with Exalted), the essence removes a random mod and adds 15–20% of damage as extra physical."), "")],
  lux=[K.desecrate("Preserved Jawbone", "Omen of the Liege", "“increased Damage against Enemies with Fully Broken Armour” (use também Omen of Sinistral Necromancy para forçar prefixo)", "“increased Damage against Enemies with Fully Broken Armour” (also use Omen of Sinistral Necromancy to force a prefix)"),
       S(L("Se levou a essence", "If it removed the essence"), L("Repita a Perfect Essence of Abrasion (o Skadoosh faz o mesmo).", "Repeat Perfect Essence of Abrasion (Skadoosh does the same)."), "")]),
 "sceptre": dict(
  base=L("Stoic Sceptre (Spirit base) nos dois sets.", "Stoic Sceptre (base Spirit) on both sets."),
  targets=[[P, "(61–65)% increased Spirit (T2 56–60%)", "82 (75)"], [X, "+4 to Level of all Minion Skills (T2 +3)", "78 (55)"], [X, "Minions have (46–50)% increased maximum Life", 80], [C, "Perfect Essence of Command: Aura Skills have (15–20)% increased Magnitudes", 72]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Dextral Exaltation", "Perfect Essence of Command", "Arcanist's Etcher"],
  cheap=[K.trade("Stoic Sceptre · “% increased Spirit” ≥ 50", "Um por set.", "One per set.")],
  value=[S(L("Spirit no Magic", "Spirit on the Magic item"), L("Stoic Sceptre branco → Transmutation/Augmentation até % Spirit → Regal.", "White Stoic Sceptre → Transmutation/Augmentation until % Spirit → Regal."), ""), K.side_exalt("s", "+ nível e vida de minions (Set 2)", "+ minion levels and life (Set 2)")],
  lux=[S(L("Set 1: Perfect Essence of Command", "Set 1: Perfect Essence of Command"), L("No sceptre do Set 1: magnitude das auras (Withering Presence, curses). Arcanist's Etcher até 20% de qualidade.", "On the Set 1 sceptre: aura magnitude (Withering Presence, curses). Arcanist's Etcher to 20% quality."), ""), K.divine]),
 "amulet": dict(
  base=L("Amuleto rare para fracturar.", "Rare amulet to fracture."),
  targets=[[X, "+3 to Level of all Minion Skills", 75], [P, "+(47–50) to Spirit", 54]],
  mats=["Chaos Orb", "Orb of Annulment", "Exalted Orb", "Fracturing Orb", "Preserved Collarbone", "Omen of Abyssal Echoes", "Necrotic Catalyst", "Omen of Dextral Exaltation", "Perfect Exalted Orb"],
  cheap=[K.trade("Amulet · +# to Spirit ≥ 40 or +# to Level of all Minion Skills ≥ 2", "", "")],
  value=[S(L("Rota do Skadoosh: fracturar", "Skadoosh's route: fracture"), L("Chaos num rare de 1 mod até +3 minions ou 45+ Spirit; 2 Exalted; um mod de Abyss NÃO revelado (Collarbone); Fracturing Orb (1 em 3 de fixar o certo).", "Chaos a 1-mod rare until +3 minions or 45+ Spirit; 2 Exalted; one UNREVEALED Abyss mod (Collarbone); Fracturing Orb (1 in 3 to lock the right one)."), L("Fracturou errado: venda e recomece com outra base.", "Wrong fracture: sell it and restart with another base."))],
  lux=[S(L("Qualidade e mods finais", "Quality and final mods"), L("Necrotic Catalyst até 34%+; Annulment de volta só com a fratura; Chaos até o segundo mod-chave; Exalted com Omen de lado; Collarbone + Echoes.", "Necrotic Catalyst to 34%+; Annulment back to just the fracture; Chaos until the second key mod; side-Omen Exalted; Collarbone + Echoes."), ""), K.divine]),
 "body": dict(
  base=L("Base ES/Evasion (Rambler Jacket, Sacrificial Regalia).", "ES/Evasion base (Rambler Jacket, Sacrificial Regalia)."),
  targets=[[P, "(101–110)% increased Evasion and Energy Shield", 75], [P, "+(142–161) Evasion / +(43–48) Energy Shield", 75], [X, "+(41–45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Armourer's Scrap"],
  cheap=[K.trade("Body (ES/Evasion) · Energy Shield · Resistances", "", "")],
  value=[S(L("Defesa no Magic", "Defence on the Magic item"), L("Transmutation/Augmentation até % Evasion/ES → Regal.", "Transmutation/Augmentation until % Evasion/ES → Regal."), ""), K.side_exalt("s", "resistências", "resistances"), K.quality("Armourer's Scrap", "")],
  lux=[K.side_exalt("p", "ES/Evasion T1", "T1 ES/Evasion"), K.divine]),
 "boots": dict(
  base="Corpsewade", targets=[[L("Unique", "Unique"), L("Nível da bota = nível do Decompose", "Boots level = Decompose level"), 58], [L("Sockets", "Sockets"), L("Perfect Jeweller's Orb: 5 sockets no Decompose", "Perfect Jeweller's Orb: 5 sockets on Decompose"), 1]],
  mats=["Perfect Jeweller's Orb", "Verisium", "Vaal Orb"],
  cheap=[K.trade("Corpsewade", "É barata no poe.ninja.", "It's cheap on poe.ninja.")],
  value=[S(L("Jeweller's no Decompose", "Jeweller's on Decompose"), L("O Decompose é gem da bota: Perfect Jeweller's Orb para 5 sockets.", "Decompose is the boots' gem: Perfect Jeweller's Orb for 5 sockets."), "")],
  lux=[K.runeforge("Corpsewade", "Verisium"), S(L("Corromper para mais sockets", "Corrupt for more sockets"), L("Compre uma de 2 sockets não corrompida e use Vaal Orb para tentar 3 (pode estragar).", "Buy an uncorrupted 2-socket one and Vaal Orb it to try for 3 (it can brick)."), "")]),
 "rings": dict(
  base=L("Prismatic Ring → Unset Ring.", "Prismatic Ring → Unset Ring."), targets=[[X, "+(15–16)% to all Elemental Resistances", 68]], mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb"],
  cheap=[K.trade("Ring · Resistances", "", "")], value=[K.side_exalt("s", "resistências", "resistances")], lux=[S("Unset Ring", L("Socket para runas úteis.", "Socket for useful runes."), "")]),
 "belt": dict(
  base="Heavy Belt", targets=[[P, "+(150–174) to maximum Life", 65]], mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb"],
  cheap=[K.trade("Belt · Life · Resistances", "", "")], value=[S("Shavronne's Satchel", L("Flask de vida também cura ES.", "Life flask also heals ES."), "")], lux=[S("Mageblood", L("Só no Uber.", "Only in Uber."), "")]),
 "life-flask": dict(
  base="Ultimate Life Flask", targets=[[P, "(76–80)% increased Amount Recovered", 83]], mats=["Orb of Transmutation", "Orb of Augmentation", "Glassblower's Bauble"],
  cheap=[S(L("Transmutation + Augmentation", "Transmutation + Augmentation"), L("Recuperação alta.", "High recovery."), "")], value=[S(L("Qualidade", "Quality"), L("Glassblower's Bauble até 20%.", "Glassblower's Bauble up to 20%."), "")], lux=[S(L("Carga por segundo", "Charges per second"), L("Para pinnacle, o sufixo 'gain 0.2 charges per second' mantém o flask.", "For pinnacles, the 'gain 0.2 charges per second' suffix keeps the flask up."), "")]),
 "charms": dict(
  base=L("Thawing, Stone e Dousing Charm.", "Thawing, Stone and Dousing Charm."), targets=[[P, "Charges / duration", 60]], mats=["Orb of Transmutation", "Orb of Augmentation"],
  cheap=[S(L("Charms normais", "Normal charms"), L("Freeze, Stun e Ignite.", "Freeze, Stun and Ignite."), "")], value=[S("For Utopia", L("Defende com 200% da Armour.", "Defend with 200% of Armour."), "")], lux=[S("For Utopia", L("Mantenha no Uber.", "Keep it in Uber."), "")]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
