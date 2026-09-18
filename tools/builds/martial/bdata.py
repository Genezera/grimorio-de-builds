# -*- coding: utf-8 -*-
"""Martial Artist: Oil Barrage + Cast on Critical + Lightning Warp (teleporte). Leveling, árvore e itens: planner do havoc616 (Maxroll: Campaign,
Maps, Endgame, Aspirational), convertido por kit/maxroll.py. Setup do teleporte: os 22 Martial Artists de Oil Barrage + Lightning Warp do poe.ninja
(Forbidden Rites, 17/09/2026). Textos de gems do Path of Building, bases do RePoE2 e preços do poe.ninja."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("martial")

PLANNER_URL = "https://maxroll.gg/poe2/planner/bl5b6d0w"
GUIDE_URL = "https://maxroll.gg/poe2/build-guides/oil-barrage-martial-artist-build-guide"
NINJA_URL = "https://poe.ninja/poe2/builds/forbiddenrites?class=Martial+Artist&skills=Oil+Barrage%2CLightning+Warp"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "17/09/2026"

CONFIG = dict(dir="martial", build="martial", store="martial1", emoji="⚡", pill="Monk · Martial Artist",
              fonts="family=Cinzel+Decorative:wght@700;900&family=Cinzel:wght@500;700&family=Oxanium:wght@500;600;700&family=Exo+2:ital,wght@0,400;0,500;0,600;1,400")
TXT = {
 "pt": dict(TITLE="Oil Barrage Teleporte", DESC="Guia interativo Martial Artist Oil Barrage + Cast on Critical + Lightning Warp (Monk) — PoE 2 Forbidden Rites",
            H1S="Storm Wave na campanha · Oil Barrage nos mapas · Lightning Warp teleportando de pack em pack", H1="O Dragão de Óleo",
            LEAD="Você vira wyvern, cospe óleo elétrico na tela inteira e cada crítico enche o Cast on Critical: o Lightning Warp te teleporta para dentro do próximo inimigo e explode tudo em volta. Diga seu nível e o que você tem."),
 "en": dict(TITLE="Oil Barrage Teleport", DESC="Interactive Martial Artist Oil Barrage + Cast on Critical + Lightning Warp (Monk) guide — PoE 2 Forbidden Rites",
            H1S="Storm Wave in the campaign · Oil Barrage in maps · Lightning Warp teleporting from pack to pack", H1="The Oil Dragon",
            LEAD="You turn into a wyvern, spit electrified oil across the whole screen, and every crit fills Cast on Critical: Lightning Warp teleports you inside the next enemy and blows up everything around it. Tell it your level and what you have."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["quando", "Quando usar", "When to use"], ["mech", "Teleporte & Cargas", "Teleport & Charges"],
        ["uniques", "Uniques", "Uniques"], ["arvore", "Árvore de Passivas", "Passive Tree"], ["rota", "Rota 1→100", "Route 1→100"], ["skills", "Skills & Supports", "Skills & Supports"],
        ["gear", "Itens", "Items"], ["asc", "Ascendência", "Ascendancy"], ["quests", "Quests", "Quests"], ["tricks", "Tricks Pro", "Pro Tricks"], ["atlas", "Atlas", "Atlas"],
        ["diag", "Diagnóstico", "Troubleshooting"], ["fontes", "Fontes", "Sources"]]

CLASS, ASC, START = "Monk", "Martial Artist", 44683
ORDER = ["a1", "a2", "a3", "a4", "swap", "maps", "endgame", "max"]
VMAP = {"a1": "A1", "a2": "A2", "a3": "A3", "a4": "A4", "swap": "Early Maps", "maps": "Late Maps", "endgame": "Endgame", "max": "Aspirational: Mapping"}
FULLMAP = {k: k for k in ORDER}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a4", "swap": "swap", "maps": "swap", "endgame": "maps", "max": "endgame"}
PHASE_ACT = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "swap": 6, "maps": 6, "endgame": 6, "max": 6}
ITEM_NOTE = {"Lunar Quarterstaff": L("Set 2 do planner (Whirling Assault/Tempest Bell): opcional aqui", "Planner's Set 2 (Whirling Assault/Tempest Bell): optional here")}
TALISMAN_RUNES = L("Farrul's Rune of the Hunt + Saqawal's Rune of the Sky (ou Greater Iron Rune)", "Farrul's Rune of the Hunt + Saqawal's Rune of the Sky (or Greater Iron Rune)")

def socket_hint(slot, name):
    if "Talisman" in name: return [TALISMAN_RUNES]
    if slot == "Luvas": return [L("Greater Iron Rune (e as runas tatuadas do Runic Meridians)", "Greater Iron Rune (plus the Runic Meridians tattoo runes)")]
    if slot == "Body Armour": return [L("Greater Iron Rune ×2 · Runic Meridians: Craiceann's Rune of Warding (tatuagem)", "Greater Iron Rune ×2 · Runic Meridians: Craiceann's Rune of Warding (tattoo)")]
    return None

SUPWHY = {
 # campanha
 "Concentrated Area": L("Área menor e mais dano: o Large Spike da Glacial Cascade mata o cristal do Frozen Locus de uma vez.", "Smaller area, more damage: Glacial Cascade's Large Spike kills the Frozen Locus crystal in one hit."),
 "Rage I": L("Rage ao acertar melee: mais dano de ataque.", "Rage on melee hit: more attack damage."), "Rage II": L("Mais Rage ao acertar.", "More Rage on hit."),
 "Ice Bite I": L("Congelar um inimigo infunde frio no seu dano por um tempo.", "Freezing an enemy infuses your damage with cold for a while."), "Ice Bite II": L("Infusão de frio mais forte ao congelar.", "Stronger cold infusion on freeze."),
 "Elemental Armament I": L("Mais dano elemental em ataques.", "More elemental damage for attacks."), "Elemental Armament II": L("Muito mais dano elemental em ataques.", "Much more elemental damage for attacks."),
 "Magnified Area I": L("Área maior.", "Larger area."), "Magnified Area II": L("Área maior.", "Larger area."),
 "Potent Exposure": L("Exposure do Frost Bomb mais forte: resistência do alvo cai mais.", "Stronger Frost Bomb Exposure: the target's resistance drops further."),
 "Deep Freeze": L("O Freeze dura mais: tempo de sobra para a Glacial Cascade consumir.", "Freeze lasts longer: plenty of time for Glacial Cascade to consume it."),
 "Innervate": L("Matar inimigo com Shock infunde raio no seu dano (o Storm Wave dá Shock fácil).", "Killing a Shocked enemy infuses lightning into your damage (Storm Wave shocks easily)."),
 "Branching Fissures I": L("O Storm Wave cria fissuras secundárias: clear bem mais largo.", "Storm Wave creates secondary fissures: much wider clear."),
 "Elemental Focus": L("Mais dano elemental, mas a skill não aplica ailments — por isso só no Glacial Cascade e no Herald of Ice (quem congela é o Wave of Frost).", "More elemental damage, but the skill can't apply ailments — so only on Glacial Cascade and Herald of Ice (Wave of Frost does the freezing)."),
 "Freezing Mark": L("Marca: mais fácil congelar; ao congelar, buff de dano extra de frio.", "Mark: easier to freeze; freezing grants an extra cold damage buff."),
 "Elemental Weakness": L("Curse: reduz as resistências elementais do alvo.", "Curse: lowers the target's elemental resistances."),
 "Cooldown Recovery II": L("Cooldown mais rápido: mais sinos do Hollow Focus, mais Pounce e Ghost Dance.", "Faster cooldown: more Hollow Focus bells, more Pounce and Ghost Dance."),
 # Oil Barrage
 "Salvo": L("Guarda selos com o tempo; ao atacar, os selos disparam projéteis extras em direções aleatórias. Presente nos 22 personagens do ladder.", "Stores seals over time; attacking breaks them for extra projectiles in random directions. On all 22 ladder characters."),
 "Nova Projectiles I": L("Projéteis em círculo: o óleo cobre a tela à sua volta. Use a I — a II impede de encaixar todas as gems (nota do havoc616).", "Projectiles in a circle: oil covers the screen around you. Use I — II stops you from socketing every gem (havoc616's note)."),
 "Ricochet II": L("Projéteis podem ricochetear no terreno (chain): mais alvos e mais críticos para o Cast on Critical.", "Projectiles can chain off terrain: more targets and more crits for Cast on Critical."),
 "Fork": L("Projéteis se dividem ao acertar: clear fora da tela.", "Projectiles fork on hit: off-screen clear."),
 "Pinpoint Critical": L("Crítico com mais frequência (menos dano por crítico). Troque por Elemental Armament II com 50%+ de crítico.", "Crits more often (less damage per crit). Swap to Elemental Armament II at 50%+ crit."),
 "Rakiata's Flow": L("Lineage: acertos tratam as resistências elementais do inimigo como invertidas (75% vira −75%). Use Oil Barrage nível 21 com 0% de qualidade e tire Elemental Weakness e o Oil Barrage do Spirit Vessel.", "Lineage: hits treat enemy elemental resistances as inverted (75% becomes −75%). Use a level 21, 0% quality Oil Barrage and remove Elemental Weakness and Spirit Vessel's Oil Barrage."),
 "Hit and Run": L("A skill só pode ser usada depois de andar um pouco, mas fica muito mais rápida — combina com o teleporte do Lightning Warp.", "The skill can only be used after moving a distance, but becomes much faster — pairs with Lightning Warp's teleport."),
 "Burgeon II": L("Mais dano quanto mais tempo você canaliza.", "More damage the longer you channel."),
 # teleporte
 "Lightning Warp": L("A spell disparada: teleporta para dentro de um inimigo abaixo do Cull e o explode em raio (ou marca o alvo para explodir quando entrar no Cull).", "The triggered spell: teleports inside an enemy under the Cull threshold and explodes it with lightning (or marks the target to explode once it enters Cull)."),
 "Boundless Energy II": L("O Cast on Critical gera energia muito mais rápido: teleporta com mais frequência.", "Cast on Critical generates Energy much faster: teleports more often."),
 "Energy Retention": L("Chance de devolver parte da energia a cada disparo: disparos em sequência.", "Chance to refund part of the Energy on each trigger: back-to-back triggers."),
 "Fluke": L("Dano do Lightning Warp aleatório para cima ou para baixo e recupera parte do custo de mana ao disparar.", "Randomly raises or lowers Lightning Warp's damage and recovers part of its mana cost when triggered."),
 "Soul Drain": L("Recupera mana quando dá Cull: cada teleporte que explode um inimigo paga o próximo.", "Recovers mana on Cull: every teleport that explodes an enemy pays for the next one."),
 "Profane Ritual": L("Segunda spell no Cast on Critical: marca um corpo e, ao completar, dá uma Power Charge — combustível extra para o Oil Barrage.", "Second spell in Cast on Critical: marks a corpse and grants a Power Charge on completion — extra fuel for Oil Barrage."),
 "Efficiency II": L("Custo menor: Lightning Warp e Refutation.", "Lower cost: Lightning Warp and Refutation."),
 # cargas
 "Heightened Charges": L("Chance de dobrar o benefício ao consumir cargas: o buff do Rend vale por dois.", "Chance to double the benefit when consuming charges: Rend's buff counts twice."),
 "Prolonged Duration II": L("Buffs mais longos (Rend, Devour, Refutation, sinos).", "Longer buffs (Rend, Devour, Refutation, bells)."),
 "Rage III": L("Rage ao acertar e muito mais velocidade de ataque enquanto não está no Rage máximo.", "Rage on hit and much more attack speed while not at max Rage."),
 "Perpetual Charge": L("Chance de não gastar a Power Charge ao consumir, ganhando o efeito mesmo assim.", "Chance not to spend the Power Charge when consuming, still gaining the effect."),
 "Rapid Attacks III": L("Ataques mais rápidos, com menos dano.", "Faster attacks, less damage."),
 "Blazing Critical": L("Críticos infundem fogo em todos os seus ataques por um tempo.", "Crits infuse fire into all your attacks for a while."),
 "Thrill of the Kill II": L("Dar Cull em inimigo com Shock infunde raio em todos os ataques e aumenta a chance de Shock.", "Culling a Shocked enemy infuses lightning into all attacks and raises Shock chance."),
 "Charge Profusion II": L("Chance de cargas extras (inclusive de tipo aleatório) quando o Devour gera Power Charge.", "Chance for extra charges (including a random type) when Devour grants Power Charges."),
 "Overabundance II": L("Mais sinos ao mesmo tempo.", "More bells at once."),
 "Living Lightning II": L("Dano de raio cria minions de Living Lightning que atacam em cadeia.", "Lightning damage creates Living Lightning minions that chain-attack."),
 "Culmination II": L("Ganha Combo com outros ataques e gasta tudo de uma vez: libera o Ailith's Chimes.", "Builds Combo from other attacks and spends it at once: enables Ailith's Chimes."),
 "Ailith's Chimes": L("Lineage: gastar Combo tem chance de dar Power Charges — carga constante em lutas paradas.", "Lineage: spending Combo can grant Power Charges — steady charges in stationary fights."),
 "Culling Strike II": L("Cull em rares e uniques e limite de Cull maior: o Lightning Warp explode alvos mais cedo.", "Culls rares and uniques with a higher threshold: Lightning Warp explodes targets sooner."),
 "Blind II": L("Blind no acerto: defesa.", "Blind on hit: defence."),
 "Repulsion": L("Curse no Blasphemy: gasta Runic Ward, aplica Fragility e explode ao acertar.", "Curse in Blasphemy: spends Runic Ward, applies Fragility and explodes on hit."),
 # boss / defesa
 "Mark of Siphoning II": L("Inimigo marcado faz você roubar vida e mana com ataques.", "Marked enemies leech life and mana to you on attacks."),
 "Charged Mark": L("A marca gera cargas quando ativa.", "The mark generates charges when it activates."),
 "Mark for Death II": L("O alvo marcado tem Armour quebrada pelo dano físico que recebe.", "The marked target's Armour is broken by physical damage it takes."),
 "Eternal Mark": L("A marca não é consumida na primeira ativação.", "The mark isn't consumed the first time it activates."),
 "Mobility": L("Refutation pode ser usada andando.", "Refutation can be used while moving."),
 "Rapid Casting II": L("Refutation sai mais rápido.", "Refutation comes out faster."),
 "Stun III": L("Mais acúmulo de Stun no knockback do Wind Dancer.", "More Stun buildup on Wind Dancer's knockback."),
 "Enduring Impact II": L("Stun mais forte no Wind Dancer.", "Stronger stun on Wind Dancer."),
 "Clarity I": L("Mais regeneração de mana enquanto o Ghost Dance está ativo.", "More mana regeneration while Ghost Dance is active."),
 "Hulking Minions": L("Spirit Vessel maior, mais vida e dano — custa bem mais Spirit.", "Bigger Spirit Vessel with more life and damage — costs much more Spirit."),
 "Romira's Requital": L("Lineage: o companion toma parte do dano que você tomaria e você recupera parte como vida (com Forgotten Warden).", "Lineage: the companion takes part of the damage you'd take and you recoup part as life (with Forgotten Warden)."),
 "Amanamu's Tithe": L("Lineage de luxo no Spirit Vessel (menor prioridade; pede 6 links).", "Luxury lineage on Spirit Vessel (lowest priority; needs 6 links)."),
 "Oil Barrage": L("Dentro do Spirit Vessel: o companion cospe Oil Barrage junto (mais dano no boss).", "Inside Spirit Vessel: the companion spits Oil Barrage too (more boss damage)."),
 "Uhtred's Exodus": L("Lineage de luxo na Charge Regulation.", "Luxury lineage on Charge Regulation."),
}

SP30, SP100 = L("30 Spirit", "30 Spirit"), L("100 Spirit", "100 Spirit")
CHECK = L("Confira no jogo", "Check in game")
PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Frozen Locus + Glacial Cascade", "Frozen Locus + Glacial Cascade"),
  carry=L("Você: Glacial Cascade", "You: Glacial Cascade"), dmgSplit=[100, 0],
  goal=L("Monk com quarterstaff até o nível 13 e depois de mãos vazias (Hollow Palm Technique). Frozen Locus cria um cristal de gelo; afaste-se e acerte o cristal com o Large Spike (a ponta final) da Glacial Cascade para uma explosão enorme — é clear e dano de boss. Nível 10: Herald of Ice (King in the Mists dá os 30 de Spirit). Pounce pede um Talisman: Changeling Talisman no Weapon Set 2. Oil Barrage só entra nos mapas: por enquanto o objetivo é passar rápido.",
         "Monk with a quarterstaff until level 13, then empty-handed (Hollow Palm Technique). Frozen Locus creates an ice crystal; step away and hit it with Glacial Cascade's Large Spike (the final spike) for a huge explosion — that's clear and boss damage. Level 10: Herald of Ice (King in the Mists grants the 30 Spirit). Pounce needs a Talisman: Changeling Talisman on Weapon Set 2. Oil Barrage only comes in maps: for now the goal is speed."),
  rotation=[L("Frozen Locus no pack", "Frozen Locus into the pack"), L("Afaste-se e acerte o cristal com o Large Spike da Glacial Cascade", "Step back and hit the crystal with Glacial Cascade's Large Spike"), L("Boss: Frost Bomb quando ele aparecer → Frozen Locus → Glacial Cascade consumindo o Freeze", "Boss: Frost Bomb as it spawns → Frozen Locus → Glacial Cascade consuming the Freeze")],
  gems=[
   G("Glacial Cascade", ["Concentrated Area", "Rage I"], L("Clear + boss", "Clear + boss"), L("Quase todo o dano está no Large Spike; consumir um Freeze dá 250% a 425% more dano.", "Almost all damage is in the Large Spike; consuming a Freeze grants 250% to 425% more damage."), "free"),
   G("Frozen Locus", ["Ice Bite I"], L("Explosão de gelo", "Ice explosion"), L("Salta para trás e invoca o cristal; pode ser usado durante outras skills.", "Leaps back and summons the crystal; usable during other skills."), "free", since=3),
   G("Frost Bomb", [], L("Exposure", "Exposure"), L("Pulsa Exposure (menos resistência) e explode no fim.", "Pulses Exposure (lower resistance) and detonates at the end."), "free"),
   G("Quarterstaff Strike", [], L("Começo", "Start"), L("Só até ter Frozen Locus e Glacial Cascade.", "Only until you have Frozen Locus and Glacial Cascade."), "free", until=3),
   G("Pounce", [], L("Mobilidade", "Mobility"), L("Salto em Wolf Form; aplica a Predator's Mark no rare. Pede Talisman.", "Wolf Form leap; applies Predator's Mark on rares. Needs a Talisman."), "free", since=6),
   G("Herald of Ice", [], L("Clear em cadeia", "Chain clear"), L("Estilhaçar inimigo congelado causa explosão de gelo.", "Shattering a frozen enemy causes an ice explosion."), "core", 1, SP30, since=10),
  ],
  cheap=["Foxshade", "Northpaw", "Luminous Pace", L("Quarterstaff Magic com mais DPS (até o 13)", "Magic quarterstaff with the most DPS (until 13)")],
  full=["Pillar of the Caged God", "Surefooted Sigil", "Breath of the Mountains", L("Changeling Talisman no Set 2 (Pounce)", "Changeling Talisman on Set 2 (Pounce)")],
  stats=[L("Dano elemental plano em ataques", "Flat elemental attack damage"), L("Vida", "Life"), L("Movement Speed", "Movement Speed")],
  tree=L("Flow Like Water e Flow State; Hollow Palm Technique no nível 13 (você para de precisar de quarterstaff).", "Flow Like Water and Flow State; Hollow Palm Technique at level 13 (you stop needing a quarterstaff)."),
  avoid=[L("Acertar o cristal com o começo da Glacial Cascade (o dano está na ponta final)", "Hitting the crystal with the start of Glacial Cascade (damage is in the final spike)"), L("Gastar currency em quarterstaff antes do nível 13", "Spending currency on quarterstaffs before level 13")],
  exit=[L("King in the Mists: Herald of Ice", "King in the Mists: Herald of Ice"), L("Nível 13: Hollow Palm Technique", "Level 13: Hollow Palm Technique")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 31], tag=L("Storm Wave + Freeze de boss", "Storm Wave + boss Freeze"),
  carry=L("Você: Storm Wave · Glacial Cascade", "You: Storm Wave · Glacial Cascade"), dmgSplit=[100, 0],
  goal=L("Nível 22: Storm Wave vira o clear — onda de raio rápida, com muita chance de Shock e sem distância mínima. Detone o Frozen Locus com ela. A Glacial Cascade fica só para o boss: Hand of Chayula (com Freezing Mark e Elemental Weakness) marca e amaldiçoa, Storm Wave enche a barra de Freeze, Wave of Frost congela por muito tempo e o Large Spike da Glacial Cascade consome o Freeze. 1ª ascendência: Way of the Mountain.",
         "Level 22: Storm Wave becomes your clear — a fast lightning wave with high Shock chance and no minimum distance. Detonate Frozen Locus with it. Glacial Cascade is now boss-only: Hand of Chayula (with Freezing Mark and Elemental Weakness) marks and curses, Storm Wave fills the Freeze bar, Wave of Frost freezes for a long time and Glacial Cascade's Large Spike consumes the Freeze. 1st ascendancy: Way of the Mountain."),
  rotation=[L("Clear: Frozen Locus → Storm Wave", "Clear: Frozen Locus → Storm Wave"), L("Boss: Hand of Chayula + Frost Bomb", "Boss: Hand of Chayula + Frost Bomb"), L("Storm Wave (e Frozen Locus) até a barra de Freeze encher", "Storm Wave (and Frozen Locus) until the Freeze bar fills"), L("Wave of Frost congela", "Wave of Frost freezes"), L("Large Spike da Glacial Cascade consome o Freeze", "Glacial Cascade's Large Spike consumes the Freeze")],
  gems=[
   G("Storm Wave", ["Rage I", "Elemental Armament II", "Innervate"], L("Clear", "Clear"), L("Fissura de raio longa e rápida; Shock alto.", "Long, fast lightning fissure; high Shock."), "free", since=22),
   G("Glacial Cascade", ["Concentrated Area", "Elemental Armament II"], L("Burst de boss", "Boss burst"), L("Só para consumir o Freeze.", "Only to consume the Freeze."), "free"),
   G("Frozen Locus", ["Ice Bite I", "Elemental Armament II"], L("Explosão + Freeze", "Explosion + Freeze"), L("Detonado pelo Storm Wave.", "Detonated by Storm Wave."), "free"),
   G("Wave of Frost", ["Deep Freeze", "Ice Bite I"], L("Congela o boss", "Freezes the boss"), L("Congela na hora quem está Primed for Freeze.", "Instantly freezes enemies Primed for Freeze."), "free", since=22),
   G("Frost Bomb", ["Potent Exposure"], L("Exposure", "Exposure"), L("Solte quando o boss aparecer; relance quando acabar.", "Drop it as the boss spawns; recast when it ends."), "free"),
   G("Hand of Chayula", ["Freezing Mark", "Elemental Weakness"], L("Marca + curse", "Mark + curse"), L("Dash até o alvo aplicando a marca (efeito maior) e a curse (duração maior).", "Dashes to the target applying the mark (higher effect) and curse (longer duration)."), "free", since=26),
   G("Herald of Ice", ["Magnified Area I", "Elemental Armament I"], L("Clear em cadeia", "Chain clear"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Pounce", [], L("Mobilidade", "Mobility"), L("Set 2 (Talisman).", "Set 2 (Talisman)."), "free"),
  ],
  cheap=["Goldrim", "Wanderlust", L("Anéis com dano elemental plano e resistência", "Rings with flat elemental damage and resistance")],
  full=["Matsya", L("Amuleto com + nível de skills melee", "Amulet with + melee skill levels")],
  stats=[L("+ nível de skills melee (luvas, amuleto)", "+ melee skill levels (gloves, amulet)"), L("Dano elemental plano", "Flat elemental damage"), L("Vida e resistências", "Life and resistances")],
  tree=L("Killer Instinct, Dizzying Sweep e Essence of the Storm; Essence of the Mountain e Step Like Mist.", "Killer Instinct, Dizzying Sweep and Essence of the Storm; Essence of the Mountain and Step Like Mist."),
  avoid=[L("Glacial Cascade no clear depois do Storm Wave (lenta)", "Glacial Cascade for clear after Storm Wave (slow)"), L("Consumir o Freeze com o começo da cascata", "Consuming the Freeze with the start of the cascade")],
  exit=[L("1ª ascendência: Way of the Mountain", "1st ascendancy: Way of the Mountain"), L("Storm Wave com 3 links", "3-link Storm Wave")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[32, 45], tag=L("Herald of Thunder + sinos do Hollow Focus", "Herald of Thunder + Hollow Focus bells"),
  carry=L("Você: Storm Wave + heralds", "You: Storm Wave + heralds"), dmgSplit=[100, 0],
  goal=L("Azak Bog (+30 Spirit): Herald of Thunder — depois de matar inimigo com Shock, seus ataques soltam raios em volta. Com Herald of Ice isso vira clear em cadeia. 2ª ascendência: Hollow Focus Technique — sinos aparecem perto de você; acertar um sino cria uma onda de choque, e acertos no sino são SEMPRE críticos. Essa é a peça que depois alimenta o Cast on Critical. Branching Fissures I no Storm Wave abre o clear.",
         "Azak Bog (+30 Spirit): Herald of Thunder — after killing a Shocked enemy your attacks release lightning bolts around you. With Herald of Ice this becomes chain clear. 2nd ascendancy: Hollow Focus Technique — bells spawn near you; hitting one creates a shockwave, and hits against bells are ALWAYS critical. That's the piece that later feeds Cast on Critical. Branching Fissures I on Storm Wave widens the clear."),
  rotation=[L("Clear: Frozen Locus → Storm Wave (heralds explodem o resto)", "Clear: Frozen Locus → Storm Wave (heralds blow up the rest)"), L("Acerte o sino do Hollow Focus quando aparecer", "Hit the Hollow Focus bell when it appears"), L("Boss: igual ao Ato 2", "Boss: same as Act 2")],
  gems=[
   G("Storm Wave", ["Rage I", "Elemental Armament II", "Branching Fissures I"], L("Clear", "Clear"), L("Fissuras secundárias.", "Secondary fissures."), "free"),
   G("Glacial Cascade", ["Concentrated Area", "Elemental Armament II"], L("Burst de boss", "Boss burst"), L("Mesmo papel.", "Same role."), "free"),
   G("Frozen Locus", ["Ice Bite II", "Elemental Armament II", "Innervate"], L("Explosão + Freeze", "Explosion + Freeze"), L("4 links.", "4 links."), "free"),
   G("Wave of Frost", ["Deep Freeze", "Ice Bite II"], L("Congela o boss", "Freezes the boss"), L("Mesmo papel.", "Same role."), "free"),
   G("Frost Bomb", ["Potent Exposure"], L("Exposure", "Exposure"), L("Mesmo papel.", "Same role."), "free"),
   G("Hand of Chayula", ["Freezing Mark", "Elemental Weakness"], L("Marca + curse", "Mark + curse"), L("Mesmo papel.", "Same role."), "free"),
   G("Hollow Focus", [], L("Sinos (sempre crítico)", "Bells (always crit)"), L("Da ascendência. Cooldown Recovery aumenta a frequência dos sinos: coloque assim que tiver o support.", "From the ascendancy. Cooldown Recovery increases bell frequency: add it as soon as you have the support."), "free", since=40),
   G("Herald of Ice", ["Magnified Area I", "Elemental Armament II"], L("Clear em cadeia", "Chain clear"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Herald of Thunder", ["Concentrated Area", "Elemental Armament II"], L("Raios em cadeia", "Chained bolts"), L("30 Spirit (Azak Bog).", "30 Spirit (Azak Bog)."), "core", 2, SP30),
   G("Pounce", [], L("Mobilidade", "Mobility"), L("Set 2.", "Set 2."), "free"),
  ],
  cheap=["Gamblesprint", "Sierran Inheritance", L("Luvas +1/+2 nível de melee + dano plano", "Gloves +1/+2 melee levels + flat damage")],
  full=["The Smiling Knight", L("Iron Rune ×2 no peito; Storm/Glacial Rune nas botas/capacete", "Iron Rune ×2 on the chest; Storm/Glacial Rune on boots/helmet")],
  stats=[L("+ nível de melee", "+ melee levels"), L("Dano elemental plano", "Flat elemental damage"), L("Resistências", "Resistances")],
  tree=L("Concussive Attack, Tenfold Attacks e Harness the Elements.", "Concussive Attack, Tenfold Attacks and Harness the Elements."),
  avoid=[L("Deixar os sinos sumirem sem acertar", "Letting bells vanish without hitting them")],
  exit=[L("Azak Bog (+30 Spirit)", "Azak Bog (+30 Spirit)"), L("2ª ascendência: Hollow Focus Technique", "2nd ascendancy: Hollow Focus Technique")]),

 dict(id="a4", name=L("Ato 4 + Interlúdios", "Act 4 + Interludes"), lv=[46, 64], tag=L("Fim da campanha + preparar a troca", "End of campaign + prepare the swap"),
  carry=L("Você: Storm Wave + heralds", "You: Storm Wave + heralds"), dmgSplit=[100, 0],
  goal=L("Mesma rotação, mais links (Elemental Focus na Glacial Cascade e no Herald of Ice). Agora comece a juntar a troca: guarde o Greater Jeweller's Orb garantido do Ato 4 para o Oil Barrage, identifique todo Talisman rare que cair (procure dano elemental plano) e guarde gold para o respec. Lythara (+40 Spirit) completa 100 de Spirit de quests. Tribal Medicine: Evasion como Deflection; Great White One: +30% Armour/Evasion/ES.",
         "Same rotation, more links (Elemental Focus on Glacial Cascade and Herald of Ice). Now start gathering the swap: save Act 4's guaranteed Greater Jeweller's Orb for Oil Barrage, identify every rare Talisman that drops (look for flat elemental damage) and save gold for the respec. Lythara (+40 Spirit) completes 100 Spirit from quests. Tribal Medicine: Evasion as Deflection; Great White One: +30% Armour/Evasion/ES."),
  rotation=[L("Clear: Frozen Locus → Storm Wave", "Clear: Frozen Locus → Storm Wave"), L("Boss: Hand of Chayula + Frost Bomb → Storm Wave → Wave of Frost → Glacial Cascade", "Boss: Hand of Chayula + Frost Bomb → Storm Wave → Wave of Frost → Glacial Cascade")],
  gems=[
   G("Storm Wave", ["Rage II", "Elemental Armament II", "Branching Fissures I"], L("Clear", "Clear"), L("Mesmo papel.", "Same role."), "free"),
   G("Glacial Cascade", ["Concentrated Area", "Elemental Armament II", "Elemental Focus"], L("Burst de boss", "Boss burst"), L("Elemental Focus: quem congela é o Wave of Frost.", "Elemental Focus: Wave of Frost does the freezing."), "free"),
   G("Frozen Locus", ["Ice Bite II", "Elemental Armament II", "Innervate"], L("Explosão + Freeze", "Explosion + Freeze"), L("Mesmo papel.", "Same role."), "free"),
   G("Wave of Frost", ["Deep Freeze", "Ice Bite II"], L("Congela o boss", "Freezes the boss"), L("Mesmo papel.", "Same role."), "free"),
   G("Frost Bomb", ["Potent Exposure"], L("Exposure", "Exposure"), L("Mesmo papel.", "Same role."), "free"),
   G("Hand of Chayula", ["Freezing Mark", "Elemental Weakness"], L("Marca + curse", "Mark + curse"), L("Mesmo papel.", "Same role."), "free"),
   G("Hollow Focus", ["Cooldown Recovery II"], L("Sinos", "Bells"), L("Mais sinos.", "More bells."), "free"),
   G("Herald of Ice", ["Magnified Area II", "Elemental Armament II", "Elemental Focus"], L("Clear em cadeia", "Chain clear"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Herald of Thunder", ["Concentrated Area", "Elemental Armament II"], L("Raios em cadeia", "Chained bolts"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Pounce", ["Cooldown Recovery II"], L("Mobilidade", "Mobility"), L("Mais saltos.", "More leaps."), "free"),
  ],
  cheap=["The Dancing Mirage", "Idle Hands", L("Resistências no cap para os mapas", "Capped resistances for maps")],
  full=["Atsak's Sight", "Beacon of Azis", L("Talisman rare guardado para a troca", "Rare Talisman saved for the swap")],
  stats=[L("Resistências 75%", "75% resistances"), L("Vida e ES", "Life and ES"), L("Movement Speed", "Movement Speed")],
  tree=L("Blinding Strike, Primal Sundering, Echoing Frost/Thunder/Flames, Escape Velocity e Alternating Current. No fim da campanha o planner já troca nós fortes do começo por escala.", "Blinding Strike, Primal Sundering, Echoing Frost/Thunder/Flames, Escape Velocity and Alternating Current. Near the end of the campaign the planner already swaps early-game nodes for scaling."),
  avoid=[L("Usar o Greater Jeweller's Orb nas skills da campanha", "Using the Greater Jeweller's Orb on campaign skills"), L("Vender Talismans rare sem identificar", "Vendoring rare Talismans unidentified")],
  exit=[L("Lythara (+40 Spirit): 100 de Spirit", "Lythara (+40 Spirit): 100 Spirit"), L("Talisman de 300+ EDPS (drop, craft ou trade)", "300+ EDPS Talisman (drop, craft or trade)")]),

 dict(id="swap", name=L("Troca: Oil Barrage", "Swap: Oil Barrage"), lv=[65, 74], tag=L("Wyvern + Power Charges", "Wyvern + Power Charges"),
  carry=L("Você: Oil Barrage", "You: Oil Barrage"), dmgSplit=[100, 0],
  goal=L("Nos primeiros mapas, com um Spiny Talisman de 300+ de dano elemental por segundo (ou outro Talisman com crítico parecido), faça o respec. Oil Barrage transforma você em wyvern: sem Power Charge ele só cospe óleo; COM Power Charges ele canaliza a rajada elétrica que mata tudo. Por isso cada mapa começa igual: dê Devour num sino do Hollow Focus (sinos podem sofrer Cull) para ganhar a primeira Power Charge. 3ª ascendência: Way of the Stonefist — suas luvas viram Fists of Stone com mods mais fortes; transforme em Runeforged Fists of Stone na Verisium Anvil para usar Refutation. Spirit: Charge Regulation, Wind Dancer e Ghost Dance (90 de 100).",
         "In your first maps, with a Spiny Talisman with 300+ elemental DPS (or another Talisman with similar crit), respec. Oil Barrage turns you into a wyvern: without Power Charges it only spits oil; WITH Power Charges it channels the electrified barrage that kills everything. So every map starts the same way: Devour a Hollow Focus bell (bells can be Culled) for your first Power Charge. 3rd ascendancy: Way of the Stonefist — your gloves become Fists of Stone with stronger mods; turn them into Runeforged Fists of Stone at the Verisium Anvil to use Refutation. Spirit: Charge Regulation, Wind Dancer and Ghost Dance (90 of 100)."),
  rotation=[L("Entrou no mapa: Devour no sino (1ª Power Charge)", "Entered the map: Devour the bell (1st Power Charge)"), L("Canalize Oil Barrage no pack", "Channel Oil Barrage into the pack"), L("Devour em sinos e corpos quando faltar carga", "Devour bells and corpses when charges run low"), L("Boss: Devour → Rend (buff) → Refutation → Hand of Chayula → Oil Barrage", "Boss: Devour → Rend (buff) → Refutation → Hand of Chayula → Oil Barrage")],
  gems=[
   G("Oil Barrage", ["Salvo", "Nova Projectiles I", "Ricochet II", "Fork"], L("Clear + boss", "Clear + boss"), L("Consome Power Charges para canalizar a rajada elétrica; os projéteis saem em sequência e vários acertam o mesmo alvo. Greater Jeweller's Orb aqui.", "Consumes Power Charges to channel the electrified barrage; projectiles fire in sequence and several hit the same target. Greater Jeweller's Orb here."), "free"),
   G("Devour", ["Blazing Critical", "Thrill of the Kill II", "Charge Profusion II", "Rage III"], L("Power Charges", "Power Charges"), L("Devora corpo, sino ou inimigo no Cull: regenera vida e dá 1 Power Charge por alvo. De longe, salta até ele.", "Devours a corpse, bell or cullable enemy: regenerates life and grants 1 Power Charge per target. From far away it leaps to it."), "free"),
   G("Rend", ["Heightened Charges", "Prolonged Duration II", "Rage III"], L("Buff de raio", "Lightning buff"), L("Consome 1 Power Charge para um buff de dano extra de raio.", "Consumes 1 Power Charge for an extra lightning damage buff."), "free"),
   G("Hollow Focus", ["Cooldown Recovery II", "Magnified Area II", "Overabundance II"], L("Sinos = cargas e críticos", "Bells = charges and crits"), L("Cooldown Recovery é obrigatório: mais sinos, mais Devour.", "Cooldown Recovery is mandatory: more bells, more Devour."), "free"),
   G("Hand of Chayula", ["Freezing Mark", "Elemental Weakness", "Mark of Siphoning II"], L("Marca + curse", "Mark + curse"), L("No começo do boss.", "At the start of the boss."), "free"),
   G("Refutation", ["Cooldown Recovery II", "Mobility", "Efficiency II"], L("Bloqueio total", "Full block"), L("Gasta todo o Runic Ward: bloqueia todos os hits bloqueáveis e aplica Parried. Só no boss (no clear pode causar Heavy Stun). Precisa das luvas Runeforged.", "Spends all Runic Ward: blocks every blockable hit and applies Parried. Bosses only (while clearing it can cause Heavy Stun). Needs Runeforged gloves."), "free"),
   G("Charge Regulation", [], L("Buffs das cargas", "Charge buffs"), L("Buffs fortes conforme as cargas ativas; consome cargas a cada poucos segundos.", "Strong buffs based on active charges; consumes charges every few seconds."), "core", 1, SP30),
   G("Wind Dancer", ["Magnified Area II", "Stun III", "Enduring Impact II"], L("Defesa", "Defence"), L("Evasão por estágio; ao ser atingido, repele em volta.", "Evasion per stage; when hit, knocks back around you."), "core", 2, SP30),
   G("Ghost Dance", ["Cooldown Recovery II", "Clarity I"], L("Recuperação de ES", "ES recovery"), L("Ghost Shrouds recuperam ES pela Evasão.", "Ghost Shrouds recover ES based on Evasion."), "core", 3, SP30),
   G("Blasphemy", ["Repulsion", "Living Lightning II", "Culmination II", "Ailith's Chimes"], L("Power Charges (opção)", "Power Charges (option)"), L("Opção do havoc616 antes do Thaumaturgic Generator e das luvas com carga no crítico: mais Power Charges em troca da Charge Regulation e do Ghost Dance.", "havoc616's option before Thaumaturgic Generator and power-charge-on-crit gloves: more Power Charges at the cost of Charge Regulation and Ghost Dance."), "opt", 1, CHECK),
  ],
  cheap=[L("Spiny Talisman 300+ EDPS (Transmutation/Augmentation → Regal)", "300+ EDPS Spiny Talisman (Transmutation/Augmentation → Regal)"), "Breath of the Mountains", L("Gems: Uncut Skill Gem nível 14", "Gems: level 14 Uncut Skill Gem")],
  full=[L("Perfect Essence of Battle no Talisman (+3 nível de ataques)", "Perfect Essence of Battle on the Talisman (+3 attack levels)"), L("Runeforged Fists of Stone", "Runeforged Fists of Stone")],
  stats=[L("Dano elemental plano no Talisman", "Flat elemental damage on the Talisman"), L("Crítico", "Crit"), L("+ nível de ataques/projéteis", "+ attack/projectile levels")],
  tree=L("Respec: sai Hollow Palm e os nós de gelo; entram True Strike, For the Jugular, Heartbreaking, Heartstopping, Struck Through (crítico), Mindful Awareness e Subterfuge Mask (defesa). Set 1: dano de ataque. Set 2: nós de Parry para a Refutation.", "Respec: Hollow Palm and the ice nodes go; True Strike, For the Jugular, Heartbreaking, Heartstopping, Struck Through (crit), Mindful Awareness and Subterfuge Mask (defence) come in. Set 1: attack damage. Set 2: Parry nodes for Refutation."),
  avoid=[L("Oil Barrage sem Power Charge (só cospe óleo)", "Oil Barrage without Power Charges (only spits oil)"), L("Nova Projectiles II no lugar da I", "Nova Projectiles II instead of I"), L("Refutation no clear", "Refutation while clearing")],
  exit=[L("3ª ascendência: Way of the Stonefist", "3rd ascendancy: Way of the Stonefist"), L("Amuleto +50 Spirit para o Cast on Critical", "+50 Spirit amulet for Cast on Critical")]),

 dict(id="maps", name=L("Mapas: teleporte", "Maps: teleport"), lv=[75, 84], tag=L("Cast on Critical + Lightning Warp", "Cast on Critical + Lightning Warp"),
  carry=L("Você: Oil Barrage + Lightning Warp", "You: Oil Barrage + Lightning Warp"), dmgSplit=[85, 15],
  goal=L("É aqui que a build começa a teleportar. Cast on Critical (100 de Spirit) ganha energia a cada crítico do Oil Barrage e, cheio, dispara o Lightning Warp: você teleporta para dentro de um inimigo abaixo do limite de Cull e ele explode em raio — em pack, o próximo alvo já está no Cull e o ciclo repete. No rare/boss, o Warp aplica um debuff que explode quando ele entrar no Cull. Os sinos do Hollow Focus são sempre críticos e também sofrem Cull: combustível infinito. Spirit: 100 de quests + 50 de amuleto = CoC + Charge Regulation (Alpha's Howl dá +100). 4ª ascendência: Runic Meridians (runas tatuadas). Instill Thaumaturgic Generator no amuleto (carga aleatória periódica) e compre Forgotten Warden.",
         "This is where the build starts teleporting. Cast on Critical (100 Spirit) gains Energy on every Oil Barrage crit and, when full, triggers Lightning Warp: you teleport inside an enemy under the Cull threshold and it explodes in lightning — in a pack, the next target is already cullable and the cycle repeats. On a rare/boss, Warp applies a debuff that explodes once it enters Cull. Hollow Focus bells are always crit and can be Culled too: endless fuel. Spirit: 100 from quests + 50 from the amulet = CoC + Charge Regulation (Alpha's Howl gives +100). 4th ascendancy: Runic Meridians (tattooed runes). Instill Thaumaturgic Generator on the amulet (periodic random charge) and buy Forgotten Warden."),
  rotation=[L("Devour no sino → canalize Oil Barrage", "Devour the bell → channel Oil Barrage"), L("Continue canalizando: o Lightning Warp teleporta sozinho de alvo em alvo", "Keep channeling: Lightning Warp teleports on its own from target to target"), L("Acerte sinos para críticos garantidos", "Hit bells for guaranteed crits"), L("Boss: Devour → Rend → Refutation → Hand of Chayula → Oil Barrage (o Warp finaliza no Cull)", "Boss: Devour → Rend → Refutation → Hand of Chayula → Oil Barrage (Warp finishes at Cull)")],
  gems=[
   G("Oil Barrage", ["Salvo", "Nova Projectiles I", "Ricochet II", "Fork", "Pinpoint Critical"], L("Clear + boss", "Clear + boss"), L("5 links. Pinpoint Critical até ter 50% de crítico.", "5 links. Pinpoint Critical until you have 50% crit."), "free"),
   G("Cast on Critical", ["Lightning Warp", "Boundless Energy II", "Energy Retention", "Fluke"], L("Teleporte automático", "Automatic teleport"), L("Setup de 18 dos 22 Martial Artists de Oil Barrage do ladder (os outros 4 usam Cast on Elemental Ailment). Gera energia com críticos e dispara o Lightning Warp no máximo.", "Setup on 18 of the 22 Oil Barrage Martial Artists on the ladder (the other 4 use Cast on Elemental Ailment). Gains Energy on crits and triggers Lightning Warp at max."), "core", 1, SP100),
   G("Devour", ["Blazing Critical", "Thrill of the Kill II", "Charge Profusion II", "Rage III"], L("Power Charges", "Power Charges"), L("Mesmo papel.", "Same role."), "free"),
   G("Rend", ["Heightened Charges", "Prolonged Duration II", "Rage III", "Perpetual Charge"], L("Buff de raio", "Lightning buff"), L("Perpetual Charge: chance de não gastar a carga.", "Perpetual Charge: chance not to spend the charge."), "free"),
   G("Hollow Focus", ["Cooldown Recovery II", "Magnified Area II", "Overabundance II", "Prolonged Duration II"], L("Sinos", "Bells"), L("Mesmo papel.", "Same role."), "free"),
   G("Hand of Chayula", ["Freezing Mark", "Elemental Weakness", "Mark of Siphoning II", "Charged Mark"], L("Marca + curse", "Mark + curse"), L("Mesmo papel.", "Same role."), "free"),
   G("Refutation", ["Cooldown Recovery II", "Efficiency II", "Prolonged Duration II", "Mobility"], L("Bloqueio total", "Full block"), L("Só no boss.", "Bosses only."), "free"),
   G("Charge Regulation", [], L("Buffs das cargas", "Charge buffs"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Wind Dancer", ["Magnified Area II", "Stun III", "Enduring Impact II", "Rage III"], L("Defesa", "Defence"), L("30 Spirit: entra com 160+ de Spirit.", "30 Spirit: comes in at 160+ Spirit."), "core", 3, SP30),
   G("Ghost Dance", ["Cooldown Recovery II", "Clarity I"], L("Recuperação de ES", "ES recovery"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Spirit Vessel", ["Oil Barrage", "Hulking Minions", "Romira's Requital"], L("Companion + defesa", "Companion + defence"), L("Com Forgotten Warden, o companion toma parte do dano. Hulking Minions custa bem mais Spirit.", "With Forgotten Warden, the companion takes part of the damage. Hulking Minions costs much more Spirit."), "opt", 1, CHECK),
  ],
  cheap=["Forgotten Warden", L("Amuleto +50 Spirit com Thaumaturgic Generator", "+50 Spirit amulet with Thaumaturgic Generator"), "Myris Uxor"],
  full=["Alpha's Howl", L("Talisman 380+ EDPS com + nível de ataques", "380+ EDPS Talisman with + attack levels"), L("Time-Lost Jewel de crítico", "Crit Time-Lost Jewel")],
  stats=[L("Crítico (meta: 50%)", "Crit (goal: 50%)"), L("Spirit (150+)", "Spirit (150+)"), L("Limite de Cull (mais teleportes)", "Cull threshold (more teleports)"), L("Evasão/ES", "Evasion/ES")],
  tree=L("Crítico completo, Spectral Ward, Stand and Deliver, Acceleration e as três de defesa do Monk (First Principle of the Hollow, First Teachings of the Keeper, The Hollowkeeper).", "Full crit, Spectral Ward, Stand and Deliver, Acceleration and the three Monk defence notables (First Principle of the Hollow, First Teachings of the Keeper, The Hollowkeeper)."),
  avoid=[L("Cast on Critical com crítico baixo (quase não dispara)", "Cast on Critical with low crit (barely triggers)"), L("Ficar sem mana para o Lightning Warp", "Running out of mana for Lightning Warp")],
  exit=[L("4ª ascendência: Runic Meridians", "4th ascendancy: Runic Meridians"), L("50% de crítico no Oil Barrage", "50% crit on Oil Barrage")]),

 dict(id="endgame", name=L("Endgame: crítico", "Endgame: crit"), lv=[85, 92], tag=L("50%+ crítico · 490 EDPS", "50%+ crit · 490 EDPS"),
  carry=L("Você: Oil Barrage + Lightning Warp", "You: Oil Barrage + Lightning Warp"), dmgSplit=[85, 15],
  goal=L("Com 50%+ de chance de crítico (confira no hideout), troque Pinpoint Critical por Elemental Armament II. Ailith's Chimes no Hollow Focus dá Power Charges em lutas paradas. Metas de item: Talisman de 490+ EDPS com 15%+ de crítico e + níveis, ~150% de raridade, botas 35% Movement Speed com Evasão e Deflection, Forgotten Warden bem rolado e Time-Lost Jewel de 3–4 mods (crítico e dano crítico). Soul Drain no Cast on Critical resolve a mana: cada Cull devolve mana.",
         "At 50%+ crit chance (check in hideout), swap Pinpoint Critical for Elemental Armament II. Ailith's Chimes on Hollow Focus grants Power Charges in stationary fights. Item goals: 490+ EDPS Talisman with 15%+ crit and + levels, ~150% rarity, 35% Movement Speed boots with Evasion and Deflection, a well-rolled Forgotten Warden and 3–4 mod Time-Lost Jewels (crit chance and crit damage). Soul Drain on Cast on Critical solves mana: every Cull refunds mana."),
  rotation=[L("Devour no sino → Oil Barrage (teleporte automático)", "Devour the bell → Oil Barrage (automatic teleport)"), L("Boss: Devour/Rend → Refutation → Hand of Chayula → Oil Barrage parado nos sinos", "Boss: Devour/Rend → Refutation → Hand of Chayula → Oil Barrage standing on the bells")],
  gems=[
   G("Oil Barrage", ["Salvo", "Nova Projectiles I", "Ricochet II", "Fork", "Elemental Armament II"], L("Clear + boss", "Clear + boss"), L("Elemental Armament II no lugar do Pinpoint com 50%+ de crítico.", "Elemental Armament II instead of Pinpoint at 50%+ crit."), "free"),
   G("Cast on Critical", ["Lightning Warp", "Boundless Energy II", "Energy Retention", "Fluke", "Soul Drain"], L("Teleporte automático", "Automatic teleport"), L("Soul Drain: mana a cada Cull.", "Soul Drain: mana on every Cull."), "core", 1, SP100),
   G("Devour", ["Blazing Critical", "Thrill of the Kill II", "Charge Profusion II", "Rage III", "Prolonged Duration II"], L("Power Charges", "Power Charges"), L("6 links.", "6 links."), "free"),
   G("Rend", ["Heightened Charges", "Prolonged Duration II", "Rage III", "Perpetual Charge", "Rapid Attacks III"], L("Buff de raio", "Lightning buff"), L("6 links.", "6 links."), "free"),
   G("Hollow Focus", ["Cooldown Recovery II", "Living Lightning II", "Culmination II", "Ailith's Chimes", "Charge Profusion II"], L("Sinos + Power Charges", "Bells + Power Charges"), L("Setup Ailith's Chimes do planner.", "Planner's Ailith's Chimes setup."), "free"),
   G("Hand of Chayula", ["Freezing Mark", "Elemental Weakness", "Mark of Siphoning II", "Charged Mark", "Mark for Death II"], L("Marca + curse", "Mark + curse"), L("Mesmo papel.", "Same role."), "free"),
   G("Refutation", ["Cooldown Recovery II", "Efficiency II", "Prolonged Duration II", "Mobility", "Rapid Casting II"], L("Bloqueio total", "Full block"), L("Só no boss.", "Bosses only."), "free"),
   G("Charge Regulation", [], L("Buffs das cargas", "Charge buffs"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Wind Dancer", ["Magnified Area II", "Stun III", "Enduring Impact II", "Rage III", "Blind II"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Ghost Dance", ["Cooldown Recovery II", "Clarity I"], L("Recuperação de ES", "ES recovery"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Spirit Vessel", ["Oil Barrage", "Hulking Minions", "Romira's Requital", "Amanamu's Tithe"], L("Companion + defesa", "Companion + defence"), L("Amanamu's Tithe é a menor prioridade.", "Amanamu's Tithe is lowest priority."), "opt", 1, CHECK),
  ],
  cheap=["Nascent Hope", "Lavianga's Spirits", "Heart of the Well"],
  full=[L("Talisman 490+ EDPS, 15%+ crítico, + níveis", "490+ EDPS Talisman, 15%+ crit, + levels"), L("Botas 35% MS com Deflection", "35% MS boots with Deflection"), L("Time-Lost Jewel 3–4 mods", "3–4 mod Time-Lost Jewel")],
  stats=[L("Crítico perto de 100% no Oil Barrage", "Crit close to 100% on Oil Barrage"), L("Dano crítico", "Crit damage"), L("Raridade (~150%)", "Rarity (~150%)"), L("Gems 19–20 com 20% de qualidade", "19–20 gems with 20% quality")],
  tree=L("+ Shimmering. Time-Lost Jewels nos sockets perto dos nós de crítico.", "+ Shimmering. Time-Lost Jewels in the sockets near the crit nodes."),
  avoid=[L("Tirar Pinpoint Critical antes de 50% de crítico", "Removing Pinpoint Critical before 50% crit")],
  exit=[L("Pinnacles com Refutation", "Pinnacles with Refutation"), L("Rakiata's Flow", "Rakiata's Flow")]),

 dict(id="max", name=L("Aspiracional: Rakiata's Flow", "Aspirational: Rakiata's Flow"), lv=[93, 100], tag=L("Resistências invertidas + Headhunter", "Inverted resistances + Headhunter"),
  carry=L("Você: Oil Barrage + Lightning Warp", "You: Oil Barrage + Lightning Warp"), dmgSplit=[85, 15],
  goal=L("Rakiata's Flow no Oil Barrage: os acertos tratam as resistências elementais do inimigo como invertidas. Use Oil Barrage nível 21 com 0% de qualidade e tire Elemental Weakness da Hand of Chayula e o Oil Barrage do Spirit Vessel. Capacete com Raven-Touched Shard e instill Thaumaturgic Generator; amuleto com instill Zarokh's Gift (socket de jewel extra). Rite of Passage: Stag > Cat > Wolf > Owl > Bear. Para mapear mais liso, o planner troca a Refutation por Blasphemy + Repulsion com o setup do Ailith's Chimes (peito com +50 Spirit).",
         "Rakiata's Flow on Oil Barrage: hits treat enemy elemental resistances as inverted. Use a level 21, 0% quality Oil Barrage and remove Elemental Weakness from Hand of Chayula and Oil Barrage from Spirit Vessel. Helmet with Raven-Touched Shard and a Thaumaturgic Generator instill; amulet with a Zarokh's Gift instill (extra jewel socket). Rite of Passage: Stag > Cat > Wolf > Owl > Bear. For smoother mapping, the planner swaps Refutation for Blasphemy + Repulsion with the Ailith's Chimes setup (chest with +50 Spirit)."),
  rotation=[L("Devour no sino → Oil Barrage", "Devour the bell → Oil Barrage"), L("Headhunter: cada rare morto vira buff de 60 s", "Headhunter: every rare killed becomes a 60 s buff"), L("Boss: Devour/Rend → Hand of Chayula → Oil Barrage", "Boss: Devour/Rend → Hand of Chayula → Oil Barrage")],
  gems=[
   G("Oil Barrage", ["Salvo", "Nova Projectiles I", "Ricochet II", "Fork", "Rakiata's Flow"], L("Clear + boss", "Clear + boss"), L("Nível 21, 0% de qualidade.", "Level 21, 0% quality."), "free"),
   G("Cast on Critical", ["Lightning Warp", "Boundless Energy II", "Energy Retention", "Fluke", "Soul Drain"], L("Teleporte automático", "Automatic teleport"), L("Mesmo papel.", "Same role."), "core", 1, SP100),
   G("Devour", ["Blazing Critical", "Thrill of the Kill II", "Charge Profusion II", "Rage III", "Prolonged Duration II"], L("Power Charges", "Power Charges"), L("Mesmo papel.", "Same role."), "free"),
   G("Rend", ["Heightened Charges", "Prolonged Duration II", "Rage III", "Perpetual Charge", "Rapid Attacks III"], L("Buff de raio", "Lightning buff"), L("Mesmo papel.", "Same role."), "free"),
   G("Hollow Focus", ["Cooldown Recovery II", "Magnified Area II", "Overabundance II", "Prolonged Duration II", "Blind II"], L("Sinos", "Bells"), L("Na versão de mapa, o Ailith's Chimes vai para o Blasphemy.", "In the mapping version, Ailith's Chimes moves to Blasphemy."), "free"),
   G("Blasphemy", ["Repulsion", "Living Lightning II", "Culmination II", "Ailith's Chimes", "Charge Profusion II"], L("Power Charges no mapa", "Power Charges while mapping"), L("Precisa de peito com +50 Spirit.", "Needs a chest with +50 Spirit."), "opt", 1, CHECK),
   G("Hand of Chayula", ["Freezing Mark", "Mark of Siphoning II", "Charged Mark", "Mark for Death II", "Eternal Mark"], L("Marca", "Mark"), L("Sem Elemental Weakness (conflita com Rakiata's Flow). Pode ser Pounce.", "No Elemental Weakness (conflicts with Rakiata's Flow). Can be Pounce."), "free"),
   G("Charge Regulation", ["Uhtred's Exodus"], L("Buffs das cargas", "Charge buffs"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Wind Dancer", ["Magnified Area II", "Stun III", "Enduring Impact II", "Rage III", "Blind II"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Ghost Dance", ["Cooldown Recovery II", "Clarity I"], L("Recuperação de ES", "ES recovery"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
  ],
  cheap=["Rite of Passage", "Kalandra's Touch"],
  full=["Headhunter", L("Raven-Touched Shard no capacete", "Raven-Touched Shard in the helmet"), L("Jewels de 5 mods e Time-Lost de 4–5 mods", "5-mod jewels and 4–5 mod Time-Lost Jewels")],
  stats=[L("+ nível do Oil Barrage (21)", "+ Oil Barrage level (21)"), L("Talisman com velocidade de ataque", "Talisman with attack speed"), L("Qualidade 20% nos jewels", "20% quality on jewels")],
  tree=L("+ Dizzying Sweep, Chakra of Impact, Killer Instinct, Enhanced Reflexes e Beastial Skin; mais um socket de jewel.", "+ Dizzying Sweep, Chakra of Impact, Killer Instinct, Enhanced Reflexes and Beastial Skin; one more jewel socket."),
  avoid=[L("Rakiata's Flow com Elemental Weakness ou Exposure", "Rakiata's Flow with Elemental Weakness or Exposure")],
  exit=[L("Pinnacles e mapas juiced", "Pinnacles and juiced maps")]),
]
PH = {p["id"]: p for p in PHASES}

BOX = {
 "a1": ("Spike", [L("da Glacial Cascade", "of Glacial Cascade")], L("O dano está na ponta final: acerte o cristal com ela.", "The damage is in the final spike: hit the crystal with it.")),
 "a2": ("Freeze", [L("consumido pela cascata", "consumed by the cascade")], L("Wave of Frost congela, Glacial Cascade consome.", "Wave of Frost freezes, Glacial Cascade consumes.")),
 "swap": ("1+", [L("Power Charge", "Power Charge")], L("Sem Power Charge o Oil Barrage só cospe óleo: Devour no sino.", "Without Power Charges Oil Barrage only spits oil: Devour the bell.")),
 "maps": ("100", [L("Spirit do Cast on Critical", "Cast on Critical Spirit")], L("O teleporte custa 100 de Spirit: amuleto com Spirit primeiro.", "The teleport costs 100 Spirit: Spirit amulet first.")),
 "endgame": ("50%", [L("chance de crítico", "crit chance")], L("Com 50%+ troque Pinpoint Critical por Elemental Armament II.", "At 50%+ swap Pinpoint Critical for Elemental Armament II.")),
 "max": ("21", [L("nível do Oil Barrage", "Oil Barrage level")], L("Rakiata's Flow: nível 21, 0% de qualidade.", "Rakiata's Flow: level 21, 0% quality.")),
}
SPIRIT_NOTE = {
 "a1": L("Herald of Ice (30).", "Herald of Ice (30)."),
 "a3": L("Herald of Ice (30) + Herald of Thunder (30).", "Herald of Ice (30) + Herald of Thunder (30)."),
 "swap": L("100 de quests: Charge Regulation + Wind Dancer + Ghost Dance (90).", "100 from quests: Charge Regulation + Wind Dancer + Ghost Dance (90)."),
 "maps": L("Ordem: Cast on Critical (100) → Charge Regulation → Wind Dancer → Ghost Dance. 150 de Spirit = CoC + 1; 210 = CoC + 3.", "Order: Cast on Critical (100) → Charge Regulation → Wind Dancer → Ghost Dance. 150 Spirit = CoC + 1; 210 = CoC + 3."),
 "endgame": L("Meta: 190+ (CoC + Charge Regulation + Wind Dancer + Ghost Dance). Spirit Vessel conforme sobrar.", "Goal: 190+ (CoC + Charge Regulation + Wind Dancer + Ghost Dance). Spirit Vessel with whatever is left."),
 "max": L("+ Blasphemy na versão de mapa (peito +50 Spirit).", "+ Blasphemy in the mapping version (+50 Spirit chest)."),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in SPIRIT_NOTE.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Quarterstaff Strike + Glacial Cascade + Frost Bomb.", "Quarterstaff Strike + Glacial Cascade + Frost Bomb."),
 3: L("Frozen Locus: detone o cristal com o Large Spike.", "Frozen Locus: detonate the crystal with the Large Spike."),
 10: L("King in the Mists (+30): Herald of Ice.", "King in the Mists (+30): Herald of Ice."),
 10: L("Goldrim (resistências) e Wanderlust no 11 (20% MS).", "Goldrim (resistances) and Wanderlust at 11 (20% MS)."),
 13: L("Hollow Palm Technique: mãos vazias. A partir daqui, Evasão dos itens = velocidade de ataque e ES = crítico.", "Hollow Palm Technique: empty hands. From here, item Evasion = attack speed and ES = crit."),
 16: L("Gamblesprint e Sierran Inheritance: Evasão barata.", "Gamblesprint and Sierran Inheritance: cheap Evasion."),
 26: L("The Smiling Knight: primeiro crítico do capacete.", "The Smiling Knight: first crit on the helmet."),
 28: L("The Dancing Mirage, Idle Hands e Atsak's Sight.", "The Dancing Mirage, Idle Hands and Atsak's Sight."),
 30: L("Beacon of Azis: crítico ignora resistência elemental.", "Beacon of Azis: crits ignore elemental resistance."),
 22: L("Storm Wave e Wave of Frost.", "Storm Wave and Wave of Frost."),
 25: L("1ª ascendência: Way of the Mountain.", "1st ascendancy: Way of the Mountain."),
 26: L("Hand of Chayula + Freezing Mark + Elemental Weakness.", "Hand of Chayula + Freezing Mark + Elemental Weakness."),
 35: L("Azak Bog (+30): Herald of Thunder.", "Azak Bog (+30): Herald of Thunder."),
 40: L("2ª ascendência: Hollow Focus Technique (sinos sempre críticos).", "2nd ascendancy: Hollow Focus Technique (always-crit bells)."),
 55: L("Guarde o Greater Jeweller's Orb e Talismans rare.", "Save the Greater Jeweller's Orb and rare Talismans."),
 62: L("Lythara (+40): 100 de Spirit.", "Lythara (+40): 100 Spirit."),
 65: L("Troca para Oil Barrage: Devour no sino para a 1ª Power Charge.", "Swap to Oil Barrage: Devour the bell for the 1st Power Charge."),
 68: L("3ª ascendência: Way of the Stonefist → Runeforged Fists of Stone.", "3rd ascendancy: Way of the Stonefist → Runeforged Fists of Stone."),
 75: L("Cast on Critical + Lightning Warp: o teleporte.", "Cast on Critical + Lightning Warp: the teleport."),
 77: L("Thaumaturgic Generator, Forgotten Warden, Time-Lost Jewel de crítico.", "Thaumaturgic Generator, Forgotten Warden, crit Time-Lost Jewel."),
 80: L("4ª ascendência: Runic Meridians.", "4th ascendancy: Runic Meridians."),
 85: L("50% de crítico: Elemental Armament II no Oil Barrage.", "50% crit: Elemental Armament II on Oil Barrage."),
 93: L("Rakiata's Flow + Headhunter.", "Rakiata's Flow + Headhunter."),
}

ASCENDANCY = [
 dict(order=1, key="mountain", node="Way of the Mountain", when=L("1º Trial (~nível 25)", "1st Trial (~level 25)"), text=L("Chance (Surpassing) de ganhar Mountain's Teachings ao imobilizar inimigos, até 30; perde uma ao ser atingido ou ao usar ataque que se beneficia delas.", "Surpassing chance to gain Mountain's Teachings when immobilising enemies, up to 30; lose one when hit or when using an attack that benefits from them."), why=L("Freeze e Heavy Stun (sinos) imobilizam: bônus constante.", "Freeze and Heavy Stun (bells) immobilise: a constant bonus.")),
 dict(order=2, key="hollow", node="Hollow Focus Technique", when=L("2º Trial (~nível 40)", "2nd Trial (~level 40)"), text=L("Concede Hollow Focus: sinos aparecem perto de você; acertar cria onda de choque. Acertos nos sinos são sempre críticos e eles podem sofrer Cull.", "Grants Hollow Focus: bells spawn near you; hitting them creates a shockwave. Hits on bells are always critical and bells can be Culled."), why=L("Obrigatório: Devour nos sinos = Power Charges; críticos garantidos = Cast on Critical.", "Mandatory: Devour on bells = Power Charges; guaranteed crits = Cast on Critical.")),
 dict(order=3, key="stonefist", node="Way of the Stonefist", when=L("3º Trial (~nível 68)", "3rd Trial (~level 68)"), text=L("Luvas viram Fists of Stone e os mods explícitos viram versões mais fortes; ignora requisitos de atributo das luvas.", "Gloves become Fists of Stone and their explicit mods become stronger versions; ignores glove attribute requirements."), why=L("Dano crítico, crítico base, velocidade e Power Charge no crítico nas luvas.", "Crit damage, base crit, speed and power charge on crit on the gloves.")),
 dict(order=4, key="meridians", node="Runic Meridians", when=L("4º Trial (~nível 80)", "4th Trial (~level 80)"), text=L("Tatua runas no corpo: sockets extras só para runas (1 capacete, 2 peito, 1 luvas, 1 botas).", "Tattoo runes on your body: extra rune-only sockets (1 helmet, 2 body armour, 1 gloves, 1 boots)."), why=L("Runas de Movement Speed, curse e recarga de ES a mais.", "Extra Movement Speed, curse and ES recharge runes.")),
]
ASC_UNLOCK = [25, 40, 68, 80]
ASC_PHASE = {"a1": [], "a2": ["Way of the Mountain"], "a3": ["Way of the Mountain", "Hollow Focus Technique"], "a4": ["Way of the Mountain", "Hollow Focus Technique"],
             "swap": ["Way of the Mountain", "Hollow Focus Technique", "Way of the Stonefist"]}

KEY_PASSIVES = [
 dict(node="Hollow Palm Technique", type="Notable", text=L("Ataca como se usasse quarterstaff com as duas mãos vazias.", "Attack as though using a quarterstaff with both hands empty."), when="13–64", why=L("Leveling sem arma; sai no respec da troca.", "Weaponless leveling; removed in the swap respec.")),
 dict(node="Overflowing Power", type="Notable", text=L("+2 Power Charges máximas.", "+2 maximum Power Charges."), when="65+", why=L("Mais combustível para o Oil Barrage (22 de 22 no ladder).", "More fuel for Oil Barrage (22 of 22 on the ladder).")),
 dict(node="Struck Through", type="Notable", text=L("Ataques com +1% de chance de crítico base.", "Attacks have +1% base crit chance."), when="65+", why=L("Crítico base = mais Cast on Critical.", "Base crit = more Cast on Critical.")),
 dict(node="Spectral Ward", type="Notable", text=L("+1 ES máximo por 12 de Evasão do peito.", "+1 max ES per 12 Evasion on the body armour."), when="75+", why=L("Defesa híbrida Evasão/ES.", "Hybrid Evasion/ES defence.")),
 dict(node="Stand and Deliver", type="Notable", text=L("Projéteis com mais dano e dano crítico a até 2 m.", "Projectiles deal more damage and crit damage within 2m."), when="75+", why=L("O Lightning Warp te coloca colado no pack.", "Lightning Warp puts you right inside the pack.")),
 dict(node="Thaumaturgic Generator", type=L("Instill", "Instill"), text=L("Ganha uma carga aleatória periodicamente (depende dos requisitos de atributo das gems).", "Gain a random charge periodically (based on your gems' attribute requirements)."), when="77+", why=L("Power Charges sem apertar botão.", "Power Charges without pressing a button.")),
]
TREE_STAGES = [
 dict(lv="1–31", focus="Flow Like Water · Hollow Palm", dmg="Glacial Cascade → Storm Wave", **{"def": L("Vida + resist", "Life + resist")}, spirit="Herald of Ice", dont=L("Quarterstaff caro", "Expensive quarterstaff")),
 dict(lv="32–64", focus=L("Elemental + Echoing", "Elemental + Echoing"), dmg="Storm Wave + heralds", **{"def": L("Evasão/ES", "Evasion/ES")}, spirit="Herald of Ice + Thunder", dont=L("Gastar o Greater Jeweller's", "Spending the Greater Jeweller's")),
 dict(lv="65–84", focus=L("Crítico + Overflowing Power", "Crit + Overflowing Power"), dmg="Oil Barrage + Lightning Warp", **{"def": "Mindful Awareness · Subterfuge Mask · Spectral Ward"}, spirit="CoC · Charge Regulation", dont=L("CoC com crítico baixo", "CoC with low crit")),
 dict(lv="85–100", focus=L("Crítico perto de 100%", "Crit close to 100%"), dmg="Rakiata's Flow", **{"def": "Enhanced Reflexes · Beastial Skin"}, spirit="+ Wind Dancer · Ghost Dance", dont=L("Rakiata's com Elemental Weakness", "Rakiata's with Elemental Weakness")),
]

UNIQUES = [
 U("Foxshade", "Body Armour", L("Armadura", "Armour"), "a1", L("+50–70 Evasão, +20–30 Destreza, 10% Movement Speed com vida cheia e 100% mais Evasão com vida cheia.", "+50–70 Evasion, +20–30 Dexterity, 10% Movement Speed on full life and 100% increased Evasion on full life."), L("Peito de nível 1: a Evasão do item vira velocidade de ataque no Hollow Palm.", "Level 1 chest: the item's Evasion becomes attack speed with Hollow Palm."), L("Peito de Evasão/ES.", "Evasion/ES chest.")),
 U("Northpaw", L("Luvas", "Gloves"), L("Armadura", "Armour"), "a1", L("Evasão, físico plano em ataques, dano crítico e mais chance de crítico base com armas.", "Evasion, flat physical to attacks, crit damage and higher base crit chance with weapons."), L("Luvas baratas de dano no Ato 1.", "Cheap Act 1 damage gloves."), L("Luvas com dano plano.", "Gloves with flat damage.")),
 U("Luminous Pace", L("Botas", "Boots"), L("Armadura", "Armour"), "a1", L("10% Movement Speed, ES e recarga de ES bem mais rápida.", "10% Movement Speed, ES and much faster ES recharge start."), L("Primeiras botas; a Wanderlust substitui no 11.", "First boots; Wanderlust replaces them at 11."), L("Botas com Movement Speed.", "Boots with Movement Speed.")),
 U("Pillar of the Caged God", "Quarterstaff", L("Arma", "Weapon"), "a1", L("Área por Inteligência, velocidade de ataque por Destreza e dano da arma por Força.", "Area per Intelligence, attack speed per Dexterity and weapon damage per Strength."), L("Quarterstaff de nível 1 que cresce com os atributos; serve até o Hollow Palm no 13.", "Level 1 quarterstaff that grows with attributes; lasts until Hollow Palm at 13."), L("Quarterstaff magic/rare com DPS.", "Magic/rare quarterstaff with DPS.")),
 U("Surefooted Sigil", L("Amuleto", "Amulet"), L("Acessório", "Accessory"), "a1", L("+40–60 vida, Destreza, +1 m de Dodge Roll e evasão depois do dodge.", "+40–60 life, Dexterity, +1 m Dodge Roll and evasion after dodging."), L("Vida e mobilidade baratas no começo.", "Cheap early life and mobility."), L("Amuleto com vida.", "Amulet with life.")),
 U("Breath of the Mountains", "Charm", "Charm", "a1", L("Dá uma Power Charge ao usar.", "Grants a Power Charge on use."), L("Guarde desde já: é carga garantida quando o Oil Barrage chegar.", "Keep it from the start: a guaranteed charge once Oil Barrage arrives."), "Sapphire Charm"),
 U("Goldrim", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a2", L("+25–33% em TODAS as resistências elementais e raridade.", "+25–33% to ALL elemental resistances and rarity."), L("Resolve resistência sozinho do 10 até uns 40.", "Solves resistances by itself from 10 to about 40."), L("Capacete com vida/ES.", "Helmet with life/ES.")),
 U("Wanderlust", L("Botas", "Boots"), L("Armadura", "Armour"), "a2", L("20% Movement Speed, ES e imunidade a Slow.", "20% Movement Speed, ES and immunity to slows."), L("Dobro de velocidade das Luminous Pace.", "Double the movement of Luminous Pace."), "Gamblesprint"),
 U("Matsya", "Quarterstaff", L("Arma", "Weapon"), "a2", L("Frio e raio planos, +3–5% de crítico, 15–20% attack speed e regen de mana.", "Flat cold and lightning, +3–5% crit, 15–20% attack speed and mana regen."), L("Se cair antes do 13 (ou se o Hollow Palm estiver fraco), é mais dano que mão vazia até o Ato 2.", "If you find it before 13 (or Hollow Palm feels weak) it beats empty hands until Act 2."), L("Mãos vazias com Hollow Palm.", "Empty hands with Hollow Palm.")),
 U("Gamblesprint", L("Botas", "Boots"), L("Armadura", "Armour"), "a3", L("100–140% Evasão, raridade, Destreza, resistência a raio e movimento variável ao ser atingido.", "100–140% Evasion, rarity, Dexterity, lightning resistance and random movement speed when hit."), L("Muita Evasão de item = mais velocidade de ataque com Hollow Palm.", "Lots of item Evasion = more attack speed with Hollow Palm."), "Wanderlust"),
 U("Sierran Inheritance", "Body Armour", L("Armadura", "Armour"), "a3", L("50–79% Evasão/ES, resistência a raio e recarga de ES mais rápida (dano de hits contribui para a recarga).", "50–79% Evasion/ES, lightning resistance and faster ES recharge (hit damage contributes to recharge)."), L("Evasão e ES no mesmo item: velocidade de ataque e crítico no Hollow Palm.", "Evasion and ES on one item: attack speed and crit with Hollow Palm."), "Foxshade"),
 U("The Smiling Knight", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a3", L("150–200% Armour/Evasão, precisão e 15–25% de chance de crítico.", "150–200% Armour/Evasion, accuracy and 15–25% crit chance."), L("Primeiro capacete de crítico da build.", "The build's first crit helmet."), "Goldrim"),
 U("Idle Hands", L("Luvas", "Gloves"), L("Armadura", "Armour"), "a4", L("40–60% Evasão, precisão, Inteligência e 25% de attack speed com mana cheia.", "40–60% Evasion, accuracy, Intelligence and 25% attack speed on full mana."), L("Velocidade de ataque grátis enquanto a mana estiver cheia — combina com o Hollow Palm.", "Free attack speed while your mana is full — pairs with Hollow Palm."), "Northpaw"),
 U("The Dancing Mirage", "Body Armour", L("Armadura", "Armour"), "a4", L("150–200% Evasão/ES, resistência a raio, 20% less dano tomado se não foi atingido e Evasão dobrada em movimento.", "150–200% Evasion/ES, lightning resistance, 20% less damage taken if not hit recently and doubled Evasion while moving."), L("O melhor peito de campanha: defesa e, com Hollow Palm, velocidade e crítico.", "The best campaign chest: defence and, with Hollow Palm, speed and crit."), "Sierran Inheritance"),
 U("Atsak's Sight", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a4", L("Evasão/ES dobrada, +30–40% de chance de crítico, Destreza e Inteligência.", "Doubled Evasion/ES, +30–40% crit chance, Dexterity and Intelligence."), L("Crítico e ES para o Cast on Critical que vem nos mapas.", "Crit and ES for the Cast on Critical that arrives in maps."), "The Smiling Knight"),
 U("Beacon of Azis", L("Amuleto", "Amulet"), L("Acessório", "Accessory"), "a4", L("+60–99 mana, +30 Spirit e críticos ignoram a resistência elemental dos monstros.", "+60–99 mana, +30 Spirit and critical hits ignore monster elemental resistances."), L("Todo o dano da build é elemental: crítico ignorando resistência é dano puro, e ainda dá Spirit.", "All the build's damage is elemental: crits ignoring resistance is pure damage, and it grants Spirit too."), L("Amuleto com Spirit.", "Amulet with Spirit.")),
 U("Breath of the Mountains", "Charm", "Charm", "swap", L("Dá uma Power Charge ao usar.", "Grants a Power Charge on use."), L("Carga extra barata na troca para Oil Barrage.", "Cheap extra charge at the Oil Barrage swap."), "Sapphire Charm"),
 U("Forgotten Warden", "Body Armour", L("Armadura", "Armour"), "maps", L("Deflection por ES faltando, Evasão/ES alta; parte do dano de hits desviados vai para a vida do companion.", "Deflection per missing ES, high Evasion/ES; part of deflected hit damage goes to your companion's life."), L("Defesa principal do planner (9 de 22 no ladder).", "The planner's main defence (9 of 22 on the ladder)."), L("Peito Evasão/ES com Spirit.", "Evasion/ES chest with Spirit.")),
 U("Myris Uxor", L("Capacete", "Helmet"), L("Armadura", "Armour"), "maps", L("Evasão, precisão, mana e 100% de limite de Cull.", "Evasion, accuracy, mana and 100% increased Cull threshold."), L("Limite de Cull maior = o Lightning Warp explode alvos mais cedo (7 de 22 no ladder).", "Higher Cull threshold = Lightning Warp explodes targets sooner (7 of 22 on the ladder)."), L("Capacete de ES.", "ES helmet.")),
 U("Alpha's Howl", L("Capacete", "Helmet"), L("Armadura", "Armour"), "maps", L("+100 Spirit, Evasão, resistência a frio e Presence dobrada.", "+100 Spirit, Evasion, cold resistance and doubled Presence."), L("Resolve o Spirit do Cast on Critical de uma vez.", "Solves Cast on Critical's Spirit in one go."), "Myris Uxor"),
 U("Ingenuity", L("Cinto", "Belt"), L("Acessório", "Accessory"), "maps", L("Bônus maiores dos anéis equipados.", "Increased bonuses from equipped rings."), L("Cinto do planner com anéis de dano plano.", "Planner belt with flat damage rings."), L("Cinto rare com vida.", "Rare life belt.")),
 U("Nascent Hope", "Charm", "Charm", "endgame", L("Recarga de ES ao usar; chance de carga ao matar.", "ES recharge on use; charge chance on kill."), L("Defesa de ES e cargas.", "ES defence and charges."), "Thawing Charm"),
 U("Lavianga's Spirits", L("Flask de mana", "Mana flask"), "Flask", "endgame", L("Efeito constante (sem usar), recuperação menor.", "Constant effect (never used), lower recovery."), L("Mana contínua para o Lightning Warp.", "Continuous mana for Lightning Warp."), L("Flask de mana normal.", "Normal mana flask.")),
 U("Heart of the Well", "Jewel", "Jewel", "endgame", L("Dano como extra de fogo/frio/raio e dano crítico.", "Damage as extra fire/cold/lightning and crit damage."), L("Jewel barato de dano (13 de 22 no ladder).", "Cheap damage jewel (13 of 22 on the ladder)."), L("Jewel rare de crítico.", "Rare crit jewel.")),
 U("Rite of Passage", "Charm", "Charm", "max", L("Possessão por espíritos (Stag, Cat, Wolf...).", "Spirit possession (Stag, Cat, Wolf...)."), L("Prioridade do havoc616: Stag > Cat > Wolf > Owl > Bear.", "havoc616's priority: Stag > Cat > Wolf > Owl > Bear."), "The Fall of the Axe"),
 U("Kalandra's Touch", L("Anel", "Ring"), L("Acessório", "Accessory"), "max", L("Reflete o anel oposto.", "Reflects the opposite ring."), L("Duplica um anel de dano plano perfeito.", "Duplicates a perfect flat damage ring."), L("Anel rare de dano plano.", "Rare flat damage ring.")),
 U("Headhunter", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Ao matar rare, ganha os mods dele por 60 s.", "Killing a rare grants its modifiers for 60 s."), L("Cinto do Aspirational do planner.", "The planner's Aspirational belt."), "Ingenuity"),
]
GEAR = [
 dict(slot="Talisman", cheap=L("Pillar of the Caged God → mãos vazias (13)", "Pillar of the Caged God → empty hands (13)"), value=L("Spiny Talisman 300–380 EDPS", "300–380 EDPS Spiny Talisman"), full=L("490+ EDPS, 15%+ crítico, + níveis, attack speed", "490+ EDPS, 15%+ crit, + levels, attack speed"), affix=L("Fogo/frio/raio plano; % elemental com ataques; crítico; +3 ataques (Perfect Essence of Battle)", "Flat fire/cold/lightning; % elemental attack damage; crit; +3 attacks (Perfect Essence of Battle)"), lvls=[dict(lv=1, n="Pillar of the Caged God"), dict(lv=13, n=L("Mãos vazias (Hollow Palm)", "Empty hands (Hollow Palm)")), dict(lv=65, n=L("Spiny Talisman 300+ EDPS", "300+ EDPS Spiny Talisman")), dict(lv=77, n=L("Spiny Talisman 380+ EDPS", "380+ EDPS Spiny Talisman")), dict(lv=85, n=L("Spiny Talisman 490+ EDPS", "490+ EDPS Spiny Talisman"))], note=TALISMAN_RUNES),
 dict(slot=L("Luvas (Fists of Stone)", "Gloves (Fists of Stone)"), cheap="Northpaw (1) · Idle Hands (28)", value=L("Runeforged Fists of Stone: dano crítico + attack speed", "Runeforged Fists of Stone: crit damage + attack speed"), full=L("Dano crítico, attack speed e Power Charge no crítico", "Crit damage, attack speed and Power Charge on crit"), affix=L("Dano crítico → crítico base; attack speed → Onslaught; dano plano → dano extra; defesa → more Evasão/ES", "Crit damage → base crit; attack speed → Onslaught; flat damage → extra damage; defence → more Evasion/ES"), lvls=[dict(lv=1, n="Northpaw"), dict(lv=28, n="Idle Hands"), dict(lv=68, n=L("Runeforged Fists of Stone", "Runeforged Fists of Stone"))], note=L("Runeforge na Verisium Anvil para a Refutation.", "Runeforge at the Verisium Anvil for Refutation.")),
 dict(slot=L("Amuleto", "Amulet"), cheap="Surefooted Sigil · Beacon of Azis (30)", value=L("Rare +50 Spirit + Thaumaturgic Generator", "Rare +50 Spirit + Thaumaturgic Generator"), full=L("Absent Amulet: Spirit, +3 projéteis, instill", "Absent Amulet: Spirit, +3 projectiles, instill"), affix=L("Spirit; + projéteis; crítico; ES", "Spirit; + projectiles; crit; ES"), lvls=[dict(lv=8, n="Surefooted Sigil"), dict(lv=30, n="Beacon of Azis"), dict(lv=75, n=L("Rare +50 Spirit (Thaumaturgic Generator)", "Rare +50 Spirit (Thaumaturgic Generator)"))], note=L("Instill: Thaumaturgic Generator (ou Zarokh's Gift no Aspirational).", "Instill: Thaumaturgic Generator (or Zarokh's Gift in Aspirational).")),
 dict(slot=L("Capacete", "Helmet"), cheap="Goldrim (10) · The Smiling Knight (26)", value="Atsak's Sight · Myris Uxor · Alpha's Howl", full=L("Ancestral Tiara: ES alto + Raven-Touched Shard", "Ancestral Tiara: high ES + Raven-Touched Shard"), affix=L("% ES; ES plano; vida", "% ES; flat ES; life"), lvls=[dict(lv=10, n="Goldrim"), dict(lv=26, n="The Smiling Knight"), dict(lv=30, n="Atsak's Sight"), dict(lv=75, n="Myris Uxor"), dict(lv=85, n=L("Ancestral Tiara (ES)", "Ancestral Tiara (ES)"))], note=L("Instill Thaumaturgic Generator no capacete quando o amuleto usar Zarokh's Gift.", "Thaumaturgic Generator instill on the helmet once the amulet uses Zarokh's Gift.")),
 dict(slot="Body Armour", cheap="Foxshade · Sierran Inheritance (16)", value="The Dancing Mirage (28)", full=L("Forgotten Warden bem rolado · Sleek Jacket +50 Spirit (mapa)", "Well-rolled Forgotten Warden · +50 Spirit Sleek Jacket (mapping)"), affix=L("% Evasão/ES; Spirit", "% Evasion/ES; Spirit"), lvls=[dict(lv=1, n="Foxshade"), dict(lv=16, n="Sierran Inheritance"), dict(lv=28, n="The Dancing Mirage"), dict(lv=77, n="Forgotten Warden")], note=L("Greater Iron Rune ×2 · Rune of Foundations.", "Greater Iron Rune ×2 · Rune of Foundations.")),
 dict(slot=L("Botas", "Boots"), cheap="Luminous Pace · Wanderlust · Gamblesprint", value=L("Rare: 30% MS + Evasão/ES", "Rare: 30% MS + Evasion/ES"), full=L("Drakeskin Boots 35% MS + Deflection", "35% MS Drakeskin Boots + Deflection"), affix=L("MS; Evasão; Deflection; resist", "MS; Evasion; Deflection; resist"), lvls=[dict(lv=1, n="Luminous Pace"), dict(lv=11, n="Wanderlust"), dict(lv=16, n="Gamblesprint"), dict(lv=60, n=L("Rare: 30–35% MS", "Rare: 30–35% MS"))], note=L("Farrul's Rune of the Chase na tatuagem.", "Farrul's Rune of the Chase as a tattoo.")),
 dict(slot=L("Anéis", "Rings"), cheap=L("Anéis com dano elemental plano", "Rings with flat elemental damage"), value=L("Prismatic Ring: frio/raio plano + resist", "Prismatic Ring: flat cold/lightning + resist"), full=L("Físico + raio plano + raridade · Kalandra's Touch", "Flat physical + lightning + rarity · Kalandra's Touch"), affix=L("Dano plano em ataques; raridade; resist", "Flat attack damage; rarity; resist"), lvls=[dict(lv=1, n=L("Anéis com dano elemental plano", "Rings with flat elemental damage")), dict(lv=60, n=L("Prismatic Ring: frio/raio + resist", "Prismatic Ring: cold/lightning + resist")), dict(lv=85, n=L("Gold Ring: dano plano + raridade", "Gold Ring: flat damage + rarity"))], note=""),
 dict(slot=L("Cinto", "Belt"), cheap=L("Cinto com vida e resistências", "Belt with life and resistances"), value="Ingenuity", full="Headhunter", affix=L("Vida; charm slots", "Life; charm slots"), lvls=[dict(lv=1, n=L("Cinto com vida", "Belt with life")), dict(lv=75, n="Ingenuity"), dict(lv=93, n="Headhunter")], note=""),
 dict(slot="Charms / Flasks", cheap="Breath of the Mountains · Nascent Hope", value="Lavianga's Spirits", full="Rite of Passage", affix="", lvls=[dict(lv=5, n="Breath of the Mountains"), dict(lv=12, n="Nascent Hope"), dict(lv=85, n="Lavianga's Spirits"), dict(lv=93, n="Rite of Passage")], note=""),
]
BUY_ORDER = [
 dict(p=1, item="Foxshade · Northpaw · Luminous Pace", phase="1+", cost=L("Barato", "Cheap"), impact=L("Evasão = attack speed no Hollow Palm", "Evasion = attack speed with Hollow Palm")),
 dict(p=2, item="Goldrim · Wanderlust", phase="10–11", cost=L("Barato", "Cheap"), impact=L("Resistências e velocidade", "Resistances and speed")),
 dict(p=3, item="The Dancing Mirage · Idle Hands", phase="28+", cost=L("Barato", "Cheap"), impact=L("Defesa, attack speed e crítico", "Defence, attack speed and crit")),
 dict(p=4, item="Beacon of Azis", phase="30+", cost=L("Barato", "Cheap"), impact=L("Crítico ignora resistência", "Crits ignore resistance")),
 dict(p=5, item=L("Spiny Talisman 300+ EDPS", "300+ EDPS Spiny Talisman"), phase="65", cost=L("Valor", "Value"), impact=L("Libera a troca", "Unlocks the swap")),
 dict(p=6, item=L("Amuleto +50 Spirit", "+50 Spirit amulet"), phase="75", cost=L("Valor", "Value"), impact=L("Cast on Critical (teleporte)", "Cast on Critical (teleport)")),
 dict(p=7, item="Forgotten Warden", phase="77", cost=L("Barato", "Cheap"), impact=L("Sobrevivência", "Survival")),
 dict(p=8, item=L("Thaumaturgic Generator (instill)", "Thaumaturgic Generator (instill)"), phase="77", cost=L("Valor", "Value"), impact="Power Charges"),
 dict(p=9, item=L("Time-Lost Jewel de crítico", "Crit Time-Lost Jewel"), phase="77", cost=L("Valor", "Value"), impact=L("Crítico → mais teleporte", "Crit → more teleport")),
 dict(p=10, item=L("Luvas com dano crítico + Power Charge no crítico", "Gloves with crit damage + Power Charge on crit"), phase="85", cost=L("Luxo", "Luxury"), impact=L("Cargas automáticas", "Automatic charges")),
 dict(p=11, item="Rakiata's Flow · Headhunter", phase="93", cost=L("Luxo", "Luxury"), impact="Min-max"),
]

TRICKS = [
 {"cat": L("Teleporte", "Teleport"), "lvl": L("Fácil", "Easy"), "title": L("Não mire o teleporte", "Don't aim the teleport"), "body": L("O Lightning Warp é disparado pelo Cast on Critical: você só canaliza o Oil Barrage na direção do pack. Cada crítico enche a energia e o Warp escolhe um alvo no Cull. Andar entre packs continua sendo com Pounce/Dodge Roll.", "Lightning Warp is triggered by Cast on Critical: you just channel Oil Barrage towards the pack. Every crit fills Energy and Warp picks a cullable target. Moving between packs is still Pounce/Dodge Roll.")},
 {"cat": L("Cargas", "Charges"), "lvl": L("Fácil", "Easy"), "title": L("Sino = primeira carga", "Bell = first charge"), "body": L("Sinos do Hollow Focus podem sofrer Cull: Devour neles dá Power Charge mesmo sem monstro por perto. Comece todo mapa assim.", "Hollow Focus bells can be Culled: Devouring them grants Power Charges even with no monsters around. Start every map this way.")},
 {"cat": L("Crítico", "Crit"), "lvl": L("Médio", "Medium"), "title": L("Sinos são sempre críticos", "Bells are always crit"), "body": L("Acertos em sinos são SEMPRE críticos: com crítico baixo, canalize o Oil Barrage passando pelos sinos para encher o Cast on Critical.", "Hits on bells are ALWAYS critical: with low crit, channel Oil Barrage through the bells to fill Cast on Critical.")},
 {"cat": L("Cull", "Cull"), "lvl": L("Médio", "Medium"), "title": L("Mais Cull, mais teleporte", "More Cull, more teleport"), "body": L("Myris Uxor (100% de limite de Cull), o instill Bounty Hunter (25%) e Culling Strike II aumentam a vida em que o inimigo vira alvo do Warp: teleportes mais cedo em cada pack.", "Myris Uxor (100% Cull threshold), the Bounty Hunter instill (25%) and Culling Strike II raise the life at which enemies become Warp targets: earlier teleports in every pack.")},
 {"cat": "Spirit", "lvl": L("Fácil", "Easy"), "title": L("Alpha's Howl", "Alpha's Howl"), "body": L("O capacete dá +100 de Spirit sozinho — o Cast on Critical inteiro. Ótimo enquanto o amuleto e o peito com Spirit não chegam.", "The helmet grants +100 Spirit by itself — a whole Cast on Critical. Great until your Spirit amulet and chest arrive.")},
 {"cat": L("Mana", "Mana"), "lvl": L("Médio", "Medium"), "title": L("Mana do Lightning Warp", "Lightning Warp mana"), "body": L("Cada Warp custa mana. Fluke devolve parte do custo, Soul Drain dá mana a cada Cull e Lavianga's Spirits recupera sem parar. Sem isso o teleporte para no meio do mapa.", "Every Warp costs mana. Fluke refunds part of the cost, Soul Drain grants mana on every Cull and Lavianga's Spirits recovers nonstop. Without it the teleport stops mid-map.")},
 {"cat": L("Gems", "Gems"), "lvl": L("Fácil", "Easy"), "title": L("Nova Projectiles I, não II", "Nova Projectiles I, not II"), "body": L("Segundo o havoc616, colocar Nova Projectiles II impede de encaixar todas as gems da build. Fique na I.", "According to havoc616, socketing Nova Projectiles II stops you from socketing all the build's gems. Stay on I.")},
 {"cat": L("Boss", "Boss"), "lvl": L("Médio", "Medium"), "title": L("Refutation só no boss", "Refutation only on bosses"), "body": L("A Refutation bloqueia tudo, mas bloquear dano demais causa Heavy Stun. No clear, não use. Precisa de Runeforged Fists of Stone (Verisium Anvil) para ter Runic Ward.", "Refutation blocks everything, but blocking too much damage causes Heavy Stun. Don't use it while clearing. Needs Runeforged Fists of Stone (Verisium Anvil) for Runic Ward.")},
 {"cat": L("Campanha", "Campaign"), "lvl": L("Fácil", "Easy"), "title": L("Greater Jeweller's do Ato 4", "Act 4 Greater Jeweller's"), "body": L("O Ato 4 dá um Greater Jeweller's Orb garantido. Guarde para o Oil Barrage e troque mais cedo.", "Act 4 grants a guaranteed Greater Jeweller's Orb. Save it for Oil Barrage and swap sooner.")},
]

TROUBLESHOOT = [
 (L("Oil Barrage só cospe óleo", "Oil Barrage only spits oil"), L("Sem Power Charge. Devour num sino ou corpo; confira Overflowing Power, Thaumaturgic Generator e Breath of the Mountains.", "No Power Charges. Devour a bell or corpse; check Overflowing Power, Thaumaturgic Generator and Breath of the Mountains.")),
 (L("O Oil Barrage não dá crítico nenhum", "Oil Barrage never crits"), L("Na ordem: (1) você tem Hollow Focus Technique e está canalizando em cima dos sinos? acerto em sino é crítico garantido; (2) seu Talisman tem o sufixo '+X% to Critical Hit Chance' e é base Spiny? sem isso você fica em ~5%; (3) Pinpoint Critical está no Oil Barrage?; (4) você alocou o cluster de crítico no respec do 65 (Struck Through, True Strike, For the Jugular, Heartbreaking, Heartstopping)?; (5) capacete The Smiling Knight ou Atsak's Sight. E lembre: sem Power Charge o Oil Barrage nem chega a disparar a rajada — ele só cospe óleo.", "In order: (1) do you have Hollow Focus Technique and are you channeling across the bells? a hit on a bell is a guaranteed crit; (2) does your Talisman have the '+X% to Critical Hit Chance' suffix on a Spiny base? without it you sit at ~5%; (3) is Pinpoint Critical socketed in Oil Barrage?; (4) did you allocate the crit cluster in the level 65 respec (Struck Through, True Strike, For the Jugular, Heartbreaking, Heartstopping)?; (5) The Smiling Knight or Atsak's Sight helmet. And remember: with no Power Charge Oil Barrage never fires the barrage at all — it only spits oil.")),
 (L("Não sei o que colocar em cada Weapon Set", "I don't know what goes in each Weapon Set"), L("Set 1: só o Spiny Talisman — é onde a build inteira mora. Set 2: na campanha, o Changeling Talisman para o Pounce; depois da troca do 65 ele serve só para os pontos de Weapon Set (nós de Parry da Refutation) e você pode deixá-lo vazio. Você joga sempre no Set 1.", "Set 1: just the Spiny Talisman — the whole build lives there. Set 2: in the campaign, the Changeling Talisman for Pounce; after the level 65 swap it only serves the Weapon Set points (Refutation's Parry nodes) and can stay empty. You always play on Set 1.")),
 (L("Não teleporta", "No teleport"), L("Cast on Critical sem Spirit (100) ou crítico baixo. Canalize nos sinos (sempre críticos), use Pinpoint Critical e busque 50% de crítico.", "Cast on Critical without Spirit (100) or low crit. Channel on bells (always crit), use Pinpoint Critical and aim for 50% crit.")),
 (L("Teleporta e para no meio do mapa", "Teleports then stops mid-map"), L("Falta mana: Fluke e Soul Drain no Cast on Critical, Lavianga's Spirits e mana ao matar.", "Out of mana: Fluke and Soul Drain on Cast on Critical, Lavianga's Spirits and mana on kill.")),
 (L("Pouco dano no boss", "Low boss damage"), L("Rend e Devour ativos? Hand of Chayula aplicada? Frost Bomb/Elemental Weakness (sem Rakiata's)? Talisman abaixo de 300 EDPS é o gargalo mais comum.", "Rend and Devour buffs active? Hand of Chayula applied? Frost Bomb/Elemental Weakness (without Rakiata's)? A Talisman under 300 EDPS is the most common bottleneck.")),
 (L("Morro na campanha", "Dying in the campaign"), L("Vida e resistências primeiro; Wave of Frost congela o boss. Pounce é seu Dodge extra.", "Life and resistances first; Wave of Frost freezes the boss. Pounce is your extra dodge.")),
 (L("Refutation não funciona", "Refutation doesn't work"), L("Luvas sem Runic Ward: transforme em Runeforged Fists of Stone na Verisium Anvil.", "Gloves without Runic Ward: turn them into Runeforged Fists of Stone at the Verisium Anvil.")),
]

ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Talisman 300+ EDPS · troca feita", "300+ EDPS Talisman · swap done"), gear="Spiny Talisman"),
 dict(stage="T1–T10", goal=L("Cast on Critical + Lightning Warp · Stonefist", "Cast on Critical + Lightning Warp · Stonefist"), gear=L("Amuleto +50 Spirit · Forgotten Warden", "+50 Spirit amulet · Forgotten Warden")),
 dict(stage="T11–T15", goal=L("50% de crítico · Runic Meridians", "50% crit · Runic Meridians"), gear=L("Time-Lost Jewel · Talisman 490 EDPS", "Time-Lost Jewel · 490 EDPS Talisman")),
 dict(stage="Pinnacle", goal=L("Rakiata's Flow", "Rakiata's Flow"), gear="Headhunter · Rite of Passage"),
]

CRAFT = [
 L("Talisman: Transmutation/Augmentation em base Normal; se sair um dano elemental plano, Regal; acima de 300 EDPS vale Perfect Essence of Battle (+3 nível de ataques).", "Talisman: Transmutation/Augmentation on a Normal base; if you hit flat elemental damage, Regal; above 300 EDPS it's worth a Perfect Essence of Battle (+3 attack levels)."),
 L("Amuleto: instill Thaumaturgic Generator (carga aleatória periódica). Se trocar de amuleto, faça de novo.", "Amulet: Thaumaturgic Generator instill (periodic random charge). If you change amulets, redo it."),
 L("Luvas: Way of the Stonefist transforma os mods; depois Runeforge na Verisium Anvil para a Refutation.", "Gloves: Way of the Stonefist transforms the mods; then Runeforge at the Verisium Anvil for Refutation."),
]

T("item", "Spiny Talisman", 65, L("Talisman 300+ EDPS", "300+ EDPS Talisman"), L("Primeiros mapas.", "First maps."), L("Libera o Oil Barrage.", "Unlocks Oil Barrage."), L("Antes disso a Storm Wave é mais forte.", "Before that Storm Wave is stronger."), "—")
T("asc", "Hollow Focus Technique", 40, L("2º Trial", "2nd Trial"), L("Assim que possível.", "As soon as possible."), L("Sinos: críticos e Power Charges.", "Bells: crits and Power Charges."), "—", "—")
T("skill", "Cast on Critical", 75, L("100 de Spirit", "100 Spirit"), L("Com amuleto +50 Spirit ou Alpha's Howl.", "With a +50 Spirit amulet or Alpha's Howl."), L("O teleporte do Lightning Warp.", "Lightning Warp's teleport."), L("Com crítico baixo quase não dispara.", "With low crit it barely triggers."), "—")
T("asc", "Way of the Stonefist", 68, L("3º Trial", "3rd Trial"), L("Na troca.", "At the swap."), L("Luvas muito mais fortes.", "Much stronger gloves."), "—", "—")
T("item", "Forgotten Warden", 1, L("Confira o nível no item", "Check the level on the item"), L("Mapas.", "Maps."), L("Deflection e companion tomando dano.", "Deflection and a companion taking damage."), "—", L("Peito Evasão/ES.", "Evasion/ES chest."))
T("skill", "Rakiata's Flow", 93, L("Lineage", "Lineage"), L("Aspiracional.", "Aspirational."), L("Resistências invertidas.", "Inverted resistances."), L("Conflita com Elemental Weakness.", "Conflicts with Elemental Weakness."), "—")

CASES = [
 (L("E se eu quiser a variante do topo do ladder?", "What about the top-of-ladder variant?"), L("O Martial Artist de Oil Barrage com mais DPS no ladder usa Martial Adept + Martial Master no lugar de Hollow Focus Technique e Way of the Mountain, com Blasphemy + Ailith's Chimes para as cargas e Chaos Inoculation. É mais cara; este guia segue os sinos do planner, que resolvem cargas e críticos com pouco investimento.", "The highest-DPS Oil Barrage Martial Artist on the ladder uses Martial Adept + Martial Master instead of Hollow Focus Technique and Way of the Mountain, with Blasphemy + Ailith's Chimes for charges and Chaos Inoculation. It's pricier; this guide follows the planner's bells, which solve charges and crits with little investment.")),
 (L("Sem Talisman de 300 EDPS no nível 65", "No 300 EDPS Talisman at level 65"), L("Continue com Storm Wave nos mapas baixos (a build de campanha aguenta) e troque quando tiver o Talisman.", "Keep Storm Wave in low maps (the campaign build holds up) and swap once you have the Talisman.")),
 (L("Só 100 de Spirit", "Only 100 Spirit"), L("Escolha: Cast on Critical sozinho (teleporte, sem buffs) ou Charge Regulation + Wind Dancer + Ghost Dance (defesa). Alpha's Howl resolve os dois.", "Pick: Cast on Critical alone (teleport, no buffs) or Charge Regulation + Wind Dancer + Ghost Dance (defence). Alpha's Howl solves both.")),
]

SOURCES = [
 dict(name="havoc616 — Oil Barrage Martial Artist (Maxroll planner)", use=L("Leveling passo a passo, árvores, itens, rotações e notas (Campaign, Maps, Endgame, Aspirational)", "Step-by-step leveling, trees, items, rotations and notes (Campaign, Maps, Endgame, Aspirational)"), url=PLANNER_URL),
 dict(name="Maxroll — Oil Barrage Martial Artist Build Guide", use=L("Metas de equipamento, prós e contras", "Gear goals, pros and cons"), url=GUIDE_URL),
 dict(name="poe.ninja — Martial Artist · Oil Barrage + Lightning Warp (Forbidden Rites)", use=L("22 personagens nível 81–97: setup do Cast on Critical, Spirit, uniques e ascendência", "22 level 81–97 characters: Cast on Critical setup, Spirit, uniques and ascendancy"), url=NINJA_URL),
 dict(name="Path of Building (PoE2)", use=L("Descrições das gems, custos de Spirit e textos de mods", "Gem descriptions, Spirit costs and mod texts"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name="RePoE2", use=L("Nomes e ícones das bases e gems", "Base and gem names and icons"), url="https://repoe-fork.github.io/poe2/"),
]
FIXES = [
 L("O planner usa Whirling Assault + Tempest Bell no boss. Aqui esses dois saem e o espaço vai para Cast on Critical + Lightning Warp — o setup de 18 dos 22 Martial Artists de Oil Barrage + Lightning Warp do poe.ninja (os outros 4 disparam o Warp com Cast on Elemental Ailment) e o que faz o teleporte.", "The planner uses Whirling Assault + Tempest Bell on bosses. Here both are removed and the slot goes to Cast on Critical + Lightning Warp — the setup on 18 of the 22 Oil Barrage + Lightning Warp Martial Artists on poe.ninja (the other 4 trigger Warp with Cast on Elemental Ailment) and what makes the teleport."),
 L("As fases dos Atos 1–4 são cortes da ordem real de alocação do planner (pontos 17, 34, 47 e 72); as gems de cada fase seguem os passos Act 1, Act 2, Act 3 e Act 5 do planner.", "The Act 1–4 phases are cuts of the planner's real allocation order (points 17, 34, 47 and 72); each phase's gems follow the planner's Act 1, Act 2, Act 3 and Act 5 steps."),
 L("O planner coloca as 4 ascendências nos mapas; o app mostra só o que os Trials liberam em cada fase (2 pontos por Trial).", "The planner shows all 4 ascendancies in maps; the app only shows what the Trials unlock in each phase (2 points per Trial)."),
 L("Blasphemy e Spirit Vessel reservam Spirit conforme a curse/companion e não estão nos dados: confira no jogo.", "Blasphemy and Spirit Vessel reserve Spirit based on the curse/companion and aren't in the data: check in game."),
 L("Muitos personagens do poe.ninja aparecem com Spirit negativo no Path of Building porque alternam buffs. As contas de Spirit daqui usam só o que cabe ligado ao mesmo tempo.", "Many poe.ninja characters show negative Spirit in Path of Building because they toggle buffs. The Spirit math here only uses what fits active at once."),
]

UI = dict(
 carry=r"^(Oil Barrage|Storm Wave|Glacial Cascade|Cast on Critical)$", box=L("CHAVE", "KEY"), spiritWhat=L("(buffs e Cast on Critical)", "(buffs and Cast on Critical)"),
 mechBtn=L("Abrir Teleporte & Cargas", "Open Teleport & Charges"), dmg2="Lightning Warp", dmgBar=L("Oil Barrage / explosões do Lightning Warp (aprox.)", "Oil Barrage / Lightning Warp explosions (approx.)"),
 dmgLegend=L("Explosões do Lightning Warp (proporção aproximada)", "Lightning Warp explosions (approximate ratio)"),
 earlyGone=L("Quarterstaff Strike já saiu: passou do nível {u}.", "Quarterstaff Strike is gone: you're past level {u}."),
 earlyNote=L("Só no começo; sai no nível ~{u}.", "Early only; leaves around level {u}."),
 treeIntro=L("Árvore real do planner do havoc616. Campanha: Hollow Palm e elemental. Mapas: crítico, Power Charges e Evasão/ES.", "Real tree from havoc616's planner. Campaign: Hollow Palm and elemental. Maps: crit, Power Charges and Evasion/ES."),
 set1=L("dano de ataque", "attack damage"), set2=L("Parry (Refutation)", "Parry (Refutation)"), asc="Martial Artist", cls="Monk",
 respecTip=L("Na troca para Oil Barrage (65) o respec é grande: tire Hollow Palm e os nós de gelo e compare com a fase anterior.", "At the Oil Barrage swap (65) the respec is big: remove Hollow Palm and the ice nodes and compare with the previous phase."),
 routeIntro=L("Oito fases: Glacial Cascade no Ato 1, Storm Wave e Freeze de boss, heralds e sinos, fim da campanha, troca para Oil Barrage, o teleporte nos mapas, crítico no endgame e Rakiata's Flow.", "Eight phases: Glacial Cascade in Act 1, Storm Wave and boss Freeze, heralds and bells, end of campaign, Oil Barrage swap, the teleport in maps, crit in endgame and Rakiata's Flow."),
 socketPrio=["Oil Barrage", "Cast on Critical", "Devour", "Rend", "Hollow Focus", "Storm Wave"],
 permIntro=L("Nada disso volta depois. Os 100 de Spirit das quests pagam os heralds na campanha e o Cast on Critical nos mapas.", "None of this comes back later. The 100 quest Spirit pays for the heralds in the campaign and Cast on Critical in maps."),
 atlasCards=[[L("Raridade", "Rarity"), L("A meta do planner é ~150% de raridade: anéis e amuleto Gold com raridade. O clear com teleporte paga mapas juiced.", "The planner's goal is ~150% rarity: Gold rings and amulet with rarity. Teleport clear pays for juiced maps.")],
             [L("Mapas ruins", "Bad maps"), L("Reflexo elemental e 'menos crítico' matam o Cast on Critical; monstros com muita vida demoram a entrar no Cull.", "Elemental reflect and 'less crit' kill Cast on Critical; high-life monsters take longer to become cullable.")]],
 foot=L("Guia baseado no planner do havoc616 (Maxroll) e nos Martial Artists do poe.ninja, dados do Path of Building e do RePoE2 e preços do poe.ninja", "Guide based on havoc616's planner (Maxroll) and poe.ninja Martial Artists, Path of Building and RePoE2 data and poe.ninja prices"),
)

CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens, Árvore e Teleporte & Cargas se adaptam na hora. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items, Tree and Teleport & Charges tabs adapt instantly. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit máximo", "Max Spirit"), L("ex.: 150", "e.g. 150")], ["crit", L("Crítico do Oil Barrage (%)", "Oil Barrage crit (%)"), L("ex.: 45", "e.g. 45")], ["edps", L("EDPS do Talisman", "Talisman EDPS"), L("ex.: 320", "e.g. 320")]],
 tiles=[[L("Spirit reservado", "Spirit reserved"), "used"], [L("Spirit livre", "Spirit free"), "free"], [L("Crítico (%)", "Crit (%)"), "crit"]],
 buffs=[dict(key="coc", name="Cast on Critical", cost=100), dict(key="cr", name="Charge Regulation", cost=30), dict(key="wd", name="Wind Dancer", cost=30), dict(key="gd", name="Ghost Dance", cost=30),
        dict(key="hoi", name="Herald of Ice", cost=30), dict(key="hot", name="Herald of Thunder", cost=30)],
 own=[
  ["gear", "talisman", L("Talisman 300+ EDPS", "300+ EDPS Talisman")], ["gear", "runeforged", "Runeforged Fists of Stone"], ["gear", "spiritamu", L("Amuleto +50 Spirit", "+50 Spirit amulet")],
  ["gear", "thaum", "Thaumaturgic Generator"], ["gear", "Forgotten Warden", "Forgotten Warden"], ["gear", "Alpha's Howl", "Alpha's Howl"], ["gear", "Myris Uxor", "Myris Uxor"], ["gear", "Headhunter", "Headhunter"],
  ["gem", "hoi", "Herald of Ice (30)"], ["gem", "hot", "Herald of Thunder (30)"], ["gem", "oil", "Oil Barrage"], ["gem", "coc", "Cast on Critical + Lightning Warp (100)"], ["gem", "cr", "Charge Regulation (30)"],
  ["gem", "wd", "Wind Dancer (30)"], ["gem", "gd", "Ghost Dance (30)"], ["gem", "novai", "Nova Projectiles I"], ["gem", "rakiata", "Rakiata's Flow"],
  ["tree", "palm", "Hollow Palm Technique"], ["tree", "overflow", "Overflowing Power"],
  ["asc", "mountain", "Way of the Mountain"], ["asc", "hollow", "Hollow Focus Technique"], ["asc", "stonefist", "Way of the Stonefist"], ["asc", "meridians", "Runic Meridians"],
 ],
 rules=[
  dict(when=dict(lvMin=65, own=["oil"], notOwn=["hollow"]), lvl="bad", t=L("Oil Barrage sem Hollow Focus Technique", "Oil Barrage without Hollow Focus Technique"), d=L("Sem sinos não há Power Charge fácil: o Oil Barrage só cospe óleo.", "Without bells there are no easy Power Charges: Oil Barrage only spits oil."), tab="asc"),
  dict(when=dict(own=["coc"], numLt=["crit", 30]), lvl="bad", t=L("Cast on Critical com crítico baixo", "Cast on Critical with low crit"), d=L("Quase não teleporta: Pinpoint Critical, nós de crítico e canalizar nos sinos.", "Barely teleports: Pinpoint Critical, crit nodes and channeling on bells."), tab="mech"),
  dict(when=dict(own=["oil"], numLt=["edps", 300]), lvl="warn", t=L("Talisman abaixo de 300 EDPS", "Talisman under 300 EDPS"), d=L("O gargalo mais comum da troca: dano elemental plano primeiro.", "The most common swap bottleneck: flat elemental damage first."), tab="gear"),
  dict(when=dict(lvMin=65, notOwn=["talisman"]), lvl="warn", t=L("Talisman para a troca", "Talisman for the swap"), d=L("Spiny Talisman 300+ EDPS libera o Oil Barrage.", "A 300+ EDPS Spiny Talisman unlocks Oil Barrage."), tab="gear"),
  dict(when=dict(lvMin=75, own=["oil"], notOwn=["coc"]), lvl="warn", t=L("Falta o teleporte", "Missing the teleport"), d=L("Cast on Critical + Lightning Warp (100 de Spirit): amuleto +50 Spirit ou Alpha's Howl.", "Cast on Critical + Lightning Warp (100 Spirit): +50 Spirit amulet or Alpha's Howl."), tab="skills"),
  dict(when=dict(lvMin=13, lvMax=64, notOwn=["palm"]), lvl="tip", t="Hollow Palm Technique", d=L("Ataque de quarterstaff com as mãos vazias: sem gastar em arma.", "Quarterstaff attacks with empty hands: no weapon spending."), tab="arvore"),
  dict(when=dict(lvMin=70, own=["stonefist"], notOwn=["runeforged"]), lvl="tip", t="Runeforged Fists of Stone", d=L("Verisium Anvil: Runic Ward para a Refutation.", "Verisium Anvil: Runic Ward for Refutation."), tab="gear"),
  dict(when=dict(lvMin=77, own=["oil"], notOwn=["thaum"]), lvl="tip", t="Thaumaturgic Generator", d=L("Instill no amuleto: Power Charges automáticas.", "Amulet instill: automatic Power Charges."), tab="gear"),
  dict(when=dict(lvMin=65, own=["oil"], notOwn=["novai"]), lvl="tip", t="Nova Projectiles I", d=L("Use a I: a II impede de encaixar todas as gems.", "Use I: II stops you from socketing every gem."), tab="skills"),
  dict(when=dict(lvMin=42, notOwn=["hollow"]), lvl="warn", t=L("2ª ascendência pendente", "2nd ascendancy pending"), d="Hollow Focus Technique.", tab="asc"),
  dict(when=dict(lvMin=26, notOwn=["mountain"]), lvl="warn", t=L("1ª ascendência pendente", "1st ascendancy pending"), d="Way of the Mountain.", tab="asc"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["swap"], when=dict(notOwn=["talisman"]), gemsFrom="a4", note=L("Sem Talisman de 300+ EDPS: mostrando o setup de Storm Wave (troque quando tiver).", "No 300+ EDPS Talisman: showing the Storm Wave setup (swap once you have it).")),
 dict(pids=["maps", "endgame", "max"], when=dict(notOwn=["oil"]), gemsFrom="a4", note=L("Sem Oil Barrage marcado: mostrando o setup de Storm Wave.", "Oil Barrage not ticked: showing the Storm Wave setup.")),
]
TREE_RULES = [
 dict(when=dict(lvMin=65, own=["palm", "oil"]), t=L("Respec: tire Hollow Palm Technique — com Talisman equipado ele não faz nada.", "Respec: remove Hollow Palm Technique — with a Talisman equipped it does nothing."), node=None),
]
TIMING_KEY = {"Spiny Talisman": "talisman", "Hollow Focus Technique": "hollow", "Cast on Critical": "coc", "Way of the Stonefist": "stonefist", "Forgotten Warden": "Forgotten Warden", "Rakiata's Flow": "rakiata"}

MECH = dict(
 title=L("Teleporte & Cargas", "Teleport & Charges"),
 intro=L("Como o Oil Barrage teleporta: Power Charges alimentam a rajada, críticos enchem o Cast on Critical e o Lightning Warp explode quem estiver no Cull.", "How Oil Barrage teleports: Power Charges fuel the barrage, crits fill Cast on Critical and Lightning Warp explodes whoever is cullable."),
 sections=[
  dict(type="cards", cards=[
   [L("1. Power Charges", "1. Power Charges"), L("Devour num sino do Hollow Focus, corpo ou inimigo no Cull dá 1 Power Charge por alvo. Thaumaturgic Generator, Breath of the Mountains e Ailith's Chimes dão mais. Overflowing Power: +2 máximas.", "Devouring a Hollow Focus bell, corpse or cullable enemy grants 1 Power Charge per target. Thaumaturgic Generator, Breath of the Mountains and Ailith's Chimes give more. Overflowing Power: +2 maximum.")],
   [L("2. Oil Barrage", "2. Oil Barrage"), L("Wyvern: consome Power Charges para canalizar óleo elétrico. Salvo, Nova Projectiles I, Ricochet II e Fork enchem a tela de projéteis — muitos acertos, muitos críticos.", "Wyvern: consumes Power Charges to channel electrified oil. Salvo, Nova Projectiles I, Ricochet II and Fork fill the screen with projectiles — lots of hits, lots of crits.")],
   [L("3. Cast on Critical", "3. Cast on Critical"), L("Buff persistente (100 de Spirit): cada crítico gera energia (mais em monstros mais fortes); no máximo, dispara as spells encaixadas. Boundless Energy II acelera; Energy Retention devolve energia.", "Persistent buff (100 Spirit): every crit generates Energy (more on stronger monsters); at max it triggers the socketed spells. Boundless Energy II speeds it up; Energy Retention refunds Energy.")],
   [L("4. Lightning Warp", "4. Lightning Warp"), L("Teleporta você para dentro de um inimigo abaixo do Cull e o explode em raio, criando Shocked Ground. Se o alvo não está no Cull, aplica um debuff que explode quando ele entrar. Sinos também sofrem Cull.", "Teleports you inside an enemy under the Cull threshold and explodes it in lightning, creating Shocked Ground. If the target isn't cullable, it applies a debuff that explodes once it is. Bells can be Culled too.")],
  ]),
  dict(type="table", h=L("De onde vem o crítico (é isso que liga o Cast on Critical)", "Where your crit comes from (this is what switches Cast on Critical on)"),
       cols=[L("Fonte", "Source"), L("Quanto vale", "How much"), L("O que fazer", "What to do")], rows=[
   [L("Sinos do Hollow Focus", "Hollow Focus bells"), L("100%: acerto em sino é SEMPRE crítico", "100%: a hit on a bell is ALWAYS a crit"),
    L("É a 2ª ascendência (Hollow Focus Technique). Canalize o Oil Barrage POR CIMA dos sinos: mesmo com 5% de crítico no personagem, o Cast on Critical enche. Se o seu Oil Barrage 'não dá crítico nenhum', é quase sempre isto que está faltando.", "It's the 2nd ascendancy (Hollow Focus Technique). Channel Oil Barrage ACROSS the bells: even at 5% character crit, Cast on Critical fills. If your Oil Barrage 'never crits', this is almost always what's missing.")],
   [L("Talisman (sua arma)", "Talisman (your weapon)"), L("A maior parte da sua chance de crítico", "Most of your crit chance"),
    L("Oil Barrage é ATAQUE: a chance de crítico vem da arma. Use base Spiny Talisman (crítico base alto) e procure o sufixo '+X% to Critical Hit Chance' — meta 15%+ além dos 300–490 EDPS. Talisman sem esse sufixo = ~5% de crítico e o Cast on Critical praticamente não dispara.", "Oil Barrage is an ATTACK: its crit chance comes from the weapon. Use a Spiny Talisman base (high base crit) and look for the '+X% to Critical Hit Chance' suffix — 15%+ on top of 300–490 EDPS. A Talisman without that suffix = ~5% crit and Cast on Critical barely triggers.")],
   [L("Pinpoint Critical (support)", "Pinpoint Critical (support)"), L("Muito crítico a mais, menos dano por crítico", "A lot more crit, less damage per crit"),
    L("Fica no Oil Barrage até você chegar a 50% de crítico. Só depois disso troque por Elemental Armament II.", "Keep it on Oil Barrage until you reach 50% crit. Only then swap it for Elemental Armament II.")],
   [L("Árvore (respec do 65)", "Tree (the level 65 respec)"), L("Struck Through, True Strike, For the Jugular, Heartbreaking, Heartstopping", "Struck Through, True Strike, For the Jugular, Heartbreaking, Heartstopping"),
    L("Esses nós entram no respec da troca. Se você trocou para Oil Barrage e não alocou o cluster de crítico, seu crítico continua o da campanha.", "These come in with the swap respec. If you swapped to Oil Barrage and didn't allocate the crit cluster, your crit is still the campaign one.")],
   [L("Capacete", "Helmet"), L("The Smiling Knight: 15–25% · Atsak's Sight: +30–40%", "The Smiling Knight: 15–25% · Atsak's Sight: +30–40%"),
    L("Duas uniques baratas que existem só para isso. Atsak's Sight ainda dá ES para o Ghost Dance.", "Two cheap uniques that exist for exactly this. Atsak's Sight also gives ES for Ghost Dance.")],
   [L("Luvas (Fists of Stone)", "Gloves (Fists of Stone)"), L("Dano crítico e Power Charge no crítico — NÃO dão chance", "Crit damage and power charge on crit — NOT crit chance"),
    L("Não conte com elas para ligar o Cast on Critical: elas multiplicam o crítico que você já tem.", "Don't count on them to switch Cast on Critical on: they multiply the crit you already have.")],
  ]),
  dict(type="table", h=L("O que vai em cada Weapon Set (e quando trocar)", "What goes in each Weapon Set (and when to swap)"),
       cols=[L("Set", "Set"), L("O que equipar", "What to equip"), L("Para que serve", "What it's for")], rows=[
   ["Set 1", L("Spiny Talisman e mais nada (Talisman não usa offhand)", "Spiny Talisman and nothing else (a Talisman uses no offhand)"),
    L("É o set em que você joga 100% do tempo: Oil Barrage, Devour, Rend, Hollow Focus, Refutation e o Cast on Critical estão todos aqui.", "This is the set you play 100% of the time: Oil Barrage, Devour, Rend, Hollow Focus, Refutation and Cast on Critical all live here.")],
   ["Set 2", L("Campanha: Changeling Talisman (só para o Pounce). Depois da troca (65): pode ficar vazio — o planner deixa um Lunar Quarterstaff ali só por causa do setup que esta página não usa.", "Campaign: Changeling Talisman (only for Pounce). After the swap (65): it can stay empty — the planner leaves a Lunar Quarterstaff there for a setup this page doesn't use."),
    L("O Set 2 existe pelos PONTOS de Weapon Set das quests (2 por quest): eles vão nos nós de Parry, que alimentam a Refutation. Você não luta nesse set.", "Set 2 exists for the Weapon Set passive POINTS from quests (2 per quest): they go into the Parry nodes that feed Refutation. You don't fight in that set.")],
   [L("Depois do nível 65", "After level 65"), L("O Spiny Talisman já é um Talisman: o Pounce funciona no Set 1.", "The Spiny Talisman is already a Talisman: Pounce works on Set 1."),
    L("Ou seja, depois da troca você nunca mais precisa apertar X no meio da luta.", "Which means after the swap you never need to press X mid-fight again.")],
  ]),
  dict(type="table", h=L("Cadeia do teleporte", "Teleport chain"), cols=[L("Peça", "Piece"), L("O que faz", "What it does"), L("Se faltar", "If missing")], rows=[
   ["Hollow Focus Technique", L("Sinos sempre críticos e com Cull", "Always-crit, cullable bells"), L("Sem carga inicial e sem crítico garantido", "No starting charge and no guaranteed crit")],
   ["Devour", L("Power Charge por alvo devorado", "Power Charge per devoured target"), L("Oil Barrage só cospe óleo", "Oil Barrage only spits oil")],
   ["Cast on Critical", L("Energia por crítico → dispara o Warp", "Energy per crit → triggers Warp"), L("Sem teleporte", "No teleport")],
   ["Lightning Warp", L("Teleporte + explosão no Cull", "Teleport + explosion on Cull"), L("Clear normal (ainda bom)", "Normal clear (still good)")],
   ["Fluke · Soul Drain", L("Devolvem mana", "Refund mana"), L("Teleporte para sem mana", "Teleport stops without mana")],
   ["Myris Uxor · Culling Strike II", L("Limite de Cull maior", "Higher Cull threshold"), L("Teleporta mais tarde em cada pack", "Teleports later in each pack")],
  ]),
  dict(type="steps", h=L("Dia da troca (nível ~65)", "Swap day (level ~65)"), steps=[
   [L("Talisman", "Talisman"), L("Spiny Talisman com 300+ de dano elemental por segundo (crafte com Transmutation/Augmentation → Regal ou compre).", "Spiny Talisman with 300+ elemental DPS (craft with Transmutation/Augmentation → Regal or buy).")],
   [L("Gems", "Gems"), L("Uncut Skill Gem nível 14 para Oil Barrage, Devour, Rend; Greater Jeweller's Orb no Oil Barrage.", "Level 14 Uncut Skill Gems for Oil Barrage, Devour, Rend; Greater Jeweller's Orb on Oil Barrage.")],
   [L("Respec", "Respec"), L("Gold para tirar Hollow Palm e os nós de gelo; siga a fase 'Troca' na aba Árvore.", "Gold to remove Hollow Palm and the ice nodes; follow the 'Swap' phase on the Tree tab.")],
   [L("Ascendência", "Ascendancy"), L("3º Trial: Way of the Stonefist; Runeforge as luvas na Verisium Anvil.", "3rd Trial: Way of the Stonefist; Runeforge the gloves at the Verisium Anvil.")],
   [L("Spirit", "Spirit"), L("100 de quests: Charge Regulation + Wind Dancer + Ghost Dance. Com +50 de Spirit: Cast on Critical.", "100 from quests: Charge Regulation + Wind Dancer + Ghost Dance. With +50 Spirit: Cast on Critical.")],
  ]),
  dict(type="rotation", blocks=[
   [L("Clear", "Clear"), [L("Devour no sino ao entrar", "Devour the bell on entry"), L("Canalize Oil Barrage no pack", "Channel Oil Barrage into the pack"), L("Deixe o Lightning Warp teleportar", "Let Lightning Warp teleport"), L("Devour em corpos/sinos quando faltar carga", "Devour corpses/bells when charges run low"), L("Rend para o buff (opcional)", "Rend for the buff (optional)")]],
   [L("Boss", "Boss"), [L("Devour até as cargas máximas", "Devour up to max charges"), L("Rend (buff de raio)", "Rend (lightning buff)"), L("Refutation", "Refutation"), L("Hand of Chayula (marca + curse)", "Hand of Chayula (mark + curse)"), L("Oil Barrage perto dos sinos; o Warp finaliza no Cull", "Oil Barrage near the bells; Warp finishes at Cull")]],
  ]),
  dict(type="spirit", h=L("Spirit do teleporte e buffs", "Teleport and buff Spirit"), p=L("Marque o que você usa. Custos do Path of Building.", "Tick what you use. Costs from Path of Building."),
       note=L("Blasphemy e Spirit Vessel variam: confira no jogo.", "Blasphemy and Spirit Vessel vary: check in game.")),
  dict(type="timeline", h=L("Arma por nível", "Weapon by level"), items=[
   dict(lv=1, t=L("Quarterstaff do vendor", "Vendor quarterstaff"), d=L("O mais DPS possível; Artificer's Orb + Lesser Rune se sobrar.", "As much DPS as possible; Artificer's Orb + Lesser Rune if you can spare.")),
   dict(lv=6, t=L("Changeling Talisman (Set 2)", "Changeling Talisman (Set 2)"), d=L("Para o Pounce.", "For Pounce.")),
   dict(lv=13, t=L("Mãos vazias (Hollow Palm)", "Empty hands (Hollow Palm)"), d=L("Sem arma no Set 1 até a troca.", "No weapon on Set 1 until the swap.")),
   dict(lv=65, t=L("Spiny Talisman 300+ EDPS", "300+ EDPS Spiny Talisman"), d=L("Oil Barrage.", "Oil Barrage.")),
   dict(lv=77, t=L("Talisman 380+ EDPS + níveis", "380+ EDPS Talisman + levels"), d=L("10–50 Exalted ou 1–2 Divine.", "10–50 Exalted or 1–2 Divine.")),
   dict(lv=85, t=L("Talisman 490+ EDPS, 15%+ crítico", "490+ EDPS Talisman, 15%+ crit"), d=L("Endgame.", "Endgame.")),
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
        if q["boss"] == "Great White One":
            q["reward"] = L("ESCOLHA: +30% Armour, Evasion e Energy Shield (Shark Fin): Evasion e ES são a defesa da build", "CHOICE: +30% Armour, Evasion and Energy Shield (Shark Fin): Evasion and ES are the build's defence"); q["prio"] = "Alta"
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="17/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=PLANNER_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=BOOK.TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None,
                ui=UI, char=CHAR, mech=MECH, adaptSwaps=ADAPT_SWAPS, treeRules=TREE_RULES, timingKey=TIMING_KEY, phaseAct=PHASE_ACT, treeOrder=ORDER + ["uber"], craftKit=CRAFT_KIT)
