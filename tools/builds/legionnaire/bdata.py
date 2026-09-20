# -*- coding: utf-8 -*-
"""Mercenary · Gemling Legionnaire: Falling Thunder com cajado, alimentado por Power Charges.

Fonte única do endgame: o Path of Building nível 96 de https://poe.ninja/poe2/pob/29764 (192M de DPS no PoB), convertido por kit/pobxml.py.
NÃO existe guia de leveling público para essa build: a rota 1→100 foi montada aqui, a partir do PoB (árvore, gems, itens), das descrições e tiers
de gem do Path of Building, dos textos de passiva de tools/tree.json e dos preços/níveis do poe.ninja. Onde o jogo pode variar (nível em que a
Uncut Skill Gem aparece, ordem dos Trials) o texto diz "confira no jogo"."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("legionnaire")

POB_URL = "https://poe.ninja/poe2/pob/29764"
GUIDE_URL = POB_URL
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "19/09/2026"

CONFIG = dict(dir="legionnaire", build="legionnaire", store="legionnaire1", emoji="⚡", pill="Mercenary · Gemling Legionnaire",
              fonts="family=Cinzel:wght@500;700;900&family=Rajdhani:wght@500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400")
TXT = {
 "pt": dict(TITLE="Cleaving Thunder", DESC="Guia interativo Mercenary Gemling Legionnaire Falling Thunder (cajado + Power Charges) — PoE 2 Forbidden Rites",
            H1S="Falling Thunder · cajado · Power Charges · do nível 1 ao 100 a partir de um PoB real de 192M de DPS", H1="Cleaving Thunder",
            LEAD="Você bate no chão com um cajado carregado de raio e cada Power Charge vira um projétil. Diga seu nível e o que você já tem: o guia mostra o que fazer agora, gema por gema, item por item, até o build de endgame."),
 "en": dict(TITLE="Cleaving Thunder", DESC="Interactive Mercenary Gemling Legionnaire Falling Thunder (quarterstaff + Power Charges) guide — PoE 2 Forbidden Rites",
            H1S="Falling Thunder · quarterstaff · Power Charges · level 1 to 100 from a real 192M-DPS PoB", H1="Cleaving Thunder",
            LEAD="You slam the ground with a lightning-charged quarterstaff and every Power Charge becomes a projectile. Tell it your level and what you already have: the guide shows what to do now, gem by gem, item by item, all the way to the endgame build."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["mech", "Power Charges", "Power Charges"], ["rota", "Rota 1→100", "Route 1→100"],
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
    if slot in (L("Capacete", "Helmet"), "Body Armour", L("Luvas", "Gloves"), L("Botas", "Boots")):
        return [L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio)", "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning)")]
    return None


CHECK = L("Confira no jogo", "Check in game")
SP30 = L("30 Spirit", "30 Spirit")

# ------------------------------------------------------------------ por que cada support
SUPWHY = {
 "Perpetual Charge": L("Chance de NÃO gastar o Power Charge ao usar a skill, mesmo ganhando o efeito: a mesma carga vale vários golpes. É o support mais importante da build.", "A chance NOT to spend the Power Charge when the skill uses it while still getting the effect: one charge pays for several hits. The most important support in the build."),
 "Heightened Charges": L("Chance de dobrar o benefício de consumir cargas: o Falling Thunder solta o dobro de projéteis.", "A chance to double the benefit of consuming charges: Falling Thunder fires twice the projectiles."),
 "Nova Projectiles I": L("Os projéteis saem em círculo: você bate no meio do pack e acerta todo mundo, sem mirar.", "Projectiles leave in a circle: you slam in the middle of the pack and hit everyone, no aiming."),
 "Rapid Attacks I": L("Ataca mais rápido: mais slams por segundo = mais Power Charges gastos e mais dano.", "Attacks faster: more slams per second = more Power Charges spent and more damage."),
 "Rapid Attacks II": L("Versão melhor do Rapid Attacks: mesmo efeito, mais velocidade.", "Better Rapid Attacks: same effect, more speed."),
 "Elemental Armament I": L("Mais dano elemental nos ataques: o Falling Thunder é raio, então serve direto.", "More elemental damage on attacks: Falling Thunder is lightning, so it applies directly."),
 "Elemental Armament II": L("Versão melhor: mais dano elemental nos ataques.", "Better version: more elemental damage on attacks."),
 "Rakiata's Flow": L("Inverte as resistências elementais do inimigo: com Elemental Weakness derrubando a resistência para negativo, ela vira dano extra em vez de perda.", "Inverts the enemy's elemental resistances: with Elemental Weakness pushing resistance below zero, it becomes extra damage instead of a penalty."),
 "Shock": L("Mais Shock: Shock alimenta o Herald of Thunder e o Innervate.", "More Shock: Shock feeds Herald of Thunder and Innervate."),
 "Innervate": L("Matar um inimigo em Shock imbui seus ataques com raio por um tempo.", "Killing a Shocked enemy imbues your attacks with lightning for a while."),
 "Life Leech I": L("Rouba vida do dano físico do ataque.", "Leeches life from the attack's physical damage."),
 "Life Leech II": L("Rouba vida do dano físico do ataque.", "Leeches life from the attack's physical damage."),
 "Life Leech III": L("Rouba vida e o leech não some com vida cheia.", "Leeches life and the leech isn't removed at full life."),
 "Ancestral Call II": L("A cada poucos segundos o Strike ganha um Ancestral Boost forte.", "Every few seconds the Strike gets a powerful Ancestral Boost."),
 "Bleed I": L("Chance de causar Bleeding com o dano físico.", "A chance to cause Bleeding with physical damage."),
 "Bleed II": L("Chance de causar Bleeding com o dano físico.", "A chance to cause Bleeding with physical damage."),
 "Behead II": L("Strike rouba dois mods de monstros Rare que mata.", "The Strike steals two modifiers from Rare monsters it kills."),
 "Armour Demolisher II": L("O Armour Break que você aplica fica mais forte.", "The Armour Break you apply is stronger."),
 "Elemental Focus": L("Mais dano elemental, mas sem ailments elementais: só na skill que não precisa deles.", "More elemental damage, but no elemental ailments: only on the skill that doesn't need them."),
 "Lightning Mastery": L("+1 nível na skill de raio.", "+1 level on the lightning skill."),
 "Culling Strike II": L("Mata na hora Rare e Unique com pouca vida: em bosses a barra final some sozinha.", "Instantly kills low-life Rares and Uniques: on bosses the last bar just disappears."),
 "Longshot II": L("Mais dano contra alvos distantes.", "More damage against distant targets."),
 "Overcharge": L("Shocks mais fortes, mas refletidos em você: use só onde o Shock importa.", "Stronger Shocks, but reflected back to you: use only where Shock matters."),
 "Spell Cascade": L("O Elemental Weakness cai em mais áreas ao mesmo tempo.", "Elemental Weakness lands in more areas at once."),
 "Cooldown Recovery II": L("Recupera cooldown mais rápido (Pinnacle of Power).", "Recovers cooldowns faster (Pinnacle of Power)."),
 "Prolonged Duration II": L("Duração maior: os buffs de carga duram mais.", "Longer duration: the charge buffs last longer."),
 "Blazing Critical": L("Crítico imbui seus ataques com fogo por um tempo.", "A critical hit imbues your attacks with fire for a while."),
 "Thrill of the Kill II": L("Matar (Cull) um inimigo em Shock imbui seus ataques com raio e aumenta o Shock.", "Culling a Shocked enemy imbues your attacks with lightning and raises Shock chance."),
 "Ice Bite II": L("Congelar um inimigo imbui seus ataques com frio.", "Freezing an enemy imbues your attacks with cold."),
 "Vitality II": L("Regeneração de vida enquanto o buff estiver ativo.", "Life regeneration while the buff is active."),
 "Precision II": L("Mais Accuracy enquanto o buff estiver ativo.", "More Accuracy while the buff is active."),
 "Warm Blooded": L("Freeze em você dura menos.", "Freeze on you lasts shorter."),
 "Strong Hearted": L("Shock em você dura menos.", "Shock on you lasts shorter."),
 "Cool Headed": L("Ignite em você dura menos.", "Ignite on you lasts shorter."),
 "Magnified Area II": L("Área maior.", "Larger area."),
 "Pin I": L("O dano físico pode dar Pin (prender) — mas o support tira o Stun.", "Physical damage can Pin — but the support removes Stun."),
 "Freeze": L("Mais chance de Freeze.", "More Freeze chance."),
 "Blind II": L("Cega inimigos ao acertar.", "Blinds enemies on hit."),
 "Bounty II": L("Inimigos mortos dão mais cargas de flask e charm.", "Enemies you kill grant more flask and charm charges."),
 "Compressed Duration II": L("Duração menor da skill.", "Shorter skill duration."),
 "Overabundance II": L("Aumenta o limite da skill (Limit) à custa da duração.", "Increases the skill's Limit at the cost of duration."),
 "Concentrated Area": L("Área menor e mais dano.", "Smaller area, more damage."),
}

# ------------------------------------------------------------------ fases
PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Cajado + Falling Thunder", "Quarterstaff + Falling Thunder"),
  carry=L("Você: Falling Thunder", "You: Falling Thunder"), dmgSplit=[100, 0],
  goal=L("Pegue qualquer cajado (Quarterstaff) e a primeira Uncut Skill Gem (nível 1): Falling Thunder. Você bate no chão e o raio atinge um cone à sua frente. Ainda sem Power Charges, ele funciona como um slam de raio normal — a build de endgame só vive de cargas depois do nível 33 (Redflare Conduit). Aqui o trabalho é simples: aprender o ritmo do slam, colocar Rapid Attacks I e Elemental Armament I, e guardar Perpetual Charge para quando as cargas aparecerem.",
         "Grab any Quarterstaff and your first Uncut Skill Gem (level 1): Falling Thunder. You slam the ground and lightning hits a cone in front of you. With no Power Charges yet it works as a plain lightning slam — the endgame build only lives on charges after level 33 (Redflare Conduit). The job here is simple: learn the slam rhythm, socket Rapid Attacks I and Elemental Armament I, and hold Perpetual Charge for when charges show up."),
  rotation=[L("Slam do Falling Thunder no pack", "Falling Thunder slam into the pack"), L("Quarterstaff Strike para andar e acertar 1 alvo", "Quarterstaff Strike to reposition and hit a single target"), L("Boss: fique perto — os projéteis do Falling Thunder causam mais dano a menos de 2 m", "Boss: stay close — Falling Thunder projectiles deal more damage within 2 m")],
  gems=[
   G("Falling Thunder", ["Rapid Attacks I", "Elemental Armament I"], L("Dano principal", "Main damage"), L("Slam em cone que fica com raio. É a sua skill do nível 1 ao 100. Uncut Skill Gem nível 1.", "A slam in a cone that turns into lightning. It's your skill from level 1 to 100. Level 1 Uncut Skill Gem."), "free"),
   G("Quarterstaff Strike", [], L("Skill básica", "Basic skill"), L("A skill padrão do cajado: use para andar e bater em alvo único.", "The staff's default skill: use it to reposition and hit single targets."), "free"),
  ],
  cheap=[L("Cajado (Quarterstaff) branco ou mágico com dano físico/elétrico", "White or magic Quarterstaff with physical/lightning damage"), L("Vida e resistências em qualquer peça", "Life and resistances on any piece")],
  full=[L("Nada de unique agora: guarde currency para o Ato 3", "No uniques now: save currency for Act 3")],
  stats=[L("Vida", "Life"), L("Dano com cajado", "Quarterstaff damage"), L("Chance de crítico com Quarterstaves", "Critical chance with Quarterstaves")],
  tree=L("Dano de melee perto do início da Mercenary: Overwhelm (+40% de dano com armas de duas mãos: o cajado é de duas mãos) e Cruel Methods (+25% de dano físico). São ~130% de dano somado nos nós no nível 15, contra 0% no caminho do PoB (uma fila de 16 nós de +5 Atributo até a região de crítico). Esses nós saem no respec do 79.", "Melee damage near the Mercenary start: Overwhelm (+40% damage with two-handed weapons: the quarterstaff is two-handed) and Cruel Methods (+25% physical damage). About 130% damage on the nodes by level 15, versus 0% on the PoB's road (a line of 16 +5 Attribute nodes to the crit region). These nodes leave in the level 79 respec."),
  avoid=[L("Trocar de arma toda hora: esta build só usa cajado", "Swapping weapons all the time: this build only uses a quarterstaff"), L("Gastar currency em item de nível baixo", "Spending currency on low-level items")],
  exit=[L("Nível 15: Perpetual Charge e Heightened Charges já estão disponíveis (tier 1–2)", "Level 15: Perpetual Charge and Heightened Charges are available (tier 1–2)")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 31], tag=L("Círculo de projéteis + primeiras cargas", "Projectile circle + first charges"),
  carry=L("Você: Falling Thunder", "You: Falling Thunder"), dmgSplit=[100, 0],
  goal=L("Nova Projectiles I muda o jeito de jogar: os projéteis do Falling Thunder saem em círculo em volta de você. Junto entram o Perpetual Charge e o Heightened Charges, que só valem se você tiver Power Charges. Fonte de carga nesta fase: o charm Breath of the Mountains (nível 5, quase de graça, dá 1 Power Charge ao usar). Na árvore você segue os nós de dano de melee (ver Árvore); o resto do tempo é juntar currency para o nível 33.",
         "Nova Projectiles I changes how you play: Falling Thunder's projectiles leave in a circle around you. Perpetual Charge and Heightened Charges join, but they only pay off if you have Power Charges. Charge source in this phase: the Breath of the Mountains charm (level 5, nearly free, grants 1 Power Charge on use). On the tree you follow the melee damage nodes (see Tree); the rest of the time is for saving currency for level 33."),
  rotation=[L("Use o charm para ter 1 Power Charge", "Use the charm to get 1 Power Charge"), L("Entre no pack e bata: Falling Thunder solta o círculo de projéteis", "Step into the pack and slam: Falling Thunder fires the projectile circle"), L("Quarterstaff Strike no intervalo", "Quarterstaff Strike in the gaps")],
  gems=[
   G("Falling Thunder", ["Nova Projectiles I", "Perpetual Charge", "Rapid Attacks I", "Elemental Armament II"], L("Dano principal", "Main damage"), L("Cada Power Charge vira um projétil no círculo. Uncut Skill Gem nível 2 para o Nova e o Elemental Armament II.", "Each Power Charge becomes a projectile in the circle. Level 2 Uncut Skill Gem for Nova and Elemental Armament II."), "free"),
   G("Quarterstaff Strike", [], L("Skill básica", "Basic skill"), L("Mantém a rotina de golpes entre os slams. Heightened Charges só entra no Falling Thunder (o Strike não gasta cargas), quando você tiver o 5º link.", "Keeps the hit routine between slams. Heightened Charges only goes on Falling Thunder (the Strike doesn't spend charges), once you have the 5th link."), "free"),
  ],
  cheap=["Breath of the Mountains", L("Cajado de nível 16 craftado: Transmutation + Augmentation até + dano físico / velocidade", "Crafted level 16 quarterstaff: Transmutation + Augmentation until + physical damage / speed")],
  full=["Breath of the Mountains"],
  stats=[L("Vida", "Life"), L("Dano de raio/elemental", "Lightning/elemental damage"), L("Velocidade de ataque", "Attack speed")],
  tree=L("Finishing Blows (+60% de dano contra inimigos em Low Life: o pack morre no fim do hit) e mais nós de dano físico e de duas mãos: ~460% de dano somado nos nós no nível 31, contra ~25% no caminho do PoB.", "Finishing Blows (+60% damage against enemies on Low Life: the pack dies at the end of the hit) and more physical and two-handed damage nodes: ~460% damage on the nodes by level 31, versus ~25% on the PoB's road."),
  avoid=[L("Equipar peças fracas só por resistência agora: conserte com runas", "Gearing weak pieces only for resistance now: fix it with runes"), L("Pegar todos os +5 Atributo de uma vez", "Taking every +5 Attribute at once")],
  exit=[L("1º Trial (~28): Essence of Virtue", "1st Trial (~28): Essence of Virtue"), L("Redflare Conduit e Powertread ficam prontos no nível 33", "Redflare Conduit and Powertread unlock at level 33"), L("Finishing Blows na árvore (dano contra Low Life)", "Finishing Blows on the tree (damage against Low Life)")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[32, 45], tag=L("Redflare Conduit: as cargas se geram sozinhas", "Redflare Conduit: charges make themselves"),
  carry=L("Você: Falling Thunder + Charged Staff", "You: Falling Thunder + Charged Staff"), dmgSplit=[100, 0],
  goal=L("Nível 33 é a virada. O Redflare Conduit (body, custa quase nada) dá 20% de chance de ganhar um Power Charge a cada acerto e o Powertread (botas, nível 33) dá +1 carga máxima e velocidade de movimento. Agora o Falling Thunder tem cargas o tempo todo, e o Perpetual Charge faz cada carga render vários slams. Uncut Skill Gem nível 9: Charged Staff, um buff de cajado que consome as cargas para somar dano de raio e um choque em onda aos seus ataques de Quarterstaff. 2º Trial (~40): Advanced Thaumaturgy.",
         "Level 33 is the turning point. Redflare Conduit (body, costs almost nothing) gives a 20% chance to gain a Power Charge on every hit, and Powertread (boots, level 33) gives +1 maximum charge and movement speed. Now Falling Thunder has charges all the time, and Perpetual Charge makes every charge pay for several slams. Level 9 Uncut Skill Gem: Charged Staff, a quarterstaff buff that consumes your charges to add lightning damage and a lightning shockwave to your Quarterstaff attacks. 2nd Trial (~40): Advanced Thaumaturgy."),
  rotation=[L("Charged Staff quando as cargas estiverem cheias", "Charged Staff when your charges are full"), L("Falling Thunder no pack: cada carga = 1 projétil", "Falling Thunder into the pack: each charge = 1 projectile"), L("O Redflare recarrega as cargas conforme você acerta", "Redflare refills the charges as you hit")],
  gems=[
   G("Falling Thunder", ["Nova Projectiles I", "Perpetual Charge", "Heightened Charges", "Rapid Attacks II", "Elemental Armament II"], L("Dano principal", "Main damage"), L("Com cargas vindo do Redflare, agora os 5 links fazem sentido. Rapid Attacks II é tier 4.", "With charges coming from Redflare, the 5 links now make sense. Rapid Attacks II is tier 4."), "free", since=32),
   G("Charged Staff", ["Perpetual Charge"], L("Buff de dano", "Damage buff"), L("Consome as Power Charges para dar dano de raio e uma onda de choque aos golpes de cajado. Uncut Skill Gem nível 9.", "Consumes Power Charges to add lightning damage and a shockwave to quarterstaff hits. Level 9 Uncut Skill Gem."), "free", since=32),
   G("Herald of Thunder", ["Shock", "Vitality II"], L("Dano extra", "Extra damage"), L("Matar um inimigo em Shock com um ataque solta raios que causam dano de ataque em volta. Tier 4, 30 Spirit.", "Killing a Shocked enemy with an attack releases lightning bolts that deal attack damage around. Tier 4, 30 Spirit."), "core", 1, SP30, since=34),
  ],
  cheap=["Redflare Conduit", "Powertread", "Breath of the Mountains"],
  full=["Redflare Conduit", "Powertread"],
  stats=[L("Vida", "Life"), L("Power Charges máximas", "Maximum Power Charges"), L("Dano crítico", "Critical damage")],
  tree=L("Prolonged Assault (+16% de dano de ataque), Blazing Arms (+16% de dano de ataque) e Voracious (+15% de velocidade de ataque com leech): dano e velocidade. As cargas de Redflare Conduit e Powertread (nível 33) escalam com o Perpetual Charge; os nós de carga entram no próximo corte.", "Prolonged Assault (+16% attack damage), Blazing Arms (+16% attack damage) and Voracious (+15% attack speed while leeching): damage and speed. The charges from Redflare Conduit and Powertread (level 33) scale with Perpetual Charge; the charge nodes come in the next cut."),
  avoid=[L("Ligar Herald of Thunder sem os 30 de Spirit livres", "Turning Herald of Thunder on without 30 free Spirit"), L("Usar Charged Staff sem cargas", "Using Charged Staff with no charges")],
  exit=[L("Body e botas de nível 33 (baratos) e a Nova + Perpetual Charge no Falling Thunder", "Level 33 body and boots (cheap) and Nova + Perpetual Charge on Falling Thunder")]),

 dict(id="a4", name=L("Ato 4 e Interlúdios", "Act 4 and Interludes"), lv=[46, 64], tag=L("Ascendência e o 2º buff de carga", "Ascendancy and the 2nd charge buff"),
  carry=L("Você: Falling Thunder + Charged Staff", "You: Falling Thunder + Charged Staff"), dmgSplit=[100, 0],
  goal=L("Três coisas nesta fase: (1) o Redflare Conduit e o Powertread sobem para as versões Runemastered (níveis 55 e 40) com sockets — runas de resistência resolvem o cap sem trocar de peça; (2) o anel Grip of Kulemak (quase de graça) dá crítico, dano crítico e +1 Power Charge; (3) Wind Dancer (tier 4, 30 Spirit) e Herald of Thunder passam a ser mantidos ligados. Advanced Thaumaturgy (2º Trial) faz a qualidade das gems virar efeito extra: comece a subir a qualidade com Gemcutter's Prism.",
         "Three things in this phase: (1) Redflare Conduit and Powertread move to the Runemastered versions (levels 55 and 40) with sockets — resistance runes fix the cap without changing pieces; (2) the Grip of Kulemak ring (nearly free) gives crit, crit damage and +1 Power Charge; (3) Wind Dancer (tier 4, 30 Spirit) and Herald of Thunder are now kept on. Advanced Thaumaturgy (2nd Trial) turns gem quality into an extra effect: start raising quality with Gemcutter's Prism."),
  rotation=[L("Wind Dancer e Herald of Thunder sempre ligados", "Wind Dancer and Herald of Thunder always on"), L("Charged Staff quando as cargas estiverem cheias", "Charged Staff when charges are full"), L("Falling Thunder no pack e no boss", "Falling Thunder on packs and bosses")],
  gems=[
   G("Falling Thunder", ["Nova Projectiles I", "Perpetual Charge", "Heightened Charges", "Rapid Attacks II", "Elemental Armament II"], L("Dano principal", "Main damage"), L("Já no setup de endgame, faltam só os links de luxo.", "Already on the endgame setup, only luxury links are missing."), "free"),
   G("Charged Staff", ["Perpetual Charge"], L("Buff de dano", "Damage buff"), L("Mantenha ativo antes dos slams grandes.", "Keep it active before big slams."), "free"),
   G("Herald of Thunder", ["Shock", "Vitality II"], L("Dano extra", "Extra damage"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Wind Dancer", ["Life Leech II", "Warm Blooded"], L("Defesa", "Defence"), L("Ganha estágios de Evasion; ao ser atingido, consome tudo para dar dano e Knock Back em volta. Tier 4, 30 Spirit.", "Gains Evasion stages; when hit, consumes them all to deal damage and Knock Back around. Tier 4, 30 Spirit."), "core", 2, SP30, since=52),
  ],
  cheap=["Redflare Conduit", "Powertread", "Grip of Kulemak"],
  full=["Redflare Conduit", "Powertread", "Grip of Kulemak"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Power Charges máximas", "Maximum Power Charges"), L("Dano crítico", "Critical damage")],
  tree=L("The Fabled Stag (cargas duram +40%, 10% de chance de não gastá-las, +10 Dex). O caminho até a região das cargas custa uns 20 pontos de atributo e de duração de carga, então o dano de árvore quase não sobe neste corte (~640% no total); o ganho vem das cargas. Confira sempre se as gems que você quer usar cumprem os requisitos de atributo.", "The Fabled Stag (charges last +40%, 10% chance not to spend them, +10 Dex). The road to the charge region costs about 20 points of attributes and charge duration, so tree damage barely rises in this cut (~640% in total); the gain comes from charges. Always check that the gems you want to use meet their attribute requirements."),
  avoid=[L("Ligar Wind Dancer + Herald sem ter os 60 de Spirit", "Turning on Wind Dancer + Herald without 60 Spirit"), L("Cortar Perpetual Charge do Falling Thunder", "Cutting Perpetual Charge from Falling Thunder")],
  exit=[L("3º Trial (~65): Implanted Gems", "3rd Trial (~65): Implanted Gems"), L("Nível 65: mapas", "Level 65: maps")]),

 dict(id="maps", name=L("Mapas 65+", "Maps 65+"), lv=[65, 78], tag=L("Motoric Implants: +2 níveis nas gems de Dexterity", "Motoric Implants: +2 levels on Dexterity gems"),
  carry=L("Você: Falling Thunder", "You: Falling Thunder"), dmgSplit=[100, 0],
  goal=L("Implanted Gems e Motoric Implants (3º e 4º Trials) somam +2 níveis a toda skill que exige Dexterity — Falling Thunder e Charged Staff ficam bem mais fortes. Adonia's Ego (wand, nível 78, custa ~0,1 Divine) entra no Weapon Set 2: Power Siphon (mata inimigos em Cull e dá 1 carga) e Pinnacle of Power (consome as cargas máximas para maestria elemental). O Darkness Enthroned (cinto) multiplica o efeito das runas e dá 3 slots de charm.",
         "Implanted Gems and Motoric Implants (3rd and 4th Trials) add +2 levels to every skill with a Dexterity requirement — Falling Thunder and Charged Staff get much stronger. Adonia's Ego (wand, level 78, costs ~0.1 Divine) goes in Weapon Set 2: Power Siphon (kills Cull-range enemies and grants 1 charge) and Pinnacle of Power (consumes max charges for elemental mastery). Darkness Enthroned (belt) multiplies rune effects and gives 3 charm slots."),
  rotation=[L("Herald e Wind Dancer sempre ligados", "Herald and Wind Dancer always on"), L("Weapon Set 2: Power Siphon + Pinnacle of Power quando as cargas estiverem no máximo", "Weapon Set 2: Power Siphon + Pinnacle of Power when charges are at max"), L("Weapon Set 1: Charged Staff e Falling Thunder", "Weapon Set 1: Charged Staff and Falling Thunder")],
  gems=[
   G("Falling Thunder", ["Nova Projectiles I", "Perpetual Charge", "Heightened Charges", "Rapid Attacks II", "Elemental Armament II", "Rakiata's Flow"], L("Dano principal", "Main damage"), L("O 6º link é o Rakiata's Flow (Lineage), que inverte as resistências do inimigo.", "The 6th link is Rakiata's Flow (Lineage), which inverts the enemy's resistances."), "free"),
   G("Charged Staff", ["Perpetual Charge", "Innervate", "Blazing Critical", "Thrill of the Kill II", "Ice Bite II"], L("Buff de dano", "Damage buff"), L("Mais supports = mais imbuições de elemento nos golpes.", "More supports = more element imbues on hits."), "free"),
   G("Herald of Thunder", ["Shock", "Elemental Focus", "Lightning Mastery"], L("Dano extra", "Extra damage"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Wind Dancer", ["Life Leech III", "Magnified Area II", "Freeze"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Charge Regulation", ["Perpetual Charge"], L("Buff por carga", "Buff per charge"), L("Ganha buffs fortes de acordo com as cargas ativas, mas consome cargas de tempos em tempos. Tier 14, 30 Spirit.", "Gains powerful buffs based on active charges, but consumes charges every few seconds. Tier 14, 30 Spirit."), "core", 3, SP30, since=52),
   G("Elemental Weakness", ["Spell Cascade"], L("Curse", "Curse"), L("Baixa as resistências elementais; com Rakiata's Flow, resistência negativa vira dano extra.", "Lowers elemental resistances; with Rakiata's Flow, negative resistance becomes extra damage."), "free", since=44),
  ],
  cheap=["Adonia's Ego", "Darkness Enthroned", "Grip of Kulemak"],
  full=["Adonia's Ego", "Darkness Enthroned", "Grip of Kulemak"],
  stats=[L("Power Charges máximas", "Maximum Power Charges"), L("Vida", "Life"), L("Crítico", "Crit")],
  tree=L("The Power Within (+1 carga máxima), One with the Storm (o Falling Thunder consome uma carga a mais: um projétil a mais por carga) e Martial Artistry (+25 Dex, +25% de dano crítico com cajado): o caminho até essas notables custa uma fila de atributos, por isso elas só entram aqui. A árvore de campanha fecha os 95 pontos; no 79 você faz o respec para a do PoB. Os Jewel Sockets recebem joias de crítico e ataque.", "The Power Within (+1 maximum charge), One with the Storm (Falling Thunder consumes one extra charge: one more projectile per charge) and Martial Artistry (+25 Dex, +25% crit damage with quarterstaves): the road to these notables costs a line of attributes, so they only come in here. The campaign tree closes its 95 points; at 79 you respec into the PoB's. The Jewel Sockets take crit and attack jewels."),
  avoid=[L("Ficar sem o Weapon Set 2 configurado", "Leaving Weapon Set 2 unconfigured"), L("Usar Pinnacle of Power sem as cargas no máximo", "Using Pinnacle of Power without max charges")],
  exit=[L("Adonia's Ego: +1 carga máxima e o skill Pinnacle of Power", "Adonia's Ego: +1 max charge and the Pinnacle of Power skill")]),

 dict(id="endgame", name=L("Endgame T15", "Endgame T15"), lv=[79, 90], tag=L("Amuleto com Eternal Rage e mais níveis de skill", "Amulet with Eternal Rage and more skill levels"),
  carry=L("Você: Falling Thunder", "You: Falling Thunder"), dmgSplit=[100, 0],
  goal=L("O amuleto rare com +4 níveis de Melee e a skill Eternal Rage (100 Spirit) vira o item que mais empurra o dano. O Sacred Flame (sceptre, ~5 Divines) dá +100 Spirit e Purity of Fire de brinde e o cajado Blood Spire (rare) traz +3 níveis de Attack. Foque em Spirit, +níveis de skill e resistências no cap.",
         "The rare amulet with +4 Melee levels and the Eternal Rage skill (100 Spirit) becomes the item that pushes damage the most. Sacred Flame (sceptre, ~5 Divines) gives +100 Spirit and a free Purity of Fire, and the Blood Spire quarterstaff (rare) brings +3 Attack levels. Focus on Spirit, + skill levels and capped resistances."),
  rotation=[L("Tudo ligado: Herald, Wind Dancer, Charge Regulation e Eternal Rage", "Everything on: Herald, Wind Dancer, Charge Regulation and Eternal Rage"), L("Pinnacle of Power ao encher as cargas", "Pinnacle of Power when charges fill"), L("Falling Thunder no boss e no pack", "Falling Thunder on boss and pack")],
  gems=[
   G("Falling Thunder", ["Nova Projectiles I", "Perpetual Charge", "Rapid Attacks II", "Elemental Armament II", "Rakiata's Flow"], L("Dano principal", "Main damage"), L("Nível 20 (+23% de qualidade).", "Level 20 (+23% quality)."), "free"),
   G("Charged Staff", ["Perpetual Charge", "Innervate", "Blazing Critical", "Thrill of the Kill II", "Ice Bite II"], L("Buff de dano", "Damage buff"), L("Nível 19, 20% de qualidade.", "Level 19, 20% quality."), "free"),
   G("Eternal Rage", [], L("Rage constante", "Constant Rage"), L("Vem do amuleto (nível 18): regenera Rage o tempo todo. 100 Spirit.", "Comes from the amulet (level 18): constantly regenerates Rage. 100 Spirit."), "core", 4, L("100 Spirit", "100 Spirit"), since=79),
   G("Purity of Fire", ["Warm Blooded", "Vitality II", "Strong Hearted", "Cool Headed", "Precision II"], L("Aura", "Aura"), L("Vem do Sacred Flame: resistência a fogo e o buff de aura.", "Comes from Sacred Flame: fire resistance and the aura buff."), "free"),
  ],
  cheap=["Sacred Flame", "Adonia's Ego", "Darkness Enthroned"],
  full=["Sacred Flame", "Adonia's Ego", "Darkness Enthroned"],
  stats=[L("Spirit", "Spirit"), L("+ níveis de skill", "+ skill levels"), L("Resistências", "Resistances")],
  tree=L("Aqui a árvore passa a ser a do PoB: ela parte do ponto inicial do Monk graças à joia Split Personality (socket 21984), por isso não gasta a fila de nós de Atributo do caminho da Mercenary. O respec desfaz a árvore de campanha (quase nada dela está na árvore do PoB) e entram Moment of Truth, Deadly Force, For the Jugular, Overflowing Power (+2 cargas), Critical Exploit, True Strike, Flow Like Water, Careful Assassin e Throatseeker. Sem a joia, continue pela árvore de campanha e vá pegando as notables de crítico pelo caminho da Mercenary.", "From here the tree is the PoB's: it starts at the Monk starting point thanks to the Split Personality jewel (socket 21984), so it doesn't spend the line of Attribute nodes on the Mercenary road. The respec undoes the campaign tree (almost none of it is on the PoB's tree) and Moment of Truth, Deadly Force, For the Jugular, Overflowing Power (+2 charges), Critical Exploit, True Strike, Flow Like Water, Careful Assassin and Throatseeker come in. Without the jewel, keep the campaign tree and pick up the crit notables along the Mercenary road."),
  avoid=[L("Ficar sem resistência de raio no cap", "Being short on lightning resistance"), L("Comprar o Sacred Flame antes do Adonia's Ego e do amuleto", "Buying Sacred Flame before Adonia's Ego and the amulet")],
  exit=[L("Sacred Flame + amuleto com +4 Melee", "Sacred Flame + a +4 Melee amulet")]),

 dict(id="max", name=L("Pinnacle / o build do PoB", "Pinnacle / the PoB build"), lv=[91, 100], tag=L("192M de DPS no PoB", "192M DPS in the PoB"),
  carry=L("Você: Falling Thunder", "You: Falling Thunder"), dmgSplit=[100, 0],
  goal=L("O build final é exatamente o PoB do poe.ninja: joias diamante corruptas (Prism of Belief +2 níveis de Falling Thunder, Heart of the Well com dano extra de frio e raio, Megalomaniac, Split Personality), o anel Kalandra's Touch (~33 Divines), capacete e luvas rare com bônus de gem. É luxo: 90% do dano já vem do endgame anterior.",
         "The final build is exactly the poe.ninja PoB: corrupted Diamond jewels (Prism of Belief +2 Falling Thunder levels, Heart of the Well with extra cold and lightning damage, Megalomaniac, Split Personality), the Kalandra's Touch ring (~33 Divines), rare helmet and gloves with gem bonuses. It's luxury: 90% of the damage already comes from the previous endgame."),
  rotation=[L("Igual ao endgame anterior", "Same as the previous endgame")],
  gems=[
   G("Falling Thunder", ["Nova Projectiles I", "Perpetual Charge", "Rapid Attacks II", "Elemental Armament II", "Rakiata's Flow"], L("Dano principal", "Main damage"), L("Nível 20 (+23% de qualidade), com Prism of Belief.", "Level 20 (+23% quality), with Prism of Belief."), "free"),
  ],
  cheap=[L("Igual ao endgame", "Same as endgame")], full=["Kalandra's Touch", "Sacred Flame"],
  stats=[L("Dano", "Damage")], tree=L("Mesma árvore do endgame.", "Same tree as the endgame."),
  avoid=[L("Gastar Divines antes de fechar Spirit, resistência e +níveis", "Spending Divines before Spirit, resistances and + levels are closed")], exit=[]),
]
PH = {p["id"]: p for p in PHASES}
for pid, note in {"a3": L("Herald of Thunder: 30 Spirit. Cabe com os 30 do King in the Mists.", "Herald of Thunder: 30 Spirit. Fits with the 30 from King in the Mists."),
                  "a4": L("Herald (30) + Wind Dancer (30) = 60 Spirit.", "Herald (30) + Wind Dancer (30) = 60 Spirit."),
                  "maps": L("Herald 30 + Wind Dancer 30 + Charge Regulation 30 = 90 Spirit.", "Herald 30 + Wind Dancer 30 + Charge Regulation 30 = 90 Spirit."),
                  "endgame": L("Sacred Flame dá 100 Spirit: Herald + Wind Dancer + Charge Regulation e sobra 10.", "Sacred Flame gives 100 Spirit: Herald + Wind Dancer + Charge Regulation with 10 left over.")}.items():
    PH[pid]["spiritNote"] = note
BOX = {
 "a1": ("3", [L("Sem fonte de carga ainda", "No charge source yet")], L("O Falling Thunder funciona como um slam de raio normal; as cargas vêm depois.", "Falling Thunder works as a plain lightning slam; charges come later.")),
 "a2": ("3", ["Breath of the Mountains"], L("A carga vem do charm, uma de cada vez.", "The charge comes from the charm, one at a time.")),
 "a3": ("4", [L("Redflare Conduit: 20% por acerto", "Redflare Conduit: 20% per hit"), "Powertread +1"], L("Agora as cargas se geram sozinhas.", "Now the charges generate themselves.")),
 "a4": ("6", ["The Power Within +1", "Grip of Kulemak +1"], L("A passiva e o anel sobem o máximo.", "The passive and the ring raise the maximum.")),
 "maps": ("8", [L("Capacete +2 (rare)", "Helmet +2 (rare)")], L("Um capacete com +2 Power Charges máximas.", "A helmet with +2 maximum Power Charges.")),
 "endgame": ("11", ["Adonia's Ego +1", "Overflowing Power +2"], L("Com a wand, o Pinnacle of Power fica sempre à mão.", "With the wand, Pinnacle of Power is always at hand.")),
 "max": ("12", ["Kalandra's Touch +1"], L("12 cargas máximas no PoB do poe.ninja (o anel copia o +1 do Grip of Kulemak).", "12 maximum charges in the poe.ninja PoB (the ring copies Grip of Kulemak's +1).")),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}

MILESTONES = {
 1: L("Falling Thunder (Uncut Skill Gem nível 1) com Rapid Attacks I e Elemental Armament I.", "Falling Thunder (level 1 Uncut Skill Gem) with Rapid Attacks I and Elemental Armament I."),
 5: L("Breath of the Mountains (charm nível 5): 1 Power Charge ao usar.", "Breath of the Mountains (level 5 charm): 1 Power Charge on use."),
 10: L("King in the Mists: +30 Spirit.", "King in the Mists: +30 Spirit."),
 16: L("Cajado nível 16 craftado.", "Crafted level 16 quarterstaff."),
 18: L("Nova Projectiles I e Perpetual Charge no Falling Thunder.", "Nova Projectiles I and Perpetual Charge on Falling Thunder."),
 28: L("1º Trial: Essence of Virtue (Virtuous Barrier).", "1st Trial: Essence of Virtue (Virtuous Barrier)."),
 32: L("Charged Staff (Uncut Skill Gem nível 9).", "Charged Staff (level 9 Uncut Skill Gem)."),
 33: L("Redflare Conduit e Powertread (nível 33): as cargas se geram sozinhas.", "Redflare Conduit and Powertread (level 33): charges generate themselves."),
 34: L("Herald of Thunder (30 Spirit).", "Herald of Thunder (30 Spirit)."),
 40: L("2º Trial: Advanced Thaumaturgy. Comece a subir a qualidade das gems.", "2nd Trial: Advanced Thaumaturgy. Start raising gem quality."),
 52: L("Wind Dancer e Charge Regulation.", "Wind Dancer and Charge Regulation."),
 55: L("Redflare Conduit Runemastered (sockets para runas).", "Runemastered Redflare Conduit (sockets for runes)."),
 62: L("Darkness Enthroned (cinto, nível 62).", "Darkness Enthroned (belt, level 62)."),
 65: L("3º Trial: Implanted Gems. Primeiros mapas.", "3rd Trial: Implanted Gems. First maps."),
 75: L("4º Trial: Motoric Implants (+2 níveis nas skills de Dex).", "4th Trial: Motoric Implants (+2 levels on Dex skills)."),
 78: L("Adonia's Ego (wand): Power Siphon + Pinnacle of Power.", "Adonia's Ego (wand): Power Siphon + Pinnacle of Power."),
 79: L("Amuleto com Eternal Rage e +4 Melee.", "Amulet with Eternal Rage and +4 Melee."),
 84: L("Sacred Flame (sceptre): +100 Spirit.", "Sacred Flame (sceptre): +100 Spirit."),
 90: L("Falling Thunder e Charged Staff no nível de gem 20.", "Falling Thunder and Charged Staff at gem level 20."),
}

ASCENDANCY = [
 dict(order=1, key="eov", node="Essence of Virtue", when=L("1º Trial (~nível 28)", "1st Trial (~level 28)"), text=L("Concede a skill Virtuous Barrier: uma barreira que acumula Motes protetores de cada atributo ao longo do tempo, mas perde um Mote quando você é atingido.", "Grants the Virtuous Barrier skill: a barrier that accumulates protective Motes of each attribute over time, but loses a random Mote when you're hit."), why=L("É a defesa da build. Ela custa 2 pontos (o nó de Skill Gem Quality no caminho também dá +2% de qualidade).", "It's the build's defence. It costs 2 points (the Skill Gem Quality node on the way also gives +2% quality).")),
 dict(order=2, key="at", node="Advanced Thaumaturgy", when=L("2º Trial (~nível 40)", "2nd Trial (~level 40)"), text=L("A qualidade das gems dá às skills equipadas um efeito adicional.", "Gem quality grants socketed skills an additional effect."), why=L("Transforma cada ponto de qualidade em poder extra. O amuleto (+5%), as notables (+2% cada) e o Gemcutter's Prism empurram o total.", "Turns every quality point into extra power. The amulet (+5%), the notables (+2% each) and Gemcutter's Prism push the total.")),
 dict(order=3, key="ig", node="Implanted Gems", when=L("3º Trial (~nível 65)", "3rd Trial (~level 65)"), text=L("Nó de passagem para Motoric Implants.", "Pass-through node to Motoric Implants."), why=L("O caminho: Skill Gem Quality → Implanted Gems → Motoric Implants.", "The path: Skill Gem Quality → Implanted Gems → Motoric Implants.")),
 dict(order=4, key="mi", node="Motoric Implants", when=L("4º Trial (~nível 75)", "4th Trial (~level 75)"), text=L("+2 níveis em todas as skills que exigem Dexterity.", "+2 levels on all skills with a Dexterity requirement."), why=L("Falling Thunder e Charged Staff exigem Dex: é o maior salto de dano de ascendência da build.", "Falling Thunder and Charged Staff require Dex: it's the biggest ascendancy damage jump of the build.")),
 dict(order=5, key="gs", node="Gem Studded", when=L("9º ponto (Trials extras)", "9th point (extra Trials)"), text=L("Para cada cor de support socketado mais numerosa: Vermelho = hits contra você sem Critical Damage Bonus; Azul = skills custam 30% menos; Verde = 40% menos penalidade de velocidade ao usar skills andando.", "For each colour of Socketed Support Gem that is most numerous: Red = hits against you have no Critical Damage Bonus; Blue = skills have 30% less cost; Green = 40% less Movement Speed Penalty from using skills while Moving."), why=L("O PoB usa Falling Thunder com 4 supports verdes (Dex): a cor mais numerosa é a verde.", "The PoB's Falling Thunder has 4 green (Dex) supports: green is the most numerous colour.")),
]
ASC_UNLOCK = [28, 40, 65, 75]
PHASE_START = {"endgame": 44683, "max": 44683}   # o PoB do endgame parte do início do Monk (joia Split Personality)
ASC_PHASE = {"a1": [], "a2": ["Essence of Virtue"], "a3": ["Essence of Virtue", "Advanced Thaumaturgy"], "a4": ["Essence of Virtue", "Advanced Thaumaturgy"],
             "maps": ["Essence of Virtue", "Advanced Thaumaturgy", "Implanted Gems"], "endgame": ["Essence of Virtue", "Advanced Thaumaturgy", "Implanted Gems", "Motoric Implants"]}

KEY_PASSIVES = [
 dict(node="Martial Artistry", type="Notable", text=L("+25 Dexterity, +25% Accuracy e +25% de dano crítico com Quarterstaves.", "+25 Dexterity, +25% Accuracy and +25% crit damage with Quarterstaves."), when=L("Mapas (65+) → sempre", "Maps (65+) → forever"), why=L("Abre o crítico de cajado e paga o requisito de Dex do Falling Thunder.", "Opens quarterstaff crit and pays the Falling Thunder Dex requirement.")),
 dict(node="Stand and Deliver", type="Notable", text=L("Projéteis: +40% de Critical Damage Bonus e +25% de dano contra inimigos a menos de 2 m.", "Projectiles: +40% Critical Damage Bonus and +25% damage against enemies within 2 m."), when=L("Endgame (79+)", "Endgame (79+)"), why=L("O Falling Thunder sai do impacto perto de você: quase sempre está a menos de 2 m.", "Falling Thunder fires from impact close to you: almost always within 2 m.")),
 dict(node="The Fabled Stag", type="Notable", text=L("+40% de duração das cargas, +10 Dex e 10% de chance de uma skill não gastar as cargas.", "+40% charge duration, +10 Dex and a 10% chance for skills not to spend charges."), when=L("Ato 4 (46+) → sempre", "Act 4 (46+) → forever"), why=L("Soma com o Perpetual Charge: as cargas duram e rendem mais.", "Stacks with Perpetual Charge: charges last longer and go further.")),
 dict(node="One with the Storm", type="Notable", text=L("Skills de Quarterstaff que consomem Power Charges contam como consumindo uma carga adicional.", "Quarterstaff skills that consume Power Charges count as consuming an additional Power Charge."), when=L("Mapas (65+) → sempre", "Maps (65+) → forever"), why=L("Cada carga rende um projétil a mais no Falling Thunder.", "Each charge yields one more Falling Thunder projectile.")),
 dict(node="The Power Within", type="Notable", text=L("+1 Power Charge máxima e +20% de dano crítico ao ganhar uma carga.", "+1 maximum Power Charge and +20% crit damage after gaining a charge."), when=L("Mapas (65+) → sempre", "Maps (65+) → forever"), why=L("Mais cargas = mais projéteis.", "More charges = more projectiles.")),
 dict(node="Overflowing Power", type="Notable", text=L("+2 Power Charges máximas.", "+2 maximum Power Charges."), when=L("Endgame", "Endgame"), why=L("O maior salto de cargas: é a última notable do caminho.", "The biggest charge jump: it's the last notable on the path.")),
 dict(node="Throatseeker", type="Notable", text=L("+60% de dano crítico, −20% de chance de crítico.", "+60% crit damage, −20% crit chance."), when=L("Endgame", "Endgame"), why=L("Só faz sentido depois que o crítico já está alto.", "Only makes sense once crit is already high.")),
]
TREE_STAGES = [
 dict(lv="1–15", focus=L("Dano de melee perto do início (Overwhelm, Cruel Methods)", "Melee damage near the start (Overwhelm, Cruel Methods)"), dmg="Falling Thunder", **{"def": L("Vida", "Life")}, spirit="—", dont=L("Pegar nós de projétil ou de spell: o Falling Thunder não os usa", "Taking projectile or spell nodes: Falling Thunder doesn't use them")),
 dict(lv="16–31", focus=L("Dano físico e de duas mãos (Finishing Blows)", "Physical and two-handed damage (Finishing Blows)"), dmg="Falling Thunder + Nova", **{"def": L("Vida e resistências", "Life and resistances")}, spirit=L("nenhum ainda", "none yet"), dont=L("Esquecer de guardar currency para o nível 33", "Forgetting to save currency for level 33")),
 dict(lv="32–64", focus=L("Dano e velocidade de ataque; cargas (Fabled Stag, depois One with the Storm e Power Within)", "Attack damage and speed; charges (Fabled Stag, then One with the Storm and Power Within)"), dmg="Falling Thunder + Charged Staff", **{"def": L("Vida e resistências com runas", "Life and resistances with runes")}, spirit="Herald · Wind Dancer", dont=L("Ligar buffs sem Spirit", "Turning buffs on without Spirit")),
 dict(lv="65–100", focus=L("Respec para o PoB: crítico, velocidade e +2 cargas (Overflowing Power)", "Respec into the PoB: crit, speed and +2 charges (Overflowing Power)"), dmg="Falling Thunder", **{"def": L("Virtuous Barrier + Wind Dancer", "Virtuous Barrier + Wind Dancer")}, spirit="Charge Regulation · Eternal Rage", dont=L("Perder o requisito de Dex", "Losing the Dex requirement")),
]

UNIQUES = [
 U("Breath of the Mountains", "Charm", "Charm", "a2", L("Charm que dá 1 Power Charge ao ser usado (quando você leva dano de frio).", "A charm that grants 1 Power Charge when used (when you take cold damage)."), L("Ele te dá a primeira carga no Ato 2, quando ainda não há Redflare.", "It gives you the first charge in Act 2, before Redflare."), L("Charm mágico com carga extra.", "A magic charm with extra charges."), 5),
 U("Redflare Conduit", "Body Armour", L("Armadura", "Armour"), "a3", L("20% de chance de ganhar um Power Charge ao acertar, mais mana e resistência a raio. Perde todas as cargas ao atingir o máximo e te choca (Shock).", "20% chance to gain a Power Charge on hit, plus mana and lightning resistance. Loses all charges when reaching maximum and Shocks you."), L("É a fonte principal de cargas da build de nível 33 até o fim. Nível 33 (base normal), 55 (Runemastered, com sockets).", "It's the main charge source from level 33 to the end. Level 33 (normal base), 55 (Runemastered, with sockets)."), L("Body de ES com Power Charge on hit.", "ES body with Power Charge on hit."), 33),
 U("Powertread", L("Botas", "Boots"), L("Armadura", "Armour"), "a3", L("+1 carga máxima, 15–20% de velocidade de movimento e mais dano crítico por carga.", "+1 maximum charge, 15–20% movement speed and more crit damage per charge."), L("Barata e forte: sobe o teto de cargas.", "Cheap and strong: raises the charge ceiling."), L("Botas com velocidade de movimento.", "Boots with movement speed."), 33),
 U("Grip of Kulemak", "Ring", L("Acessório", "Accessory"), "a4", L("Crítico, dano crítico, +1 carga máxima e Abyssal Wasting nos acertos.", "Crit, crit damage, +1 maximum charge and Abyssal Wasting on hit."), L("Quase de graça e empurra o crítico.", "Nearly free and pushes crit."), L("Anel com crítico.", "A ring with crit.")),
 U("Darkness Enthroned", L("Cinto", "Belt"), L("Acessório", "Accessory"), "maps", L("3 slots de charm, dobra o efeito das runas socketadas e o cinto conta como body armour.", "3 charm slots, doubles the effect of socketed runes and the belt counts as a body armour."), L("Runas de gem/quality rendem muito mais.", "Gem/quality runes go much further."), L("Cinto com slot de charm.", "A belt with charm slots."), 62),
 U("Adonia's Ego", "Wand", L("Arma", "Weapon"), "maps", L("+3 níveis de Spell, +1 carga máxima, e concede Power Siphon (nível 18) e Pinnacle of Power. Em contrapartida: −10% a todas as resistências elementais por carga.", "+3 levels of Spell skills, +1 maximum charge, and grants Power Siphon (level 18) and Pinnacle of Power. In exchange: −10% to all elemental resistances per charge."), L("Use no Weapon Set 2 apenas para as duas skills.", "Use in Weapon Set 2 just for the two skills."), L("Wand normal com Power Siphon.", "A plain wand with Power Siphon."), 78),
 U("Sacred Flame", "Sceptre", L("Arma", "Weapon"), "endgame", L("Spirit +100, Purity of Fire (nível 20) e +44% do dano como fogo extra.", "+100 Spirit, Purity of Fire (level 20) and +44% of damage as extra fire."), L("Paga Herald + Wind Dancer + Charge Regulation.", "Pays for Herald + Wind Dancer + Charge Regulation."), L("Sceptre com Spirit.", "A sceptre with Spirit."), 84),
 U("Nascent Hope", "Charm", "Charm", "a4", L("Usado ao ficar Frozen; dá carga ao matar e recarrega o ES.", "Used when Frozen; gains a charge when you kill and recharges ES."), L("Cobre o Freeze e gera cargas de charm.", "Covers Freeze and generates charm charges."), L("Thawing Charm normal.", "A regular Thawing Charm."), 12),
 U("Lavianga's Spirits", "Flask", "Flask", "maps", L("O flask não pode ser usado: o efeito fica ativo o tempo todo (71% menos recuperado).", "The flask cannot be used: the effect is always active (71% less recovered)."), L("Mana constante sem apertar nada.", "Constant mana without pressing anything."), L("Flask de mana normal.", "A regular mana flask."), 49),
 U("The Fall of the Axe", "Charm", "Charm", "max", L("Dá Onslaught durante o efeito.", "Grants Onslaught during its effect."), L("Luxo.", "Luxury."), L("Silver Charm normal.", "A regular Silver Charm."), 10),
 U("Kalandra's Touch", "Ring", L("Acessório", "Accessory"), "max", L("Copia o outro anel (espelha os mods).", "Copies the other ring (mirrors its mods)."), L("Só depois de tudo: ~33 Divines.", "Only after everything else: ~33 Divines."), L("Anel rare bom.", "A good rare ring.")),
]

GEAR = [
 dict(slot=L("Cajado (Set 1)", "Quarterstaff (Set 1)"), cheap=L("Craftado a cada salto: 16 → 33 → 59", "Crafted at each jump: 16 → 33 → 59"), value=L("Rare com + níveis de Attack e dano elemental", "Rare with + Attack levels and elemental damage"), full=L("Blood Spire: +3 níveis de Attack, dano de fogo e raio adicionados", "Blood Spire: +3 Attack levels, added fire and lightning damage"), affix=L("+ níveis de Attack; dano elemental; velocidade", "+ Attack levels; elemental damage; speed"), note=""),
 dict(slot=L("Wand (Set 2)", "Wand (Set 2)"), cheap=L("Nada", "None"), value="Adonia's Ego", full="Adonia's Ego", affix="—", note=L("Só para Power Siphon e Pinnacle of Power", "Only for Power Siphon and Pinnacle of Power")),
 dict(slot=L("Capacete", "Helmet"), cheap=L("Vida, ES e resistências", "Life, ES and resistances"), value=L("Base com +2 Power Charges máximas", "Base with +2 maximum Power Charges"), full=L("Gloom Crown: ES alto, +2 cargas, vida", "Gloom Crown: high ES, +2 charges, life"), affix=L("+ Power Charges máximas; ES; resistências", "+ maximum Power Charges; ES; resistances"), note=""),
 dict(slot="Body Armour", cheap="Redflare Conduit", value="Redflare Conduit (Runemastered)", full="Redflare Conduit (Runemastered)", affix="—", note=""),
 dict(slot=L("Luvas", "Gloves"), cheap=L("Vida e resistências", "Life and resistances"), value=L("Dano adicionado a ataques", "Added damage to attacks"), full=L("Storm Fingers: dano adicionado, +2 níveis de Melee", "Storm Fingers: added damage, +2 Melee levels"), affix=L("Dano adicionado; + níveis de Melee", "Added damage; + Melee levels"), note=""),
 dict(slot=L("Botas", "Boots"), cheap="Powertread", value="Powertread (Runemastered)", full="Powertread (Runemastered)", affix="—", note=L("Três sockets: Desert, Glacial e Storm para fechar as resistências", "Three sockets: Desert, Glacial and Storm to close resistances")),
 dict(slot=L("Amuleto", "Amulet"), cheap=L("Vida e resistências", "Life and resistances"), value=L("Spirit ou + níveis", "Spirit or + levels"), full=L("Brimstone Torc: +4 níveis de Melee, Eternal Rage, +5% qualidade", "Brimstone Torc: +4 Melee levels, Eternal Rage, +5% quality"), affix=L("+ níveis de Melee; qualidade; ES", "+ Melee levels; quality; ES"), note=""),
 dict(slot=L("Anéis", "Rings"), cheap=L("Vida e resistências", "Life and resistances"), value="Grip of Kulemak", full="Grip of Kulemak · Kalandra's Touch", affix=L("Crítico; resistências", "Crit; resistances"), note=""),
 dict(slot=L("Cinto", "Belt"), cheap=L("Vida e resistências", "Life and resistances"), value="Darkness Enthroned", full="Darkness Enthroned", affix="—", note=""),
 dict(slot="Charms", cheap="Breath of the Mountains", value="Nascent Hope", full="Nascent Hope · The Fall of the Axe", affix=L("Cobrir Freeze/Slow", "Cover Freeze/Slow"), note=""),
 dict(slot="Flasks", cheap=L("Vida e mana", "Life and mana"), value="Lavianga's Spirits", full="Lavianga's Spirits · Ultimate Life", affix=L("Recuperação", "Recovery"), note=""),
 dict(slot=L("Joias", "Jewels"), cheap=L("Nenhuma", "None"), value=L("Rare de crítico e ataque", "Rare crit and attack jewels"), full=L("Prism of Belief, Heart of the Well, Megalomaniac, Split Personality + 3 rares", "Prism of Belief, Heart of the Well, Megalomaniac, Split Personality + 3 rares"), affix=L("Crítico; velocidade; dano elemental", "Crit; speed; elemental damage"), note=L("Os diamantes corruptos são luxo", "The corrupted Diamonds are luxury")),
]
BUY_ORDER = [
 dict(p=1, item="Breath of the Mountains", phase=L("Ato 2", "Act 2"), cost=L("Barato", "Cheap"), impact=L("Primeira Power Charge", "First Power Charge")),
 dict(p=2, item="Redflare Conduit + Powertread", phase=L("Ato 3", "Act 3"), cost=L("Barato", "Cheap"), impact=L("Cargas contínuas: a build vira", "Continuous charges: the build turns on")),
 dict(p=3, item="Grip of Kulemak", phase=L("Ato 4", "Act 4"), cost=L("Barato", "Cheap"), impact=L("Crítico e +1 carga", "Crit and +1 charge")),
 dict(p=4, item="Darkness Enthroned", phase=L("Mapas", "Maps"), cost=L("Barato", "Cheap"), impact=L("Charm slots e runas dobradas", "Charm slots and doubled runes")),
 dict(p=5, item="Adonia's Ego", phase=L("Mapas", "Maps"), cost=L("Barato", "Cheap"), impact=L("Power Siphon + Pinnacle", "Power Siphon + Pinnacle")),
 dict(p=6, item=L("Amuleto com +Melee e Eternal Rage", "Amulet with + Melee and Eternal Rage"), phase="T15", cost=L("Valor", "Value"), impact=L("Mais níveis de skill", "More skill levels")),
 dict(p=7, item="Sacred Flame", phase="T15", cost=L("Valor", "Value"), impact=L("+100 Spirit", "+100 Spirit")),
 dict(p=8, item="Kalandra's Touch + diamantes", phase="Pinnacle", cost=L("Luxo", "Luxury"), impact=L("Teto de dano", "Damage ceiling")),
]

TRICKS = [
 {"cat": L("Cargas", "Charges"), "lvl": L("Fácil", "Easy"), "title": L("Perpetual Charge faz uma carga render vários slams", "Perpetual Charge makes one charge pay for several slams"), "body": L("Skills que consomem carga têm uma chance de NÃO removê-la (ainda ganhando o efeito). Coloque o Perpetual Charge em toda skill que consome carga: Falling Thunder, Charged Staff, Charge Regulation. A passiva The Fabled Stag soma mais 10% de chance.", "Skills that consume charges have a chance NOT to remove them (still getting the effect). Put Perpetual Charge on every skill that consumes charges: Falling Thunder, Charged Staff, Charge Regulation. The Fabled Stag passive adds another 10% chance.")},
 {"cat": L("Cargas", "Charges"), "lvl": L("Médio", "Medium"), "title": L("Redflare Conduit: o custo escondido", "Redflare Conduit: the hidden cost"), "body": L("O body dá cargas, mas perde todas ao chegar no máximo e te choca (Shock). Por isso o Strong Hearted (Shock em você dura menos) aparece nos supports do Purity of Fire. Não use Overcharge onde você não precisa do Shock.", "The body gives charges, but loses all of them when you hit maximum and Shocks you. That's why Strong Hearted (Shock on you lasts shorter) shows up in the Purity of Fire supports. Don't use Overcharge where you don't need the Shock.")},
 {"cat": L("Cargas", "Charges"), "lvl": L("Médio", "Medium"), "title": L("Adonia's Ego custa resistência", "Adonia's Ego costs resistance"), "body": L("Cada Power Charge tira 10% de todas as resistências elementais. Como o Falling Thunder gasta cargas o tempo todo, você quase nunca fica no máximo — mas mantenha resistência de sobra para o momento em que ficar.", "Every Power Charge takes away 10% of all elemental resistances. Since Falling Thunder spends charges all the time you're rarely at maximum — but keep some spare resistance for when you are.")},
 {"cat": L("Gems", "Gems"), "lvl": L("Fácil", "Easy"), "title": L("Advanced Thaumaturgy vive de qualidade", "Advanced Thaumaturgy lives on quality"), "body": L("Cada 1% de qualidade nas skills da ascendência conta: notables de Skill Gem Quality (+2%), amuleto (+5%), cinto Darkness Enthroned (+10% pela runa) e Gemcutter's Prism nas gems principais.", "Every 1% of quality on skills counts: Skill Gem Quality notables (+2%), amulet (+5%), Darkness Enthroned (+10% via rune) and Gemcutter's Prism on the main gems.")},
 {"cat": L("Gems", "Gems"), "lvl": L("Médio", "Medium"), "title": L("Rakiata's Flow + Elemental Weakness", "Rakiata's Flow + Elemental Weakness"), "body": L("Elemental Weakness abaixa as resistências do inimigo; o Rakiata's Flow trata resistências como invertidas. Se o inimigo chegar em resistência negativa, ela vira dano extra em vez de perda.", "Elemental Weakness lowers enemy resistances; Rakiata's Flow treats resistances as inverted. If the enemy reaches negative resistance, it becomes extra damage instead of a loss.")},
 {"cat": L("Gems", "Gems"), "lvl": L("Fácil", "Easy"), "title": L("Gem Studded: a cor que mais aparece manda", "Gem Studded: the most common colour rules"), "body": L("Conte os supports por cor: verde (Dex) → menos penalidade de movimento; azul (Int) → skills custam 30% menos; vermelho (Str) → hits contra você sem dano crítico bônus. Trocar um support pode virar a cor.", "Count supports by colour: green (Dex) → less movement penalty; blue (Int) → skills cost 30% less; red (Str) → hits against you have no critical bonus. Swapping one support can flip the colour.")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Atributos: +5 é o caminho, não o destino", "Attributes: +5 is the path, not the destination"), "body": L("A árvore da build tem dezenas de nós de +5 Atributo. Eles cumprem os requisitos (Dex/Int/Str) das gems; se você já cumpre, pule e siga para a próxima notable.", "The build's tree has dozens of +5 Attribute nodes. They meet gem requirements (Dex/Int/Str); if you already do, skip and head for the next notable.")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Nível de gem x nível do personagem", "Gem level vs. character level"), "body": L("Pelos dados do Path of Building, gem nível 5 exige personagem 14, nível 10 exige 36, nível 15 exige 64 e nível 20 exige 90. Não adianta comprar a gem antes.", "According to Path of Building data, gem level 5 requires character level 14, level 10 requires 36, level 15 requires 64 and level 20 requires 90. There's no point buying the gem earlier.")},
 {"cat": L("Defesa", "Defence"), "lvl": L("Médio", "Medium"), "title": L("Virtuous Barrier", "Virtuous Barrier"), "body": L("Fica ligada e vai acumulando Motes protetores; cada hit derruba um Mote aleatório. Fugir de hit importa mais que curar.", "It stays on and keeps accumulating protective Motes; every hit drops a random Mote. Avoiding hits matters more than healing.")},
]

TROUBLESHOOT = [
 (L("O Falling Thunder não solta projéteis", "Falling Thunder isn't firing projectiles"), L("Ele só solta projéteis se consumir Power Charges. Sem carga é só um slam. Veja se o Redflare Conduit está equipado e se você tem um charm ou Power Siphon para gerar cargas.", "It only fires projectiles when it consumes Power Charges. With none it's just a slam. Check that Redflare Conduit is equipped and that you have a charm or Power Siphon to generate charges.")),
 (L("As cargas acabam rápido", "Charges run out fast"), L("Faltou Perpetual Charge (ou a passiva The Fabled Stag). Suba também o máximo de cargas: The Power Within, Overflowing Power, Powertread e o capacete.", "You're missing Perpetual Charge (or The Fabled Stag). Also raise the maximum: The Power Within, Overflowing Power, Powertread and the helmet.")),
 (L("Levo Shock o tempo todo", "I keep getting Shocked"), L("É o efeito do Redflare Conduit ao chegar no máximo de cargas. Coloque Strong Hearted num buff persistente e, se puder, gaste as cargas com o Charged Staff antes de encher.", "That's Redflare Conduit's effect when you hit max charges. Put Strong Hearted on a persistent buff and, if you can, spend charges with Charged Staff before they fill.")),
 (L("Não consigo usar a gem que quero", "I can't use the gem I want"), L("Confira o requisito de Dex/Int/Str na gem. Pegue os +5 Atributo do caminho e o nó Reduced Attribute Requirements da ascendência.", "Check the gem's Dex/Int/Str requirement. Take the +5 Attribute nodes on the path and the Reduced Attribute Requirements ascendancy node.")),
 (L("O Spirit não fecha", "Spirit doesn't add up"), L("Herald (30) + Wind Dancer (30) + Charge Regulation (30) = 90; Eternal Rage é 100. No PoB o Spirit total é 100 (Sacred Flame): desligue Eternal Rage se ele for do amuleto e você não tiver o sceptre.", "Herald (30) + Wind Dancer (30) + Charge Regulation (30) = 90; Eternal Rage is 100. In the PoB total Spirit is 100 (Sacred Flame): turn Eternal Rage off if it comes from the amulet and you don't have the sceptre.")),
 (L("Estou fraco depois do nível 75", "I'm weak after level 75"), L("Confira os 4 Trials: Motoric Implants dá +2 níveis de skill Dex. E veja se o cajado tem + níveis de Attack.", "Check the 4 Trials: Motoric Implants gives +2 levels of Dex skills. And check that the quarterstaff has + Attack levels.")),
]

ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Resistências no cap · Redflare Conduit + Powertread runemastered", "Resistances capped · Runemastered Redflare Conduit + Powertread"), gear="Redflare · Powertread · Grip of Kulemak"),
 dict(stage="T1–T10", goal=L("Motoric Implants · Adonia's Ego · Darkness Enthroned", "Motoric Implants · Adonia's Ego · Darkness Enthroned"), gear=L("Cajado rare + Adonia's Ego", "Rare quarterstaff + Adonia's Ego")),
 dict(stage="T11–T15", goal=L("Amuleto +4 Melee · Sacred Flame · Spirit 100", "+4 Melee amulet · Sacred Flame · 100 Spirit"), gear="Sacred Flame"),
 dict(stage="Pinnacle", goal=L("Diamantes e Kalandra's Touch", "Diamonds and Kalandra's Touch"), gear=L("Diamantes corruptos", "Corrupted Diamonds")),
]

CRAFT = [
 L("Cajado a cada salto (16, 33, 59): base branca do vendor → Transmutation + Augmentation até sair + dano físico/elétrico ou velocidade → Regal → Exalted para completar.", "Quarterstaff at each jump (16, 33, 59): white vendor base → Transmutation + Augmentation until you get + physical/lightning damage or speed → Regal → Exalted to fill."),
 L("Body e botas são unique: não craft. Gastar currency em cajado, amuleto (níveis de Melee, Spirit) e luvas (dano adicionado).", "Body and boots are uniques: don't craft. Spend currency on the quarterstaff, amulet (Melee levels, Spirit) and gloves (added damage)."),
 L("Gemcutter's Prism na Falling Thunder e no Charged Staff: cada 1% de qualidade vira efeito com Advanced Thaumaturgy.", "Gemcutter's Prism on Falling Thunder and Charged Staff: each 1% quality becomes an effect with Advanced Thaumaturgy."),
]
CASES = [
 (L("Já tenho o Adonia's Ego mas não tenho cargas", "I have Adonia's Ego but no charges"), L("O Power Siphon gera 1 carga ao matar um inimigo em Cull. Use em elite fraco. Mas a fonte real é o Redflare Conduit.", "Power Siphon grants 1 charge when it kills a Cull-range enemy. Use it on a weakened elite. But the real source is Redflare Conduit.")),
 (L("Não tenho o Redflare Conduit ainda", "I don't have Redflare Conduit yet"), L("Até o nível 33 use o charm Breath of the Mountains e o Power Siphon; o Falling Thunder também funciona sem cargas, com menos dano.", "Until level 33 use the Breath of the Mountains charm and Power Siphon; Falling Thunder also works without charges, with less damage.")),
 (L("Ainda não tenho os +2 níveis de Dex", "I don't have the +2 Dex levels yet"), L("Motoric Implants vem no 4º Trial (~nível 75). Antes disso, o dano vem de qualidade e nível de gem.", "Motoric Implants comes at the 4th Trial (~level 75). Before that, damage comes from quality and gem level.")),
]

SOURCES = [
 dict(name=L("poe.ninja — Path of Building do Gemling Legionnaire nível 96", "poe.ninja — Level 96 Gemling Legionnaire Path of Building"), use=L("Build base: árvore, gems, supports, itens, ascendência e stats (192M de DPS no PoB)", "Base build: tree, gems, supports, items, ascendancy and stats (192M DPS in the PoB)"), url=POB_URL),
 dict(name="Path of Building (PoE2) — Gems.lua, Skills", use=L("Descrições das gems, custos de Spirit, tiers e níveis exigidos", "Gem descriptions, Spirit costs, tiers and level requirements"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name="poe.ninja — Economia (Forbidden Rites)", use=L("Preços e níveis dos uniques do leveling", "Prices and levels of the leveling uniques"), url="https://poe.ninja/poe2/economy/forbiddenrites"),
 dict(name=L("Árvore 0.5 (Path of Building)", "0.5 tree (Path of Building)"), use=L("Nós, notables e a ascendência Gemling Legionnaire", "Nodes, notables and the Gemling Legionnaire ascendancy"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
]
FIXES = [
 L("ADAPTAÇÃO da árvore de campanha (A1–Mapas): o PoB só tem o endgame, e o caminho dele a partir da Mercenary até as notables de crítico de cajado é uma fila de 16+ nós de atributo (0% de dano até o nível 30). A campanha aqui usa nós de dano de melee/duas mãos perto do início da Mercenary (kit/treescore.py mede o valor de cada nó para esta build) e leva as notables de carga (Fabled Stag, One with the Storm, The Power Within) no nível em que o guia já tem fonte de carga. O custo é o respec do 79: quase nenhum nó da campanha está na árvore final. O dano por fase é medido na árvore, não no jogo.", "ADAPTATION of the campaign tree (A1–Maps): the PoB is endgame only, and its road from the Mercenary to the quarterstaff-crit notables is a line of 16+ attribute nodes (0% damage until level 30). The campaign here uses melee/two-handed damage nodes near the Mercenary start (kit/treescore.py measures each node's value for this build) and brings the charge notables (Fabled Stag, One with the Storm, The Power Within) at the level where the guide already has a charge source. The cost is the level 79 respec: almost no campaign node is on the final tree. Damage per phase is measured on the tree, not in game."),
 L("NÃO existe um guia de leveling público desta build. A rota 1→100 foi montada a partir do PoB de endgame; os níveis em que cada gem/item aparece seguem os dados do Path of Building e do poe.ninja, e o texto avisa quando é aproximado.", "There is NO public leveling guide for this build. The 1→100 route was built from the endgame PoB; the levels at which each gem/item appears follow Path of Building and poe.ninja data, and the text says when it's approximate."),
 L("O PoB inclui várias gems de nível 9 que não são a rotação (Spark, Arc, Frost Darts, Orb of Storms, Incinerate, Frost Wall, Lightning Warp): o PoB não explica o papel de cada uma e o guia não as trata como parte do leveling.", "The PoB includes several level 9 gems that are not the rotation (Spark, Arc, Frost Darts, Orb of Storms, Incinerate, Frost Wall, Lightning Warp): the PoB doesn't explain their role and the guide doesn't treat them as part of leveling."),
 L("A ordem dos Trials de ascendência e os níveis 28/40/65/75 são aproximados.", "The order of ascendancy Trials and levels 28/40/65/75 are approximate."),
]

UI = dict(
 setNote=L("rares com + níveis de skill, Spirit e resistência.", "rares with + skill levels, Spirit and resistance."),
 carry=r"^(Falling Thunder|Charged Staff)$", box=L("CARGAS", "CHARGES"), spiritWhat=L("(buffs persistentes)", "(persistent buffs)"),
 mechBtn=L("Abrir Power Charges", "Open Power Charges"), dmg2="Charged Staff", dmgBar=L("Dano do Falling Thunder / Charged Staff (aprox.)", "Falling Thunder / Charged Staff damage (approx.)"),
 dmgLegend=L("dano do Charged Staff (proporção aproximada)", "Charged Staff damage (approximate ratio)"),
 earlyGone=L("As skills iniciais já saíram da barra: você passou do nível {u}.", "Starting skills already left the bar: you're past level {u}."),
 earlyNote=L("Skills de começo; saem no nível ~{u}.", "Early skills; they leave around level {u}."),
 treeIntro=L("Atos 1–Mapas: árvore de campanha montada aqui (ADAPTAÇÃO: o PoB do poe.ninja é só o endgame e o caminho dele até o crítico de cajado é uma fila de atributos). Dano de melee perto do início da Mercenary; Fabled Stag no Ato 4; One with the Storm, The Power Within e Martial Artistry nos Mapas. Endgame: respec para a árvore exata do PoB, com a joia Split Personality.", "Acts 1–Maps: a campaign tree built here (ADAPTATION: the poe.ninja PoB is endgame only and its road to quarterstaff crit is a line of attributes). Melee damage near the Mercenary start; Fabled Stag in Act 4; One with the Storm, The Power Within and Martial Artistry in Maps. Endgame: respec into the PoB's exact tree, with the Split Personality jewel."),
 set1=L("sem pontos separados nesta build", "no separate points in this build"), set2=L("idem", "same"), asc="Gemling Legionnaire", cls="Mercenary",
 respecTip=L("Compare com a fase anterior: nós sem contorno verde já eram seus. A árvore inteira tem dezenas de +5 Atributo: pegue-os no ritmo das gems.", "Compare with the previous phase: nodes without a green outline were already yours. The whole tree has dozens of +5 Attribute nodes: take them at the pace of your gems."),
 routeIntro=L("Sete fases do nível 1 ao 100. O ponto de virada é o nível 33 (Redflare Conduit + Powertread); o dano final vem de Motoric Implants (~75) e da Adonia's Ego (78).", "Seven phases from level 1 to 100. The turning point is level 33 (Redflare Conduit + Powertread); final damage comes from Motoric Implants (~75) and Adonia's Ego (78)."),
 socketPrio=["Falling Thunder", "Charged Staff", "Herald of Thunder", "Wind Dancer", "Charge Regulation"],
 permIntro=L("Nada disso volta depois. Spirit paga Herald, Wind Dancer e Charge Regulation. As quests que dão Spirit e passivas valem em cada personagem.", "None of this comes back later. Spirit pays for Herald, Wind Dancer and Charge Regulation. The quests that give Spirit and passives are per character."),
 atlasCards=[[L("Mapas que atrapalham", "Maps that hurt"), L("Evite mapas que tiram Power Charges ou dão less Recovery (a build depende de carga).", "Avoid maps that remove Power Charges or give less Recovery (the build depends on charges).")],
             [L("Farm", "Farming"), L("A partir do T1 guarde bases de cajado ilvl 82; no T15 confira Amuleto com +4 Melee.", "From T1 keep ilvl 82 quarterstaff bases; at T15 check for a +4 Melee amulet.")]],
 foot=L("Guia baseado no PoB do poe.ninja, dados de jogo do Path of Building e preços do poe.ninja", "Guide based on the poe.ninja PoB, Path of Building game data and poe.ninja prices"),
)

CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens e Árvore se adaptam na hora ao seu Spirit e ao que você marcou. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items and Tree tabs adapt instantly to your Spirit and what you ticked. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit máximo", "Max Spirit"), L("ex.: 90", "e.g. 90")], ["life", L("Vida máxima", "Max life"), ""], ["charges", L("Cargas máximas", "Max charges"), L("ex.: 4", "e.g. 4")]],
 tiles=[[L("Spirit reservado", "Spirit reserved"), "used"], [L("Spirit livre", "Spirit free"), "free"], [L("Cargas máximas", "Max charges"), "armour"]],
 halve="", halveLabel="", halveTip="",
 buffs=[dict(key="herald", name="Herald of Thunder", cost=30), dict(key="wind", name="Wind Dancer", cost=30), dict(key="reg", name="Charge Regulation", cost=30), dict(key="rage", name="Eternal Rage", cost=100)],
 own=[
  ["gear", "breath", "Breath of the Mountains"], ["gear", "Redflare Conduit", "Redflare Conduit"], ["gear", "Powertread", "Powertread"], ["gear", "Grip of Kulemak", "Grip of Kulemak"],
  ["gear", "Darkness Enthroned", "Darkness Enthroned"], ["gear", "Adonia's Ego", "Adonia's Ego"], ["gear", "Sacred Flame", "Sacred Flame"],
  ["gem", "herald", "Herald of Thunder (30)"], ["gem", "wind", "Wind Dancer (30)"], ["gem", "reg", "Charge Regulation (30)"], ["gem", "rage", "Eternal Rage (100)"], ["gem", "cs", "Charged Staff"],
  ["tree", "stag", "The Fabled Stag"], ["tree", "power", "The Power Within"], ["tree", "storm", "One with the Storm"], ["tree", "overflow", "Overflowing Power"],
  ["asc", "eov", "Essence of Virtue"], ["asc", "at", "Advanced Thaumaturgy"], ["asc", "ig", "Implanted Gems"], ["asc", "mi", "Motoric Implants"],
 ],
 rules=[
  dict(when=dict(lvMin=33, notOwn=["Redflare Conduit"]), lvl="bad", t=L("Falta o Redflare Conduit", "Redflare Conduit missing"), d=L("É a sua fonte de Power Charges. Nível 33, custa quase nada.", "It's your Power Charge source. Level 33, costs almost nothing."), tab="gear"),
  dict(when=dict(lvMin=33, notOwn=["Powertread"]), lvl="warn", t=L("Powertread", "Powertread"), d=L("+1 carga máxima e velocidade de movimento, nível 33.", "+1 maximum charge and movement speed, level 33."), tab="gear"),
  dict(when=dict(lvMin=46, notOwn=["stag"]), lvl="warn", t=L("The Fabled Stag não pego", "The Fabled Stag not taken"), d=L("Cargas duram mais e podem não ser gastas.", "Charges last longer and may not be spent."), tab="arvore"),
  dict(when=dict(lvMin=65, notOwn=["storm"]), lvl="warn", t=L("One with the Storm não pego", "One with the Storm not taken"), d=L("O Falling Thunder consome uma carga a mais: 1 projétil a mais por carga.", "Falling Thunder consumes an extra charge: one more projectile per charge."), tab="arvore"),
  dict(when=dict(lvMin=32, notOwn=["cs"]), lvl="tip", t=L("Charged Staff", "Charged Staff"), d=L("Uncut Skill Gem nível 9: dano de raio e onda de choque nos golpes.", "Level 9 Uncut Skill Gem: lightning damage and shockwave on hits."), tab="skills"),
  dict(when=dict(lvMin=40, notOwn=["at"]), lvl="warn", t=L("Advanced Thaumaturgy", "Advanced Thaumaturgy"), d=L("Qualidade vira efeito extra. Faça o 2º Trial.", "Quality becomes an extra effect. Do the 2nd Trial."), tab="asc"),
  dict(when=dict(lvMin=75, notOwn=["mi"]), lvl="bad", t=L("Motoric Implants", "Motoric Implants"), d=L("+2 níveis nas skills que exigem Dex: o maior salto de dano da ascendência.", "+2 levels on skills with a Dex requirement: the ascendancy's biggest damage jump."), tab="asc"),
  dict(when=dict(lvMin=78, notOwn=["Adonia's Ego"]), lvl="warn", t=L("Adonia's Ego", "Adonia's Ego"), d=L("Wand para Power Siphon e Pinnacle of Power (~0,1 Divine).", "Wand for Power Siphon and Pinnacle of Power (~0.1 Divine)."), tab="gear"),
  dict(when=dict(own=["rage"], notOwn=["Sacred Flame"]), lvl="bad", t=L("Eternal Rage sem Sacred Flame", "Eternal Rage without Sacred Flame"), d=L("São 100 Spirit; sem o sceptre não cabe.", "That's 100 Spirit; it doesn't fit without the sceptre."), tab="gear"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["maps", "endgame", "max"], when=dict(notOwn=["Adonia's Ego"]), gemsFrom="a4", note=L("Sem Adonia's Ego: mostrando o setup do Ato 4.", "No Adonia's Ego: showing the Act 4 setup.")),
]
TREE_RULES = [
 dict(when=dict(lvMin=46, notOwn=["stag"]), t=L("Pegue The Fabled Stag: cargas duram mais.", "Take The Fabled Stag: charges last longer."), node="The Fabled Stag"),
 dict(when=dict(lvMin=65, notOwn=["storm"]), t=L("One with the Storm: 1 projétil a mais por carga.", "One with the Storm: 1 more projectile per charge."), node="One with the Storm"),
 dict(when=dict(lvMin=79, notOwn=["overflow"]), t=L("Overflowing Power: +2 cargas máximas (com a árvore do PoB).", "Overflowing Power: +2 maximum charges."), node="Overflowing Power"),
]
TIMING_KEY = {"Redflare Conduit": "Redflare Conduit", "Powertread": "Powertread", "Adonia's Ego": "Adonia's Ego", "Sacred Flame": "Sacred Flame", "Charge Regulation": "reg", "Herald of Thunder": "herald", "Wind Dancer": "wind",
              "Eternal Rage": "rage", "Advanced Thaumaturgy": "at", "Motoric Implants": "mi", "Charged Staff": "cs"}

T("item", "Redflare Conduit", 33, L("Nível 33, vendor ou drop; barato", "Level 33, vendor or drop; cheap"), L("Ato 3.", "Act 3."), L("A fonte contínua de Power Charges.", "The continuous Power Charge source."), L("Até lá use o charm Breath of the Mountains.", "Until then use the Breath of the Mountains charm."), L("Sem ele a build não vira.", "Without it the build doesn't turn on."), [L("Compre o normal (nível 33) e troque pelo Runemastered (55).", "Buy the normal one (level 33) and swap to the Runemastered (55).")])
T("item", "Powertread", 33, L("Nível 33; barato", "Level 33; cheap"), L("Ato 3.", "Act 3."), L("+1 carga máxima e velocidade de movimento.", "+1 maximum charge and movement speed."), L("Use botas com velocidade até lá.", "Use boots with movement speed until then."), "—")
T("item", "Adonia's Ego", 78, L("Nível 78; ~0,1 Divine", "Level 78; ~0.1 Divine"), L("Mapas.", "Maps."), L("Power Siphon e Pinnacle of Power.", "Power Siphon and Pinnacle of Power."), L("Não compre antes: o nível trava.", "Don't buy early: the level locks it."), "—")
T("item", "Sacred Flame", 84, L("Nível 84; ~5 Divines", "Level 84; ~5 Divines"), "T15", L("+100 Spirit e Purity of Fire.", "+100 Spirit and Purity of Fire."), "—", "—")
T("skill", "Charged Staff", 32, L("Uncut Skill Gem nível 9", "Level 9 Uncut Skill Gem"), L("Ato 3.", "Act 3."), L("Dano de raio e onda de choque nos golpes de cajado.", "Lightning damage and shockwave on quarterstaff hits."), L("Sem cargas ele não faz nada.", "Without charges it does nothing."), "—")
T("skill", "Herald of Thunder", 34, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Ato 3.", "Act 3."), L("Raios ao matar inimigos em Shock.", "Lightning bolts on killing Shocked enemies."), L("Não ligue sem 30 de Spirit livres.", "Don't turn on without 30 free Spirit."), "—")
T("skill", "Wind Dancer", 52, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Interlúdios.", "Interludes."), L("Defesa com dano em volta ao ser atingido.", "Defence with area damage when hit."), "—", "—")
T("skill", "Charge Regulation", 52, L("Tier 14, 30 Spirit", "Tier 14, 30 Spirit"), L("Interlúdios.", "Interludes."), L("Buffs fortes por carga ativa.", "Powerful buffs per active charge."), "—", "—")
T("asc", "Advanced Thaumaturgy", 40, L("2º Trial", "2nd Trial"), L("Ato 3.", "Act 3."), L("Qualidade vira efeito extra.", "Quality becomes an extra effect."), "—", "—")
T("asc", "Motoric Implants", 75, L("4º Trial", "4th Trial"), L("Mapas.", "Maps."), L("+2 níveis em skills de Dex.", "+2 levels on Dex skills."), "—", "—")

MECH = dict(
 title=L("Power Charges", "Power Charges"),
 intro=L("Tudo na build gira em torno de uma coisa: Power Charges. Aqui está o ciclo — de onde elas vêm, como o Falling Thunder as gasta e o que faz uma carga render mais.", "Everything in the build revolves around one thing: Power Charges. Here's the cycle — where they come from, how Falling Thunder spends them and what makes a charge go further."),
 sections=[
  dict(type="cards", cards=[
   [L("1. De onde vêm", "1. Where they come from"), L("Redflare Conduit: 20% de chance de ganhar uma carga ao acertar. Powertread, Grip of Kulemak, Adonia's Ego e The Power Within somam +1 de máximo cada; Overflowing Power e um capacete rare, +2 cada. O Power Siphon (Adonia's Ego) dá 1 carga ao matar um inimigo em Cull.", "Redflare Conduit: a 20% chance to gain a charge on hit. Powertread, Grip of Kulemak, Adonia's Ego and The Power Within add +1 maximum each; Overflowing Power and a rare helmet, +2 each. Power Siphon (Adonia's Ego) grants 1 charge when it kills a Cull-range enemy.")],
   [L("2. Como são gastas", "2. How they're spent"), L("Falling Thunder: consome as cargas para soltar um projétil de raio por carga (e One with the Storm faz cada carga contar como duas). Charged Staff: consome todas para carregar o cajado. Pinnacle of Power: só com cargas no máximo, consome todas e dá maestria elemental.", "Falling Thunder: consumes charges to fire one lightning projectile per charge (and One with the Storm makes each count as two). Charged Staff: consumes all to charge the staff. Pinnacle of Power: only at max charges, consumes them all and grants elemental mastery.")],
   [L("3. Como render mais", "3. How to make them go further"), L("Perpetual Charge (chance de não remover a carga), Heightened Charges (chance de dobrar o benefício), The Fabled Stag (cargas duram +40% e +10% de chance de não gastar) e Charge Regulation (buffs por carga, mas consome cargas de tempos em tempos).", "Perpetual Charge (chance not to remove the charge), Heightened Charges (chance to double the benefit), The Fabled Stag (charges last +40% and +10% chance not to spend) and Charge Regulation (buffs per charge, but consumes charges every so often).")],
   [L("4. O preço", "4. The price"), L("Redflare Conduit perde todas as cargas ao chegar no máximo e te choca. Adonia's Ego tira 10% de resistências elementais por carga. Por isso Strong Hearted e resistência sobrando importam.", "Redflare Conduit loses all charges at maximum and Shocks you. Adonia's Ego takes 10% elemental resistances per charge. That's why Strong Hearted and spare resistance matter.")],
  ]),
  dict(type="rotation", blocks=[
   [L("Boss", "Boss"), [L("Herald, Wind Dancer e Charge Regulation ligados", "Herald, Wind Dancer and Charge Regulation on"), L("Elemental Weakness na frente", "Elemental Weakness first"), L("Pinnacle of Power quando as cargas estiverem no máximo", "Pinnacle of Power when charges are at max"), L("Charged Staff e depois Falling Thunder, de perto", "Charged Staff, then Falling Thunder up close")]],
   [L("Clear", "Clear"), [L("Falling Thunder no meio do pack", "Falling Thunder in the middle of the pack"), L("O Redflare Conduit repõe as cargas", "Redflare Conduit refills the charges"), L("Charged Staff quando encher", "Charged Staff when it fills")]],
  ]),
  dict(type="table", h=L("Weapon sets", "Weapon sets"), cols=[L("Fase", "Phase"), "Weapon Set 1", "Weapon Set 2"], rows=[
   [L("Atos 1–4", "Acts 1–4"), L("Cajado + tudo", "Quarterstaff + everything"), L("Vazio", "Empty")],
   [L("Mapas 65+", "Maps 65+"), L("Cajado: Falling Thunder e Charged Staff", "Quarterstaff: Falling Thunder and Charged Staff"), "Adonia's Ego: Power Siphon + Pinnacle of Power"],
   ["T15+", L("Cajado com +3 níveis de Attack", "Quarterstaff with +3 Attack levels"), "Adonia's Ego + Sacred Flame"],
  ]),
  dict(type="spirit", h=L("Spirit dos buffs", "Buff Spirit"), p=L("Marque o que você usa. Custos do Path of Building.", "Tick what you use. Costs from Path of Building."),
       note=L("Ordem: Herald → Wind Dancer → Charge Regulation → Eternal Rage. Se faltar, desligue o último.", "Order: Herald → Wind Dancer → Charge Regulation → Eternal Rage. If short, turn off the last one.")),
  dict(type="timeline", h=L("Peças-chave por nível", "Key pieces by level"), items=[
   dict(lv=5, t="Breath of the Mountains", d=L("1 Power Charge ao usar.", "1 Power Charge on use.")),
   dict(lv=33, t="Redflare Conduit + Powertread", d=L("As cargas passam a vir sozinhas.", "Charges start coming on their own.")),
   dict(lv=75, t="Motoric Implants", d=L("+2 níveis nas skills de Dex.", "+2 levels on Dex skills.")),
   dict(lv=78, t="Adonia's Ego", d=L("Power Siphon e Pinnacle of Power.", "Power Siphon and Pinnacle of Power.")),
   dict(lv=84, t="Sacred Flame", d=L("+100 Spirit.", "+100 Spirit.")),
  ]),
 ],
)

exec(open(os.path.join(HERE, "bcraft.py"), encoding="utf-8").read())


def build(QUESTS_PT):
    quests = []
    for q in QUESTS_PT:
        q = dict(q)
        if q["boss"] == "Mighty Silverfist":       # o alvo do Tame é do Silverfist; aqui só valem os pontos de Weapon Set
            q["reward"] = "2 Weapon Set Passive Points"; q["prio"] = "Média"
        if q["boss"] == "Tribal Medicine":         # a escolha de Deflection é do Silverfist: a build não usa Deflection
            q["reward"] = L("ESCOLHA: qualquer uma (a build não depende dela)", "CHOICE: any (the build doesn't depend on it)"); q["prio"] = "Média"
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="19/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=GUIDE_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=BOOK.TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None,
                ui=UI, char=CHAR, mech=MECH, adaptSwaps=ADAPT_SWAPS, treeRules=TREE_RULES, timingKey=TIMING_KEY, phaseAct=PHASE_ACT, treeOrder=ORDER + ["uber"], craftKit=CRAFT_KIT)
