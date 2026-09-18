# -*- coding: utf-8 -*-
"""Druid · Shaman: Spark + Archmage na campanha e Comet automatizado pelo Cast on Critical nos mapas. Árvore e itens de endgame: os 10 Shamans de maior
DPS do poe.ninja (Forbidden Rites, 17/09/2026), convertidos por kit/ninja.py. Leveling, gems por nível, uniques baratas e rotações: montados aqui a partir
dos tiers e textos de gem do Path of Building, dos textos de passiva de tools/tree.json e dos preços do poe.ninja."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("shaman")

NINJA_URL = "https://poe.ninja/poe2/builds/forbiddenrites?class=Shaman&sort=dps"
POB_URL = "https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "17/09/2026"

CONFIG = dict(dir="shaman", build="shaman", store="shaman1", emoji="🌩", pill="Druid · Shaman",
              fonts="family=Cinzel+Decorative:wght@700;900&family=Cinzel:wght@500;700&family=Oxanium:wght@500;600;700&family=Exo+2:ital,wght@0,400;0,500;0,600;1,400")
TXT = {
 "pt": dict(TITLE="Tempestade de Mana", DESC="Guia interativo Druid Shaman Archmage Spark + Comet (Cast on Critical) — PoE 2 Forbidden Rites",
            H1S="Spark desde o nível 1 · Comet automático nos mapas · uma barra de mana que é dano e vida ao mesmo tempo", H1="A Tempestade de Mana",
            LEAD="Build de um botão: sua mana vira dano de raio (Archmage), o Spark cobre a tela inteira e o Comet cai sozinho a cada crítico. Diga seu nível, seu ato e o que você já tem."),
 "en": dict(TITLE="Mana Storm", DESC="Interactive Druid Shaman Archmage Spark + Comet (Cast on Critical) guide — PoE 2 Forbidden Rites",
            H1S="Spark from level 1 · automatic Comet in maps · one mana bar that is both damage and life", H1="The Mana Storm",
            LEAD="A one-button build: your mana becomes lightning damage (Archmage), Spark covers the whole screen and Comet falls on its own with every crit. Tell it your level, your act and what you already have."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["quando", "Quando usar", "When to use"], ["mech", "Mana & Infusões", "Mana & Infusions"],
        ["uniques", "Uniques", "Uniques"], ["arvore", "Árvore de Passivas", "Passive Tree"], ["rota", "Rota 1→100", "Route 1→100"], ["skills", "Skills & Supports", "Skills & Supports"],
        ["gear", "Itens", "Items"], ["asc", "Ascendência", "Ascendancy"], ["quests", "Quests", "Quests"], ["tricks", "Tricks Pro", "Pro Tricks"], ["atlas", "Atlas & Challenges", "Atlas & Challenges"],
        ["diag", "Diagnóstico", "Troubleshooting"], ["fontes", "Fontes", "Sources"]]

CLASS, ASC, START = "Druid", "Shaman", 61525
ORDER = ["a1", "a2", "a3", "a4", "maps", "endgame", "max"]
VMAP = {"a1": "A1", "a2": "A2", "a3": "A3", "a4": "A4", "maps": "Mapas", "endgame": "Endgame", "max": "Aspiracional"}
FULLMAP = {k: k for k in ORDER}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a4", "maps": "a4", "endgame": "maps", "max": "endgame"}
PHASE_ACT = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "maps": 6, "endgame": 6, "max": 6}
ITEM_NOTE = {}
RUNE_NOTE = L("Com Wisdom of the Maji cada runa também dá a linha 'Bonded' dela: vida e mana de graça em todo item com socket.",
              "With Wisdom of the Maji every rune also grants its 'Bonded' line: free life and mana on every socketed item.")


def socket_hint(slot, name):
    if slot == "Body Armour":
        return [L("Greater Iron Rune ×2", "Greater Iron Rune ×2"), RUNE_NOTE]
    if slot in (L("Cajado", "Staff"), L("Capacete", "Helmet"), L("Botas", "Boots"), L("Luvas", "Gloves")):
        return [L("Runa de resistência que faltar", "Whatever resistance rune you're missing"), RUNE_NOTE]
    return None


SP30, SP60, SP100 = L("30 Spirit", "30 Spirit"), L("60 Spirit", "60 Spirit"), L("100 Spirit", "100 Spirit")
CHECK = L("Confira no jogo", "Check in game")

SUPWHY = {
 "Chain I": L("Os sparks pulam para outros inimigos: é o clear inteiro do Ato 1 com uma gem só.", "Sparks jump to other enemies: that's your whole Act 1 clear with a single gem."),
 "Chain II": L("Mais pulos por spark.", "More jumps per spark."),
 "Shock": L("Mais chance de Shock — o Shock é o que alimenta as infusões do Siphon Elements depois.", "Higher Shock chance — Shock is what feeds Siphon Elements' infusions later."),
 "Zenith I": L("Mais dano enquanto você está acima de 90% da mana: com Archmage você quase sempre está.", "More damage while above 90% of your mana: with Archmage you almost always are."),
 "Zenith II": L("Mais dano acima de 90% de mana E mais eficiência de custo — as duas coisas que a build mais quer (10 de 10 no ladder).", "More damage above 90% mana AND more cost efficiency — the two things this build wants most (10 of 10 on the ladder)."),
 "Nova Projectiles I": L("Spark em círculo: você fica no meio do pack e todos os sparks saem ao mesmo tempo.", "Spark in a circle: you stand in the pack and every spark leaves at once."),
 "Wildshards I": L("Chance de disparar muitos projéteis extras em círculo — o ensaio barato do Sire of Shards.", "Chance to fire many extra projectiles in a circle — the cheap rehearsal for Sire of Shards."),
 "Fork": L("Cada spark se divide ao acertar: cobre corredores inteiros.", "Each spark forks on hit: covers entire corridors."),
 "Pierce I": L("Sparks atravessam o primeiro alvo em vez de parar nele.", "Sparks go through the first target instead of stopping on it."),
 "Spell Cascade": L("O Comet cai três vezes, em linha: o dano de boss triplica sem gastar mais mana por cast.", "Comet falls three times in a line: triple boss damage without paying more mana per cast."),
 "Considered Casting": L("Mais dano por custo de cast speed — no Comet você não liga, porque quem dispara é o Cast on Critical.", "More damage at the cost of cast speed — on Comet you don't care, because Cast on Critical pulls the trigger."),
 "Comet": L("A spell disparada pelo Cast on Critical: cada crítico do Spark tem chance de detoná-la sozinha, sem você apertar nada.", "The spell triggered by Cast on Critical: every Spark crit has a chance to set it off on its own, without you pressing anything."),
 "Execute III": L("Mais dano contra inimigos em Low Life e mais dano enquanto VOCÊ está em Low Life (com Rathpith Globe você fica sempre).", "More damage against enemies on Low Life and more damage while YOU are on Low Life (with Rathpith Globe you always are)."),
 "Efficiency II": L("Custo menor: com Archmage cada spell custa uma fatia da sua mana máxima, então eficiência é dano sustentado.", "Lower cost: with Archmage every spell costs a slice of your maximum mana, so efficiency is sustained damage."),
 "Rapid Casting II": L("Mais casts por segundo do Spark = mais críticos = mais Comet.", "More Spark casts per second = more crits = more Comet."),
 "Magnified Area II": L("Área maior do Comet.", "Bigger Comet area."),
 "Concentrated Area": L("Área menor e mais dano: versão de boss do Comet.", "Smaller area, more damage: the boss version of Comet."),
 "Cold Penetration": L("O Comet ignora parte da resistência a frio do boss.", "Comet ignores part of the boss's cold resistance."),
 "Lightning Penetration": L("O Spark ignora parte da resistência a raio.", "Spark ignores part of lightning resistance."),
 "Cold Exposure": L("Congelar aplica Exposure: menos resistência a frio no alvo.", "Freezing applies Exposure: less cold resistance on the target."),
 "Lightning Exposure": L("Shockar aplica Exposure: menos resistência a raio no pack inteiro.", "Shocking applies Exposure: less lightning resistance on the whole pack."),
 "Shock Conduction": L("Ao shockar, chance de shockar os vizinhos: mais alvos com ailment para o Siphon Elements virar infusão.", "When you shock, a chance to shock neighbours: more ailment targets for Siphon Elements to turn into infusions."),
 "Harmonic Remnants II": L("Os Remnants (mana e infusão) duram mais.", "Remnants (mana and infusion) last longer."),
 "Remnant Potency I": L("Cada Remnant recuperado vale mais.", "Every Remnant you pick up is worth more."),
 "Clarity II": L("Mais regeneração de mana enquanto o buff estiver ativo.", "More mana regeneration while the buff is active."),
 "Cold Mastery": L("Mais dano de frio no Arctic Armour e no Comet.", "More cold damage on Arctic Armour and Comet."),
 "Lightning Mastery": L("Mais dano de raio — o dano do Archmage é todo de raio.", "More lightning damage — all of Archmage's damage is lightning."),
 "Arcane Surge": L("Gastar mana dá um surto de regeneração e dano de spell: com Archmage você gasta muita mana por cast.", "Spending mana grants a burst of regeneration and spell damage: with Archmage you spend a lot of mana per cast."),
 "Cooldown Recovery II": L("Blink com menos cooldown.", "Shorter Blink cooldown."),
 "Energy Retention": L("Chance de devolver parte da energia do Cast on Critical: Comets em sequência.", "Chance to refund part of Cast on Critical's Energy: back-to-back Comets."),
 "Energy Capacitor": L("Mais energia máxima no Cast on Critical: ele segura mais críticos antes de disparar.", "Higher maximum Energy on Cast on Critical: it holds more crits before triggering."),
 "Powered by Verisium": L("Gasta Ward para criar infusões Verisium, que valem por qualquer infusão elemental: o Comet nunca fica sem a infusão de fogo.", "Spends Ward to create Verisium Infusions, which count as any elemental infusion: Comet never runs out of its fire infusion."),
 "Supercritical": L("Mais dano crítico com menos chance: só quando o crítico já estiver alto.", "More crit damage for less crit chance: only once your crit is already high."),
 "Ambush": L("Mais chance de crítico contra inimigos com vida cheia — é o primeiro hit do pack que precisa criticar.", "More crit chance against full-life enemies — it's the pack's first hit that needs to crit."),
 "Pinpoint Critical": L("Critica com mais frequência (menos dano por crítico): mais disparos do Cast on Critical enquanto o crítico está baixo.", "Crits more often (less damage per crit): more Cast on Critical triggers while your crit is low."),
 "Biting Frost I": L("Mais dano contra congelados, mas consome o Freeze — só na versão de boss do Comet.", "More damage against frozen enemies, but consumes the Freeze — boss version of Comet only."),
 "Deep Freeze": L("O Freeze do Comet dura mais: o boss fica parado mais tempo.", "Comet's Freeze lasts longer: the boss stands still for longer."),
 "Potent Exposure": L("Exposure mais forte do Frost Bomb.", "Stronger Frost Bomb Exposure."),
 "Elemental Discharge": L("Consome ailments no acerto para disparar uma descarga elemental: dano extra grátis em pack shockado.", "Consumes ailments on hit to trigger an elemental discharge: free extra damage on a shocked pack."),
 "Mysticism II": L("Mais dano de spell enquanto o ES estiver cheio.", "More spell damage while your energy shield is full."),
 "Knockback": L("O Arctic Armour empurra quem encosta em você.", "Arctic Armour pushes away whoever touches you."),
}

PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Spark + Chain I", "Spark + Chain I"),
  carry=L("Você: Spark", "You: Spark"), dmgSplit=[100, 0],
  goal=L("O primeiro Uncut Skill Gem (nível 1) já é a build inteira: Spark. Os projéteis andam sozinhos pelo chão e, com Chain I, pulam de inimigo em inimigo — você anda e segura o botão. Frost Bomb é o único outro botão (Exposure para os bosses de ato). Nível 12: Mana Remnants com os 30 de Spirit do King in the Mists; a partir daí, matar inimigo com ailment devolve mana e a sua barra azul nunca mais some.",
         "Your very first Uncut Skill Gem (level 1) is already the whole build: Spark. The projectiles travel along the ground by themselves and, with Chain I, jump from enemy to enemy — you walk and hold the button. Frost Bomb is your only other button (Exposure for act bosses). Level 12: Mana Remnants with the 30 Spirit from King in the Mists; from then on, killing an ailing enemy refunds mana and your blue bar never empties again."),
  rotation=[L("Ande até o pack e segure o Spark", "Walk up to the pack and hold Spark"), L("Boss: Frost Bomb no chão → Spark colado (os sparks quicam nas paredes e voltam)", "Boss: Frost Bomb on the ground → Spark up close (sparks bounce off walls and come back)"), L("Mana no fim: pare 2 s (a regeneração do Ato 1 é rápida) ou pegue um Mana Remnant", "Out of mana: stand still for 2 s (Act 1 regen is fast) or pick up a Mana Remnant")],
  gems=[
   G("Spark", ["Chain I"], L("Clear + boss", "Clear + boss"), L("Projéteis erráticos que andam pelo chão até acertar alguém. É a skill que você usa do nível 1 ao 100.", "Erratic projectiles that travel along the ground until they hit something. It's the skill you use from level 1 to 100."), "free"),
   G("Frost Bomb", [], L("Exposure", "Exposure"), L("Pulsa Exposure (menos resistência) e explode no fim. Uncut Skill Gem nível 1.", "Pulses Exposure (lower resistance) and detonates at the end. Level 1 Uncut Skill Gem."), "free"),
   G("Orb of Storms", ["Shock"], L("Shock de boss", "Boss shock"), L("Orbe parada que shocka sozinha: dano extra no boss sem tirar a mão do Spark. Uncut Skill Gem nível 3.", "A stationary orb that shocks on its own: extra boss damage without taking your hand off Spark. Level 3 Uncut Skill Gem."), "free", since=8),
   G("Mana Remnants", [], L("Mana no chão", "Mana on the ground"), L("Matar inimigo com ailment (o Shock do Spark serve) cria um Remnant de mana; pegar recupera mana e pode passar do máximo.", "Killing an ailing enemy (Spark's Shock counts) creates a mana Remnant; picking it up restores mana and can overflow your maximum."), "core", 1, SP30, since=12),
  ],
  cheap=["Threaded Light", "Stone of Lazhwar", L("Cajado com 'increased Spell Damage' e mana (compre no vendor a cada ato)", "Staff with 'increased Spell Damage' and mana (buy one from the vendor every act)")],
  full=["Goldrim", "Wanderlust", "Dream Fragments"],
  stats=[L("Mana máxima", "Maximum mana"), L("Dano de spell / raio", "Spell / lightning damage"), L("Vida e resistências", "Life and resistances")],
  tree=L("Primeiro os nós de mana e dano de raio do começo do Druid (Raw Mana, Brain Storm): mana já é dano nesta build, mesmo antes do Archmage.", "First the mana and lightning nodes at the Druid start (Raw Mana, Brain Storm): mana is already damage in this build, even before Archmage."),
  avoid=[L("Trocar o Spark por outra skill 'de leveling' — ele escala até o nível 100", "Swapping Spark for some other 'leveling' skill — it scales to level 100"), L("Gastar ouro em cajado caro: qualquer Magic com dano de spell serve", "Spending gold on an expensive staff: any Magic one with spell damage works")],
  exit=[L("King in the Mists: +30 de Spirit → Mana Remnants", "King in the Mists: +30 Spirit → Mana Remnants"), L("Goldrim e Wanderlust (10/11): resistências e velocidade", "Goldrim and Wanderlust (10/11): resistances and speed")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 31], tag=L("Spark em círculo + 1ª ascendência", "Circle Spark + 1st ascendancy"),
  carry=L("Você: Spark", "You: Spark"), dmgSplit=[100, 0],
  goal=L("Nova Projectiles I transforma o Spark: em vez de sair para frente, os projéteis saem em círculo à sua volta — você entra no meio do pack e solta. 1º Trial (~25): Sacred Flow, que dá +40 de Spirit para CADA slot de charm vazio. Com o cinto do ato e nenhum charm equipado, seu Spirit dobra de uma vez e o Arctic Armour entra junto do Mana Remnants. Continue com Frost Bomb e Orb of Storms nos bosses.",
         "Nova Projectiles I transforms Spark: instead of firing forwards, the projectiles leave in a circle around you — you walk into the middle of the pack and release. 1st Trial (~25): Sacred Flow, which grants +40 Spirit for EACH empty charm slot. With the act's belt and no charms equipped your Spirit doubles at once, and Arctic Armour joins Mana Remnants. Keep Frost Bomb and Orb of Storms for bosses."),
  rotation=[L("Entre no pack e solte o Spark (círculo)", "Step into the pack and release Spark (circle)"), L("Boss: Frost Bomb → Orb of Storms → Spark colado", "Boss: Frost Bomb → Orb of Storms → Spark up close"), L("Pegue os Mana Remnants que caem: eles passam do máximo de mana", "Pick up the Mana Remnants that drop: they overflow your maximum mana")],
  gems=[
   G("Spark", ["Chain I", "Nova Projectiles I", "Shock"], L("Clear", "Clear"), L("Círculo de sparks: o pack inteiro toma vários hits e fica shockado.", "A circle of sparks: the whole pack takes several hits and ends up shocked."), "free"),
   G("Frost Bomb", ["Potent Exposure"], L("Exposure", "Exposure"), L("Solte quando o boss aparecer e relance quando acabar.", "Drop it as the boss appears and recast when it ends."), "free"),
   G("Orb of Storms", ["Shock", "Lightning Exposure"], L("Boss", "Boss"), L("Fica shockando sozinha embaixo do boss.", "Keeps shocking the boss on its own."), "free"),
   G("Mana Remnants", ["Harmonic Remnants II"], L("Mana no chão", "Mana on the ground"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Arctic Armour", [], L("Defesa", "Defence"), L("Barreira de gelo que ganha estágios: quem te bate em melee perde um estágio e toma dano de frio. Entra com o Spirit do Sacred Flow.", "An icy barrier that gains stages: melee attackers remove a stage and take cold damage. Comes online with Sacred Flow's Spirit."), "core", 2, SP30, since=25),
  ],
  cheap=["Doedre's Tenure", "Serpent's Lesson", L("Anéis e cinto com mana máxima e resistência", "Rings and belt with maximum mana and resistance")],
  full=["Astramentis", "The Eternal Spark"],
  stats=[L("Mana máxima", "Maximum mana"), L("% dano de spell", "% spell damage"), L("Resistências", "Resistances")],
  tree=L("Arcane Intensity (dano de spell por 100 de mana máxima) e Brain Storm; comece a pegar vida no caminho para o Ato 3.", "Arcane Intensity (spell damage per 100 maximum mana) and Brain Storm; start picking up life on the way to Act 3."),
  avoid=[L("Equipar charm sem precisar: com Sacred Flow, cada charm equipado custa 40 de Spirit", "Equipping a charm you don't need: with Sacred Flow every equipped charm costs you 40 Spirit"), L("Nova Projectiles II no lugar da I (cooldown e menos dano)", "Nova Projectiles II instead of I (cooldown and less damage)")],
  exit=[L("1ª ascendência: Sacred Flow", "1st ascendancy: Sacred Flow"), L("Spark com 3 supports", "3-support Spark")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[32, 45], tag=L("Comet + o loop das infusões", "Comet + the infusion loop"),
  carry=L("Você: Spark (clear) · Comet (boss)", "You: Spark (clear) · Comet (boss)"), dmgSplit=[75, 25],
  goal=L("Uncut Skill Gem nível 11: Comet. Ele cai do céu, dá um dano enorme num ponto e congela — é o seu botão de boss do Ato 3 até o nível 100. Uncut nível 8: Siphon Elements (30 de Spirit), que cria Infusion Remnants quando você congela, shocka ou incendeia. Aqui entra o truque da build: com a keystone Elemental Equilibrium, o Shock passa a criar infusão de FRIO (que o Spark consome para disparar sparks em círculo) e o Freeze passa a criar infusão de FOGO (que o Comet consome para uma explosão de gelo e fogo). Uma skill alimenta a outra. 2º Trial (~40): Wisdom of the Maji.",
         "Level 11 Uncut Skill Gem: Comet. It falls from the sky, deals huge damage at one spot and freezes — your boss button from Act 3 to level 100. Level 8 Uncut: Siphon Elements (30 Spirit), which creates Infusion Remnants when you freeze, shock or ignite. Here's the build's trick: with the Elemental Equilibrium keystone, Shock starts creating COLD infusions (which Spark consumes to fire sparks in a circle) and Freeze starts creating FIRE infusions (which Comet consumes for a devastating ice-and-fire blast). Each skill feeds the other. 2nd Trial (~40): Wisdom of the Maji."),
  rotation=[L("Clear: Spark no pack (o Shock vira infusão de frio)", "Clear: Spark into the pack (the Shock becomes a cold infusion)"), L("Pegue o Infusion Remnant e solte o Spark de novo: sai o círculo grande", "Pick up the Infusion Remnant and cast Spark again: you get the big circle"), L("Boss: Frost Bomb → Comet → Spark para recarregar mana e infusão → Comet", "Boss: Frost Bomb → Comet → Spark to recharge mana and infusion → Comet")],
  gems=[
   G("Spark", ["Chain I", "Nova Projectiles I", "Shock", "Lightning Exposure"], L("Clear", "Clear"), L("Consome infusão de frio para disparar muitos sparks em círculo.", "Consumes a cold infusion to fire many sparks in a circle."), "free"),
   G("Comet", ["Spell Cascade", "Concentrated Area"], L("Boss", "Boss"), L("Bloco de gelo do céu: dano alto num ponto e Freeze. Spell Cascade faz cair três vezes. Uncut Skill Gem nível 11.", "A mass of ice from the sky: high damage at one point and Freeze. Spell Cascade makes it fall three times. Level 11 Uncut Skill Gem."), "free", since=34),
   G("Siphon Elements", ["Harmonic Remnants II"], L("Infusões", "Infusions"), L("Chance de criar um Infusion Remnant quando você congela, shocka ou incendeia. Com Elemental Equilibrium o tipo criado é trocado.", "A chance to create an Infusion Remnant when you freeze, shock or ignite. With Elemental Equilibrium the type created is swapped."), "core", 3, SP30, since=36),
   G("Frost Bomb", ["Potent Exposure", "Cold Exposure"], L("Exposure", "Exposure"), L("Abre o boss antes do Comet.", "Softens the boss before Comet."), "free"),
   G("Mana Remnants", ["Harmonic Remnants II", "Remnant Potency I"], L("Mana no chão", "Mana on the ground"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Arctic Armour", ["Cold Mastery"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
  ],
  cheap=["Snakepit", "The Everlasting Gaze", L("Cajado rare: % dano de spell + mana + cast speed", "Rare staff: % spell damage + mana + cast speed")],
  full=[L("Focus com ES e mana (The Eternal Spark)", "Focus with ES and mana (The Eternal Spark)"), L("Anéis com mana máxima e resistência", "Rings with maximum mana and resistance")],
  stats=[L("Mana máxima", "Maximum mana"), L("Cast speed", "Cast speed"), L("Resistências no cap", "Capped resistances")],
  tree=L("Elemental Equilibrium (a keystone do loop de infusões), Chakra of Elements e os nós de Remnant (Remnant Attraction, Arcane Remnants).", "Elemental Equilibrium (the infusion loop keystone), Chakra of Elements and the Remnant nodes (Remnant Attraction, Arcane Remnants)."),
  avoid=[L("Pegar Elemental Equilibrium sem o Siphon Elements ligado (aí ela não faz nada por você)", "Taking Elemental Equilibrium without Siphon Elements active (then it does nothing for you)"), L("Usar o Comet no clear: é caro e lento para pack", "Using Comet to clear: it's expensive and slow against packs")],
  exit=[L("Azak Bog: +30 de Spirit", "Azak Bog: +30 Spirit"), L("2ª ascendência: Wisdom of the Maji", "2nd ascendancy: Wisdom of the Maji")]),

 dict(id="a4", name=L("Ato 4 + Interlúdios", "Act 4 + Interludes"), lv=[46, 64], tag=L("Archmage: a mana vira dano", "Archmage: mana becomes damage"),
  carry=L("Você: Spark + Archmage", "You: Spark + Archmage"), dmgSplit=[80, 20],
  goal=L("Uncut Skill Gem nível 14: Archmage (100 de Spirit). Enquanto ativo, suas spells custam mana a mais E ganham dano de raio extra com base na sua mana máxima. A partir daqui, +100 de mana máxima em qualquer item é dano puro. Aloque Eldritch Battery (todo o seu Energy Shield vira mana, então item de ES também é dano) e Mind Over Matter (o dano que você toma sai da mana antes da vida — a mesma barra é dano e defesa). Nível 58: Sire of Shards, um cajado que custa quase nada e faz TODA spell disparar 4 projéteis a mais, em círculo.",
         "Level 14 Uncut Skill Gem: Archmage (100 Spirit). While active your spells cost extra mana AND gain extra lightning damage based on your maximum mana. From here, +100 maximum mana on any item is raw damage. Allocate Eldritch Battery (all your Energy Shield becomes mana, so ES gear is damage too) and Mind Over Matter (damage you take comes from mana before life — the same bar is damage and defence). Level 58: Sire of Shards, a staff that costs almost nothing and makes EVERY spell fire 4 extra projectiles, in a circle."),
  rotation=[L("Clear: um Spark por pack (com Sire of Shards é a tela inteira)", "Clear: one Spark per pack (with Sire of Shards that's the whole screen)"), L("Boss: Frost Bomb → Comet ×2 → Spark para recarregar → Comet", "Boss: Frost Bomb → Comet ×2 → Spark to recharge → Comet"), L("Mana baixa é perigo: Mind Over Matter usa a mana como escudo — recue e deixe o Mana Remnants encher", "Low mana is danger: Mind Over Matter uses mana as your shield — back off and let Mana Remnants refill it")],
  gems=[
   G("Spark", ["Chain I", "Nova Projectiles I", "Zenith I", "Lightning Exposure"], L("Clear", "Clear"), L("Com Archmage cada spark carrega dano de raio plano vindo da sua mana máxima.", "With Archmage every spark carries flat lightning damage from your maximum mana."), "free"),
   G("Comet", ["Spell Cascade", "Concentrated Area", "Considered Casting"], L("Boss", "Boss"), L("Ainda na mão: o gatilho automático só chega nos mapas.", "Still manual: the automatic trigger only arrives in maps."), "free"),
   G("Archmage", ["Clarity II"], L("Mana = dano", "Mana = damage"), L("100 de Spirit (os 100 das quests). É a virada da build: mana máxima vira dano de raio nas spells.", "100 Spirit (the 100 from quests). This is the build's turning point: maximum mana becomes lightning damage on your spells."), "core", 1, SP100, since=50),
   G("Siphon Elements", ["Harmonic Remnants II", "Remnant Potency I"], L("Infusões", "Infusions"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Mana Remnants", ["Harmonic Remnants II", "Remnant Potency I"], L("Mana no chão", "Mana on the ground"), L("30 Spirit. Com Archmage, mana no chão é munição.", "30 Spirit. With Archmage, mana on the ground is ammunition."), "core", 3, SP30),
   G("Arctic Armour", ["Cold Mastery", "Knockback"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Frost Bomb", ["Potent Exposure", "Cold Exposure"], L("Exposure", "Exposure"), L("Só em boss.", "Bosses only."), "free"),
  ],
  cheap=["Lavianga's Spirits", "Uhtred's Chalice", "Ghostwrithe", "Sire of Shards"],
  full=["Olroth's Resolve", L("Rares com +mana máxima em todo slot", "Rares with +maximum mana in every slot")],
  stats=[L("Mana máxima (a estatística principal)", "Maximum mana (the main stat)"), L("Energy Shield (vira mana com Eldritch Battery)", "Energy Shield (becomes mana with Eldritch Battery)"), L("Resistências 75%", "75% resistances")],
  tree=L("Eldritch Battery e Mind Over Matter, Raw Mana, Tempered Mind e Mental Alacrity; os nós de Archon (Invigorating/Energising Archon) no caminho.", "Eldritch Battery and Mind Over Matter, Raw Mana, Tempered Mind and Mental Alacrity; the Archon nodes (Invigorating/Energising Archon) along the way."),
  avoid=[L("Scold's Bridle: você toma dano físico por mana gasta — com Archmage isso te mata", "Scold's Bridle: you take physical damage per mana spent — with Archmage that kills you"), L("Ligar o Archmage sem resistências no cap: a mana passa a ser sua vida", "Turning Archmage on without capped resistances: mana is your life now")],
  exit=[L("Lythara (+40): 100 de Spirit para o Archmage", "Lythara (+40): 100 Spirit for Archmage"), L("Sire of Shards (58): 4 projéteis extras em círculo", "Sire of Shards (58): 4 extra projectiles in a circle")]),

 dict(id="maps", name=L("Mapas: Comet automático", "Maps: automatic Comet"), lv=[65, 79], tag=L("Cast on Critical + Comet", "Cast on Critical + Comet"),
  carry=L("Você: Spark · automático: Comet", "You: Spark · automatic: Comet"), dmgSplit=[45, 55],
  goal=L("Aqui a build vira um botão só. Cast on Critical (100 de Spirit) ganha energia a cada crítico e, cheio, dispara as spells encaixadas nele: coloque o Comet + Spell Cascade. Como o Spark dispara dezenas de projéteis por cast, você critica o tempo todo e o Comet cai sozinho, em cima do pack e em cima do boss, enquanto você só anda segurando o Spark. Para caber os dois buffs de 100 você precisa de Spirit: Sacred Flow (charms vazios), amuleto e peito com Spirit. 3ª ascendência (~68): Reactive Growth.",
         "This is where the build becomes a single button. Cast on Critical (100 Spirit) gains Energy on every crit and, when full, triggers the spells socketed in it: put Comet + Spell Cascade there. Since Spark fires dozens of projectiles per cast you crit constantly, and Comet falls on its own — on packs and on bosses — while you just walk holding Spark. To fit both 100-Spirit buffs you need Spirit: Sacred Flow (empty charm slots), amulet and chest with Spirit. 3rd ascendancy (~68): Reactive Growth."),
  rotation=[L("Clear: ande segurando o Spark. O Comet cai sozinho.", "Clear: walk holding Spark. Comet falls by itself."), L("Boss: Frost Bomb → Spark colado (cada crítico enche o Cast on Critical) → Comet na mão quando quiser empurrar", "Boss: Frost Bomb → Spark up close (every crit fills Cast on Critical) → manual Comet when you want to push"), L("Blink para sair de mecânica e reposicionar", "Blink to dodge mechanics and reposition")],
  gems=[
   G("Spark", ["Nova Projectiles I", "Chain I", "Zenith II", "Lightning Penetration", "Rapid Casting II"], L("Clear + gatilho", "Clear + trigger"), L("Além de limpar, é ele que gera os críticos que disparam o Comet.", "Besides clearing, it's what generates the crits that trigger Comet."), "free"),
   G("Cast on Critical", ["Comet", "Spell Cascade", "Efficiency II", "Energy Retention"], L("Comet automático", "Automatic Comet"), L("Setup de 10 dos 10 Shamans de maior DPS do ladder. 100 de Spirit.", "The setup on 10 of the 10 highest-DPS Shamans on the ladder. 100 Spirit."), "core", 1, SP100, since=65),
   G("Archmage", ["Clarity II", "Lightning Mastery"], L("Mana = dano", "Mana = damage"), L("100 de Spirit.", "100 Spirit."), "core", 2, SP100),
   G("Comet", ["Spell Cascade", "Concentrated Area", "Considered Casting", "Cold Penetration"], L("Boss na mão", "Manual boss"), L("A versão que você lança você mesmo, para empurrar dano no boss.", "The version you cast yourself, to push damage on a boss."), "free"),
   G("Siphon Elements", ["Harmonic Remnants II", "Remnant Potency I", "Cold Mastery"], L("Infusões", "Infusions"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Mana Remnants", ["Harmonic Remnants II", "Remnant Potency I"], L("Mana no chão", "Mana on the ground"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Arctic Armour", ["Cold Mastery", "Knockback"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 5, SP30),
   G("Blink", ["Cooldown Recovery II", "Efficiency II"], L("Mobilidade", "Mobility"), L("Troca seu dodge roll por um teleporte curto. 60 de Spirit: entre nele só quando sobrar.", "Replaces your dodge roll with a short teleport. 60 Spirit: only take it when you have room."), "opt", 1, SP60),
  ],
  cheap=["Cloak of Defiance", L("Amuleto rare com +Spirit e mana", "Rare amulet with +Spirit and mana"), L("Runas de resistência (com Wisdom of the Maji cada uma vale dobrado)", "Resistance runes (with Wisdom of the Maji each one counts double)")],
  full=["Rathpith Globe", L("Ancestral Tiara (ES + mana) e Vile Robe (ES + mana)", "Ancestral Tiara (ES + mana) and Vile Robe (ES + mana)")],
  stats=[L("Spirit (meta: 230+)", "Spirit (goal: 230+)"), L("Mana máxima (meta: 2.000+)", "Maximum mana (goal: 2,000+)"), L("Chance de crítico para spells", "Spell crit chance"), L("Resistências 75% e vida", "75% resistances and life")],
  tree=L("Invocated Efficiency (spells disparadas dão mais dano), Dreamcatcher, Mental Alacrity e os nós de crítico para spells.", "Invocated Efficiency (triggered spells deal more damage), Dreamcatcher, Mental Alacrity and the spell crit nodes."),
  avoid=[L("Cast on Critical sem chance de crítico: sem crítico ele não dispara nunca", "Cast on Critical with no crit chance: without crits it never triggers"), L("Encaixar Spark dentro do Cast on Critical (o gatilho é ele, não o disparado)", "Socketing Spark inside Cast on Critical (Spark is the trigger, not the triggered spell)")],
  exit=[L("3ª ascendência: Reactive Growth", "3rd ascendancy: Reactive Growth"), L("Rathpith Globe (75): crítico por vida e o truque do Low Life", "Rathpith Globe (75): crit per life and the Low Life trick")]),

 dict(id="endgame", name=L("Endgame: Low Life", "Endgame: Low Life"), lv=[80, 92], tag=L("Rathpith + Pain Attunement", "Rathpith + Pain Attunement"),
  carry=L("Você: Spark · automático: Comet", "You: Spark · automatic: Comet"), dmgSplit=[40, 60],
  goal=L("O empurrão final de dano é uma troca que parece suicídio e não é: o Rathpith Globe faz cada spell não-canalizada custar 6% da sua vida máxima, então você vive em Low Life. Com Mind Over Matter o dano que chega sai da MANA (que é enorme), enquanto o Low Life liga três bônus ao mesmo tempo: Pain Attunement (30% more dano crítico), Execute III (more dano enquanto você está em Low Life) e Final Barrage (mais cast speed em Low Life). 4ª ascendência (~80): Avatar of Evolution, que dobra as Adaptations do Reactive Growth.",
         "The last damage push is a trade that looks suicidal and isn't: Rathpith Globe makes every non-channelling spell cost 6% of your maximum life, so you live on Low Life. With Mind Over Matter incoming damage comes out of your MANA (which is huge), while Low Life switches on three bonuses at once: Pain Attunement (30% more crit damage), Execute III (more damage while you are on Low Life) and Final Barrage (more cast speed on Low Life). 4th ascendancy (~80): Avatar of Evolution, which doubles Reactive Growth's Adaptations."),
  rotation=[L("Clear: Spark andando; o Comet do Cast on Critical limpa o resto", "Clear: Spark while walking; Cast on Critical's Comet cleans up the rest"), L("Boss: Frost Bomb → Spark colado → Comet na mão entre as mecânicas", "Boss: Frost Bomb → Spark up close → manual Comet between mechanics"), L("Mana é sua vida: Uhtred's Chalice/Lavianga's Spirits sempre ativos", "Mana is your life: keep Uhtred's Chalice/Lavianga's Spirits up")],
  gems=[
   G("Spark", ["Nova Projectiles I", "Zenith II", "Execute III", "Lightning Penetration", "Rapid Casting II"], L("Clear + gatilho", "Clear + trigger"), L("Execute III entra quando o Rathpith te deixa em Low Life permanente.", "Execute III comes in once Rathpith keeps you permanently on Low Life."), "free"),
   G("Cast on Critical", ["Comet", "Spell Cascade", "Execute III", "Efficiency II", "Energy Retention"], L("Comet automático", "Automatic Comet"), L("100 de Spirit.", "100 Spirit."), "core", 1, SP100),
   G("Archmage", ["Clarity II", "Lightning Mastery"], L("Mana = dano", "Mana = damage"), L("100 de Spirit.", "100 Spirit."), "core", 2, SP100),
   G("Comet", ["Spell Cascade", "Considered Casting", "Execute III", "Cold Penetration"], L("Boss na mão", "Manual boss"), L("Versão de empurrar dano.", "The damage-push version."), "free"),
   G("Siphon Elements", ["Harmonic Remnants II", "Remnant Potency I", "Cold Mastery"], L("Infusões", "Infusions"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Mana Remnants", ["Harmonic Remnants II", "Remnant Potency I"], L("Mana no chão", "Mana on the ground"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Arctic Armour", ["Cold Mastery", "Knockback", "Mysticism II"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 5, SP30),
   G("Remnants of Kalguur", ["Harmonic Remnants II", "Remnant Potency I"], L("Runic Ward", "Runic Ward"), L("Inimigos que você stuna ou mata podem gerar Remnants de Runic Ward — é o que o Olroth's Resolve transforma em Guard. 30 de Spirit.", "Enemies you stun or kill can generate Runic Ward Remnants — what Olroth's Resolve turns into Guard. 30 Spirit."), "opt", 1, SP30),
   G("Blink", ["Cooldown Recovery II", "Efficiency II"], L("Mobilidade", "Mobility"), L("60 de Spirit.", "60 Spirit."), "opt", 2, SP60),
  ],
  cheap=["Taryn's Shiver", L("Jewels Sapphire: % dano de spell + crítico para spells", "Sapphire jewels: % spell damage + spell crit")],
  full=["Rite of Passage", L("Absent Amulet com Zarokh's Gift · Mnemonic Ring · Sirenscale Gloves", "Absent Amulet with Zarokh's Gift · Mnemonic Ring · Sirenscale Gloves")],
  stats=[L("Mana máxima (meta: 3.000+)", "Maximum mana (goal: 3,000+)"), L("Crítico para spells", "Spell crit"), L("Vida máxima (o Rathpith escala com ela)", "Maximum life (Rathpith scales with it)"), L("Resistências e Chaos Resistance", "Resistances and chaos resistance")],
  tree=L("Pain Attunement, Final Barrage e os nós de crítico/dano crítico; jewels de dano de spell nos sockets que abriram.", "Pain Attunement, Final Barrage and the crit/crit damage nodes; spell damage jewels in the sockets you opened."),
  avoid=[L("Pain Attunement sem o Rathpith (aí ela é 30% LESS dano crítico com a vida cheia)", "Pain Attunement without Rathpith (then it's 30% LESS crit damage on full life)"), L("Chaos damage: ele fura o Mind Over Matter direto na vida — e sua vida está baixa", "Chaos damage: it goes straight past Mind Over Matter into your life — and your life is low")],
  exit=[L("4ª ascendência: Avatar of Evolution", "4th ascendancy: Avatar of Evolution"), L("T15 e pinnacles em rotação", "T15s and pinnacles on farm")]),

 dict(id="max", name=L("Aspiracional", "Aspirational"), lv=[93, 100], tag=L("Runeseeker's Call · Mageblood", "Runeseeker's Call · Mageblood"),
  carry=L("Você: Spark · automático: Comet", "You: Spark · automatic: Comet"), dmgSplit=[35, 65],
  goal=L("O teto da build são três itens caros que multiplicam o que você já tem: Runeseeker's Call (a arma de runa dos 10 do ladder: +mana máxima gigante, +níveis de spell e 200% do efeito das runas — que a Wisdom of the Maji já dobra), Mageblood (flasks de utilidade permanentes; lembre que cada charm equipado custa 40 de Spirit do Sacred Flow) e Kalandra's Touch, que copia o seu melhor anel de mana. The Stars Answer entra como terceira skill: fica disparando Starfall sozinha em volta.",
         "The build's ceiling is three expensive items that multiply what you already have: Runeseeker's Call (the rune weapon all 10 ladder characters use: huge +maximum mana, +spell levels and 200% rune effect — which Wisdom of the Maji already doubles), Mageblood (permanent utility flasks; remember every equipped charm costs 40 Spirit from Sacred Flow) and Kalandra's Touch, which copies your best mana ring. The Stars Answer joins as a third skill: it keeps triggering Starfall around you on its own."),
  rotation=[L("Igual ao endgame: Spark andando, Comet automático", "Same as endgame: Spark while walking, automatic Comet"), L("Boss: Frost Bomb → Spark → Comet na mão", "Boss: Frost Bomb → Spark → manual Comet")],
  gems=[
   G("Spark", ["Nova Projectiles I", "Zenith II", "Execute III", "Lightning Penetration", "Rapid Casting II"], L("Clear + gatilho", "Clear + trigger"), L("Mesmo papel.", "Same role."), "free"),
   G("Cast on Critical", ["Comet", "Spell Cascade", "Execute III", "Efficiency II", "Powered by Verisium"], L("Comet automático", "Automatic Comet"), L("Powered by Verisium gasta Ward para criar infusões que valem por qualquer elemento: o Comet sempre sai na versão explosiva.", "Powered by Verisium spends Ward to create infusions that count as any element: Comet always lands in its explosive version."), "core", 1, SP100),
   G("Archmage", ["Clarity II", "Lightning Mastery"], L("Mana = dano", "Mana = damage"), L("100 de Spirit.", "100 Spirit."), "core", 2, SP100),
   G("The Stars Answer", [], L("Starfall automática", "Automatic Starfall"), L("Fica disparando Starfall em inimigos à sua volta. Os 10 do ladder usam; é gem tier 0 (não sai de Uncut Skill Gem comum) — confira no jogo como você consegue a sua.", "Keeps triggering Starfall at enemies around you. All 10 ladder characters use it; it's a tier 0 gem (not from a normal Uncut Skill Gem) — check in game how to get yours."), "opt", 1, CHECK),
   G("Siphon Elements", ["Harmonic Remnants II", "Remnant Potency I", "Cold Mastery"], L("Infusões", "Infusions"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Mana Remnants", ["Harmonic Remnants II", "Remnant Potency I"], L("Mana no chão", "Mana on the ground"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Arctic Armour", ["Cold Mastery", "Knockback", "Mysticism II"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 5, SP30),
   G("Remnants of Kalguur", ["Harmonic Remnants II", "Remnant Potency I"], L("Runic Ward", "Runic Ward"), L("30 Spirit.", "30 Spirit."), "opt", 2, SP30),
  ],
  cheap=[L("Jewels Sapphire de dano de spell e crítico", "Sapphire jewels with spell damage and crit")],
  full=["Runeseeker's Call", "Mageblood", "Kalandra's Touch", "Temporalis"],
  stats=[L("Mana máxima acima de 4.000", "Maximum mana above 4,000"), L("+ níveis de spell", "+ spell levels"), L("Crítico e dano crítico", "Crit and crit damage")],
  tree=L("Fecha os clusters de mana e crítico e usa os jewels (From Nothing/Voices) se você chegar lá.", "Finish the mana and crit clusters and use the jewels (From Nothing/Voices) if you get there."),
  avoid=[L("Comprar Mageblood antes de resolver Spirit: charm equipado é −40 de Spirit", "Buying Mageblood before solving Spirit: an equipped charm is −40 Spirit")],
  exit=[L("Pinnacles e mapas juiced", "Pinnacles and juiced maps")]),
]
PH = {p["id"]: p for p in PHASES}

BOX = {
 "a1": ("1", [L("botão: Spark", "button: Spark")], L("Chain I no Spark resolve o Ato 1 inteiro.", "Chain I on Spark solves all of Act 1.")),
 "a2": ("+40", [L("Spirit por charm vazio", "Spirit per empty charm slot")], L("Sacred Flow: slot de charm vazio vale 40 de Spirit.", "Sacred Flow: an empty charm slot is worth 40 Spirit.")),
 "a3": ("EE", [L("troca o tipo da infusão", "swaps the infusion type")], L("Shock → infusão de frio (Spark) · Freeze → infusão de fogo (Comet).", "Shock → cold infusion (Spark) · Freeze → fire infusion (Comet).")),
 "a4": ("100", [L("Spirit do Archmage", "Archmage Spirit")], L("A partir daqui, mana máxima é dano.", "From here on, maximum mana is damage.")),
 "maps": ("CoC", [L("dispara o Comet", "triggers Comet")], L("Cada crítico do Spark enche a energia; cheio, cai Comet.", "Every Spark crit fills the Energy; when full, Comet falls.")),
 "endgame": ("6%", [L("da vida por spell (Rathpith)", "of life per spell (Rathpith)")], L("Low Life permanente: Pain Attunement + Execute III + Final Barrage.", "Permanent Low Life: Pain Attunement + Execute III + Final Barrage.")),
 "max": ("200%", [L("efeito das runas", "rune effect")], L("Runeseeker's Call + Wisdom of the Maji: cada runa vale por várias.", "Runeseeker's Call + Wisdom of the Maji: every rune counts for several.")),
}
SPIRIT_NOTE = {
 "a1": L("30 das quests: Mana Remnants.", "30 from quests: Mana Remnants."),
 "a2": L("30 das quests + 40 por slot de charm vazio (Sacred Flow): Mana Remnants + Arctic Armour.", "30 from quests + 40 per empty charm slot (Sacred Flow): Mana Remnants + Arctic Armour."),
 "a3": L("60 das quests + Sacred Flow: + Siphon Elements.", "60 from quests + Sacred Flow: + Siphon Elements."),
 "a4": L("100 das quests + Sacred Flow: Archmage (100) primeiro, o resto conforme sobrar.", "100 from quests + Sacred Flow: Archmage (100) first, the rest with whatever is left."),
 "maps": L("Meta: 230+ (Archmage 100 + Cast on Critical 100 + 30). Spirit vem de amuleto, peito e dos slots de charm vazios.", "Goal: 230+ (Archmage 100 + Cast on Critical 100 + 30). Spirit comes from the amulet, the chest and empty charm slots."),
 "endgame": L("Meta: 290+ para Archmage + Cast on Critical + Siphon Elements + Mana Remnants + Arctic Armour. Mods de Reservation Efficiency contam: confira no jogo.", "Goal: 290+ for Archmage + Cast on Critical + Siphon Elements + Mana Remnants + Arctic Armour. Reservation Efficiency mods count: check in game."),
 "max": L("Cada charm equipado (Rite of Passage, Mageblood) custa 40 de Spirit do Sacred Flow: some antes de equipar.", "Every equipped charm (Rite of Passage, Mageblood) costs 40 Spirit from Sacred Flow: do the math before equipping."),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in SPIRIT_NOTE.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Spark (Uncut Skill Gem nível 1) + Frost Bomb: a build começa aqui.", "Spark (level 1 Uncut Skill Gem) + Frost Bomb: the build starts here."),
 4: L("Chain I no Spark: os projéteis pulam de inimigo em inimigo.", "Chain I on Spark: projectiles jump from enemy to enemy."),
 6: L("Threaded Light (focus): ES, regen de mana e dano de spell por Spirit.", "Threaded Light (focus): ES, mana regen and spell damage per Spirit."),
 8: L("Stone of Lazhwar: +50–99 de mana e cast speed. Orb of Storms para bosses.", "Stone of Lazhwar: +50–99 mana and cast speed. Orb of Storms for bosses."),
 10: L("Goldrim: resistências resolvidas até o Ato 3.", "Goldrim: resistances solved until Act 3."),
 11: L("Wanderlust: 20% de Movement Speed e imune a Slow.", "Wanderlust: 20% Movement Speed and slow immunity."),
 12: L("King in the Mists (+30 Spirit): Mana Remnants. Dream Fragments: mana e imune a Freeze.", "King in the Mists (+30 Spirit): Mana Remnants. Dream Fragments: mana and freeze immunity."),
 16: L("Doedre's Tenure: 100% increased Spell Damage por ~0,003 divine.", "Doedre's Tenure: 100% increased Spell Damage for ~0.003 divine."),
 18: L("Nova Projectiles I: Spark em círculo.", "Nova Projectiles I: Spark in a circle."),
 22: L("Serpent's Lesson: +vida e +mana (e o gancho de Low Life para o endgame).", "Serpent's Lesson: +life and +mana (and the Low Life hook for endgame)."),
 24: L("Astramentis: +50–95 em todos os atributos — nunca mais falta requisito de gem.", "Astramentis: +50–95 to all attributes — no gem requirement problems ever again."),
 25: L("1ª ascendência: Sacred Flow (+40 de Spirit por slot de charm vazio).", "1st ascendancy: Sacred Flow (+40 Spirit per empty charm slot)."),
 26: L("The Eternal Spark: +5% de resistência máxima a raio e regen de mana.", "The Eternal Spark: +5% maximum lightning resistance and mana regen."),
 34: L("Comet (Uncut nível 11): o botão de boss.", "Comet (level 11 Uncut): the boss button."),
 36: L("Siphon Elements + Elemental Equilibrium: o loop das infusões.", "Siphon Elements + Elemental Equilibrium: the infusion loop."),
 40: L("2ª ascendência: Wisdom of the Maji (runas passam a dar a linha Bonded).", "2nd ascendancy: Wisdom of the Maji (runes start granting their Bonded line)."),
 49: L("Lavianga's Spirits: flask de mana com efeito constante.", "Lavianga's Spirits: mana flask with a constant effect."),
 50: L("Archmage (Uncut nível 14, 100 de Spirit): mana vira dano. Uhtred's Chalice.", "Archmage (level 14 Uncut, 100 Spirit): mana becomes damage. Uhtred's Chalice."),
 52: L("Eldritch Battery + Mind Over Matter: ES vira mana e a mana vira sua vida.", "Eldritch Battery + Mind Over Matter: ES becomes mana and mana becomes your life."),
 58: L("Sire of Shards: TODA spell dispara 4 projéteis a mais, em círculo.", "Sire of Shards: EVERY spell fires 4 extra projectiles, in a circle."),
 60: L("Olroth's Resolve: Guard igual ao seu Runic Ward quando o flask acaba.", "Olroth's Resolve: Guard equal to your Runic Ward when the flask ends."),
 65: L("Cast on Critical + Comet: o Comet passa a cair sozinho.", "Cast on Critical + Comet: Comet starts falling on its own."),
 68: L("3ª ascendência: Reactive Growth (10% less dano elemental + Adaptations).", "3rd ascendancy: Reactive Growth (10% less elemental damage + Adaptations)."),
 75: L("Rathpith Globe: crítico por vida máxima e Low Life permanente.", "Rathpith Globe: crit per maximum life and permanent Low Life."),
 80: L("4ª ascendência: Avatar of Evolution (Adaptation dobrada).", "4th ascendancy: Avatar of Evolution (doubled Adaptation)."),
 85: L("Pain Attunement + Execute III + Final Barrage: o pacote de Low Life.", "Pain Attunement + Execute III + Final Barrage: the Low Life package."),
 93: L("Runeseeker's Call, Mageblood e Kalandra's Touch.", "Runeseeker's Call, Mageblood and Kalandra's Touch."),
}

ASCENDANCY = [
 dict(order=1, key="sacred", node="Sacred Flow", when=L("1º Trial (~nível 25)", "1st Trial (~level 25)"), text=L("+40 de Spirit para cada slot de charm vazio.", "+40 to Spirit for each of your empty Charm slots."), why=L("É o seu segundo (e maior) bloco de Spirit. Dois slots vazios = +80, o que paga o Arctic Armour e o Siphon Elements na campanha e ajuda a caber Archmage + Cast on Critical depois.", "It's your second (and biggest) block of Spirit. Two empty slots = +80, which pays for Arctic Armour and Siphon Elements in the campaign and helps fit Archmage + Cast on Critical later.")),
 dict(order=2, key="maji", node="Wisdom of the Maji", when=L("2º Trial (~nível 40)", "2nd Trial (~level 40)"), text=L("Você recebe os benefícios dos modificadores Bonded de Runes e Idols.", "Gain the benefits of Bonded modifiers on Runes and Idols."), why=L("Cada runa barata que você socketa passa a dar também a linha 'Bonded' (vida e mana). É o upgrade mais barato da build inteira: runas custam alguns exalted.", "Every cheap rune you socket also grants its 'Bonded' line (life and mana). It's the cheapest upgrade in the whole build: runes cost a few exalted.")),
 dict(order=3, key="reactive", node="Reactive Growth", when=L("3º Trial (~nível 68)", "3rd Trial (~level 68)"), text=L("10% less dano elemental tomado; você se adapta ao tipo elemental mais alto de cada hit que toma e toma 10% less dano daquele tipo por adaptação.", "10% less elemental damage taken; you adapt to the highest elemental damage type of each hit you take and take 10% less damage of each matching type per adaptation."), why=L("A defesa do endgame: o mapa te bate uma vez e você passa a tomar muito menos daquele elemento.", "Your endgame defence: the map hits you once and you start taking much less of that element.")),
 dict(order=4, key="avatar", node="Avatar of Evolution", when=L("4º Trial (~nível 80)", "4th Trial (~level 80)"), text=L("5% do dano físico tomado como fogo, frio e raio; Adaptations duram 5 s; efeito de Adaptation dobrado.", "5% of physical damage taken as fire, cold and lightning; Adaptations last 5 s; double Adaptation effect."), why=L("Dobra o Reactive Growth e ainda faz o dano físico virar elemental — que é justamente o que você reduz.", "Doubles Reactive Growth and also turns physical damage into elemental damage — exactly what you reduce.")),
]
ASC_UNLOCK = [25, 40, 68, 80]

KEY_PASSIVES = [
 dict(node="Elemental Equilibrium", type="Keystone", text=L("Cria Infusion Remnants de raio no lugar de fogo, de frio no lugar de raio e de fogo no lugar de frio.", "Create Lightning Infusion Remnants instead of Fire, Cold instead of Lightning and Fire instead of Cold."), when="36+", why=L("O Shock do Spark passa a criar infusão de frio (que o Spark consome) e o Freeze do Comet cria infusão de fogo (que o Comet consome).", "Spark's Shock starts creating cold infusions (which Spark consumes) and Comet's Freeze creates fire infusions (which Comet consumes).")),
 dict(node="Eldritch Battery", type="Keystone", text=L("Converte 100% do Energy Shield máximo em mana máxima; custos de mana são dobrados.", "Convert 100% of maximum Energy Shield to maximum Mana; mana costs are doubled."), when="52+", why=L("Todo item de ES vira mana — e mana é dano (Archmage) e defesa (Mind Over Matter).", "Every ES item becomes mana — and mana is damage (Archmage) and defence (Mind Over Matter).")),
 dict(node="Mind Over Matter", type="Keystone", text=L("Todo dano é tomado da mana antes da vida; 50% less de recuperação de mana.", "All damage is taken from mana before life; 50% less mana recovery rate."), when="52+", why=L("Sua barra azul vira sua vida real. Por isso Mana Remnants e os flasks de mana são itens de defesa.", "Your blue bar becomes your real health. That's why Mana Remnants and mana flasks are defensive items.")),
 dict(node="Pain Attunement", type="Keystone", text=L("30% less dano crítico com a vida cheia; 30% more dano crítico em Low Life.", "30% less crit damage on full life; 30% more crit damage on Low Life."), when="85+", why=L("Só depois do Rathpith Globe, que te mantém em Low Life de propósito. Antes disso, é perda de dano.", "Only after Rathpith Globe, which keeps you on Low Life on purpose. Before that, it's a damage loss.")),
 dict(node="Arcane Intensity", type="Notable", text=L("3% increased Spell Damage por 100 de mana máxima.", "3% increased Spell Damage per 100 maximum mana."), when="16+", why=L("O primeiro nó que transforma mana em dano, muito antes do Archmage.", "The first node that turns mana into damage, long before Archmage.")),
 dict(node="Final Barrage", type="Notable", text=L("20% increased Cast Speed em Low Life; 10% reduced com a vida cheia.", "20% increased Cast Speed when on Low Life; 10% reduced on full life."), when="85+", why=L("Combina com o pacote Rathpith: mais casts = mais críticos = mais Comet.", "Pairs with the Rathpith package: more casts = more crits = more Comet.")),
 dict(node="Invocated Efficiency", type="Notable", text=L("10% increased Mana Cost Efficiency; spells disparadas dão 40% increased Spell Damage.", "10% increased Mana Cost Efficiency; triggered spells deal 40% increased Spell Damage."), when="65+", why=L("O Comet do Cast on Critical é uma spell disparada: é dano direto no gatilho.", "Cast on Critical's Comet is a triggered spell: direct damage on your trigger.")),
 dict(node="Remnant Attraction", type="Notable", text=L("10% de chance de criar um Remnant adicional; Remnants podem ser coletados de 50% mais longe.", "10% chance to create an additional Remnant; Remnants can be collected from 50% further away."), when="36+", why=L("Mais mana e mais infusão sem parar de andar.", "More mana and more infusions without stopping to walk over them.")),
]
TREE_STAGES = [
 dict(lv="1–31", focus=L("Mana e raio do começo do Druid", "Druid start: mana and lightning"), dmg="Spark (Chain I → Nova Projectiles I)", **{"def": L("Vida + resistências", "Life + resistances")}, spirit="Mana Remnants · Arctic Armour", dont=L("Gastar em arma cara", "Spending on an expensive weapon")),
 dict(lv="32–51", focus="Elemental Equilibrium · Chakra of Elements", dmg="Spark + Comet", **{"def": L("Vida + Remnants", "Life + Remnants")}, spirit="+ Siphon Elements", dont=L("EE sem Siphon Elements", "EE without Siphon Elements")),
 dict(lv="52–79", focus="Eldritch Battery · Mind Over Matter · Arcane Intensity", dmg="Archmage → Cast on Critical", **{"def": L("Mana como vida", "Mana as life")}, spirit="Archmage (100) · CoC (100)", dont=L("Archmage sem resistência no cap", "Archmage without capped resistances")),
 dict(lv="80–100", focus="Pain Attunement · Final Barrage · crítico", dmg="Comet automático", **{"def": "Reactive Growth · Avatar of Evolution"}, spirit=L("290+ com Reservation Efficiency", "290+ with Reservation Efficiency"), dont=L("Pain Attunement sem Rathpith", "Pain Attunement without Rathpith")),
]

UNIQUES = [
 U("Threaded Light", "Focus", L("Armadura", "Armour"), "a1", L("50–70% ES, 30–40% de regeneração de mana e 8–12% de dano de spell por 10 de Spirit.", "50–70% ES, 30–40% mana regeneration and 8–12% spell damage per 10 Spirit."), L("Primeiro item da build: dano de spell escalando com o Spirit que as quests vão te dar.", "The build's first item: spell damage scaling with the Spirit the quests are about to give you."), L("Focus rare com mana e ES.", "Rare focus with mana and ES."), lvl=6),
 U("Stone of Lazhwar", L("Amuleto", "Amulet"), L("Acessório", "Accessory"), "a1", L("+50–99 de mana máxima, 15–25% de cast speed e block com Focus.", "+50–99 maximum mana, 15–25% cast speed and block while holding a Focus."), L("Mana máxima + cast speed em um amuleto de alguns exalted: exatamente as duas estatísticas da build.", "Maximum mana + cast speed on an amulet worth a few exalted: exactly the build's two stats."), L("Amuleto rare com mana.", "Rare amulet with mana."), lvl=8),
 U("Goldrim", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a1", L("+25–33% em TODAS as resistências elementais e raridade.", "+25–33% to ALL elemental resistances and rarity."), L("Resolve resistência sozinho do nível 10 até o Ato 3.", "Solves resistances by itself from level 10 to Act 3."), L("Capacete com vida/ES.", "Helmet with life/ES."), lvl=10),
 U("Wanderlust", L("Botas", "Boots"), L("Armadura", "Armour"), "a1", L("20% de Movement Speed, ES e imunidade a Slow.", "20% Movement Speed, ES and slow immunity."), L("Velocidade de campanha barata; a imunidade a Slow salva em chão congelado.", "Cheap campaign speed; the slow immunity saves you on chilled ground."), L("Botas com Movement Speed.", "Boots with Movement Speed."), lvl=11),
 U("Dream Fragments", L("Anel", "Ring"), L("Acessório", "Accessory"), "a1", L("10–15% de mana máxima, 30–50% de regeneração de mana e você não pode ser Chilled nem Frozen.", "10–15% maximum mana, 30–50% mana regeneration and you cannot be Chilled or Frozen."), L("Mana em %, que cresce junto com a build, e imunidade a Freeze — que é metade das mortes da campanha.", "Percentage mana, which grows with the build, and freeze immunity — half of all campaign deaths."), L("Anel com mana e resistência.", "Ring with mana and resistance."), lvl=12),
 U("Doedre's Tenure", L("Luvas", "Gloves"), L("Armadura", "Armour"), "a2", L("+20–30 de ES, 100% increased Spell Damage, 16–25% reduced Cast Speed e +10–15 de Inteligência.", "+20–30 ES, 100% increased Spell Damage, 16–25% reduced cast speed and +10–15 Intelligence."), L("100% de dano de spell por ~0,003 divine. O cast speed a menos dói pouco enquanto o Spark ainda faz o trabalho por chain.", "100% spell damage for ~0.003 divine. The lost cast speed barely matters while Spark still does the work through chaining."), L("Luvas com mana e resistência.", "Gloves with mana and resistance."), lvl=16),
 U("Serpent's Lesson", "Focus", L("Armadura", "Armour"), "a2", L("+60–100 de vida, +60–100 de mana; você conta como em Low Life com 35% ou menos de mana (e como Low Mana com 35% ou menos de vida).", "+60–100 life, +60–100 mana; you count as on Low Life at 35% mana or below (and as on Low Mana at 35% life or below)."), L("Vida e mana no mesmo item barato. Guarde: no endgame ele vira uma alternativa ao Rathpith para ligar o pacote de Low Life.", "Life and mana on one cheap item. Keep it: in endgame it becomes an alternative to Rathpith for switching on the Low Life package."), "Threaded Light", lvl=22),
 U("Astramentis", L("Amuleto", "Amulet"), L("Acessório", "Accessory"), "a2", L("+50–95 em todos os atributos e −4 de dano físico de ataques.", "+50–95 to all attributes and −4 physical damage taken from attack hits."), L("Atributo é o que trava gem no meio da campanha: com ele, qualquer support entra.", "Attributes are what block gems mid-campaign: with this, every support fits."), "Stone of Lazhwar", lvl=24),
 U("The Eternal Spark", "Focus", L("Armadura", "Armour"), "a2", L("50–70% de ES, +5% de resistência MÁXIMA a raio, +20–30% de resistência a raio e 40% de regeneração de mana (mais 40% parado).", "50–70% ES, +5% MAXIMUM lightning resistance, +20–30% lightning resistance and 40% mana regeneration (plus 40% while stationary)."), L("Resistência máxima é raríssimo em item barato: +5% de max raio vale por muita vida no endgame.", "Maximum resistance is very rare on a cheap item: +5% max lightning is worth a lot of effective life later."), "Serpent's Lesson", lvl=26),
 U("Snakepit", L("Anel", "Ring"), L("Acessório", "Accessory"), "a3", L("20–30% de dano de spell, 10–15% de cast speed; no slot direito, projéteis de spell dão Chain +1.", "20–30% spell damage, 10–15% cast speed; in the right slot, spell projectiles Chain +1 time."), L("No anel DIREITO ele dá um chain a mais para todo spark — clear de graça. No esquerdo, os projéteis passam a dar Fork.", "In the RIGHT ring it grants one more chain to every spark — free clear. In the left, projectiles Fork instead."), "Dream Fragments", lvl=32),
 U("The Everlasting Gaze", L("Amuleto", "Amulet"), L("Acessório", "Accessory"), "a3", L("+40–60 de mana, 40–60% de regeneração de mana e ganha 4–6% da mana máxima como ES máximo extra.", "+40–60 mana, 40–60% mana regeneration and gain 4–6% of maximum mana as extra maximum ES."), L("Depois do Eldritch Battery o ES volta a virar mana: o amuleto faz mana gerar mana.", "After Eldritch Battery the ES turns back into mana: the amulet makes mana generate mana."), "Astramentis", lvl=0),
 U("Ghostwrithe", "Body Armour", L("Armadura", "Armour"), "a4", L("+100 de ES, +29–37% de resistência a caos e 35% da vida máxima convertida em ES.", "+100 ES, +29–37% chaos resistance and 35% of maximum life converted to ES."), L("Com Eldritch Battery, ES é mana: este peito converte parte da sua vida direto em mana (dano e defesa).", "With Eldritch Battery, ES is mana: this chest converts part of your life straight into mana (damage and defence)."), L("Peito rare de ES e mana.", "Rare ES and mana chest."), lvl=0),
 U("Lavianga's Spirits", L("Flask de mana", "Mana flask"), "Flask", "a4", L("Não pode ser usado, mas aplica o efeito o tempo todo; 70–80% reduced de recuperação.", "Cannot be used, but applies its effect constantly; 70–80% reduced amount recovered."), L("Recuperação de mana permanente, sem apertar botão — com Mind Over Matter isso é regeneração de vida.", "Permanent mana recovery with no button press — with Mind Over Matter that's life regeneration."), L("Flask de mana normal.", "Normal mana flask."), lvl=49),
 U("Uhtred's Chalice", L("Flask de mana", "Mana flask"), "Flask", "a4", L("200–297% increased de recuperação, 70% reduced de velocidade de recuperação; a recuperação de mana de flasks pode passar do máximo durante o efeito.", "200–297% increased amount recovered, 70% reduced recovery rate; mana recovery from flasks can overflow your maximum during the effect."), L("Passar do máximo de mana = passar do teto de dano do Archmage. 7 dos 10 do ladder usam.", "Overflowing your maximum mana = overflowing Archmage's damage ceiling. 7 of the 10 ladder characters use it."), "Lavianga's Spirits", lvl=50),
 U("Sire of Shards", L("Cajado", "Staff"), L("Arma", "Weapon"), "a4", L("80–119% de dano de spell, 10–20% de cast speed, +5–10% em todas as resistências; spells disparam 4 projéteis a mais e disparam projéteis em círculo.", "80–119% spell damage, 10–20% cast speed, +5–10% to all resistances; spells fire 4 additional projectiles and fire projectiles in a circle."), L("O item que faz a build parecer ridícula, e custa menos de 0,01 divine: o Spark sai em círculo com 4 projéteis a mais, sem gastar support.", "The item that makes the build look ridiculous, and it costs less than 0.01 divine: Spark comes out in a circle with 4 extra projectiles, without spending a support."), L("Cajado rare com % dano de spell e mana.", "Rare staff with % spell damage and mana."), lvl=58),
 U("Olroth's Resolve", L("Flask de vida", "Life flask"), "Flask", "a4", L("105–149% increased de cargas por uso; regenera 2,5–4,6% do Runic Ward máximo durante o efeito e dá Guard igual ao Runic Ward atual por 10 s quando acaba.", "105–149% increased charges per use; regenerates 2.5–4.6% of maximum Runic Ward per second during the effect and grants Guard equal to your current Runic Ward for 10 s when it ends."), L("Botão de pânico: acaba o flask e você ganha um escudo do tamanho do seu Runic Ward.", "Panic button: the flask ends and you gain a shield the size of your Runic Ward."), L("Flask de vida normal.", "Normal life flask."), lvl=60),
 U("Cloak of Defiance", "Body Armour", L("Armadura", "Armour"), "maps", L("50–100% de ES, +100–149 de mana, 50–100% de regeneração de mana e 50% do dano é tomado da mana antes da vida.", "50–100% ES, +100–149 mana, 50–100% mana regeneration and 50% of damage is taken from mana before life."), L("Peito de mapa barato: mana, ES (que vira mana) e mais mitigação por mana em cima do Mind Over Matter.", "Cheap mapping chest: mana, ES (which becomes mana) and more mana mitigation on top of Mind Over Matter."), "Ghostwrithe", lvl=65),
 U("Indigon", L("Capacete", "Helmet"), L("Armadura", "Armour"), "maps", L("100–140% de ES, +80–118 de mana; custo das skills e dano de spell sobem conforme a mana gasta recentemente.", "100–140% ES, +80–118 mana; skill cost and spell damage both scale with mana spent recently."), L("Opção avançada: com Archmage você gasta mana muito rápido, então o dano sobe rápido — e o custo também. Só com muita recuperação de mana.", "Advanced option: with Archmage you spend mana very fast, so the damage climbs fast — and so does the cost. Only with plenty of mana recovery."), L("Ancestral Tiara rare (ES + mana).", "Rare Ancestral Tiara (ES + mana)."), lvl=65),
 U("Rathpith Globe", "Focus", L("Armadura", "Armour"), "maps", L("60–100% de ES, +60–100 de vida; spells não-canalizadas custam 6% da vida máxima a mais e têm 3% de crítico por 100 de vida máxima.", "60–100% ES, +60–100 life; non-channelling spells cost an additional 6% of maximum life and have 3% increased crit chance per 100 maximum life."), L("Dois em um: dá o crítico que o Cast on Critical precisa e te deixa em Low Life de propósito (Pain Attunement, Execute III, Final Barrage). 10 dos 10 do ladder usam.", "Two in one: it gives the crit Cast on Critical needs and puts you on Low Life on purpose (Pain Attunement, Execute III, Final Barrage). 10 of the 10 ladder characters use it."), "The Eternal Spark", lvl=75),
 U("Taryn's Shiver", L("Cajado", "Staff"), L("Arma", "Weapon"), "endgame", L("80–120% de dano de spell, 10–20% de cast speed, 30% de Freeze Buildup; inimigos congelados por você tomam 100% increased de dano.", "80–120% spell damage, 10–20% cast speed, 30% freeze buildup; enemies you freeze take 100% increased damage."), L("Cajado de troca para boss: o Comet congela, e congelado toma 100% increased de dano. Custa quase nada.", "Boss swap staff: Comet freezes, and frozen enemies take 100% increased damage. Costs almost nothing."), "Sire of Shards", lvl=66),
 U("Rite of Passage", "Charm", "Charm", "endgame", L("Possessão por espíritos (Cat, Stag, Boar, Serpent...) ao usar.", "Spirit possession (Cat, Stag, Boar, Serpent...) on use."), L("7 dos 10 do ladder usam. Lembre do preço escondido: ocupar um slot de charm custa 40 de Spirit do Sacred Flow.", "7 of the 10 ladder characters use it. Remember the hidden price: filling a charm slot costs 40 Spirit from Sacred Flow."), L("Slot vazio (+40 de Spirit).", "Empty slot (+40 Spirit)."), lvl=50),
 U("Kalandra's Touch", L("Anel", "Ring"), L("Acessório", "Accessory"), "max", L("Reflete o anel oposto.", "Reflects the opposite ring."), L("Duplica o seu melhor anel de mana (Mnemonic Ring): mana dobrada é dano dobrado do Archmage.", "Duplicates your best mana ring (Mnemonic Ring): doubled mana is doubled Archmage damage."), "Snakepit", lvl=0),
 U("Runeseeker's Call", L("Cajado", "Staff"), L("Arma", "Weapon"), "max", L("Só runas podem ser socketadas; 200% increased do efeito das runas socketadas (na versão Runemastered: +mana máxima gigante e + níveis de spell).", "Only runes can be socketed; 200% increased effect of socketed runes (the Runemastered version also carries huge +maximum mana and + spell levels)."), L("A arma dos 10 do ladder. Com Wisdom of the Maji, cada runa dá efeito triplicado E a linha Bonded.", "The weapon all 10 ladder characters use. With Wisdom of the Maji every rune gives triple effect AND its Bonded line."), "Sire of Shards", lvl=90),
 U("Mageblood", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Mantém os flasks de utilidade sempre ativos e tem 2 slots de charm.", "Keeps utility flasks permanently active and has 2 charm slots."), L("Flasks permanentes (inclusive os de mana). Conta o Spirit antes: com Sacred Flow, cada charm equipado custa 40.", "Permanent flasks (including the mana ones). Do the Spirit math first: with Sacred Flow every equipped charm costs 40."), L("Cinto rare com vida e resistências.", "Rare belt with life and resistances."), lvl=55),
 U("Temporalis", "Body Armour", L("Armadura", "Armour"), "max", L("+100–148 de ES, +10–20% em todas as resistências, recoup de vida e mana e −2 s no cooldown das skills.", "+100–148 ES, +10–20% to all resistances, life and mana recoup and −2 s to skill cooldowns."), L("O luxo absoluto: Blink praticamente sem cooldown e recoup de mana (que é sua vida).", "The absolute luxury: Blink with practically no cooldown and mana recoup (which is your life)."), "Cloak of Defiance", lvl=64),
]

GEAR = [
 dict(slot=L("Cajado", "Staff"), cheap=L("Cajado Magic do vendor com % dano de spell", "Vendor magic staff with % spell damage"), value="Sire of Shards (58)", full=L("Runeseeker's Call (Runemastered) · Taryn's Shiver para boss", "Runeseeker's Call (Runemastered) · Taryn's Shiver for bosses"),
      affix=L("% dano de spell; +mana máxima; cast speed; + níveis de spell", "% spell damage; +maximum mana; cast speed; + spell levels"),
      lvls=[dict(lv=1, n=L("Cajado Magic com dano de spell", "Magic staff with spell damage")), dict(lv=32, n=L("Cajado rare: % spell + mana", "Rare staff: % spell + mana")), dict(lv=58, n="Sire of Shards"), dict(lv=66, n="Taryn's Shiver"), dict(lv=90, n="Runeseeker's Call")],
      note=L("Compre um cajado Magic novo em todo ato: é a maior fonte de dano barata da campanha.", "Buy a new magic staff every act: it's the campaign's biggest cheap damage source.")),
 dict(slot="Focus", cheap="Threaded Light (6) · Serpent's Lesson (22)", value="The Eternal Spark (26)", full="Rathpith Globe (75)",
      affix=L("% ES; +mana máxima; resistências; crítico para spells", "% ES; +maximum mana; resistances; spell crit"),
      lvls=[dict(lv=6, n="Threaded Light"), dict(lv=22, n="Serpent's Lesson"), dict(lv=26, n="The Eternal Spark"), dict(lv=75, n="Rathpith Globe")],
      note=L("O Focus é onde mora o ES — e com Eldritch Battery o ES é mana.", "The focus is where your ES lives — and with Eldritch Battery ES is mana.")),
 dict(slot=L("Amuleto", "Amulet"), cheap="Stone of Lazhwar (8)", value="Astramentis (24) · The Everlasting Gaze", full=L("Absent Amulet: +Spirit, + níveis de spell, Zarokh's Gift", "Absent Amulet: +Spirit, + spell levels, Zarokh's Gift"),
      affix=L("+Spirit; +mana máxima; + níveis de spell; cast speed", "+Spirit; +maximum mana; + spell levels; cast speed"),
      lvls=[dict(lv=8, n="Stone of Lazhwar"), dict(lv=24, n="Astramentis"), dict(lv=50, n="The Everlasting Gaze"), dict(lv=65, n=L("Rare com +Spirit e mana", "Rare with +Spirit and mana")), dict(lv=85, n=L("Absent Amulet (+níveis de spell)", "Absent Amulet (+spell levels)"))],
      note=L("Spirit no amuleto é o que faz Archmage e Cast on Critical caberem juntos.", "Amulet Spirit is what makes Archmage and Cast on Critical fit together.")),
 dict(slot=L("Capacete", "Helmet"), cheap="Goldrim (10)", value=L("Ancestral Tiara rare: ES + mana", "Rare Ancestral Tiara: ES + mana"), full=L("Ancestral Tiara com crítico para spells · Indigon (avançado)", "Ancestral Tiara with spell crit · Indigon (advanced)"),
      affix=L("% ES; +mana máxima; crítico; resistências", "% ES; +maximum mana; crit; resistances"),
      lvls=[dict(lv=10, n="Goldrim"), dict(lv=45, n=L("Capacete rare: ES + mana + resist", "Rare helmet: ES + mana + resist")), dict(lv=65, n=L("Ancestral Tiara (ES + mana)", "Ancestral Tiara (ES + mana)")), dict(lv=80, n=L("Ancestral Tiara com crítico", "Ancestral Tiara with crit"))],
      note=L("Socket de runa: resistência que faltar (a Bonded do Wisdom of the Maji dá vida e mana junto).", "Rune socket: whatever resistance you're missing (Wisdom of the Maji's Bonded adds life and mana too).")),
 dict(slot="Body Armour", cheap=L("Peito rare com ES e resistências", "Rare chest with ES and resistances"), value="Ghostwrithe · Cloak of Defiance (65)", full=L("Vile Robe rare: ES + mana + Spirit · Temporalis", "Rare Vile Robe: ES + mana + Spirit · Temporalis"),
      affix=L("% ES; +mana máxima; +Spirit; resistências", "% ES; +maximum mana; +Spirit; resistances"),
      lvls=[dict(lv=1, n=L("Peito com ES e vida", "Chest with ES and life")), dict(lv=40, n="Ghostwrithe"), dict(lv=65, n="Cloak of Defiance"), dict(lv=80, n=L("Vile Robe rare (ES + mana + Spirit)", "Rare Vile Robe (ES + mana + Spirit)"))],
      note=L("Greater Iron Rune ×2 — com Wisdom of the Maji cada uma vale duas.", "Greater Iron Rune ×2 — with Wisdom of the Maji each one counts double.")),
 dict(slot=L("Luvas", "Gloves"), cheap="Doedre's Tenure (16)", value=L("Luvas rare: mana + cast speed", "Rare gloves: mana + cast speed"), full=L("Sirenscale Gloves: + níveis de projétil e mana", "Sirenscale Gloves: + projectile levels and mana"),
      affix=L("+mana máxima; cast speed; + níveis de skills de projétil; resistências", "+maximum mana; cast speed; + projectile skill levels; resistances"),
      lvls=[dict(lv=16, n="Doedre's Tenure"), dict(lv=45, n=L("Luvas rare: mana + resist", "Rare gloves: mana + resist")), dict(lv=75, n=L("Sirenscale Gloves (+2 projétil)", "Sirenscale Gloves (+2 projectile)"))],
      note=L("'+ níveis de skills de projétil' vale para o Spark (projétil), não para o Comet.", "'+ projectile skill levels' applies to Spark (a projectile), not to Comet.")),
 dict(slot=L("Botas", "Boots"), cheap="Wanderlust (11)", value=L("Botas rare: 30% MS + mana", "Rare boots: 30% MS + mana"), full=L("35% de Movement Speed + mana + resistências", "35% Movement Speed + mana + resistances"),
      affix=L("Movement Speed; +mana máxima; resistências; ES", "Movement Speed; +maximum mana; resistances; ES"),
      lvls=[dict(lv=11, n="Wanderlust"), dict(lv=45, n=L("Botas rare: 25–30% MS", "Rare boots: 25–30% MS")), dict(lv=75, n=L("Botas: 35% MS + mana", "Boots: 35% MS + mana"))],
      note=""),
 dict(slot=L("Anéis", "Rings"), cheap="Dream Fragments (12)", value="Snakepit (32, anel direito)", full=L("Mnemonic Ring (mana + eficiência) · Kalandra's Touch", "Mnemonic Ring (mana + efficiency) · Kalandra's Touch"),
      affix=L("+mana máxima; % mana máxima; regeneração e eficiência de custo; resistências", "+maximum mana; % maximum mana; regeneration and cost efficiency; resistances"),
      lvls=[dict(lv=12, n="Dream Fragments"), dict(lv=32, n="Snakepit"), dict(lv=65, n=L("Mnemonic Ring (mana)", "Mnemonic Ring (mana)")), dict(lv=93, n="Kalandra's Touch")],
      note=L("Snakepit no anel DIREITO: chain +1 nos projéteis de spell.", "Snakepit in the RIGHT ring: +1 chain on spell projectiles.")),
 dict(slot=L("Cinto", "Belt"), cheap=L("Cinto com vida e resistências", "Belt with life and resistances"), value=L("Cinto rare: vida + mana + resist", "Rare belt: life + mana + resist"), full="Mageblood",
      affix=L("Vida; mana; resistências; slots de charm (cuidado com o Sacred Flow)", "Life; mana; resistances; charm slots (mind Sacred Flow)"),
      lvls=[dict(lv=1, n=L("Cinto com vida", "Belt with life")), dict(lv=45, n=L("Cinto rare: vida + resist", "Rare belt: life + resist")), dict(lv=93, n="Mageblood")],
      note=L("Slot de charm VAZIO = +40 de Spirit (Sacred Flow). Só encha se o que entrar valer mais que 40 de Spirit.", "An EMPTY charm slot = +40 Spirit (Sacred Flow). Only fill it if what goes in is worth more than 40 Spirit.")),
 dict(slot="Charms / Flasks", cheap=L("Flask de vida e de mana normais", "Normal life and mana flasks"), value="Lavianga's Spirits (49) · Uhtred's Chalice (50)", full="Olroth's Resolve (60) · Rite of Passage",
      affix=L("Recuperação de mana (com Mind Over Matter, isso é cura)", "Mana recovery (with Mind Over Matter, that's healing)"),
      lvls=[dict(lv=1, n=L("Flask de mana Magic", "Magic mana flask")), dict(lv=49, n="Lavianga's Spirits"), dict(lv=50, n="Uhtred's Chalice"), dict(lv=60, n="Olroth's Resolve"), dict(lv=85, n="Rite of Passage")],
      note=L("Flask de mana é item de defesa nesta build.", "A mana flask is a defensive item in this build.")),
]

BUY_ORDER = [
 dict(p=1, item="Threaded Light · Stone of Lazhwar", phase="6–8", cost=L("Barato", "Cheap"), impact=L("Mana e dano de spell desde o Ato 1", "Mana and spell damage from Act 1")),
 dict(p=2, item="Goldrim · Wanderlust · Dream Fragments", phase="10–12", cost=L("Barato", "Cheap"), impact=L("Resistências, velocidade e imunidade a Freeze", "Resistances, speed and freeze immunity")),
 dict(p=3, item="Doedre's Tenure", phase="16", cost=L("Barato", "Cheap"), impact=L("100% de dano de spell", "100% spell damage")),
 dict(p=4, item="Astramentis · The Eternal Spark", phase="24–26", cost=L("Barato", "Cheap"), impact=L("Atributos e resistência máxima", "Attributes and maximum resistance")),
 dict(p=5, item="Sire of Shards", phase="58", cost=L("Barato", "Cheap"), impact=L("4 projéteis extras em círculo", "4 extra projectiles in a circle")),
 dict(p=6, item="Lavianga's Spirits · Uhtred's Chalice", phase="49–50", cost=L("Barato", "Cheap"), impact=L("Mana constante = vida constante", "Constant mana = constant life")),
 dict(p=7, item=L("Amuleto/peito com +Spirit", "+Spirit amulet/chest"), phase="65", cost=L("Valor", "Value"), impact=L("Cast on Critical junto do Archmage", "Cast on Critical alongside Archmage")),
 dict(p=8, item="Rathpith Globe", phase="75", cost=L("Valor", "Value"), impact=L("Crítico + pacote de Low Life", "Crit + the Low Life package")),
 dict(p=9, item=L("Rares de mana (Ancestral Tiara, Vile Robe, Mnemonic Ring)", "Mana rares (Ancestral Tiara, Vile Robe, Mnemonic Ring)"), phase="80", cost=L("Valor", "Value"), impact=L("Mana máxima = dano", "Maximum mana = damage")),
 dict(p=10, item="Kalandra's Touch", phase="93", cost=L("Luxo", "Luxury"), impact=L("Duplica o melhor anel", "Duplicates your best ring")),
 dict(p=11, item="Runeseeker's Call · Mageblood", phase="95+", cost=L("Luxo", "Luxury"), impact="Min-max"),
]

TRICKS = [
 {"cat": L("Clear", "Clear"), "lvl": L("Fácil", "Easy"), "title": L("Um botão só", "One button"), "body": L("Do nível 1 ao 100 o clear é: andar segurando o Spark. Tudo o que muda é quantos projéteis saem (Chain I → Nova Projectiles I → Sire of Shards) e quem cai do céu junto (Comet no Cast on Critical).", "From level 1 to 100 the clear is: walk while holding Spark. All that changes is how many projectiles come out (Chain I → Nova Projectiles I → Sire of Shards) and what falls from the sky with them (Comet on Cast on Critical).")},
 {"cat": L("Infusões", "Infusions"), "lvl": L("Médio", "Medium"), "title": L("Shock vira frio, Freeze vira fogo", "Shock becomes cold, Freeze becomes fire"), "body": L("Siphon Elements cria uma infusão quando você aplica um ailment; Elemental Equilibrium troca o tipo criado. Resultado: seu Shock (Spark) cria a infusão de FRIO que o Spark consome, e seu Freeze (Comet) cria a infusão de FOGO que o Comet consome. Você nunca fica sem.", "Siphon Elements creates an infusion when you apply an ailment; Elemental Equilibrium swaps the type created. The result: your Shock (Spark) creates the COLD infusion that Spark consumes, and your Freeze (Comet) creates the FIRE infusion that Comet consumes. You never run dry.")},
 {"cat": "Spirit", "lvl": L("Fácil", "Easy"), "title": L("Slot de charm vazio = 40 de Spirit", "Empty charm slot = 40 Spirit"), "body": L("Sacred Flow paga 40 de Spirit por slot de charm VAZIO. Antes de equipar qualquer charm (inclusive o Rite of Passage), pergunte: isso vale mais que 40 de Spirit? Muitas vezes vale mais deixar vazio e ligar outro buff.", "Sacred Flow pays 40 Spirit per EMPTY charm slot. Before equipping any charm (including Rite of Passage), ask: is this worth more than 40 Spirit? Often leaving it empty and running another buff is worth more.")},
 {"cat": L("Mana", "Mana"), "lvl": L("Médio", "Medium"), "title": L("Sua barra azul é sua vida", "Your blue bar is your life"), "body": L("Com Mind Over Matter o dano sai da mana antes da vida, e com Eldritch Battery o ES já virou mana. Então: flask de mana é poção de vida, Mana Remnants é regeneração e 'ficar sem mana' significa 'ficar sem defesa'. Recue e deixe encher.", "With Mind Over Matter damage comes out of mana before life, and with Eldritch Battery your ES has already become mana. So: a mana flask is a health potion, Mana Remnants is regeneration, and 'out of mana' means 'out of defence'. Back off and let it refill.")},
 {"cat": L("Boss", "Boss"), "lvl": L("Médio", "Medium"), "title": L("Comet não precisa de mira", "Comet doesn't need aiming"), "body": L("Nos mapas quem lança o Comet é o Cast on Critical: você fica colado no boss segurando o Spark e o Comet cai em cima. Lançar o Comet na mão só vale quando o boss está parado (pós-mecânica) e você quer empurrar dano.", "In maps Cast on Critical casts Comet for you: you stand close to the boss holding Spark and Comet lands on top of it. Casting Comet manually is only worth it when the boss is stationary (post-mechanic) and you want to push damage.")},
 {"cat": L("Crítico", "Crit"), "lvl": L("Médio", "Medium"), "title": L("Muitos projéteis = muitos críticos", "Many projectiles = many crits"), "body": L("O Cast on Critical não liga para o seu dano por hit: ele conta críticos. Como o Spark dispara dezenas de projéteis (Nova + Sire of Shards), mesmo 20% de chance de crítico enche a barra rápido. Por isso Rathpith (crítico por vida) é tão forte aqui.", "Cast on Critical doesn't care about your damage per hit: it counts crits. Since Spark fires dozens of projectiles (Nova + Sire of Shards), even 20% crit chance fills the bar fast. That's why Rathpith (crit per life) is so strong here.")},
 {"cat": L("Runas", "Runes"), "lvl": L("Fácil", "Easy"), "title": L("Runas valem dobrado", "Runes count double"), "body": L("Depois do Wisdom of the Maji, toda runa socketada também dá a linha 'Bonded' dela (normalmente vida e mana). Encha todos os sockets com runas baratas de resistência: é o upgrade mais barato da build.", "After Wisdom of the Maji, every socketed rune also grants its 'Bonded' line (usually life and mana). Fill every socket with cheap resistance runes: it's the cheapest upgrade in the build.")},
 {"cat": L("Campanha", "Campaign"), "lvl": L("Fácil", "Easy"), "title": L("Cajado novo a cada ato", "A new staff every act"), "body": L("Você não precisa de arma unique na campanha: um cajado Magic do vendor com '% increased Spell Damage' e mana já dobra seu dano. Compre um novo em todo ato até o Sire of Shards (58).", "You don't need a unique weapon in the campaign: a vendor magic staff with '% increased Spell Damage' and mana already doubles your damage. Buy a new one every act until Sire of Shards (58).")},
 {"cat": L("Defesa", "Defence"), "lvl": L("Médio", "Medium"), "title": L("Deixe o mapa te bater uma vez", "Let the map hit you once"), "body": L("Reactive Growth e Avatar of Evolution te adaptam ao elemento do último hit que você tomou — e Avatar dobra o efeito. Em mapa com dano elemental pesado, o primeiro hit é o caro; do segundo em diante você toma bem menos.", "Reactive Growth and Avatar of Evolution adapt you to the element of the last hit you took — and Avatar doubles the effect. In a map with heavy elemental damage the first hit is the expensive one; from the second on you take far less.")},
]

TROUBLESHOOT = [
 (L("O Comet não cai sozinho", "Comet doesn't fall on its own"), L("Cast on Critical sem os 100 de Spirit, sem o Comet encaixado nele, ou chance de crítico perto de zero. Confira nesta ordem: Spirit → Comet dentro do Cast on Critical → crítico (Rathpith Globe, nós de crítico para spells, Pinpoint Critical).", "Cast on Critical without the 100 Spirit, without Comet socketed in it, or crit chance near zero. Check in this order: Spirit → Comet inside Cast on Critical → crit (Rathpith Globe, spell crit nodes, Pinpoint Critical).")),
 (L("Fico sem mana o tempo todo", "I'm always out of mana"), L("Archmage faz cada spell custar uma fatia da mana máxima e o Eldritch Battery dobra custos. Soluções, da mais barata para a mais cara: Efficiency II/Zenith II, Mana Remnants com Remnant Potency, Lavianga's Spirits, Uhtred's Chalice e mods de 'Mana Cost Efficiency' nos anéis.", "Archmage makes every spell cost a slice of your maximum mana and Eldritch Battery doubles costs. Fixes, cheapest first: Efficiency II/Zenith II, Mana Remnants with Remnant Potency, Lavianga's Spirits, Uhtred's Chalice and 'Mana Cost Efficiency' mods on rings.")),
 (L("Morro do nada nos mapas", "I die out of nowhere in maps"), L("Sua vida real é a mana: se ela zera, o próximo hit vai direto na vida. Cheque resistências em 75%, Chaos Resistance (o caos passa pelo Mind Over Matter) e mantenha Uhtred's Chalice/Lavianga's Spirits ativos. Em Low Life (Rathpith), Chaos Resistance é obrigatório.", "Your real health is mana: if it empties, the next hit goes straight to life. Check 75% resistances, chaos resistance (chaos bypasses Mind Over Matter) and keep Uhtred's Chalice/Lavianga's Spirits running. On Low Life (Rathpith), chaos resistance is mandatory.")),
 (L("Dano fraco no boss", "Weak boss damage"), L("Frost Bomb antes do burst, Comet com Spell Cascade, e confira se a infusão de fogo está saindo (Siphon Elements + Elemental Equilibrium). Sem os dois, o Comet sai na versão fraca.", "Frost Bomb before the burst, Comet with Spell Cascade, and check that the fire infusion is coming out (Siphon Elements + Elemental Equilibrium). Without both, Comet lands in its weak version.")),
 (L("O clear parou de crescer", "My clear stopped growing"), L("Na ordem: Sire of Shards (58), Nova Projectiles I, Snakepit no anel direito e mana máxima. Com Archmage, +mana em qualquer slot é dano em todos os projéteis ao mesmo tempo.", "In order: Sire of Shards (58), Nova Projectiles I, Snakepit in the right ring and maximum mana. With Archmage, +mana in any slot is damage on every projectile at once.")),
 (L("Não tenho Spirit para tudo", "I don't have Spirit for everything"), L("Ordem de prioridade: Archmage (100) → Cast on Critical (100) → Mana Remnants (30) → Arctic Armour (30) → Siphon Elements (30). Spirit vem de: quests (100), slots de charm vazios (40 cada, Sacred Flow), amuleto e peito.", "Priority order: Archmage (100) → Cast on Critical (100) → Mana Remnants (30) → Arctic Armour (30) → Siphon Elements (30). Spirit comes from: quests (100), empty charm slots (40 each, Sacred Flow), amulet and chest.")),
]

ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Archmage ligado · resistências em 75%", "Archmage running · 75% resistances"), gear="Sire of Shards"),
 dict(stage="T1–T10", goal=L("Cast on Critical + Comet · Reactive Growth", "Cast on Critical + Comet · Reactive Growth"), gear=L("Amuleto/peito com Spirit · Cloak of Defiance", "Amulet/chest with Spirit · Cloak of Defiance")),
 dict(stage="T11–T15", goal=L("Rathpith Globe · Avatar of Evolution · 3.000 de mana", "Rathpith Globe · Avatar of Evolution · 3,000 mana"), gear=L("Rares de mana (Tiara, Robe, Mnemonic Ring)", "Mana rares (Tiara, Robe, Mnemonic Ring)")),
 dict(stage=L("Pinnacle e challenges", "Pinnacle and challenges"), goal=L("Comet automático matando pinnacle · mapas juiced sem parar", "Automatic Comet killing pinnacles · juiced maps nonstop"), gear="Kalandra's Touch · Runeseeker's Call"),
]

CRAFT = [
 L("Regra única de craft desta build: mana máxima em todo slot. Transmutation/Augmentation na base até sair '+ to maximum Mana' ou '% increased Energy Shield', depois Regal e Exalted nas resistências.", "This build's one crafting rule: maximum mana in every slot. Transmutation/Augmentation on the base until '+ to maximum Mana' or '% increased Energy Shield' shows up, then Regal and Exalted into resistances."),
 L("Runas: depois do Wisdom of the Maji (nível ~40) toda runa também dá a linha Bonded dela. Encher os sockets com runas de resistência baratas é o melhor custo-benefício do guia.", "Runes: after Wisdom of the Maji (level ~40) every rune also grants its Bonded line. Filling your sockets with cheap resistance runes is the best value in this guide."),
 L("Amuleto: procure '+ to Spirit' primeiro — é o que decide se Archmage e Cast on Critical rodam juntos.", "Amulet: look for '+ to Spirit' first — it decides whether Archmage and Cast on Critical run together."),
]

T("skill", "Archmage", 50, L("100 de Spirit + Uncut nível 14", "100 Spirit + level 14 Uncut"), L("Assim que os 100 de Spirit das quests estiverem completos.", "As soon as the 100 quest Spirit is complete."), L("Mana máxima vira dano de raio em todas as spells.", "Maximum mana becomes lightning damage on every spell."), L("Antes dos 100 de Spirit ele não cabe com mais nada.", "Before you have 100 Spirit it doesn't fit alongside anything else."), "—")
T("item", "Sire of Shards", 58, L("Nível 58", "Level 58"), L("Compre assim que chegar no nível (custa menos de 0,01 divine).", "Buy it the moment you hit the level (it costs less than 0.01 divine)."), L("4 projéteis extras em círculo em todas as spells.", "4 extra projectiles in a circle on every spell."), "—", L("Cajado rare com % dano de spell.", "Rare staff with % spell damage."))
T("skill", "Cast on Critical", 65, L("100 de Spirit (além do Archmage)", "100 Spirit (on top of Archmage)"), L("Primeiros mapas, com amuleto/peito de Spirit.", "First maps, with a Spirit amulet/chest."), L("O Comet passa a cair sozinho a cada crítico.", "Comet starts falling on its own with every crit."), L("Com crítico baixo quase não dispara.", "With low crit it barely triggers."), "—")
T("item", "Rathpith Globe", 75, L("Nível 75", "Level 75"), L("Quando você já tiver Pain Attunement e Chaos Resistance.", "Once you already have Pain Attunement and chaos resistance."), L("Crítico por vida máxima e Low Life permanente.", "Crit per maximum life and permanent Low Life."), L("Sem Mind Over Matter, viver em Low Life é morrer.", "Without Mind Over Matter, living on Low Life means dying."), "—")
T("asc", "Sacred Flow", 25, L("1º Trial", "1st Trial"), L("Primeira ascendência, sempre.", "First ascendancy, always."), L("+40 de Spirit por slot de charm vazio.", "+40 Spirit per empty charm slot."), "—", "—")
T("asc", "Wisdom of the Maji", 40, L("2º Trial", "2nd Trial"), L("Assim que possível.", "As soon as possible."), L("Runas passam a dar a linha Bonded.", "Runes start granting their Bonded line."), "—", "—")

CASES = [
 (L("Qual a diferença para a página do Oracle (que também é Druid)?", "How is this different from the Oracle page (also a Druid)?"), L("O Oracle joga com Spell Totems: os totems lançam as spells por você e a build vira Grim Pillars + Bitter Dead. Aqui não tem totem nenhum: você lança o Spark na mão do começo ao fim e o Comet é automatizado pelo Cast on Critical. As ascendências e as rotações são diferentes; o que as duas compartilham é a ideia de usar mana como dano (Archmage).", "The Oracle plays with Spell Totems: the totems cast for you and the build becomes Grim Pillars + Bitter Dead. Here there are no totems at all: you cast Spark yourself from start to finish and Comet is automated by Cast on Critical. The ascendancies and rotations are different; what the two share is the idea of turning mana into damage (Archmage).")),
 (L("Dá para jogar sem o Cast on Critical?", "Can I play without Cast on Critical?"), L("Dá: continue lançando o Comet na mão nos bosses (é como você joga do Ato 3 ao 64). Você perde o dano automático em mapa, mas o clear do Spark é o mesmo. Faça a troca quando tiver Spirit para os dois buffs de 100.", "You can: keep casting Comet manually on bosses (that's how you play from Act 3 to 64). You lose the automatic damage in maps, but Spark's clear is the same. Make the swap once you have Spirit for both 100-Spirit buffs.")),
 (L("Vale a pena o Runeseeker's Call?", "Is Runeseeker's Call worth it?"), L("Os 10 personagens de maior DPS do ladder usam — mas ele custa centenas de divines. Até lá, Sire of Shards (menos de 0,01 divine) faz o clear e Taryn's Shiver faz o boss. A build não depende dele para completar T15/T20 nem as challenges.", "The 10 highest-DPS ladder characters use it — but it costs hundreds of divines. Until then, Sire of Shards (under 0.01 divine) does the clear and Taryn's Shiver does the bosses. The build doesn't need it to complete T15/T20 or the challenges.")),
 (L("Posso ficar com Serpent's Lesson no lugar do Rathpith?", "Can I keep Serpent's Lesson instead of Rathpith?"), L("O Serpent's Lesson te conta como em Low Life quando a mana cai abaixo de 35% — ou seja, só quando você já está em perigo. O Rathpith te deixa em Low Life de propósito, com a mana cheia. Para o pacote Pain Attunement + Execute III, o Rathpith é o item certo.", "Serpent's Lesson counts you as Low Life when your mana drops below 35% — that is, only when you're already in danger. Rathpith puts you on Low Life on purpose, with full mana. For the Pain Attunement + Execute III package, Rathpith is the right item.")),
]

SOURCES = [
 dict(name="poe.ninja — Druid · Shaman (Forbidden Rites)", use=L("Os 10 Shamans de maior DPS (nível 94–98): árvore, ascendência, itens, gems e supports do endgame", "The 10 highest-DPS Shamans (level 94–98): endgame tree, ascendancy, items, gems and supports"), url=NINJA_URL),
 dict(name="Path of Building (PoE2)", use=L("Tier de cada gem (quando ela entra no leveling), custos de Spirit e textos das skills e supports", "Each gem's tier (when it enters your leveling), Spirit costs and skill/support texts"), url=POB_URL),
 dict(name=L("Árvore de passivas 0.5.5 (tools/tree.json)", "Passive tree 0.5.5 (tools/tree.json)"), use=L("Textos exatos das keystones (Elemental Equilibrium, Eldritch Battery, Mind Over Matter, Pain Attunement), notáveis e ascendência Shaman", "Exact keystone texts (Elemental Equilibrium, Eldritch Battery, Mind Over Matter, Pain Attunement), notables and the Shaman ascendancy"), url="https://poe2db.tw/us/Shaman"),
 dict(name="RePoE2", use=L("Nomes e ícones das bases, uniques e gems", "Base, unique and gem names and icons"), url="https://repoe-fork.github.io/poe2/"),
 dict(name=L("poe.ninja — economia", "poe.ninja — economy"), use=L("Preços das uniques (as do leveling custam frações de divine)", "Unique prices (the leveling ones cost fractions of a divine)"), url="https://poe.ninja/poe2/economy/forbiddenrites"),
]

FIXES = [
 L("A árvore das fases A1–A4, Mapas e Endgame é um corte da ordem real de alocação do personagem de maior DPS do ladder (17, 34, 50, 72, 95 e 118 pontos), calculada a partir do início do Druid. A fase Aspiracional é a árvore completa dele.", "The A1–A4, Maps and Endgame trees are cuts of the real allocation order of the ladder's highest-DPS character (17, 34, 50, 72, 95 and 118 points), computed from the Druid's starting node. The Aspirational phase is that character's full tree."),
 L("O poe.ninja não guarda o histórico de leveling: as gems, supports e uniques de cada fase da campanha foram montadas aqui a partir do tier de cada gem no Path of Building (o nível do Uncut Skill Gem que ela pede) e dos preços atuais, não copiadas de um planner.", "poe.ninja doesn't store leveling history: each campaign phase's gems, supports and uniques were assembled here from each gem's tier in Path of Building (the Uncut Skill Gem level it needs) and from current prices, not copied from a planner."),
 L("Os 10 personagens do ladder usam Runeseeker's Call, Mageblood e Kalandra's Touch — itens de centenas de divines. Eles estão na fase Aspiracional; o resto do guia foi montado para funcionar sem eles.", "The 10 ladder characters use Runeseeker's Call, Mageblood and Kalandra's Touch — items worth hundreds of divines. Those live in the Aspirational phase; the rest of the guide is built to work without them."),
 L("As contas de Spirit aqui somam só o custo base dos buffs. Mods de Reservation Efficiency (comuns em Ancestral Tiara) e o Spirit do Sacred Flow mudam o total: confira no jogo.", "The Spirit math here only adds up the buffs' base costs. Reservation Efficiency mods (common on Ancestral Tiaras) and Sacred Flow's Spirit change the total: check in game."),
 L("The Stars Answer é uma gem tier 0 (não sai de Uncut Skill Gem comum). Ela aparece só como opção na fase Aspiracional, porque os 10 do ladder usam.", "The Stars Answer is a tier 0 gem (it doesn't come from a normal Uncut Skill Gem). It only appears as an option in the Aspirational phase, because all 10 ladder characters use it."),
]

UI = dict(
 carry=r"^(Spark|Comet|Archmage|Cast on Critical)$", box=L("CHAVE", "KEY"), spiritWhat=L("(Archmage, Cast on Critical e buffs)", "(Archmage, Cast on Critical and buffs)"),
 mechBtn=L("Abrir Mana & Infusões", "Open Mana & Infusions"), dmg2="Comet", dmgBar=L("Spark / Comet (aprox.)", "Spark / Comet (approx.)"),
 dmgLegend=L("Comet (proporção aproximada do dano)", "Comet (approximate share of damage)"),
 earlyGone=L("Essa gem já saiu: passou do nível {u}.", "That gem is gone: you're past level {u}."),
 earlyNote=L("Só no começo; sai no nível ~{u}.", "Early only; leaves around level {u}."),
 treeIntro=L("Árvore real do Shaman de maior DPS do ladder, cortada por pontos em cada fase. Campanha: mana, dano de raio e Elemental Equilibrium. Mapas: Eldritch Battery, Mind Over Matter e crítico para spells.", "The real tree of the ladder's highest-DPS Shaman, cut by points for each phase. Campaign: mana, lightning damage and Elemental Equilibrium. Maps: Eldritch Battery, Mind Over Matter and spell crit."),
 set1=L("dano de spell", "spell damage"), set2=L("não usado", "not used"), asc="Shaman", cls="Druid",
 respecTip=L("O único respec grande é no nível ~52, quando Eldritch Battery e Mind Over Matter entram: compare com a fase anterior antes de gastar ouro.", "The only big respec is around level 52, when Eldritch Battery and Mind Over Matter come in: compare with the previous phase before spending gold."),
 routeIntro=L("Sete fases: Spark com Chain no Ato 1, Spark em círculo e Sacred Flow no Ato 2, Comet e o loop das infusões no Ato 3, Archmage no Ato 4, Comet automático nos mapas, o pacote de Low Life no endgame e os itens de centenas de divines no Aspiracional.", "Seven phases: chaining Spark in Act 1, circle Spark and Sacred Flow in Act 2, Comet and the infusion loop in Act 3, Archmage in Act 4, automatic Comet in maps, the Low Life package in endgame and the hundreds-of-divines items in Aspirational."),
 socketPrio=["Spark", "Cast on Critical", "Comet", "Archmage", "Siphon Elements", "Mana Remnants"],
 permIntro=L("Nada disso volta depois. Os 100 de Spirit das quests pagam o Archmage; o resto vem do Sacred Flow e dos itens.", "None of this comes back later. The 100 quest Spirit pays for Archmage; the rest comes from Sacred Flow and your items."),
 atlasCards=[[L("Por que ela fecha challenges", "Why it clears challenges"), L("Clear de tela inteira com um botão (mapas rápidos e em série), burst de Comet automático para rares e bosses de mecânica, e Blink para as partes de correr. É a mesma rotação em Breach, Ritual, Delirium ou Expedition: andar segurando o Spark.", "Full-screen clear with one button (fast maps, back to back), automatic Comet burst for rares and mechanic bosses, and Blink for the running parts. It's the same rotation in Breach, Ritual, Delirium or Expedition: walk while holding Spark.")],
             [L("Mapas ruins", "Bad maps"), L("'Monstros refletem dano elemental' e 'menos chance de crítico' são os dois mods que quebram a build (o segundo desliga o Comet automático). Mapas com dano de caos pedem Chaos Resistance, porque o caos passa pelo Mind Over Matter.", "'Monsters reflect elemental damage' and 'less critical hit chance' are the two mods that break the build (the second one switches off the automatic Comet). Chaos damage maps need chaos resistance, because chaos bypasses Mind Over Matter.")]],
 foot=L("Guia montado a partir dos 10 Shamans de maior DPS do poe.ninja, dos dados do Path of Building e da árvore 0.5.5, com preços do poe.ninja", "Guide assembled from poe.ninja's 10 highest-DPS Shamans, Path of Building data and the 0.5.5 tree, with poe.ninja prices"),
)

CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens, Árvore e Mana & Infusões se adaptam na hora. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items, Tree and Mana & Infusions tabs adapt instantly. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit máximo", "Max Spirit"), L("ex.: 230", "e.g. 230")], ["mana", L("Mana máxima", "Max mana"), L("ex.: 1800", "e.g. 1800")], ["crit", L("Crítico do Spark (%)", "Spark crit (%)"), L("ex.: 25", "e.g. 25")]],
 tiles=[[L("Spirit reservado", "Spirit reserved"), "used"], [L("Spirit livre", "Spirit free"), "free"], [L("Mana máxima", "Max mana"), "mana"]],
 buffs=[dict(key="archmage", name="Archmage", cost=100), dict(key="coc", name="Cast on Critical", cost=100), dict(key="mr", name="Mana Remnants", cost=30),
        dict(key="aa", name="Arctic Armour", cost=30), dict(key="se", name="Siphon Elements", cost=30), dict(key="blink", name="Blink", cost=60)],
 own=[
  ["gear", "sire", "Sire of Shards"], ["gear", "rathpith", "Rathpith Globe"], ["gear", "spiritamu", L("Amuleto com +Spirit", "Amulet with +Spirit")],
  ["gear", "manarares", L("Rares com +mana máxima (Tiara/Robe/Ring)", "Rares with +maximum mana (Tiara/Robe/Ring)")],
  ["gem", "archmage", "Archmage (100)"], ["gem", "coc", "Cast on Critical + Comet (100)"], ["gem", "se", "Siphon Elements (30)"], ["gem", "mr", "Mana Remnants (30)"],
  ["gem", "aa", "Arctic Armour (30)"], ["gem", "comet", "Comet"], ["gem", "nova", "Nova Projectiles I"], ["gem", "cascade", "Spell Cascade"],
  ["tree", "ee", "Elemental Equilibrium"], ["tree", "eb", "Eldritch Battery"], ["tree", "mom", "Mind Over Matter"], ["tree", "pain", "Pain Attunement"],
  ["asc", "sacred", "Sacred Flow"], ["asc", "maji", "Wisdom of the Maji"], ["asc", "reactive", "Reactive Growth"], ["asc", "avatar", "Avatar of Evolution"],
 ],
 rules=[
  dict(when=dict(lvMin=65, own=["coc"], notOwn=["comet"]), lvl="bad", t=L("Cast on Critical sem Comet dentro", "Cast on Critical with no Comet inside"), d=L("O Cast on Critical não faz nada sozinho: ele dispara as spells encaixadas nele. Coloque Comet + Spell Cascade.", "Cast on Critical does nothing by itself: it triggers the spells socketed in it. Put Comet + Spell Cascade in."), tab="skills"),
  dict(when=dict(own=["coc"], numLt=["crit", 15]), lvl="bad", t=L("Crítico baixo demais para o Cast on Critical", "Crit too low for Cast on Critical"), d=L("Rathpith Globe, nós de crítico para spells e Pinpoint Critical. Abaixo de ~15% o Comet quase não cai.", "Rathpith Globe, spell crit nodes and Pinpoint Critical. Below ~15% Comet barely falls."), tab="mech"),
  dict(when=dict(own=["archmage"], notOwn=["eb"]), lvl="warn", t=L("Archmage sem Eldritch Battery", "Archmage without Eldritch Battery"), d=L("Metade da sua mana está presa em Energy Shield. Aloque Eldritch Battery: ES vira mana, e mana é dano.", "Half your mana is stuck in energy shield. Allocate Eldritch Battery: ES becomes mana, and mana is damage."), tab="arvore"),
  dict(when=dict(own=["se"], notOwn=["ee"]), lvl="warn", t=L("Siphon Elements sem Elemental Equilibrium", "Siphon Elements without Elemental Equilibrium"), d=L("Sem a keystone, o Shock cria infusão de raio (que nem o Spark nem o Comet usam). Com ela, Shock vira infusão de frio e Freeze vira infusão de fogo.", "Without the keystone, Shock creates a lightning infusion (which neither Spark nor Comet uses). With it, Shock becomes a cold infusion and Freeze becomes a fire infusion."), tab="mech"),
  dict(when=dict(lvMin=58, notOwn=["sire"]), lvl="tip", t="Sire of Shards", d=L("Custa menos de 0,01 divine e dá 4 projéteis extras em círculo em TODAS as spells.", "It costs less than 0.01 divine and gives 4 extra projectiles in a circle on EVERY spell."), tab="gear"),
  dict(when=dict(lvMin=50, notOwn=["archmage"]), lvl="warn", t=L("Archmage pendente", "Archmage pending"), d=L("Uncut Skill Gem nível 14 + 100 de Spirit. É a virada da build.", "Level 14 Uncut Skill Gem + 100 Spirit. It's the build's turning point."), tab="skills"),
  dict(when=dict(lvMin=85, own=["pain"], notOwn=["rathpith"]), lvl="bad", t=L("Pain Attunement sem Rathpith Globe", "Pain Attunement without Rathpith Globe"), d=L("Com a vida cheia, Pain Attunement é 30% LESS dano crítico. Ou pegue o Rathpith, ou tire a keystone.", "On full life, Pain Attunement is 30% LESS crit damage. Either get Rathpith, or drop the keystone."), tab="arvore"),
  dict(when=dict(lvMin=26, notOwn=["sacred"]), lvl="warn", t=L("1ª ascendência pendente", "1st ascendancy pending"), d="Sacred Flow (+40 Spirit).", tab="asc"),
  dict(when=dict(lvMin=42, notOwn=["maji"]), lvl="warn", t=L("2ª ascendência pendente", "2nd ascendancy pending"), d=L("Wisdom of the Maji: runas passam a dar a linha Bonded.", "Wisdom of the Maji: runes start granting their Bonded line."), tab="asc"),
  dict(when=dict(lvMin=45, numLt=["mana", 600]), lvl="tip", t=L("Mana máxima baixa", "Low maximum mana"), d=L("Mana é dano (Archmage) e vida (Mind Over Matter). Procure '+ to maximum Mana' em todo slot.", "Mana is damage (Archmage) and life (Mind Over Matter). Look for '+ to maximum Mana' in every slot."), tab="gear"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["a4"], when=dict(notOwn=["archmage"]), gemsFrom="a3", note=L("Sem Archmage marcado: mostrando o setup do Ato 3 (Spark + Comet na mão).", "Archmage not ticked: showing the Act 3 setup (Spark + manual Comet).")),
 dict(pids=["maps", "endgame", "max"], when=dict(notOwn=["coc"]), gemsFrom="a4", note=L("Sem Cast on Critical: mostrando o setup do Ato 4 (Comet na mão nos bosses).", "No Cast on Critical: showing the Act 4 setup (manual Comet on bosses).")),
]
TREE_RULES = [
 dict(when=dict(lvMin=36, own=["se"], notOwn=["ee"]), t=L("Aloque Elemental Equilibrium: é ela que faz o Shock virar infusão de frio para o Spark.", "Allocate Elemental Equilibrium: it's what turns your Shock into the cold infusion Spark wants."), node="Elemental Equilibrium"),
 dict(when=dict(lvMin=50, own=["archmage"], notOwn=["mom"]), t=L("Aloque Mind Over Matter: com a mana que o Archmage pede, ela vira sua maior defesa.", "Allocate Mind Over Matter: with the mana Archmage demands, it becomes your biggest defence."), node="Mind Over Matter"),
]
TIMING_KEY = {"Archmage": "archmage", "Sire of Shards": "sire", "Cast on Critical": "coc", "Rathpith Globe": "rathpith", "Sacred Flow": "sacred", "Wisdom of the Maji": "maji"}

MECH = dict(
 title=L("Mana & Infusões", "Mana & Infusions"),
 intro=L("Duas engrenagens explicam a build inteira: a mana (que é dano e vida ao mesmo tempo) e as infusões (que fazem Spark e Comet se alimentarem um do outro).", "Two gears explain the whole build: mana (which is damage and life at once) and infusions (which make Spark and Comet feed each other)."),
 sections=[
  dict(type="cards", cards=[
   [L("1. Mana = dano", "1. Mana = damage"), L("Archmage (100 de Spirit): enquanto ativo, suas spells não-canalizadas custam mana a mais e ganham dano de raio extra baseado na sua mana MÁXIMA. Por isso '+80 de mana' num anel é mais dano que '% dano de spell'.", "Archmage (100 Spirit): while active, your non-channelling spells cost extra mana and gain extra lightning damage based on your MAXIMUM mana. That's why '+80 mana' on a ring is more damage than '% spell damage'.")],
   [L("2. ES = mana", "2. ES = mana"), L("Eldritch Battery converte 100% do Energy Shield máximo em mana (e dobra os custos). Focus, capacete e peito de ES viram dano direto.", "Eldritch Battery converts 100% of maximum Energy Shield into mana (and doubles costs). ES focus, helmet and chest become raw damage.")],
   [L("3. Mana = vida", "3. Mana = life"), L("Mind Over Matter: todo dano sai da mana antes da vida. A mesma barra que dá dano é a que segura os hits — e o Mana Remnants enche ela no meio do pack.", "Mind Over Matter: all damage comes out of mana before life. The same bar that deals damage is the one that eats the hits — and Mana Remnants refills it inside the pack.")],
   [L("4. Crítico = Comet", "4. Crit = Comet"), L("Cast on Critical (100 de Spirit) ganha energia a cada crítico e, cheio, dispara o Comet + Spell Cascade. O Spark dispara dezenas de projéteis por cast: é uma máquina de críticos.", "Cast on Critical (100 Spirit) gains Energy on every crit and, when full, triggers Comet + Spell Cascade. Spark fires dozens of projectiles per cast: it's a crit machine.")],
  ]),
  dict(type="table", h=L("O loop das infusões", "The infusion loop"), cols=[L("Peça", "Piece"), L("O que faz", "What it does"), L("Se faltar", "If missing")], rows=[
   ["Spark", L("Aplica Shock em vários alvos por cast", "Shocks several targets per cast"), L("Sem ailment, o Siphon Elements não cria nada", "With no ailment, Siphon Elements creates nothing")],
   ["Siphon Elements", L("Cria Infusion Remnant quando você congela, shocka ou incendeia", "Creates an Infusion Remnant when you freeze, shock or ignite"), L("Spark e Comet ficam sempre na versão fraca", "Spark and Comet stay in their weak versions")],
   ["Elemental Equilibrium", L("Troca o tipo criado: Shock → infusão de frio · Freeze → infusão de fogo", "Swaps the type created: Shock → cold infusion · Freeze → fire infusion"), L("Você cria infusão de raio, que nenhuma das duas skills usa", "You create lightning infusions, which neither skill uses")],
   [L("Spark (infusão de frio)", "Spark (cold infusion)"), L("Consome a infusão de frio: dispara muitos sparks em círculo", "Consumes the cold infusion: fires many sparks in a circle"), L("Clear normal (ainda bom)", "Normal clear (still good)")],
   [L("Comet (infusão de fogo)", "Comet (fire infusion)"), L("Consome a infusão de fogo: explosão devastadora de gelo e fogo", "Consumes the fire infusion: a devastating ice-and-fire blast"), L("Comet normal: menos dano de boss", "Normal Comet: less boss damage")],
   ["Powered by Verisium", L("Gasta Ward para criar infusão que vale por qualquer elemento", "Spends Ward to create an infusion that counts as any element"), L("Depende só do Siphon Elements", "You depend on Siphon Elements alone")],
  ]),
  dict(type="steps", h=L("O dia do Archmage (nível ~50)", "Archmage day (level ~50)"), steps=[
   [L("Gem", "Gem"), L("Uncut Skill Gem nível 14 → Archmage.", "Level 14 Uncut Skill Gem → Archmage.")],
   [L("Spirit", "Spirit"), L("100 das quests. Se faltar, esvazie um slot de charm (Sacred Flow paga 40 por slot vazio).", "100 from quests. If you're short, empty a charm slot (Sacred Flow pays 40 per empty slot).")],
   [L("Árvore", "Tree"), L("Eldritch Battery e Mind Over Matter; depois os nós de mana (Raw Mana, Arcane Intensity).", "Eldritch Battery and Mind Over Matter; then the mana nodes (Raw Mana, Arcane Intensity).")],
   [L("Itens", "Items"), L("Troque tudo que não tem mana: '+ to maximum Mana' e '% increased Energy Shield' em todo slot.", "Replace anything without mana: '+ to maximum Mana' and '% increased Energy Shield' in every slot.")],
   [L("Flasks", "Flasks"), L("Lavianga's Spirits (constante) e Uhtred's Chalice (passa do máximo). Agora flask de mana é poção de vida.", "Lavianga's Spirits (constant) and Uhtred's Chalice (overflows). A mana flask is a health potion now.")],
  ]),
  dict(type="rotation", blocks=[
   [L("Clear", "Clear"), [L("Ande até o pack", "Walk into the pack"), L("Segure o Spark (círculo)", "Hold Spark (circle)"), L("Pegue os Remnants de mana e infusão no caminho", "Pick up mana and infusion Remnants on the way"), L("Deixe o Comet do Cast on Critical limpar o resto", "Let Cast on Critical's Comet clean up the rest"), L("Blink para o próximo pack", "Blink to the next pack")]],
   [L("Boss", "Boss"), [L("Frost Bomb no chão (Exposure)", "Frost Bomb on the ground (Exposure)"), L("Spark colado: cada crítico enche o Cast on Critical", "Spark up close: every crit fills Cast on Critical"), L("Comet na mão quando ele parar", "Manual Comet when it stops moving"), L("Mana baixa = recue e deixe encher (é a sua vida)", "Low mana = back off and let it refill (it's your life)")]],
  ]),
  dict(type="spirit", h=L("Spirit: o que cabe e quando", "Spirit: what fits and when"), p=L("Marque o que você usa. Custos base do Path of Building.", "Tick what you use. Base costs from Path of Building."),
       note=L("Sacred Flow dá +40 por slot de charm VAZIO e mods de Reservation Efficiency reduzem os custos: confira no jogo.", "Sacred Flow grants +40 per EMPTY charm slot and Reservation Efficiency mods lower the costs: check in game.")),
  dict(type="timeline", h=L("Arma por nível", "Weapon by level"), items=[
   dict(lv=1, t=L("Cajado Magic do vendor", "Vendor magic staff"), d=L("'% increased Spell Damage' + mana. Compre um novo em todo ato.", "'% increased Spell Damage' + mana. Buy a new one every act.")),
   dict(lv=32, t=L("Cajado rare", "Rare staff"), d=L("% dano de spell, +mana máxima e cast speed.", "% spell damage, +maximum mana and cast speed.")),
   dict(lv=58, t="Sire of Shards", d=L("4 projéteis extras em círculo em todas as spells (menos de 0,01 divine).", "4 extra projectiles in a circle on every spell (under 0.01 divine).")),
   dict(lv=66, t="Taryn's Shiver", d=L("Troca de boss: congelados tomam 100% increased de dano.", "Boss swap: frozen enemies take 100% increased damage.")),
   dict(lv=90, t="Runeseeker's Call", d=L("Aspiracional: +mana gigante, + níveis de spell e 200% do efeito das runas.", "Aspirational: huge +mana, + spell levels and 200% rune effect.")),
  ]),
 ],
)

exec(open(os.path.join(HERE, "bcraft.py"), encoding="utf-8").read())


def build(QUESTS_PT):
    quests = []
    for q in QUESTS_PT:
        q = dict(q)
        if q["boss"] == "Great White One":
            q["reward"] = L("ESCOLHA: +30% Armour, Evasion e Energy Shield (Shark Fin): o Energy Shield vira mana com Eldritch Battery", "CHOICE: +30% Armour, Evasion and Energy Shield (Shark Fin): energy shield becomes mana with Eldritch Battery")
            q["prio"] = "Alta"
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="17/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=NINJA_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=BOOK.TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None,
                ui=UI, char=CHAR, mech=MECH, adaptSwaps=ADAPT_SWAPS, treeRules=TREE_RULES, timingKey=TIMING_KEY, phaseAct=PHASE_ACT, treeOrder=ORDER + ["uber"], craftKit=CRAFT_KIT)
