# -*- coding: utf-8 -*-
"""Mercenary · Gemling Legionnaire: Whirling Slash + Glacial Bolt (besta de gelo), com a build de endgame já no leveling.

Fonte: WHIRLING Glacial Bolt Gemling [POE2 0.5] do Phylaris POE (Mobalytics, 13/08/2026): notas do autor, a árvore e os itens da variante Endgame (Early) e o PoB do endgame (nível 97).
O leveling deste guia é uma ADAPTAÇÃO: a árvore Endgame (Early) do autor é seguida desde o Ato 1 (ordem de alocação pelo menor caminho a partir da Mercenary), Whirling Slash na spear (Set 1)
e a besta no Set 2 (Permafrost no começo, Glacial Bolt do nível ~24). Níveis de gems, runas e itens seguem o Path of Building e o poe.ninja; o texto diz quando é aproximado."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("whirling")

GUIDE_URL = "https://mobalytics.gg/poe-2/profile/stone-dagger-zuckm8/builds/whirling-glacial-bolt-gemling-poe2-0-5"
POB_URL = "https://poe.ninja/poe2/pob/25d58"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "19/09/2026"

CONFIG = dict(dir="whirling", build="whirling", store="whirling1", emoji="❄", pill="Mercenary · Gemling Legionnaire",
              fonts="family=Cinzel:wght@500;700;900&family=Oxanium:wght@500;600;700&family=Exo+2:ital,wght@0,400;0,500;0,600;1,400")
TXT = {
 "pt": dict(TITLE="Ciclone de Gelo", DESC="Guia interativo Mercenary Gemling Legionnaire Whirling Glacial Bolt (besta de gelo, do nível 1 ao 100, a mesma build a campanha inteira) — PoE 2 Forbidden Rites",
            H1S="Whirling Slash na spear desde o nível 1 · Glacial Bolt do nível 24 · a build do endgame durante toda a campanha, sem respec", H1="O Ciclone de Gelo",
            LEAD="A build final já é a build do nível 1: a spear gira e quebra o gelo, a besta congela e planta as paredes de cristal. Diga seu nível e o que você já tem, e o guia mostra o que fazer agora, gema por gema, item por item, sem respec, até o Whirling Glacial Bolt de endgame."),
 "en": dict(TITLE="Frost Cyclone", DESC="Interactive Mercenary Gemling Whirling Glacial Bolt guide (ice crossbow, level 1 to 100, the same build through the whole campaign) — PoE 2 Forbidden Rites",
            H1S="Whirling Slash on the spear from level 1 · Glacial Bolt from level 24 · the endgame build all through the campaign, no respec", H1="The Frost Cyclone",
            LEAD="The final build is already the level 1 build: the spear spins and breaks the ice, the crossbow freezes and plants the crystal walls. Tell it your level and what you already have, and the guide shows what to do now, gem by gem, item by item, with no respec, up to the endgame Whirling Glacial Bolt."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["mech", "Gelo & Ciclone", "Ice & Cyclone"], ["rota", "Rota 1→100", "Route 1→100"],
        ["skills", "Skills & Supports", "Skills & Supports"], ["gear", "Itens", "Items"], ["uniques", "Uniques", "Uniques"], ["arvore", "Árvore de Passivas", "Passive Tree"],
        ["asc", "Ascendência", "Ascendancy"], ["quests", "Quests", "Quests"], ["tricks", "Truques", "Tricks"], ["diag", "Diagnóstico", "Troubleshooting"], ["fontes", "Fontes", "Sources"]]

CLASS, ASC, START = "Mercenary", "Gemling Legionnaire", 50986
ORDER = ["a1", "a2", "a3", "a4", "maps", "endgame", "max"]
VMAP = {"a1": "A1", "a2": "A2", "a3": "A3", "a4": "A4", "maps": "Mapas", "endgame": "Endgame", "max": "Aspiracional"}
FULLMAP = {k: k for k in ORDER}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a3", "maps": "a4", "endgame": "maps", "max": "endgame"}
PHASE_ACT = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "maps": 6, "endgame": 6, "max": 6}
ITEM_NOTE = {}


def socket_hint(slot, name):
    if "Crossbow" in name or "Raptor" in name:
        return [L("Glacial Rune (dano de frio na arma): Lesser no nível 1, Greater no 30", "Glacial Rune (cold damage on the weapon): Lesser at level 1, Greater at 30")]
    if slot in ("Body Armour", L("Capacete", "Helmet"), L("Luvas", "Gloves"), L("Botas", "Boots")):
        return [L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio)", "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning)")]
    return None


SP30 = L("30 Spirit", "30 Spirit")
EXTRA_ICONS = {"Morrigan's Insight": "Art/2DItems/Gems/New/NewSupport/Lineage/MorrigansRefuge.dds"}   # no RePoE o nome tem acento (Mórrigan)

# ------------------------------------------------------------------ por que cada support
SUPWHY = {
 "Rapid Attacks I": L("Ataca mais rápido: mais balas por segundo = mais Freeze e mais estilhaços.", "Attacks faster: more bolts per second = more Freeze and more shrapnel."),
 "Rapid Attacks II": L("Versão melhor do Rapid Attacks (tier 4).", "Better Rapid Attacks (tier 4)."),
 "Rapid Attacks III": L("Versão final do Rapid Attacks (tier 5).", "Final Rapid Attacks (tier 5)."),
 "Elemental Armament I": L("Mais dano elemental nos ataques: o dano da bala de gelo é todo elemental.", "More elemental damage on attacks: the ice bolt's damage is all elemental."),
 "Elemental Armament II": L("Versão melhor do Elemental Armament: mais dano elemental nos ataques.", "Better Elemental Armament: more elemental damage on attacks."),
 "Frozen Spite": L("Ao matar um inimigo Congelado, cria Ice Fragments que machucam o resto do pack.", "Killing a Frozen enemy creates Ice Fragments that hurt the rest of the pack."),
 "Concentrated Area": L("Área menor e mais dano: o estilhaço da Fragmentation acerta mais forte.", "Smaller area, more damage: Fragmentation's shrapnel hits harder."),
 "Close Combat I": L("Mais dano contra inimigos perto de você.", "More damage against enemies close to you."),
 "Close Combat II": L("Mais dano contra inimigos perto de você (versão melhor).", "More damage against enemies close to you (better version)."),
 "Deliberation": L("Você se move mais devagar ao usar a skill, mas ela dá mais dano.", "You move slower while using the skill, but it deals more damage."),
 "Magnified Area II": L("Área maior: a explosão do Herald e dos buffs pega mais gente.", "Bigger area: Herald's explosion and the buffs reach more enemies."),
 "Elemental Focus": L("Mais dano elemental, sem ailments elementais: o Herald de Gelo não precisa deles.", "More elemental damage, no elemental ailments: the Herald of Ice doesn't need them."),
 "Expanse": L("Área muito maior, mas com cooldown longo: o War Banner cobre a tela.", "Much larger area but a long cooldown: War Banner covers the screen."),
 "Prolonged Duration II": L("Duração maior do buff.", "Longer buff duration."),
 "Mark for Death II": L("O Mark causa mais dano físico e aumenta o dano que o alvo sofre.", "The Mark deals more physical damage and raises the damage the target takes."),
 "Mark of Siphoning II": L("Recupera mana ao acertar o alvo marcado.", "Recovers mana when you hit the marked target."),
 "Charged Mark": L("Ao ativar o Mark, cria chão Shocked no alvo.", "When the Mark activates, it creates Shocked Ground at the target."),
 "Eternal Mark": L("O Mark não é consumido na primeira ativação: o Freezing Mark dura mais.", "The Mark isn't consumed the first time it activates: Freezing Mark lasts longer."),
 "Multishot I": L("Mais projéteis por disparo.", "More projectiles per shot."),
 "Multishot II": L("Mais projéteis por disparo (versão melhor).", "More projectiles per shot (better version)."),
 "Pierce III": L("Projéteis atravessam mais alvos.", "Projectiles pierce more targets."),
 "Biting Frost II": L("Mais dano contra Congelados, mas consome o Freeze (deixa Chilled): só onde você quer quebrar o gelo.", "More damage against Frozen enemies but consumes the Freeze (leaves Chilled): only where you want to break the ice."),
 "Cold Mastery": L("+1 nível em skills de frio.", "+1 level on cold skills."),
 "Slow Potency": L("Slows mais fortes.", "Stronger Slows."),
 "Rapid Casting II": L("Conjura mais rápido.", "Casts faster."),
 "Cooldown Recovery II": L("Recupera cooldown mais rápido.", "Recovers cooldowns faster."),
 "Blind II": L("Cega inimigos ao acertar, com mais efeito.", "Blinds enemies on hit, with a stronger effect."),
 "Freeze": L("Mais chance de Freeze.", "More Freeze chance."),
 "Efficiency II": L("Custo menor.", "Lower cost."),
 "Echoing Cry": L("O Warcry ecoa e é usado de novo por conta própria.", "The Warcry echoes and is used again by itself."),
 "Raging Cry": L("O Warcry dá Rage para você.", "The Warcry grants you Rage."),
 "Enraged Warcry II": L("Warcries mais fortes enquanto você tem Rage.", "Stronger Warcries while you have Rage."),
 "Knockback": L("Empurra inimigos: o giro da Whirling Slash afasta o que chega perto.", "Pushes enemies: Whirling Slash's spin keeps things away."),
 "Rage III": L("A Whirling Slash gera Rage: ela é melee, então dispensa o Eternal Rage.", "Whirling Slash generates Rage: it's melee, so you can skip Eternal Rage."),
 "Longshot II": L("Mais dano contra alvos distantes.", "More damage against distant targets."),
 "Shock": L("Mais chance de Shock.", "More Shock chance."),
 "Armour Explosion": L("Consumir Armour por Warcry causa uma explosão.", "Consuming Armour via a Warcry causes an explosion."),
 "Minion Mastery": L("+1 nível nas skills de minion: a Verisium Manifestation bate mais forte.", "+1 level on minion skills: Verisium Manifestation hits harder."),
 "Vitality II": L("Regeneração de vida enquanto o buff estiver ativo.", "Life regeneration while the buff is active."),
 "Ahn's Citadel": L("Lineage: as paredes de Ice Crystals do Glacial Bolt saem ao longo de uma fissura.", "Lineage: Glacial Bolt's Ice Crystal walls come out along a fissure."),
 "Kaom's Madness": L("Lineage: cria muitas fissuras a mais (mais cristais) ao custo de dano, velocidade e área.", "Lineage: creates many more fissures (more crystals) at the cost of damage, speed and area."),
 "Vorana's Siege": L("Lineage: área maior e mais dano contra alvos isolados.", "Lineage: larger area and more damage against isolated targets."),
 "Rakiata's Flow": L("Lineage: trata as resistências elementais do inimigo como invertidas.", "Lineage: treats the enemy's elemental resistances as inverted."),
 "Rigwald's Ferocity": L("Lineage: troca dano por velocidade de ataque (ou o contrário) conforme o Weapon Set em que a skill está.", "Lineage: trades damage for attack speed (or the reverse) depending on the Weapon Set the skill is in."),
 "Morrigan's Insight": L("Lineage: mais dano e dispara Nature's Exchange ao consumir Freeze; não vai em skill que consome Freeze.", "Lineage: more damage and triggers Nature's Exchange when consuming Freeze; can't support skills that Consume Freeze."),
 "Uhtred's Augury": L("Lineage: +níveis à skill se ela tiver exatamente dois outros suportes.", "Lineage: adds levels to the skill if it has exactly two other supports."),
 "Dialla's Desire": L("Lineage: mais nível e qualidade, menos custo e reserva.", "Lineage: more level and quality, lower cost and reservation."),
 "Ritualistic Curse": L("Curse com área maior, mas que demora mais para pegar.", "A curse with larger area that takes longer to land."),
 "Temporal Chains": L("A curse que o Blasphemy vira aura: lentidão em toda a tela.", "The curse Blasphemy turns into an aura: slow across the whole screen."),
 "Armour Demolisher I": L("O Armour Break que você aplica fica mais forte (alimenta o Scavenged Plating).", "The Armour Break you apply is stronger (it feeds Scavenged Plating)."),
}

# ------------------------------------------------------------------ fases
# ------------------------------------------------------------------ fases
PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Whirling Slash + Permafrost Bolts", "Whirling Slash + Permafrost Bolts"),
  carry=L("Você: Whirling Slash (Set 1) + Permafrost Bolts (Set 2)", "You: Whirling Slash (Set 1) + Permafrost Bolts (Set 2)"), dmgSplit=[100, 0],
  goal=L("A build do endgame começa no nível 1: Set 1 = spear branca do vendor com Whirling Slash; Set 2 = Rampart Raptor (Tense Crossbow, nível 4, quase de graça; até lá, a besta que você já tem) com Permafrost Bolts e uma Lesser Glacial Rune. A Permafrost congela o pack de longe; você troca de set no botão de movimento, entra girando com a Whirling Slash (ela Desacelera, Cega e empurra) e mata o que está congelado. Fragmentation Rounds fica no Set 2 para estilhaçar o boss congelado. Depois do King in the Mists (~10, +30 Spirit) entra o Herald of Ice (nível 12): cada inimigo congelado que morre explode em gelo. Na árvore você já segue o mapa final do autor, começando pela vida e defesa (Battle-hardened e Hard to Kill).",
         "The endgame build starts at level 1: Set 1 = a white vendor spear with Whirling Slash; Set 2 = the Rampart Raptor (Tense Crossbow, level 4, nearly free; until then, the crossbow you already have) with Permafrost Bolts and a Lesser Glacial Rune. Permafrost freezes the pack from range; you swap sets on the movement button, spin in with Whirling Slash (it Slows, Blinds and knocks back) and kill what is frozen. Fragmentation Rounds stays on Set 2 to shatter the frozen boss. After King in the Mists (~10, +30 Spirit) Herald of Ice comes in (level 12): every frozen enemy that dies explodes into ice. On the tree you already follow the author's final map, starting with life and defence (Battle-hardened and Hard to Kill)."),
  rotation=[L("Permafrost Bolts (Set 2) no pack até congelar", "Permafrost Bolts (Set 2) into the pack until frozen"), L("Troque para o Set 1 e entre girando com a Whirling Slash", "Swap to Set 1 and spin in with Whirling Slash"), L("Boss congelado: Fragmentation Rounds (estilhaços)", "Frozen boss: Fragmentation Rounds (shrapnel)")],
  gems=[
   G("Whirling Slash", ["Rapid Attacks I", "Close Combat I"], L("Mover + limpar de perto", "Move + close-range clear"), L("Uncut Skill Gem nível 1 (exige spear no set): gira, Desacelera, Cega e Empurra. É o botão de movimento da build do nível 1 ao 100.", "Level 1 Uncut Skill Gem (needs a spear in the set): spins, Slows, Blinds and Knocks Back. It's the build's movement button from level 1 to 100."), "free"),
   G("Permafrost Bolts", ["Rapid Attacks I", "Elemental Armament I", "Frozen Spite"], L("Limpar + Freeze", "Clear + Freeze"), L("Balas de gelo que se fragmentam e Congelam quase tudo. Uncut nível 1: é a skill de besta até o Glacial Bolt (~24).", "Ice bolts that fragment and Freeze almost everything. Level 1 Uncut: it's your crossbow skill until Glacial Bolt (~24)."), "free"),
   G("Fragmentation Rounds", ["Elemental Armament I", "Concentrated Area", "Close Combat I"], L("Estilhaçar", "Shatter"), L("Bala perfurante que consome o Freeze e explode; acertar um Ice Crystal também o explode. Uncut nível 1: sai da barra quando o Glacial Bolt chega.", "A piercing bolt that consumes Freeze and explodes; hitting an Ice Crystal also explodes it. Level 1 Uncut: it leaves the bar when Glacial Bolt arrives."), "free", until=24),
   G("Herald of Ice", ["Magnified Area II"], L("Explosão de gelo", "Ice explosion"), L("Matar (Shatter) inimigo Congelado solta uma explosão de gelo. Uncut nível 4, 30 Spirit: só depois do King in the Mists (+30 Spirit).", "Killing (Shattering) a Frozen enemy releases an ice explosion. Level 4 Uncut, 30 Spirit: only after King in the Mists (+30 Spirit)."), "core", 1, SP30, since=12),
  ],
  cheap=["Rampart Raptor", "Tabula Rasa", "Blackheart", "Meginord's Girdle"],
  full=["Rampart Raptor", "Tabula Rasa", "Blackheart", "Meginord's Girdle"],
  stats=[L("Vida", "Life"), L("Resistência a fogo/frio/raio", "Fire/cold/lightning resistance"), L("Velocidade de ataque", "Attack speed")],
  tree=L("Os primeiros 17 pontos do mapa final: Battle-hardened (+20% Armour e Evasion) e Hard to Kill (regeneração de vida). O caminho vai da Mercenary até a região da Armour, sempre pelo menor caminho.", "The first 17 points of the final map: Battle-hardened (+20% Armour and Evasion) and Hard to Kill (life regeneration). The path runs from the Mercenary to the Armour area, always by the shortest route."),
  avoid=[L("Ficar sem spear no Set 1: sem ela a Whirling Slash não funciona", "Having no spear in Set 1: Whirling Slash doesn't work without it"), L("Gastar currency em item que sobe de nível logo", "Spending currency on an item you'll outlevel soon")],
  exit=[L("King in the Mists (~10): +30 Spirit → Herald of Ice", "King in the Mists (~10): +30 Spirit → Herald of Ice"), L("Nível 11: Wanderlust (botas) · Nível 16: Skysliver", "Level 11: Wanderlust (boots) · Level 16: Skysliver")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 31], tag=L("Skysliver e Glacial Bolt", "Skysliver and Glacial Bolt"),
  carry=L("Você: Whirling Slash (Set 1) + Glacial Bolt (Set 2)", "You: Whirling Slash (Set 1) + Glacial Bolt (Set 2)"), dmgSplit=[100, 0],
  goal=L("A virada do Ato 2 é o nível 16 e o nível 24. No 16 você troca a spear branca pela Skysliver (Winged Spear, ~0,1 Divine): dano de raio, velocidade e crítico. No ~24 cai (ou você compra) o Glacial Bolt, Uncut nível 7: ele planta duas paredes de Ice Crystals no fim do voo e vira a skill principal do Set 2; a Fragmentation sai. Agora o ciclo do endgame já existe: Glacial Bolt planta o gelo, a Whirling Slash com Biting Frost II gira e quebra os cristais. A Permafrost fica como abridor de pack até o Glacial Bolt ter os três suportes. Herald of Ice segue ligado; 1º Trial (~28): Essence of Virtue. No 30, Greater Glacial Rune na Rampart Raptor.",
         "The Act 2 turning points are level 16 and level 24. At 16 you swap the white spear for Skysliver (Winged Spear, ~0.1 Divine): lightning damage, speed and crit. Around 24 Glacial Bolt (level 7 Uncut) drops (or you buy it): it plants two walls of Ice Crystals at the end of flight and becomes your main Set 2 skill; Fragmentation leaves. Now the endgame loop already exists: Glacial Bolt plants the ice, Whirling Slash with Biting Frost II spins and breaks the crystals. Permafrost stays as the pack opener until Glacial Bolt has its three supports. Herald of Ice stays on; 1st Trial (~28): Essence of Virtue. At 30, a Greater Glacial Rune on the Rampart Raptor."),
  rotation=[L("Set 2: Glacial Bolt (Permafrost para abrir o pack)", "Set 2: Glacial Bolt (Permafrost to open the pack)"), L("Set 1: Whirling Slash gira e quebra os cristais", "Set 1: Whirling Slash spins and breaks the crystals"), L("Boss: Glacial Bolt nos pés dele, Whirling Slash em volta", "Boss: Glacial Bolt at its feet, Whirling Slash around it")],
  gems=[
   G("Whirling Slash", ["Rapid Attacks II", "Biting Frost II", "Knockback"], L("Mover + quebrar o gelo", "Move + break the ice"), L("Biting Frost II dá dano contra Congelados e quebra os Ice Crystals; Knockback afasta o que chega perto.", "Biting Frost II adds damage against Frozen enemies and breaks Ice Crystals; Knockback keeps things away."), "free"),
   G("Glacial Bolt", ["Elemental Armament II", "Rapid Attacks II", "Pierce III"], L("Dano principal", "Main damage"), L("Uncut nível 7 (~24): cria duas paredes de Ice Crystals no fim do voo. É a skill principal do nível 24 ao 100.", "Level 7 Uncut (~24): creates two walls of Ice Crystals at the end of flight. It's your main skill from level 24 to 100."), "free", since=24),
   G("Permafrost Bolts", ["Elemental Armament II", "Rapid Attacks II", "Frozen Spite"], L("Abrir o pack", "Pack opener"), L("Mesma skill de antes, suportes melhores. Sai da barra perto do 32.", "Same skill as before, better supports. It leaves the bar around 32."), "free", until=32),
   G("Fragmentation Rounds", ["Elemental Armament II", "Concentrated Area", "Deliberation", "Close Combat II"], L("Estilhaçar", "Shatter"), L("Close Combat II e Deliberation somam dano de perto. Sai quando o Glacial Bolt chega.", "Close Combat II and Deliberation add close-range damage. It leaves when Glacial Bolt arrives."), "free", since=16, until=24),
   G("Herald of Ice", ["Magnified Area II", "Elemental Focus"], L("Explosão de gelo", "Ice explosion"), L("30 Spirit (King in the Mists).", "30 Spirit (King in the Mists)."), "core", 1, SP30),
  ],
  cheap=["Skysliver", "Wanderlust", "Thrillsteel", "Rampart Raptor"],
  full=["Skysliver", "Wanderlust", "Thrillsteel", "Tabula Rasa"],
  stats=[L("Vida", "Life"), L("Resistências", "Resistances"), L("Velocidade de ataque", "Attack speed")],
  tree=L("Pontos 18–34: Sand in the Eyes (+10% velocidade de ataque e Cegueira), Authority (+15% área de ataque) e Adrenaline Rush (velocidade ao matar). Os primeiros 2 pontos de Weapon Set entram em cada set.", "Points 18–34: Sand in the Eyes (+10% attack speed and Blind), Authority (+15% attack area) and Adrenaline Rush (speed on kill). The first 2 Weapon Set points go into each set."),
  avoid=[L("Ligar o Herald sem ter os 30 Spirit livres", "Turning on Herald without the 30 Spirit free"), L("Deixar a Fragmentation no lugar do Glacial Bolt depois do 24", "Leaving Fragmentation in place of Glacial Bolt after 24")],
  exit=[L("Nível 24: Glacial Bolt (Uncut nível 7)", "Level 24: Glacial Bolt (level 7 Uncut)"), L("1º Trial (~28): Essence of Virtue · Nível 30: Greater Glacial Rune", "1st Trial (~28): Essence of Virtue · Level 30: Greater Glacial Rune")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[32, 45], tag=L("War Banner e armas forjadas", "War Banner and runeforged weapons"),
  carry=L("Você: Whirling Slash (Set 1) + Glacial Bolt (Set 2)", "You: Whirling Slash (Set 1) + Glacial Bolt (Set 2)"), dmgSplit=[100, 0],
  goal=L("A build é a mesma; agora ela ganha peças. Permafrost saiu da barra: o Glacial Bolt já abre o pack sozinho. Nível 38 é a virada de itens: Rampart Raptor Runeforged (custa quase nada) e o Ignagduk (Azak Bog) dá +30 Spirit para o War Banner (t4, 30 Spirit). No 40 a Skysliver vira Runeforged (com Soul Core of Speed), cai o Emergency Reload (Uncut nível 11: recarrega o pente e reforça as balas) e o 2º Trial libera o Gem Studded. Whirling Slash ganha Rage III: ela gera Rage, que vira dano.",
         "The build is the same; now it gains pieces. Permafrost left the bar: Glacial Bolt opens the pack on its own. Level 38 is the item turning point: a Runeforged Rampart Raptor (costs almost nothing) and Ignagduk (Azak Bog) gives +30 Spirit for War Banner (t4, 30 Spirit). At 40 Skysliver becomes Runeforged (with a Soul Core of Speed), Emergency Reload drops (level 11 Uncut: reloads the clip and empowers the bolts) and the 2nd Trial unlocks Gem Studded. Whirling Slash gains Rage III: it generates Rage, which becomes damage."),
  rotation=[L("Herald de gelo e War Banner sempre ligados", "Ice Herald and War Banner always on"), L("Set 2: Glacial Bolt; Emergency Reload quando o pente acabar", "Set 2: Glacial Bolt; Emergency Reload when the clip runs out"), L("Set 1: Whirling Slash para andar e quebrar os cristais", "Set 1: Whirling Slash to move and break the crystals")],
  gems=[
   G("Whirling Slash", ["Rapid Attacks II", "Biting Frost II", "Knockback", "Rage III"], L("Mover + quebrar o gelo", "Move + break the ice"), L("Rage III: a Whirling Slash gera Rage; mais Rage, mais dano.", "Rage III: Whirling Slash generates Rage; more Rage, more damage."), "free"),
   G("Glacial Bolt", ["Elemental Armament II", "Rapid Attacks II", "Pierce III"], L("Dano principal", "Main damage"), L("Sem mudança nos suportes.", "No support changes."), "free"),
   G("Herald of Ice", ["Magnified Area II", "Elemental Focus"], L("Explosão de gelo", "Ice explosion"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("War Banner", ["Expanse", "Prolonged Duration II"], L("Buff de ataque", "Attack buff"), L("Ao atacar você acumula Glory; no máximo, planta um Banner que dá dano, velocidade e Accuracy. Uncut nível 4, 30 Spirit (Ignagduk).", "Attacking builds Glory; at maximum you plant a Banner that grants damage, speed and Accuracy. Level 4 Uncut, 30 Spirit (Ignagduk)."), "core", 2, SP30, since=38),
   G("Emergency Reload", ["Cooldown Recovery II", "Prolonged Duration II"], L("Recarga", "Reload"), L("Recarrega todos os pentes na hora e reforça as balas por um tempo. Uncut nível 11.", "Reloads every clip instantly and empowers the bolts for a while. Level 11 Uncut."), "free", since=40),
  ],
  cheap=["Rampart Raptor", "Skysliver", "Wanderlust", "Thrillsteel"],
  full=["Rampart Raptor", "Skysliver", "Wanderlust", "Thrillsteel", "Tabula Rasa"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Velocidade de ataque", "Attack speed"), L("Dano de projétil", "Projectile damage")],
  tree=L("Pontos 35–50: Colossal Weapon (+12% área), Acceleration (+10% velocidade de skill) e Dance with Death (+25% velocidade de skill com uma arma de uma mão na mão principal e a off hand vazia — a spear). Weapon Sets: 6 pontos em cada.", "Points 35–50: Colossal Weapon (+12% area), Acceleration (+10% skill speed) and Dance with Death (+25% skill speed with a one-handed weapon in the main hand and an empty off hand — the spear). Weapon Sets: 6 points in each."),
  avoid=[L("Ligar Herald + Banner com menos de 60 Spirit", "Turning on Herald + Banner with less than 60 Spirit"), L("Esquecer de forjar a Rampart Raptor no 38", "Forgetting to runeforge the Rampart Raptor at 38")],
  exit=[L("Rampart Raptor Runeforged (38)", "Runeforged Rampart Raptor (38)"), L("Ignagduk: +30 Spirit → War Banner · 40: Emergency Reload", "Ignagduk: +30 Spirit → War Banner · 40: Emergency Reload")]),

 dict(id="a4", name=L("Ato 4 e Interlúdios", "Act 4 and Interludes"), lv=[46, 64], tag=L("Runemastered e Scavenged Plating", "Runemastered and Scavenged Plating"),
  carry=L("Você: Whirling Slash (Set 1) + Glacial Bolt (Set 2)", "You: Whirling Slash (Set 1) + Glacial Bolt (Set 2)"), dmgSplit=[100, 0],
  goal=L("Só ficar mais forte. Itens: anéis rares melhores (~50) e a Rampart Raptor Runemastered no 55 (~2 Divines, opcional — a Runeforged aguenta). O Lythara (Kriar Village, ~62) dá +40 Spirit: com 100 de Spirit você ganha o Scavenged Plating (t4, 30 Spirit), que dá defesa quando você quebra a Armour do inimigo. A árvore chega ao Battle Trance (+8 de Rage máxima, que a Whirling Slash enche) e ao Primal Growth (área).",
         "Just getting stronger. Items: better rare rings (~50) and the Runemastered Rampart Raptor at 55 (~2 Divines, optional — the Runeforged holds up). Lythara (Kriar Village, ~62) gives +40 Spirit: with 100 Spirit you get Scavenged Plating (t4, 30 Spirit), which gives defence when you break enemy Armour. The tree reaches Battle Trance (+8 maximum Rage, which Whirling Slash fills) and Primal Growth (area)."),
  rotation=[L("Herald, War Banner e Plating sempre ligados", "Herald, War Banner and Plating always on"), L("Set 2: Glacial Bolt; Emergency Reload no pente vazio", "Set 2: Glacial Bolt; Emergency Reload on an empty clip"), L("Set 1: Whirling Slash para andar, quebrar cristais e gerar Rage", "Set 1: Whirling Slash to move, break crystals and build Rage")],
  gems=[
   G("Whirling Slash", ["Rapid Attacks II", "Biting Frost II", "Knockback", "Rage III"], L("Mover + quebrar o gelo", "Move + break the ice"), L("Sem mudança.", "No change."), "free"),
   G("Glacial Bolt", ["Elemental Armament II", "Rapid Attacks II", "Pierce III"], L("Dano principal", "Main damage"), L("Sem mudança.", "No change."), "free"),
   G("Herald of Ice", ["Magnified Area II", "Elemental Focus"], L("Explosão de gelo", "Ice explosion"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("War Banner", ["Expanse", "Prolonged Duration II"], L("Buff de ataque", "Attack buff"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Scavenged Plating", ["Prolonged Duration II"], L("Defesa", "Defence"), L("Quebrar a Armour de um inimigo dá stacks de Armour e Thorns. Tier 4, 30 Spirit (Lythara).", "Breaking an enemy's Armour grants Armour and Thorns stacks. Tier 4, 30 Spirit (Lythara)."), "core", 3, SP30, since=62),
   G("Emergency Reload", ["Cooldown Recovery II", "Prolonged Duration II"], L("Recarga", "Reload"), L("Sem mudança.", "No change."), "free"),
  ],
  cheap=["Skysliver", "Thrillsteel", "Rampart Raptor", "Wanderlust"],
  full=["Rampart Raptor", "Skysliver", "Thrillsteel", "Wanderlust", "Tabula Rasa"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Velocidade de ataque e recarga", "Attack speed and reload"), L("Spirit", "Spirit")],
  tree=L("Pontos 51–72: Battle Trance (+8 de Rage máxima) e Primal Growth (+15% área ao matar). Weapon Sets: 12 pontos em cada; no Set 2 entram Forces of Nature (penetração elemental) e Presence Present.", "Points 51–72: Battle Trance (+8 maximum Rage) and Primal Growth (+15% area on kill). Weapon Sets: 12 points in each; Set 2 gets Forces of Nature (elemental penetration) and Presence Present."),
  avoid=[L("Ficar sem Spirit para o Plating (precisa dos 100 do Lythara)", "Running short of Spirit for Plating (it needs Lythara's 100)"), L("Pagar 2 Divines na Rampart antes de fechar resistências", "Paying 2 Divines for the Rampart before resistances are capped")],
  exit=[L("3º Trial (~65): Advanced Thaumaturgy", "3rd Trial (~65): Advanced Thaumaturgy"), L("Rampart Raptor Runemastered (55)", "Runemastered Rampart Raptor (55)")]),

 dict(id="maps", name=L("Mapas 65+", "Maps 65+"), lv=[65, 78], tag=L("Árvore completa e Morior Invictus", "Full tree and Morior Invictus"),
  carry=L("Você: Whirling Slash (Set 1) + Glacial Bolt (Set 2)", "You: Whirling Slash (Set 1) + Glacial Bolt (Set 2)"), dmgSplit=[100, 0],
  goal=L("Aqui a árvore principal fecha os 85 pontos do autor: nada de respec depois. Entram Maiming Strike (+25% dano de ataque), Beef e o keystone Iron Reflexes (Evasion vira Armour). Rapid Attacks III sobe no Glacial Bolt. O trabalho agora é juntar dinheiro para o Morior Invictus (nível 65, ~6 Divines): ele dá Armour, vida e Spirit por socket, e com o Spirit extra você troca Herald e Banner pelas reservas do endgame do autor (Arctic Armour, Verisium, Berserk). 4º Trial (~75): Motoric Implants (+2 níveis nas skills de Dex).",
         "Here the main tree closes the author's 85 points: no respec later. Maiming Strike (+25% attack damage), Beef and the Iron Reflexes keystone (Evasion becomes Armour) come in. Rapid Attacks III goes on Glacial Bolt. The job now is saving for Morior Invictus (level 65, ~6 Divines): it gives Armour, life and Spirit per socket, and with the extra Spirit you swap Herald and Banner for the author's endgame reservations (Arctic Armour, Verisium, Berserk). 4th Trial (~75): Motoric Implants (+2 levels on Dex skills)."),
  rotation=[L("Buffs sempre ligados", "Buffs always on"), L("Set 2: Glacial Bolt planta as paredes de gelo", "Set 2: Glacial Bolt plants the ice walls"), L("Set 1: Whirling Slash quebra e move; Emergency Reload no pente vazio", "Set 1: Whirling Slash breaks and moves; Emergency Reload on an empty clip")],
  gems=[
   G("Whirling Slash", ["Rapid Attacks III", "Biting Frost II", "Knockback", "Rage III"], L("Mover + quebrar o gelo", "Move + break the ice"), L("Rapid Attacks III (tier 5) no lugar do II.", "Rapid Attacks III (tier 5) instead of II."), "free"),
   G("Glacial Bolt", ["Elemental Armament II", "Rapid Attacks III", "Pierce III"], L("Dano principal", "Main damage"), L("Rapid Attacks III (tier 5) no lugar do II.", "Rapid Attacks III (tier 5) instead of II."), "free"),
   G("Herald of Ice", ["Magnified Area II", "Elemental Focus"], L("Explosão de gelo", "Ice explosion"), L("30 Spirit. Sai quando o Morior entrar.", "30 Spirit. Leaves when Morior comes in."), "core", 1, SP30),
   G("War Banner", ["Expanse", "Prolonged Duration II"], L("Buff de ataque", "Attack buff"), L("30 Spirit. Sai quando o Morior entrar.", "30 Spirit. Leaves when Morior comes in."), "core", 2, SP30),
   G("Scavenged Plating", ["Prolonged Duration II"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Emergency Reload", ["Cooldown Recovery II", "Prolonged Duration II"], L("Recarga", "Reload"), L("Sem mudança.", "No change."), "free"),
  ],
  cheap=["Skysliver", "Rampart Raptor", "Thrillsteel"],
  full=["Skysliver", "Morior Invictus", "Rampart Raptor"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Velocidade de ataque", "Attack speed"), L("Armour", "Armour")],
  tree=L("Pontos 73–85 fecham a árvore principal: Maiming Strike, Beef e Iron Reflexes. Weapon Sets: 20 pontos em cada (Set 1: Unyielding, Roaring Cries, Stimulants, Bond of the Wolf; Set 2: Crystal Elixir, Crushing Verdict).", "Points 73–85 close the main tree: Maiming Strike, Beef and Iron Reflexes. Weapon Sets: 20 points in each (Set 1: Unyielding, Roaring Cries, Stimulants, Bond of the Wolf; Set 2: Crystal Elixir, Crushing Verdict)."),
  avoid=[L("Comprar o Morior Invictus antes das resistências", "Buying Morior Invictus before resistances"), L("Trocar Herald e Banner pelas reservas do endgame sem o Spirit do Morior", "Swapping Herald and Banner for the endgame reservations without Morior's Spirit")],
  exit=[L("4º Trial (~75): Motoric Implants (+2 níveis nas skills de Dex)", "4th Trial (~75): Motoric Implants (+2 levels on Dex skills)"), L("Morior Invictus + Desolate Crossbow", "Morior Invictus + Desolate Crossbow")]),

 dict(id="endgame", name=L("Endgame (Early) 79+", "Endgame (Early) 79+"), lv=[79, 90], tag=L("A build do autor, completa", "The author's build, complete"),
  carry=L("Você: Whirling Slash → Glacial Bolt", "You: Whirling Slash → Glacial Bolt"), dmgSplit=[100, 0],
  goal=L("Sem respec, sem troca de skill: os Weapon Sets fecham 30 e 31 pontos e o que muda são as peças. Set 1: spear (Skysliver Runeforged) com Whirling Slash — você anda girando, Desacelera e Cega os inimigos e o giro quebra os Ice Crystals. Set 2: Desolate Crossbow com Glacial Bolt (duas paredes de Ice Crystals), Emergency Reload e Herald of Thunder. Morior Invictus dá Armour e vida por socket; Iron Reflexes converte Evasion em Armour; Scavenged Plating e Arctic Armour seguram o dano de perto. É o setup 'Endgame (Early)' do autor, sem os suportes de Lineage caros.",
         "No respec, no skill swap: the Weapon Sets close at 30 and 31 points and what changes are the pieces. Set 1: spear (Runeforged Skysliver) with Whirling Slash — you move while spinning, Slow and Blind enemies and the spin breaks the Ice Crystals. Set 2: Desolate Crossbow with Glacial Bolt (two walls of Ice Crystals), Emergency Reload and Herald of Thunder. Morior Invictus gives Armour and life per socket; Iron Reflexes converts Evasion to Armour; Scavenged Plating and Arctic Armour hold up close-range damage. It's the author's 'Endgame (Early)' setup, without the expensive Lineage supports."),
  rotation=[L("Whirling Slash para andar e quebrar cristais", "Whirling Slash to move and break crystals"), L("Weapon Set 2: Glacial Bolt cria as paredes de gelo", "Weapon Set 2: Glacial Bolt creates the ice walls"), L("Emergency Reload no pente vazio; Seismic Cry no boss", "Emergency Reload on an empty clip; Seismic Cry on the boss")],
  gems=[
   G("Whirling Slash", ["Knockback", "Rage III", "Rapid Attacks III", "Morrigan's Insight"], L("Movimento + quebra", "Movement + breaking"), L("Gira, Desacelera, Cega e Empurra; o Morrigan's Insight (Lineage) e o Biting Frost II quebram os cristais sozinhos. Uncut Skill Gem nível 1 (spear).", "Spins, Slows, Blinds and Knocks Back; Morrigan's Insight (Lineage) and Biting Frost II break the crystals by themselves. Level 1 Uncut Skill Gem (spear)."), "free", since=79),
   G("Glacial Bolt", ["Elemental Armament II", "Rapid Attacks III", "Pierce III", "Ahn's Citadel"], L("Dano principal", "Main damage"), L("Cria duas paredes de Ice Crystals no fim do voo: é o dano do endgame. Uncut Skill Gem nível 7.", "Creates two walls of Ice Crystals at the end of flight: it's the endgame damage. Level 7 Uncut Skill Gem."), "free", since=79),
   G("Emergency Reload", ["Cooldown Recovery II", "Prolonged Duration II"], L("Recarga", "Reload"), L("Com o Uhtred's Rite (Lineage) a recarga vira reforço.", "With Uhtred's Rite (Lineage) the reload becomes an empowerment."), "free"),
   G("Scavenged Plating", ["Prolonged Duration II"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Arctic Armour", ["Cold Mastery", "Slow Potency", "Rapid Casting II", "Freeze", "Cooldown Recovery II"], L("Defesa", "Defence"), L("Barreira de gelo que vira dano contra quem bate em você. Tier 4, 30 Spirit.", "An ice barrier that turns into damage against whoever hits you. Tier 4, 30 Spirit."), "core", 2, SP30),
   G("Verisium Manifestations", ["Biting Frost II", "Multishot II", "Rapid Attacks III", "Pierce III", "Minion Mastery"], L("Dano extra", "Extra damage"), L("Cada golpe gasta Runic Ward e invoca uma Manifestation que ataca sozinha. Tier 0, 30 Spirit.", "Every hit spends Runic Ward and summons a Manifestation that attacks on its own. Tier 0, 30 Spirit."), "core", 3, SP30),
   G("Pounce", ["Rapid Attacks III", "Cooldown Recovery II", "Biting Frost II", "Blind II"], L("Movimento", "Movement"), L("Vira lobisomem e salta; exige um Talisman no set. Uncut nível 3.", "Turns into a werewolf and leaps; needs a Talisman in the set. Level 3 Uncut."), "free"),
   G("Berserk", [], L("Rage", "Rage"), L("Reforça a Rage que a Whirling Slash gera; drena vida se você para de bater. Tier 14, 30 Spirit.", "Strengthens the Rage Whirling Slash generates; drains life if you stop attacking. Tier 14, 30 Spirit."), "core", 4, SP30, since=79),
   G("Seismic Cry", ["Echoing Cry", "Magnified Area II", "Raging Cry", "Enraged Warcry II"], L("Warcry", "Warcry"), L("Empurra e dá Heavy Stun; ajuda a manter o boss no lugar. Uncut nível 11.", "Knocks back and Heavy Stuns; helps keep the boss in place. Level 11 Uncut."), "free"),
   G("Virtuous Barrier", [], L("Defesa", "Defence"), L("Da ascendência (Essence of Virtue): barreira com Motes que se perdem quando você toma dano.", "From the ascendancy (Essence of Virtue): a barrier of Motes that are lost when you're hit."), "free"),
  ],
  cheap=["Skysliver", "Morior Invictus", "Lavianga's Spirits"],
  full=["Skysliver", "Morior Invictus", "Headhunter", "Lavianga's Spirits"],
  stats=[L("Armour e vida", "Armour and life"), L("Velocidade de ataque", "Attack speed"), L("Spirit", "Spirit")],
  tree=L("Sem respec: a árvore principal já está fechada em 85 pontos e os Weapon Sets completam 30 (spear: Unyielding, Roaring Cries, Stimulants, Bond of the Wolf, Versatile Arms) e 31 (besta: Overwhelm, Forces of Nature, Crystal Elixir, Crushing Verdict, Spray and Pray, Singular Purpose).", "No respec: the main tree is already closed at 85 points and the Weapon Sets complete 30 (spear: Unyielding, Roaring Cries, Stimulants, Bond of the Wolf, Versatile Arms) and 31 (crossbow: Overwhelm, Forces of Nature, Crystal Elixir, Crushing Verdict, Spray and Pray, Singular Purpose)."),
  avoid=[L("Ligar Berserk sem ter vida/regeneração", "Turning on Berserk without life/regeneration"), L("Se equipar a spear e o jogo disser que precisa remover Pounce: arraste a spear para o slot de offhand", "If equipping the spear and the game says you need to remove Pounce: drag the spear into the offhand slot")],
  exit=[L("Trinity no amuleto (100 Spirit) e Blasphemy + Temporal Chains", "Trinity on the amulet (100 Spirit) and Blasphemy + Temporal Chains"), L("Mageblood, Rite of Passage e os suportes de Lineage", "Mageblood, Rite of Passage and the Lineage supports")]),

 dict(id="max", name=L("Endgame final", "Final endgame"), lv=[91, 100], tag=L("Blasphemy, Trinity e Lineage", "Blasphemy, Trinity and Lineage"),
  carry=L("Você: Whirling Slash → Glacial Bolt", "You: Whirling Slash → Glacial Bolt"), dmgSplit=[100, 0],
  goal=L("O PoB de endgame do autor (nível 97): amuleto Viper Heart com a skill Trinity (100 Spirit), Blasphemy + Temporal Chains (curse em toda a tela), Mageblood e o Rite of Passage. Como a Whirling Slash gera Rage, você não precisa do Eternal Rage e coloca o Spirit em skills de reserva melhores. Os suportes de Lineage (Ahn's Citadel, Kaom's Madness, Rakiata's Flow, Vorana's Siege) são luxo: coloque-os conforme entrar dinheiro. O autor diz que o Gem Studded precisa ser balanceado à mão conferindo o custo de mana.",
         "The author's endgame PoB (level 97): Viper Heart amulet with the Trinity skill (100 Spirit), Blasphemy + Temporal Chains (a curse across the whole screen), Mageblood and Rite of Passage. Since Whirling Slash generates Rage, you don't need Eternal Rage and put Spirit into better reservation skills. The Lineage supports (Ahn's Citadel, Kaom's Madness, Rakiata's Flow, Vorana's Siege) are luxury: add them as money comes in. The author says Gem Studded has to be balanced by hand by checking mana costs."),
  rotation=[L("Igual ao Endgame (Early)", "Same as Endgame (Early)")],
  gems=[
   G("Whirling Slash", ["Knockback", "Morrigan's Insight", "Rigwald's Ferocity", "Rage III", "Rapid Attacks III"], L("Movimento + quebra", "Movement + breaking"), L("Com Lineage: Morrigan's Insight e Rigwald's Ferocity.", "With Lineage: Morrigan's Insight and Rigwald's Ferocity."), "free"),
   G("Glacial Bolt", ["Ahn's Citadel", "Kaom's Madness", "Rakiata's Flow", "Elemental Armament II", "Vorana's Siege"], L("Dano principal", "Main damage"), L("Nível 20 (23% de qualidade no PoB).", "Level 20 (23% quality in the PoB)."), "free"),
   G("Blasphemy", ["Temporal Chains", "Magnified Area II", "Ritualistic Curse", "Vitality II", "Dialla's Desire"], L("Curse em área", "Area curse"), L("Vira Temporal Chains numa aura: toda a tela fica lenta. Reserva Spirit: só cabe com o amuleto de Spirit alto.", "Turns Temporal Chains into an aura: the whole screen is slowed. It reserves Spirit: only fits with the high-Spirit amulet."), "core", 1, L("Reserva Spirit", "Reserves Spirit")),
   G("Trinity", ["Cold Mastery", "Uhtred's Augury", "Armour Demolisher I"], L("Elementos", "Elements"), L("Vem do amuleto (nível 20): dá Afinidade de Fogo, Gelo e Raio e mais dano elemental. 100 Spirit.", "Comes from the amulet (level 20): builds Fire, Cold and Lightning Affinity and more elemental damage. 100 Spirit."), "core", 2, L("100 Spirit", "100 Spirit")),
  ],
  cheap=[L("Igual ao Endgame (Early)", "Same as Endgame (Early)")], full=["Mageblood", "Rite of Passage"],
  stats=[L("Dano", "Damage")], tree=L("A árvore final do autor: 92 pontos + 30 + 31 nos Weapon Sets, com os notables 'From Nothing' (Blood Magic): confira o PoB.", "The author's final tree: 92 points + 30 + 31 on the Weapon Sets, with the 'From Nothing' notables (Blood Magic): check the PoB."),
  avoid=[L("Gastar Divines antes de fechar resistência e Spirit", "Spending Divines before resistances and Spirit are closed")], exit=[]),
]
PH = {p["id"]: p for p in PHASES}
BOX = {
 "a1": ("2", ["Whirling Slash", "Permafrost"], L("Set 1 gira com a spear, Set 2 congela com a besta: dois botões, dois Weapon Sets desde o nível 1.", "Set 1 spins with the spear, Set 2 freezes with the crossbow: two buttons, two Weapon Sets from level 1.")),
 "a2": ("2", ["Whirling Slash", "Glacial Bolt"], L("Do nível 24 o Glacial Bolt planta o gelo e a Whirling Slash o quebra: o ciclo final já está de pé.", "From level 24 Glacial Bolt plants the ice and Whirling Slash breaks it: the final loop is already up.")),
 "a3": ("2", ["Whirling Slash", "Glacial Bolt"], L("O Emergency Reload recarrega o pente sem parar de atirar.", "Emergency Reload reloads the clip without stopping.")),
 "a4": ("2", ["Whirling Slash", "Glacial Bolt"], L("Três reservas de Spirit (Herald, Banner, Plating) somam 90 dos 100.", "Three Spirit reservations (Herald, Banner, Plating) use 90 of the 100.")),
 "maps": ("2", ["Whirling Slash", "Glacial Bolt"], L("Sem pressa para trocar as reservas: só com o Spirit do Morior Invictus.", "No rush to swap the reservations: only with Morior Invictus' Spirit.")),
 "endgame": ("2", ["Whirling Slash", "Glacial Bolt"], L("A spear gira e quebra o gelo que a besta planta: a mesma build de sempre, completa.", "The spear spins and breaks the ice the crossbow plants: the same build as always, complete.")),
 "max": ("2", ["Whirling Slash", "Glacial Bolt"], L("Igual, com suportes de Lineage e Blasphemy.", "Same, with Lineage supports and Blasphemy.")),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in {"a1": L("Nenhuma reserva ainda: o Herald de Gelo espera o King in the Mists (+30 Spirit, ~10).", "No reservation yet: Ice Herald waits for King in the Mists (+30 Spirit, ~10)."),
                  "a2": L("Herald (30) de 30 Spirit: sobra o que vier do Ignagduk.", "Herald (30) of 30 Spirit: what's left comes from Ignagduk."),
                  "a3": L("Herald (30) + War Banner (30) = 60 Spirit (King in the Mists + Ignagduk).", "Herald (30) + War Banner (30) = 60 Spirit (King in the Mists + Ignagduk)."),
                  "a4": L("Herald + Banner + Plating = 90 dos 100 Spirit (com o Lythara).", "Herald + Banner + Plating = 90 of 100 Spirit (with Lythara)."),
                  "maps": L("90 de 100 Spirit. Com o Morior Invictus (+13 por socket cheio) você troca Herald e Banner pelas reservas do endgame.", "90 of 100 Spirit. With Morior Invictus (+13 per filled socket) you swap Herald and Banner for the endgame reservations."),
                  "endgame": L("Plating 30 + Arctic Armour 30 + Verisium 30 + Berserk 30 = 120: o Morior Invictus dá +13 Spirit por socket cheio.", "Plating 30 + Arctic Armour 30 + Verisium 30 + Berserk 30 = 120: Morior Invictus gives +13 Spirit per filled socket."),
                  "max": L("Trinity reserva 100 de Spirit e o Blasphemy também reserva: só com amuleto de Spirit alto (por isso a variante Early corta os dois).", "Trinity reserves 100 Spirit and Blasphemy reserves too: only with a high-Spirit amulet (that's why the Early variant cuts both).")}.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Whirling Slash, Permafrost Bolts e Fragmentation Rounds (Uncut nível 1). Spear branca no Set 1; Rampart Raptor com Lesser Glacial Rune no Set 2.", "Whirling Slash, Permafrost Bolts and Fragmentation Rounds (level 1 Uncut). White spear in Set 1; Rampart Raptor with a Lesser Glacial Rune in Set 2."),
 4: L("Rampart Raptor (a Tense Crossbow exige nível 4). Frozen Spite e Elemental Armament II nos suportes.", "Rampart Raptor (the Tense Crossbow needs level 4). Frozen Spite and Elemental Armament II on the supports."),
 10: L("King in the Mists: +30 Spirit.", "King in the Mists: +30 Spirit."),
 11: L("Wanderlust (botas, 20% de movimento).", "Wanderlust (boots, 20% movement)."),
 12: L("Herald of Ice (Uncut nível 4, 30 Spirit) e Rapid Attacks II.", "Herald of Ice (level 4 Uncut, 30 Spirit) and Rapid Attacks II."),
 16: L("Skysliver (Winged Spear) no Set 1. Close Combat II. Whirling Slash com Biting Frost II e Knockback.", "Skysliver (Winged Spear) in Set 1. Close Combat II. Whirling Slash with Biting Frost II and Knockback."),
 24: L("Glacial Bolt (Uncut nível 7) vira a skill principal do Set 2; a Fragmentation Rounds sai.", "Glacial Bolt (level 7 Uncut) becomes the main Set 2 skill; Fragmentation Rounds leaves."),
 27: L("Thrillsteel (capacete).", "Thrillsteel (helmet)."),
 28: L("1º Trial: Essence of Virtue.", "1st Trial: Essence of Virtue."),
 30: L("Greater Glacial Rune na Rampart Raptor; anéis rares (~30 e ~50).", "Greater Glacial Rune on the Rampart Raptor; rare rings (~30 and ~50)."),
 32: L("O Glacial Bolt tem os três suportes: a Permafrost Bolts sai da barra.", "Glacial Bolt has all three supports: Permafrost Bolts leaves the bar."),
 38: L("Rampart Raptor Runeforged (e Wanderlust forjada); Ignagduk: +30 Spirit → War Banner. Rage III na Whirling Slash.", "Runeforged Rampart Raptor (and forged Wanderlust); Ignagduk: +30 Spirit → War Banner. Rage III on Whirling Slash."),
 40: L("2º Trial: Gem Studded. Emergency Reload (Uncut nível 11). Skysliver e Thrillsteel Runeforged/Runemastered.", "2nd Trial: Gem Studded. Emergency Reload (level 11 Uncut). Runeforged Skysliver and Runemastered Thrillsteel."),
 50: L("Anéis rares melhores. Árvore: Dance with Death.", "Better rare rings. Tree: Dance with Death."),
 55: L("Rampart Raptor Runemastered (~2 Divines, opcional).", "Runemastered Rampart Raptor (~2 Divines, optional)."),
 62: L("Lythara: +40 Spirit → Scavenged Plating.", "Lythara: +40 Spirit → Scavenged Plating."),
 65: L("3º Trial: Advanced Thaumaturgy. Morior Invictus fica disponível. Árvore principal fecha em 85 pontos.", "3rd Trial: Advanced Thaumaturgy. Morior Invictus becomes available. The main tree closes at 85 points."),
 75: L("4º Trial: Motoric Implants (+2 níveis nas skills de Dex).", "4th Trial: Motoric Implants (+2 levels on Dex skills)."),
 79: L("Endgame (Early): sem troca. Desolate Crossbow, Morior Invictus e as reservas do autor (Arctic Armour, Verisium, Berserk).", "Endgame (Early): no swap. Desolate Crossbow, Morior Invictus and the author's reservations (Arctic Armour, Verisium, Berserk)."),
 90: L("Amuleto com Spirit alto (Trinity) e suportes de Lineage.", "High-Spirit amulet (Trinity) and Lineage supports."),
}

ASCENDANCY = [
 dict(order=1, key="eov", node="Essence of Virtue", when=L("1º Trial (~nível 28)", "1st Trial (~level 28)"), text=L("Concede a skill Virtuous Barrier: uma barreira que junta Motes protetores de cada atributo, mas perde um Mote quando você é atingido.", "Grants the Virtuous Barrier skill: a barrier that gathers protective Motes of each attribute but loses one when you're hit."), why=L("É a defesa da build desde cedo e fornece os Motes usados no balanço do Gem Studded.", "It's the build's defence from early on and provides the Motes used to balance Gem Studded.")),
 dict(order=2, key="gs", node="Gem Studded", when=L("2º Trial (~nível 40)", "2nd Trial (~level 40)"), text=L("Para cada cor de suporte mais numerosa: Vermelho = hits contra você sem Critical Damage Bonus; Azul = skills custam 30% menos; Verde = 40% menos penalidade de movimento ao usar skills.", "For each most-numerous support colour: Red = hits against you have no Critical Damage Bonus; Blue = skills cost 30% less; Green = 40% less movement penalty while using skills."), why=L("A Whirling Slash e o Glacial Bolt usam muitos suportes de Dex (verde): andar atirando fica bem mais rápido. Conte as cores.", "Whirling Slash and Glacial Bolt use many Dex (green) supports: moving while shooting gets much faster. Count the colours.")),
 dict(order=3, key="at", node="Advanced Thaumaturgy", when=L("3º Trial (~nível 65)", "3rd Trial (~level 65)"), text=L("A qualidade das gems dá às skills equipadas um efeito adicional.", "Gem quality grants socketed skills an additional effect."), why=L("Suba a qualidade das skills principais (o PoB usa 20–23%).", "Raise the quality of your main skills (the PoB uses 20–23%).")),
 dict(order=4, key="mi", node="Motoric Implants", when=L("4º Trial (~nível 75)", "4th Trial (~level 75)"), text=L("+2 níveis em todas as skills que exigem Dexterity.", "+2 levels on all skills with a Dexterity requirement."), why=L("Permafrost, Fragmentation, Glacial Bolt e Whirling Slash exigem Dex: é o maior salto de dano da ascendência (3 pontos: Implanted Gems e o nó do meio).", "Permafrost, Fragmentation, Glacial Bolt and Whirling Slash require Dex: it's the ascendancy's biggest damage jump (3 points: Implanted Gems and the middle node).")),
]
ASC_UNLOCK = [28, 40, 65, 75]
PHASE_START = {}
ASC_PHASE = {"a1": [], "a2": ["Essence of Virtue"], "a3": ["Essence of Virtue", "Gem Studded"], "a4": ["Essence of Virtue", "Gem Studded"],
             "maps": ["Essence of Virtue", "Gem Studded", "Advanced Thaumaturgy"]}


KEY_PASSIVES = [
 dict(node="Battle-hardened", type="Notable", text=L("Hits contra você têm 20% menos Critical Damage Bonus, +20% Armour e Evasion, +5 Força e Destreza.", "Hits against you have 20% reduced Critical Damage Bonus, +20% Armour and Evasion, +5 Strength and Dexterity."), when=L("Ato 1 → sempre", "Act 1 → forever"), why=L("Defesa e atributos logo no começo do mapa final.", "Defence and attributes right at the start of the final map.")),
 dict(node="Hard to Kill", type="Notable", text=L("+40% de recuperação de vida por flask e regenera 0,75% da vida máxima por segundo.", "+40% Flask Life Recovery rate and regenerate 0.75% of maximum life per second."), when=L("Ato 1 → sempre", "Act 1 → forever"), why=L("Regeneração para andar girando sem parar.", "Regeneration for spinning nonstop.")),
 dict(node="Sand in the Eyes", type="Notable", text=L("+10% de velocidade de ataque e 15% de chance de Cegar com ataques.", "+10% attack speed and 15% chance to Blind with attacks."), when=L("Ato 2 → sempre", "Act 2 → forever"), why=L("Velocidade para os dois sets e Cegueira combinando com a Whirling Slash.", "Speed for both sets and Blind that pairs with Whirling Slash.")),
 dict(node="Adrenaline Rush", type="Notable", text=L("+4% de movimento e +8% de velocidade de ataque se você matou há pouco.", "+4% movement speed and +8% attack speed if you killed recently."), when=L("Ato 2 → sempre", "Act 2 → forever"), why=L("Cada pack que morre acelera o próximo.", "Every pack that dies speeds up the next one.")),
 dict(node="Dance with Death", type="Notable", text=L("+25% de velocidade de skill com uma arma marcial de uma mão na mão principal e a off hand vazia.", "+25% skill speed with a one-handed martial weapon in the main hand and an empty off hand."), when=L("Ato 3 → sempre", "Act 3 → forever"), why=L("A spear do Set 1 é exatamente essa arma: a Whirling Slash fica muito mais rápida.", "The Set 1 spear is exactly that weapon: Whirling Slash gets much faster.")),
 dict(node="Acceleration", type="Notable", text=L("+3% de movimento e +10% de velocidade de skill.", "+3% movement speed and +10% skill speed."), when=L("Ato 3 → sempre", "Act 3 → forever"), why=L("Movimento e ritmo para o Glacial Bolt e a Whirling Slash.", "Movement and rhythm for Glacial Bolt and Whirling Slash.")),
 dict(node="Battle Trance", type="Notable", text=L("+8 de Rage máxima.", "+8 maximum Rage."), when=L("Ato 4 → sempre", "Act 4 → forever"), why=L("A Whirling Slash gera Rage: mais teto de Rage, mais dano.", "Whirling Slash generates Rage: a higher Rage cap, more damage.")),
 dict(node="Iron Reflexes", type="Keystone", text=L("Converte toda a Evasion em Armour.", "Converts all Evasion Rating to Armour."), when=L("Mapas → sempre", "Maps → forever"), why=L("O Morior Invictus e as peças de Armour transformam isso em 100 mil de Armour no PoB.", "Morior Invictus and the Armour pieces turn this into 100k Armour in the PoB.")),
]
TREE_STAGES = [
 dict(lv="1–15", focus=L("Vida, defesa e atributos", "Life, defence and attributes"), dmg="Whirling Slash + Permafrost", **{"def": L("Vida e Armour", "Life and Armour")}, spirit="—", dont=L("Sair do caminho do mapa final", "Leaving the final map's path")),
 dict(lv="16–45", focus=L("Velocidade de ataque, área e Dance with Death", "Attack speed, area and Dance with Death"), dmg="Whirling Slash + Glacial Bolt", **{"def": L("Vida e resistências", "Life and resistances")}, spirit="Herald · Banner", dont=L("Pegar nó fora do mapa final", "Taking nodes off the final map")),
 dict(lv="46–78", focus=L("Rage, área e Iron Reflexes", "Rage, area and Iron Reflexes"), dmg="Whirling Slash + Glacial Bolt", **{"def": L("Armour (Plating, Iron Reflexes)", "Armour (Plating, Iron Reflexes)")}, spirit="Herald · Banner · Plating", dont=L("Deixar os Weapon Sets para depois", "Leaving Weapon Sets for later")),
 dict(lv="79–100", focus=L("Weapon Sets completos (30 + 31)", "Complete Weapon Sets (30 + 31)"), dmg="Whirling Slash + Glacial Bolt", **{"def": L("Iron Reflexes + Armour", "Iron Reflexes + Armour")}, spirit="Plating · Arctic · Verisium · Berserk", dont=L("Perder o requisito de Dex", "Losing the Dex requirement")),
]

UNIQUES = [
 U("Rampart Raptor", L("Besta", "Crossbow"), L("Arma", "Weapon"), "a1", L("+40–60% de dano físico, +30–40% de velocidade de ataque, −30% de recarga e 100% de chance de não gastar munição se você recarregou há pouco.", "+40–60% physical damage, +30–40% attack speed, −30% reload and a 100% chance not to expend ammo if you've reloaded recently."), L("Do nível 4 ao 78 é a sua besta (Set 2): Tense Crossbow, nível 4 (~0,005 Divine); Runeforged no 38 (~0,01), Runemastered no 55 (~2 Divines).", "From level 4 to 78 it's your crossbow (Set 2): Tense Crossbow, level 4 (~0.005 Divine); Runeforged at 38 (~0.01), Runemastered at 55 (~2 Divines)."), L("Besta rare com dano elemental e velocidade.", "A rare crossbow with elemental damage and speed."), 1),
 U("Tabula Rasa", "Body Armour", L("Armadura", "Armour"), "a1", L("Corpo com muitos sockets e sem defesa própria: você enche de runas de dano.", "A body with many sockets and no defences of its own: you fill it with damage runes."), L("Custa ~0,5 Divine. Qualquer mistura de runas de projétil, ataque, elemental e besta (autor).", "Costs ~0.5 Divine. Any mix of projectile, attack, elemental and crossbow runes (author)."), L("Body normal com vida e resistências.", "A normal body with life and resistances."), 1),
 U("Blackheart", "Ring", L("Acessório", "Accessory"), "a1", L("Regeneração de vida, dano adicionado a ataques e dano também aplicado como caos.", "Life regeneration, added attack damage and damage also applied as chaos."), L("Dois anéis por ~0,01 Divine. Troque por rares com dano adicionado e resistência no ~30 e no ~50.", "Two rings for ~0.01 Divine. Swap them for rares with added damage and resistance at ~30 and ~50."), L("Anel rare de dano e resistência.", "A rare ring with damage and resistance."), 1),
 U("Meginord's Girdle", L("Cinto", "Belt"), L("Acessório", "Accessory"), "a1", L("+40–50 de Força, +10–15% de resistência a frio e muito mais cargas de flask.", "+40–50 Strength, +10–15% cold resistance and far more flask charges."), L("Nível 0, quase de graça.", "Level 0, nearly free."), L("Cinto com vida e resistências.", "A belt with life and resistances."), 1),
 U("Wanderlust", L("Botas", "Boots"), L("Armadura", "Armour"), "a1", L("+20% de velocidade de movimento, ES e imunidade à lentidão.", "+20% movement speed, ES and immunity to Slow."), L("Nível 11 (Wrapped Sandals); a versão Runemastered pede nível 38.", "Level 11 (Wrapped Sandals); the Runemastered version needs level 38."), L("Botas com movimento.", "Boots with movement."), 11),
 U("Skysliver", "Spear", L("Arma", "Weapon"), "a2", L("Adiciona dano de raio, velocidade de ataque e chance de crítico; só rola o mínimo ou o máximo de dano.", "Adds lightning damage, attack speed and crit chance; rolls only the minimum or maximum damage."), L("Sua spear do Set 1 (Whirling Slash) do nível 16 ao 100: Winged Spear nível 16 (~0,1 Divine), Runeforged no 40 com Soul Core of Speed. Até o 16, uma spear branca do vendor. Se o jogo disser que precisa remover Pounce, arraste a spear para o slot de offhand.", "Your Set 1 spear (Whirling Slash) from level 16 to 100: level 16 Winged Spear (~0.1 Divine), Runeforged at 40 with a Soul Core of Speed. Until 16, a white vendor spear. If the game says you must remove Pounce, drag the spear to the offhand slot."), L("Spear rare com velocidade.", "A rare spear with speed."), 16),
 U("Thrillsteel", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a2", L("Capacete de Força e vida para a fase de leveling.", "A Strength helmet with life for the leveling phase."), L("Nível 27 (Spired Greathelm, ~0,03 Divine); Runemastered no 40.", "Level 27 (Spired Greathelm, ~0.03 Divine); Runemastered at 40."), L("Capacete rare de vida.", "A rare life helmet."), 27),
 U("Morior Invictus", "Body Armour", L("Armadura", "Armour"), "maps", L("+300–400% de Armour, Evasion e ES e bônus por socket cheio: vida, mana, atributos, resistência a caos e Spirit.", "+300–400% Armour, Evasion and ES and bonuses per filled socket: life, mana, attributes, chaos resistance and Spirit."), L("Nível 65, ~6 Divines. É a peça que faz a Armour e o Spirit do endgame.", "Level 65, ~6 Divines. It's the piece that provides endgame Armour and Spirit."), L("Body de Armour com vida.", "An Armour body with life."), 65),
 U("Lavianga's Spirits", "Flask", "Flask", "endgame", L("O flask não pode ser usado: o efeito de mana fica sempre ativo (73% menos recuperado).", "The flask cannot be used: the mana effect is always active (73% less recovered)."), L("Mana constante sem apertar nada (~0,1 Divine, nível 49).", "Constant mana without pressing anything (~0.1 Divine, level 49)."), L("Flask de mana normal.", "A regular mana flask."), 49),
 U("Rite of Passage", "Charm", "Charm", "max", L("Ao matar um Rare ou Unique, você fica possuído por espíritos animais (o autor usa o Lobo: velocidade de ataque).", "On killing a Rare or Unique you're possessed by animal spirits (the author uses the Wolf: attack speed)."), L("Luxo (~15 Divines).", "Luxury (~15 Divines)."), L("Golden Charm normal.", "A regular Golden Charm."), 50),
 U("Headhunter", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Ao matar um Rare você ganha os modificadores dele por 60 s.", "On killing a Rare you gain its modifiers for 60 s."), L("Cinto da variante Early do autor (~246 Divines).", "Belt of the author's Early variant (~246 Divines)."), L("Cinto de vida e Armour.", "A life and Armour belt."), 50),
 U("Mageblood", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Efeitos de flask permanentes.", "Permanent flask effects."), L("O cinto do PoB final (~570 Divines): só no fim.", "The final PoB's belt (~570 Divines): only at the very end."), L("Cinto com vida.", "A belt with life."), 55),
]
GEAR = [
 dict(slot=L("Besta (Set 2)", "Crossbow (Set 2)"), cheap=L("Rampart Raptor (Tense → Runeforged 38 → Runemastered 55)", "Rampart Raptor (Tense → Runeforged 38 → Runemastered 55)"), value=L("Desolate Crossbow rare com + níveis de Attack e dano elemental (a partir do 79)", "Rare Desolate Crossbow with + Attack levels and elemental damage (from 79)"), full=L("Desolate Crossbow: +3 níveis de Attack, dano de fogo e raio adicionados", "Desolate Crossbow: +3 Attack levels, added fire and lightning damage"), affix=L("+ níveis de Attack; dano elemental adicionado; velocidade", "+ Attack levels; added elemental damage; speed"), note=L("Glacial Bolt (Set 2) do nível 24 ao 100", "Glacial Bolt (Set 2) from level 24 to 100")),
 dict(slot=L("Spear (Set 1)", "Spear (Set 1)"), cheap=L("Spear branca do vendor (1–15) → Skysliver (16)", "White vendor spear (1–15) → Skysliver (16)"), value=L("Skysliver Runeforged (40)", "Runeforged Skysliver (40)"), full=L("Rune Edge/Skysliver com Soul Cores de velocidade", "Rune Edge/Skysliver with speed Soul Cores"), affix=L("Velocidade de ataque; dano elemental", "Attack speed; elemental damage"), note=L("Whirling Slash do nível 1 ao 100", "Whirling Slash from level 1 to 100")),
 dict(slot=L("Capacete", "Helmet"), cheap="Thrillsteel", value=L("Base de Armour com vida e resistências", "Armour base with life and resistances"), full=L("Mind Salvation: Armour alta, resistência e Armour aplicada a elemental", "Mind Salvation: high Armour, resistance and Armour applied to elemental"), affix=L("Vida; Armour; resistência a frio", "Life; Armour; cold resistance"), note=""),
 dict(slot="Body Armour", cheap="Tabula Rasa", value="Morior Invictus", full="Morior Invictus", affix="—", note=L("Cinco sockets: runas de vida, Fox/Panther Idol e Tecrod's Gaze", "Five sockets: life runes, Fox/Panther Idol and Tecrod's Gaze")),
 dict(slot=L("Luvas", "Gloves"), cheap=L("Vida e resistências", "Life and resistances"), value=L("Armour com vida e dano de frio adicionado", "Armour with life and added cold damage"), full=L("Dire Caress: Armour, vida e resistência a caos", "Dire Caress: Armour, life and chaos resistance"), affix=L("Vida; Armour; resistência a caos", "Life; Armour; chaos resistance"), note=L("EVITE 'chance de projétil extra' nas luvas: o autor diz que está bugada", "AVOID 'chance for an extra projectile' on gloves: the author says it's bugged")),
 dict(slot=L("Botas", "Boots"), cheap="Wanderlust", value=L("35% de movimento + vida", "35% movement + life"), full=L("Armageddon Tread: 30% de movimento, vida, mana e 3 Perfect Body Runes", "Armageddon Tread: 30% movement, life, mana and 3 Perfect Body Runes"), affix=L("Movimento; vida; resistências", "Movement; life; resistances"), note=""),
 dict(slot=L("Amuleto", "Amulet"), cheap=L("Vida e resistências", "Life and resistances"), value=L("Absent Amulet com Spirit", "Absent Amulet with Spirit"), full=L("Viper Heart: Trinity nível 20 e +3 de projétil", "Viper Heart: level 20 Trinity and +3 projectile"), affix=L("Spirit; + nível de projétil; Armour", "Spirit; + projectile level; Armour"), note=""),
 dict(slot=L("Anéis", "Rings"), cheap="Blackheart", value=L("Rares com dano adicionado (~30 e ~50)", "Rares with added damage (~30 and ~50)"), full=L("Miracle Gyre + Morbid Knuckle: dano adicionado, vida e resistências", "Miracle Gyre + Morbid Knuckle: added damage, life and resistances"), affix=L("Dano adicionado; vida; resistência", "Added damage; life; resistance"), note=""),
 dict(slot=L("Cinto", "Belt"), cheap="Meginord's Girdle", value=L("Vida e resistências", "Life and resistances"), full="Mageblood", affix="—", note=""),
 dict(slot="Charms", cheap=L("Dousing + Silver", "Dousing + Silver"), value="Rite of Passage", full="Rite of Passage", affix=L("Cobrir Ignite e Slow", "Cover Ignite and Slow"), note=""),
 dict(slot="Flasks", cheap=L("Vida", "Life"), value="Lavianga's Spirits", full=L("Ultimate Life + Lavianga's Spirits", "Ultimate Life + Lavianga's Spirits"), affix=L("Recuperação", "Recovery"), note=""),
]
exec(open(os.path.join(HERE, "gear_opts.py"), encoding="utf-8").read())
for _g, _k in zip(GEAR, SLOT_OPTS):
    _g["opts"] = GEAR_OPTS[_k]
BUY_ORDER = [
 dict(p=1, item=L("Spear branca + Rampart Raptor + Lesser Glacial Rune", "White spear + Rampart Raptor + Lesser Glacial Rune"), phase=L("Nível 1–4", "Level 1–4"), cost=L("Barato", "Cheap"), impact=L("A build inteira: Whirling Slash e besta", "The whole build: Whirling Slash and crossbow")),
 dict(p=2, item="Tabula Rasa", phase=L("Ato 1", "Act 1"), cost=L("Barato", "Cheap"), impact=L("Sockets para runas de dano", "Sockets for damage runes")),
 dict(p=3, item="Skysliver (Winged Spear)", phase=L("Nível 16", "Level 16"), cost=L("Barato", "Cheap"), impact=L("Dano e velocidade para a Whirling Slash", "Damage and speed for Whirling Slash")),
 dict(p=4, item="Wanderlust + Thrillsteel", phase=L("Ato 2", "Act 2"), cost=L("Barato", "Cheap"), impact=L("Movimento e vida", "Movement and life")),
 dict(p=5, item=L("Rampart Raptor Runeforged + Skysliver Runeforged", "Runeforged Rampart Raptor + Runeforged Skysliver"), phase=L("Nível 38–40", "Level 38–40"), cost=L("Barato", "Cheap"), impact=L("Mais dano e slots de runa nos dois sets", "More damage and rune slots in both sets")),
 dict(p=6, item=L("Rampart Raptor Runemastered", "Runemastered Rampart Raptor"), phase=L("Nível 55", "Level 55"), cost=L("Valor", "Value"), impact=L("Teto de dano até a Desolate Crossbow", "Damage ceiling until the Desolate Crossbow")),
 dict(p=7, item="Morior Invictus", phase=L("Mapas", "Maps"), cost=L("Valor", "Value"), impact=L("Armour, vida e Spirit por socket", "Armour, life and Spirit per socket")),
 dict(p=8, item="Desolate Crossbow", phase="Endgame", cost=L("Valor", "Value"), impact=L("Dano do Glacial Bolt", "Glacial Bolt damage")),
 dict(p=9, item=L("Viper Heart (Trinity) + Lineage", "Viper Heart (Trinity) + Lineage"), phase="Pinnacle", cost=L("Luxo", "Luxury"), impact=L("Teto de dano", "Damage ceiling")),
]

TRICKS = [
 {"cat": L("Setup", "Setup"), "lvl": L("Fácil", "Easy"), "title": L("Spear no Set 1, besta no Set 2, desde o nível 1", "Spear in Set 1, crossbow in Set 2, from level 1"), "body": L("O Set 1 leva a spear (branca no começo, Skysliver do 16) e a Whirling Slash; o Set 2 leva a Rampart Raptor e a skill de besta. Você troca de set no botão de movimento e usa 'ataque básico (Set 1)' e '(Set 2)' em botões separados. É o mesmo setup do endgame: só as peças e as gems mudam.", "Set 1 holds the spear (white at first, Skysliver from 16) and Whirling Slash; Set 2 holds the Rampart Raptor and the crossbow skill. You swap sets on the movement button and use 'basic attack (Set 1)' and '(Set 2)' on separate buttons. It's the same setup as endgame: only the pieces and gems change.")},
 {"cat": L("Gelo", "Ice"), "lvl": L("Fácil", "Easy"), "title": L("Congele de longe, entre girando", "Freeze from range, spin in"), "body": L("Do 1 ao 24: Permafrost Bolts congela o pack, você troca de set e entra com a Whirling Slash; o Herald of Ice (12+) faz cada congelado que morre explodir. Nos bosses use a Fragmentation Rounds no congelado para estilhaçar.", "From 1 to 24: Permafrost Bolts freezes the pack, you swap sets and go in with Whirling Slash; Herald of Ice (12+) makes every frozen enemy that dies explode. On bosses use Fragmentation Rounds on the frozen target to shatter it.")},
 {"cat": L("Gelo", "Ice"), "lvl": L("Médio", "Medium"), "title": L("Do 24: Glacial Bolt planta, Whirling Slash quebra", "From 24: Glacial Bolt plants, Whirling Slash breaks"), "body": L("O Glacial Bolt cria duas paredes de Ice Crystals no fim do voo; a Whirling Slash (melee) gira, quebra todos eles com Biting Frost II (depois Morrigan's Insight) e ainda te move. É o ciclo do endgame inteiro e você o tem a partir do Ato 2.", "Glacial Bolt creates two walls of Ice Crystals at the end of flight; Whirling Slash (melee) spins, breaks them all with Biting Frost II (later Morrigan's Insight) and also moves you. It's the whole endgame loop and you have it from Act 2.")},
 {"cat": L("Setup", "Setup"), "lvl": L("Fácil", "Easy"), "title": L("Rampart Raptor: recarga trocada por munição infinita", "Rampart Raptor: reload traded for infinite ammo"), "body": L("A unique tem −30% de recarga, mas 100% de chance de não gastar munição depois de recarregar. Por isso a velocidade de ataque e o Emergency Reload (40) suavizam tudo.", "The unique has −30% reload but a 100% chance not to expend ammo after reloading. That's why attack speed and Emergency Reload (40) smooth everything out.")},
 {"cat": L("Endgame", "Endgame"), "lvl": L("Médio", "Medium"), "title": L("Se o Glacial Bolt parece lento", "If Glacial Bolt feels sluggish"), "body": L("Suba a velocidade de ataque: 10% de ataque escala a recarga como 10% de recarga. No começo, recarga ajuda; com Dance with Death, Acceleration e Mageblood ela deixa de importar.", "Raise attack speed: 10% attack speed scales reload like 10% reload speed. Early on reload helps; with Dance with Death, Acceleration and Mageblood it stops mattering.")},
 {"cat": L("Itens", "Items"), "lvl": L("Fácil", "Easy"), "title": L("EVITE projétil extra nas luvas", "AVOID extra projectile on gloves"), "body": L("Segundo o autor, o mod 'chance de projétil extra' (Surpassing Chance) é bugado: o segundo projétil sai separado, não dispara cristais extras e atrasa. Evite a todo custo.", "According to the author, the 'chance for an extra projectile' mod (Surpassing Chance) is bugged: the second projectile comes out separately, doesn't fire extra crystals and adds a delay. Avoid at all costs.")},
 {"cat": L("Gems", "Gems"), "lvl": L("Difícil", "Hard"), "title": L("Balanceie o Gem Studded", "Balance Gem Studded"), "body": L("O Gem Studded (2º Trial, ~40) conta só os suportes do Weapon Set ativo. Confira o custo de mana das skills para saber qual cor manda. O autor usa Time of Need e Explosive Shot desligados só para somar Motes e slots de suporte.", "Gem Studded (2nd Trial, ~40) only counts the active Weapon Set's supports. Check your skills' mana costs to see which colour rules. The author uses Time of Need and Explosive Shot switched off just to add Motes and support slots.")},
 {"cat": L("Itens", "Items"), "lvl": L("Fácil", "Easy"), "title": L("Spear que não equipa", "Spear that won't equip"), "body": L("Se o jogo disser que você precisa remover o Pounce (endgame) ao trocar o Talisman pela spear, arraste a spear para o slot de offhand (escudo/sceptro) e não para o principal.", "If the game says you must remove Pounce (endgame) when swapping the Talisman for the spear, drag the spear into the offhand slot (shield/sceptre) instead of the main one.")},
 {"cat": L("Anoints", "Anoints"), "lvl": L("Médio", "Medium"), "title": L("Lista de anoints e Megalomaniac (autor)", "Anoint and Megalomaniac list (author)"), "body": L("Augmented Flesh > Paragon > Jack of All Trades / Harness the Elements / Stormbreaker / Wild Storm / Frantic Reach / Resolute Reach / Dizzying Sweep / Engineered Blaze / Endless Blizzard / Imbibed Power / Chakra of Thought.", "Augmented Flesh > Paragon > Jack of All Trades / Harness the Elements / Stormbreaker / Wild Storm / Frantic Reach / Resolute Reach / Dizzying Sweep / Engineered Blaze / Endless Blizzard / Imbibed Power / Chakra of Thought.")},
]
TROUBLESHOOT = [
 (L("A Whirling Slash não equipa", "Whirling Slash won't equip"), L("Ela exige spear no set. Ponha uma spear (branca serve) no Weapon Set 1. Se pedir para remover o Pounce, arraste a spear para o slot de offhand.", "It requires a spear in the set. Put a spear (a white one works) in Weapon Set 1. If it asks to remove Pounce, drag the spear to the offhand slot.")),
 (L("A Fragmentation não faz nada", "Fragmentation does nothing"), L("Ela precisa de um alvo Congelado ou de um Ice Crystal. Comece com a Permafrost até o inimigo congelar.", "It needs a Frozen target or an Ice Crystal. Start with Permafrost until the enemy freezes.")),
 (L("Os cristais do Glacial Bolt não quebram", "Glacial Bolt's crystals don't break"), L("A Whirling Slash quebra os Ice Crystals com Biting Frost II (ou Morrigan's Insight no endgame). Confira o suporte e gire em cima deles.", "Whirling Slash breaks Ice Crystals with Biting Frost II (or Morrigan's Insight in endgame). Check the support and spin over them.")),
 (L("Minha recarga está muito lenta", "My reload is too slow"), L("A Rampart Raptor tem −30% de recarga. Suba a velocidade de ataque (Sand in the Eyes, Adrenaline Rush, Acceleration) e use o Emergency Reload (40).", "The Rampart Raptor has −30% reload. Raise attack speed (Sand in the Eyes, Adrenaline Rush, Acceleration) and use Emergency Reload (40).")),
 (L("O Herald de Gelo não explode", "Ice Herald doesn't explode"), L("Ele só solta quando você mata (Shatter) um inimigo Congelado com um ataque. Confira o Freeze e se a explosão tem área suficiente.", "It only releases when you kill (Shatter) a Frozen enemy with an attack. Check Freeze and that the explosion has enough area.")),
 (L("Não fecho o Spirit", "Spirit doesn't add up"), L("Herald 30, War Banner 30 e Plating 30 = 90 de 100 (quests). No endgame: Plating, Arctic, Verisium e Berserk = 120; o Morior Invictus dá +13 Spirit por socket.", "Herald 30, War Banner 30 and Plating 30 = 90 of 100 (quests). In endgame: Plating, Arctic, Verisium and Berserk = 120; Morior Invictus gives +13 Spirit per socket.")),
 (L("Estou fraco para o meu nível", "I'm weak for my level"), L("Confira os anéis rares (~30 e ~50), a Rampart Raptor (Runeforged no 38), a Skysliver (16 e 40) e se os nós de velocidade da árvore estão pegos.", "Check the rare rings (~30 and ~50), the Rampart Raptor (Runeforged at 38), Skysliver (16 and 40) and whether the tree's speed nodes are taken.")),
]
ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Resistências no cap · Árvore em 85 pontos · Rampart Raptor Runemastered", "Resistances capped · Tree at 85 points · Runemastered Rampart Raptor"), gear="Rampart Raptor · Skysliver · Thrillsteel"),
 dict(stage="T1–T10", goal=L("Motoric Implants · Morior Invictus · Desolate Crossbow", "Motoric Implants · Morior Invictus · Desolate Crossbow"), gear=L("Spear + besta", "Spear + crossbow")),
 dict(stage="T11–T15", goal=L("Weapon Sets completos · Spirit fechado (Arctic, Verisium, Berserk)", "Complete Weapon Sets · Spirit closed (Arctic, Verisium, Berserk)"), gear="Morior Invictus"),
 dict(stage="Pinnacle", goal=L("Trinity + Blasphemy · Lineage", "Trinity + Blasphemy · Lineage"), gear="Mageblood · Rite of Passage"),
]
CRAFT = [
 L("Desolate Crossbow: base branca ilvl 82 → Transmutation + Augmentation até + níveis de Attack ou dano elemental adicionado → Regal → Exalted para completar. No PoB: +3 de Attack, fogo e raio adicionados. Só vale a partir do 79: até lá a besta é a Rampart Raptor.", "Desolate Crossbow: white ilvl 82 base → Transmutation + Augmentation until + Attack levels or added elemental damage → Regal → Exalted to fill. In the PoB: +3 Attack, added fire and lightning. Only worth it from 79: until then the crossbow is the Rampart Raptor."),
 L("Armadura (capacete, luvas, botas): vida, Armour e resistências primeiro; movimento nas botas.", "Armour (helmet, gloves, boots): life, Armour and resistances first; movement on the boots."),
 L("Runas: Glacial Rune na besta (Lesser no 1, Greater no 30), Soul Core of Speed na spear e runas de dano na Tabula Rasa.", "Runes: Glacial Rune on the crossbow (Lesser at 1, Greater at 30), Soul Core of Speed on the spear and damage runes on Tabula Rasa."),
]
CASES = [
 (L("Não tenho a Skysliver", "I don't have Skysliver"), L("Use uma spear branca do vendor no Set 1: a Whirling Slash funciona igual, só com menos dano. A Winged Spear nível 16 custa ~0,1 Divine.", "Use a white vendor spear in Set 1: Whirling Slash works the same, just with less damage. A level 16 Winged Spear costs ~0.1 Divine.")),
 (L("Ainda não caiu o Glacial Bolt", "Glacial Bolt hasn't dropped yet"), L("Continue com Permafrost + Fragmentation no Set 2 e a Whirling Slash no Set 1: é a mesma build, só sem as paredes de gelo.", "Keep Permafrost + Fragmentation in Set 2 and Whirling Slash in Set 1: it's the same build, just without the ice walls.")),
 (L("Não tenho Spirit para o Plating", "I don't have Spirit for Plating"), L("Faltou o Lythara (~62, +40 Spirit). Use só Herald e Banner até lá.", "You're missing Lythara (~62, +40 Spirit). Use only Herald and Banner until then.")),
]
SOURCES = [
 dict(name="Phylaris POE — WHIRLING Glacial Bolt Gemling [POE2 0.5] (Mobalytics)", use=L("Build base: variantes Leveling/Endgame (Early)/Endgame, gems, itens, notas e FAQ", "Base build: Leveling/Endgame (Early)/Endgame variants, gems, items, notes and FAQ"), url=GUIDE_URL),
 dict(name="PoB do autor (poe.ninja)", use=L("Endgame nível 97: árvore, gems, itens e jóias", "Level 97 endgame: tree, gems, items and jewels"), url=POB_URL),
 dict(name="Path of Building (PoE2) — Gems.lua", use=L("Descrições das gems, tiers e custos de Spirit", "Gem descriptions, tiers and Spirit costs"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name="poe.ninja — Economia (Forbidden Rites)", use=L("Preços e níveis dos uniques", "Prices and levels of the uniques"), url="https://poe.ninja/poe2/economy/forbiddenrites"),
]
FIXES = [
 L("Este plano é uma ADAPTAÇÃO, não a variante Leveling do autor. O guia dele tem UMA variante de leveling (87 pontos, sem ascendência) e duas de endgame; aqui a árvore Endgame (Early) dele é seguida desde o Ato 1 (ordem de alocação calculada pelo menor caminho a partir da Mercenary) para você não precisar de respec, e a Whirling Slash + Glacial Bolt entram assim que o jogo permite. O autor não valida essa progressão.", "This plan is an ADAPTATION, not the author's Leveling variant. His guide has ONE leveling variant (87 points, no ascendancy) and two endgame ones; here his Endgame (Early) tree is followed from Act 1 (allocation order computed as the shortest path from the Mercenary) so you never need a respec, and Whirling Slash + Glacial Bolt come in as soon as the game allows. The author doesn't validate this progression."),
 L("Os níveis em que gems, runas e itens aparecem seguem o Path of Building e o poe.ninja (Uncut Skill Gem = nível da gem, aproximado); o texto avisa quando é aproximado. Confira no jogo o que cai e o que está no vendor.", "The levels at which gems, runes and items appear follow Path of Building and poe.ninja (Uncut Skill Gem = gem tier, approximate); the text says when it's approximate. Check in game what drops and what's at the vendor."),
 L("Até o Glacial Bolt (~24) o dano vem da Permafrost/Fragmentation na besta; a Whirling Slash é o botão de mover e limpar de perto. Uma spear branca faz pouco dano físico: é por isso que a Skysliver entra no 16.", "Until Glacial Bolt (~24) the damage comes from Permafrost/Fragmentation on the crossbow; Whirling Slash is the move-and-clear-up-close button. A white spear does little physical damage: that's why Skysliver comes in at 16."),
 L("Os pontos de Weapon Set por fase (2/6/12/20 e depois 30/31) são uma estimativa de quando as quests e os níveis liberam pontos; a árvore principal (17/34/50/72/85) também. A ordem dos Trials e os níveis 28/40/65/75 são aproximados.", "Weapon Set points per phase (2/6/12/20 and then 30/31) are an estimate of when quests and levels give points; the main tree (17/34/50/72/85) too. Trial order and levels 28/40/65/75 are approximate."),
]
UI = dict(
 setNote=L("rares com + níveis de Attack, dano elemental e Spirit.", "rares with + Attack levels, elemental damage and Spirit."),
 carry=r"^(Permafrost Bolts|Glacial Bolt)$", box=L("SKILLS", "SKILLS"), spiritWhat=L("(buffs persistentes)", "(persistent buffs)"),
 mechBtn=L("Abrir Gelo & Ciclone", "Open Ice & Cyclone"), dmg2="Fragmentation", dmgBar=L("Dano da skill de besta (aprox.)", "Crossbow skill damage (approx.)"),
 dmgLegend=L("dano da Fragmentation (proporção aproximada)", "Fragmentation damage (approximate ratio)"),
 earlyGone=L("As skills iniciais já saíram da barra: você passou do nível {u}.", "Starting skills already left the bar: you're past level {u}."),
 earlyNote=L("Skills de começo; saem no nível ~{u}.", "Early skills; they leave around level {u}."),
 treeIntro=L("Árvore real do guia do Phylaris POE (variante Endgame (Early), 85 pontos + Weapon Sets), seguida desde o Ato 1: cada fase só acrescenta nós, sem respec. Ordem: vida e defesa, depois velocidade e área, depois Rage e Iron Reflexes; os Weapon Sets crescem 2 → 6 → 12 → 20 → 30/31.", "Real tree from Phylaris POE's guide (Endgame (Early) variant, 85 points + Weapon Sets), followed from Act 1: each phase only adds nodes, no respec. Order: life and defence, then speed and area, then Rage and Iron Reflexes; Weapon Sets grow 2 → 6 → 12 → 20 → 30/31."),
 set1=L("spear (Whirling Slash)", "spear (Whirling Slash)"), set2=L("besta (Glacial Bolt)", "crossbow (Glacial Bolt)"), asc="Gemling Legionnaire", cls="Mercenary",
 respecTip=L("Sem respec: compare com a fase anterior — nós sem contorno verde já eram seus. Weapon Set 1 = spear; Set 2 = besta.", "No respec: compare with the previous phase — nodes without a green outline were already yours. Weapon Set 1 = spear; Set 2 = crossbow."),
 routeIntro=L("Sete fases do nível 1 ao 100, sempre a mesma build: Whirling Slash na spear (Set 1) e a besta no Set 2 — Permafrost no começo, Glacial Bolt do nível 24. O que sobe são suportes, itens e a árvore do autor, sem respec.", "Seven phases from level 1 to 100, always the same build: Whirling Slash on the spear (Set 1) and the crossbow in Set 2 — Permafrost at the start, Glacial Bolt from level 24. What grows are supports, items and the author's tree, with no respec."),
 socketPrio=["Whirling Slash", "Glacial Bolt", "Permafrost Bolts", "Herald of Ice", "War Banner", "Scavenged Plating"],
 permIntro=L("Nada disso volta depois. Spirit paga Herald, Banner e Plating. Os pontos de Weapon Set alimentam o Set 1 (spear) e o Set 2 (besta) desde o Ato 2.", "None of this comes back later. Spirit pays for Herald, Banner and Plating. Weapon Set points fuel Set 1 (spear) and Set 2 (crossbow) from Act 2."),
 atlasCards=[[L("Mapas que atrapalham", "Maps that hurt"), L("Evite mapas com Freeze/Chill imunes ou less Recovery: a build vive de congelar.", "Avoid maps with Freeze/Chill immunity or less Recovery: the build lives on freezing.")],
             [L("Farm", "Farming"), L("Guarde bases de besta ilvl 82 para a Desolate Crossbow e procure Winged Spear para a Skysliver.", "Keep ilvl 82 crossbow bases for the Desolate Crossbow and look for a Winged Spear for Skysliver.")]],
 foot=L("Guia adaptado do build do Phylaris POE (Mobalytics), dados de jogo do Path of Building e preços do poe.ninja", "Guide adapted from Phylaris POE's build (Mobalytics), Path of Building game data and poe.ninja prices"),
)
CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens e Árvore se adaptam na hora ao seu Spirit e ao que você marcou. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items and Tree tabs adapt instantly to your Spirit and what you ticked. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit máximo", "Max Spirit"), L("ex.: 100", "e.g. 100")], ["life", L("Vida máxima", "Max life"), ""], ["armour", "Armour", ""]],
 tiles=[[L("Spirit reservado", "Spirit reserved"), "used"], [L("Spirit livre", "Spirit free"), "free"], ["Armour", "armour"]],
 halve="", halveLabel="", halveTip="",
 buffs=[dict(key="herald", name="Herald of Ice", cost=30), dict(key="banner", name="War Banner", cost=30), dict(key="plating", name="Scavenged Plating", cost=30), dict(key="arctic", name="Arctic Armour", cost=30),
        dict(key="verisium", name="Verisium Manifestations", cost=30), dict(key="berserk", name="Berserk", cost=30)],
 own=[
  ["gear", "Rampart Raptor", "Rampart Raptor"], ["gear", "Tabula Rasa", "Tabula Rasa"], ["gear", "Blackheart", "Blackheart"], ["gear", "Wanderlust", "Wanderlust"], ["gear", "Thrillsteel", "Thrillsteel"],
  ["gear", "Skysliver", "Skysliver"], ["gear", "Morior Invictus", "Morior Invictus"], ["gear", "Lavianga's Spirits", "Lavianga's Spirits"],
  ["gem", "herald", "Herald of Ice (30)"], ["gem", "banner", "War Banner (30)"], ["gem", "plating", "Scavenged Plating (30)"], ["gem", "arctic", "Arctic Armour (30)"], ["gem", "glacial", "Glacial Bolt"], ["gem", "whirl", "Whirling Slash"],
  ["tree", "sand", "Sand in the Eyes"], ["tree", "dance", "Dance with Death"], ["tree", "trance", "Battle Trance"], ["tree", "iron", "Iron Reflexes"],
  ["asc", "eov", "Essence of Virtue"], ["asc", "gs", "Gem Studded"], ["asc", "at", "Advanced Thaumaturgy"], ["asc", "mi", "Motoric Implants"],
 ],
 rules=[
  dict(when=dict(lvMin=4, notOwn=["Rampart Raptor"]), lvl="bad", t=L("Falta a Rampart Raptor", "Rampart Raptor missing"), d=L("Tense Crossbow, nível 4, ~0,005 Divine: é a sua besta (Set 2) do nível 4 ao 78.", "Tense Crossbow, level 4, ~0.005 Divine: it's your crossbow (Set 2) from level 4 to 78."), tab="gear"),
  dict(when=dict(lvMin=1, notOwn=["whirl"]), lvl="bad", t=L("Falta a Whirling Slash", "Whirling Slash missing"), d=L("Uncut Skill Gem nível 1 (spear): ela é a sua skill de movimento do 1 ao 100. Coloque uma spear no Set 1.", "Level 1 Uncut Skill Gem (spear): it's your movement skill from 1 to 100. Put a spear in Set 1."), tab="skills"),
  dict(when=dict(lvMin=5, notOwn=["Tabula Rasa"]), lvl="warn", t=L("Tabula Rasa", "Tabula Rasa"), d=L("~0,5 Divine: sockets para runas de dano.", "~0.5 Divine: sockets for damage runes."), tab="gear"),
  dict(when=dict(lvMin=11, notOwn=["Wanderlust"]), lvl="warn", t=L("Wanderlust", "Wanderlust"), d=L("Botas com 20% de movimento, nível 11.", "Boots with 20% movement, level 11."), tab="gear"),
  dict(when=dict(lvMin=14, notOwn=["herald"]), lvl="warn", t=L("Herald of Ice", "Herald of Ice"), d=L("Uncut nível 4 com os 30 Spirit do King in the Mists.", "Level 4 Uncut with the 30 Spirit from King in the Mists."), tab="skills"),
  dict(when=dict(lvMin=17, notOwn=["Skysliver"]), lvl="warn", t=L("Skysliver", "Skysliver"), d=L("Winged Spear nível 16, ~0,1 Divine: a spear do Set 1 (Whirling Slash).", "Level 16 Winged Spear, ~0.1 Divine: the Set 1 spear (Whirling Slash)."), tab="gear"),
  dict(when=dict(lvMin=26, notOwn=["glacial"]), lvl="warn", t=L("Glacial Bolt", "Glacial Bolt"), d=L("Uncut nível 7 (~24): as paredes de gelo que a Whirling Slash quebra.", "Level 7 Uncut (~24): the ice walls Whirling Slash breaks."), tab="skills"),
  dict(when=dict(lvMin=27, notOwn=["Thrillsteel"]), lvl="tip", t=L("Thrillsteel", "Thrillsteel"), d=L("Capacete de leveling, nível 27, quase de graça.", "Leveling helmet, level 27, nearly free."), tab="gear"),
  dict(when=dict(lvMin=40, notOwn=["banner"]), lvl="warn", t=L("War Banner", "War Banner"), d=L("Precisa dos +30 Spirit do Ignagduk (~38).", "Needs Ignagduk's +30 Spirit (~38)."), tab="skills"),
  dict(when=dict(lvMin=40, notOwn=["gs"]), lvl="warn", t=L("Gem Studded", "Gem Studded"), d=L("2º Trial: bônus pela cor de suporte mais comum.", "2nd Trial: bonus for the most common support colour."), tab="asc"),
  dict(when=dict(lvMin=64, notOwn=["plating"]), lvl="warn", t=L("Scavenged Plating", "Scavenged Plating"), d=L("Precisa dos +40 Spirit do Lythara (~62).", "Needs Lythara's +40 Spirit (~62)."), tab="skills"),
  dict(when=dict(lvMin=75, notOwn=["mi"]), lvl="bad", t=L("Motoric Implants", "Motoric Implants"), d=L("+2 níveis em todas as skills de Dex: o maior salto de dano.", "+2 levels on all Dex skills: the biggest damage jump."), tab="asc"),
  dict(when=dict(lvMin=70, notOwn=["Morior Invictus"]), lvl="tip", t=L("Morior Invictus", "Morior Invictus"), d=L("Armour, vida e Spirit por socket (~6 Divines, nível 65).", "Armour, life and Spirit per socket (~6 Divines, level 65)."), tab="gear"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["a3", "a4", "maps", "endgame", "max"], when=dict(notOwn=["glacial"]), gemsFrom="a1", note=L("Sem Glacial Bolt: mostrando Whirling Slash + Permafrost + Fragmentation.", "No Glacial Bolt: showing Whirling Slash + Permafrost + Fragmentation.")),
]
TREE_RULES = [
 dict(when=dict(lvMin=18, notOwn=["sand"]), t=L("Sand in the Eyes: +10% de velocidade de ataque e Cegueira.", "Sand in the Eyes: +10% attack speed and Blind."), node="Sand in the Eyes"),
 dict(when=dict(lvMin=35, notOwn=["dance"]), t=L("Dance with Death: +25% de velocidade de skill com a spear.", "Dance with Death: +25% skill speed with the spear."), node="Dance with Death"),
 dict(when=dict(lvMin=51, notOwn=["trance"]), t=L("Battle Trance: +8 de Rage máxima para a Whirling Slash.", "Battle Trance: +8 maximum Rage for Whirling Slash."), node="Battle Trance"),
 dict(when=dict(lvMin=65, notOwn=["iron"]), t=L("Iron Reflexes converte Evasion em Armour.", "Iron Reflexes converts Evasion to Armour."), node="Iron Reflexes"),
]
TIMING_KEY = {"Rampart Raptor": "Rampart Raptor", "Tabula Rasa": "Tabula Rasa", "Wanderlust": "Wanderlust", "Thrillsteel": "Thrillsteel", "Skysliver": "Skysliver", "Morior Invictus": "Morior Invictus",
              "Herald of Ice": "herald", "War Banner": "banner", "Scavenged Plating": "plating", "Arctic Armour": "arctic", "Glacial Bolt": "glacial", "Whirling Slash": "whirl", "Motoric Implants": "mi", "Gem Studded": "gs"}

T("item", "Rampart Raptor", 4, L("Tense Crossbow, nível 4; ~0,005 Divine", "Tense Crossbow, level 4; ~0.005 Divine"), L("Nível 4.", "Level 4."), L("Toda a sua ofensiva de besta do 1 ao 78.", "All your crossbow offence from 1 to 78."), "—", L("Sem ela o Ato 1 fica lento (do 1 ao 3 use a besta inicial).", "Without it Act 1 is slow (from 1 to 3 use the starting crossbow)."), [L("Runeforged no 38, Runemastered no 55.", "Runeforged at 38, Runemastered at 55.")])
T("item", "Wanderlust", 11, L("Wrapped Sandals nível 11; ~0,01 Divine", "Level 11 Wrapped Sandals; ~0.01 Divine"), L("Ato 1.", "Act 1."), L("20% de movimento e imunidade à lentidão.", "20% movement and Slow immunity."), L("Botas com movimento até lá.", "Boots with movement until then."), "—")
T("item", "Skysliver", 16, L("Winged Spear nível 16; ~0,1 Divine", "Level 16 Winged Spear; ~0.1 Divine"), L("Ato 2.", "Act 2."), L("Dano e velocidade para a Whirling Slash.", "Damage and speed for Whirling Slash."), L("Spear branca do vendor até lá.", "White vendor spear until then."), "—")
T("item", "Thrillsteel", 27, L("Spired Greathelm nível 27; ~0,03 Divine", "Level 27 Spired Greathelm; ~0.03 Divine"), L("Ato 2.", "Act 2."), L("Capacete de vida.", "A life helmet."), "—", "—")
T("item", "Morior Invictus", 65, L("Nível 65; ~6 Divines", "Level 65; ~6 Divines"), L("Mapas.", "Maps."), L("Armour, vida e Spirit por socket.", "Armour, life and Spirit per socket."), "—", "—")
T("skill", "Whirling Slash", 1, L("Uncut nível 1 (spear)", "Level 1 Uncut (spear)"), L("Nível 1.", "Level 1."), L("Movimento e quebra dos cristais.", "Movement and crystal breaking."), "—", "—")
T("skill", "Herald of Ice", 12, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Depois do King in the Mists.", "After King in the Mists."), L("Explosão de gelo ao matar congelados.", "Ice explosion on killing frozen enemies."), L("Não ligue sem 30 Spirit livres.", "Don't turn on without 30 free Spirit."), "—")
T("skill", "Glacial Bolt", 24, L("Uncut nível 7", "Level 7 Uncut"), L("Ato 2.", "Act 2."), L("Duas paredes de Ice Crystals: o dano principal do 24 ao 100.", "Two walls of Ice Crystals: your main damage from 24 to 100."), L("Permafrost + Fragmentation até lá.", "Permafrost + Fragmentation until then."), "—")
T("skill", "War Banner", 38, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Depois do Ignagduk.", "After Ignagduk."), L("Buff de dano e velocidade de ataque.", "Attack damage and speed buff."), "—", "—")
T("skill", "Scavenged Plating", 62, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Depois do Lythara.", "After Lythara."), L("Armour e Thorns ao quebrar Armour.", "Armour and Thorns on breaking Armour."), "—", "—")
T("asc", "Gem Studded", 40, L("2º Trial", "2nd Trial"), L("Ato 3.", "Act 3."), L("Bônus pela cor de suporte mais comum.", "Bonus for the most common support colour."), "—", "—")
T("asc", "Motoric Implants", 75, L("4º Trial", "4th Trial"), L("Mapas.", "Maps."), L("+2 níveis em skills de Dex.", "+2 levels on Dex skills."), "—", "—")

MECH = dict(
 title=L("Gelo & Ciclone", "Ice & Cyclone"),
 intro=L("A build inteira é uma ideia só: congelar e estilhaçar enquanto você gira. Ela é a mesma do nível 1 ao 100: a spear (Set 1) gira e quebra, a besta (Set 2) congela e planta o gelo.", "The whole build is one idea: freeze and shatter while you spin. It's the same from level 1 to 100: the spear (Set 1) spins and breaks, the crossbow (Set 2) freezes and plants the ice."),
 sections=[
  dict(type="cards", cards=[
   [L("1. Congelar", "1. Freeze"), L("Permafrost Bolts dispara balas de gelo que se fragmentam e Congelam quase tudo (nível 1). Do nível 24, o Glacial Bolt planta duas paredes de Ice Crystals. Sand in the Eyes, Authority e Acceleration na árvore aceleram tudo.", "Permafrost Bolts fires ice bolts that fragment and Freeze almost everything (level 1). From level 24, Glacial Bolt plants two walls of Ice Crystals. Sand in the Eyes, Authority and Acceleration on the tree speed it all up.")],
   [L("2. Estilhaçar", "2. Shatter"), L("Fragmentation Rounds acerta o Congelado, gasta o Freeze e explode em estilhaços; se acertar um Ice Crystal, ele explode. Herald of Ice (12+) solta uma explosão quando você mata um congelado.", "Fragmentation Rounds hits the Frozen enemy, spends the Freeze and explodes into shrapnel; if it hits an Ice Crystal, it explodes. Herald of Ice (12+) releases an explosion when you kill a frozen enemy.")],
   [L("3. Ciclone (Set 1, desde o 1)", "3. Cyclone (Set 1, from level 1)"), L("A Whirling Slash (melee) gira, Desacelera e Cega, gera Rage e, com Biting Frost II (depois Morrigan's Insight), quebra os cristais do Glacial Bolt. Você anda atacando, e as explosões saem sozinhas. Dance with Death dá +25% de velocidade de skill com a spear.", "Whirling Slash (melee) spins, Slows and Blinds, generates Rage and, with Biting Frost II (later Morrigan's Insight), breaks Glacial Bolt's crystals. You move while attacking and the explosions happen on their own. Dance with Death gives +25% skill speed with the spear.")],
   [L("4. Cores e Spirit", "4. Colours and Spirit"), L("Gem Studded (2º Trial) dá bônus pela cor de suporte mais comum: verde = menos penalidade de movimento, azul = skills 30% mais baratas, vermelho = hits sem dano crítico bônus contra você. Só conta o Weapon Set ativo. Spirit vem de quests: 30, +30 (Ignagduk), +40 (Lythara).", "Gem Studded (2nd Trial) gives a bonus for the most common support colour: green = less movement penalty, blue = skills 30% cheaper, red = hits without critical bonus against you. It only counts the active Weapon Set. Spirit comes from quests: 30, +30 (Ignagduk), +40 (Lythara).")],
  ]),
  dict(type="rotation", blocks=[
   [L("Nível 1–23", "Levels 1–23"), [L("Set 2: Permafrost Bolts congela o pack", "Set 2: Permafrost Bolts freezes the pack"), L("Set 1: Whirling Slash entra girando e mata os congelados", "Set 1: Whirling Slash spins in and kills the frozen"), L("Boss: Fragmentation Rounds no congelado", "Boss: Fragmentation Rounds on the frozen target")]],
   [L("Nível 24+", "Level 24+"), [L("Set 2: Glacial Bolt planta as paredes de gelo", "Set 2: Glacial Bolt plants the ice walls"), L("Set 1: Whirling Slash gira, quebra os cristais e move", "Set 1: Whirling Slash spins, breaks the crystals and moves"), L("Emergency Reload no pente vazio (40+); no endgame, Seismic Cry, Pounce e Berserk no boss", "Emergency Reload on an empty clip (40+); in endgame, Seismic Cry, Pounce and Berserk on the boss")]],
  ]),
  dict(type="table", h=L("Weapon sets por fase", "Weapon sets per phase"), cols=[L("Fase", "Phase"), "Weapon Set 1", "Weapon Set 2"], rows=[
   [L("1–15", "1–15"), L("Spear branca: Whirling Slash", "White spear: Whirling Slash"), L("Rampart Raptor: Permafrost Bolts, Fragmentation Rounds", "Rampart Raptor: Permafrost Bolts, Fragmentation Rounds")],
   [L("16–78", "16–78"), L("Skysliver: Whirling Slash", "Skysliver: Whirling Slash"), L("Rampart Raptor: Glacial Bolt (24+), Emergency Reload (40+)", "Rampart Raptor: Glacial Bolt (24+), Emergency Reload (40+)")],
   [L("79+", "79+"), L("Skysliver Runeforged: Whirling Slash, Seismic Cry", "Runeforged Skysliver: Whirling Slash, Seismic Cry"), L("Desolate Crossbow: Glacial Bolt, Emergency Reload", "Desolate Crossbow: Glacial Bolt, Emergency Reload")],
   [L("Sempre", "Always"), L("Buffs persistentes nos dois sets", "Persistent buffs on both sets"), L("Buffs persistentes nos dois sets", "Persistent buffs on both sets")],
  ]),
  dict(type="spirit", h=L("Spirit dos buffs", "Buff Spirit"), p=L("Marque o que você usa. Custos do Path of Building.", "Tick what you use. Costs from Path of Building."),
       note=L("Ordem: Herald → War Banner → Scavenged Plating → Arctic Armour → Verisium → Berserk. Se faltar, desligue o último.", "Order: Herald → War Banner → Scavenged Plating → Arctic Armour → Verisium → Berserk. If short, turn off the last one.")),
  dict(type="timeline", h=L("Peças-chave por nível", "Key pieces by level"), items=[
   dict(lv=1, t="Whirling Slash + Permafrost Bolts", d=L("Spear no Set 1, Rampart Raptor no Set 2: a build inteira desde o primeiro nível.", "Spear in Set 1, Rampart Raptor in Set 2: the whole build from the first level.")),
   dict(lv=12, t="Herald of Ice", d=L("Depois do King in the Mists (+30 Spirit).", "After King in the Mists (+30 Spirit).")),
   dict(lv=16, t="Skysliver", d=L("A spear boa para a Whirling Slash.", "The good spear for Whirling Slash.")),
   dict(lv=24, t="Glacial Bolt", d=L("O ciclo do endgame (planta + quebra) já existe.", "The endgame loop (plant + break) already exists.")),
   dict(lv=38, t=L("Rampart Raptor Runeforged + War Banner", "Runeforged Rampart Raptor + War Banner"), d=L("Ignagduk: +30 Spirit.", "Ignagduk: +30 Spirit.")),
   dict(lv=62, t="Scavenged Plating", d=L("Lythara: +40 Spirit.", "Lythara: +40 Spirit.")),
   dict(lv=75, t="Motoric Implants", d=L("+2 níveis em skills de Dex.", "+2 levels on Dex skills.")),
   dict(lv=79, t="Desolate Crossbow + Arctic/Verisium/Berserk", d=L("As peças do endgame do autor; a build já é ela.", "The author's endgame pieces; the build already is it.")),
  ]),
 ],
)

exec(open(os.path.join(HERE, "bcraft.py"), encoding="utf-8").read())


def build(QUESTS_PT):
    quests = []
    for q in QUESTS_PT:
        q = dict(q)
        if q["boss"] == "Mighty Silverfist":
            q["reward"] = "2 Weapon Set Passive Points"; q["prio"] = "Média"
        if q["boss"] == "Tribal Medicine":
            q["reward"] = L("ESCOLHA: +30% Armour, Evasion e Energy Shield (autor)", "CHOICE: +30% Armour, Evasion and Energy Shield (author)"); q["prio"] = "Alta"
        if q["boss"] == "Medallion":
            q["reward"] = L("+1 Charm Slot · ESCOLHA: 30% de cargas de charm (autor)", "+1 Charm Slot · CHOICE: 30% increased Charm Charges gained (author)")
        if q["boss"] == "Venom Draught":
            q["reward"] = L("ESCOLHA: 25% de Stun Threshold (autor)", "CHOICE: 25% increased Stun Threshold (author)")
        if q["boss"] == "Goddess of Justice":
            q["reward"] = L("ESCOLHA: 30% de recuperação de vida por flask (autor)", "CHOICE: 30% increased Life Recovery from Flasks (author)")
        if q["boss"] == "Tabana's Pillar":
            q["reward"] = L("ESCOLHA: 3% de velocidade de movimento (autor)", "CHOICE: 3% increased Movement Speed (author)"); q["prio"] = "Alta"
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="19/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=GUIDE_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=BOOK.TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None,
                ui=UI, char=CHAR, mech=MECH, adaptSwaps=ADAPT_SWAPS, treeRules=TREE_RULES, timingKey=TIMING_KEY, phaseAct=PHASE_ACT, treeOrder=ORDER + ["uber"], craftKit=CRAFT_KIT)
