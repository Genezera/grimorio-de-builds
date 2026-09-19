# -*- coding: utf-8 -*-
# Oficina de crafting do Legionnaire (executado dentro de bdata.py: usa L, BOOK). Tiers e ilvl do cache do PoE2DB (tools/dl/web/mods_*.json).
# Enxuta de propósito: só as quatro peças em que vale gastar currency (body e botas são unique).
import craftkit
K = craftkit.Kit(BOOK); S = K.S; P, X, DS, DP, C = K.P, K.X, K.D, K.DP, K.C

CK_ITEMS = [
 K.item("weapon", L("Cajado (Quarterstaff)", "Quarterstaff"), "Quarterstaves", L("Dano físico e elemental, velocidade de ataque e crítico: é a arma do Falling Thunder.", "Physical and elemental damage, attack speed and crit: it's the Falling Thunder weapon."),
        L("Uma base branca do vendor a cada salto (nível 16, 33 e 59); no endgame, ilvl 82.", "A white vendor base at each jump (level 16, 33 and 59); in endgame, ilvl 82."),
        L("Pare com dois mods de dano fortes e velocidade; + níveis de Attack é luxo.", "Stop with two strong damage mods and speed; + Attack levels are luxury."),
        L("Adonia's Ego fica no Weapon Set 2: não gaste currency nela.", "Adonia's Ego sits in Weapon Set 2: don't spend currency on it."),
        ["increased Physical Damage$", "Adds .* Lightning Damage$", "Adds .* Fire Damage$", "Elemental Damage with Attacks", "increased Attack Speed", "Critical Hit Chance"], ["Blood Spire"]),
 K.item("helmet", L("Capacete", "Helmet"), "Helmets_int", L("Energy Shield, vida, resistências e, se aparecer, + Power Charges máximas.", "Energy Shield, life, resistances and, if it shows up, + maximum Power Charges."),
        L("Base de Energy Shield (Int), ilvl 82.", "Energy Shield (Int) base, ilvl 82."), L("Vida + duas resistências já resolvem.", "Life + two resistances already do the job."),
        L("+ Power Charges máximas é implícito de corrupção: não dá para craftar.", "+ maximum Power Charges is a corruption implicit: it can't be crafted."),
        ["increased Energy Shield$", "to maximum Life$", "to Fire Resistance", "to Cold Resistance", "to Lightning Resistance"], []),
 K.item("amulet", L("Amuleto", "Amulet"), "Amulets", L("+ níveis de Melee e Spirit para o Eternal Rage.", "+ Melee levels and Spirit for Eternal Rage."),
        L("Absent Amulet ou base com Spirit, ilvl 75+.", "Absent Amulet or a Spirit base, ilvl 75+."), L("+3 níveis de Melee (ou +4 num corrompido) e vida.", "+3 Melee levels (or +4 on a corrupted one) and life."),
        L("O Eternal Rage do PoB vem do amuleto corrompido (100 Spirit): sem o Sacred Flame ele não cabe.", "The PoB's Eternal Rage comes from the corrupted amulet (100 Spirit): without Sacred Flame it doesn't fit."),
        ["Level of all Melee", "to Spirit$", "maximum Energy Shield", "maximum Life"], ["Brimstone Torc"]),
 K.item("gloves", L("Luvas", "Gloves"), "Gloves_dex_int", L("Dano adicionado a ataques (raio, fogo), vida e resistências.", "Added attack damage (lightning, fire), life and resistances."),
        L("Base Dex/Int (Energy Shield e Evasão), ilvl 75+.", "Dex/Int base (Energy Shield and Evasion), ilvl 75+."), L("Raio adicionado + vida + resistências.", "Added lightning + life + resistances."),
        L("A Runeforged Vaal Gloves do PoB tem +2 níveis de Melee (sufixo raro): não vale perseguir.", "The PoB's Runeforged Vaal Gloves has +2 Melee levels (a rare suffix): not worth chasing."),
        ["Adds .* Lightning damage to Attacks", "Adds .* Fire damage to Attacks", "to maximum Life$", "Level of all Melee"], ["Storm Fingers"]),
]

CK_DETAIL = {
 "weapon": dict(
  base=L("Cajado branco do vendor em cada salto; no endgame, Bolting Quarterstaff ilvl 82 (a base do PoB).", "White vendor quarterstaff at each jump; in endgame, ilvl 82 Bolting Quarterstaff (the PoB's base)."),
  targets=[[P, "(170–179)% increased Physical Damage (T2 155–169%)", "82 (75)"], [P, "Adds (37–55) to (63–94) Physical Damage", 75], [P, "Adds (1–19) to (310–358) Lightning Damage", 81], [P, "(120–139)% increased Elemental Damage with Attacks", 81], [X, "(26–28)% increased Attack Speed", 77], [X, "+(4.41–5)% to Critical Hit Chance", 73]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Perfect Essence of Battle", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Artificer's Orb", "Blacksmith's Whetstone"],
  cheap=[K.trade("Quarterstaff · % increased Elemental Damage with Attacks · Attack Speed · Adds Lightning", "No trade uma rare pronta costuma sair barata; compare com o custo do craft.", "On trade a finished rare is usually cheap; compare with the crafting cost.")],
  value=[S(L("Magic com um mod bom", "Magic with one good mod"), L("Base branca → Transmutation + Augmentation até sair dano físico/elemental ou velocidade. Só continue com um mod útil.", "White base → Transmutation + Augmentation until you get physical/elemental damage or speed. Only continue with a useful mod."), ""),
         S(L("Rare com Regal", "Rare with Regal"), L("Regal Orb mantém os mods e adiciona um.", "A Regal Orb keeps the mods and adds one."), ""),
         K.side_exalt("p", "dano físico e elemental", "physical and elemental damage"), K.side_exalt("s", "velocidade de ataque e crítico", "attack speed and crit"), K.quality("Blacksmith's Whetstone", "")],
  lux=[S(L("Perfect Essence of Battle (se faltar nível)", "Perfect Essence of Battle (if levels are missing)"), L("Num Rare, remove um mod aleatório e adiciona +3 níveis de Attack. Ocupa o único mod crafted.", "On a Rare, removes a random modifier and adds +3 Attack levels. It takes the only crafted mod."), ""), K.divine]),
 "helmet": dict(
  base=L("Capacete de Energy Shield (Int) ilvl 82.", "ilvl 82 Energy Shield (Int) helmet."),
  targets=[[P, "(92–100)% increased Energy Shield", 65], [P, "+(150–174) to maximum Life", 65], [X, "+(41–45)% Fire/Cold/Lightning Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Helmet (ES) · Life ≥ 100 · Total Resistance ≥ 60")],
  value=[S(L("Vida e ES no Magic", "Life and ES on the Magic item"), L("Base branca → Transmutation/Augmentation até vida ou % Energy Shield → Regal.", "White base → Transmutation/Augmentation until life or % Energy Shield → Regal."), ""), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.divine]),
 "amulet": dict(
  base=L("Absent Amulet (ou Solar Amulet, com Spirit).", "Absent Amulet (or Solar Amulet, with Spirit)."),
  targets=[[X, "+3 to Level of all Melee Skills", 75], [P, "+(47–50) to Spirit", 54], [P, "(7–8)% increased maximum Life", 75]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Greater Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation", "Divine Orb"],
  cheap=[K.trade("Amulet · Level of all Melee Skills ≥ 3 · Spirit")],
  value=[S(L("Spirit no Magic", "Spirit on the Magic item"), L("Base branca → Transmutation/Augmentation até Spirit (prefixo) → Regal.", "White base → Transmutation/Augmentation until Spirit (prefix) → Regal."), ""), K.side_exalt("s", "+ níveis de Melee", "+ Melee levels")],
  lux=[K.divine]),
 "gloves": dict(
  base=L("Luvas Dex/Int ilvl 75+.", "ilvl 75+ Dex/Int gloves."),
  targets=[[P, "Adds (1–4) to (60–71) Lightning damage to Attacks", 75], [P, "(39–42)% increased Evasion and Energy Shield / +(42–49) to maximum Life", 78], [X, "+(41–45)% Resistance", 82]],
  mats=["Orb of Transmutation", "Orb of Augmentation", "Regal Orb", "Exalted Orb", "Omen of Sinistral Exaltation", "Omen of Dextral Exaltation"],
  cheap=[K.trade("Gloves · Adds Lightning to Attacks · Life ≥ 80")],
  value=[S(L("Dano adicionado primeiro", "Added damage first"), L("Transmutation/Augmentation até raio adicionado → Regal.", "Transmutation/Augmentation until added lightning → Regal."), ""), K.side_exalt("p", "vida", "life"), K.side_exalt("s", "resistências", "resistances")],
  lux=[K.divine]),
}
CRAFT_KIT = dict(items=CK_ITEMS, detail=CK_DETAIL)
