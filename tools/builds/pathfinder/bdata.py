# -*- coding: utf-8 -*-
"""Pathfinder: poison bow no leveling (1–57) → Corpsewade Decompose no endgame. Base: guias do Skadoosh (Mobalytics, 0.5.5),
árvore/gems/itens das variantes, textos do jogo pelo Path of Building e preços do poe.ninja (Forbidden Rites)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("pathfinder")

GUIDE_URL = "https://mobalytics.gg/poe-2/builds/skadoosh-decompose-pathfinder"
LEVELING_URL = "https://mobalytics.gg/poe-2/builds/pathfinder-leveling-skadoosh"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "21/09/2026"
SOURCE_UPDATED = "20/09/2026"  # Mobalytics: build guide (verificado ao vivo via __PRELOADED_STATE__.updatedAt)
LEVELING_SOURCE_UPDATED = "06/09/2026"  # Mobalytics: guia de leveling
SNAPSHOT = "21/09/2026"  # data desta auditoria/conversão

CONFIG = dict(dir="pathfinder", build="pathfinder", store="pathfinder1", emoji="🧪", pill="Ranger · Pathfinder",
              fonts="family=Cinzel:wght@500;700;900&family=Alegreya+Sans+SC:wght@500;700&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400")
TXT = {
 "pt": dict(TITLE="Venom Trail", DESC="Guia interativo Pathfinder Poison Bow → Corpsewade Decompose (Ranger) — PoE 2 Forbidden Rites",
            H1S="Poison bow no leveling · Corpsewade Decompose no endgame · guias do Skadoosh explicados", H1="The Venom Trail",
            LEAD="Suba de nível com arco de veneno (Poisonburst Arrow, Toxic Growth, Contagion) e, no 58, vire o Pathfinder que envenena o mapa só andando: cada passo com Corpsewade solta Decompose nos corpos. Diga seu nível e o que você tem: o guia mostra skills, weapon sets, passivas e o Spirit dos dois sets."),
 "en": dict(TITLE="Venom Trail", DESC="Interactive Pathfinder Poison Bow → Corpsewade Decompose (Ranger) guide — PoE 2 Forbidden Rites",
            H1S="Poison bow while leveling · Corpsewade Decompose in endgame · Skadoosh's guides explained", H1="The Venom Trail",
            LEAD="Level with a poison bow (Poisonburst Arrow, Toxic Growth, Contagion) and, at 58, become the Pathfinder who poisons the map just by walking: every Corpsewade step casts Decompose on corpses. Tell it your level and what you have: the guide shows skills, weapon sets, passives and both sets' Spirit."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["quando", "Quando usar", "When to use"], ["mech", "Veneno & Decompose", "Poison & Decompose"],
        ["uniques", "Uniques", "Uniques"], ["arvore", "Árvore de Passivas", "Passive Tree"], ["rota", "Rota 1→100", "Route 1→100"], ["skills", "Skills & Supports", "Skills & Supports"],
        ["gear", "Itens", "Items"], ["asc", "Ascendência", "Ascendancy"], ["quests", "Quests", "Quests"], ["tricks", "Tricks Pro", "Pro Tricks"], ["atlas", "Atlas", "Atlas"],
        ["diag", "Diagnóstico", "Troubleshooting"], ["fontes", "Fontes", "Sources"]]

CLASS, ASC, START = "Ranger", "Pathfinder", 50459
ORDER = ["a1", "a2", "a3", "a4", "a5", "start", "end", "max"]
VMAP = {"a1": "pf_lvl: Level 1 - 10", "a2": "pf_lvl: Lvl 11 - 20", "a3": "pf_lvl: Lvl 21 - 30", "a4": "pf_lvl: Lvl 31 - 40", "a5": "pf_lvl: Lvl 41 - 58",
        "start": "pf_decomp: Starter", "end": "pf_decomp: Endgame", "max": "pf_decomp: Uber Endgame"}
VITEMS = {"start": ["pf_lvl: Lvl 41 - 58", "pf_decomp: Starter"]}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a4", "a5": "a5", "start": "start", "end": "start", "max": "end"}
FULLMAP = {k: k for k in ORDER}
PHASE_ACT = {"a1": 1, "a2": 2, "a3": 2, "a4": 3, "a5": 4, "start": 5, "end": 6, "max": 6}
BOW_RUNE = L("Iron Rune (% dano físico) — o veneno escala com físico", "Iron Rune (% physical damage) — poison scales with physical")

def socket_hint(slot, name):
    if "Bow" in name: return [BOW_RUNE]
    if slot in ("Capacete", "Body Armour", "Luvas", "Botas"):
        return [L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio) · resist no cap: Body Rune (vida)", "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning) · resists capped: Body Rune (life)")]
    return None

UHTRED_CONFLICT_NOTE = L("Uhtred's Augury: a FONTE tem informação conflitante. O changelog do patch 0.5 (22/05/2026) do próprio Skadoosh diz: \u201cUhtred's Augury now +2 to level of skill (was 3). Not really worth it anymore\u201d — mas a lista \u201cLineage gem priority\u201d na mesma página ainda o rankeia em 2º lugar (Arakaali's Lust > Uhtred's Augury > Uul-Netol's Embrace > ...), sem ter sido atualizada depois do nerf. Trate como Lineage OPCIONAL e de valor questionável no patch atual, não como upgrade garantido — compare o ganho real de nível antes de gastar nele.",
                            "Uhtred's Augury: the SOURCE has conflicting information. Skadoosh's own 0.5 patch changelog (22/05/2026) says: \u201cUhtred's Augury now +2 to level of skill (was 3). Not really worth it anymore\u201d — yet the \u201cLineage gem priority\u201d list on the same page still ranks it 2nd (Arakaali's Lust > Uhtred's Augury > Uul-Netol's Embrace > ...), never updated after the nerf. Treat it as OPTIONAL Lineage of questionable value in the current patch, not a guaranteed upgrade — compare the real level gain before spending on it.")
SUPWHY = {
 "Uhtred's Augury": UHTRED_CONFLICT_NOTE,
 "Escalating Poison": L("Aplica um veneno extra no alvo, com duração menor: mais stacks no Poisonburst Arrow.", "Applies an extra poison to the target with shorter duration: more stacks on Poisonburst Arrow."),
 "Concentrated Area": L("Área menor, dano maior.", "Smaller area, higher damage."),
 "Swift Affliction I": L("Mais dano de dano-ao-longo-do-tempo (não-ailment) com duração menor: planta do Vine Arrow bate mais.", "More non-ailment damage over time with shorter duration: Vine Arrow's plant hits harder."),
 "Deadly Poison I": L("Menos dano de hit, veneno bem mais forte.", "Less hit damage, much stronger poison."),
 "Deadly Poison II": L("Versão mais forte: é o support central de qualquer skill de veneno da build.", "Stronger version: the core support on every poison skill in the build."),
 "Shock": L("Mais chance de Shock: o Stormcaller Arrow deixa o boss tomando mais dano.", "Higher Shock chance: Stormcaller Arrow makes the boss take more damage."),
 "Corrosion": L("O veneno também quebra Armour: Exploit Weakness e Mace de Fully Broken Armour aproveitam.", "Poison also breaks Armour: Exploit Weakness and the Fully Broken Armour mace take advantage."),
 "Short Fuse I": L("As pústulas do Toxic Growth detonam mais cedo.", "Toxic Growth's pustules detonate sooner."),
 "Long Fuse II": L("Pústulas demoram mais para detonar, mas explodem bem mais forte — ótimo no boss parado.", "Pustules take longer to detonate but explode much harder — great on a standing boss."),
 "Persistent Ground II": L("A nuvem do Gas Arrow dura muito mais.", "Gas Arrow's cloud lasts much longer."),
 "Persistent Ground III": L("Nuvens do Decompose duram mais e reduzem a recuperação de cooldown dos inimigos.", "Decompose clouds last longer and slow enemies' cooldown recovery."),
 "Multishot I": L("Mais flechas de gás por uso.", "More gas arrows per use."),
 "Multishot II": L("Versão mais forte do Multishot.", "Stronger Multishot."),
 "Magnified Area I": L("Área maior.", "Larger area."),
 "Magnified Area II": L("Área ainda maior.", "Even larger area."),
 "Bursting Plague": L("Inimigos envenenados acumulam Plague e explodem ao morrer: cadeia de mortes no pack.", "Poisoned enemies gain Plague and explode on death: a chain of kills through the pack."),
 "Poison II": L("Chance de veneno no Plague Bearer.", "Poison chance on Plague Bearer."),
 "Poison III": L("Chance de veneno e veneno mais forte contra inimigos sangrando.", "Poison chance and stronger poison against bleeding enemies."),
 "Efficiency II": L("Custa menos mana.", "Costs less mana."),
 "Lasting Shock": L("Shock menos frequente, mas dura mais: fica ativo no boss.", "Less frequent Shock that lasts longer: stays up on bosses."),
 "Impale": L("Toxic Domain passa a dar Impale.", "Toxic Domain now Impales."),
 "Encroaching Ground": L("A nuvem do Decompose cresce com o tempo.", "Decompose's cloud grows over time."),
 "Exploit Weakness": L("Mais dano contra inimigos com Armour quebrada (a Corrosion quebra).", "More damage against enemies with broken Armour (Corrosion breaks it)."),
 "Prolonged Duration II": L("Mais duração.", "Longer duration."),
 "Minion Mastery": L("+1 nível nos minions: Blood Elemental com mais vida = Decompose mais forte.", "+1 level to minions: a Blood Elemental with more life = stronger Decompose."),
 "Hulking Minions": L("Minions maiores com mais vida e dano (custam bem mais Spirit). Mais vida no Blood Elemental = nuvem mais forte.", "Bigger minions with more life and damage (much higher Spirit cost). More Blood Elemental life = a stronger cloud."),
 "Heightened Curse": L("Curse mais forte.", "Stronger curse."),
 "Focused Curse": L("Curse aplica mais rápido.", "Curse applies faster."),
 "Ritualistic Curse": L("Curse com área maior, mais lenta para aplicar.", "Larger curse area, slower to apply."),
 "Cursed Ground": L("A curse vira uma área no chão que amaldiçoa quem entrar.", "The curse becomes a ground area that curses whoever enters."),
 "Expand": L("Spells ganham Seals; ao lançar, a área cresce.", "Spells gain Seals; casting breaks them for more area."),
 "Rapid Casting I": L("Conjura mais rápido.", "Casts faster."),
 "Rapid Casting II": L("Versão mais forte.", "Stronger version."),
 "Harmonic Remnants II": L("Remnants do Grim Feast de mais longe e às vezes um extra.", "Grim Feast remnants from further away and sometimes an extra one."),
 "Remnant Potency I": L("Remnants mais fortes.", "Stronger remnants."),
 "Herbalism II": L("Mais cura dos flasks de vida enquanto a aura está ativa.", "More life flask healing while the aura is active."),
 "Cooldown Recovery II": L("Ghost Shroud volta mais rápido.", "Ghost Shroud comes back faster."),
 "Blind II": L("Cega inimigos acertados.", "Blinds enemies hit."),
 "Chaos Mastery": L("+1 nível em skills de Chaos.", "+1 level to Chaos skills."),
 "Contagion": L("Gem de SKILL no Cast on Minion Death: Contagion dispara quando seus minions morrem.", "SKILL gem in Cast on Minion Death: Contagion triggers when your minions die."),
 "Entangle": L("Gem de SKILL no Cast on Minion Death: vinhas que prendem e dão Critical Weakness.", "SKILL gem in Cast on Minion Death: vines that bind and apply Critical Weakness."),
 "Temporal Chains": L("Curse no Blasphemy: deixa os inimigos lentos (e efeitos neles duram mais).", "Curse in Blasphemy: slows enemies (and effects on them last longer)."),
 "Enfeeble": L("Curse no Blasphemy: inimigos causam menos dano.", "Curse in Blasphemy: enemies deal less damage."),
 "Acrimony": L("Reduz a regeneração de vida dos inimigos com dano ao longo do tempo.", "Reduces enemy life regeneration from damage over time."),
 "Bleed III": L("Causa Bleeding: com Poison III o veneno fica mais forte.", "Inflicts Bleeding: with Poison III poison gets stronger."),
 "Maim": L("Maim nos inimigos.", "Maims enemies."),
 "Mobility": L("Anda mais rápido usando o skill.", "Move faster while using the skill."),
 "Arakaali's Lust": L("Lineage: dano maior quanto mais venenos no alvo.", "Lineage: more damage the more poisons are on the target."),
 "Vorana's Siege": L("Lineage: área maior e hits mais fortes em alvo isolado.", "Lineage: larger area and harder hits on isolated targets."),
 "Uul-Netol's Embrace": L("Lineage: Chaos extra e o Chaos passa a quebrar Armour.", "Lineage: extra Chaos and Chaos damage breaks Armour."),
 "Dialla's Desire": L("Lineage: mais nível e qualidade, menos custo e reserva.", "Lineage: more level and quality, less cost and reservation."),
  "Uhtred's Omen": L("Lineage: níveis extras se o skill tiver exatamente 1 outro support.", "Lineage: extra levels if the skill has exactly 1 other support."),
 "Kurgal's Leash": L("Lineage: você e o minion comandado ganham Unholy Might.", "Lineage: you and the commanded minion gain Unholy Might."),
 "Brutus' Brain": L("Lineage: o minion não causa nem recebe dano (Skeletal Sniper só para o buff).", "Lineage: the minion can't deal or take damage (Skeletal Sniper just for the buff)."),
 "Atziri's Allure": L("Lineage: curses ignoram o limite, mas são refletidas em você.", "Lineage: curses ignore the curse limit but are reflected onto you."),
 "Her Declaration": L("Lineage: inimigos que entram na Presence ficam Intimidated.", "Lineage: enemies entering your Presence become Intimidated."),
}

SP30 = L("30 Spirit", "30 Spirit")
PHASES = [
 dict(id="a1", name=L("Nível 1–10", "Level 1–10"), lv=[1, 10], tag=L("Poisonburst Arrow + Contagion", "Poisonburst Arrow + Contagion"),
  carry=L("Você: Poisonburst Arrow + Contagion", "You: Poisonburst Arrow + Contagion"), dmgSplit=[100, 0],
  goal=L("Arco de veneno desde o começo. No pack: Contagion num inimigo e Poisonburst Arrow nele — quando ele morre, o Contagion espalha o veneno. Stormcaller Arrow dá dano no boss antes das outras skills. Vine Arrow (crie e deixe no nível 1) segura e envenena. Transmutation e Augmentation em arcos brancos já são upgrade.",
         "Poison bow from the start. On packs: Contagion on one enemy and Poisonburst Arrow on it — when it dies, Contagion spreads the poison. Stormcaller Arrow gives boss damage before your other skills. Vine Arrow (create it and keep it level 1) holds and poisons. Transmutation and Augmentation on white bows are already upgrades."),
  rotation=[L("Contagion no inimigo mais resistente", "Contagion on the toughest enemy"), L("Poisonburst Arrow nele", "Poisonburst Arrow on it"), L("Vine Arrow para segurar", "Vine Arrow to hold them"), L("Boss: Stormcaller Arrow + Poisonburst", "Boss: Stormcaller Arrow + Poisonburst")],
  gems=[
   G("Poisonburst Arrow", ["Escalating Poison", "Concentrated Area"], L("Dano principal", "Main damage"), L("Flecha que explode em veneno numa área ao acertar.", "An arrow that bursts into poison in an area on hit."), "free"),
   G("Contagion", [], L("Espalha o veneno", "Spreads poison"), L("Quando o alvo morre, o Contagion espalha ele, as curses e o veneno para os vizinhos.", "When the target dies, Contagion spreads itself, curses and poison to nearby enemies."), "free"),
   G("Vine Arrow", ["Swift Affliction I"], L("Controle", "Control"), L("Planta que prende e causa Chaos ao longo do tempo. Pode ser envenenada.", "A plant that latches on and deals Chaos over time. It can be poisoned."), "free"),
   G("Stormcaller Arrow", [], L("Boss (início)", "Boss (early)"), L("Raio com Shock no ponto de impacto. Dano de boss antes das outras skills.", "Lightning with Shock at the impact point. Boss damage before other skills."), "free"),
  ],
  cheap=[L("Arco com dano físico (Transmutation/Augmentation)", "Bow with physical damage (Transmutation/Augmentation)"), "Surefooted Sigil (8)", "Goldrim (10)"],
  full=[L("Mesmo do barato: nada mais dropa a esse nível", "Same as budget: nothing else drops this early")],
  stats=[L("% dano físico e físico adicionado", "% physical damage and added physical"), L("+ nível de projéteis", "+ projectile levels"), L("Movement Speed", "Movement Speed"), L("Vida", "Life")],
  tree=L("Nós de projétil e veneno perto do início da Ranger.", "Projectile and poison nodes near the Ranger start."),
  avoid=[L("Achar que dano elemental ajuda o veneno (só físico e Chaos)", "Thinking elemental damage helps poison (only physical and Chaos)")],
  exit=[L("Contagion + Poisonburst Arrow limpando packs", "Contagion + Poisonburst Arrow clearing packs")]),

 dict(id="a2", name=L("Nível 11–20", "Level 11–20"), lv=[11, 20], tag=L("Plague Bearer + weapon sets", "Plague Bearer + weapon sets"),
  carry=L("Você: Poisonburst Arrow + Plague Bearer", "You: Poisonburst Arrow + Plague Bearer"), dmgSplit=[100, 0],
  goal=L("Plague Bearer guarda parte do veneno que você causa e solta tudo de uma vez: use para limpar um pack grande ou um inimigo forte (o veneno ainda espalha com o Contagion). Começam os weapon sets: Set 1 (rosa) = Poisonburst, Vine, Contagion e Plague Bearer; Set 2 (verde) = Stormcaller Arrow. Tenha arco e aljava nos DOIS sets.",
         "Plague Bearer stores part of the poison you deal and releases it all at once: use it to clear a big pack or a strong enemy (the poison still spreads with Contagion). Weapon sets begin: Set 1 (pink) = Poisonburst, Vine, Contagion and Plague Bearer; Set 2 (green) = Stormcaller Arrow. Have a bow and quiver on BOTH sets."),
  rotation=[L("Set 2: Stormcaller Arrow (Shock) no boss", "Set 2: Stormcaller Arrow (Shock) on the boss"), L("Set 1: Contagion + Poisonburst Arrow", "Set 1: Contagion + Poisonburst Arrow"), L("Plague Bearer cheio: solte no pack/boss", "Plague Bearer full: release it on the pack/boss")],
  gems=[
   G("Poisonburst Arrow", ["Escalating Poison", "Deadly Poison I"], L("Dano principal · Set 1", "Main damage · Set 1"), L("Deadly Poison I troca hit por veneno mais forte.", "Deadly Poison I trades hit damage for stronger poison."), "free"),
   G("Vine Arrow", ["Swift Affliction I"], L("Controle · Set 1", "Control · Set 1"), L("Igual.", "Same."), "free"),
   G("Stormcaller Arrow", ["Shock"], L("Shock no boss · Set 2", "Shock on bosses · Set 2"), L("Shock = inimigo toma mais dano de tudo.", "Shock = the enemy takes more damage from everything."), "free"),
   G("Contagion", [], L("Espalha · Set 1", "Spreads · Set 1"), L("Igual.", "Same."), "free"),
   G("Plague Bearer", ["Concentrated Area"], L("Burst de veneno · Set 1", "Poison burst · Set 1"), L("Guarda o veneno e solta numa nova. Reserva 30 Spirit (King in the Mists).", "Stores poison and releases it in a nova. Reserves 30 Spirit (King in the Mists)."), "core", 1, SP30),
  ],
  cheap=["Wanderlust (11)", "Splinterheart (16)"],
  full=["Ghostmarch (16)", "The Lethal Draw (16)"],
  stats=[L("% físico / físico adicionado", "% physical / added physical"), L("+ nível de projéteis", "+ projectile levels"), L("Attack speed", "Attack speed")],
  tree=L("Pontos de Weapon Set: rosa = Set 1, verde = Set 2. Para usar um ponto de set você precisa de um ponto normal livre.", "Weapon Set points: pink = Set 1, green = Set 2. To use a set point you need a free normal point."),
  avoid=[L("Esquecer arco/aljava no Set 2", "Forgetting a bow/quiver on Set 2")],
  exit=[L("Plague Bearer ligado", "Plague Bearer on"), L("Skills atribuídas ao set certo (tecla G)", "Skills assigned to the right set (G key)")]),

 dict(id="a3", name=L("Nível 21–30", "Level 21–30"), lv=[21, 30], tag=L("Toxic Growth + Gas Arrow", "Toxic Growth + Gas Arrow"),
  carry=L("Você: Toxic Growth nas nuvens do Gas Arrow", "You: Toxic Growth on Gas Arrow clouds"), dmgSplit=[100, 0],
  goal=L("Toxic Growth vira o dano principal: chuva de pústulas que detonam — e explodem mais rápido e mais forte quando envenenadas. Antes, cubra a área com 2+ nuvens do Gas Arrow (mais venenos nas pústulas = mais dano). Poisonburst Arrow passa a só aplicar Corrosion para quebrar Armour. Primeira ascendência: Relentless Pursuit (sua velocidade ignora Slows).",
         "Toxic Growth becomes your main damage: a rain of pustules that detonate — faster and harder when poisoned. First cover the area with 2+ Gas Arrow clouds (more poisons on the pustules = more damage). Poisonburst Arrow now only applies Corrosion to break Armour. First ascendancy: Relentless Pursuit (your speed ignores Slows)."),
  rotation=[L("Gas Arrow 2x na área", "Gas Arrow twice on the area"), L("Poisonburst Arrow uma vez (Corrosion quebra Armour)", "Poisonburst Arrow once (Corrosion breaks Armour)"), L("Toxic Growth em cima das nuvens", "Toxic Growth on top of the clouds"), L("Plague Bearer cheio no final", "Plague Bearer when full")],
  gems=[
   G("Toxic Growth", ["Short Fuse I", "Concentrated Area"], L("Dano principal · Set 1", "Main damage · Set 1"), L("Pústulas que detonam; envenenadas detonam antes e mais forte.", "Pustules that detonate; poisoned ones detonate sooner and harder."), "free"),
   G("Gas Arrow", ["Persistent Ground II", "Multishot I"], L("Nuvens de veneno · Set 1", "Poison clouds · Set 1"), L("Flecha que cria nuvem de gás inflamável; envenena as pústulas.", "Arrow that creates a flammable gas cloud; poisons the pustules."), "free"),
   G("Poisonburst Arrow", ["Escalating Poison", "Corrosion"], L("Armour Break · Set 1", "Armour Break · Set 1"), L("Corrosion: o veneno quebra Armour.", "Corrosion: poison breaks Armour."), "free"),
   G("Stormcaller Arrow", ["Shock"], L("Shock · Set 2", "Shock · Set 2"), L("Igual.", "Same."), "free"),
   G("Contagion", ["Magnified Area I"], L("Espalha · Set 1", "Spreads · Set 1"), L("Área maior para espalhar.", "Larger spread area."), "free"),
   G("Plague Bearer", ["Bursting Plague", "Poison II"], L("Burst · Set 1", "Burst · Set 1"), L("Bursting Plague: inimigos envenenados explodem ao morrer.", "Bursting Plague: poisoned enemies explode on death."), "core", 1, SP30),
  ],
  cheap=["Death's Harp (28)", L("Resistências equilibradas", "Balanced resistances")],
  full=[L("Blacksmith's Whetstone até 20% no arco", "Blacksmith's Whetstone to 20% on the bow")],
  stats=[L("% físico / físico adicionado", "% physical / added physical"), L("+ nível de projéteis", "+ projectile levels"), L("Attack speed", "Attack speed"), L("Resistências", "Resistances")],
  tree=L("Nós de veneno e projétil; a respec dos pontos de Set 2 vai para o Stormcaller.", "Poison and projectile nodes; Set 2 points get respecced toward Stormcaller."),
  avoid=[L("Toxic Growth sem nuvens por baixo", "Toxic Growth without clouds underneath")],
  exit=[L("1ª ascendência: Relentless Pursuit", "1st ascendancy: Relentless Pursuit"), L("Lesser Jeweller's Orb no Toxic Growth (Sandswept Marsh)", "Lesser Jeweller's Orb on Toxic Growth (Sandswept Marsh)")]),

 dict(id="a4", name=L("Nível 31–40", "Level 31–40"), lv=[31, 40], tag=L("Path Seeker + Herald of Plague", "Path Seeker + Herald of Plague"),
  carry=L("Você: Toxic Growth + Plague Bearer", "You: Toxic Growth + Plague Bearer"), dmgSplit=[100, 0],
  goal=L("Segunda ascendência (Trial of Chaos): Path Seeker — escolha a área inicial da Witch/Sorceress. Herald of Plague espalha veneno de inimigos mortos e dá Hinder. Guarde supports e Lesser Jeweller's Orbs extras para o Decompose do 58. Venom Draught: escolha Stun Threshold.",
         "Second ascendancy (Trial of Chaos): Path Seeker — pick the Witch/Sorceress starting area. Herald of Plague spreads poison from killed enemies and Hinders. Keep spare supports and Lesser Jeweller's Orbs for the level 58 Decompose swap. Venom Draught: pick Stun Threshold."),
  rotation=[L("Gas Arrow → Poisonburst → Toxic Growth", "Gas Arrow → Poisonburst → Toxic Growth"), L("Herald of Plague limpa em cadeia", "Herald of Plague chain-clears"), L("Plague Bearer no boss", "Plague Bearer on bosses")],
  gems=[
   G("Toxic Growth", ["Short Fuse I", "Concentrated Area", "Efficiency II"], L("Dano principal · Set 1", "Main damage · Set 1"), L("3 links com o primeiro Lesser Jeweller's Orb.", "3 links with your first Lesser Jeweller's Orb."), "free"),
   G("Gas Arrow", ["Persistent Ground II", "Multishot II"], L("Nuvens · Set 1", "Clouds · Set 1"), L("Multishot II: mais nuvens.", "Multishot II: more clouds."), "free"),
   G("Poisonburst Arrow", ["Escalating Poison", "Corrosion"], L("Armour Break · Set 1", "Armour Break · Set 1"), L("Igual.", "Same."), "free"),
   G("Stormcaller Arrow", ["Shock", "Lasting Shock"], L("Shock · Set 2", "Shock · Set 2"), L("Lasting Shock mantém o Shock no boss.", "Lasting Shock keeps Shock up on bosses."), "free"),
   G("Contagion", ["Magnified Area I"], L("Espalha · Set 1", "Spreads · Set 1"), L("Igual.", "Same."), "free"),
   G("Plague Bearer", ["Bursting Plague", "Poison II"], L("Burst · Set 1", "Burst · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Herald of Plague", [], L("Clear em cadeia (opcional)", "Chain clear (optional)"), L("Matar inimigo envenenado espalha o veneno e dá Hinder. 30 Spirit (Azak Bog). O próprio Skadoosh testou e confirmou: NÃO é obrigatório para o clear — dá para deixar de fora e usar o Spirit em defesa (ele mesmo cita Desert Buckler como alternativa).", "Killing a poisoned enemy spreads poison and Hinders. 30 Spirit (Azak Bog). Skadoosh himself tested and confirmed it: NOT required for clear — you can skip it and spend that Spirit on defence instead (he cites Desert Buckler as the alternative)."), "opt", 1, SP30),
  ],
  cheap=["Slivertongue (39)", "Snakebite (33)"],
  full=[L("Supports extras guardados para o 58", "Spare supports saved for level 58")],
  stats=[L("% físico / físico adicionado", "% physical / added physical"), L("+ nível de projéteis", "+ projectile levels"), L("Resistências", "Resistances"), L("Vida", "Life")],
  tree=L("Path Seeker liga a área inicial da Witch/Sorceress; respec dos pontos pequenos em volta.", "Path Seeker connects the Witch/Sorceress start area; respec the small points around it."),
  avoid=[L("Gastar os Lesser Jeweller's Orbs que o Decompose vai precisar", "Spending the Lesser Jeweller's Orbs Decompose will need")],
  exit=[L("2ª ascendência: Path Seeker", "2nd ascendancy: Path Seeker"), L("Herald of Plague ligado", "Herald of Plague on")]),

 dict(id="a5", name=L("Nível 41–57", "Level 41–57"), lv=[41, 57], tag=L("Toxic Domain + preparar o Decompose", "Toxic Domain + prepare Decompose"),
  carry=L("Você: Toxic Growth + Plague Bearer", "You: Toxic Growth + Plague Bearer"), dmgSplit=[100, 0],
  goal=L("Toxic Domain cria uma área onde seus ataques de projétil grudam pústulas que detonam com veneno. Long Fuse II deixa o Toxic Growth mais forte no boss. Principal tarefa: preparar a troca do nível 58 — compre Corpsewade (já pode equipar: ela funciona desde o nível 11 como bônus passivo, mas só vira dano principal com Sacrifice no 58) e Snakebite (baratos), um Blood Elemental para o Bind Spectre (encontrado a partir do Aggorat, Ato 3), um Trenchtimbre e guarde gold para o respec. Act 4 e Interlúdio: pegue as resistências.",
         "Toxic Domain creates an area where your projectile attacks attach pustules that detonate with poison. Long Fuse II makes Toxic Growth stronger on bosses. Main task: prepare the level 58 swap — buy Corpsewade (you can already equip it: it works from level 11 as a passive bonus, but only becomes main damage with Sacrifice at 58) and Snakebite (cheap), a Blood Elemental for Bind Spectre (found from Aggorat, Act 3), a Trenchtimbre and save gold for the respec. Act 4 and Interludes: take the resistances."),
  rotation=[L("Toxic Domain no chão", "Toxic Domain on the ground"), L("Gas Arrow → Poisonburst → Toxic Growth", "Gas Arrow → Poisonburst → Toxic Growth"), L("Plague Bearer cheio", "Plague Bearer when full")],
  gems=[
   G("Toxic Growth", ["Long Fuse II", "Concentrated Area", "Efficiency II"], L("Dano principal · Set 1", "Main damage · Set 1"), L("Long Fuse II: detonação mais lenta e bem mais forte. Se não estiver explodindo rápido, volte para o Poisonburst.", "Long Fuse II: slower, much stronger detonation. If it isn't blowing up fast, go back to Poisonburst."), "free"),
   G("Gas Arrow", ["Persistent Ground II", "Multishot II"], L("Nuvens · Set 1", "Clouds · Set 1"), L("Igual.", "Same."), "free"),
   G("Poisonburst Arrow", ["Escalating Poison", "Corrosion"], L("Armour Break · Set 1", "Armour Break · Set 1"), L("Igual.", "Same."), "free"),
   G("Stormcaller Arrow", ["Shock", "Lasting Shock"], L("Shock · Set 2", "Shock · Set 2"), L("Igual.", "Same."), "free"),
   G("Contagion", [], L("Espalha · Set 1", "Spreads · Set 1"), L("Igual.", "Same."), "free"),
   G("Plague Bearer", ["Bursting Plague", "Poison II", "Deadly Poison II"], L("Burst · Set 1", "Burst · Set 1"), L("Deadly Poison II: burst bem mais forte.", "Deadly Poison II: a much stronger burst."), "core", 1, SP30),
   G("Herald of Plague", [], L("Clear em cadeia (opcional)", "Chain clear (optional)"), L("30 Spirit. Não é obrigatório para o clear (testado pelo Skadoosh) — dá para trocar por defesa.", "30 Spirit. Not required for clear (tested by Skadoosh) — can be swapped for defence."), "opt", 1, SP30),
   G("Toxic Domain", ["Magnified Area I", "Impale"], L("Dano extra no boss", "Extra boss damage"), L("Opcional: mais um botão para dano e regen no boss.", "Optional: one more button for boss damage and regen."), "free"),
  ],
  cheap=[L("Corpsewade + Snakebite (compre antes do 58)", "Corpsewade + Snakebite (buy before 58)"), L("Trenchtimbre", "Trenchtimbre")],
  full=[L("Stoic Sceptre com Spirit nos dois sets", "Stoic Sceptre with Spirit on both sets"), L("Gold guardado para o respec", "Gold saved for the respec")],
  stats=[L("Resistências (+50% no fim da campanha)", "Resistances (+50% by the end of the campaign)"), L("Chaos Resistance ≥ 0", "Chaos Resistance ≥ 0"), L("Vida", "Life")],
  tree=L("Tudo até o 58 fica pronto para o respec do Decompose.", "Everything up to 58 gets ready for the Decompose respec."),
  avoid=[L("Chegar no 58 sem Corpsewade", "Reaching 58 without Corpsewade"), L("Apostar todo o gold", "Gambling away all your gold")],
  exit=[L("Corpsewade, Snakebite, Trenchtimbre", "Corpsewade, Snakebite, Trenchtimbre"), L("Blood Elemental capturável", "A capturable Blood Elemental"), L("Gold para o respec", "Gold for the respec")]),

 dict(id="start", name=L("Decompose: início (58+)", "Decompose: start (58+)"), lv=[58, 64], tag=L("Corpsewade + Blood Elemental", "Corpsewade + Blood Elemental"),
  carry=L("Corpsewade: Decompose a cada passo", "Corpsewade: Decompose every step"), dmgSplit=[40, 60],
  goal=L("Corpsewade dispara Decompose a cada 1,2 m andados (ela já podia estar equipada desde o nível 11 — o que muda agora é o Sacrifice, obrigatório e liberado só no 58): consome corpos e cria nuvens de veneno que causam dano baseado na vida do monstro que morreu. Com Sacrifice, seus próprios minions (Blood Elemental do Bind Spectre) servem de corpo. Weapon Set 1 = auras e debuffs (Plague Bearer, Despair, Contagion, Withering Presence, Herald of Plague); Weapon Set 2 = Trenchtimbre + Bind Spectre. Troque de set para invocar os Blood Elementals e ande em cima deles. Respec: primeiro pegue e depois solte a área inicial da árvore.",
         "Corpsewade triggers Decompose every 1.2 m travelled (it could already be equipped from level 11 — what changes now is Sacrifice, mandatory and unlocked only at 58): it consumes corpses and creates poison clouds that deal damage based on the dead monster's life. With Sacrifice your own minions (Bind Spectre's Blood Elemental) count as corpses. Weapon Set 1 = auras and debuffs (Plague Bearer, Despair, Contagion, Withering Presence, Herald of Plague); Weapon Set 2 = Trenchtimbre + Bind Spectre. Swap sets to summon the Blood Elementals and walk over them. Respec: first allocate, then deallocate the tree's starting area."),
  rotation=[L("Set 2: invoque os Blood Elementals", "Set 2: summon the Blood Elementals"), L("Ande: Corpsewade consome e cria nuvens", "Walk: Corpsewade consumes them and creates clouds"), L("Set 1: Despair + Contagion + Plague Bearer", "Set 1: Despair + Contagion + Plague Bearer"), L("Packs: Plague Bearer mata alguns; as nuvens limpam o resto", "Packs: Plague Bearer kills some; clouds clean up the rest")],
  gems=[
   G("Decompose", ["Persistent Ground III", "Deadly Poison II", "Exploit Weakness", "Prolonged Duration II"], L("Dano principal (Corpsewade)", "Main damage (Corpsewade)"), L("Vem das botas: nível da Corpsewade = nível do skill e sockets. Nuvens de veneno inflamável que escalam com a vida do corpo.", "Comes from the boots: Corpsewade's level = skill level and sockets. Flammable poison clouds that scale with the corpse's life."), "free"),
   G("Plague Bearer", ["Magnified Area II", "Deadly Poison II", "Corrosion"], L("Clear de packs · Set 1", "Pack clear · Set 1"), L("Mata parte do pack para o Decompose ter corpos.", "Kills part of the pack so Decompose has corpses."), "core", 1, SP30),
   G("Bind Spectre", ["Minion Mastery"], L("Blood Elemental · Set 2", "Blood Elemental · Set 2"), L("Minion com muita vida: com Sacrifice vira combustível para nuvens fortes. Configure a quantidade só no Set 2.", "A high-life minion: with Sacrifice it becomes fuel for strong clouds. Set the summon amount on Set 2 only."), "core", 2, L("Blood Elemental ≈ 67 Spirit (PoE2DB)", "Blood Elemental ≈ 67 Spirit (PoE2DB)")),
   G("Sacrifice", [], L("Minions viram corpos", "Minions become corpses"), L("Seus minions revivíveis podem ser usados como corpos (revivem mais devagar). 60 Spirit.", "Your reviving minions can be used as corpses (they revive more slowly). 60 Spirit."), "core", 3, L("60 Spirit", "60 Spirit")),
   G("Despair", ["Heightened Curse"], L("Curse · Set 1", "Curse · Set 1"), L("Menos resistência a Chaos. Mantenha no nível máximo possível.", "Lowers Chaos resistance. Keep it at the highest level possible."), "free"),
   G("Contagion", ["Expand", "Rapid Casting II"], L("Espalha · Set 1", "Spreads · Set 1"), L("Lance manualmente para espalhar venenos mais rápido; pode ficar em nível baixo.", "Cast manually to spread poisons faster; it can stay low level."), "free"),
   G("Withering Presence", ["Prolonged Duration II"], L("Wither · Set 1", "Wither · Set 1"), L("Aura que aplica Wither (mais dano de Chaos recebido).", "Aura that applies Wither (more Chaos damage taken)."), "core", 4, SP30),
   G("Herald of Plague", [], L("Clear em cadeia · Set 1 (opcional)", "Chain clear · Set 1 (optional)"), L("30 Spirit. Não é obrigatório para o clear (testado pelo Skadoosh) — dá para trocar por defesa (ex.: Desert Buckler).", "30 Spirit. Not required for clear (tested by Skadoosh) — can be swapped for defence (e.g. Desert Buckler)."), "opt", 1, SP30),
  ],
  cheap=["Corpsewade", "Snakebite", "Trenchtimbre", L("Stoic Sceptre nos dois sets", "Stoic Sceptre on both sets")],
  full=[L("Brigand Mace (Set 1) com Perfect Essence of Abrasion", "Brigand Mace (Set 1) with Perfect Essence of Abrasion"), L("Solar Amulet com Spirit", "Solar Amulet with Spirit")],
  stats=[L("Resistências elementais 75% (Chaos não precisa)", "Elemental resistances 75% (Chaos not needed)"), L("Spirit", "Spirit"), L("Energy Shield e Evasion", "Energy Shield and Evasion"), L("+ nível de minions", "+ minion levels")],
  tree=L("Mix de Destreza e Inteligência. Não pegue Overwhelming Toxicity antes de sustentar o máximo de venenos.", "Mix of Dexterity and Intelligence. Don't take Overwhelming Toxicity before you can sustain max poisons."),
  avoid=[L("Começar antes do 58 ou sem Corpsewade", "Starting before 58 or without Corpsewade"), L("Deixar Bind Spectre invocando nos dois sets", "Leaving Bind Spectre summoning on both sets")],
  exit=[L("Blood Elementals invocados no Set 2", "Blood Elementals summoned on Set 2"), L("3ª ascendência: Enduring Elixirs", "3rd ascendancy: Enduring Elixirs")]),

 dict(id="end", name=L("Endgame (65+)", "Endgame (65+)"), lv=[65, 79], tag=L("Overwhelming Toxicity + Traveller's Wisdom", "Overwhelming Toxicity + Traveller's Wisdom"),
  carry=L("Corpsewade: Decompose · Plague Bearer", "Corpsewade: Decompose · Plague Bearer"), dmgSplit=[40, 60],
  goal=L("Overwhelming Toxicity dobra o número de venenos no alvo (com 50% less duração) e Traveller's Wisdom transforma cada nó de atributo em 5% de dano ou defesa. Blasphemy com Temporal Chains deixa tudo em câmera lenta; Ghost Dance e Wind Dancer dão defesa. Grim Feast (Set 2) revive os minions mais rápido. Até 10 venenos por alvo: mais nuvens enchem o máximo mais rápido — não aumentam o dano por veneno.",
         "Overwhelming Toxicity doubles the number of poisons on a target (with 50% less duration) and Traveller's Wisdom turns every attribute node into 5% damage or defence. Blasphemy with Temporal Chains slows everything to a crawl; Ghost Dance and Wind Dancer give defence. Grim Feast (Set 2) revives minions faster. Up to 10 poisons per target: more clouds reach the cap faster — they don't raise damage per poison."),
  rotation=[L("Pré-carregue nuvens antes do boss (troque de set fora de combate)", "Pre-load clouds before the boss (swap sets out of combat)"), L("Em combate: spam de Grim Feast no Set 2 para reviver", "In combat: spam Grim Feast on Set 2 to revive"), L("Set 1: Contagion + Plague Bearer", "Set 1: Contagion + Plague Bearer")],
  gems=[
   G("Decompose", ["Persistent Ground III", "Deadly Poison II", "Prolonged Duration II", "Exploit Weakness", "Encroaching Ground"], L("Dano principal", "Main damage"), L("Encroaching Ground: a nuvem cresce.", "Encroaching Ground: the cloud grows."), "free"),
   G("Plague Bearer", ["Deadly Poison II", "Bursting Plague", "Poison III", "Corrosion"], L("Clear · Set 1", "Clear · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Bind Spectre", ["Minion Mastery", "Hulking Minions"], L("Blood Elemental · Set 2", "Blood Elemental · Set 2"), L("Hulking Minions: mais vida = nuvem mais forte (mais Spirit).", "Hulking Minions: more life = stronger cloud (more Spirit)."), "core", 2, L("Blood Elemental ≈ 67 Spirit + Hulking", "Blood Elemental ≈ 67 Spirit + Hulking")),
   G("Sacrifice", ["Minion Mastery"], L("Minions viram corpos", "Minions become corpses"), L("60 Spirit.", "60 Spirit."), "core", 3, L("60 Spirit", "60 Spirit")),
   G("Despair", ["Heightened Curse", "Focused Curse", "Prolonged Duration II"], L("Curse · Set 1", "Curse · Set 1"), L("No nível máximo possível.", "At the highest level possible."), "free"),
   G("Blasphemy", ["Temporal Chains", "Magnified Area II", "Ritualistic Curse"], L("Aura de curse · Set 1", "Curse aura · Set 1"), L("Temporal Chains vira aura: inimigos lentos e efeitos neles duram mais.", "Temporal Chains becomes an aura: slow enemies and longer effects on them."), "core", 4, L("Reserva conforme a curse", "Reserves based on the curse")),
   G("Wind Dancer", ["Blind II"], L("Defesa · Set 1", "Defence · Set 1"), L("Stages de Evasion; ao ser atingido, empurra os inimigos.", "Evasion stages; when hit, knocks enemies back."), "core", 5, SP30),
   G("Contagion", ["Expand", "Rapid Casting I"], L("Espalha · Set 1", "Spreads · Set 1"), L("Nível baixo para economizar mana.", "Low level to save mana."), "free"),
   G("Withering Presence", ["Prolonged Duration II", "Herbalism II"], L("Wither · Set 1", "Wither · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 6, SP30),
   G("Ghost Dance", ["Cooldown Recovery II"], L("Defesa · Set 1", "Defence · Set 1"), L("Ghost Shrouds recuperam ES baseado na Evasion.", "Ghost Shrouds recover ES based on Evasion."), "core", 7, SP30),
   G("Herald of Plague", [], L("Clear em cadeia · Set 1 (opcional)", "Chain clear · Set 1 (optional)"), L("30 Spirit. Não é obrigatório para o clear (testado pelo Skadoosh) — dá para trocar por defesa (ex.: Desert Buckler).", "30 Spirit. Not required for clear (tested by Skadoosh) — can be swapped for defence (e.g. Desert Buckler)."), "opt", 1, SP30),
   G("Grim Feast", ["Harmonic Remnants II", "Remnant Potency I", "Rapid Casting I"], L("Reviver minions · Set 2", "Revive minions · Set 2"), L("Revive os Blood Elementals em combate.", "Revives Blood Elementals in combat."), "core", 9, SP30),
  ],
  cheap=[L("Shavronne's Satchel (cinto)", "Shavronne's Satchel (belt)"), "Astramentis", L("Rambler Jacket / Sorcerous Tiara", "Rambler Jacket / Sorcerous Tiara")],
  full=[L("Stoic Sceptres com Spirit alto e + minions", "Stoic Sceptres with high Spirit and + minions"), L("Timeless jewel para o Traveller's Wisdom", "Timeless jewel for Traveller's Wisdom")],
  stats=[L("Spirit (os dois sets)", "Spirit (both sets)"), L("Resistências elementais", "Elemental resistances"), L("ES/Evasion", "ES/Evasion"), L("+ nível de minions", "+ minion levels")],
  tree=L("Traveller's Wisdom: troque nós de atributo por 5% de defesa até o jewel socket, o resto por 5% de dano.", "Traveller's Wisdom: swap attribute nodes for 5% defence up to the jewel socket, the rest for 5% damage."),
  avoid=[L("Overwhelming Toxicity sem sustentar o máximo de venenos", "Overwhelming Toxicity without sustaining max poisons"), L("Mapas com less Recovery (Decompose em você mesmo)", "Maps with less Recovery (Decompose on yourself)")],
  exit=[L("4ª ascendência: Overwhelming Toxicity + Traveller's Wisdom", "4th ascendancy: Overwhelming Toxicity + Traveller's Wisdom"), L("10 venenos sustentados no boss", "10 poisons sustained on bosses")]),

 dict(id="max", name=L("Uber (80+)", "Uber (80+)"), lv=[80, 100], tag=L("Cast on Minion Death + Lineage", "Cast on Minion Death + Lineage"),
  carry=L("Corpsewade: Decompose · Cast on Minion Death", "Corpsewade: Decompose · Cast on Minion Death"), dmgSplit=[35, 65],
  goal=L("Setup do Skadoosh que fez mapas T16 de 11 mods com Aldur's 6 runas: Cast on Minion Death dispara Contagion e Entangle quando os Blood Elementals morrem no Decompose; Arakaali's Lust e Uul-Netol's Embrace nos supports; Sustainable Practices (50% da Evasion vira redução de dano elemental). Precisa de nível 80+ e bastante currency — nada disso é necessário para começar a variante.",
         "Skadoosh's setup that ran 11-mod T16 maps with Aldur's 6 runes: Cast on Minion Death triggers Contagion and Entangle when Blood Elementals die to Decompose; Arakaali's Lust and Uul-Netol's Embrace on supports; Sustainable Practices (50% of Evasion becomes elemental damage reduction). Needs level 80+ and a good amount of currency — none of it is required to start the variant."),
  rotation=[L("Igual ao endgame; Cast on Minion Death faz o resto", "Same as endgame; Cast on Minion Death does the rest")],
  gems=[
   G("Decompose", ["Persistent Ground III", "Deadly Poison II", "Encroaching Ground", "Arakaali's Lust", "Exploit Weakness"], L("Dano principal", "Main damage"), L("Arakaali's Lust: mais dano com mais venenos.", "Arakaali's Lust: more damage with more poisons."), "free"),
   G("Plague Bearer", ["Bursting Plague", "Poison III", "Deadly Poison II", "Vorana's Siege", "Uul-Netol's Embrace"], L("Clear · Set 1", "Clear · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Bind Spectre", ["Minion Mastery", "Dialla's Desire", "Uhtred's Augury"], L("Blood Elemental · Set 2", "Blood Elemental · Set 2"), L("Dialla's Desire: mais nível e menos reserva.", "Dialla's Desire: more level and less reservation."), "core", 2, L("Blood Elemental (Dialla reduz)", "Blood Elemental (Dialla reduces it)")),
   G("Sacrifice", ["Minion Mastery"], L("Minions viram corpos", "Minions become corpses"), L("60 Spirit.", "60 Spirit."), "core", 3, L("60 Spirit", "60 Spirit")),
   G("Cast on Minion Death", ["Contagion", "Acrimony", "Entangle", "Bleed III", "Blind II"], L("Gatilho · Set 2", "Trigger · Set 2"), L("Minion morreu = Contagion + Entangle automáticos.", "Minion died = automatic Contagion + Entangle."), "core", 4, SP30),
   G("Skeletal Sniper", ["Kurgal's Leash", "Brutus' Brain", "Mobility", "Efficiency II", "Minion Mastery"], L("Unholy Might", "Unholy Might"), L("Brutus' Brain (não morre) + Kurgal's Leash: comande para ganhar Unholy Might. Exclua do alvo do Decompose (opção de controle).", "Brutus' Brain (can't die) + Kurgal's Leash: command it to gain Unholy Might. Exclude it from Decompose targeting (controller option)."), "core", 5, SP30),
   G("Blasphemy", ["Temporal Chains", "Enfeeble", "Magnified Area II", "Ritualistic Curse", "Heightened Curse"], L("Auras de curse · Set 1", "Curse auras · Set 1"), L("Temporal Chains + Enfeeble.", "Temporal Chains + Enfeeble."), "core", 6, L("Reserva conforme as curses", "Reserves based on the curses")),
   G("Despair", ["Atziri's Allure", "Heightened Curse", "Focused Curse", "Prolonged Duration II", "Cursed Ground"], L("Curse · Set 1", "Curse · Set 1"), L("Atziri's Allure passa do limite de curses.", "Atziri's Allure goes past the curse limit."), "free"),
   G("Withering Presence", ["Prolonged Duration II", "Chaos Mastery", "Her Declaration"], L("Wither · Set 1", "Wither · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 7, SP30),
   G("Ghost Dance", ["Cooldown Recovery II", "Uhtred's Omen"], L("Defesa · Set 1", "Defence · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 8, SP30),
   G("Wind Dancer", ["Blind II", "Magnified Area II", "Maim", "Bleed III"], L("Defesa · Set 1", "Defence · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 9, SP30),
   G("Herald of Plague", ["Chaos Mastery"], L("Clear em cadeia · Set 1 (opcional)", "Chain clear · Set 1 (optional)"), L("30 Spirit. Não é obrigatório para o clear (testado pelo Skadoosh) — dá para trocar por defesa (ex.: Desert Buckler).", "30 Spirit. Not required for clear (tested by Skadoosh) — can be swapped for defence (e.g. Desert Buckler)."), "opt", 1, SP30),
  ],
  cheap=[L("Setup do endgame + Cast on Minion Death", "Endgame setup + Cast on Minion Death")],
  full=["Mageblood · For Utopia · Lavianga's Spirits", L("Unset Rings com runas · Sacrificial Regalia", "Unset Rings with runes · Sacrificial Regalia")],
  stats=[L("Spirit: 413 no Set 1 e 444 no Set 2 (5 Blood Elementals)", "Spirit: 413 on Set 1 and 444 on Set 2 (5 Blood Elementals)"), L("Resistências", "Resistances"), L("ES/Evasion", "ES/Evasion")],
  tree=L("Mesma do endgame com Sustainable Practices no lugar do Enduring Elixirs.", "Same as endgame with Sustainable Practices replacing Enduring Elixirs."),
  avoid=[L("Deixar o Skeletal Sniper ser consumido pelo Decompose", "Letting Decompose consume the Skeletal Sniper")],
  exit=[L("Pinnacle e mapas juiced", "Pinnacles and juiced maps")]),
]
PH = {p["id"]: p for p in PHASES}

BOX = {
 "a3": ("2+", [L("nuvens de Gas Arrow", "Gas Arrow clouds")], L("Duas ou mais nuvens por baixo do Toxic Growth: mais venenos nas pústulas = mais dano e detonação mais rápida.", "Two or more clouds under Toxic Growth: more poisons on the pustules = more damage and faster detonation.")),
 "start": ("2–3", [L("Blood Elementals", "Blood Elementals")], L("Cada Blood Elemental consumido vira uma nuvem. Com pouco Spirit, tire supports do Bind Spectre até caberem 3.", "Each consumed Blood Elemental becomes a cloud. With little Spirit, remove Bind Spectre supports until 3 fit.")),
 "end": ("10", [L("venenos máximos", "max poisons")], L("Snakebite, Overwhelming Toxicity e o resto chegam a 10 venenos por alvo. Mais nuvens = chega no máximo mais rápido.", "Snakebite, Overwhelming Toxicity and the rest reach 10 poisons per target. More clouds = reach the cap faster.")),
 "max": ("5", [L("Blood Elementals", "Blood Elementals")], L("444 de Spirit no Set 2 para 5 Blood Elementals.", "444 Spirit on Set 2 for 5 Blood Elementals.")),
}
SPIRIT_NOTE = {
 "a2": L("Plague Bearer reserva 30 Spirit (King in the Mists).", "Plague Bearer reserves 30 Spirit (King in the Mists)."),
 "a4": L("Plague Bearer (30) + Herald of Plague (30).", "Plague Bearer (30) + Herald of Plague (30)."),
 "start": L("O Spirit é por weapon set: Set 1 paga auras e debuffs; Set 2 paga Bind Spectre + Sacrifice. Os sceptres dos dois sets dão o Spirit.", "Spirit is per weapon set: Set 1 pays for auras and debuffs; Set 2 pays for Bind Spectre + Sacrifice. The sceptres on both sets provide the Spirit."),
 "end": L("Set 1: Plague Bearer, Blasphemy, Wind Dancer, Withering Presence, Ghost Dance, Herald of Plague. Set 2: Bind Spectre, Sacrifice, Grim Feast.", "Set 1: Plague Bearer, Blasphemy, Wind Dancer, Withering Presence, Ghost Dance, Herald of Plague. Set 2: Bind Spectre, Sacrifice, Grim Feast."),
 "max": L("Skadoosh: 413 Spirit no Set 1 e 444 no Set 2.", "Skadoosh: 413 Spirit on Set 1 and 444 on Set 2."),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in SPIRIT_NOTE.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Poisonburst Arrow + Contagion. Vine Arrow nível 1.", "Poisonburst Arrow + Contagion. Vine Arrow level 1."),
 8: L("Surefooted Sigil: vida e mobilidade baratas.", "Surefooted Sigil: cheap life and mobility."),
 10: L("Goldrim: resistências resolvidas até o meio da campanha.", "Goldrim: resistances solved until mid-campaign."),
 3: L("Stormcaller Arrow para o boss.", "Stormcaller Arrow for bosses."),
 10: L("King in the Mists (+30 Spirit) → Plague Bearer.", "King in the Mists (+30 Spirit) → Plague Bearer."),
 11: L("Wanderlust: 20% de Movement Speed.", "Wanderlust: 20% Movement Speed."),
 12: L("Weapon sets: arco e aljava nos dois.", "Weapon sets: bow and quiver on both."),
 16: L("Splinterheart (arco) + Ghostmarch (botas) + The Lethal Draw (aljava): o trio mais barato da campanha.", "Splinterheart (bow) + Ghostmarch (boots) + The Lethal Draw (quiver): the campaign's cheapest trio."),
 22: L("Toxic Growth + Gas Arrow.", "Toxic Growth + Gas Arrow."),
 28: L("Death's Harp: flecha adicional garantida.", "Death's Harp: a guaranteed extra arrow."),
 26: L("1ª ascendência: Relentless Pursuit.", "1st ascendancy: Relentless Pursuit."),
 32: L("Sandswept Marsh: Lesser Jeweller's Orb garantido → Toxic Growth.", "Sandswept Marsh: guaranteed Lesser Jeweller's Orb → Toxic Growth."),
 33: L("Snakebite: +1 veneno por alvo (dropa por volta daqui, bem antes do Decompose).", "Snakebite: +1 poison per target (drops around here, well before Decompose)."),
 36: L("Venom Draught: Stun Threshold.", "Venom Draught: Stun Threshold."),
 39: L("Slivertongue: o último arco antes da troca — Fork de graça.", "Slivertongue: the last bow before the swap — free Fork."),
 38: L("Azak Bog (+30 Spirit) → Herald of Plague. 2ª ascendência: Path Seeker (área da Witch/Sorceress).", "Azak Bog (+30 Spirit) → Herald of Plague. 2nd ascendancy: Path Seeker (Witch/Sorceress area)."),
 45: L("Compre Corpsewade (já pode equipar — funciona desde o 11), Snakebite e Trenchtimbre. Guarde gold.", "Buy Corpsewade (already equippable — it works from 11), Snakebite and Trenchtimbre. Save gold."),
 50: L("Capture um Blood Elemental (a partir do Aggorat).", "Capture a Blood Elemental (from Aggorat onwards)."),
 58: L("A VIRADA DE VERDADE: Sacrifice libera (não a Corpsewade, que já podia estar equipada) — Bind Spectre + Sacrifice no Set 2, respec da árvore.", "THE REAL PIVOT: Sacrifice unlocks (not Corpsewade, which could already be equipped) — Bind Spectre + Sacrifice on Set 2, tree respec."),
 62: L("Lythara (+40 Spirit). 3ª ascendência: Enduring Elixirs.", "Lythara (+40 Spirit). 3rd ascendancy: Enduring Elixirs."),
 66: L("Blasphemy (Temporal Chains), Ghost Dance, Wind Dancer.", "Blasphemy (Temporal Chains), Ghost Dance, Wind Dancer."),
 72: L("4ª ascendência: Overwhelming Toxicity + Traveller's Wisdom.", "4th ascendancy: Overwhelming Toxicity + Traveller's Wisdom."),
 80: L("Uber: Cast on Minion Death, Sustainable Practices, supports de Lineage.", "Uber: Cast on Minion Death, Sustainable Practices, Lineage supports."),
}

ASCENDANCY = [
 dict(order=1, key="relentless", node="Relentless Pursuit", when=L("1º Trial (~nível 26) — SÓ NO LEVELING", "1st Trial (~level 26) — LEVELING ONLY"), text=L("Sua velocidade não é afetada por Slows.", "Your speed is unaffected by Slows."), why=L("Pick de leveling: ajuda a andar sem ser atrasado até o 58. Conferido ao vivo nas 3 variantes do build atual (Starter, Endgame e Uber): NENHUMA usa Relentless Pursuit — no respec do 58 esse mesmo ponto do 1º Trial vira Enduring Elixirs (não é uma ascendência a mais, é uma realocação).", "A leveling pick: helps you keep moving without being slowed until 58. Checked live against the 3 current variants (Starter, Endgame and Uber): NONE of them use Relentless Pursuit — at the level 58 respec that same 1st Trial point becomes Enduring Elixirs (not an extra ascendancy, a reallocation).")),
 dict(order=2, key="seeker", node="Path Seeker", when=L("2º Trial (~nível 38)", "2nd Trial (~level 38)"), text=L("Escolha um caminho de outra classe — o Skadoosh pega Path of the Sorceress (área inicial da Witch/Sorceress).", "Choose another class's path — Skadoosh takes Path of the Sorceress (Witch/Sorceress starting area)."), why=L("Nós de Chaos, minion e Energy Shield perto de você. É a ÚNICA ascendência que se mantém igual do leveling até o Uber — nunca é respecada.", "Chaos, minion and Energy Shield nodes close to you. It's the ONLY ascendancy that stays the same from leveling to Uber — never respecced.")),
 dict(order=3, key="elixirs", node="Enduring Elixirs", when=L("Respec do nível 58 (usa o ponto do 1º Trial)", "Level 58 respec (reuses the 1st Trial's point)"), text=L("Efeitos de flask de vida não saem quando a vida enche e não entram em fila.", "Life Flask effects are not removed when unreserved life is filled and don't queue."), why=L("Substitui Relentless Pursuit no respec do 58: regen constante enquanto o Decompose te dá dano. Continua até o Uber, quando é substituída por Sustainable Practices ao conseguir Mageblood.", "Replaces Relentless Pursuit at the 58 respec: constant regen while Decompose deals damage to you. Stays until Uber, where it's replaced by Sustainable Practices once you get Mageblood.")),
 dict(order=4, key="toxicity", node="Overwhelming Toxicity", when=L("3º/4º Trial, entre o 58 e o 79 (verifique no jogo qual Trial libera primeiro)", "3rd/4th Trial, between 58 and 79 (check in-game which Trial unlocks first)"), text=L("Dobra o número de venenos que o alvo pode ter; 50% less duração de veneno (0.5 patch: era 35% less).", "Double the number of your Poisons that targets can be affected by; 50% less Poison Duration (0.5 patch: was 35% less)."), why=L("Dano de boss: só pegue quando sustentar o máximo de venenos. Agora custa só 2 pontos de ascendência no total (patch 0.4), mais barata do que era.", "Boss damage: only take it once you sustain max poisons. Now only costs 2 ascendancy points total (patch 0.4), cheaper than before.")),
 dict(order=5, key="wisdom", node="Traveller's Wisdom", when=L("3º/4º Trial, entre o 58 e o 79", "3rd/4th Trial, between 58 and 79"), text=L("Nós de atributo podem dar 5% dano, 5% defesas ou 5% eficiência de custo.", "Attribute passives can instead grant 5% damage, 5% Armour/Evasion/ES or 5% cost efficiency."), why=L("Dezenas de nós de viagem viram dano/defesa. O guia recomenda conseguir a runa de capacete Legacy of Greymake primeiro — fica melhor com ela.", "Dozens of travel nodes become damage/defence. The guide recommends getting the Legacy of Greymake helmet rune first — it's better with it.")),
 dict(order=6, key="sustainable", node="Sustainable Practices", when=L("Uber (80+, depois de conseguir Mageblood)", "Uber (80+, after getting Mageblood)"), text=L("50% da Evasion também dá redução de dano elemental.", "50% of Evasion Rating also grants Elemental Damage reduction."), why=L("Substitui o Enduring Elixirs quando o Mageblood já mantém os flasks ativos sozinho (Enduring Elixirs vira redundante). Alternativa citada pela fonte para esse mesmo slot: Running Assault (menos penalidade de sprint) — o Sustainable Practices é o que aparece de fato na árvore/equipamento do Uber.", "Replaces Enduring Elixirs once Mageblood already keeps flasks active on its own (Enduring Elixirs becomes redundant). An alternative the source mentions for this same slot: Running Assault (less sprint penalty) — Sustainable Practices is what's actually in the live Uber tree/gear.")),
]
ASC_UNLOCK = [26, 38, 58, 72, 72, 80]
ASC_PHASE = {"a4": ["Relentless Pursuit", "Path Seeker"], "a5": ["Relentless Pursuit", "Path Seeker"]}

KEY_PASSIVES = [
 dict(node="Overwhelming Toxicity", type=L("Ascendência", "Ascendancy"), text=L("Dobra o limite de venenos; 50% less duração.", "Doubles the poison cap; 50% less duration."), when="72+", why=L("Não pegue antes de sustentar o máximo de venenos.", "Don't take it before sustaining max poisons.")),
 dict(node="Traveller's Wisdom", type=L("Ascendência", "Ascendancy"), text=L("Atributos viram 5% dano/defesa.", "Attributes become 5% damage/defence."), when="72+", why=L("Um timeless jewel ajuda a aproveitar.", "A timeless jewel helps make the most of it.")),
 dict(node="Corpsewade", type=L("Unique (botas)", "Unique (boots)"), text=L("Trigger Decompose every 1.2 metres travelled.", "Trigger Decompose every 1.2 metres travelled."), when=L("Equipa no 11 · dano principal no 58 (Sacrifice)", "Equips at 11 · main damage at 58 (Sacrifice)"), why=L("A build inteira depende dela, mas só a partir do 58 (com Sacrifice) ela vira dano principal em vez de bônus passivo.", "The whole build depends on it, but only from 58 (with Sacrifice) does it become main damage instead of a passive bonus.")),
]
TREE_STAGES = [
 dict(lv="1–30", focus=L("Projétil e veneno", "Projectile and poison"), dmg="Poisonburst Arrow / Toxic Growth", **{"def": L("Evasion + vida", "Evasion + life")}, spirit="Plague Bearer", dont=L("Dano elemental no arco", "Elemental damage on the bow")),
 dict(lv="31–57", focus=L("Veneno + Path Seeker", "Poison + Path Seeker"), dmg="Toxic Growth + Plague Bearer", **{"def": L("Resistências", "Resistances")}, spirit="Herald of Plague", dont=L("Gastar o gold do respec", "Spending the respec gold")),
 dict(lv="58–79", focus=L("Minions, curses, Chaos", "Minions, curses, Chaos"), dmg="Decompose (Corpsewade)", **{"def": L("ES/Evasion, Ghost Dance", "ES/Evasion, Ghost Dance")}, spirit=L("Dois sets separados", "Two separate sets"), dont="Overwhelming Toxicity cedo"),
 dict(lv="80–100", focus=L("Lineage e Cast on Minion Death", "Lineage and Cast on Minion Death"), dmg="Decompose + Contagion/Entangle", **{"def": "Sustainable Practices"}, spirit="413 / 444", dont=L("Deixar o Sniper ser consumido", "Letting the Sniper get consumed")),
]

UNIQUES = [
 U("Surefooted Sigil", L("Amuleto", "Amulet"), L("Acessório", "Accessory"), "a1", L("+40–60 de vida, +5–15 de Destreza, +1 m de Dodge Roll e 50% de Evasão a mais depois de rolar.", "+40–60 life, +5–15 Dexterity, +1 m Dodge Roll distance and 50% more Evasion after dodge rolling."), L("Vida e mobilidade baratas desde o começo.", "Cheap early life and mobility."), L("Amuleto rare com vida.", "Rare amulet with life."), lvl=8),
 U("Goldrim", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a1", L("+30–50 de Evasão, 10% de raridade e +25–33% em TODAS as resistências elementais.", "+30–50 Evasion, 10% rarity and +25–33% to ALL elemental resistances."), L("Resolve resistência sozinho até o meio da campanha.", "Solves resistances by itself until mid-campaign."), L("Capacete rare com vida/Evasão.", "Rare Evasion/life helmet."), lvl=10),
 U("Wanderlust", L("Botas", "Boots"), L("Armadura", "Armour"), "a2", L("20% de Movement Speed, ES e imunidade a Slow.", "20% Movement Speed, ES and slow immunity."), L("Velocidade de campanha barata; ande mais rápido do que qualquer bota rare desse nível.", "Cheap campaign speed; faster than any rare boot at this level."), L("Botas com Movement Speed.", "Boots with Movement Speed."), lvl=11),
 U("Splinterheart", L("Arco", "Bow"), L("Arma", "Weapon"), "a2", L("120–158% de dano físico, precisão, velocidade de projétil e os projéteis se dividem para +2 alvos.", "120–158% physical damage, accuracy, projectile speed and projectiles split towards +2 targets."), L("O melhor arco do leveling: o split cobre pack sozinho, e o físico alto é dano puro de veneno.", "The best leveling bow: the split covers packs by itself, and the high physical is pure poison damage."), L("Arco rare com dano físico.", "Rare physical bow."), lvl=16),
 U("The Lethal Draw", L("Aljava", "Quiver"), L("Acessório", "Accessory"), "a2", L("5–10% de attack speed, vida por acerto, 15–25% de chance de Pierce e físico extra consumindo carga do flask de vida.", "5–10% attack speed, life per hit, 15–25% Pierce chance and extra physical by consuming Life Flask charges."), L("Pierce ajuda o Poisonburst Arrow a acertar mais de um alvo em fila; monitore as cargas do flask em boss longo.", "Pierce helps Poisonburst Arrow hit more than one target in a line; watch flask charges on long bosses."), L("Aljava rare com físico.", "Rare physical quiver."), lvl=16),
 U("Ghostmarch", L("Botas", "Boots"), L("Armadura", "Armour"), "a2", L("15% de Movement Speed, 100–148% de Evasão/ES, +30–50 de mana, +17–23% de Chaos Resistance e o dodge roll atravessa inimigos.", "15% Movement Speed, 100–148% Evasion/ES, +30–50 mana, +17–23% Chaos Resistance and dodge roll passes through enemies."), L("Atravessar inimigos ao rolar é a segurança mais barata da campanha; troque depois por bota rare de 25–30% MS.", "Passing through enemies on dodge roll is the cheapest safety net in the campaign; swap later for a 25–30% MS rare boot."), "Wanderlust", lvl=16),
 U("Death's Harp", L("Arco", "Bow"), L("Arma", "Weapon"), "a3", L("+20–25% de dano crítico, vida e mana por inimigo morto e +250–325% de Surpassing chance de disparar uma flecha adicional.", "+20–25% crit damage, life and mana per enemy killed and +250–325% Surpassing chance to fire an additional arrow."), L("O total de 250%+ garante duas flechas extras e chance para a terceira: mais alvos por disparo do Poisonburst.", "The 250%+ total guarantees two extra arrows and a chance at a third: more targets per Poisonburst shot."), "Splinterheart", lvl=28),
 U("Corpsewade", L("Botas", "Boots"), L("Armadura", "Armour"), "start", L("10% Movement Speed, Armour, +5–10 de Força e concede a skill Decompose (nível 4 na base; sobe com o item level da bota), disparando-a a cada 1,2 m andados.", "10% Movement Speed, Armour, +5–10 Strength and grants the Decompose skill (level 4 on the base roll; scales with the boots' item level), triggering it every 1.2 m travelled."),
   L("PODE EQUIPAR: nível 11 (PoE2DB) — funciona desde já como bônus passivo, consumindo corpos normais que você mata. TRANSIÇÃO COMPLETA para a build Decompose: nível 58, porque é aí que Sacrifice libera (deixa seus próprios minions servirem de corpo, o que transforma o Decompose de 'bônus' em dano principal). Sem Sacrifice, ela ainda funciona, só não vira o carro-chefe. Perfect Jeweller's Orb para 5 sockets; Runeforged dá +5% de movimento; buscar item level alto para o Decompose nascer em nível mais alto.",
     "CAN EQUIP: level 11 (PoE2DB) — it already works as a passive bonus from level 11, consuming normal corpses you kill. FULL TRANSITION to the Decompose build: level 58, because that's when Sacrifice unlocks (letting your own minions count as corpses, which turns Decompose from 'bonus' into main damage). Without Sacrifice it still works, it just isn't your main damage yet. Perfect Jeweller's Orb for 5 sockets; Runeforged gives +5% movement; look for a high item level so Decompose rolls at a higher skill level."),
   L("Não há substituto para o Decompose em si; até equipar, qualquer bota de Movement Speed serve.", "There's no substitute for Decompose itself; until you equip it, any Movement Speed boot works."), lvl=11),
 U("Snakebite", L("Luvas", "Gloves"), L("Armadura", "Armour"), "a4", L("40–60% Evasão, +7–17% Chaos Resistance, 6–10 de regeneração de vida por segundo, 20–30% de chance de veneno e +1 veneno simultâneo por alvo.", "40–60% Evasion, +7–17% Chaos Resistance, 6–10 life regen per second, 20–30% chance to Poison and +1 simultaneous poison per target."), L("Dropa/compra no nível 33 (PoE2DB) — bem antes do Decompose (58); use no arco também, o +1 veneno já ajuda o Poisonburst. QUANDO NÃO VALE: se a resistência elemental ainda não estiver em 75%, uma luva rare com resist/vida normalmente resolve mais problema do que os 40-60% de Evasão da Snakebite — ela não dá resistência elemental nenhuma. Ela também disputa o slot de luvas com a Plaguefinger (veja Power/Twink): dê preferência à Snakebite se você já tem +1 veneno suficiente e quer regen/Chaos Resistance; prefira a Plaguefinger se ainda faltam anos de dano elemental sobrando no resto do equipamento.", "Drops/buys at level 33 (PoE2DB) — well before Decompose (58); use it on the bow too, the +1 poison already helps Poisonburst. WHEN IT'S NOT WORTH IT: if your elemental resistance isn't at 75% yet, a rare glove with resist/life usually solves more of a problem than Snakebite's 40-60% Evasion — it gives zero elemental resistance. It also competes for the glove slot with Plaguefinger (see Power/Twink): prefer Snakebite once you already have enough poison stacking and want regen/Chaos Resistance; prefer Plaguefinger if you still have spare elemental damage sitting unused elsewhere on your gear."), L("Luvas de ES/Evasion com resistências.", "ES/Evasion gloves with resistances."), lvl=33),
 U("Slivertongue", L("Arco", "Bow"), L("Arma", "Weapon"), "a4", L("Físico alto, +4–6% de crítico, leech de vida e mana e as flechas fazem Fork e perfuram tudo depois de dividir.", "High physical, +4–6% crit, life and mana leech, and arrows Fork and pierce everything after forking."), L("[Alternativa / opção de leveling Power — não vem do guia do Skadoosh] O último arco antes do 58: Fork de graça cobre corredores inteiros com veneno. Vale a pena porque o físico alto e o Fork gratuito escalam com o próprio dano do arco (o que o veneno usa), diferente de itens que só amplificam a aljava.", "[Alternative / Power leveling option — not from Skadoosh's guide] The last bow before 58: free Fork covers whole corridors with poison. It's worth it because the high physical and free Fork scale off the bow's own damage (what poison uses), unlike items that only amplify the quiver."), "Death's Harp", lvl=39),
 U("Plaguefinger", L("Luvas", "Gloves"), L("Armadura", "Armour"), "a1", L("30–50% Evasão/ES, 4–6% de attack speed, 20–30% de chance de veneno e a linha que muda a regra do jogo: 'All Damage from Hits Contributes to Poison Magnitude' (todo dano de hit conta para o veneno, elemental incluso) — em troca de não poder aplicar Shock/Freeze/Ignite.", "30–50% Evasion/ES, 4–6% attack speed, 20–30% chance to Poison and the game-changing line: 'All Damage from Hits Contributes to Poison Magnitude' (all hit damage counts toward poison, elemental included) — in exchange for being unable to inflict Shock/Freeze/Ignite."),
   L("[Alternativa / opção de leveling Power — não vem do guia do Skadoosh; validada aqui via PoE2DB] Nível 4 para equipar: dá para usar praticamente desde o início. Como esta build não depende de ailments elementais (Shock/Freeze/Ignite) em nenhuma fase, a troca é quase de graça — e ela libera qualquer dano elemental de anéis, amuleto e luvas para também alimentar o veneno. DISPUTA O MESMO SLOT que a Snakebite (luvas): marque a caixinha 'Plaguefinger equipada' em Meu personagem para a página trocar a prioridade de afixos (elemental passa a valer) — sem marcar, a página continua recomendando só físico/Chaos.", "[Alternative / Power leveling option — not from Skadoosh's guide; validated here via PoE2DB] Level 4 to equip: usable from almost the very start. Since this build never relies on elemental ailments (Shock/Freeze/Ignite) in any phase, the trade-off is nearly free — and it frees up any elemental damage on rings, amulet and gloves to also feed poison. COMPETES FOR THE SAME SLOT as Snakebite (gloves): tick the 'Plaguefinger equipped' checkbox in My character to make the page flip its affix priority (elemental starts to count) — without it, the page keeps recommending physical/Chaos only."),
   L("Snakebite (poison count + regen) ou luvas rare com resist.", "Snakebite (poison count + regen) or rare resist gloves.")),
 U("Trenchtimbre", L("Maça (Set 2)", "Mace (Set 2)"), L("Arma", "Weapon"), "start", L("Rola +1 A +2 nível de todas as skills de minion (a attack speed dos minions também afeta você).", "Rolls +1 TO +2 to Level of all Minion Skills (minion attack speed also affects you)."), L("Nível 16 para equipar (PoE2DB) — muito antes do Decompose. Weapon Set 2 (invocação). Compre a versão +1 assim que puder (é barata, serve para toda a transição do 58); guarde currency para a +2 (a que o guia atual recomenda para o endgame — confira essa linha antes de comprar, a +1 é só uma opção temporária).", "Level 16 to equip (PoE2DB) — well before Decompose. Weapon Set 2 (summoning). Buy the +1 version as soon as you can (it's cheap and works through the whole 58 transition); save currency for the +2 roll (what the current guide recommends for endgame — check that line before buying, +1 is only a temporary option)."), L("Maça com + nível de minions.", "Mace with + minion levels."), lvl=16),
 U("Shavronne's Satchel", L("Cinto", "Belt"), L("Acessório", "Accessory"), "start", L("1–3 Charm Slots, +20–30 de Inteligência, mais cargas de flask e recuperação de vida dos flasks também virando Energy Shield.", "1–3 Charm Slots, +20–30 Intelligence, more flask charges and Life Recovery from Flasks also applying to Energy Shield."), L("Nível 62 para equipar (PoE2DB), não '65+' genérico — ela entra assim que Enduring Elixirs estiver ativa (o efeito de flask permanente perde metade da graça sem a ascendência), o que costuma acontecer ainda dentro da fase 'Decompose: início (58–64)'.", "Level 62 to equip (PoE2DB), not a generic '65+' — it comes online once Enduring Elixirs is active (the permanent flask effect loses half its point without the ascendancy), which usually happens still inside the 'Decompose: start (58–64)' phase."), L("Cinto rare de vida/resists.", "Rare life/resists belt."), lvl=62),
 U("Astramentis", L("Amuleto", "Amulet"), L("Acessório", "Accessory"), "end", L("+50–100 em todos os atributos e −4 de dano físico recebido de ataques.", "+50–100 to all attributes and −4 physical damage taken from attack hits."), L("Nível 24 para equipar (PoE2DB) — NÃO é só item de endgame: se você tem a currency (custa poucos centavos de divine), ela já resolve Destreza, Inteligência e Força para gems e sceptres desde a campanha. Twink/Power: equipável muito antes do Decompose. Deixa de ser 'a melhor opção' só quando você troca por um amuleto de Spirit fraturado (+3 minions ou 45+ Spirit) no Endgame — ela resolve atributos, não é automaticamente mais dano.", "Level 24 to equip (PoE2DB) — NOT just an endgame item: if you have the currency (it costs a few cents of a divine), it already solves Dexterity, Intelligence and Strength for gems and sceptres from the campaign onward. Twink/Power: equippable well before Decompose. It stops being 'the best pick' only once you swap to a fractured Spirit amulet (+3 minions or 45+ Spirit) in Endgame — it fixes attributes, it isn't automatically more damage."), L("Solar Amulet com Spirit.", "Solar Amulet with Spirit."), lvl=24),
 U("Mageblood", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Legados de flask permanentes.", "Permanent flask legacies."), L("Uber.", "Uber."), "Shavronne's Satchel"),
 U("For Utopia", "Charm", "Charm", "max", L("Defende com 200% da Armour durante o efeito.", "Defend with 200% of Armour during its effect."), L("Uber.", "Uber."), L("Stone Charm.", "Stone Charm.")),
 U("Lavianga's Spirits", "Flask", "Flask", "max", L("Flask de mana com efeito constante.", "Mana flask with a constant effect."), L("Uber.", "Uber."), L("Flask de mana normal.", "Normal mana flask.")),
]

GEAR = [
 dict(slot=L("Arco (1–57)", "Bow (1–57)"), cheap=L("Arco Magic com físico (Transmutation/Augmentation)", "Magic bow with physical (Transmutation/Augmentation)"), value="Splinterheart (16) · Death's Harp (28)", full="Slivertongue (39)", affix=L("% físico; físico adicionado; + projéteis", "% physical; added physical; + projectiles"),
      lvls=[dict(lv=1, n=L("Arco Magic com físico", "Magic bow with physical")), dict(lv=16, n="Splinterheart"), dict(lv=28, n="Death's Harp"), dict(lv=39, n="Slivertongue")],
      note=L("Na configuração padrão, elemental no arco não aumenta o veneno — só físico e Chaos contam. Isso muda com a Plaguefinger (Power/Twink, nível 4), que faz todo dano de hit contar para o veneno.", "In the default setup, elemental on the bow doesn't raise poison — only physical and Chaos count. This changes with Plaguefinger (Power/Twink, level 4), which makes all hit damage count toward poison.")),
 dict(slot=L("Aljava", "Quiver"), cheap=L("Aljava rare com físico adicionado", "Rare quiver with added physical"), value="The Lethal Draw (16)", full=L("Toxic Quiver rare com físico e veneno", "Rare Toxic Quiver with physical and poison"),
      affix=L("Físico adicionado; % dano de veneno; resist", "Added physical; % poison damage; resist"),
      lvls=[dict(lv=1, n=L("Aljava rare com físico", "Rare quiver with physical")), dict(lv=16, n="The Lethal Draw"), dict(lv=40, n=L("Toxic Quiver rare", "Rare Toxic Quiver"))], note=""),
 dict(slot=L("Maça + Sceptre (58+)", "Mace + Sceptre (58+)"), cheap=L("Maça qualquer (Set 1) + Stoic Sceptre com Spirit nos dois sets", "Any mace (Set 1) + Spirit Stoic Sceptre on both sets"), value=L("Brigand Mace com Perfect Essence of Abrasion + mod de Fully Broken Armour", "Brigand Mace with Perfect Essence of Abrasion + Fully Broken Armour mod"), full=L("Trenchtimbre (Set 2) + sceptres de Spirit alto e Perfect Essence of Command", "Trenchtimbre (Set 2) + high-Spirit sceptres and Perfect Essence of Command"), affix=L("Spirit; + nível de minions; vida de minions", "Spirit; + minion levels; minion life"), note=L("Spirit é por set: Set 1 auras, Set 2 minions.", "Spirit is per set: Set 1 auras, Set 2 minions.")),
 dict(slot=L("Capacete", "Helmet"), cheap="Goldrim (10)", value="Sorcerous Tiara", full=L("Ancestral Tiara com + curses/minions", "Ancestral Tiara with + curses/minions"), affix=L("ES; resist", "ES; resist"),
      lvls=[dict(lv=10, n="Goldrim"), dict(lv=58, n=L("Rare ES/Evasion + resist", "Rare ES/Evasion + resist")), dict(lv=65, n="Sorcerous Tiara")], note=""),
 dict(slot="Body Armour", cheap=L("ES/Evasion + resists", "ES/Evasion + resists"), value="Rambler Jacket", full="Sacrificial Regalia", affix=L("ES; Evasion; resist", "ES; Evasion; resist"), note=""),
 dict(slot=L("Luvas", "Gloves"), cheap=L("Luvas rare com resist até o 33", "Rare resist gloves until 33"), value="Snakebite (33)", full=L("Luvas com mods de Transcendent Limbs (magnitude de ailment/curse)", "Gloves with Transcendent Limbs mods (ailment/curse magnitude)"), affix=L("Veneno; resist", "Poison; resist"),
      lvls=[dict(lv=1, n=L("Luvas rare com resist", "Rare resist gloves")), dict(lv=33, n="Snakebite")], note=""),
 dict(slot=L("Botas", "Boots"), cheap="Wanderlust (11) · Ghostmarch (16)", value=L("Corpsewade com 3+ sockets", "Corpsewade with 3+ sockets"), full=L("Corpsewade Runeforged + corrompida (5 sockets)", "Runeforged + corrupted Corpsewade (5 sockets)"), affix=L("Nível da bota = nível do Decompose (58+)", "Boots level = Decompose level (58+)"),
      lvls=[dict(lv=11, n="Wanderlust"), dict(lv=16, n="Ghostmarch"), dict(lv=58, n="Corpsewade")], note=L("Corpsewade JÁ PODE ser equipada no 11 (funciona como bônus passivo desde então) — mas só vale trocar as botas de Movement Speed por ela quando Sacrifice (58) transformar o Decompose em dano principal.", "Corpsewade CAN already be equipped at 11 (it works as a passive bonus from then on) — but it's only worth swapping your Movement Speed boots for it once Sacrifice (58) turns Decompose into main damage.")),
 dict(slot=L("Amuleto", "Amulet"), cheap="Surefooted Sigil (8) · Solar Amulet (58)", value="Astramentis", full=L("Fracturado com +3 minions ou 45+ Spirit", "Fractured with +3 minions or 45+ Spirit"), affix=L("Spirit; + minions", "Spirit; + minions"),
      lvls=[dict(lv=8, n="Surefooted Sigil"), dict(lv=24, n=L("Astramentis (Power/Twink, se tiver currency)", "Astramentis (Power/Twink, if you have the currency)")), dict(lv=58, n="Solar Amulet"), dict(lv=65, n=L("Astramentis (padrão do Endgame)", "Astramentis (Endgame default)"))], note=L("Astramentis resolve atributos, não dano — pode entrar cedo (24) OU ficar para o Endgame (65), depende só da sua currency.", "Astramentis fixes attributes, not damage — it can come in early (24) OR wait for Endgame (65), it's purely a currency call.")),
 dict(slot=L("Anéis", "Rings"), cheap=L("Resistências", "Resistances"), value="Prismatic Ring", full=L("Unset Rings com runas úteis", "Unset Rings with useful runes"), affix=L("Resist; veneno", "Resist; poison"), note=""),
 dict(slot=L("Cinto", "Belt"), cheap=L("Vida/resists", "Life/resists"), value="Shavronne's Satchel (62)", full="Mageblood", affix=L("Resist", "Resist"),
      lvls=[dict(lv=1, n=L("Cinto rare vida/resist", "Rare life/resist belt")), dict(lv=62, n="Shavronne's Satchel"), dict(lv=80, n="Mageblood")], note=""),
 dict(slot="Charms", cheap=L("Thawing + Stone + Dousing", "Thawing + Stone + Dousing"), value="For Utopia", full="For Utopia", affix=L("Freeze/Stun/Ignite", "Freeze/Stun/Ignite"), note=""),
]
BUY_ORDER = [
 dict(p=1, item=L("Arco com físico", "Physical bow"), phase="1–57", cost=L("Barato", "Cheap"), impact=L("Dano do leveling", "Leveling damage")),
 dict(p=2, item="Corpsewade", phase="58", cost=L("Barato", "Cheap"), impact=L("Liga a build", "Enables the build")),
 dict(p=3, item="Snakebite + Trenchtimbre", phase="58", cost=L("Barato", "Cheap"), impact=L("Veneno extra + minions", "Extra poison + minions")),
 dict(p=4, item=L("Stoic Sceptres com Spirit", "Stoic Sceptres with Spirit"), phase="58+", cost=L("Valor", "Value"), impact=L("Mais Blood Elementals e auras", "More Blood Elementals and auras")),
 dict(p=5, item="Shavronne's Satchel + Astramentis", phase="65+", cost=L("Barato", "Cheap"), impact=L("Defesa e atributos", "Defence and attributes")),
 dict(p=6, item=L("Lineage supports", "Lineage supports"), phase="80+", cost=L("Luxo", "Luxury"), impact=L("Teto de dano", "Damage ceiling")),
]

TRICKS = [
 {"cat": "Decompose", "lvl": L("Médio", "Medium"), "title": L("Mais vida no corpo = mais dano", "More corpse life = more damage"), "body": L("O Decompose causa dano baseado na vida do monstro que virou corpo. Monstros de mapa alto e Blood Elementals com mais vida (Minion Mastery, Hulking Minions, sceptres com vida de minion) = nuvens mais fortes.", "Decompose deals damage based on the life of the monster that became the corpse. High-map monsters and Blood Elementals with more life (Minion Mastery, Hulking Minions, sceptres with minion life) = stronger clouds.")},
 {"cat": "Decompose", "lvl": L("Médio", "Medium"), "title": L("Nuvens não somam dano", "Clouds don't stack damage"), "body": L("Cada nuvem aplica um veneno a cada 2 s até o limite. Mais nuvens = chega em 10 venenos mais rápido e fica lá mais tempo, não mais dano por veneno.", "Each cloud applies a poison every 2 s up to the cap. More clouds = reach 10 poisons faster and stay there longer, not more damage per poison.")},
 {"cat": "Decompose", "lvl": L("Fácil", "Easy"), "title": L("Swap para reviver", "Swap to revive"), "body": L("Fora de combate, trocar de weapon set invoca os minions na hora (pula o timer). Em combate, use Grim Feast. Pré-carregue nuvens antes do boss.", "Out of combat, swapping weapon sets summons minions instantly (skips the timer). In combat, use Grim Feast. Pre-load clouds before bosses.")},
 {"cat": "Decompose", "lvl": L("Fácil", "Easy"), "title": L("Weapon swap no mouse", "Weapon swap on the mouse"), "body": L("Você vai trocar de set o tempo todo: coloque a troca num botão do mouse (o Skadoosh usa o Mouse 5).", "You'll swap sets constantly: bind swap to a mouse button (Skadoosh uses Mouse 5).")},
 {"cat": "Minions", "lvl": L("Médio", "Medium"), "title": L("Timer de 'X minutos'", "'X minute' respawn timer"), "body": L("Acontece quando a quantidade de minions selecionada passa do Spirit. Aperte − até o + acender e clique uma vez no +.", "It happens when the selected minion count exceeds your Spirit. Press − until + lights up and click + once.")},
 {"cat": "Minions", "lvl": L("Avançado", "Advanced"), "title": L("Excluir o Sniper do Decompose", "Exclude the Sniper from Decompose"), "body": L("Para o Decompose não consumir o Skeletal Sniper, conecte um controle para liberar a opção 'excluir do alvo'.", "To stop Decompose consuming the Skeletal Sniper, plug in a controller to unlock the 'exclude from targeting' option.")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Sprint", "Sprint"), "body": L("Segure o dodge roll para começar a correr e dirija com o mouse (solte o WASD). Tomar hit correndo te derruba.", "Hold dodge roll to start sprinting and steer with the mouse (release WASD). Getting hit while sprinting knocks you down.")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Priorize Physical/Chaos para o veneno", "Prioritise Physical/Chaos for poison"), "body": L("Na configuração padrão, dano elemental no arco não aumenta o veneno — priorize % físico e físico adicionado. Isso muda SE você equipar a Plaguefinger (Power/Twink, nível 4): com ela, todo dano de hit passa a contribuir para a magnitude do veneno, elemental incluso.", "In the default setup, elemental damage on the bow doesn't raise poison — prioritise % physical and added physical. This changes IF you equip Plaguefinger (Power/Twink, level 4): with it, all hit damage contributes to poison magnitude, elemental included.")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Lesser Jeweller's Orb garantido", "Guaranteed Lesser Jeweller's Orb"), "body": L("Sandswept Marsh, Orok Campfire (primeira área do Ato 3) tem um Lesser Jeweller's Orb garantido.", "Sandswept Marsh, Orok Campfire (first Act 3 area) has a guaranteed Lesser Jeweller's Orb.")},
 {"cat": L("Respec", "Respec"), "lvl": L("Médio", "Medium"), "title": L("Respec do 58", "The level 58 respec"), "body": L("Primeiro aloque e depois desaloque a área inicial da árvore; é caro em gold, então não aposte tudo antes.", "First allocate, then deallocate the tree's starting area; it's gold-expensive, so don't gamble it all away first.")},
 {"cat": L("Defesa", "Defence"), "lvl": L("Médio", "Medium"), "title": L("Morri com ES cheio", "Died with full ES"), "body": L("Decompose e Sacrifice podem te matar sem regeneração de vida fixa (Snakebite dá regen). Tenha uma fonte de regen flat.", "Decompose and Sacrifice can kill you without flat life regen (Snakebite gives regen). Keep a flat regen source.")},
]

TROUBLESHOOT = [
 (L("No 58 não funciona nada", "Nothing works at 58"), L("Confira: Corpsewade equipada, Bind Spectre só no Set 2 com a quantidade no máximo, Sacrifice ativo e arma nos dois sets. Sem supports o dano é baixo — guarde-os no leveling.", "Check: Corpsewade equipped, Bind Spectre only on Set 2 with the amount at max, Sacrifice active and a weapon on both sets. Without supports damage is low — save them while leveling.")),
 (L("Minions não aparecem no Set 2", "Minions don't appear on Set 2"), L("Cada skill deve estar ativa em só um set. Bind Spectre: quantidade máxima no Set 2 e 0 no Set 1 (tecla G → seta → caixas no canto).", "Each skill must be active on only one set. Bind Spectre: max amount on Set 2 and 0 on Set 1 (G key → arrow → checkboxes in the corner).")),
 (L("Decompose fraco", "Weak Decompose"), L("Suba o nível da Corpsewade (nível do skill), coloque Deadly Poison II e Persistent Ground III e use Despair/Withering Presence no nível máximo.", "Raise Corpsewade's level (skill level), use Deadly Poison II and Persistent Ground III and keep Despair/Withering Presence at max level.")),
 (L("Tomo dano ao trocar de set", "I take damage when swapping sets"), L("O ES total muda entre sets e algum efeito de swap dá dano físico depois de 4 s em troca de um buff de 15% — é esperado.", "Total ES changes between sets and a swap effect deals physical damage after 4 s in exchange for a 15% buff — that's expected.")),
 (L("Toxic Growth não explode rápido", "Toxic Growth isn't blowing up fast"), L("Faltam nuvens por baixo (Gas Arrow) ou venenos. Enquanto isso, use Poisonburst Arrow.", "Missing clouds underneath (Gas Arrow) or poisons. Meanwhile, use Poisonburst Arrow.")),
]

ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Resists 75% · Blood Elementals", "Resists 75% · Blood Elementals"), gear="Corpsewade · Snakebite"),
 dict(stage="T1–T10", goal=L("Blasphemy · Ghost Dance · Wind Dancer", "Blasphemy · Ghost Dance · Wind Dancer"), gear=L("Sceptres com Spirit", "Spirit sceptres")),
 dict(stage="T11–T15", goal=L("Overwhelming Toxicity · Traveller's Wisdom", "Overwhelming Toxicity · Traveller's Wisdom"), gear="Shavronne's Satchel · Astramentis"),
 dict(stage=L("Juiced / Pinnacle", "Juiced / Pinnacle"), goal=L("Cast on Minion Death · Lineage", "Cast on Minion Death · Lineage"), gear="Mageblood · For Utopia"),
]

FIXES_LEVELING_NOTE = L("O guia de leveling do Skadoosh (Mobalytics) só dá prioridade de afixo (% físico, físico adicionado, + projéteis, Movement Speed) sem nenhuma unique nos níveis 1-57. As uniques desta página nesses níveis (Surefooted Sigil, Goldrim, Wanderlust, Splinterheart, Ghostmarch, The Lethal Draw, Death's Harp, Snakebite, Slivertongue) foram preenchidas aqui com itens reais e baratos (todos abaixo de 0,03 divine) que combinam com Poisonburst Arrow/Toxic Growth — os mesmos validados nas páginas de outras builds de veneno.",
                              "Skadoosh's leveling guide (Mobalytics) only gives affix priority (% physical, added physical, + projectiles, Movement Speed) with no uniques at all for levels 1-57. This page's uniques at those levels (Surefooted Sigil, Goldrim, Wanderlust, Splinterheart, Ghostmarch, The Lethal Draw, Death's Harp, Snakebite, Slivertongue) were filled in here with real, cheap items (all under 0.03 divine) that fit Poisonburst Arrow/Toxic Growth — the same ones validated on other poison-build pages.")
CRAFT = [
 FIXES_LEVELING_NOTE,
 L("Arco de leveling: Transmutation/Augmentation em arcos brancos; Regal/Exalted só se já tiver vários stats bons.", "Leveling bow: Transmutation/Augmentation on white bows; Regal/Exalted only if it already has several good stats."),
 L("Maça do Set 1 (Skadoosh): maça de uma mão com 2 sockets → Perfect Essence of Abrasion num item de 6 mods → Omen of Sinistral Necromancy + Omen of the Liege + Preserved Jawbone para 'increased Damage against Fully Broken Armour'.", "Set 1 mace (Skadoosh): 2-socket one-handed mace → Perfect Essence of Abrasion on a 6-mod item → Omen of Sinistral Necromancy + Omen of the Liege + Preserved Jawbone for 'increased Damage against Fully Broken Armour'."),
 L("Sceptres: Spirit acima de tudo; Perfect Essence of Command no Set 1 (magnitude das auras).", "Sceptres: Spirit above all; Perfect Essence of Command on Set 1 (aura magnitude)."),
]

T("item", "Corpsewade", 11, L("Nível 11 para equipar · Sacrifice (58) para virar dano principal", "Level 11 to equip · Sacrifice (58) to become main damage"), L("Equipável desde o 11; a transição de verdade é no 58.", "Equippable from 11; the real transition is at 58."), L("Decompose a cada passo — bônus passivo antes do 58, dano principal depois (com Sacrifice).", "Decompose every step — a passive bonus before 58, main damage after (with Sacrifice)."), L("Compre e guarde cedo se achar barata; ela não estraga nada equipando antes do 58, só não é seu dano principal ainda.", "Buy and stash it early if it's cheap; equipping it before 58 doesn't hurt anything, it just isn't your main damage yet."), L("Continue no poison bow como dano principal.", "Stay on the poison bow as your main damage."), [L("Perfect Jeweller's Orb para 5 sockets.", "Perfect Jeweller's Orb for 5 sockets.")])
T("item", "Snakebite", 33, L("Nível 33 (PoE2DB)", "Level 33 (PoE2DB)"), L("Muito antes do Decompose (58); serve no arco também.", "Well before Decompose (58); also works on the bow."), L("+1 veneno simultâneo por alvo + regen + Chaos Resistance.", "+1 simultaneous poison per target + regen + Chaos Resistance."), L("Se a resistência elemental ainda estiver baixa, uma luva rare resolve mais.", "If elemental resistance is still low, a rare glove solves more."), L("Disputa o slot com a Plaguefinger (nível 4).", "Competes for the slot with Plaguefinger (level 4)."))
T("item", "Trenchtimbre", 16, L("Nível 16 (PoE2DB)", "Level 16 (PoE2DB)"), L("Compre a +1 cedo; guarde currency para a +2 (o alvo do endgame).", "Buy the +1 early; save currency for the +2 (the endgame target)."), L("+1 a +2 nível de todas as skills de minion.", "+1 to +2 to Level of all Minion Skills."), "—", L("Maça com + nível de minions.", "Mace with + minion levels."))
T("item", "Plaguefinger", 4, L("Nível 4 (PoE2DB)", "Level 4 (PoE2DB)"), L("[Alternativa/Power] Usável quase desde o início.", "[Alternative/Power] Usable from almost the very start."), L("Todo dano de hit conta para o veneno (elemental incluso).", "All hit damage counts toward poison (elemental included)."), L("Sem ailments elementais — irrelevante para esta build.", "No elemental ailments — irrelevant for this build."), L("Disputa o slot com a Snakebite (nível 33).", "Competes for the slot with Snakebite (level 33)."))
T("item", "Shavronne's Satchel", 62, L("Nível 62 (PoE2DB)", "Level 62 (PoE2DB)"), L("Entra quando Enduring Elixirs estiver ativa.", "Comes in once Enduring Elixirs is active."), L("Recuperação de flask também vira Energy Shield.", "Flask recovery also becomes Energy Shield."), "—", "—")
T("item", "Astramentis", 24, L("Nível 24 (PoE2DB)", "Level 24 (PoE2DB)"), L("Twink/Power desde a campanha se tiver currency; padrão do Endgame a partir do 65.", "Twink/Power from the campaign if you have the currency; Endgame default from 65."), L("+50–100 em todos os atributos.", "+50–100 to all attributes."), L("Resolve atributos, não é dano.", "Fixes attributes, isn't damage."), "—")
T("skill", "Bind Spectre", 50, L("Blood Elemental (~67 Spirit)", "Blood Elemental (~67 Spirit)"), L("Capture antes do 58 (Aggorat em diante).", "Capture before 58 (Aggorat onwards)."), L("Combustível do Decompose.", "Decompose fuel."), "—", "—")
T("skill", "Sacrifice", 58, L("60 Spirit", "60 Spirit"), L("No 58.", "At 58."), L("Minions servem de corpo.", "Minions serve as corpses."), "—", "—")
T("asc", "Overwhelming Toxicity", 72, L("Ascendência Pathfinder", "Pathfinder ascendancy"), L("4º Trial, só com venenos sustentados.", "4th Trial, only with sustained poisons."), L("Dobra o limite de venenos.", "Doubles the poison cap."), L("Sem sustentar, os 50% less duração atrapalham.", "Without sustain, the 50% less duration hurts."), "—")

CASES = [
 (L("Devo usar Uhtred's Augury no Bind Spectre?", "Should I use Uhtred's Augury on Bind Spectre?"), UHTRED_CONFLICT_NOTE),
 (L("Herald of Plague é obrigatório?", "Is Herald of Plague mandatory?"), L("Não. O próprio Skadoosh testou e confirmou (changelog 0.4): não é necessário para o clear. As 3 variantes atuais ainda o incluem, mas você pode desligá-lo em Meu personagem e usar esse Spirit em defesa — ele mesmo cita Desert Buckler como opção.", "No. Skadoosh himself tested and confirmed it (0.4 changelog): it isn't required for clear. The 3 current variants still include it, but you can untick it in My character and spend that Spirit on defence instead — he cites Desert Buckler as an option.")),
 (L("Cheguei no 58 sem Blood Elemental", "I reached 58 without a Blood Elemental"), L("Continue no poison bow (selecione 'Nível 41–57') até capturar um — a partir do Aggorat.", "Stay on the poison bow (pick 'Level 41–57') until you capture one — from Aggorat onwards.")),
 (L("Pouco Spirit no Set 2", "Little Spirit on Set 2"), L("Se não cabem 3 Blood Elementals, tire Minion Mastery do Bind Spectre até caberem.", "If 3 Blood Elementals don't fit, remove Minion Mastery from Bind Spectre until they do.")),
 (L("Quero single target sem gear", "I want single target without gear"), L("Plague Bearer com Deadly Poison II e Poison III no boss; Toxic Growth com Long Fuse II ainda funciona como opção.", "Plague Bearer with Deadly Poison II and Poison III on bosses; Toxic Growth with Long Fuse II still works as an option.")),
]

SOURCES = [
 dict(name="Skadoosh — [0.5.5] Fartfinder: Corpsewade Decompose Pathfinder (Mobalytics)", use=L("Endgame: 3 variantes, gems, itens, árvore, FAQ e crafts", "Endgame: 3 variants, gems, items, tree, FAQ and crafts"), url=GUIDE_URL),
 dict(name="Skadoosh — Poison Pathfinder Leveling 1–58 (Mobalytics)", use=L("Leveling: 5 fases de 1 a 58", "Leveling: 5 phases from 1 to 58"), url=LEVELING_URL),
 dict(name="PoE2DB — Blood Elemental", use=L("Spectre e reserva de Spirit", "Spectre and Spirit reservation"), url="https://poe2db.tw/us/Blood_Elemental"),
 dict(name="Game8 — Blood Elemental Location", use=L("Onde capturar (Aggorat, Ato 3)", "Where to capture (Aggorat, Act 3)"), url="https://game8.co/games/Path-of-Exile-2/archives/515159"),
 dict(name="Path of Building (PoE2) — Gems.lua, Skills", use=L("Descrições, custos de Spirit e tiers", "Descriptions, Spirit costs and tiers"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name="PoE2DB — Corpsewade, Snakebite, Trenchtimbre, Shavronne's Satchel, Astramentis, Widowhail, Plaguefinger", use=L("Required level real de cada item, conferido item a item em 21/09/2026 — não inferido pela fase do guia", "Each item's real required level, checked item by item on 21/09/2026 — not inferred from the guide's phase"), url="https://poe2db.tw/us/Corpsewade"),
 dict(name="Mobalytics — __PRELOADED_STATE__ das 3 variantes (Starter, Endgame e Uber)", use=L("Ascendência real nó a nó, gems por variante e updatedAt da fonte, lidos ao vivo em 21/09/2026", "Real node-by-node ascendancy, gems per variant and source updatedAt, read live on 21/09/2026"), url=GUIDE_URL),
]
WIDOWHAIL_NOTE = L("Widowhail (arco, nível 1, '150-250% increased bonuses from equipped Quiver') foi AVALIADA e NÃO recomendada nesta build. A base 'Crude Bow' tem dano físico fixo e baixíssimo (6-9, não escala com nada) — como o veneno escala com o dano do PRÓPRIO ARCO, amplificar os bônus de uma aljava comum (The Lethal Draw, Toxic Quiver) não chega perto de compensar perder o físico alto de um arco normal ou da Slivertongue. Não é BIS por padrão: só valeria com uma aljava com dano bruto excepcional, que não existe entre as opções desta build.",
                     "Widowhail (bow, level 1, '150-250% increased bonuses from equipped Quiver') was EVALUATED and NOT recommended for this build. The 'Crude Bow' base has fixed, very low physical damage (6-9, doesn't scale with anything) — since poison scales off the BOW's OWN damage, amplifying a normal quiver's bonuses (The Lethal Draw, Toxic Quiver) comes nowhere close to compensating for losing a normal bow's or Slivertongue's high physical. It isn't BiS by default: it would only be worth it with an exceptionally high-damage quiver, which doesn't exist among this build's options.")
FIXES = [
 WIDOWHAIL_NOTE,
 L("As árvores de ascendência de algumas variantes do guia tinham mais pontos do que os Trials dão naquele nível; o app mostra só o que dá para alocar em cada fase (2 pontos por Trial).", "Some guide variants had more ascendancy points than the Trials grant at that level; the app only shows what you can allocate in each phase (2 points per Trial)."),
 L("Os dois guias do Skadoosh viraram uma rota só: leveling (1–57) e Decompose (58+). A árvore muda no 58 (respec).", "Skadoosh's two guides became a single route: leveling (1–57) and Decompose (58+). The tree changes at 58 (respec)."),
 L("Custos: Plague Bearer, Herald of Plague, Withering Presence, Ghost Dance, Wind Dancer, Cast on Minion Death e Grim Feast = 30 Spirit; Sacrifice = 60 (Path of Building). Blood Elemental ≈ 67 (PoE2DB).", "Costs: Plague Bearer, Herald of Plague, Withering Presence, Ghost Dance, Wind Dancer, Cast on Minion Death and Grim Feast = 30 Spirit; Sacrifice = 60 (Path of Building). Blood Elemental ≈ 67 (PoE2DB)."),
 L("O Spirit do endgame é por weapon set: o planejador soma um set de cada vez.", "Endgame Spirit is per weapon set: the planner sums one set at a time."),
 L(f"Fonte verificada ao vivo em {SNAPSHOT}: guia de build atualizado em {SOURCE_UPDATED}, guia de leveling em {LEVELING_SOURCE_UPDATED} (checado via __PRELOADED_STATE__.updatedAt do Mobalytics, não pela data exibida na página). Se a fonte for atualizada de novo depois desta data, esta página pode ficar desatualizada até a próxima conversão.",
   f"Live-checked on {SNAPSHOT}: build guide last updated {SOURCE_UPDATED}, leveling guide {LEVELING_SOURCE_UPDATED} (checked via Mobalytics' __PRELOADED_STATE__.updatedAt, not the date shown on the page). If the source updates again after this date, this page may fall behind until the next conversion."),
 L("Ascendência corrigida contra os dados reais: Relentless Pursuit NUNCA aparece nas 3 variantes atuais (Starter, Endgame e Uber) — é pick só de leveling, respecado para Enduring Elixirs no switch do 58 (conferido nó a nó contra tree.json).", "Ascendancy corrected against the real data: Relentless Pursuit NEVER appears in the 3 current variants (Starter, Endgame and Uber) — it's a leveling-only pick, respecced into Enduring Elixirs at the level 58 switch (checked node-by-node against tree.json)."),
 L("Herald of Plague reclassificado de obrigatório para opcional: o próprio Skadoosh testou e confirmou no changelog 0.4 que não é necessário para o clear, citando Desert Buckler como alternativa de defesa.", "Herald of Plague reclassified from mandatory to optional: Skadoosh himself tested and confirmed in the 0.4 changelog that it isn't needed for clear, citing Desert Buckler as a defensive alternative."),
]

UI = dict(
 setNote=L("rares com dano de caos, veneno e defesa.", "rares with chaos damage, poison and defence."),
 carry=r"^(Poisonburst Arrow|Toxic Growth|Decompose)$", box=L("VENENO", "POISON"), spiritWhat=L("(buffs e minions)", "(buffs and minions)"),
 mechBtn=L("Abrir Veneno & Decompose", "Open Poison & Decompose"), dmg2=L("Nuvens do Decompose", "Decompose clouds"), dmgBar=L("Dano seu / das nuvens do Decompose (aprox.)", "Your damage / Decompose clouds (approx.)"),
 dmgLegend=L("nuvens do Decompose (proporção aproximada)", "Decompose clouds (approximate ratio)"),
 earlyGone=L("Skills iniciais já saíram da barra: você passou do nível {u}.", "Starting skills already left the bar: you're past level {u}."),
 earlyNote=L("Skills de começo; saem no nível ~{u}.", "Early skills; they leave around level {u}."),
 treeIntro=L("Árvore real do patch 0.5.5 com os caminhos dos dois guias do Skadoosh. Até o 57: projétil e veneno com arco. No 58: respec para minions, curses e Chaos do Decompose.", "Real patch 0.5.5 tree with the paths from Skadoosh's two guides. Until 57: projectile and poison with a bow. At 58: respec into Decompose's minions, curses and Chaos."),
 set1=L("auras e debuffs", "auras and debuffs"), set2=L("minions (Bind Spectre)", "minions (Bind Spectre)"), asc="Pathfinder", cls="Ranger",
 respecTip=L("No 58 a árvore é refeita: aloque e depois desaloque a área inicial. Set 1 (vermelho) = auras; Set 2 (verde) = minions.", "At 58 the tree is rebuilt: allocate then deallocate the starting area. Set 1 (red) = auras; Set 2 (green) = minions."),
 routeIntro=L("Oito fases: cinco de leveling com arco de veneno e três de Decompose a partir do nível 58 com Corpsewade.", "Eight phases: five poison bow leveling phases and three Decompose phases from level 58 with Corpsewade."),
 socketPrio=["Toxic Growth / Decompose (Perfect Jeweller's)", "Plague Bearer", "Bind Spectre", "Blasphemy · Despair", "Cast on Minion Death"],
 permIntro=L("Nada disso volta depois. Spirit paga Plague Bearer e Herald of Plague no leveling e, no endgame, dois sets separados (auras no Set 1, minions no Set 2).", "None of this comes back later. Spirit pays for Plague Bearer and Herald of Plague while leveling and, in endgame, two separate sets (auras on Set 1, minions on Set 2)."),
 atlasCards=[[L("Mapas de monstros com muita vida", "High-life monster maps"), L("O Decompose escala com a vida do corpo: mapas com monstros mais fortes rendem nuvens mais fortes. O Skadoosh mostra T16 de 11 mods com Aldur's 6 runas.", "Decompose scales with corpse life: maps with stronger monsters give stronger clouds. Skadoosh shows 11-mod T16 with Aldur's 6 runes.")],
             [L("Cuidado com", "Watch out for"), L("Mods que bloqueiam recuperação e ambientes onde você não consegue andar muito (Decompose depende de passos).", "Mods that block recovery and places where you can't walk much (Decompose depends on steps).")]],
 foot=L("Guia baseado nos builds do Skadoosh (Mobalytics), dados de jogo do Path of Building e preços do poe.ninja", "Guide based on Skadoosh's builds (Mobalytics), Path of Building game data and poe.ninja prices"),
)

CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens, Árvore e Veneno & Decompose se adaptam na hora. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items, Tree and Poison & Decompose tabs adapt instantly. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit do Set 1", "Set 1 Spirit"), L("ex.: 250", "e.g. 250")], ["spirit2", L("Spirit do Set 2", "Set 2 Spirit"), L("ex.: 300", "e.g. 300")], ["life", L("Vida máxima", "Max life"), ""]],
 tiles=[[L("Set 1 reservado", "Set 1 reserved"), "used"], [L("Set 1 livre", "Set 1 free"), "free"], [L("Spirit do Set 2", "Set 2 Spirit"), "spirit2"]],
 buffs=[dict(key="pbear", name="Plague Bearer", cost=30), dict(key="herald", name="Herald of Plague", cost=30), dict(key="wither", name="Withering Presence", cost=30), dict(key="ghost", name="Ghost Dance", cost=30), dict(key="wind", name="Wind Dancer", cost=30), dict(key="sniper", name="Skeletal Sniper", cost=30, note=L("nível 20", "level 20"))],
 own=[
  ["gear", "Corpsewade", "Corpsewade"], ["gear", "Snakebite", "Snakebite"], ["gear", "Trenchtimbre", "Trenchtimbre"], ["gear", "sceptres", L("Stoic Sceptre com Spirit nos dois sets", "Spirit Stoic Sceptre on both sets")],
  ["gear", "Shavronne's Satchel", "Shavronne's Satchel"], ["gear", "Astramentis", "Astramentis"], ["gear", "Mageblood", "Mageblood"], ["gear", "respecgold", L("Gold para o respec do 58", "Gold for the level 58 respec")],
  ["gear", "Plaguefinger", L("Plaguefinger equipada (Power/Twink)", "Plaguefinger equipped (Power/Twink)")],
  ["gem", "pbear", "Plague Bearer (30)"], ["gem", "herald", "Herald of Plague (30)"], ["gem", "wither", "Withering Presence (30)"], ["gem", "ghost", "Ghost Dance (30)"], ["gem", "wind", "Wind Dancer (30)"], ["gem", "sniper", L("Skeletal Sniper (30 no nível 20)", "Skeletal Sniper (30 at level 20)")],
  ["gem", "elemental", L("Blood Elemental capturado", "Captured Blood Elemental")], ["gem", "bindset2", L("Bind Spectre: 0 no Set 1, máximo no Set 2", "Bind Spectre: 0 on Set 1, max on Set 2")], ["gem", "sacrifice", "Sacrifice (60)"], ["gem", "blasph", "Blasphemy + Temporal Chains"], ["gem", "grim", "Grim Feast"], ["gem", "comd", "Cast on Minion Death"],
  ["tree", "respec", L("Árvore do Decompose (respec feito)", "Decompose tree (respec done)")], ["tree", "timeless", L("Timeless jewel", "Timeless jewel")],
  ["asc", "relentless", "Relentless Pursuit"], ["asc", "seeker", "Path Seeker"], ["asc", "elixirs", "Enduring Elixirs"], ["asc", "toxicity", "Overwhelming Toxicity"], ["asc", "wisdom", "Traveller's Wisdom"], ["asc", "sustainable", "Sustainable Practices"],
 ],
 rules=[
  dict(when=dict(lvMin=11, lvMax=57, notOwn=["Corpsewade"]), lvl="tip", t=L("Corpsewade já pode ser equipada", "Corpsewade can already be equipped"), d=L("Nível 11 (PoE2DB) — funciona desde já como bônus passivo. Não é obrigatória agora, mas comprar cedo custa pouco.", "Level 11 (PoE2DB) — already works as a passive bonus. Not mandatory yet, but buying it early is cheap."), tab="gear"),
  dict(when=dict(lvMin=58, notOwn=["Corpsewade"]), lvl="bad", t=L("Sem Corpsewade", "No Corpsewade"), d=L("Sem ela não existe Decompose: continue no poison bow (fase Nível 41–57).", "Without it there's no Decompose: stay on the poison bow (Level 41–57 phase)."), tab="gear"),
  dict(when=dict(lvMin=52, lvMax=57, notOwn=["Corpsewade"]), lvl="warn", t=L("Compre a Corpsewade agora", "Buy Corpsewade now"), d=L("É barata; sem ela o switch do 58 não começa (o que É obrigatório no 58 é Sacrifice, não a bota em si).", "It's cheap; without it the level 58 switch can't start (what IS mandatory at 58 is Sacrifice, not the boots themselves)."), tab="gear"),
  dict(when=dict(lvMin=58, own=["Corpsewade"], notOwn=["sacrifice", "elemental", "bindset2"]), lvl="bad", t=L("Ainda NÃO faça o switch — setup mínimo incompleto", "Do NOT switch yet — minimum setup incomplete"), d=L("Faltam: Sacrifice e/ou Blood Elemental e/ou Bind Spectre configurado (0 no Set 1, máximo no Set 2). Continue no poison bow até marcar os três.", "Missing: Sacrifice and/or Blood Elemental and/or Bind Spectre configured (0 on Set 1, max on Set 2). Stay on the poison bow until all three are ticked."), tab="mech"),
  dict(when=dict(lvMin=58, own=["Corpsewade", "sacrifice", "elemental", "bindset2"], numLt=["spirit2", 90]), lvl="warn", t=L("Setup mínimo pronto, mas Spirit do Set 2 está curto", "Minimum setup ready, but Set 2 Spirit is short"), d=L("Sacrifice (60) + pelo menos 1 Blood Elemental (~67, estimado a partir do custo do PoE2DB) pedem uns 127 de Spirit no Set 2. Abaixo disso o respec ainda compensa, mas você só sustenta 1 minion.", "Sacrifice (60) + at least 1 Blood Elemental (~67, estimated from PoE2DB's cost) need around 127 Set 2 Spirit. Below that the respec still pays off, but you'll only sustain 1 minion."), tab="mech"),
  dict(when=dict(lvMin=58, own=["Corpsewade", "sacrifice", "elemental", "bindset2"], numGt=["spirit2", 89], numLt=["spirit2", 250]), lvl="tip", t=L("Setup CONFORTÁVEL: 2–3 Blood Elementals", "COMFORTABLE setup: 2–3 Blood Elementals"), d=L("Com esse Spirit de Set 2 você já sustenta vários minions de corpo — dá para jogar mapas normais sem sofrer. O alvo do autor no Uber é 444 (para 5), não é requisito do Starter.", "With this much Set 2 Spirit you already sustain several corpse minions — good enough for regular maps without suffering. The author's Uber target is 444 (for 5), that is not a Starter requirement."), tab="mech"),
  dict(when=dict(lvMin=58, own=["Corpsewade", "sacrifice", "elemental", "bindset2"], numGt=["spirit2", 249]), lvl="ok", t=L("Setup ENDGAME TARGET: Spirit de Set 2 alto", "ENDGAME TARGET setup: high Set 2 Spirit"), d=L("Você já está perto do alvo avançado do próprio Skadoosh (444 de Spirit no Set 2 para 5 Blood Elementals no Uber).", "You're already close to Skadoosh's own advanced target (444 Set 2 Spirit for 5 Blood Elementals at Uber)."), tab="mech"),
  dict(when=dict(lvMin=50, notOwn=["elemental"]), lvl="warn", t=L("Capture um Blood Elemental", "Capture a Blood Elemental"), d=L("Bind Spectre num Blood Elemental (a partir do Aggorat, Ato 3).", "Bind Spectre on a Blood Elemental (from Aggorat, Act 3)."), tab="mech"),
  dict(when=dict(lvMin=52, lvMax=58, notOwn=["respecgold"]), lvl="tip", t=L("Guarde gold", "Save gold"), d=L("O respec do 58 é caro.", "The 58 respec is expensive."), tab="mech"),
  dict(when=dict(own=["toxicity"], lvMax=75), lvl="tip", t=L("Overwhelming Toxicity cedo?", "Overwhelming Toxicity early?"), d=L("Só vale se você sustenta o máximo de venenos no boss.", "Only worth it if you sustain max poisons on bosses."), tab="asc"),
  dict(when=dict(own=["Corpsewade"], notOwn=["sacrifice"], lvMin=58), lvl="warn", t=L("Sem Sacrifice", "No Sacrifice"), d=L("Sem ele seus minions não servem de corpo para o Decompose.", "Without it your minions can't be corpses for Decompose."), tab="skills"),
  dict(when=dict(own=["Corpsewade"], notOwn=["sceptres"], lvMin=62), lvl="tip", t=L("Sceptres de Spirit", "Spirit sceptres"), d=L("Spirit é por set: um sceptre em cada set.", "Spirit is per set: one sceptre on each set."), tab="gear"),
  dict(when=dict(lvMin=26, notOwn=["relentless"]), lvl="warn", t=L("1ª ascendência pendente", "1st ascendancy pending"), d="Relentless Pursuit.", tab="asc"),
  dict(when=dict(own=["comd"], notOwn=["elemental"]), lvl="bad", t=L("Cast on Minion Death sem minions", "Cast on Minion Death without minions"), d=L("Ele precisa de minions persistentes morrendo.", "It needs persistent minions dying."), tab="skills"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["start", "end", "max"], when=dict(notOwn=["Corpsewade"]), gemsFrom="a5", note=L("Sem Corpsewade: mostrando o setup de poison bow (41–57).", "No Corpsewade: showing the poison bow setup (41–57).")),
 dict(pids=["end", "max"], when=dict(own=["Corpsewade"], notOwn=["toxicity"]), gemsFrom="start", note=L("Sem Overwhelming Toxicity: mostrando o setup inicial do Decompose.", "No Overwhelming Toxicity: showing the Decompose starter setup.")),
]
TREE_RULES = [
 dict(when=dict(lvMin=58, own=["Corpsewade"], notOwn=["respec"]), t=L("Hora do respec: aloque e depois desaloque a área inicial.", "Respec time: allocate then deallocate the starting area."), node=None),
]
TIMING_KEY = {"Corpsewade": "Corpsewade", "Snakebite": "Snakebite", "Trenchtimbre": "Trenchtimbre", "Bind Spectre": "elemental", "Sacrifice": "sacrifice", "Overwhelming Toxicity": "toxicity"}

MECH = dict(
 title=L("Veneno & Decompose", "Poison & Decompose"),
 intro=L("Como o Pathfinder mata: até o 57, flechas e pústulas de veneno; do 58 em diante, cada passo com Corpsewade transforma corpos (inclusive seus Blood Elementals) em nuvens de veneno.", "How the Pathfinder kills: until 57, poison arrows and pustules; from 58, every Corpsewade step turns corpses (including your Blood Elementals) into poison clouds."),
 sections=[
  dict(type="cards", cards=[
   [L("1. Veneno", "1. Poison"), L("Na configuração padrão desta build, priorize Physical/Chaos para a magnitude do veneno. Dano elemental normalmente NÃO contribui para o veneno desta rota — a menos que uma mecânica específica habilite isso, como a Plaguefinger (veja Power/Twink: 'All Damage from Hits Contributes to Poison Magnitude'). Cada veneno é um stack separado até o limite do alvo; Snakebite e Overwhelming Toxicity aumentam o limite.", "In this build's default setup, prioritise Physical/Chaos for poison magnitude. Elemental damage normally does NOT contribute to poison on this route — unless a specific mechanic enables it, like Plaguefinger (see Power/Twink: 'All Damage from Hits Contributes to Poison Magnitude'). Each poison is a separate stack up to the target's cap; Snakebite and Overwhelming Toxicity raise the cap.")],
   [L("2. Leveling: pústulas", "2. Leveling: pustules"), L("Gas Arrow cria nuvens; Toxic Growth solta pústulas que, envenenadas, detonam antes e mais forte. Contagion espalha tudo quando o alvo morre; Plague Bearer guarda veneno e solta de uma vez.", "Gas Arrow creates clouds; Toxic Growth drops pustules that detonate sooner and harder when poisoned. Contagion spreads everything when the target dies; Plague Bearer stores poison and releases it at once.")],
   [L("3. Corpsewade", "3. Corpsewade"), L("A cada 1,2 m andados a bota lança Decompose num corpo perto: uma nuvem de gás venenoso inflamável cujo dano depende da vida do monstro. Com Sacrifice, seus minions revivíveis servem de corpo.", "Every 1.2 m travelled the boots cast Decompose on a nearby corpse: a flammable poison gas cloud whose damage depends on the monster's life. With Sacrifice, your reviving minions serve as corpses.")],
   [L("4. Dois sets, dois Spirits", "4. Two sets, two Spirits"), L("Set 1 (maça + sceptre) guarda auras e debuffs; Set 2 (Trenchtimbre + sceptre) invoca Blood Elementals. Trocar de set invoca os minions — eles viram combustível do Decompose. Assim você usa quase o dobro de Spirit.", "Set 1 (mace + sceptre) holds auras and debuffs; Set 2 (Trenchtimbre + sceptre) summons Blood Elementals. Swapping sets summons the minions — they become Decompose fuel. That way you use almost double Spirit.")],
  ]),
  dict(type="steps", h=L("A troca do nível 58", "The level 58 swap"), steps=[
   [L("Antes", "Before"), L("Corpsewade, Snakebite, Trenchtimbre, dois Stoic Sceptres, gold e supports guardados.", "Corpsewade, Snakebite, Trenchtimbre, two Stoic Sceptres, gold and saved supports.")],
   [L("Capturar", "Capture"), L("Bind Spectre num Blood Elemental (a partir do Aggorat, Ato 3).", "Bind Spectre on a Blood Elemental (from Aggorat, Act 3).")],
   [L("Respec", "Respec"), L("Aloque e depois desaloque a área inicial da árvore; siga a árvore da fase 'Decompose: início'.", "Allocate then deallocate the tree's starting area; follow the 'Decompose: start' phase tree.")],
   [L("Configurar os sets", "Set up the sets"), L("Tecla G → seta ao lado do dano → marque o set de cada skill. Bind Spectre: quantidade máxima no Set 2, zero no Set 1.", "G key → arrow next to damage → tick each skill's set. Bind Spectre: max amount on Set 2, zero on Set 1.")],
   [L("Testar", "Test"), L("Troque para o Set 2, ande em cima dos Blood Elementals e veja as nuvens nascerem; volte ao Set 1 para as auras.", "Swap to Set 2, walk over the Blood Elementals and watch the clouds spawn; swap back to Set 1 for the auras.")],
  ]),
  dict(type="rotation", blocks=[
   [L("Mapas", "Maps"), [L("Ande: Corpsewade usa os corpos dos packs", "Walk: Corpsewade uses pack corpses"), L("Plague Bearer mata parte de vários packs (não tudo)", "Plague Bearer kills part of several packs (not everything)"), L("Nuvens limpam os sobreviventes", "Clouds clean up survivors"), L("Corra (sprint) para o próximo pack", "Sprint to the next pack")]],
   [L("Boss (Decompose completo)", "Boss (full Decompose)"), [L("Fora de combate: troque de set e pré-carregue nuvens", "Out of combat: swap sets and pre-load clouds"), L("Set 1: Despair + Contagion + Plague Bearer", "Set 1: Despair + Contagion + Plague Bearer"), L("Blood Elementals morreram: Set 2 + Grim Feast", "Blood Elementals died: Set 2 + Grim Feast"), L("Volte ao Set 1 (debuffs só funcionam nele)", "Back to Set 1 (debuffs only work there)")]],
   [L("Boss (Decompose ainda incompleto — fallback)", "Boss (Decompose still incomplete — fallback)"), [L("A própria fonte é honesta sobre isso: single-target fraco cedo/sem gear é uma fraqueza conhecida da build, não um erro seu.", "The source itself is upfront about this: weak single-target early/without gear is a known build weakness, not something you're doing wrong."), L("Sem Blood Elemental/Sacrifice prontos: NÃO force o switch. Use Despair (curse) + Plague Bearer (Deadly Poison II + Poison III) no boss, igual à fase 'Nível 41–57'", "Without Blood Elemental/Sacrifice ready: do NOT force the switch. Use Despair (curse) + Plague Bearer (Deadly Poison II + Poison III) on the boss, same as the 'Level 41–57' phase"), L("Toxic Growth com Long Fuse II ainda funciona como opção de alvo único se você tiver as gems", "Toxic Growth with Long Fuse II still works as a single-target option if you have the gems"), L("Nunca fique numa transição que limpa pack mas não mata boss: volte ao setup anterior até o checklist do switch fechar", "Never stay on a transition that clears packs but can't kill a boss: fall back to the previous setup until the switch checklist is complete")]],
  ]),
  dict(type="spirit", h=L("Spirit do Set 1", "Set 1 Spirit"), p=L("Marque as auras e buffs do Set 1. O Set 2 paga Bind Spectre (~67 por Blood Elemental, estimado do custo do PoE2DB — o autor não publica o valor exato) e Sacrifice (60) à parte.", "Tick Set 1 auras and buffs. Set 2 pays Bind Spectre (~67 per Blood Elemental, estimated from PoE2DB's cost — the author doesn't publish an exact figure) and Sacrifice (60) separately."),
       note=L("Blasphemy reserva conforme a curse; confira no jogo. Herald of Plague é OPCIONAL (o próprio Skadoosh testou e confirmou que não é necessário para o clear) — desligue-o aqui se quiser gastar o Spirit em defesa (ex.: Desert Buckler) em vez dele.", "Blasphemy reserves based on the curse; check in game. Herald of Plague is OPTIONAL (Skadoosh himself tested and confirmed it's not needed for clear) — untick it here if you'd rather spend that Spirit on defence (e.g. Desert Buckler) instead.")),
  dict(type="table", h=L("Pronto para o Decompose? (checklist do switch do 58)", "Ready for Decompose? (level 58 switch checklist)"),
       cols=[L("Item", "Item"), L("Como saber", "How to tell"), L("Status na página", "Status on this page")], rows=[
   [L("Level ≥ 58", "Level ≥ 58"), L("Seu nível de personagem", "Your character level"), L("Automático (campo de nível no topo)", "Automatic (level field at the top)")],
   [L("Corpsewade equipada", "Corpsewade equipped"), L("Já pode desde o 11 — confira se está NO PÉ, não só no baú", "Already possible from 11 — check it's WORN, not just in your stash"), L("Marque 'Corpsewade' em Meu personagem", "Tick 'Corpsewade' in My character")],
   [L("Sacrifice desbloqueado", "Sacrifice unlocked"), L("Só existe a partir do nível 58", "Only exists from level 58 on"), L("Marque 'Sacrifice (60)' em Meu personagem", "Tick 'Sacrifice (60)' in My character")],
   [L("Blood Elemental capturado", "Blood Elemental captured"), L("Bind Spectre num Blood Elemental, a partir do Aggorat (Ato 3)", "Bind Spectre on a Blood Elemental, from Aggorat (Act 3) onward"), L("Marque 'Blood Elemental capturado'", "Tick 'Captured Blood Elemental'")],
   [L("Bind Spectre presente e configurado", "Bind Spectre present and configured"), L("Tecla G → seta ao lado do dano → 0 no Set 1, máximo no Set 2", "G key → arrow next to the damage number → 0 on Set 1, max on Set 2"), L("Marque 'Bind Spectre: 0 no Set 1, máximo no Set 2'", "Tick 'Bind Spectre: 0 on Set 1, max on Set 2'")],
   [L("Spirit suficiente no Set 2", "Enough Set 2 Spirit"), L("Sacrifice (60) + ~67 por Blood Elemental", "Sacrifice (60) + ~67 per Blood Elemental"), L("Preencha 'Spirit do Set 2' — a página calcula mínimo, confortável ou endgame sozinha", "Fill in 'Set 2 Spirit' — the page works out minimum, comfortable or endgame on its own")],
   [L("Weapon Set 1 correto (auras/debuffs)", "Weapon Set 1 correct (auras/debuffs)"), L("Plague Bearer, Despair, Contagion, Withering Presence — Herald of Plague é opcional", "Plague Bearer, Despair, Contagion, Withering Presence — Herald of Plague is optional"), L("Confira na aba Skills", "Check the Skills tab")],
   [L("Weapon Set 2 correto (minions)", "Weapon Set 2 correct (minions)"), L("Trenchtimbre + Bind Spectre + Sacrifice", "Trenchtimbre + Bind Spectre + Sacrifice"), L("Confira na aba Skills", "Check the Skills tab")],
   [L("Sceptres/Spirit corretos nos dois sets", "Sceptres/Spirit correct on both sets"), L("Um Stoic Sceptre com Spirit em cada set", "One Spirit Stoic Sceptre in each set"), L("Marque 'Stoic Sceptre com Spirit nos dois sets'", "Tick 'Spirit Stoic Sceptre on both sets'")],
   [L("Trenchtimbre +2 de preferência", "Trenchtimbre +2 preferred"), L("A versão +1 já funciona; +2 é o alvo", "The +1 version already works; +2 is the target"), L("Sem checagem automática — confira o item", "No automatic check — verify the item")],
   [L("Gold do respec disponível", "Respec gold available"), L("O respec do 58 é caro em gold", "The level 58 respec is gold-expensive"), L("Marque 'Gold para o respec do 58'", "Tick 'Gold for the level 58 respec'")],
   [L("Resistências aceitáveis", "Acceptable resistances"), L("75% nas três elementais; Chaos não precisa", "75% on all three elemental; Chaos isn't needed"), L("Confira no jogo (a página não pede esse número aqui)", "Check in game (the page doesn't ask for this number here)")],
   [L("Rotação de boss conhecida", "Boss rotation known"), L("Leia o fallback de boss acima ANTES de precisar dele", "Read the boss fallback above BEFORE you need it"), L("Seção 'Boss (Decompose ainda incompleto)' nesta aba", "'Boss (Decompose still incomplete)' section in this tab")],
  ]),
  dict(type="timeline", h=L("Roteiro de power spikes (1 → 100)", "Power spike roadmap (1 → 100)"), items=[
   dict(lv=1, t=L("Poisonburst Arrow + Contagion", "Poisonburst Arrow + Contagion"), d=L("A build inteira em duas gems.", "The whole build in two gems.")),
   dict(lv=3, t=L("Stormcaller Arrow", "Stormcaller Arrow"), d=L("Primeiro dano de boss (Shock).", "First boss damage (Shock).")),
   dict(lv=4, t=L("Plaguefinger (Power/Twink, opcional)", "Plaguefinger (Power/Twink, optional)"), d=L("Se equipada: todo dano de hit passa a alimentar o veneno.", "If equipped: all hit damage starts feeding poison.")),
   dict(lv=10, t=L("Plague Bearer (King in the Mists)", "Plague Bearer (King in the Mists)"), d=L("Burst de veneno guardado.", "Stored poison burst.")),
   dict(lv=22, t=L("Toxic Growth + Gas Arrow", "Toxic Growth + Gas Arrow"), d=L("Vira o dano principal do leveling.", "Becomes the leveling's main damage.")),
   dict(lv=26, t=L("1º Trial: Relentless Pursuit", "1st Trial: Relentless Pursuit"), d=L("Leveling only — some no respec do 58.", "Leveling only — gone at the 58 respec.")),
   dict(lv=33, t=L("Snakebite (ou Plaguefinger)", "Snakebite (or Plaguefinger)"), d=L("+1 veneno simultâneo; disputa o slot com a Plaguefinger.", "+1 simultaneous poison; competes for the slot with Plaguefinger.")),
   dict(lv=38, t=L("2º Trial: Path Seeker", "2nd Trial: Path Seeker"), d=L("A única ascendência que nunca é respecada.", "The only ascendancy that's never respecced.")),
   dict(lv=39, t=L("Slivertongue (Power, opcional)", "Slivertongue (Power, optional)"), d=L("Fork de graça: fecha o buraco de dano final antes do 58.", "Free Fork: closes the last damage gap before 58.")),
   dict(lv=45, t=L("Compre e guarde: Corpsewade, Trenchtimbre", "Buy and stash: Corpsewade, Trenchtimbre"), d=L("Ambas já equipáveis (11/16); guarde gold para o respec.", "Both already equippable (11/16); save gold for the respec.")),
   dict(lv=50, t=L("Capture o Blood Elemental", "Capture the Blood Elemental"), d=L("Bind Spectre, a partir do Aggorat (Ato 3).", "Bind Spectre, from Aggorat (Act 3) onward.")),
   dict(lv=58, t=L("DECOMPOSE SWITCH", "DECOMPOSE SWITCH"), d=L("Sacrifice libera. Rode o checklist 'Pronto para o Decompose?' antes de trocar.", "Sacrifice unlocks. Run the 'Ready for Decompose?' checklist before switching.")),
   dict(lv=62, t=L("Enduring Elixirs + Shavronne's Satchel", "Enduring Elixirs + Shavronne's Satchel"), d=L("O respec do 1º Trial vira flask permanente.", "The 1st Trial's respec becomes permanent flasks.")),
   dict(lv=72, t=L("3º/4º Trial: Overwhelming Toxicity + Traveller's Wisdom", "3rd/4th Trial: Overwhelming Toxicity + Traveller's Wisdom"), d=L("Só pegue Overwhelming Toxicity sustentando o máximo de venenos.", "Only take Overwhelming Toxicity once you sustain max poisons.")),
   dict(lv=80, t=L("Uber: Cast on Minion Death, Skeletal Sniper, Lineage", "Uber: Cast on Minion Death, Skeletal Sniper, Lineage"), d=L("Mageblood troca Enduring Elixirs por Sustainable Practices.", "Mageblood swaps Enduring Elixirs for Sustainable Practices.")),
  ]),
 ],
)

exec(open(os.path.join(HERE, "bcraft.py"), encoding="utf-8").read())


def build(QUESTS_PT):
    quests = []
    for q in QUESTS_PT:
        q = dict(q)
        if q["boss"] == "Mighty Silverfist":
            q["reward"] = "2 Weapon Set Passive Points"; q["prio"] = "Alta"
        if q["boss"] == 'Medallion':
            q["reward"] = L('+1 Charm Slot · ESCOLHA: 30% increased Charm Charges gained (Skadoosh)', '+1 Charm Slot · CHOICE: 30% increased Charm Charges gained (Skadoosh)'); q["prio"] = 'Alta'
        if q["boss"] == 'Venom Draught':
            q["reward"] = L('ESCOLHA: 25% increased Stun Threshold (Skadoosh)', 'CHOICE: 25% increased Stun Threshold (Skadoosh)'); q["prio"] = 'Média'
        if q["boss"] == 'Goddess of Justice':
            q["reward"] = L('ESCOLHA: 30% increased Life Recovery from Flasks (Skadoosh)', 'CHOICE: 30% increased Life Recovery from Flasks (Skadoosh)'); q["prio"] = 'Média'
        if q["boss"] == 'Great White One':
            q["reward"] = L('ESCOLHA: +30% Armour, Evasion e Energy Shield (Shark Fin, Skadoosh)', 'CHOICE: +30% Armour, Evasion and Energy Shield (Shark Fin, Skadoosh)'); q["prio"] = 'Alta'
        if q["boss"] == "Tabana's Pillar":
            q["reward"] = L('ESCOLHA: 3% increased Movement Speed (Skadoosh: andar é o dano)', 'CHOICE: 3% increased Movement Speed (Skadoosh: walking is the damage)'); q["prio"] = 'CRÍTICA'
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="15/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=GUIDE_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=BOOK.TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None,
                ui=UI, char=CHAR, mech=MECH, adaptSwaps=ADAPT_SWAPS, treeRules=TREE_RULES, timingKey=TIMING_KEY, phaseAct=PHASE_ACT, treeOrder=ORDER + ["uber"], craftKit=CRAFT_KIT)
