# -*- coding: utf-8 -*-
"""Mercenary · Gemling Legionnaire: Twister + Whirling Slash (spear, crítico e elementos).

Fonte: PoB do Maxroll (https://maxroll.gg/poe2/pob/834d3y0q, "Spear Throw Twister Gemling Legionnaire", nível 100). O PoB é só o ENDGAME: não há guia nem leveling do autor.
O leveling deste guia é uma ADAPTAÇÃO: as skills do endgame (Whirling Slash e Twister na spear) entram no nível 1; a árvore da campanha é a do PoB numa ordem 'dano primeiro' com um pequeno
desvio pelos nós de dano de projétil perto do início da Mercenary (que saem no respec do 79); os itens seguem o ranking por nível (gear_opts.py). Descrições e tiers das gems vêm do
Path of Building (Gems.lua e skills_*.lua), níveis e preços dos uniques do poe.ninja; o texto diz quando é aproximado."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("twister")

GUIDE_URL = "https://maxroll.gg/poe2/pob/834d3y0q"
POB_URL = "https://maxroll.gg/poe2/pob/834d3y0q"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "19/09/2026"

CONFIG = dict(dir="twister", build="twister", store="twister1", emoji="🌪", pill="Mercenary · Gemling Legionnaire",
              fonts="family=Cinzel:wght@500;700;900&family=Oxanium:wght@500;600;700&family=Exo+2:ital,wght@0,400;0,500;0,600;1,400")
TXT = {
 "pt": dict(TITLE="Tornado da Lança", DESC="Guia interativo Mercenary Gemling Legionnaire Twister + Whirling Slash (spear, crítico e elementos, do nível 1 ao 100) — PoE 2 Forbidden Rites",
            H1S="Twister e Whirling Slash na spear desde o nível 1 · o redemoinho vira tornado · crítico e elementos", H1="O Tornado da Lança",
            LEAD="A Whirling Slash levanta um redemoinho; o Twister encosta nele, consome e cria tornados extras. São duas skills de spear do nível 1 ao 100. Diga seu nível e o que você já tem, e o guia mostra o que fazer agora, gema por gema, item por item, até o Twister de endgame."),
 "en": dict(TITLE="Spear Twister", DESC="Interactive Mercenary Gemling Legionnaire Twister + Whirling Slash guide (spear, crit and elements, level 1 to 100) — PoE 2 Forbidden Rites",
            H1S="Twister and Whirling Slash on the spear from level 1 · the whirlwind becomes a tornado · crit and elements", H1="The Spear Twister",
            LEAD="Whirling Slash kicks up a whirlwind; Twister touches it, consumes it and spawns extra tornadoes. Two spear skills from level 1 to 100. Tell it your level and what you already have, and the guide shows what to do now, gem by gem, item by item, up to the endgame Twister."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["mech", "Redemoinho & Cargas", "Whirlwind & Charges"], ["rota", "Rota 1→100", "Route 1→100"],
        ["skills", "Skills & Supports", "Skills & Supports"], ["gear", "Itens", "Items"], ["uniques", "Uniques", "Uniques"], ["arvore", "Árvore de Passivas", "Passive Tree"],
        ["asc", "Ascendência", "Ascendancy"], ["quests", "Quests", "Quests"], ["tricks", "Truques", "Tricks"], ["diag", "Diagnóstico", "Troubleshooting"], ["fontes", "Fontes", "Sources"]]

CLASS, ASC, START = "Mercenary", "Gemling Legionnaire", 50986
ORDER = ["a1", "a2", "a3", "a4", "maps", "endgame", "max"]
VMAP = {"a1": "A1", "a2": "A2", "a3": "A3", "a4": "A4", "maps": "Mapas", "endgame": "Endgame", "max": "Aspiracional"}
FULLMAP = {k: k for k in ORDER}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a3", "maps": "a4", "endgame": "maps", "max": "endgame"}
PHASE_ACT = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "maps": 6, "endgame": 6, "max": 6}
ITEM_NOTE = {}


HINT_SPEAR = L("Soul Core de velocidade ou runa de dano elemental na spear (Thrud's Might no PoB)", "A speed Soul Core or elemental damage rune on the spear (the PoB's Thrud's Might)")
HINT_RES = L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio)", "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning)")


def socket_hint(slot, name):
    if "Spear" in name or "Edge" in name or "Skysliver" in name:
        return [HINT_SPEAR]
    if slot in ("Body Armour", L("Capacete", "Helmet"), L("Luvas", "Gloves"), L("Botas", "Boots")):
        return [HINT_RES]
    return None


SP30 = L("30 Spirit", "30 Spirit")

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

SUPWHY.update({
 "Rage I": L("A Whirling Slash (melee) gera Rage a cada golpe: a Rage vira dano.", "Whirling Slash (melee) generates Rage on every hit: Rage becomes damage."),
 "Rage II": L("Versão melhor do Rage I.", "Better Rage I."),
 "Magnified Area I": L("Área maior: o Whirlwind da Whirling Slash e as explosões pegam mais inimigos.", "Bigger area: Whirling Slash's Whirlwind and the explosions reach more enemies."),
 "Projectile Acceleration I": L("Projéteis mais rápidos: o Twister cobre mais chão e chega antes ao Whirlwind.", "Faster projectiles: Twister covers more ground and reaches the Whirlwind sooner."),
 "Projectile Acceleration II": L("Versão melhor (tier 4).", "Better version (tier 4)."),
 "Projectile Acceleration III": L("Versão final (tier 5).", "Final version (tier 5)."),
 "Execute I": L("Mais dano contra inimigos com pouca vida: acaba o pack e o boss no fim.", "More damage against enemies on Low Life: finishes packs and the boss at the end."),
 "Execute II": L("Versão melhor (tier 4).", "Better version (tier 4)."),
 "Execute III": L("Versão final (tier 5).", "Final version (tier 5)."),
 "Pinpoint Critical": L("Crítica com mais frequência (mas com menos dano por crítico): a árvore do PoB é de crítico.", "Crits more often (but with less damage per crit): the PoB's tree is crit-based."),
 "Blazing Critical": L("Um crítico deixa TODOS os seus ataques com dano de fogo por um tempo (o Twister aproveita).", "A crit imbues ALL your Attacks with fire damage for a while (Twister benefits)."),
 "Verglas": L("Ao destruir Ice Crystals (Frost Wall) você ganha dano de frio extra nas skills apoiadas.", "Destroying Ice Crystals (Frost Wall) gives supported skills extra cold damage."),
 "Embitter": L("Todo dano 'ganho como extra' vira dano ganho como frio extra: casa com o Sacred Flame e o Mind Edge.", "All 'gained as extra' damage becomes gained as extra cold: pairs with Sacred Flame and Mind Edge."),
 "Perpetual Charge": L("Chance de NÃO gastar cada Frenzy Charge que o Barrage consome (e ainda ganhar o efeito).", "Chance not to spend each Frenzy Charge Barrage consumes (and still get the effect)."),
 "Heightened Charges": L("Chance de o efeito de gastar cargas valer em dobro: mais repetições do Twister.", "Chance for the effect of consuming charges to be doubled: more Twister repeats."),
 "Charge Profusion I": L("Chance de gerar uma carga a mais quando gera Frenzy Charge.", "Chance to generate an additional charge when you generate a Frenzy Charge."),
 "Charge Profusion II": L("Versão melhor: mais cargas para o Barrage.", "Better version: more charges for Barrage."),
 "Armour Break III": L("Quebra a Armour do inimigo com o golpe: alimenta o Armour Explosion.", "Breaks the enemy's Armour on hit: feeds Armour Explosion."),
 "Armour Demolisher II": L("O Armour Break que você aplica fica mais forte.", "The Armour Break you apply is stronger."),
 "Ambush": L("Mais chance de crítico contra inimigos com a vida cheia (o começo de cada pack).", "More crit chance against full-life enemies (the start of every pack)."),
 "Direstrike I": L("Mais dano de ataque enquanto você está com pouca vida, com a skill de buff ligada.", "More attack damage while on Low Life, with the buff skill active."),
 "Direstrike II": L("Versão melhor (tier 4).", "Better version (tier 4)."),
 "Empowered Sparks I": L("Ao gerar Frenzy Charge (Combat Frenzy) solta Sparks de raio.", "Generating a Frenzy Charge (Combat Frenzy) releases lightning Sparks."),
 "Boundless Energy II": L("Meta skills geram Energy bem mais rápido: a Cast on Critical solta a Frost Wall com menos críticos.", "Meta skills generate Energy much faster: Cast on Critical releases Frost Wall on fewer crits."),
 "Fire Mastery": L("+1 nível em skills de fogo (Trinity).", "+1 level on fire skills (Trinity)."),
})

# ------------------------------------------------------------------ fases
PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Whirling Slash + Twister", "Whirling Slash + Twister"),
  carry=L("Você: Whirling Slash → Twister (spear, Set 1)", "You: Whirling Slash → Twister (spear, Set 1)"), dmgSplit=[100, 0],
  goal=L("As duas skills do endgame já no nível 1, com uma spear branca do vendor (Hardwood Spear) no Set 1. A Whirling Slash levanta um Whirlwind em volta de você (Desacelera e Cega); o Twister, ao encostar nesse Whirlwind, o consome e cria tornados extras que causam mais dano. Rotação: Whirling Slash quando o pack chega perto, Twister no meio do redemoinho. O Twister é projétil: na árvore você começa por Remorseless e Ricochet (+15% de dano de projétil cada), um desvio pelo início da Mercenary que sai no respec do 79. Depois do King in the Mists (~10, +30 Spirit) entra o Herald of Thunder (nível 12). O Enfolding Dawn (+100 Spirit) deixa ligar os buffs bem mais cedo.",
         "Both endgame skills from level 1, with a white vendor spear (Hardwood Spear) in Set 1. Whirling Slash kicks up a Whirlwind around you (Slows and Blinds); Twister, on touching that Whirlwind, consumes it and spawns extra tornadoes that deal more damage. Rotation: Whirling Slash when the pack gets close, Twister in the middle of the whirlwind. Twister is a projectile: on the tree you start with Remorseless and Ricochet (+15% projectile damage each), a detour near the Mercenary start that leaves at the 79 respec. After King in the Mists (~10, +30 Spirit) Herald of Thunder comes in (level 12). Enfolding Dawn (+100 Spirit) lets you run the buffs much earlier."),
  rotation=[L("Whirling Slash no pack (levanta o Whirlwind, Desacelera e Cega)", "Whirling Slash on the pack (raises the Whirlwind, Slows and Blinds)"), L("Twister dentro do redemoinho: consome o Whirlwind e cria tornados extras", "Twister inside the whirlwind: consumes the Whirlwind and spawns extra tornadoes"), L("Boss: Twister de longe; Whirling Slash para se afastar", "Boss: Twister from range; Whirling Slash to back off")],
  gems=[
   G("Whirling Slash", ["Rage I", "Magnified Area I"], L("Levantar o Whirlwind", "Raise the Whirlwind"), L("Uncut Skill Gem nível 1 (exige spear): círculo que levanta um Whirlwind, Desacelera e Cega. É o que o Twister consome para se multiplicar.", "Level 1 Uncut Skill Gem (needs a spear): a circular slash that kicks up a Whirlwind, Slows and Blinds. It's what Twister consumes to multiply."), "free"),
   G("Twister", ["Rapid Attacks I", "Projectile Acceleration I", "Execute I"], L("Dano principal", "Main damage"), L("Uncut Skill Gem nível 1 (exige spear): um tornado que avança errático, Cega e Acerta várias vezes; consome o Whirlwind para criar tornados extras. É a sua skill do 1 ao 100.", "Level 1 Uncut Skill Gem (needs a spear): a tornado that moves erratically, Blinds and Hits repeatedly; it consumes the Whirlwind to create extra tornadoes. It's your skill from 1 to 100."), "free"),
   G("Herald of Thunder", ["Magnified Area I"], L("Raios ao matar", "Lightning on kill"), L("Matar inimigos Shockados solta raios que atingem tudo em volta. Uncut Spirit Gem nível 4, 30 Spirit: só depois do King in the Mists (+30 Spirit).", "Killing Shocked enemies releases lightning bolts that hit everything around. Level 4 Uncut Spirit Gem, 30 Spirit: only after King in the Mists (+30 Spirit)."), "core", 1, SP30, since=12),
  ],
  cheap=["Enfolding Dawn", "Blackheart", "Meginord's Girdle"],
  full=["Enfolding Dawn", "Blackheart", "Meginord's Girdle"],
  stats=[L("Vida", "Life"), L("Resistência a fogo/frio/raio", "Fire/cold/lightning resistance"), L("Velocidade de ataque", "Attack speed")],
  tree=L("Os primeiros 17 pontos: Remorseless e Ricochet (+15% de dano de projétil cada) perto do início da Mercenary. São +96% de dano de árvore contra +8% se você seguisse só o caminho do PoB; esses nós saem no respec do 79.", "The first 17 points: Remorseless and Ricochet (+15% projectile damage each) near the Mercenary start. That's +96% tree damage against +8% if you followed only the PoB path; these nodes leave at the 79 respec."),
  avoid=[L("Ficar sem spear no Set 1: as duas skills exigem spear", "Having no spear in Set 1: both skills need a spear"), L("Gastar currency em item que sobe de nível logo", "Spending currency on an item you'll outlevel soon")],
  exit=[L("King in the Mists (~10): +30 Spirit → Herald of Thunder", "King in the Mists (~10): +30 Spirit → Herald of Thunder"), L("Nível 11: Wanderlust (botas) · Nível 16: Skysliver e Barrage", "Level 11: Wanderlust (boots) · Level 16: Skysliver and Barrage")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 31], tag=L("Skysliver, Barrage e as Frenzy Charges", "Skysliver, Barrage and Frenzy Charges"),
  carry=L("Você: Whirling Slash → Twister (Barrage no boss)", "You: Whirling Slash → Twister (Barrage on bosses)"), dmgSplit=[100, 0],
  goal=L("No 16 a spear vira a Skysliver (Winged Spear, ~0,1 Divine: dano de raio) e cai o Barrage (Uncut nível 5): ele prepara o PRÓXIMO Twister para se repetir várias vezes e gasta Frenzy Charges para repetir ainda mais. As cargas vêm do Sniper's Mark (Uncut nível 7, ~24): um crítico no alvo marcado dá uma Frenzy Charge. Rotação de boss: Sniper's Mark → Barrage → Twister. O Infernal Cry (Warcry) reforça os próximos ataques melee, isto é, a Whirling Slash. 1º Trial (~28): Essence of Virtue. Herald of Thunder segue ligado.",
         "At 16 the spear becomes Skysliver (Winged Spear, ~0.1 Divine: lightning damage) and Barrage drops (Level 5 Uncut): it readies the NEXT Twister to repeat several times and spends Frenzy Charges to repeat even more. The charges come from Sniper's Mark (Level 7 Uncut, ~24): a crit on the marked target gives a Frenzy Charge. Boss rotation: Sniper's Mark → Barrage → Twister. Infernal Cry (Warcry) empowers your next melee attacks, i.e. Whirling Slash. 1st Trial (~28): Essence of Virtue. Herald of Thunder stays on."),
  rotation=[L("Whirling Slash no pack, depois Twister no redemoinho", "Whirling Slash on the pack, then Twister in the whirlwind"), L("Boss: Sniper's Mark → Barrage → Twister repetido", "Boss: Sniper's Mark → Barrage → repeated Twister"), L("Infernal Cry antes de entrar no pack", "Infernal Cry before entering the pack")],
  gems=[
   G("Whirling Slash", ["Rage II", "Magnified Area II", "Rapid Attacks II"], L("Levantar o Whirlwind", "Raise the Whirlwind"), L("Suportes melhores (tier 3 e 4).", "Better supports (tier 3 and 4)."), "free"),
   G("Twister", ["Rapid Attacks II", "Projectile Acceleration II", "Execute II", "Elemental Armament II"], L("Dano principal", "Main damage"), L("Elemental Armament II: mais dano elemental (o Twister ganha elemento do chão e da spear).", "Elemental Armament II: more elemental damage (Twister gets element from the ground and the spear)."), "free"),
   G("Barrage", ["Perpetual Charge", "Heightened Charges"], L("Repetir o Twister", "Repeat Twister"), L("Prepara o próximo ataque de projétil de spear repetível (o Twister) para se repetir várias vezes; gasta Frenzy Charges para repetir mais. Uncut nível 5.", "Readies your next Repeatable Projectile Spear Attack (Twister) to repeat several times; spends Frenzy Charges to repeat more. Level 5 Uncut."), "free", since=16),
   G("Sniper's Mark", ["Charge Profusion I", "Eternal Mark"], L("Frenzy Charges", "Frenzy Charges"), L("Marca o alvo: o próximo crítico nele causa dano extra e dá uma Frenzy Charge. Uncut nível 7.", "Marks a target: the next crit on it deals extra damage and grants a Frenzy Charge. Level 7 Uncut."), "free", since=24),
   G("Infernal Cry", [], L("Warcry", "Warcry"), L("Reforça os próximos ataques melee (a Whirling Slash) e faz os inimigos explodirem ao morrer. Uncut nível 3.", "Empowers your next melee attacks (Whirling Slash) and makes enemies combust on death. Level 3 Uncut."), "free", since=16),
   G("Herald of Thunder", ["Magnified Area II", "Pinpoint Critical"], L("Raios ao matar", "Lightning on kill"), L("30 Spirit (King in the Mists).", "30 Spirit (King in the Mists)."), "core", 1, SP30),
  ],
  cheap=["Skysliver", "Wanderlust", "Thrillsteel", "The Fall of the Axe"],
  full=["Skysliver", "Wanderlust", "Thrillsteel", "The Fall of the Axe"],
  stats=[L("Vida", "Life"), L("Resistências", "Resistances"), L("Velocidade de ataque", "Attack speed")],
  tree=L("Pontos 18–34: Swift Flight (+15% de velocidade de projétil e +20% de dano físico), Last Stand (só de passagem: o bônus dele exige pouca vida) e o caminho para Javelin. Aqui o dano de árvore sobe de +96% para +260%.", "Points 18–34: Swift Flight (+15% projectile speed and +20% physical damage), Last Stand (just passing through: its bonus needs low life) and the road to Javelin. Tree damage goes from +96% to +260% here."),
  avoid=[L("Ligar o Herald sem ter os 30 Spirit livres", "Turning on Herald without the 30 Spirit free"), L("Usar o Barrage sem Frenzy Charge: ele só repete de verdade com cargas", "Using Barrage without a Frenzy Charge: it only truly repeats with charges")],
  exit=[L("Nível 24: Sniper's Mark (Frenzy Charges)", "Level 24: Sniper's Mark (Frenzy Charges)"), L("1º Trial (~28): Essence of Virtue · Nível 27: Thrillsteel", "1st Trial (~28): Essence of Virtue · Level 27: Thrillsteel")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[32, 45], tag=L("Wind Dancer, Dance with Death e a Skysliver forjada", "Wind Dancer, Dance with Death and the runeforged Skysliver"),
  carry=L("Você: Whirling Slash → Twister (Barrage no boss)", "You: Whirling Slash → Twister (Barrage on bosses)"), dmgSplit=[100, 0],
  goal=L("O Ignagduk (Azak Bog, ~38) dá +30 Spirit e paga o Wind Dancer (Uncut Spirit Gem nível 4): ele acumula stages de Evasion e, quando você leva um golpe, gasta tudo para causar dano e empurrar em volta. No 40 a Skysliver vira Runeforged (mais slots de runa) e o 2º Trial libera o Gem Studded. Na árvore entram Javelin (+40% de dano crítico com Spears), Dance with Death (+25% de velocidade de skill com a spear e a off hand vazia: mantenha o Set 1 sem off hand) e Acceleration.",
         "Ignagduk (Azak Bog, ~38) gives +30 Spirit and pays for Wind Dancer (Level 4 Uncut Spirit Gem): it builds stages of Evasion and, when you're hit, spends them all to deal damage and knock back around you. At 40 Skysliver becomes Runeforged (more rune slots) and the 2nd Trial unlocks Gem Studded. The tree adds Javelin (+40% Critical Damage Bonus with Spears), Dance with Death (+25% skill speed with the spear and an empty off hand: keep Set 1 without an off hand) and Acceleration."),
  rotation=[L("Herald de Thunder e Wind Dancer sempre ligados", "Herald of Thunder and Wind Dancer always on"), L("Whirling Slash no pack, Twister no redemoinho", "Whirling Slash on the pack, Twister in the whirlwind"), L("Boss: Sniper's Mark → Barrage → Twister; Infernal Cry antes", "Boss: Sniper's Mark → Barrage → Twister; Infernal Cry first")],
  gems=[
   G("Whirling Slash", ["Rage II", "Magnified Area II", "Rapid Attacks II"], L("Levantar o Whirlwind", "Raise the Whirlwind"), L("Sem mudança.", "No change."), "free"),
   G("Twister", ["Rapid Attacks II", "Projectile Acceleration II", "Execute II", "Elemental Armament II"], L("Dano principal", "Main damage"), L("Sem mudança.", "No change."), "free"),
   G("Barrage", ["Perpetual Charge", "Heightened Charges"], L("Repetir o Twister", "Repeat Twister"), L("Sem mudança.", "No change."), "free"),
   G("Sniper's Mark", ["Charge Profusion I", "Eternal Mark", "Mark for Death II"], L("Frenzy Charges", "Frenzy Charges"), L("Mark for Death II: o alvo marcado sofre mais dano.", "Mark for Death II: the marked target takes more damage."), "free"),
   G("Infernal Cry", [], L("Warcry", "Warcry"), L("Sem mudança.", "No change."), "free"),
   G("Herald of Thunder", ["Magnified Area II", "Pinpoint Critical"], L("Raios ao matar", "Lightning on kill"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Wind Dancer", ["Magnified Area II"], L("Defesa e empurrão", "Defence and knockback"), L("Acumula stages de Evasion; ao ser atingido gasta todos para causar dano e empurrar. Uncut nível 4, 30 Spirit (Ignagduk).", "Builds Evasion stages; when hit it spends them all to deal damage and knock back. Level 4 Uncut, 30 Spirit (Ignagduk)."), "core", 2, SP30, since=38),
  ],
  cheap=["Skysliver", "Wanderlust", "Thrillsteel", "The Fall of the Axe", "Nascent Hope"],
  full=["Skysliver", "Wanderlust", "Thrillsteel", "The Fall of the Axe", "Nascent Hope"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Velocidade de ataque", "Attack speed"), L("Dano crítico", "Critical damage")],
  tree=L("Pontos 35–50: Javelin (+40% de dano crítico com Spears), Dance with Death (+25% de velocidade de skill) e Acceleration. Dano de árvore +340%, velocidade +41%.", "Points 35–50: Javelin (+40% Critical Damage Bonus with Spears), Dance with Death (+25% skill speed) and Acceleration. Tree damage +340%, speed +41%."),
  avoid=[L("Ligar Herald + Wind Dancer com menos de 60 Spirit", "Turning on Herald + Wind Dancer with less than 60 Spirit"), L("Pôr algo na off hand do Set 1: o Dance with Death exige a off hand vazia", "Putting something in Set 1's off hand: Dance with Death needs it empty")],
  exit=[L("Skysliver Runeforged (40)", "Runeforged Skysliver (40)"), L("Ignagduk: +30 Spirit → Wind Dancer · 2º Trial (~40): Gem Studded", "Ignagduk: +30 Spirit → Wind Dancer · 2nd Trial (~40): Gem Studded")]),

 dict(id="a4", name=L("Ato 4 e Interlúdios", "Act 4 and Interludes"), lv=[46, 64], tag=L("Combat Frenzy e o crítico da árvore", "Combat Frenzy and the tree's crit"),
  carry=L("Você: Whirling Slash → Twister (Barrage no boss)", "You: Whirling Slash → Twister (Barrage on bosses)"), dmgSplit=[100, 0],
  goal=L("O Lythara (Kriar Village, ~62) dá +40 Spirit: com 100 de Spirit você liga o Combat Frenzy (Uncut Spirit Gem nível 8, 30 Spirit), que dá uma Frenzy Charge quando você Congela, Eletrocuta ou Prende um inimigo, e o Barrage passa a ter carga o tempo todo. O Widow's Reign (nível 45) e o Cat O' Nine Tails (nível 55) seguram a vida. A Whirling Slash ganha Blazing Critical: cada crítico imbui seus ataques com fogo. A árvore chega ao crítico: Heartbreaking, Heartstopping, Catalysis (+20% de dano elemental de ataque) e Sand in the Eyes.",
         "Lythara (Kriar Village, ~62) gives +40 Spirit: with 100 Spirit you turn on Combat Frenzy (Level 8 Uncut Spirit Gem, 30 Spirit), which grants a Frenzy Charge when you Freeze, Electrocute or Pin an enemy, and Barrage always has charges. Widow's Reign (level 45) and Cat O' Nine Tails (level 55) hold your life up. Whirling Slash gains Blazing Critical: every crit imbues your attacks with fire. The tree reaches crit: Heartbreaking, Heartstopping, Catalysis (+20% elemental attack damage) and Sand in the Eyes."),
  rotation=[L("Herald, Wind Dancer e Combat Frenzy sempre ligados", "Herald, Wind Dancer and Combat Frenzy always on"), L("Whirling Slash no pack, Twister no redemoinho", "Whirling Slash on the pack, Twister in the whirlwind"), L("Boss: Sniper's Mark → Barrage → Twister; Infernal Cry antes", "Boss: Sniper's Mark → Barrage → Twister; Infernal Cry first")],
  gems=[
   G("Whirling Slash", ["Rage II", "Magnified Area II", "Rapid Attacks II", "Blazing Critical"], L("Levantar o Whirlwind", "Raise the Whirlwind"), L("Blazing Critical: um crítico deixa seus ataques com dano de fogo.", "Blazing Critical: a crit makes your attacks deal fire damage."), "free"),
   G("Twister", ["Rapid Attacks II", "Projectile Acceleration II", "Execute II", "Elemental Armament II"], L("Dano principal", "Main damage"), L("Sem mudança.", "No change."), "free"),
   G("Barrage", ["Perpetual Charge", "Heightened Charges"], L("Repetir o Twister", "Repeat Twister"), L("Sem mudança.", "No change."), "free"),
   G("Sniper's Mark", ["Charge Profusion I", "Eternal Mark", "Mark for Death II"], L("Frenzy Charges", "Frenzy Charges"), L("Sem mudança.", "No change."), "free"),
   G("Infernal Cry", [], L("Warcry", "Warcry"), L("Sem mudança.", "No change."), "free"),
   G("Herald of Thunder", ["Magnified Area II", "Pinpoint Critical"], L("Raios ao matar", "Lightning on kill"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Wind Dancer", ["Magnified Area II"], L("Defesa e empurrão", "Defence and knockback"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Combat Frenzy", ["Charge Profusion I"], L("Frenzy Charges", "Frenzy Charges"), L("Ganha uma Frenzy Charge quando você Congela, Eletrocuta ou Prende um inimigo (a cada poucos segundos). Uncut Spirit Gem nível 8, 30 Spirit (Lythara).", "Grants a Frenzy Charge when you Freeze, Electrocute or Pin an enemy (once every few seconds). Level 8 Uncut Spirit Gem, 30 Spirit (Lythara)."), "core", 3, SP30, since=62),
  ],
  cheap=["Skysliver", "Cat O' Nine Tails", "Widow's Reign", "Nascent Hope"],
  full=["Skysliver", "Cat O' Nine Tails", "Widow's Reign", "Nascent Hope"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Velocidade de ataque", "Attack speed"), L("Chance de crítico", "Critical chance")],
  tree=L("Pontos 51–72: Heartbreaking (+25% de dano crítico), Heartstopping (+20% de chance de crítico), Catalysis (+20% de dano elemental de ataque), Sand in the Eyes (+10% de velocidade de ataque) e Spray and Pray (+50% de dano de ataque andando). Dano de árvore +527%, velocidade +57%.", "Points 51–72: Heartbreaking (+25% Critical Damage Bonus), Heartstopping (+20% Critical Hit Chance), Catalysis (+20% elemental attack damage), Sand in the Eyes (+10% attack speed) and Spray and Pray (+50% attack damage while moving). Tree damage +527%, speed +57%."),
  avoid=[L("Ficar sem Spirit para o Combat Frenzy (precisa dos 100 do Lythara)", "Running short of Spirit for Combat Frenzy (it needs Lythara's 100)"), L("Comprar itens caros antes das resistências fecharem", "Buying expensive items before resistances close")],
  exit=[L("3º Trial (~65): Advanced Thaumaturgy", "3rd Trial (~65): Advanced Thaumaturgy"), L("Nível 65: Morior Invictus fica disponível", "Level 65: Morior Invictus becomes available")]),

 dict(id="maps", name=L("Mapas 65+", "Maps 65+"), lv=[65, 78], tag=L("Herald of Ice, The Taming e Morior Invictus", "Herald of Ice, The Taming and Morior Invictus"),
  carry=L("Você: Whirling Slash → Twister (Barrage no boss)", "You: Whirling Slash → Twister (Barrage on bosses)"), dmgSplit=[100, 0],
  goal=L("A árvore da campanha fecha os 95 pontos (Short Shot, Killer Instinct e mais nós de dano de projétil). O trabalho agora é juntar dinheiro para o respec do 79 e para as peças do endgame: The Taming (anel, nível 42, ~4 Divines: deixa o Twister usar VÁRIAS superfícies elementais ao mesmo tempo), Morior Invictus (nível 65, ~6 Divines) e o Sacred Flame (nível 84, ~5 Divines: Spirit, 60% do dano como fogo extra). Com um amuleto rare de Spirit você liga o Herald of Ice. 4º Trial (~75): Motoric Implants (+2 níveis nas skills de Dex).",
         "The campaign tree closes its 95 points (Short Shot, Killer Instinct and more projectile damage nodes). The job now is saving for the 79 respec and the endgame pieces: The Taming (ring, level 42, ~4 Divines: lets Twister use MULTIPLE elemental ground surfaces at once), Morior Invictus (level 65, ~6 Divines) and Sacred Flame (level 84, ~5 Divines: Spirit, 60% of damage as extra fire). With a rare Spirit amulet you turn on Herald of Ice. 4th Trial (~75): Motoric Implants (+2 levels on Dex skills)."),
  rotation=[L("Buffs sempre ligados", "Buffs always on"), L("Whirling Slash no pack, Twister no redemoinho", "Whirling Slash on the pack, Twister in the whirlwind"), L("Boss: Sniper's Mark → Barrage → Twister; Infernal Cry antes", "Boss: Sniper's Mark → Barrage → Twister; Infernal Cry first")],
  gems=[
   G("Whirling Slash", ["Rage III", "Magnified Area II", "Rapid Attacks III", "Blazing Critical"], L("Levantar o Whirlwind", "Raise the Whirlwind"), L("Rage III e Rapid Attacks III (tier 5).", "Rage III and Rapid Attacks III (tier 5)."), "free"),
   G("Twister", ["Rapid Attacks III", "Projectile Acceleration III", "Execute III", "Elemental Armament II"], L("Dano principal", "Main damage"), L("Versões tier 5 dos suportes.", "Tier 5 versions of the supports."), "free"),
   G("Barrage", ["Perpetual Charge", "Heightened Charges", "Efficiency II"], L("Repetir o Twister", "Repeat Twister"), L("Efficiency II: custo menor.", "Efficiency II: lower cost."), "free"),
   G("Sniper's Mark", ["Charge Profusion II", "Eternal Mark", "Mark for Death II"], L("Frenzy Charges", "Frenzy Charges"), L("Charge Profusion II (tier 5).", "Charge Profusion II (tier 5)."), "free"),
   G("Infernal Cry", [], L("Warcry", "Warcry"), L("Sem mudança.", "No change."), "free"),
   G("Herald of Thunder", ["Magnified Area II", "Pinpoint Critical"], L("Raios ao matar", "Lightning on kill"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Wind Dancer", ["Magnified Area II"], L("Defesa e empurrão", "Defence and knockback"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Combat Frenzy", ["Charge Profusion I"], L("Frenzy Charges", "Frenzy Charges"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Herald of Ice", ["Magnified Area II", "Execute II"], L("Explosão de gelo", "Ice explosion"), L("Matar (Shatter) inimigo Congelado com um ataque solta uma explosão de gelo. Uncut Spirit Gem nível 4, 30 Spirit: precisa de um amuleto rare de Spirit (passa dos 100).", "Killing (Shattering) a Frozen enemy with an attack releases an ice explosion. Level 4 Uncut Spirit Gem, 30 Spirit: needs a rare Spirit amulet (goes past 100)."), "core", 4, SP30, since=70),
  ],
  cheap=["Skysliver", "Cat O' Nine Tails", "The Taming", "Morior Invictus"],
  full=["Skysliver", "The Taming", "Morior Invictus", "Sacred Flame"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Velocidade de ataque", "Attack speed"), L("Chance de crítico", "Critical chance")],
  tree=L("Pontos 73–95: Short Shot (+20% de dano de projétil), Killer Instinct (+40% de dano de ataque com a vida cheia) e mais nós de dano de projétil. Tenfold Attacks, Flow State e Flow Like Water (velocidade) só entram na árvore do PoB. No 79 você faz o respec para a árvore do PoB: os nós de dano de projétil do começo (26 no total) saem.", "Points 73–95: Short Shot (+20% projectile damage), Killer Instinct (+40% attack damage on Full Life) and more projectile damage nodes. Tenfold Attacks, Flow State and Flow Like Water (speed) only come in on the PoB tree. At 79 you respec into the PoB tree: the early projectile damage nodes (26 in total) leave."),
  avoid=[L("Comprar o Morior Invictus antes das resistências", "Buying Morior Invictus before resistances"), L("Ligar o Herald of Ice sem Spirit acima de 100", "Turning on Herald of Ice without Spirit above 100")],
  exit=[L("4º Trial (~75): Motoric Implants", "4th Trial (~75): Motoric Implants"), L("Morior Invictus + The Taming + Sacred Flame para o respec do 79", "Morior Invictus + The Taming + Sacred Flame for the 79 respec")]),

 dict(id="endgame", name=L("Endgame 79+", "Endgame 79+"), lv=[79, 90], tag=L("A árvore do PoB e o Set 2 com Sacred Flame", "The PoB tree and Set 2 with Sacred Flame"),
  carry=L("Você: Whirling Slash → Twister", "You: Whirling Slash → Twister"), dmgSplit=[100, 0],
  goal=L("Respec para a árvore do PoB (as skills não mudam): sai o desvio de projétil do começo e entram Killer Instinct, Javelin, Stimulants e o resto do crítico. Set 1: spear (Armageddon Edge no PoB) com a off hand vazia (Dance with Death). Set 2: uma segunda spear (Mind Edge: raio e fogo adicionados) e o Sacred Flame na off hand (+Spirit, 60% do dano como fogo extra). Com o Spirit do Sacred Flame (138 no PoB) e do amuleto entram Ghost Dance, Charge Regulation e o resto das reservas. As joias (Megalomaniac, From Nothing, Split Personality e as de crítico de spear) estão na aba Árvore.",
         "Respec into the PoB tree (skills don't change): the early projectile detour goes and Killer Instinct, Javelin, Stimulants and the rest of the crit come in. Set 1: spear (the PoB's Armageddon Edge) with an empty off hand (Dance with Death). Set 2: a second spear (Mind Edge: added lightning and fire) and Sacred Flame in the off hand (+Spirit, 60% of damage as extra fire). With Sacred Flame's Spirit (138 in the PoB) and the amulet's, Ghost Dance, Charge Regulation and the rest of the reservations come in. The jewels (Megalomaniac, From Nothing, Split Personality and the spear crit ones) are in the Tree tab."),
  rotation=[L("Whirling Slash no pack, Twister no redemoinho", "Whirling Slash on the pack, Twister in the whirlwind"), L("Boss: Sniper's Mark → Barrage → Twister; Set 2 para o dano de fogo", "Boss: Sniper's Mark → Barrage → Twister; Set 2 for the fire damage"), L("Infernal Cry no pack; Berserk quando a Rage estiver cheia", "Infernal Cry on the pack; Berserk once Rage is full")],
  gems=[
   G("Whirling Slash", ["Rage III", "Magnified Area II", "Rapid Attacks III", "Blazing Critical"], L("Levantar o Whirlwind", "Raise the Whirlwind"), L("O PoB soma Rigwald's Ferocity (Lineage, luxo).", "The PoB adds Rigwald's Ferocity (Lineage, luxury)."), "free"),
   G("Twister", ["Execute III", "Projectile Acceleration III", "Verglas", "Rapid Attacks III"], L("Dano principal", "Main damage"), L("O PoB usa Execute III, Projectile Acceleration III, Verglas e dois Lineage (Rakiata's Flow e Garukhan's Resolve: luxo).", "The PoB uses Execute III, Projectile Acceleration III, Verglas and two Lineage supports (Rakiata's Flow and Garukhan's Resolve: luxury)."), "free"),
   G("Barrage", ["Perpetual Charge", "Heightened Charges", "Efficiency II"], L("Repetir o Twister", "Repeat Twister"), L("Igual ao PoB (sem os Lineage).", "Same as the PoB (without the Lineage supports)."), "free"),
   G("Sniper's Mark", ["Charge Profusion II", "Eternal Mark", "Mark for Death II", "Armour Demolisher II"], L("Frenzy Charges", "Frenzy Charges"), L("Armour Demolisher II: o Armour Break fica mais forte.", "Armour Demolisher II: the Armour Break is stronger."), "free"),
   G("Herald of Ice", ["Execute III", "Magnified Area II", "Armour Break III", "Armour Explosion"], L("Explosão de gelo", "Ice explosion"), L("Armour Break III + Armour Explosion: quebrar Armour vira explosão.", "Armour Break III + Armour Explosion: breaking Armour becomes an explosion."), "core", 1, SP30),
   G("Herald of Thunder", ["Execute III", "Magnified Area II", "Pinpoint Critical", "Embitter", "Freeze"], L("Raios ao matar", "Lightning on kill"), L("Embitter + Freeze: o dano extra vira frio e o Freeze alimenta o Herald of Ice e o Combat Frenzy.", "Embitter + Freeze: the extra damage becomes cold and Freeze feeds Herald of Ice and Combat Frenzy."), "core", 2, SP30),
   G("Wind Dancer", ["Execute III", "Magnified Area II", "Pinpoint Critical", "Ambush", "Blind II"], L("Defesa e empurrão", "Defence and knockback"), L("Os suportes de dano viram o empurrão do Wind Dancer em dano de verdade.", "The damage supports turn Wind Dancer's knockback into real damage."), "core", 3, SP30),
   G("Ghost Dance", ["Cooldown Recovery II", "Armour Demolisher II", "Direstrike II"], L("Defesa", "Defence"), L("Ao ser atingido com um Ghost Shroud, recupera Energy Shield com base na Evasion. Uncut Spirit Gem nível 4, 30 Spirit.", "When hit with a Ghost Shroud, recovers Energy Shield based on Evasion. Level 4 Uncut Spirit Gem, 30 Spirit."), "core", 4, SP30, since=79),
   G("Combat Frenzy", ["Charge Profusion II", "Empowered Sparks I"], L("Frenzy Charges", "Frenzy Charges"), L("Empowered Sparks I solta Sparks ao gerar a carga.", "Empowered Sparks I releases Sparks when the charge is generated."), "core", 5, SP30),
   G("Charge Regulation", ["Direstrike I"], L("Buffs das cargas", "Charge buffs"), L("Buffs fortes conforme as cargas ativas; gasta cargas de tempos em tempos. Uncut Spirit Gem nível 14, 30 Spirit.", "Strong buffs based on your active charges; spends charges every few seconds. Level 14 Uncut Spirit Gem, 30 Spirit."), "core", 6, SP30, since=79),
   G("Infernal Cry", [], L("Warcry", "Warcry"), L("Sem mudança.", "No change."), "free"),
   G("Berserk", [], L("Rage", "Rage"), L("Reforça a Rage que a Whirling Slash gera; drena vida se você para de bater. Tier 14, 30 Spirit.", "Strengthens the Rage Whirling Slash generates; drains life if you stop attacking. Tier 14, 30 Spirit."), "core", 7, SP30, since=79),
   G("Virtuous Barrier", [], L("Defesa", "Defence"), L("Da ascendência (Essence of Virtue): barreira com Motes que se perdem quando você toma dano.", "From the ascendancy (Essence of Virtue): a barrier of Motes that are lost when you're hit."), "free"),
  ],
  cheap=["Skysliver", "Morior Invictus", "The Taming", "Sacred Flame"],
  full=["Skysliver", "Morior Invictus", "The Taming", "Sacred Flame", "Headhunter"],
  stats=[L("Vida, Armour e Evasion", "Life, Armour and Evasion"), L("Velocidade de ataque", "Attack speed"), L("Spirit", "Spirit")],
  tree=L("Respec para a árvore do PoB: 148 nós em volta da região de crítico de spear (Javelin, Heartbreaking, Killer Instinct, Stimulants) + as joias. Nada de nós de projétil do começo.", "Respec into the PoB tree: 148 nodes around the spear crit region (Javelin, Heartbreaking, Killer Instinct, Stimulants) + the jewels. No early projectile nodes."),
  avoid=[L("Fazer o respec antes de ter o Morior Invictus e o Sacred Flame: a árvore do PoB conta com eles", "Respeccing before you have Morior Invictus and Sacred Flame: the PoB tree counts on them"), L("Ligar Berserk sem vida/regeneração", "Turning on Berserk without life/regeneration")],
  exit=[L("Trinity e Cast on Critical (Spirit de amuleto)", "Trinity and Cast on Critical (amulet Spirit)"), L("Headhunter, Rite of Passage e os Lineage", "Headhunter, Rite of Passage and the Lineage supports")]),

 dict(id="max", name=L("Endgame final", "Final endgame"), lv=[91, 100], tag=L("Trinity, Cast on Critical e Lineage", "Trinity, Cast on Critical and Lineage"),
  carry=L("Você: Whirling Slash → Twister", "You: Whirling Slash → Twister"), dmgSplit=[100, 0],
  goal=L("O PoB de endgame do autor (nível 100): Headhunter, Rite of Passage, amuleto que dá Cast on Critical (com Frost Wall, o que alimenta o Verglas do Twister) e Trinity (100 Spirit), mais os suportes de Lineage (Rakiata's Flow, Garukhan's Resolve, Uhtred's Constellation, Olroth's Conviction, Rigwald's Ferocity, Uruk's Smelting): tudo luxo, coloque conforme entrar dinheiro. O Gem Studded exige contar as cores dos suportes: confira o custo de mana.",
         "The author's endgame PoB (level 100): Headhunter, Rite of Passage, an amulet that gives Cast on Critical (with Frost Wall, which feeds Twister's Verglas) and Trinity (100 Spirit), plus the Lineage supports (Rakiata's Flow, Garukhan's Resolve, Uhtred's Constellation, Olroth's Conviction, Rigwald's Ferocity, Uruk's Smelting): all luxury, add them as money comes in. Gem Studded requires counting support colours: check mana costs."),
  rotation=[L("Igual ao Endgame", "Same as Endgame")],
  gems=[
   G("Twister", ["Execute III", "Projectile Acceleration III", "Verglas", "Rapid Attacks III"], L("Dano principal", "Main damage"), L("Com os Lineage do PoB (Rakiata's Flow e Garukhan's Resolve).", "With the PoB's Lineage supports (Rakiata's Flow and Garukhan's Resolve)."), "free"),
   G("Whirling Slash", ["Rage III", "Magnified Area II", "Rapid Attacks III", "Blazing Critical"], L("Levantar o Whirlwind", "Raise the Whirlwind"), L("Com Rigwald's Ferocity (Lineage).", "With Rigwald's Ferocity (Lineage)."), "free"),
   G("Cast on Critical", ["Boundless Energy II", "Cold Mastery"], L("Frost Wall automático", "Automatic Frost Wall"), L("Vem do amuleto (nível 20): ganha Energy nos críticos e dispara a Frost Wall; as Ice Crystals ativam o Verglas. 100 Spirit.", "Comes from the amulet (level 20): gains Energy on crits and triggers Frost Wall; the Ice Crystals activate Verglas. 100 Spirit."), "core", 1, L("100 Spirit", "100 Spirit")),
   G("Trinity", ["Fire Mastery"], L("Elementos", "Elements"), L("Fogo, Gelo e Raio: o dano elemental aumenta com a Afinidade acumulada. Tier 14, 100 Spirit.", "Fire, Cold and Lightning: elemental damage increases with the Affinity you build. Tier 14, 100 Spirit."), "core", 2, L("100 Spirit", "100 Spirit")),
  ],
  cheap=[L("Igual ao Endgame", "Same as Endgame")], full=["Headhunter", "Rite of Passage"],
  stats=[L("Dano", "Damage")], tree=L("A árvore do PoB completa (148 nós + as joias); os 9 nós do fim exigem a joia Split Personality.", "The full PoB tree (148 nodes + the jewels); the last 9 nodes need the Split Personality jewel."),
  avoid=[L("Gastar Divines antes de fechar resistência e Spirit", "Spending Divines before resistances and Spirit are closed")], exit=[]),
]
PH = {p["id"]: p for p in PHASES}
BOX = {
 "a1": ("2", ["Whirling Slash", "Twister"], L("Duas skills de spear no mesmo set: o redemoinho da primeira é o que o Twister consome.", "Two spear skills in the same set: the first one's whirlwind is what Twister consumes.")),
 "a2": ("2", ["Sniper's Mark", "Barrage"], L("O Sniper's Mark dá a carga, o Barrage a gasta para repetir o Twister.", "Sniper's Mark gives the charge, Barrage spends it to repeat Twister.")),
 "a3": ("2", ["Whirling Slash", "Twister"], L("O Set 1 fica sem off hand: Dance with Death.", "Set 1 stays without an off hand: Dance with Death.")),
 "a4": ("2", ["Whirling Slash", "Twister"], L("Três reservas de Spirit (Herald, Wind Dancer, Combat Frenzy) somam 90 dos 100.", "Three Spirit reservations (Herald, Wind Dancer, Combat Frenzy) use 90 of the 100.")),
 "maps": ("2", ["Whirling Slash", "Twister"], L("Sem pressa: o respec do 79 só vale com Morior e Sacred Flame.", "No rush: the 79 respec only pays off with Morior and Sacred Flame.")),
 "endgame": ("2", ["Whirling Slash", "Twister"], L("Set 1 spear; Set 2 spear + Sacred Flame.", "Set 1 spear; Set 2 spear + Sacred Flame.")),
 "max": ("2", ["Whirling Slash", "Twister"], L("Igual, com Cast on Critical, Trinity e Lineage.", "Same, with Cast on Critical, Trinity and Lineage.")),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in {"a1": L("Nenhuma reserva ainda: o Herald of Thunder espera o King in the Mists (+30 Spirit, ~10). O Enfolding Dawn (+100) adianta tudo.", "No reservation yet: Herald of Thunder waits for King in the Mists (+30 Spirit, ~10). Enfolding Dawn (+100) speeds everything up."),
                  "a2": L("Herald (30) de 30 Spirit: sobra o que vier do Ignagduk.", "Herald (30) of 30 Spirit: what's left comes from Ignagduk."),
                  "a3": L("Herald (30) + Wind Dancer (30) = 60 Spirit (King in the Mists + Ignagduk).", "Herald (30) + Wind Dancer (30) = 60 Spirit (King in the Mists + Ignagduk)."),
                  "a4": L("Herald + Wind Dancer + Combat Frenzy = 90 dos 100 Spirit (com o Lythara).", "Herald + Wind Dancer + Combat Frenzy = 90 of 100 Spirit (with Lythara)."),
                  "maps": L("90 de 100 Spirit. O Herald of Ice (mais 30) só cabe com um amuleto rare de Spirit.", "90 of 100 Spirit. Herald of Ice (another 30) only fits with a rare Spirit amulet."),
                  "endgame": L("Sete reservas (210): o Sacred Flame (138 no PoB) e o amuleto (+50) pagam além dos 100 das quests.", "Seven reservations (210): Sacred Flame (138 in the PoB) and the amulet (+50) pay beyond the quests' 100."),
                  "max": L("Cast on Critical (100) e Trinity (100) somam 200 além das reservas do endgame: só com amuleto e Sacred Flame bem rolados.", "Cast on Critical (100) and Trinity (100) add 200 on top of the endgame reservations: only with a well-rolled amulet and Sacred Flame.")}.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Whirling Slash e Twister (Uncut nível 1) com uma spear branca no Set 1. Enfolding Dawn (+100 Spirit) se você conseguir.", "Whirling Slash and Twister (level 1 Uncut) with a white spear in Set 1. Enfolding Dawn (+100 Spirit) if you can get it."),
 4: L("Elemental Armament II nos suportes.", "Elemental Armament II on the supports."),
 10: L("King in the Mists: +30 Spirit.", "King in the Mists: +30 Spirit."),
 11: L("Wanderlust (botas, 20% de movimento).", "Wanderlust (boots, 20% movement)."),
 12: L("Herald of Thunder (Uncut Spirit Gem nível 4, 30 Spirit) e os suportes tier 4 (Rapid Attacks II, Projectile Acceleration II, Execute II).", "Herald of Thunder (Level 4 Uncut Spirit Gem, 30 Spirit) and the tier 4 supports (Rapid Attacks II, Projectile Acceleration II, Execute II)."),
 16: L("Skysliver (Winged Spear) no Set 1. Barrage (Uncut nível 5) e Infernal Cry.", "Skysliver (Winged Spear) in Set 1. Barrage (Level 5 Uncut) and Infernal Cry."),
 24: L("Sniper's Mark (Uncut nível 7): as Frenzy Charges do Barrage.", "Sniper's Mark (Level 7 Uncut): Barrage's Frenzy Charges."),
 27: L("Thrillsteel (capacete).", "Thrillsteel (helmet)."),
 28: L("1º Trial: Essence of Virtue.", "1st Trial: Essence of Virtue."),
 30: L("Anéis rares com dano adicionado e resistência (~30 e ~50).", "Rare rings with added damage and resistance (~30 and ~50)."),
 38: L("Ignagduk: +30 Spirit → Wind Dancer.", "Ignagduk: +30 Spirit → Wind Dancer."),
 40: L("2º Trial: Gem Studded. Skysliver Runeforged. Árvore: Javelin e Dance with Death (Set 1 sem off hand).", "2nd Trial: Gem Studded. Runeforged Skysliver. Tree: Javelin and Dance with Death (Set 1 without an off hand)."),
 42: L("The Taming (anel, ~4 Divines): o Twister usa várias superfícies elementais.", "The Taming (ring, ~4 Divines): Twister uses multiple elemental surfaces."),
 45: L("Widow's Reign (corpo).", "Widow's Reign (body)."),
 55: L("Cat O' Nine Tails (cinto).", "Cat O' Nine Tails (belt)."),
 62: L("Lythara: +40 Spirit → Combat Frenzy.", "Lythara: +40 Spirit → Combat Frenzy."),
 65: L("3º Trial: Advanced Thaumaturgy. Morior Invictus fica disponível.", "3rd Trial: Advanced Thaumaturgy. Morior Invictus becomes available."),
 75: L("4º Trial: Motoric Implants (+2 níveis nas skills de Dex).", "4th Trial: Motoric Implants (+2 levels on Dex skills)."),
 79: L("Respec para a árvore do PoB (as skills não mudam) com Morior Invictus e Sacred Flame (nível 84).", "Respec into the PoB tree (skills don't change) with Morior Invictus and Sacred Flame (level 84)."),
 90: L("Amuleto com Spirit e +3 de projétil, Trinity, Cast on Critical e os Lineage.", "Amulet with Spirit and +3 projectile, Trinity, Cast on Critical and the Lineage supports."),
}


ASCENDANCY = [
 dict(order=1, key="eov", node="Essence of Virtue", when=L("1º Trial (~nível 28)", "1st Trial (~level 28)"), text=L("Concede a skill Virtuous Barrier: uma barreira que junta Motes protetores de cada atributo, mas perde um Mote quando você é atingido.", "Grants the Virtuous Barrier skill: a barrier that gathers protective Motes of each attribute but loses one when you're hit."), why=L("É a defesa da build desde cedo e fornece os Motes usados no balanço do Gem Studded.", "It's the build's defence from early on and provides the Motes used to balance Gem Studded.")),
 dict(order=2, key="gs", node="Gem Studded", when=L("2º Trial (~nível 40)", "2nd Trial (~level 40)"), text=L("Para cada cor de suporte mais numerosa: Vermelho = hits contra você sem Critical Damage Bonus; Azul = skills custam 30% menos; Verde = 40% menos penalidade de movimento ao usar skills.", "For each most-numerous support colour: Red = hits against you have no Critical Damage Bonus; Blue = skills cost 30% less; Green = 40% less movement penalty while using skills."), why=L("Twister e Whirling Slash usam muitos suportes verdes (Dex): andar atacando fica mais rápido. O PoB usa grupos de skills desligados só para acertar a contagem. Só vale o Weapon Set ativo.", "Twister and Whirling Slash use many green (Dex) supports: moving while attacking gets faster. The PoB uses switched-off skill groups just to get the count right. Only the active Weapon Set counts.")),
 dict(order=3, key="at", node="Advanced Thaumaturgy", when=L("3º Trial (~nível 65)", "3rd Trial (~level 65)"), text=L("A qualidade das gems dá às skills equipadas um efeito adicional.", "Gem quality grants socketed skills an additional effect."), why=L("Suba a qualidade das skills principais (o PoB usa Skill Gem Quality em três nós).", "Raise the quality of your main skills (the PoB uses Skill Gem Quality on three nodes).")),
 dict(order=4, key="mi", node="Motoric Implants", when=L("4º Trial (~nível 75)", "4th Trial (~level 75)"), text=L("+2 níveis em todas as skills que exigem Dexterity.", "+2 levels on all skills with a Dexterity requirement."), why=L("Twister, Whirling Slash e Barrage exigem Dex: é o maior salto de dano da ascendência.", "Twister, Whirling Slash and Barrage require Dex: it's the ascendancy's biggest damage jump.")),
]
ASC_UNLOCK = [28, 40, 65, 75]
PHASE_START = {}
ASC_PHASE = {"a1": [], "a2": ["Essence of Virtue"], "a3": ["Essence of Virtue", "Gem Studded"], "a4": ["Essence of Virtue", "Gem Studded"],
             "maps": ["Essence of Virtue", "Gem Studded", "Advanced Thaumaturgy"]}

KEY_PASSIVES = [
 dict(node="Remorseless", type="Notable", text=L("+15% de dano de projétil, +30% de Stun buildup contra inimigos a menos de 2 m, +5 Força.", "+15% projectile damage, +30% Stun buildup against enemies within 2 m, +5 Strength."), when=L("Ato 1 → 78", "Act 1 → 78"), why=L("O Twister é projétil: o primeiro dano de projétil perto do início da Mercenary.", "Twister is a projectile: the first projectile damage near the Mercenary start.")),
 dict(node="Ricochet", type="Notable", text=L("+15% de dano de projétil e chance de o projétil encadear no terreno.", "+15% projectile damage and a chance for projectiles to chain off terrain."), when=L("Ato 1 → 78", "Act 1 → 78"), why=L("Mais +15% logo nos primeiros 17 pontos.", "Another +15% right in the first 17 points.")),
 dict(node="Swift Flight", type="Notable", text=L("+15% de velocidade de projétil e +20% de dano físico.", "+15% projectile speed and +20% physical damage."), when=L("Ato 2 → sempre", "Act 2 → forever"), why=L("Está na árvore do PoB: fica depois do respec.", "It's on the PoB tree: it stays after the respec.")),
 dict(node="Javelin", type="Notable", text=L("+40% de dano crítico com Spears.", "+40% Critical Damage Bonus with Spears."), when=L("Ato 3 → sempre", "Act 3 → forever"), why=L("O maior bônus de crítico de spear; base do crítico do PoB.", "The biggest spear crit bonus; the base of the PoB's crit.")),
 dict(node="Dance with Death", type="Notable", text=L("+25% de velocidade de skill com uma arma de uma mão e a off hand vazia (a spear do Set 1).", "+25% skill speed with a one-handed weapon and an empty off hand (the Set 1 spear)."), when=L("Ato 3 → sempre", "Act 3 → forever"), why=L("Mantenha o Set 1 sem off hand para ligar.", "Keep Set 1 without an off hand to turn it on.")),
 dict(node="Heartbreaking", type="Notable", text=L("+25% de dano crítico, +10 Força.", "+25% Critical Damage Bonus, +10 Strength."), when=L("Ato 4 → sempre", "Act 4 → forever"), why=L("Crítico: a build inteira gira em torno dele.", "Crit: the whole build revolves around it.")),
 dict(node="Heartstopping", type="Notable", text=L("+20% de chance de crítico, +10 Inteligência.", "+20% Critical Hit Chance, +10 Intelligence."), when=L("Ato 4 → sempre", "Act 4 → forever"), why=L("Mais críticos: mais Frenzy Charges pelo Sniper's Mark e mais Blazing Critical.", "More crits: more Frenzy Charges from Sniper's Mark and more Blazing Critical.")),
 dict(node="Killer Instinct", type="Notable", text=L("+40% de dano de ataque com a vida cheia e +60% com pouca vida.", "+40% attack damage on Full Life and +60% on Low Life."), when=L("Mapas → sempre", "Maps → forever"), why=L("O maior dano de ataque da árvore; a vida cheia é o normal.", "The biggest attack damage on the tree; full life is the norm.")),
]
TREE_STAGES = [
 dict(lv="1–15", focus=L("Dano de projétil perto do início", "Projectile damage near the start"), dmg="Whirling Slash + Twister", **{"def": L("Vida", "Life")}, spirit="—", dont=L("Pegar Atributo demais", "Taking too much Attribute")),
 dict(lv="16–45", focus=L("Velocidade e crítico de spear", "Speed and spear crit"), dmg="Twister + Barrage", **{"def": L("Vida e resistências", "Life and resistances")}, spirit="Herald · Wind Dancer", dont=L("Pegar nó de arma que você não usa", "Taking nodes for a weapon you don't use")),
 dict(lv="46–78", focus=L("Crítico, Killer Instinct e velocidade", "Crit, Killer Instinct and speed"), dmg="Twister + Barrage", **{"def": L("Armour/Evasion (Morior)", "Armour/Evasion (Morior)")}, spirit="Herald · Wind Dancer · Combat Frenzy", dont=L("Respec cedo demais", "Respeccing too early")),
 dict(lv="79–100", focus=L("Respec para a árvore do PoB + joias", "Respec into the PoB tree + jewels"), dmg="Twister + Barrage", **{"def": L("Evasion/ES (Morior)", "Evasion/ES (Morior)")}, spirit="Sete reservas + Trinity", dont=L("Perder o requisito de Dex", "Losing the Dex requirement")),
]

UNIQUES = [
 U("Enfolding Dawn", "Body Armour", L("Armadura", "Armour"), "a1", L("(50–100)% de Armour e Energy Shield, +100 de Spirit e 5–15% de resistências; não ganha bônus de Inteligência.", "(50–100)% Armour and Energy Shield, +100 Spirit and 5–15% resistances; gains no bonus from Intelligence."), L("Nível 0, ~0,003 Divine: +100 de Spirit deixam ligar Herald, Wind Dancer e Combat Frenzy assim que você tiver as gems.", "Level 0, ~0.003 Divine: +100 Spirit lets you run Herald, Wind Dancer and Combat Frenzy as soon as you have the gems."), L("Body rare Str/Dex com vida e resistências.", "A Str/Dex rare body with life and resistances."), 1),
 U("Blackheart", "Ring", L("Acessório", "Accessory"), "a1", L("Regeneração de vida, dano adicionado a ataques e dano também aplicado como caos.", "Life regeneration, added attack damage and damage also applied as chaos."), L("Dois anéis por ~0,01 Divine.", "Two rings for ~0.01 Divine."), L("Anel rare de dano e resistência.", "A rare ring with damage and resistance."), 1),
 U("Meginord's Girdle", L("Cinto", "Belt"), L("Acessório", "Accessory"), "a1", L("+40–50 de Força, +10–15% de resistência a frio e os flasks gastam 50% mais cargas (desvantagem).", "+40–50 Strength, +10–15% cold resistance and flasks use 50% more charges (a drawback)."), L("Nível 0, quase de graça.", "Level 0, nearly free."), L("Cinto com vida e resistências.", "A belt with life and resistances."), 1),
 U("Wanderlust", L("Botas", "Boots"), L("Armadura", "Armour"), "a1", L("+20% de velocidade de movimento, ES e imunidade à lentidão.", "+20% movement speed, ES and immunity to Slow."), L("Nível 11 (Wrapped Sandals: exige 17 de Inteligência).", "Level 11 (Wrapped Sandals: needs 17 Intelligence)."), L("Botas com movimento.", "Boots with movement."), 11),
 U("Skysliver", "Spear", L("Arma", "Weapon"), "a2", L("Adiciona dano de raio, velocidade de ataque e chance de Shock; só rola o mínimo ou o máximo de dano.", "Adds lightning damage, attack speed and Shock chance; rolls only the minimum or maximum damage."), L("Sua spear do Set 1 do nível 16 ao ~60: Winged Spear (~0,1 Divine). Se o jogo pedir para remover algo ao equipar, arraste para o slot de off hand.", "Your Set 1 spear from level 16 to ~60: Winged Spear (~0.1 Divine). If the game asks you to remove something when equipping, drag to the off hand slot."), L("Spear rare com dano elemental e velocidade.", "A rare spear with elemental damage and speed."), 16),
 U("Thrillsteel", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a2", L("Onslaught permanente (mais velocidade de ataque e movimento).", "Permanent Onslaught (more attack and movement speed)."), L("Spired Greathelm, ~0,03 Divine.", "Spired Greathelm, ~0.03 Divine."), L("Capacete rare de vida.", "A rare life helmet."), 27),
 U("The Fall of the Axe", "Charm", "Charm", "a2", L("Usado quando você sofre Slow: dá Onslaught durante o efeito.", "Used when you're Slowed: grants Onslaught during the effect."), L("Silver Charm, ~0,6 Divine; a Whirling Slash já Desacelera os outros, mas os bosses te Desaceleram.", "Silver Charm, ~0.6 Divine; Whirling Slash already Slows others, but bosses Slow you."), L("Silver Charm mágico.", "A magic Silver Charm."), 10),
 U("Nascent Hope", "Charm", "Charm", "a3", L("Usado quando você é Congelado; ganha carga ao matar e recarrega o Energy Shield.", "Used when you're Frozen; gains a charge on kill and starts Energy Shield recharge."), L("Thawing Charm, ~0,1 Divine.", "Thawing Charm, ~0.1 Divine."), L("Thawing Charm mágico.", "A magic Thawing Charm."), 12),
 U("Widow's Reign", "Body Armour", L("Armadura", "Armour"), "a4", L("101–149% de Armour e Evasion, +100–150 de vida e 17–23% de resistência a caos.", "101–149% Armour and Evasion, +100–150 life and 17–23% chaos resistance."), L("Knight Armour: a melhor defesa barata do meio do jogo.", "Knight Armour: the best cheap defence of the mid game."), L("Body rare Str/Dex com vida.", "A Str/Dex rare body with life."), 45),
 U("Cat O' Nine Tails", L("Cinto", "Belt"), L("Acessório", "Accessory"), "a4", L("+120–199 de vida e regeneração de vida ao ser atingido.", "+120–199 life and life regeneration when hit."), L("Utility Belt (nível 55).", "Utility Belt (level 55)."), L("Cinto de vida.", "A life belt."), 55),
 U("The Taming", "Ring", L("Acessório", "Accessory"), "maps", L("Mais dano por tipo de ailment elemental no inimigo; skills de Wind podem usar várias superfícies elementais.", "More damage per type of elemental ailment on the enemy; Wind skills can use multiple elemental surfaces."), L("Prismatic Ring, ~4 Divines (nível 42): casa com o Twister e o Herald of Thunder/Ice.", "Prismatic Ring, ~4 Divines (level 42): pairs with Twister and Herald of Thunder/Ice."), L("Anel rare de resistência.", "A rare resistance ring."), 42),
 U("Morior Invictus", "Body Armour", L("Armadura", "Armour"), "maps", L("+300–400% de Armour, Evasion e ES e bônus por socket cheio: atributos, vida, mana, resistência a caos, regeneração e resistências elementais.", "+300–400% Armour, Evasion and ES and bonuses per filled socket: attributes, life, mana, chaos resistance, regeneration and elemental resistances."), L("Nível 65, ~6 Divines: a peça que faz a Armour/Evasion/ES do endgame do PoB.", "Level 65, ~6 Divines: the piece that makes the PoB's endgame Armour/Evasion/ES."), L("Body de Armour com vida.", "An Armour body with life."), 65),
 U("Sacred Flame", "Sceptre", L("Arma", "Weapon"), "endgame", L("+Spirit, ganha 60% do dano como fogo extra e concede a skill Purity of Fire.", "+Spirit, gain 60% of damage as extra fire and grants the Purity of Fire skill."), L("Shrine Sceptre (nível 84, ~5 Divines): a off hand do Set 2; com ele você paga as reservas do endgame.", "Shrine Sceptre (level 84, ~5 Divines): the Set 2 off hand; with it you pay for the endgame reservations."), L("Sceptre rare com Spirit.", "A rare Spirit sceptre."), 84),
 U("Lavianga's Spirits", "Flask", "Flask", "maps", L("O flask não pode ser usado: o efeito de mana fica sempre ativo (menos mana recuperada).", "The flask cannot be used: the mana effect is always active (less mana recovered)."), L("Mana constante sem apertar nada (~0,1 Divine, nível 49).", "Constant mana without pressing anything (~0.1 Divine, level 49)."), L("Flask de mana normal.", "A regular mana flask."), 49),
 U("Rite of Passage", "Charm", "Charm", "max", L("Ao matar um Rare ou Unique, você é possuído por espíritos animais (o autor usa o Lobo).", "On killing a Rare or Unique you're possessed by animal spirits (the author uses the Wolf)."), L("Luxo (~15 Divines).", "Luxury (~15 Divines)."), L("Golden Charm normal.", "A regular Golden Charm."), 50),
 U("Headhunter", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Ao matar um Rare você ganha os modificadores dele por 60 s.", "On killing a Rare you gain its modifiers for 60 s."), L("O cinto do PoB (~246 Divines).", "The PoB's belt (~246 Divines)."), L("Cinto de vida e Armour.", "A life and Armour belt."), 50),
]
GEAR = [
 dict(slot=L("Spear (Set 1)", "Spear (Set 1)"), cheap=L("Spear branca do vendor (1–15) → Skysliver (16)", "White vendor spear (1–15) → Skysliver (16)"), value="Skysliver", full=L("Soaring Spear rare ilvl 82 (Armageddon Edge)", "Rare Soaring Spear ilvl 82 (Armageddon Edge)"), affix=L("Velocidade de ataque; dano elemental adicionado; chance de crítico", "Attack speed; added elemental damage; crit chance"), note=L("Twister e Whirling Slash do nível 1 ao 100; off hand vazia (Dance with Death)", "Twister and Whirling Slash from level 1 to 100; empty off hand (Dance with Death)")),
 dict(slot=L("Set 2 (spear + Sacred Flame)", "Set 2 (spear + Sacred Flame)"), cheap=L("Nada até o endgame", "Nothing until endgame"), value="Sacred Flame", full=L("Mind Edge + Sacred Flame", "Mind Edge + Sacred Flame"), affix=L("Raio e fogo adicionados; Spirit", "Added lightning and fire; Spirit"), note=L("Só a partir do 79–84", "Only from 79–84"), from_lv=78, no_cheap=True),
 dict(slot=L("Capacete", "Helmet"), cheap="Thrillsteel", value=L("Base de Armour com vida e resistências", "Armour base with life and resistances"), full=L("Ancestral Tiara rare com Energy Shield", "Rare Ancestral Tiara with Energy Shield"), affix=L("Vida; Armour/ES; resistências", "Life; Armour/ES; resistances"), note=""),
 dict(slot="Body Armour", cheap="Enfolding Dawn", value="Widow's Reign", full="Morior Invictus", affix="—", note=L("Cinco sockets: runas de vida e idols", "Five sockets: life runes and idols")),
 dict(slot=L("Luvas", "Gloves"), cheap=L("Vida e resistências", "Life and resistances"), value=L("Armour com vida e dano adicionado", "Armour with life and added damage"), full=L("Secured Wraps rare: +2 de projétil e dano de raio", "Rare Secured Wraps: +2 projectile and lightning damage"), affix=L("+ nível de projétil; dano adicionado; vida", "+ projectile levels; added damage; life"), note=L("EVITE 'chance de projétil extra': está bugada", "AVOID 'chance for an extra projectile': it's bugged")),
 dict(slot=L("Botas", "Boots"), cheap="Wanderlust", value=L("35% de movimento + vida", "35% movement + life"), full=L("Daggerfoot Shoes rare: movimento e Evasion/ES", "Rare Daggerfoot Shoes: movement and Evasion/ES"), affix=L("Movimento; vida; resistências", "Movement; life; resistances"), note=""),
 dict(slot=L("Amuleto", "Amulet"), cheap=L("Vida e resistências", "Life and resistances"), value=L("Absent Amulet com Spirit", "Absent Amulet with Spirit"), full=L("Absent Amulet: +3 de projétil e Spirit (Gale Gorget)", "Absent Amulet: +3 projectile and Spirit (Gale Gorget)"), affix=L("Spirit; + nível de projétil; Armour/Evasion/ES", "Spirit; + projectile levels; Armour/Evasion/ES"), note=""),
 dict(slot=L("Anéis", "Rings"), cheap="Blackheart", value="The Taming", full=L("The Taming + Unset Ring rare com +1 slot de skill (Entropy Coil)", "The Taming + rare Unset Ring with +1 skill slot (Entropy Coil)"), affix=L("Dano adicionado; vida; resistência", "Added damage; life; resistance"), note=""),
 dict(slot=L("Cinto", "Belt"), cheap="Meginord's Girdle", value="Cat O' Nine Tails", full="Headhunter", affix="—", note=""),
 dict(slot="Charms", cheap="The Fall of the Axe", value="Nascent Hope", full="Rite of Passage", affix=L("Cobrir Slow e Freeze", "Cover Slow and Freeze"), note=""),
 dict(slot="Flasks", cheap=L("Vida", "Life"), value="Lavianga's Spirits", full=L("Ultimate Life Flask + Lavianga's Spirits", "Ultimate Life Flask + Lavianga's Spirits"), affix=L("Recuperação", "Recovery"), note=""),
]
exec(open(os.path.join(HERE, "gear_opts.py"), encoding="utf-8").read())
for _g, _k in zip(GEAR, SLOT_OPTS):
    _g["opts"] = GEAR_OPTS[_k]
BUY_ORDER = [
 dict(p=1, item=L("Spear branca + (se der) Enfolding Dawn", "White spear + (if you can) Enfolding Dawn"), phase=L("Nível 1", "Level 1"), cost=L("Barato", "Cheap"), impact=L("A build inteira: as duas skills exigem spear", "The whole build: both skills need a spear")),
 dict(p=2, item="Skysliver (Winged Spear)", phase=L("Nível 16", "Level 16"), cost=L("Barato", "Cheap"), impact=L("Dano e velocidade para o Twister", "Damage and speed for Twister")),
 dict(p=3, item="Wanderlust + Thrillsteel", phase=L("Ato 2", "Act 2"), cost=L("Barato", "Cheap"), impact=L("Movimento e vida", "Movement and life")),
 dict(p=4, item="The Taming", phase=L("Nível 42+", "Level 42+"), cost=L("Valor", "Value"), impact=L("O Twister usa várias superfícies elementais", "Twister uses multiple elemental surfaces")),
 dict(p=5, item="Widow's Reign + Cat O' Nine Tails", phase=L("Nível 45–55", "Level 45–55"), cost=L("Barato", "Cheap"), impact=L("Vida e defesa para os mapas", "Life and defence for maps")),
 dict(p=6, item="Morior Invictus", phase=L("Mapas", "Maps"), cost=L("Valor", "Value"), impact=L("Armour/Evasion/ES e atributos por socket", "Armour/Evasion/ES and attributes per socket")),
 dict(p=7, item="Sacred Flame", phase="Endgame", cost=L("Valor", "Value"), impact=L("Spirit e 60% do dano como fogo extra", "Spirit and 60% of damage as extra fire")),
 dict(p=8, item=L("Headhunter + Lineage", "Headhunter + Lineage"), phase="Pinnacle", cost=L("Luxo", "Luxury"), impact=L("Teto de dano", "Damage ceiling")),
]
TRICKS = [
 {"cat": L("Skills", "Skills"), "lvl": L("Fácil", "Easy"), "title": L("Levante o redemoinho, depois solte o Twister", "Raise the whirlwind, then release Twister"), "body": L("A Whirling Slash levanta um Whirlwind em volta de você. O Twister, quando encosta nele, o consome e cria tornados extras que causam mais dano. Por isso as duas skills andam juntas do nível 1 ao 100: Whirling Slash no pack, Twister no meio do redemoinho.", "Whirling Slash kicks up a Whirlwind around you. Twister, when it touches it, consumes it and spawns extra tornadoes that deal more damage. That's why the two skills go together from level 1 to 100: Whirling Slash on the pack, Twister in the middle of the whirlwind.")},
 {"cat": L("Cargas", "Charges"), "lvl": L("Médio", "Medium"), "title": L("Barrage só rende com Frenzy Charge", "Barrage only pays off with Frenzy Charges"), "body": L("O Barrage prepara o próximo Twister para se repetir, e gasta Frenzy Charges para repetir mais. As cargas vêm do Sniper's Mark (crítico no alvo marcado) e do Combat Frenzy (Freeze, Electrocute ou Pin). Perpetual Charge e Heightened Charges fazem as cargas render mais.", "Barrage readies the next Twister to repeat, and spends Frenzy Charges to repeat more. The charges come from Sniper's Mark (a crit on the marked target) and Combat Frenzy (Freeze, Electrocute or Pin). Perpetual Charge and Heightened Charges make the charges go further.")},
 {"cat": L("Setup", "Setup"), "lvl": L("Fácil", "Easy"), "title": L("Set 1 sem off hand", "Set 1 without an off hand"), "body": L("Dance with Death (+25% de velocidade de skill) só vale com uma arma de uma mão e a off hand vazia. Mantenha o Set 1 assim; o Sacred Flame vai no Set 2.", "Dance with Death (+25% skill speed) only works with a one-handed weapon and an empty off hand. Keep Set 1 that way; Sacred Flame goes in Set 2.")},
 {"cat": L("Elementos", "Elements"), "lvl": L("Médio", "Medium"), "title": L("O Twister ganha elemento do chão", "Twister takes element from the ground"), "body": L("Passar por superfícies elementais (ou consumir um Whirlwind elemental) dá dano extra daquele elemento ao Twister; o anel The Taming deixa usar várias ao mesmo tempo. Herald of Thunder e Ice e a Frost Wall da Cast on Critical criam essas superfícies.", "Passing over elemental surfaces (or consuming an elemental Whirlwind) gives Twister extra damage of that element; the ring The Taming lets you use several at once. Herald of Thunder and Ice and Cast on Critical's Frost Wall create them.")},
 {"cat": L("Itens", "Items"), "lvl": L("Fácil", "Easy"), "title": L("EVITE projétil extra nas luvas", "AVOID extra projectile on gloves"), "body": L("O mod 'chance de projétil extra' está bugado nesta versão (segundo o autor da build Whirling Glacial Bolt: confirme no jogo): evite. Prefira +2 de nível de skills de projétil.", "The 'chance for an extra projectile' mod is bugged in this version (per the author of the Whirling Glacial Bolt build: confirm in game): avoid it. Prefer +2 projectile skill levels.")},
 {"cat": L("Gems", "Gems"), "lvl": L("Difícil", "Hard"), "title": L("Balanceie o Gem Studded", "Balance Gem Studded"), "body": L("O Gem Studded (2º Trial, ~40) conta só os suportes do Weapon Set ativo. O PoB tem grupos de skills desligados só para acertar a contagem de cores; confira o custo de mana das skills para saber qual cor manda.", "Gem Studded (2nd Trial, ~40) only counts the active Weapon Set's supports. The PoB has switched-off skill groups just to get the colour count right; check your skills' mana costs to see which colour rules.")},
 {"cat": L("Respec", "Respec"), "lvl": L("Médio", "Medium"), "title": L("Quando fazer o respec do 79", "When to do the 79 respec"), "body": L("A árvore da campanha inclui um desvio de projétil (26 nós) que sai no respec. Faça o respec quando tiver o Morior Invictus e o Sacred Flame: a árvore do PoB conta com a defesa do Morior e com o Spirit do Sacred Flame.", "The campaign tree includes a projectile detour (26 nodes) that leaves at the respec. Respec once you have Morior Invictus and Sacred Flame: the PoB tree counts on Morior's defence and Sacred Flame's Spirit.")},
]
TROUBLESHOOT = [
 (L("O Twister não cria tornados extras", "Twister doesn't spawn extra tornadoes"), L("Ele precisa tocar um Whirlwind. Use a Whirling Slash antes e solte o Twister em cima do redemoinho.", "It needs to touch a Whirlwind. Use Whirling Slash first and release Twister over the whirlwind.")),
 (L("O Barrage parece não fazer nada", "Barrage seems to do nothing"), L("Ele só repete de verdade com Frenzy Charges. Use o Sniper's Mark num alvo e critique; no 62, ligue o Combat Frenzy.", "It only truly repeats with Frenzy Charges. Use Sniper's Mark on a target and crit; at 62, turn on Combat Frenzy.")),
 (L("As skills não equipam", "The skills won't equip"), L("Twister e Whirling Slash exigem spear. Ponha uma spear (a branca serve) no Weapon Set 1.", "Twister and Whirling Slash require a spear. Put a spear (a white one works) in Weapon Set 1.")),
 (L("O Dance with Death não funciona", "Dance with Death isn't working"), L("A off hand do Set 1 precisa estar vazia e a arma tem que ser de uma mão (a spear).", "Set 1's off hand must be empty and the weapon must be one-handed (the spear).")),
 (L("Não fecho o Spirit", "Spirit doesn't add up"), L("Herald 30 + Wind Dancer 30 + Combat Frenzy 30 = 90 dos 100 das quests. O Enfolding Dawn (+100) adianta; no endgame o Sacred Flame e o amuleto pagam as reservas a mais.", "Herald 30 + Wind Dancer 30 + Combat Frenzy 30 = 90 of the quests' 100. Enfolding Dawn (+100) speeds it up; in endgame Sacred Flame and the amulet pay the extra reservations.")),
 (L("Estou fraco para o meu nível", "I'm weak for my level"), L("Confira a spear (Skysliver no 16, Runeforged no 40), os anéis rares (~30 e ~50) e se os nós de dano de projétil (Remorseless, Ricochet) e de crítico da árvore estão pegos.", "Check the spear (Skysliver at 16, Runeforged at 40), the rare rings (~30 and ~50) and whether the tree's projectile damage (Remorseless, Ricochet) and crit nodes are taken.")),
]
ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Resistências no cap · árvore de 95 pontos · The Taming e Morior Invictus", "Resistances capped · 95-point tree · The Taming and Morior Invictus"), gear="Skysliver · Widow's Reign"),
 dict(stage="T1–T10", goal=L("Motoric Implants · respec do 79 · Sacred Flame", "Motoric Implants · the 79 respec · Sacred Flame"), gear=L("Spear + Sacred Flame", "Spear + Sacred Flame")),
 dict(stage="T11–T15", goal=L("Sete reservas de Spirit fechadas · joias do PoB", "Seven Spirit reservations closed · the PoB's jewels"), gear="Morior Invictus"),
 dict(stage="Pinnacle", goal=L("Trinity + Cast on Critical · Lineage", "Trinity + Cast on Critical · Lineage"), gear="Headhunter · Rite of Passage"),
]
CRAFT = [
 L("Spear rare: base branca (Ironhead 5 → Hunting 10 → Winged 16 → War 21 → Soaring 70) → Transmutation + Augmentation até dano elemental adicionado ou velocidade → Regal → Exalted. Do 16 ao ~60 a Skysliver dispensa craft.", "Rare spear: white base (Ironhead 5 → Hunting 10 → Winged 16 → War 21 → Soaring 70) → Transmutation + Augmentation until added elemental damage or speed → Regal → Exalted. From 16 to ~60 Skysliver needs no craft."),
 L("Armadura (capacete, luvas, botas): vida, resistências e Evasion/ES primeiro; movimento nas botas.", "Armour (helmet, gloves, boots): life, resistances and Evasion/ES first; movement on the boots."),
 L("Runas: Soul Core de velocidade ou runa elemental na spear e as de resistência que faltarem no corpo.", "Runes: a speed Soul Core or elemental rune on the spear and whatever resistance runes you're missing on the body."),
]
CASES = [
 (L("Não tenho a Skysliver", "I don't have Skysliver"), L("Use uma spear rare da base do seu nível ou a branca do vendor: as duas skills funcionam igual, só com menos dano. A Winged Spear custa ~0,1 Divine.", "Use a rare spear on a base of your level or the white vendor one: both skills work the same, just with less damage. A Winged Spear costs ~0.1 Divine.")),
 (L("Ainda não caiu o Barrage", "Barrage hasn't dropped yet"), L("Siga com Whirling Slash + Twister: é a mesma build, só sem as repetições. O Barrage é Uncut nível 5.", "Keep going with Whirling Slash + Twister: it's the same build, just without the repeats. Barrage is a level 5 Uncut.")),
 (L("Não tenho Spirit para o Combat Frenzy", "I don't have Spirit for Combat Frenzy"), L("Faltou o Lythara (~62, +40 Spirit) ou o Enfolding Dawn (+100). Use só Herald e Wind Dancer até lá.", "You're missing Lythara (~62, +40 Spirit) or Enfolding Dawn (+100). Use only Herald and Wind Dancer until then.")),
]
SOURCES = [
 dict(name="Maxroll — Spear Throw Twister Gemling Legionnaire (PoB, Onelonelyhunter)", use=L("Build base: árvore, gems, itens, joias e ascendência do endgame (nível 100)", "Base build: endgame tree, gems, items, jewels and ascendancy (level 100)"), url=GUIDE_URL),
 dict(name="Path of Building (PoE2) — Gems.lua e skills_*.lua", use=L("Descrições das gems, tiers e custos de Spirit", "Gem descriptions, tiers and Spirit costs"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name="poe.ninja — Economia e Builds (Forbidden Rites)", use=L("Preços e níveis dos uniques; uso da ascendência e da skill", "Prices and levels of the uniques; ascendancy and skill usage"), url="https://poe.ninja/poe2/builds/forbiddenrites"),
]

FIXES = [
 L("Este plano é uma ADAPTAÇÃO: o PoB do Maxroll é só o endgame (nível 100), sem guia nem leveling do autor. As skills do endgame (Whirling Slash e Twister na spear) entram no nível 1; a árvore da campanha é a do PoB numa ordem 'dano primeiro' com um desvio de 26 nós de dano de projétil perto do início da Mercenary (medido: +96% de dano de árvore aos 17 pontos contra +8% só com o caminho do PoB), que sai no respec do 79. O autor não valida essa progressão.", "This plan is an ADAPTATION: the Maxroll PoB is only the endgame (level 100), with no guide or leveling from the author. The endgame skills (Whirling Slash and Twister on the spear) come in at level 1; the campaign tree is the PoB's in a 'damage first' order with a 26-node detour through projectile damage near the Mercenary start (measured: +96% tree damage at 17 points against +8% with only the PoB's path), which leaves at the 79 respec. The author doesn't validate this progression."),
 L("A ordem dos nós e dos itens foi calculada, não jogada: o guia soma nós de dano, velocidade, crítico e vida da árvore, mas não simula o DPS no jogo. Se algum ato ficar fraco, diga qual e o guia é ajustado.", "The order of nodes and items was computed, not played: the guide adds up the tree's damage, speed, crit and life nodes but doesn't simulate DPS in game. If any act feels weak, say which and the guide gets adjusted."),
 L("Níveis das gems seguem o tier do Path of Building (Uncut = tier, aproximado); os níveis dos uniques vêm do poe.ninja. A ordem dos Trials e os níveis 28/40/65/75 são aproximados.", "Gem levels follow Path of Building's tier (Uncut = tier, approximate); the uniques' levels come from poe.ninja. Trial order and levels 28/40/65/75 are approximate."),
 L("O PoB tem 9 nós que só se alcançam com a joia Split Personality (socket 60735) e vários grupos de skills desligados só para acertar o Gem Studded: o guia lista só o que é jogado.", "The PoB has 9 nodes that are only reachable with the Split Personality jewel (socket 60735) and several switched-off skill groups just to get Gem Studded right: the guide lists only what is played."),
]
UI = dict(
 setNote=L("rares com + níveis de projétil, dano elemental adicionado e Spirit.", "rares with + projectile levels, added elemental damage and Spirit."),
 carry=r"^(Twister|Whirling Slash)$", box=L("SKILLS", "SKILLS"), spiritWhat=L("(buffs persistentes)", "(persistent buffs)"),
 mechBtn=L("Abrir Redemoinho & Cargas", "Open Whirlwind & Charges"), dmg2="Barrage", dmgBar=L("Dano do Twister (aprox.)", "Twister damage (approx.)"),
 dmgLegend=L("dano das repetições do Barrage (proporção aproximada)", "Barrage repeat damage (approximate ratio)"),
 earlyGone=L("As skills iniciais já saíram da barra: você passou do nível {u}.", "Starting skills already left the bar: you're past level {u}."),
 earlyNote=L("Skills de começo; saem no nível ~{u}.", "Early skills; they leave around level {u}."),
 treeIntro=L("Árvore real do PoB do Maxroll (148 nós + as joias), com a ordem 'dano primeiro': a campanha passa por nós de dano de projétil perto do início da Mercenary e no 79 você faz respec para a árvore do PoB.", "Real tree from the Maxroll PoB (148 nodes + the jewels), in a 'damage first' order: the campaign passes through projectile damage nodes near the Mercenary start and at 79 you respec into the PoB tree."),
 set1=L("spear (Twister e Whirling Slash)", "spear (Twister and Whirling Slash)"), set2=L("spear + Sacred Flame (endgame)", "spear + Sacred Flame (endgame)"), asc="Gemling Legionnaire", cls="Mercenary",
 respecTip=L("Na troca do 79 (respec), compare com a fase anterior: nós sem contorno verde já eram seus. Weapon Set 1 = spear; Set 2 = spear + Sacred Flame.", "At the 79 switch (respec), compare with the previous phase: nodes without a green outline were already yours. Weapon Set 1 = spear; Set 2 = spear + Sacred Flame."),
 routeIntro=L("Sete fases do nível 1 ao 100 com as mesmas duas skills de spear: Whirling Slash e Twister (Barrage a partir do 16). A campanha usa a árvore de dano; no 79 há um respec para a árvore do PoB.", "Seven phases from level 1 to 100 with the same two spear skills: Whirling Slash and Twister (Barrage from 16). The campaign uses the damage tree; at 79 there is a respec into the PoB tree."),
 socketPrio=["Twister", "Whirling Slash", "Barrage", "Herald of Thunder", "Wind Dancer", "Combat Frenzy"],
 permIntro=L("Nada disso volta depois. Spirit paga Herald, Wind Dancer e Combat Frenzy; o respec do 79 troca só a árvore.", "None of this comes back later. Spirit pays for Herald, Wind Dancer and Combat Frenzy; the 79 respec swaps only the tree."),
 atlasCards=[[L("Mapas que atrapalham", "Maps that hurt"), L("Evite mapas com 'Slow' e com sem-crítico: a build vive de crítico e movimento.", "Avoid maps with heavy Slow and crit-immunity: the build lives on crit and movement.")],
             [L("Farm", "Farming"), L("Guarde bases de spear (Soaring ilvl 82, Akoyan) para as spears do PoB e procure uma Winged Spear para a Skysliver.", "Keep spear bases (Soaring ilvl 82, Akoyan) for the PoB's spears and look for a Winged Spear for Skysliver.")]],
 foot=L("Guia adaptado do PoB do Maxroll, dados de jogo do Path of Building e preços do poe.ninja", "Guide adapted from the Maxroll PoB, Path of Building game data and poe.ninja prices"),
)
CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens e Árvore se adaptam na hora ao seu Spirit e ao que você marcou. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items and Tree tabs adapt instantly to your Spirit and what you ticked. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit máximo", "Max Spirit"), L("ex.: 100", "e.g. 100")], ["life", L("Vida máxima", "Max life"), ""], ["armour", "Armour", ""]],
 tiles=[[L("Spirit reservado", "Spirit reserved"), "used"], [L("Spirit livre", "Spirit free"), "free"], ["Armour", "armour"]],
 halve="", halveLabel="", halveTip="",
 buffs=[dict(key="herald", name="Herald of Thunder", cost=30), dict(key="wd", name="Wind Dancer", cost=30), dict(key="cf", name="Combat Frenzy", cost=30), dict(key="hice", name="Herald of Ice", cost=30),
        dict(key="gd", name="Ghost Dance", cost=30), dict(key="cr", name="Charge Regulation", cost=30), dict(key="berserk", name="Berserk", cost=30), dict(key="trinity", name="Trinity", cost=100)],
 own=[
  ["gear", "Enfolding Dawn", "Enfolding Dawn"], ["gear", "Blackheart", "Blackheart"], ["gear", "Wanderlust", "Wanderlust"], ["gear", "Skysliver", "Skysliver"], ["gear", "Thrillsteel", "Thrillsteel"],
  ["gear", "The Taming", "The Taming"], ["gear", "Morior Invictus", "Morior Invictus"], ["gear", "Sacred Flame", "Sacred Flame"], ["gear", "Lavianga's Spirits", "Lavianga's Spirits"],
  ["gem", "herald", "Herald of Thunder (30)"], ["gem", "wd", "Wind Dancer (30)"], ["gem", "cf", "Combat Frenzy (30)"], ["gem", "hice", "Herald of Ice (30)"], ["gem", "barrage", "Barrage"], ["gem", "sniper", "Sniper's Mark"],
  ["tree", "javelin", "Javelin"], ["tree", "dance", "Dance with Death"], ["tree", "killer", "Killer Instinct"],
  ["asc", "eov", "Essence of Virtue"], ["asc", "gs", "Gem Studded"], ["asc", "at", "Advanced Thaumaturgy"], ["asc", "mi", "Motoric Implants"],
 ],
 rules=[
  dict(when=dict(lvMin=1, notOwn=["Skysliver"]), lvl="tip", t=L("Spear no Set 1", "Spear in Set 1"), d=L("As duas skills exigem spear: uma branca do vendor serve até o 15; no 16, a Skysliver (~0,1 Divine).", "Both skills need a spear: a white vendor one works until 15; at 16, Skysliver (~0.1 Divine)."), tab="gear"),
  dict(when=dict(lvMin=1, notOwn=["Enfolding Dawn"]), lvl="tip", t=L("Enfolding Dawn", "Enfolding Dawn"), d=L("+100 de Spirit por ~0,003 Divine: liga Herald, Wind Dancer e Combat Frenzy cedo.", "+100 Spirit for ~0.003 Divine: turns on Herald, Wind Dancer and Combat Frenzy early."), tab="gear"),
  dict(when=dict(lvMin=11, notOwn=["Wanderlust"]), lvl="warn", t=L("Wanderlust", "Wanderlust"), d=L("Botas com 20% de movimento, nível 11.", "Boots with 20% movement, level 11."), tab="gear"),
  dict(when=dict(lvMin=14, notOwn=["herald"]), lvl="warn", t=L("Herald of Thunder", "Herald of Thunder"), d=L("Uncut Spirit Gem nível 4 com os 30 Spirit do King in the Mists.", "Level 4 Uncut Spirit Gem with the 30 Spirit from King in the Mists."), tab="skills"),
  dict(when=dict(lvMin=18, notOwn=["barrage"]), lvl="warn", t=L("Barrage", "Barrage"), d=L("Uncut nível 5: repete o Twister; precisa de Frenzy Charges.", "Level 5 Uncut: repeats Twister; needs Frenzy Charges."), tab="skills"),
  dict(when=dict(lvMin=26, notOwn=["sniper"]), lvl="warn", t=L("Sniper's Mark", "Sniper's Mark"), d=L("Uncut nível 7: o crítico no alvo marcado dá Frenzy Charge.", "Level 7 Uncut: a crit on the marked target gives a Frenzy Charge."), tab="skills"),
  dict(when=dict(lvMin=40, notOwn=["wd"]), lvl="warn", t=L("Wind Dancer", "Wind Dancer"), d=L("Precisa dos +30 Spirit do Ignagduk (~38).", "Needs Ignagduk's +30 Spirit (~38)."), tab="skills"),
  dict(when=dict(lvMin=40, notOwn=["gs"]), lvl="warn", t=L("Gem Studded", "Gem Studded"), d=L("2º Trial: bônus pela cor de suporte mais comum.", "2nd Trial: bonus for the most common support colour."), tab="asc"),
  dict(when=dict(lvMin=64, notOwn=["cf"]), lvl="warn", t=L("Combat Frenzy", "Combat Frenzy"), d=L("Precisa dos +40 Spirit do Lythara (~62).", "Needs Lythara's +40 Spirit (~62)."), tab="skills"),
  dict(when=dict(lvMin=75, notOwn=["mi"]), lvl="bad", t=L("Motoric Implants", "Motoric Implants"), d=L("+2 níveis em todas as skills de Dex: o maior salto de dano.", "+2 levels on all Dex skills: the biggest damage jump."), tab="asc"),
  dict(when=dict(lvMin=70, notOwn=["Morior Invictus"]), lvl="tip", t=L("Morior Invictus", "Morior Invictus"), d=L("Armour/Evasion/ES e atributos por socket (~6 Divines, nível 65).", "Armour/Evasion/ES and attributes per socket (~6 Divines, level 65)."), tab="gear"),
  dict(when=dict(lvMin=84, notOwn=["Sacred Flame"]), lvl="warn", t=L("Sacred Flame", "Sacred Flame"), d=L("Nível 84, ~5 Divines: Spirit e 60% do dano como fogo extra (Set 2).", "Level 84, ~5 Divines: Spirit and 60% of damage as extra fire (Set 2)."), tab="gear"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["a3", "a4", "maps", "endgame", "max"], when=dict(notOwn=["barrage"]), gemsFrom="a1", note=L("Sem o Barrage: mostrando Whirling Slash + Twister.", "No Barrage: showing Whirling Slash + Twister.")),
]
TREE_RULES = [
 dict(when=dict(lvMin=40, notOwn=["javelin"]), t=L("Javelin: +40% de dano crítico com Spears.", "Javelin: +40% Critical Damage Bonus with Spears."), node="Javelin"),
 dict(when=dict(lvMin=40, notOwn=["dance"]), t=L("Dance with Death: +25% de velocidade de skill com a spear e a off hand vazia.", "Dance with Death: +25% skill speed with the spear and an empty off hand."), node="Dance with Death"),
 dict(when=dict(lvMin=65, notOwn=["killer"]), t=L("Killer Instinct: +40% de dano de ataque com a vida cheia.", "Killer Instinct: +40% attack damage on Full Life."), node="Killer Instinct"),
]
TIMING_KEY = {"Skysliver": "Skysliver", "Wanderlust": "Wanderlust", "Thrillsteel": "Thrillsteel", "Enfolding Dawn": "Enfolding Dawn", "The Taming": "The Taming", "Morior Invictus": "Morior Invictus", "Sacred Flame": "Sacred Flame",
              "Herald of Thunder": "herald", "Wind Dancer": "wd", "Combat Frenzy": "cf", "Herald of Ice": "hice", "Barrage": "barrage", "Sniper's Mark": "sniper", "Motoric Implants": "mi", "Gem Studded": "gs"}

T("item", "Enfolding Dawn", 1, L("Pilgrim Vestments, nível 0; ~0,003 Divine", "Pilgrim Vestments, level 0; ~0.003 Divine"), L("Nível 1.", "Level 1."), L("+100 de Spirit desde o começo.", "+100 Spirit from the start."), L("Corpo qualquer com vida.", "Any body with life."), "—")
T("item", "Wanderlust", 11, L("Wrapped Sandals nível 11; ~0,01 Divine", "Level 11 Wrapped Sandals; ~0.01 Divine"), L("Ato 1.", "Act 1."), L("20% de movimento e imunidade à lentidão.", "20% movement and Slow immunity."), L("Botas com movimento até lá.", "Boots with movement until then."), "—")
T("item", "Skysliver", 16, L("Winged Spear nível 16; ~0,1 Divine", "Level 16 Winged Spear; ~0.1 Divine"), L("Ato 2.", "Act 2."), L("Dano e velocidade para o Twister.", "Damage and speed for Twister."), L("Spear branca do vendor até lá.", "White vendor spear until then."), "—")
T("item", "Thrillsteel", 27, L("Spired Greathelm nível 27; ~0,03 Divine", "Level 27 Spired Greathelm; ~0.03 Divine"), L("Ato 2.", "Act 2."), L("Capacete de vida.", "A life helmet."), "—", "—")
T("item", "The Taming", 42, L("Prismatic Ring nível 42; ~4 Divines", "Level 42 Prismatic Ring; ~4 Divines"), L("Ato 3.", "Act 3."), L("O Twister usa várias superfícies elementais.", "Twister uses multiple elemental surfaces."), "—", "—")
T("item", "Morior Invictus", 65, L("Nível 65; ~6 Divines", "Level 65; ~6 Divines"), L("Mapas.", "Maps."), L("Armour/Evasion/ES e atributos por socket.", "Armour/Evasion/ES and attributes per socket."), "—", "—")
T("item", "Sacred Flame", 84, L("Shrine Sceptre nível 84; ~5 Divines", "Level 84 Shrine Sceptre; ~5 Divines"), L("Endgame.", "Endgame."), L("Spirit e 60% do dano como fogo extra.", "Spirit and 60% of damage as extra fire."), "—", "—")
T("skill", "Herald of Thunder", 12, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Depois do King in the Mists.", "After King in the Mists."), L("Raios ao matar Shockados.", "Lightning on killing Shocked enemies."), L("Não ligue sem 30 Spirit livres.", "Don't turn on without 30 free Spirit."), "—")
T("skill", "Barrage", 16, L("Uncut nível 5", "Level 5 Uncut"), L("Ato 2.", "Act 2."), L("Repete o Twister várias vezes.", "Repeats Twister several times."), L("Whirling Slash + Twister até lá.", "Whirling Slash + Twister until then."), "—")
T("skill", "Sniper's Mark", 24, L("Uncut nível 7", "Level 7 Uncut"), L("Ato 2.", "Act 2."), L("Frenzy Charges pelo crítico.", "Frenzy Charges from crits."), "—", "—")
T("skill", "Wind Dancer", 38, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Depois do Ignagduk.", "After Ignagduk."), L("Defesa e empurrão ao ser atingido.", "Defence and knockback when hit."), "—", "—")
T("skill", "Combat Frenzy", 62, L("Tier 8, 30 Spirit", "Tier 8, 30 Spirit"), L("Depois do Lythara.", "After Lythara."), L("Frenzy Charge ao Congelar, Eletrocutar ou Prender.", "Frenzy Charge on Freeze, Electrocute or Pin."), "—", "—")
T("asc", "Gem Studded", 40, L("2º Trial", "2nd Trial"), L("Ato 3.", "Act 3."), L("Bônus pela cor de suporte mais comum.", "Bonus for the most common support colour."), "—", "—")
T("asc", "Motoric Implants", 75, L("4º Trial", "4th Trial"), L("Mapas.", "Maps."), L("+2 níveis em skills de Dex.", "+2 levels on Dex skills."), "—", "—")

MECH = dict(
 title=L("Redemoinho & Cargas", "Whirlwind & Charges"),
 intro=L("A build inteira é uma ideia só: a Whirling Slash levanta um redemoinho, o Twister o consome e se multiplica, e o Barrage repete o Twister com Frenzy Charges. É a mesma do nível 1 ao 100: só o dano, os suportes e os itens crescem.", "The whole build is one idea: Whirling Slash raises a whirlwind, Twister consumes it and multiplies, and Barrage repeats Twister with Frenzy Charges. It's the same from level 1 to 100: only damage, supports and items grow."),
 sections=[
  dict(type="cards", cards=[
   [L("1. Redemoinho", "1. Whirlwind"), L("A Whirling Slash (melee) gira em círculo e levanta um Whirlwind em volta de você: Desacelera e Cega os inimigos, e sair da área faz a tempestade colapsar causando dano e Knockback. Rage I–III faz cada golpe gerar Rage.", "Whirling Slash (melee) slashes in a circle and kicks up a Whirlwind around you: it Slows and Blinds enemies, and leaving the area collapses the storm, dealing damage and Knockback. Rage I–III makes every hit generate Rage.")],
   [L("2. Tornado", "2. Tornado"), L("O Twister avança errático, Cega e Acerta várias vezes. Se um tornado toca um Whirlwind das suas outras skills, consome o Whirlwind e cria tornados extras com mais dano. Passar por superfície elemental (ou consumir um Whirlwind elemental) dá dano extra daquele elemento.", "Twister moves erratically, Blinds and Hits repeatedly. If a tornado touches a Whirlwind from your other skills, it consumes the Whirlwind and creates extra tornadoes that deal more damage. Passing over an elemental surface (or consuming an elemental Whirlwind) grants extra damage of that element.")],
   [L("3. Cargas", "3. Charges"), L("O Barrage prepara o próximo ataque de projétil de spear repetível (o Twister) para se repetir várias vezes e gasta Frenzy Charges para repetir mais. Sniper's Mark (crítico no alvo) e Combat Frenzy (Freeze, Electrocute ou Pin) geram as cargas; Perpetual Charge e Heightened Charges as fazem render.", "Barrage readies your next Repeatable Projectile Spear Attack (Twister) to repeat several times and spends Frenzy Charges to repeat more. Sniper's Mark (a crit on the target) and Combat Frenzy (Freeze, Electrocute or Pin) generate the charges; Perpetual Charge and Heightened Charges make them go further.")],
   [L("4. Cores e Spirit", "4. Colours and Spirit"), L("Gem Studded (2º Trial) dá bônus pela cor de suporte mais comum: verde = menos penalidade de movimento, azul = skills 30% mais baratas, vermelho = hits sem dano crítico bônus contra você. Só conta o Weapon Set ativo. Spirit: 30, +30 (Ignagduk), +40 (Lythara); Enfolding Dawn dá +100 e Sacred Flame +138 no PoB.", "Gem Studded (2nd Trial) gives a bonus for the most common support colour: green = less movement penalty, blue = skills 30% cheaper, red = hits without critical bonus against you. It only counts the active Weapon Set. Spirit: 30, +30 (Ignagduk), +40 (Lythara); Enfolding Dawn gives +100 and Sacred Flame +138 in the PoB.")],
  ]),
  dict(type="rotation", blocks=[
   [L("Nível 1–15", "Levels 1–15"), [L("Whirling Slash quando o pack chega perto", "Whirling Slash when the pack gets close"), L("Twister dentro do redemoinho", "Twister inside the whirlwind"), L("Boss: Twister de longe; Whirling Slash para se afastar", "Boss: Twister from range; Whirling Slash to back off")]],
   [L("Nível 16+", "Level 16+"), [L("Pack: Infernal Cry → Whirling Slash → Twister", "Pack: Infernal Cry → Whirling Slash → Twister"), L("Boss: Sniper's Mark → (crítico) → Barrage → Twister repetido", "Boss: Sniper's Mark → (crit) → Barrage → repeated Twister"), L("Buffs sempre ligados; no endgame, Berserk quando a Rage estiver cheia", "Buffs always on; in endgame, Berserk once Rage is full")]],
  ]),
  dict(type="table", h=L("Weapon sets por fase", "Weapon sets per phase"), cols=[L("Fase", "Phase"), "Weapon Set 1", "Weapon Set 2"], rows=[
   [L("1–15", "1–15"), L("Spear branca: Whirling Slash e Twister", "White spear: Whirling Slash and Twister"), L("Vazio", "Empty")],
   [L("16–78", "16–78"), L("Skysliver: Whirling Slash, Twister, Barrage", "Skysliver: Whirling Slash, Twister, Barrage"), L("Vazio", "Empty")],
   [L("79+", "79+"), L("Spear (Armageddon Edge no PoB), off hand vazia", "Spear (the PoB's Armageddon Edge), empty off hand"), L("Spear (Mind Edge) + Sacred Flame", "Spear (Mind Edge) + Sacred Flame")],
   [L("Sempre", "Always"), L("Buffs persistentes nos dois sets", "Persistent buffs on both sets"), L("Buffs persistentes nos dois sets", "Persistent buffs on both sets")],
  ]),
  dict(type="spirit", h=L("Spirit dos buffs", "Buff Spirit"), p=L("Marque o que você usa. Custos do Path of Building.", "Tick what you use. Costs from Path of Building."),
       note=L("Ordem: Herald of Thunder → Wind Dancer → Combat Frenzy → Herald of Ice → Ghost Dance → Charge Regulation → Berserk → Trinity. Se faltar, desligue o último.", "Order: Herald of Thunder → Wind Dancer → Combat Frenzy → Herald of Ice → Ghost Dance → Charge Regulation → Berserk → Trinity. If short, turn off the last one.")),
  dict(type="timeline", h=L("Peças-chave por nível", "Key pieces by level"), items=[
   dict(lv=1, t="Whirling Slash + Twister", d=L("A build inteira desde o primeiro nível (spear no Set 1).", "The whole build from the first level (spear in Set 1).")),
   dict(lv=12, t="Herald of Thunder", d=L("Depois do King in the Mists (+30 Spirit).", "After King in the Mists (+30 Spirit).")),
   dict(lv=16, t="Skysliver + Barrage", d=L("Dano de raio e as repetições do Twister.", "Lightning damage and Twister's repeats.")),
   dict(lv=24, t="Sniper's Mark", d=L("Frenzy Charges para o Barrage.", "Frenzy Charges for Barrage.")),
   dict(lv=38, t="Wind Dancer", d=L("Ignagduk: +30 Spirit.", "Ignagduk: +30 Spirit.")),
   dict(lv=62, t="Combat Frenzy", d=L("Lythara: +40 Spirit.", "Lythara: +40 Spirit.")),
   dict(lv=75, t="Motoric Implants", d=L("+2 níveis em skills de Dex.", "+2 levels on Dex skills.")),
   dict(lv=79, t=L("Respec para a árvore do PoB", "Respec into the PoB tree"), d=L("Com Morior Invictus e Sacred Flame; as skills não mudam.", "With Morior Invictus and Sacred Flame; the skills don't change.")),
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
