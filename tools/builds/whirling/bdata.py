# -*- coding: utf-8 -*-
"""Mercenary · Gemling Legionnaire: Whirling Slash + Glacial Bolt (besta de gelo).

Fonte: WHIRLING Glacial Bolt Gemling [POE2 0.5] do Phylaris POE (Mobalytics, 13/08/2026): variantes Leveling / Endgame (Early) / Endgame, notas do autor e o PoB do endgame
(nível 97). O guia do autor tem UMA variante de leveling (87 pontos, sem ascendência); aqui ela é cortada em fases por pontos e cada fase ganha os níveis em que gems,
runas e itens ficam disponíveis (tiers do Path of Building, níveis e preços do poe.ninja). Onde o jogo pode variar o texto diz "confira no jogo"."""
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
 "pt": dict(TITLE="Ciclone de Gelo", DESC="Guia interativo Mercenary Gemling Legionnaire Whirling Glacial Bolt (besta de gelo, do nível 1 ao 100) — PoE 2 Forbidden Rites",
            H1S="Permafrost Bolts desde o nível 1 · Whirling Slash + Glacial Bolt no endgame · barato e forte em todos os níveis", H1="O Ciclone de Gelo",
            LEAD="Você congela tudo com a besta e estilhaça com o segundo botão: forte desde o Ato 1 com uma unique de graça. Diga seu nível e o que você já tem, e o guia mostra o que fazer agora, gema por gema, item por item, até o Whirling Glacial Bolt de endgame."),
 "en": dict(TITLE="Frost Cyclone", DESC="Interactive Mercenary Gemling Whirling Glacial Bolt guide (ice crossbow, level 1 to 100) — PoE 2 Forbidden Rites",
            H1S="Permafrost Bolts from level 1 · Whirling Slash + Glacial Bolt in endgame · cheap and strong at every level", H1="The Frost Cyclone",
            LEAD="You freeze everything with the crossbow and shatter it with the second button: strong from Act 1 with a nearly free unique. Tell it your level and what you already have, and the guide shows what to do now, gem by gem, item by item, up to the endgame Whirling Glacial Bolt."),
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
PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Permafrost Bolts + Fragmentation Rounds", "Permafrost Bolts + Fragmentation Rounds"),
  carry=L("Você: Permafrost Bolts → Fragmentation Rounds", "You: Permafrost Bolts → Fragmentation Rounds"), dmgSplit=[100, 0],
  goal=L("Do nível 1 você já tem a build inteira: as duas Uncut Skill Gems de nível 1, Permafrost Bolts e Fragmentation Rounds. Permafrost dispara balas de gelo que se fragmentam e Congelam quase tudo; a Fragmentation Rounds acerta o inimigo Congelado, gasta o Freeze e explode em estilhaços. Equipe a Rampart Raptor (Tense Crossbow, sem requisito de nível, quase de graça) com uma Lesser Glacial Rune. Limpar: só Permafrost. Boss: Permafrost até congelar, depois Fragmentation. Ponha uma skill em cada Weapon Set e dois botões de ataque básico, um para cada set: você alterna as balas sem trocar de arma.",
         "From level 1 you already have the whole build: the two level 1 Uncut Skill Gems, Permafrost Bolts and Fragmentation Rounds. Permafrost fires ice bolts that fragment and Freeze almost everything; Fragmentation Rounds hits the Frozen enemy, spends the Freeze and explodes into shrapnel. Equip the Rampart Raptor (Tense Crossbow, no level requirement, nearly free) with a Lesser Glacial Rune. Clearing: just Permafrost. Bosses: Permafrost until frozen, then Fragmentation. Put one skill in each Weapon Set and two basic attack buttons, one per set: you swap bolts without swapping weapons."),
  rotation=[L("Permafrost Bolts no pack até morrer", "Permafrost Bolts into the pack until it dies"), L("Boss: Permafrost até congelar", "Boss: Permafrost until frozen"), L("Boss congelado: Fragmentation Rounds (estilhaços)", "Frozen boss: Fragmentation Rounds (shrapnel)")],
  gems=[
   G("Permafrost Bolts", ["Rapid Attacks I", "Elemental Armament I", "Frozen Spite"], L("Limpar + Freeze", "Clear + Freeze"), L("Balas de gelo que se fragmentam e Congelam. Uncut Skill Gem nível 1: é a skill do nível 1 ao 75.", "Ice bolts that fragment and Freeze. Level 1 Uncut Skill Gem: it's your skill from level 1 to 75."), "free"),
   G("Fragmentation Rounds", ["Elemental Armament I", "Concentrated Area", "Close Combat I"], L("Estilhaçar", "Shatter"), L("Bala perfurante que consome o Freeze e explode; acertar um Ice Crystal também o explode. Uncut Skill Gem nível 1.", "A piercing bolt that consumes Freeze and explodes; hitting an Ice Crystal also explodes it. Level 1 Uncut Skill Gem."), "free"),
   G("Herald of Ice", ["Magnified Area II"], L("Explosão de gelo", "Ice explosion"), L("Matar (Shatter) inimigo Congelado solta uma explosão de gelo: encaixa com o Permafrost. Uncut nível 4, 30 Spirit: só depois do King in the Mists (+30 Spirit).", "Killing (Shattering) a Frozen enemy releases an ice explosion: it fits Permafrost. Level 4 Uncut, 30 Spirit: only after King in the Mists (+30 Spirit)."), "core", 1, SP30, since=12),
  ],
  cheap=["Rampart Raptor", "Tabula Rasa", "Blackheart", "Meginord's Girdle"],
  full=["Rampart Raptor", "Tabula Rasa", "Blackheart", "Meginord's Girdle"],
  stats=[L("Vida", "Life"), L("Resistência a fogo/frio/raio", "Fire/cold/lightning resistance"), L("Velocidade de ataque", "Attack speed")],
  tree=L("Dano de projétil no começo: Remorseless, Ricochet e Blur (+4% movimento). O caminho é o do autor: primeiro projétil, depois velocidade.", "Projectile damage early: Remorseless, Ricochet and Blur (+4% movement). It's the author's path: projectile first, then speed."),
  avoid=[L("Trocar de skill: a build do 1 ao 75 é Permafrost + Fragmentation", "Swapping skills: the build from 1 to 75 is Permafrost + Fragmentation"), L("Gastar currency em item que sobe de nível logo", "Spending currency on an item you'll outlevel soon")],
  exit=[L("King in the Mists (~10): +30 Spirit → Herald of Ice", "King in the Mists (~10): +30 Spirit → Herald of Ice"), L("Nível 11: Wanderlust (botas)", "Level 11: Wanderlust (boots)")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 31], tag=L("Herald de gelo + botas e elmo baratos", "Ice Herald + cheap boots and helmet"),
  carry=L("Você: Permafrost Bolts → Fragmentation Rounds", "You: Permafrost Bolts → Fragmentation Rounds"), dmgSplit=[100, 0],
  goal=L("Nada muda nas skills: você só fica mais forte. Herald of Ice roda o tempo todo (30 Spirit), os suportes sobem para as versões II (Elemental Armament II, Rapid Attacks II, Close Combat II) e o 1º Trial (~28) libera a Essence of Virtue (defesa). Itens: Wanderlust no 11 (20% de movimento) e Thrillsteel no 27 (capacete, quase de graça). No 30, troque a Lesser pela Greater Glacial Rune na Rampart Raptor e suba os anéis para rares com dano adicionado e resistência (~30 e ~50). No 24 caem duas gems para guardar: Freezing Mark (boss) e Glacial Bolt (a skill do endgame).",
         "Skills don't change: you just get stronger. Herald of Ice runs all the time (30 Spirit), supports rise to the II versions (Elemental Armament II, Rapid Attacks II, Close Combat II) and the 1st Trial (~28) unlocks Essence of Virtue (defence). Items: Wanderlust at 11 (20% movement) and Thrillsteel at 27 (helmet, nearly free). At 30, swap the Lesser for the Greater Glacial Rune on the Rampart Raptor and upgrade the rings to rares with added damage and resistance (~30 and ~50). At 24 two gems drop that you should keep: Freezing Mark (bosses) and Glacial Bolt (the endgame skill)."),
  rotation=[L("Permafrost Bolts no pack", "Permafrost Bolts on the pack"), L("Boss: Freezing Mark → Permafrost até congelar", "Boss: Freezing Mark → Permafrost until frozen"), L("Fragmentation Rounds no boss congelado", "Fragmentation Rounds on the frozen boss")],
  gems=[
   G("Permafrost Bolts", ["Elemental Armament II", "Rapid Attacks II", "Frozen Spite"], L("Limpar + Freeze", "Clear + Freeze"), L("Mesma skill, suportes melhores (tier 2 e 4).", "Same skill, better supports (tier 2 and 4)."), "free"),
   G("Fragmentation Rounds", ["Elemental Armament II", "Concentrated Area", "Deliberation", "Close Combat II"], L("Estilhaçar", "Shatter"), L("Close Combat II e Deliberation somam dano de perto.", "Close Combat II and Deliberation add close-range damage."), "free", since=16),
   G("Herald of Ice", ["Magnified Area II", "Elemental Focus"], L("Explosão de gelo", "Ice explosion"), L("30 Spirit (King in the Mists).", "30 Spirit (King in the Mists)."), "core", 1, SP30),
   G("Freezing Mark", ["Eternal Mark"], L("Boss", "Boss"), L("Marca o alvo: quando ele Congela, você ganha dano de frio extra. Uncut Skill Gem nível 7.", "Marks the target: when it Freezes, you gain extra cold damage. Level 7 Uncut Skill Gem."), "free", since=24),
  ],
  cheap=["Wanderlust", "Thrillsteel", "Rampart Raptor"],
  full=["Wanderlust", "Thrillsteel", "Tabula Rasa"],
  stats=[L("Vida", "Life"), L("Resistências", "Resistances"), L("Velocidade de ataque", "Attack speed")],
  tree=L("Heavy Ammunition (+40% dano de projétil), Careful Aim e Adrenaline Rush (velocidade ao matar): dano e ritmo.", "Heavy Ammunition (+40% projectile damage), Careful Aim and Adrenaline Rush (speed on kill): damage and rhythm."),
  avoid=[L("Ligar o Herald sem ter os 30 Spirit livres", "Turning on Herald without the 30 Spirit free"), L("Comprar item de nível alto antes de precisar", "Buying a high-level item before you need it")],
  exit=[L("1º Trial (~28): Essence of Virtue", "1st Trial (~28): Essence of Virtue"), L("Greater Glacial Rune no 30 e anéis rares", "Greater Glacial Rune at 30 and rare rings")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[32, 45], tag=L("War Banner e a Rampart Raptor forjada", "War Banner and the runeforged Rampart Raptor"),
  carry=L("Você: Permafrost Bolts → Fragmentation Rounds", "You: Permafrost Bolts → Fragmentation Rounds"), dmgSplit=[100, 0],
  goal=L("Nível 38 é a virada de itens: compre uma Rampart Raptor Runeforged (custa quase nada) e as botas Wanderlust também na versão forjada; o Ignagduk (Azak Bog, ~38) dá mais 30 Spirit e paga o War Banner (t4, 30 Spirit). Com o Freezing Mark completo (Mark for Death II, Mark of Siphoning II, Charged Mark, Eternal Mark) e o Emergency Reload no 40 (recarrega o pente e reforça as balas), o boss congela e cai. 2º Trial (~40): Gem Studded, que dá bônus pela cor mais comum entre seus suportes.",
         "Level 38 is the item turning point: buy a Runeforged Rampart Raptor (costs almost nothing) and the Wanderlust boots in the forged version too; Ignagduk (Azak Bog, ~38) gives 30 more Spirit and pays for War Banner (t4, 30 Spirit). With the full Freezing Mark (Mark for Death II, Mark of Siphoning II, Charged Mark, Eternal Mark) and Emergency Reload at 40 (reloads the clip and empowers the bolts), the boss freezes and falls. 2nd Trial (~40): Gem Studded, which gives a bonus for the most common colour among your supports."),
  rotation=[L("Herald de gelo e War Banner sempre ligados", "Ice Herald and War Banner always on"), L("Permafrost no pack; Emergency Reload quando o pente acabar", "Permafrost on the pack; Emergency Reload when the clip runs out"), L("Boss: Freezing Mark → Permafrost até congelar → Fragmentation", "Boss: Freezing Mark → Permafrost until frozen → Fragmentation")],
  gems=[
   G("Permafrost Bolts", ["Elemental Armament II", "Rapid Attacks II", "Frozen Spite"], L("Limpar + Freeze", "Clear + Freeze"), L("Sem mudança nos suportes.", "No support changes."), "free"),
   G("Fragmentation Rounds", ["Elemental Armament II", "Concentrated Area", "Deliberation", "Close Combat II"], L("Estilhaçar", "Shatter"), L("Sem mudança nos suportes.", "No support changes."), "free"),
   G("Herald of Ice", ["Magnified Area II", "Elemental Focus"], L("Explosão de gelo", "Ice explosion"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("War Banner", ["Expanse", "Prolonged Duration II"], L("Buff de ataque", "Attack buff"), L("Ao atacar você acumula Glory; no máximo, planta um Banner que dá dano, velocidade e Accuracy. Uncut nível 4, 30 Spirit (Ignagduk).", "Attacking builds Glory; at maximum you plant a Banner that grants damage, speed and Accuracy. Level 4 Uncut, 30 Spirit (Ignagduk)."), "core", 2, SP30, since=38),
   G("Freezing Mark", ["Mark for Death II", "Mark of Siphoning II", "Charged Mark", "Eternal Mark"], L("Boss", "Boss"), L("Quatro suportes: o Mark dura, dá mana e deixa o chão Shocked.", "Four supports: the Mark lasts, gives mana and leaves the ground Shocked."), "free"),
   G("Emergency Reload", ["Cooldown Recovery II", "Prolonged Duration II"], L("Recarga", "Reload"), L("Recarrega todos os pentes na hora e reforça as balas por um tempo. Uncut nível 11.", "Reloads every clip instantly and empowers the bolts for a while. Level 11 Uncut."), "free", since=40),
  ],
  cheap=["Rampart Raptor", "Wanderlust", "Thrillsteel"],
  full=["Rampart Raptor", "Wanderlust", "Thrillsteel", "Tabula Rasa"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Velocidade de ataque", "Attack speed"), L("Dano de projétil", "Projectile damage")],
  tree=L("Honed Instincts (velocidade de ataque e de projétil), Vile Wounds (+33% contra alvos com ailment — o Freeze conta), Clean Shot e Colossal Weapon.", "Honed Instincts (attack and projectile speed), Vile Wounds (+33% against ailed targets — Freeze counts), Clean Shot and Colossal Weapon."),
  avoid=[L("Ligar Herald + Banner com menos de 60 Spirit", "Turning on Herald + Banner with less than 60 Spirit"), L("Esquecer de forjar a Rampart Raptor no 38", "Forgetting to runeforge the Rampart Raptor at 38")],
  exit=[L("Rampart Raptor Runeforged (38)", "Runeforged Rampart Raptor (38)"), L("Ignagduk: +30 Spirit → War Banner", "Ignagduk: +30 Spirit → War Banner")]),

 dict(id="a4", name=L("Ato 4 e Interlúdios", "Act 4 and Interludes"), lv=[46, 64], tag=L("Runemastered e Scavenged Plating", "Runemastered and Scavenged Plating"),
  carry=L("Você: Permafrost Bolts → Fragmentation Rounds", "You: Permafrost Bolts → Fragmentation Rounds"), dmgSplit=[100, 0],
  goal=L("Os itens sobem de faixa: Thrillsteel Runemastered (40), anéis rares melhores (~50) e a Rampart Raptor Runemastered no 55 (~2 Divines, opcional — a Runeforged aguenta). O Lythara (Kriar Village, ~62) dá +40 Spirit: com 100 de Spirit você ganha o Scavenged Plating (t4, 30 Spirit), que bloqueia dano quando você quebra a Armour do inimigo. A árvore chega a Rapid Reload (+40% de recarga) e Forces of Nature (penetração elemental).",
         "Items move up a tier: Runemastered Thrillsteel (40), better rare rings (~50) and the Runemastered Rampart Raptor at 55 (~2 Divines, optional — the Runeforged holds up). Lythara (Kriar Village, ~62) gives +40 Spirit: with 100 Spirit you get Scavenged Plating (t4, 30 Spirit), which fortifies you when you break enemy Armour. The tree reaches Rapid Reload (+40% reload) and Forces of Nature (elemental penetration)."),
  rotation=[L("Herald, War Banner e Plating sempre ligados", "Herald, War Banner and Plating always on"), L("Permafrost no pack; Emergency Reload no pente vazio", "Permafrost on the pack; Emergency Reload on an empty clip"), L("Boss: Freezing Mark → Permafrost → Fragmentation", "Boss: Freezing Mark → Permafrost → Fragmentation")],
  gems=[
   G("Permafrost Bolts", ["Elemental Armament II", "Rapid Attacks II", "Frozen Spite"], L("Limpar + Freeze", "Clear + Freeze"), L("Sem mudança.", "No change."), "free"),
   G("Fragmentation Rounds", ["Elemental Armament II", "Concentrated Area", "Deliberation", "Close Combat II"], L("Estilhaçar", "Shatter"), L("Sem mudança.", "No change."), "free"),
   G("Herald of Ice", ["Magnified Area II", "Elemental Focus"], L("Explosão de gelo", "Ice explosion"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("War Banner", ["Expanse", "Prolonged Duration II"], L("Buff de ataque", "Attack buff"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Scavenged Plating", ["Prolonged Duration II"], L("Defesa", "Defence"), L("Quebrar a Armour de um inimigo dá stacks de Armour e Thorns. Tier 4, 30 Spirit (Lythara).", "Breaking an enemy's Armour grants Armour and Thorns stacks. Tier 4, 30 Spirit (Lythara)."), "core", 3, SP30, since=62),
   G("Freezing Mark", ["Mark for Death II", "Mark of Siphoning II", "Charged Mark", "Eternal Mark"], L("Boss", "Boss"), L("Sem mudança.", "No change."), "free"),
   G("Emergency Reload", ["Cooldown Recovery II", "Prolonged Duration II"], L("Recarga", "Reload"), L("Sem mudança.", "No change."), "free"),
  ],
  cheap=["Thrillsteel", "Rampart Raptor", "Wanderlust"],
  full=["Rampart Raptor", "Thrillsteel", "Wanderlust", "Tabula Rasa"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Velocidade de ataque e recarga", "Attack speed and reload"), L("Spirit", "Spirit")],
  tree=L("Rapid Reload (+40% de recarga), Crystal Elixir (+40% dano elemental durante flask), Emboldened Avatar (+25% Freeze buildup), Short Shot e Forces of Nature.", "Rapid Reload (+40% reload), Crystal Elixir (+40% elemental damage during a flask), Emboldened Avatar (+25% Freeze buildup), Short Shot and Forces of Nature."),
  avoid=[L("Ficar sem Spirit para o Plating (precisa dos 100 do Lythara)", "Running short of Spirit for Plating (it needs Lythara's 100)"), L("Pagar 2 Divines na Rampart antes de fechar resistências", "Paying 2 Divines for the Rampart before resistances are capped")],
  exit=[L("3º Trial (~65): Advanced Thaumaturgy", "3rd Trial (~65): Advanced Thaumaturgy"), L("Rampart Raptor Runemastered (55)", "Runemastered Rampart Raptor (55)")]),

 dict(id="maps", name=L("Mapas 65+", "Maps 65+"), lv=[65, 78], tag=L("Mesma build, árvore completa e caixa de guerra", "Same build, full tree and war chest"),
  carry=L("Você: Permafrost Bolts → Fragmentation Rounds", "You: Permafrost Bolts → Fragmentation Rounds"), dmgSplit=[100, 0],
  goal=L("Nos primeiros mapas a build continua a mesma — ela ainda é forte — e o trabalho é juntar dinheiro para o endgame. A árvore de Leveling do autor fecha os 87 pontos (Pressure Points: +35% Freeze buildup; Acceleration; Run and Gun) e os pontos que sobram esperam o respec. Prepare a troca do nível 79: um Skysliver (Winged Spear, nível 16, ~0,1 Divine) para a Whirling Slash, uma Desolate Crossbow boa para o Glacial Bolt, e o Morior Invictus (nível 65, ~6 Divines). Sem essas peças, não troque: a build de Permafrost segue firme.",
         "In the first maps the build stays the same — it's still strong — and the job is saving money for endgame. The author's Leveling tree closes its 87 points (Pressure Points: +35% Freeze buildup; Acceleration; Run and Gun) and the leftover points wait for the respec. Prepare the level 79 switch: a Skysliver (Winged Spear, level 16, ~0.1 Divine) for Whirling Slash, a good Desolate Crossbow for Glacial Bolt, and Morior Invictus (level 65, ~6 Divines). Without those pieces, don't switch: the Permafrost build is still solid."),
  rotation=[L("Buffs sempre ligados", "Buffs always on"), L("Permafrost no pack", "Permafrost on the pack"), L("Boss: Freezing Mark → Permafrost → Fragmentation", "Boss: Freezing Mark → Permafrost → Fragmentation")],
  gems=[
   G("Permafrost Bolts", ["Elemental Armament II", "Rapid Attacks III", "Frozen Spite"], L("Limpar + Freeze", "Clear + Freeze"), L("Rapid Attacks III (tier 5) no lugar do II.", "Rapid Attacks III (tier 5) instead of II."), "free"),
   G("Fragmentation Rounds", ["Elemental Armament II", "Concentrated Area", "Deliberation", "Close Combat II"], L("Estilhaçar", "Shatter"), L("Sem mudança.", "No change."), "free"),
   G("Herald of Ice", ["Magnified Area II", "Elemental Focus"], L("Explosão de gelo", "Ice explosion"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("War Banner", ["Expanse", "Prolonged Duration II"], L("Buff de ataque", "Attack buff"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Scavenged Plating", ["Prolonged Duration II"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Freezing Mark", ["Mark for Death II", "Mark of Siphoning II", "Charged Mark", "Eternal Mark"], L("Boss", "Boss"), L("Sem mudança.", "No change."), "free"),
   G("Emergency Reload", ["Cooldown Recovery II", "Prolonged Duration II"], L("Recarga", "Reload"), L("Sem mudança.", "No change."), "free"),
  ],
  cheap=["Skysliver", "Rampart Raptor", "Thrillsteel"],
  full=["Skysliver", "Morior Invictus", "Rampart Raptor"],
  stats=[L("Vida e resistências", "Life and resistances"), L("Velocidade de ataque", "Attack speed"), L("Armour", "Armour")],
  tree=L("Fecha os 87 pontos da árvore de Leveling: Spray and Pray, Run and Gun, Pressure Points (+35% Freeze buildup) e Acceleration.", "Closes the 87 points of the Leveling tree: Spray and Pray, Run and Gun, Pressure Points (+35% Freeze buildup) and Acceleration."),
  avoid=[L("Trocar para a Whirling Slash sem spear e sem o Glacial Bolt no nível 14+", "Switching to Whirling Slash without a spear and a level 14+ Glacial Bolt"), L("Comprar o Morior Invictus antes das resistências", "Buying Morior Invictus before resistances")],
  exit=[L("4º Trial (~75): Motoric Implants (+2 níveis nas skills de Dex)", "4th Trial (~75): Motoric Implants (+2 levels on Dex skills)"), L("Skysliver + Desolate Crossbow + Morior Invictus", "Skysliver + Desolate Crossbow + Morior Invictus")]),

 dict(id="endgame", name=L("Endgame (Early) 79+", "Endgame (Early) 79+"), lv=[79, 90], tag=L("Whirling Slash + Glacial Bolt", "Whirling Slash + Glacial Bolt"),
  carry=L("Você: Whirling Slash → Glacial Bolt", "You: Whirling Slash → Glacial Bolt"), dmgSplit=[100, 0],
  goal=L("Agora a build vira a do autor. Weapon Set 1: spear (Skysliver) com Whirling Slash — você anda girando, Desacelera e Cega os inimigos e o giro quebra os Ice Crystals do Glacial Bolt. Weapon Set 2: besta com Glacial Bolt (duas paredes de Ice Crystals), Emergency Reload e Herald of Thunder. Você troca de set no mesmo botão do movimento. Morior Invictus dá Armour e vida por socket; Iron Reflexes converte Evasion em Armour; o Scavenged Plating e a Arctic Armour seguram o dano de perto. É o setup 'Endgame (Early)' do autor, sem os suportes de Lineage caros.",
         "Now the build becomes the author's. Weapon Set 1: spear (Skysliver) with Whirling Slash — you move while spinning, Slow and Blind enemies, and the spin breaks Glacial Bolt's Ice Crystals. Weapon Set 2: crossbow with Glacial Bolt (two walls of Ice Crystals), Emergency Reload and Herald of Thunder. You swap sets on the movement button. Morior Invictus gives Armour and life per socket; Iron Reflexes converts Evasion to Armour; Scavenged Plating and Arctic Armour hold up close-range damage. It's the author's 'Endgame (Early)' setup, without the expensive Lineage supports."),
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
  tree=L("Respec para a árvore Endgame (Early) do autor: 85 pontos + 30 do Weapon Set 1 + 31 do Set 2. Iron Reflexes, Battle Trance (+8 Rage máxima), Dance with Death, Authority e Sand in the Eyes.", "Respec to the author's Endgame (Early) tree: 85 points + 30 on Weapon Set 1 + 31 on Set 2. Iron Reflexes, Battle Trance (+8 maximum Rage), Dance with Death, Authority and Sand in the Eyes."),
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
 "a1": ("2", [L("Permafrost", "Permafrost"), "Fragmentation"], L("Uma bala congela, a outra estilhaça: dois botões, dois Weapon Sets.", "One bolt freezes, the other shatters: two buttons, two Weapon Sets.")),
 "a2": ("2", ["Permafrost", "Fragmentation"], L("Mesmas duas balas; agora o Freezing Mark abre o boss.", "The same two bolts; now Freezing Mark opens the boss.")),
 "a3": ("2", ["Permafrost", "Fragmentation"], L("O Emergency Reload recarrega o pente sem parar de atirar.", "Emergency Reload reloads the clip without stopping.")),
 "a4": ("2", ["Permafrost", "Fragmentation"], L("Três reservas de Spirit (Herald, Banner, Plating) somam 90 dos 100.", "Three Spirit reservations (Herald, Banner, Plating) use 90 of the 100.")),
 "maps": ("2", ["Permafrost", "Fragmentation"], L("Sem pressa para trocar: a troca só vale com spear, besta e Morior prontos.", "No rush to switch: it only pays off with spear, crossbow and Morior ready.")),
 "endgame": ("2", ["Whirling Slash", "Glacial Bolt"], L("A spear gira e quebra o gelo que a besta planta.", "The spear spins and breaks the ice the crossbow plants.")),
 "max": ("2", ["Whirling Slash", "Glacial Bolt"], L("Igual, com suportes de Lineage e Blasphemy.", "Same, with Lineage supports and Blasphemy.")),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in {"a1": L("Nenhuma reserva ainda: o Herald de Gelo espera o King in the Mists (+30 Spirit).", "No reservation yet: Ice Herald waits for King in the Mists (+30 Spirit)."),
                  "a3": L("Herald (30) + War Banner (30) = 60 Spirit (King in the Mists + Ignagduk).", "Herald (30) + War Banner (30) = 60 Spirit (King in the Mists + Ignagduk)."),
                  "a4": L("Herald + Banner + Plating = 90 dos 100 Spirit (com o Lythara).", "Herald + Banner + Plating = 90 of 100 Spirit (with Lythara)."),
                  "endgame": L("Plating 30 + Arctic Armour 30 + Verisium 30 + Berserk 30 = 120: o Morior Invictus dá +13 Spirit por socket cheio.", "Plating 30 + Arctic Armour 30 + Verisium 30 + Berserk 30 = 120: Morior Invictus gives +13 Spirit per filled socket."),
                  "max": L("Trinity reserva 100 de Spirit e o Blasphemy também reserva: só com amuleto de Spirit alto (por isso a variante Early corta os dois).", "Trinity reserves 100 Spirit and Blasphemy reserves too: only with a high-Spirit amulet (that's why the Early variant cuts both).")}.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Permafrost Bolts + Fragmentation Rounds (Uncut nível 1) e a Rampart Raptor com Lesser Glacial Rune.", "Permafrost Bolts + Fragmentation Rounds (level 1 Uncut) and the Rampart Raptor with a Lesser Glacial Rune."),
 4: L("Frozen Spite e Elemental Armament II nos suportes.", "Frozen Spite and Elemental Armament II on the supports."),
 10: L("King in the Mists: +30 Spirit.", "King in the Mists: +30 Spirit."),
 11: L("Wanderlust (botas, 20% de movimento).", "Wanderlust (boots, 20% movement)."),
 12: L("Herald of Ice (Uncut nível 4, 30 Spirit) e Rapid Attacks II.", "Herald of Ice (level 4 Uncut, 30 Spirit) and Rapid Attacks II."),
 16: L("Close Combat II na Fragmentation.", "Close Combat II on Fragmentation."),
 24: L("Freezing Mark e Glacial Bolt (Uncut nível 7): guarde o Glacial Bolt.", "Freezing Mark and Glacial Bolt (level 7 Uncut): keep the Glacial Bolt."),
 27: L("Thrillsteel (capacete).", "Thrillsteel (helmet)."),
 28: L("1º Trial: Essence of Virtue.", "1st Trial: Essence of Virtue."),
 30: L("Greater Glacial Rune na Rampart Raptor; anéis rares (~30 e ~50).", "Greater Glacial Rune on the Rampart Raptor; rare rings (~30 and ~50)."),
 38: L("Rampart Raptor Runeforged (e Wanderlust forjada); Ignagduk: +30 Spirit → War Banner.", "Runeforged Rampart Raptor (and forged Wanderlust); Ignagduk: +30 Spirit → War Banner."),
 40: L("2º Trial: Gem Studded. Emergency Reload (Uncut nível 11). Thrillsteel Runemastered.", "2nd Trial: Gem Studded. Emergency Reload (level 11 Uncut). Runemastered Thrillsteel."),
 50: L("Anéis rares melhores.", "Better rare rings."),
 55: L("Rampart Raptor Runemastered (~2 Divines, opcional).", "Runemastered Rampart Raptor (~2 Divines, optional)."),
 62: L("Lythara: +40 Spirit → Scavenged Plating.", "Lythara: +40 Spirit → Scavenged Plating."),
 65: L("3º Trial: Advanced Thaumaturgy. Morior Invictus fica disponível.", "3rd Trial: Advanced Thaumaturgy. Morior Invictus becomes available."),
 75: L("4º Trial: Motoric Implants (+2 níveis nas skills de Dex).", "4th Trial: Motoric Implants (+2 levels on Dex skills)."),
 79: L("Troca para o Endgame (Early): Skysliver + Whirling Slash e Desolate Crossbow + Glacial Bolt.", "Switch to Endgame (Early): Skysliver + Whirling Slash and Desolate Crossbow + Glacial Bolt."),
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
 dict(node="Remorseless", type="Notable", text=L("+15% de dano de projétil, +30% de Stun buildup contra inimigos a menos de 2 m, +5 Força.", "+15% projectile damage, +30% Stun buildup against enemies within 2 m, +5 Strength."), when=L("Ato 1 → sempre", "Act 1 → forever"), why=L("Primeiro dano de projétil da árvore do autor.", "The first projectile damage on the author's tree.")),
 dict(node="Heavy Ammunition", type="Notable", text=L("+40% de dano de projétil e de Stun buildup de projétil; −5% de velocidade de ataque.", "+40% projectile damage and projectile Stun buildup; −5% attack speed."), when=L("Ato 2 → sempre", "Act 2 → forever"), why=L("O maior dano de projétil do começo; a velocidade volta com Honed Instincts.", "The biggest early projectile damage; speed comes back with Honed Instincts.")),
 dict(node="Vile Wounds", type="Notable", text=L("+33% de dano com hits contra inimigos afetados por ailments.", "+33% damage with hits against enemies affected by ailments."), when=L("Ato 3 → sempre", "Act 3 → forever"), why=L("Tudo o que você acerta está Congelado: o bônus está sempre ligado.", "Everything you hit is Frozen: the bonus is always on.")),
 dict(node="Rapid Reload", type="Notable", text=L("+40% de velocidade de recarga da besta.", "+40% crossbow reload speed."), when=L("Ato 4 → sempre", "Act 4 → forever"), why=L("A Rampart Raptor tem −30% de recarga: este nó compensa e mantém o pente cheio.", "The Rampart Raptor has −30% reload: this node compensates and keeps the clip full.")),
 dict(node="Forces of Nature", type="Notable", text=L("Dano de ataque penetra 15% das resistências elementais do inimigo.", "Attack damage penetrates 15% of enemy elemental resistances."), when=L("Ato 4 → sempre", "Act 4 → forever"), why=L("Todo o seu dano é elemental (gelo).", "All your damage is elemental (cold).")),
 dict(node="Pressure Points", type="Notable", text=L("+35% de Stun buildup e +35% de Freeze buildup.", "+35% Stun buildup and +35% Freeze buildup."), when=L("Mapas → sempre", "Maps → forever"), why=L("Mais Freeze = mais estilhaços.", "More Freeze = more shrapnel.")),
 dict(node="Iron Reflexes", type="Keystone", text=L("Converte toda a Evasion em Armour.", "Converts all Evasion Rating to Armour."), when=L("Endgame", "Endgame"), why=L("O Morior Invictus e as peças de Armour transformam isso em 100 mil de Armour no PoB.", "Morior Invictus and the Armour pieces turn this into 100k Armour in the PoB.")),
 dict(node="Battle Trance", type="Notable", text=L("+8 de Rage máxima.", "+8 maximum Rage."), when=L("Endgame", "Endgame"), why=L("A Whirling Slash gera Rage: mais teto de Rage, mais dano.", "Whirling Slash generates Rage: a higher Rage cap, more damage.")),
]
TREE_STAGES = [
 dict(lv="1–15", focus=L("Dano de projétil e movimento", "Projectile damage and movement"), dmg="Permafrost + Fragmentation", **{"def": L("Vida", "Life")}, spirit="—", dont=L("Pegar Atributo demais", "Taking too much Attribute")),
 dict(lv="16–45", focus=L("Projétil, velocidade e Vile Wounds", "Projectile, speed and Vile Wounds"), dmg="Permafrost + Fragmentation", **{"def": L("Vida e resistências", "Life and resistances")}, spirit="Herald · Banner", dont=L("Esquecer o Rapid Reload depois", "Forgetting Rapid Reload later")),
 dict(lv="46–78", focus=L("Recarga, penetração e Freeze", "Reload, penetration and Freeze"), dmg="Permafrost + Fragmentation", **{"def": L("Armour (Plating)", "Armour (Plating)")}, spirit="Herald · Banner · Plating", dont=L("Respec cedo demais", "Respeccing too early")),
 dict(lv="79–100", focus=L("Árvore do autor com Weapon Sets", "The author's tree with Weapon Sets"), dmg="Whirling Slash + Glacial Bolt", **{"def": L("Iron Reflexes + Armour", "Iron Reflexes + Armour")}, spirit="Plating · Arctic · Verisium · Berserk", dont=L("Perder o requisito de Dex", "Losing the Dex requirement")),
]

UNIQUES = [
 U("Rampart Raptor", L("Besta", "Crossbow"), L("Arma", "Weapon"), "a1", L("+40–60% de dano elemental, +30–40% de velocidade de ataque, −30% de recarga e 100% de chance de não gastar munição se você recarregou há pouco.", "+40–60% elemental damage, +30–40% attack speed, −30% reload and a 100% chance not to expend ammo if you've reloaded recently."), L("Do nível 1 ao 75 é a sua arma: Tense Crossbow sem requisito de nível (~0,005 Divine); Runeforged no 38 (~0,01), Runemastered no 55 (~2 Divines).", "From level 1 to 75 it's your weapon: Tense Crossbow with no level requirement (~0.005 Divine); Runeforged at 38 (~0.01), Runemastered at 55 (~2 Divines)."), L("Besta rare com dano elemental e velocidade.", "A rare crossbow with elemental damage and speed."), 1),
 U("Tabula Rasa", "Body Armour", L("Armadura", "Armour"), "a1", L("Corpo com muitos sockets e sem defesa própria: você enche de runas de dano.", "A body with many sockets and no defences of its own: you fill it with damage runes."), L("Custa ~0,5 Divine. Qualquer mistura de runas de projétil, ataque, elemental e besta (autor).", "Costs ~0.5 Divine. Any mix of projectile, attack, elemental and crossbow runes (author)."), L("Body normal com vida e resistências.", "A normal body with life and resistances."), 1),
 U("Blackheart", "Ring", L("Acessório", "Accessory"), "a1", L("Regeneração de vida, dano adicionado a ataques e dano também aplicado como caos.", "Life regeneration, added attack damage and damage also applied as chaos."), L("Dois anéis por ~0,01 Divine. Troque por rares com dano adicionado e resistência no ~30 e no ~50.", "Two rings for ~0.01 Divine. Swap them for rares with added damage and resistance at ~30 and ~50."), L("Anel rare de dano e resistência.", "A rare ring with damage and resistance."), 1),
 U("Meginord's Girdle", L("Cinto", "Belt"), L("Acessório", "Accessory"), "a1", L("+40–50 de Força, +10–15% de resistência a frio e muito mais cargas de flask.", "+40–50 Strength, +10–15% cold resistance and far more flask charges."), L("Nível 0, quase de graça.", "Level 0, nearly free."), L("Cinto com vida e resistências.", "A belt with life and resistances."), 1),
 U("Wanderlust", L("Botas", "Boots"), L("Armadura", "Armour"), "a2", L("+20% de velocidade de movimento, ES e imunidade à lentidão.", "+20% movement speed, ES and immunity to Slow."), L("Nível 11 (Wrapped Sandals); a versão Runemastered pede nível 38.", "Level 11 (Wrapped Sandals); the Runemastered version needs level 38."), L("Botas com movimento.", "Boots with movement."), 11),
 U("Thrillsteel", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a2", L("Capacete de Força e vida para a fase de leveling.", "A Strength helmet with life for the leveling phase."), L("Nível 27 (Spired Greathelm, ~0,03 Divine); Runemastered no 40.", "Level 27 (Spired Greathelm, ~0.03 Divine); Runemastered at 40."), L("Capacete rare de vida.", "A rare life helmet."), 27),
 U("Skysliver", "Spear", L("Arma", "Weapon"), "maps", L("Adiciona dano de raio, velocidade de ataque e chance de crítico; só rola o mínimo ou o máximo de dano.", "Adds lightning damage, attack speed and crit chance; rolls only the minimum or maximum damage."), L("Serve para a Whirling Slash: nível 16 (~0,1 Divine) ou Runeforged no 40. Se o jogo disser que precisa remover Pounce, arraste a spear para o slot de offhand.", "It's for Whirling Slash: level 16 (~0.1 Divine) or Runeforged at 40. If the game says you must remove Pounce, drag the spear to the offhand slot."), L("Spear rare com velocidade.", "A rare spear with speed."), 16),
 U("Morior Invictus", "Body Armour", L("Armadura", "Armour"), "endgame", L("+300–400% de Armour, Evasion e ES e bônus por socket cheio: vida, mana, atributos, resistência a caos e Spirit.", "+300–400% Armour, Evasion and ES and bonuses per filled socket: life, mana, attributes, chaos resistance and Spirit."), L("Nível 65, ~6 Divines. É a peça que faz a Armour e o Spirit do endgame.", "Level 65, ~6 Divines. It's the piece that provides endgame Armour and Spirit."), L("Body de Armour com vida.", "An Armour body with life."), 65),
 U("Lavianga's Spirits", "Flask", "Flask", "endgame", L("O flask não pode ser usado: o efeito de mana fica sempre ativo (73% menos recuperado).", "The flask cannot be used: the mana effect is always active (73% less recovered)."), L("Mana constante sem apertar nada (~0,1 Divine, nível 49).", "Constant mana without pressing anything (~0.1 Divine, level 49)."), L("Flask de mana normal.", "A regular mana flask."), 49),
 U("Rite of Passage", "Charm", "Charm", "max", L("Ao matar um Rare ou Unique, você fica possuído por espíritos animais (o autor usa o Lobo: velocidade de ataque).", "On killing a Rare or Unique you're possessed by animal spirits (the author uses the Wolf: attack speed)."), L("Luxo (~15 Divines).", "Luxury (~15 Divines)."), L("Golden Charm normal.", "A regular Golden Charm."), 50),
 U("Headhunter", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Ao matar um Rare você ganha os modificadores dele por 60 s.", "On killing a Rare you gain its modifiers for 60 s."), L("Cinto da variante Early do autor (~246 Divines).", "Belt of the author's Early variant (~246 Divines)."), L("Cinto de vida e Armour.", "A life and Armour belt."), 50),
 U("Mageblood", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Efeitos de flask permanentes.", "Permanent flask effects."), L("O cinto do PoB final (~570 Divines): só no fim.", "The final PoB's belt (~570 Divines): only at the very end."), L("Cinto com vida.", "A belt with life."), 55),
]
GEAR = [
 dict(slot=L("Besta (Set 1/2)", "Crossbow (Set 1/2)"), cheap=L("Rampart Raptor (Tense → Runeforged 38 → Runemastered 55)", "Rampart Raptor (Tense → Runeforged 38 → Runemastered 55)"), value=L("Desolate Crossbow rare com + níveis de Attack e dano elemental", "Rare Desolate Crossbow with + Attack levels and elemental damage"), full=L("Desolate Crossbow: +3 níveis de Attack, dano de fogo e raio adicionados", "Desolate Crossbow: +3 Attack levels, added fire and lightning damage"), affix=L("+ níveis de Attack; dano elemental adicionado; velocidade", "+ Attack levels; added elemental damage; speed"), note=""),
 dict(slot=L("Spear (Set 1)", "Spear (Set 1)"), cheap=L("Nada até o 79", "Nothing until 79"), value="Skysliver", full=L("Rune Edge/Skysliver com Soul Cores de velocidade", "Rune Edge/Skysliver with speed Soul Cores"), affix=L("Velocidade de ataque; dano elemental", "Attack speed; elemental damage"), note=L("Só para a Whirling Slash", "Only for Whirling Slash")),
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
BUY_ORDER = [
 dict(p=1, item="Rampart Raptor + Lesser Glacial Rune", phase=L("Nível 1", "Level 1"), cost=L("Barato", "Cheap"), impact=L("A build inteira: dano e velocidade", "The whole build: damage and speed")),
 dict(p=2, item="Tabula Rasa", phase=L("Ato 1", "Act 1"), cost=L("Barato", "Cheap"), impact=L("Sockets para runas de dano", "Sockets for damage runes")),
 dict(p=3, item="Wanderlust + Thrillsteel", phase=L("Ato 2", "Act 2"), cost=L("Barato", "Cheap"), impact=L("Movimento e vida", "Movement and life")),
 dict(p=4, item=L("Rampart Raptor Runeforged", "Runeforged Rampart Raptor"), phase=L("Nível 38", "Level 38"), cost=L("Barato", "Cheap"), impact=L("Mais dano e slots de runa", "More damage and rune slots")),
 dict(p=5, item=L("Rampart Raptor Runemastered", "Runemastered Rampart Raptor"), phase=L("Nível 55", "Level 55"), cost=L("Valor", "Value"), impact=L("Teto do dano do leveling", "Leveling damage ceiling")),
 dict(p=6, item="Skysliver", phase=L("Mapas", "Maps"), cost=L("Barato", "Cheap"), impact=L("Libera a Whirling Slash", "Unlocks Whirling Slash")),
 dict(p=7, item="Morior Invictus", phase=L("Endgame", "Endgame"), cost=L("Valor", "Value"), impact=L("Armour, vida e Spirit por socket", "Armour, life and Spirit per socket")),
 dict(p=8, item=L("Viper Heart (Trinity) + Lineage", "Viper Heart (Trinity) + Lineage"), phase="Pinnacle", cost=L("Luxo", "Luxury"), impact=L("Teto de dano", "Damage ceiling")),
]

TRICKS = [
 {"cat": L("Gelo", "Ice"), "lvl": L("Fácil", "Easy"), "title": L("Congele, depois estilhace", "Freeze, then shatter"), "body": L("Permafrost Bolts Congela quase tudo; a Fragmentation Rounds consome o Freeze e explode em estilhaços, e também explode qualquer Ice Crystal que ela acerte. Nos bosses use a Permafrost até congelar e só então a Fragmentation.", "Permafrost Bolts Freezes almost everything; Fragmentation Rounds consumes the Freeze and explodes into shrapnel, and also explodes any Ice Crystal it hits. On bosses use Permafrost until frozen and only then Fragmentation.")},
 {"cat": L("Setup", "Setup"), "lvl": L("Fácil", "Easy"), "title": L("Um botão para cada Weapon Set", "One button per Weapon Set"), "body": L("Ponha a Permafrost Bolts em um set e a Fragmentation Rounds no outro, e coloque 'ataque básico (Set 1)' e 'ataque básico (Set 2)' em botões separados. Você usa as duas balas sem trocar de set na mão. Confira no jogo se o Set 2 precisa de uma segunda besta.", "Put Permafrost Bolts in one set and Fragmentation Rounds in the other, and put 'basic attack (Set 1)' and 'basic attack (Set 2)' on separate buttons. You use both bolts without swapping sets by hand. Check in game whether Set 2 needs a second crossbow.")},
 {"cat": L("Setup", "Setup"), "lvl": L("Fácil", "Easy"), "title": L("Rampart Raptor: recarga trocada por munição infinita", "Rampart Raptor: reload traded for infinite ammo"), "body": L("A unique tem −30% de recarga, mas 100% de chance de não gastar munição depois de recarregar. Por isso o Rapid Reload da árvore (+40%) e a velocidade de ataque suavizam tudo.", "The unique has −30% reload but a 100% chance not to expend ammo after reloading. That's why the tree's Rapid Reload (+40%) and attack speed smooth everything out.")},
 {"cat": L("Endgame", "Endgame"), "lvl": L("Médio", "Medium"), "title": L("Whirling Slash quebra o gelo sozinha", "Whirling Slash breaks the ice by itself"), "body": L("O Glacial Bolt planta duas paredes de Ice Crystals; a Whirling Slash (melee) gira, quebra todos eles com Biting Frost II/Morrigan's Insight e ainda te move. É o que deixa a build 'super rápida' e consistente.", "Glacial Bolt plants two walls of Ice Crystals; Whirling Slash (melee) spins, breaks them all with Biting Frost II/Morrigan's Insight and also moves you. It's what makes the build 'super fast' and consistent.")},
 {"cat": L("Endgame", "Endgame"), "lvl": L("Médio", "Medium"), "title": L("Se o Glacial Bolt parece lento", "If Glacial Bolt feels sluggish"), "body": L("Depois do giro ele fica pesado se faltar velocidade de ataque. Suba a velocidade: 10% de ataque escala a recarga como 10% de recarga. No começo, recarga ajuda; com onslaught, joias e Mageblood ela deixa de importar.", "After the spin it feels heavy if you lack attack speed. Raise attack speed: 10% attack speed scales reload like 10% reload speed. Early on reload helps; with onslaught, jewels and Mageblood it stops mattering.")},
 {"cat": L("Itens", "Items"), "lvl": L("Fácil", "Easy"), "title": L("EVITE projétil extra nas luvas", "AVOID extra projectile on gloves"), "body": L("Segundo o autor, o mod 'chance de projétil extra' (Surpassing Chance) é bugado: o segundo projétil sai separado, não dispara cristais extras e atrasa. Evite a todo custo.", "According to the author, the 'chance for an extra projectile' mod (Surpassing Chance) is bugged: the second projectile comes out separately, doesn't fire extra crystals and adds a delay. Avoid at all costs.")},
 {"cat": L("Gems", "Gems"), "lvl": L("Difícil", "Hard"), "title": L("Balanceie o Gem Studded", "Balance Gem Studded"), "body": L("O Gem Studded conta só os suportes do Weapon Set ativo. Confira o custo de mana das skills para saber qual cor manda. O autor usa Time of Need e Explosive Shot desligados só para somar Motes e slots de suporte.", "Gem Studded only counts the active Weapon Set's supports. Check your skills' mana costs to see which colour rules. The author uses Time of Need and Explosive Shot switched off just to add Motes and support slots.")},
 {"cat": L("Itens", "Items"), "lvl": L("Fácil", "Easy"), "title": L("Spear que não equipa", "Spear that won't equip"), "body": L("Se o jogo disser que você precisa remover o Pounce ao trocar o Talisman pela spear, arraste a spear para o slot de offhand (escudo/sceptro) e não para o principal.", "If the game says you must remove Pounce when swapping the Talisman for the spear, drag the spear into the offhand slot (shield/sceptre) instead of the main one.")},
 {"cat": L("Anoints", "Anoints"), "lvl": L("Médio", "Medium"), "title": L("Lista de anoints e Megalomaniac (autor)", "Anoint and Megalomaniac list (author)"), "body": L("Augmented Flesh > Paragon > Jack of All Trades / Harness the Elements / Stormbreaker / Wild Storm / Frantic Reach / Resolute Reach / Dizzying Sweep / Engineered Blaze / Endless Blizzard / Imbibed Power / Chakra of Thought.", "Augmented Flesh > Paragon > Jack of All Trades / Harness the Elements / Stormbreaker / Wild Storm / Frantic Reach / Resolute Reach / Dizzying Sweep / Engineered Blaze / Endless Blizzard / Imbibed Power / Chakra of Thought.")},
]
TROUBLESHOOT = [
 (L("A Fragmentation não faz nada", "Fragmentation does nothing"), L("Ela precisa de um alvo Congelado ou de um Ice Crystal. Comece com a Permafrost até o inimigo congelar.", "It needs a Frozen target or an Ice Crystal. Start with Permafrost until the enemy freezes.")),
 (L("Minha recarga está muito lenta", "My reload is too slow"), L("A Rampart Raptor tem −30% de recarga. Pegue Rapid Reload na árvore, suba a velocidade de ataque e use o Emergency Reload.", "The Rampart Raptor has −30% reload. Take Rapid Reload on the tree, raise attack speed and use Emergency Reload.")),
 (L("O Herald de Gelo não explode", "Ice Herald doesn't explode"), L("Ele só solta quando você mata (Shatter) um inimigo Congelado com um ataque. Confira o Freeze e se a explosão tem área suficiente.", "It only releases when you kill (Shatter) a Frozen enemy with an attack. Check Freeze and that the explosion has enough area.")),
 (L("Não fecho o Spirit", "Spirit doesn't add up"), L("Herald 30, War Banner 30 e Plating 30 = 90 de 100 (quests). No endgame: Plating, Arctic, Verisium e Berserk = 120; o Morior Invictus dá +13 Spirit por socket.", "Herald 30, War Banner 30 and Plating 30 = 90 of 100 (quests). In endgame: Plating, Arctic, Verisium and Berserk = 120; Morior Invictus gives +13 Spirit per socket.")),
 (L("A Whirling Slash não equipa", "Whirling Slash won't equip"), L("Ela exige spear no set. Se pedir para remover o Pounce, arraste a spear para o slot de offhand.", "It requires a spear in the set. If it asks to remove Pounce, drag the spear to the offhand slot.")),
 (L("Estou fraco antes do 79", "I'm weak before 79"), L("Confira a Rampart Raptor (Runeforged no 38), os anéis rares (~30 e ~50) e o Rapid Reload. A troca para Glacial Bolt só vale com spear, besta e Morior prontos.", "Check the Rampart Raptor (Runeforged at 38), rare rings (~30 and ~50) and Rapid Reload. Switching to Glacial Bolt only pays off with spear, crossbow and Morior ready.")),
]
ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Resistências no cap · Rampart Raptor Runemastered", "Resistances capped · Runemastered Rampart Raptor"), gear="Rampart Raptor · Thrillsteel"),
 dict(stage="T1–T10", goal=L("Motoric Implants · Skysliver · Desolate Crossbow", "Motoric Implants · Skysliver · Desolate Crossbow"), gear=L("Spear + besta", "Spear + crossbow")),
 dict(stage="T11–T15", goal=L("Morior Invictus · Iron Reflexes · Spirit fechado", "Morior Invictus · Iron Reflexes · Spirit closed"), gear="Morior Invictus"),
 dict(stage="Pinnacle", goal=L("Trinity + Blasphemy · Lineage", "Trinity + Blasphemy · Lineage"), gear="Mageblood · Rite of Passage"),
]
CRAFT = [
 L("Desolate Crossbow: base branca ilvl 82 → Transmutation + Augmentation até + níveis de Attack ou dano elemental adicionado → Regal → Exalted para completar. No PoB: +3 de Attack, fogo e raio adicionados.", "Desolate Crossbow: white ilvl 82 base → Transmutation + Augmentation until + Attack levels or added elemental damage → Regal → Exalted to fill. In the PoB: +3 Attack, added fire and lightning."),
 L("Armadura (capacete, luvas, botas): vida, Armour e resistências primeiro; movimento nas botas.", "Armour (helmet, gloves, boots): life, Armour and resistances first; movement on the boots."),
 L("Runas: Glacial Rune na arma (Lesser no 1, Greater no 30) e runas de dano na Tabula Rasa.", "Runes: Glacial Rune on the weapon (Lesser at 1, Greater at 30) and damage runes on Tabula Rasa."),
]
CASES = [
 (L("Achei uma Desolate Crossbow boa antes do 79", "I found a great Desolate Crossbow before 79"), L("Guarde: sem spear e sem o Glacial Bolt em nível 14+ ela não rende. A Permafrost segue forte até lá.", "Keep it: without a spear and a level 14+ Glacial Bolt it doesn't pay off. Permafrost stays strong until then.")),
 (L("Não tenho a Skysliver", "I don't have Skysliver"), L("Winged Spear nível 16 custa ~0,1 Divine. Até lá fique na Permafrost.", "A level 16 Winged Spear costs ~0.1 Divine. Until then stay on Permafrost.")),
 (L("Não tenho Spirit para o Plating", "I don't have Spirit for Plating"), L("Faltou o Lythara (~62, +40 Spirit). Use só Herald e Banner até lá.", "You're missing Lythara (~62, +40 Spirit). Use only Herald and Banner until then.")),
]
SOURCES = [
 dict(name="Phylaris POE — WHIRLING Glacial Bolt Gemling [POE2 0.5] (Mobalytics)", use=L("Build base: variantes Leveling/Endgame (Early)/Endgame, gems, itens, notas e FAQ", "Base build: Leveling/Endgame (Early)/Endgame variants, gems, items, notes and FAQ"), url=GUIDE_URL),
 dict(name="PoB do autor (poe.ninja)", use=L("Endgame nível 97: árvore, gems, itens e jóias", "Level 97 endgame: tree, gems, items and jewels"), url=POB_URL),
 dict(name="Path of Building (PoE2) — Gems.lua", use=L("Descrições das gems, tiers e custos de Spirit", "Gem descriptions, tiers and Spirit costs"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name="poe.ninja — Economia (Forbidden Rites)", use=L("Preços e níveis dos uniques", "Prices and levels of the uniques"), url="https://poe.ninja/poe2/economy/forbiddenrites"),
]
FIXES = [
 L("O guia do autor tem UMA variante de leveling (87 pontos, sem ascendência). As fases A1–A4 são cortes dela por pontos; os níveis em que gems, runas e itens aparecem seguem o Path of Building e o poe.ninja e o texto avisa quando é aproximado.", "The author's guide has ONE leveling variant (87 points, no ascendancy). Phases A1–A4 are cuts of it by points; the levels at which gems, runes and items appear follow Path of Building and poe.ninja and the text says when it's approximate."),
 L("O autor recomenda uma skill em cada Weapon Set, mas a variante Leveling só lista uma arma: confira no jogo se o Set 2 precisa de uma segunda besta.", "The author recommends one skill in each Weapon Set, but the Leveling variant only lists one weapon: check in game whether Set 2 needs a second crossbow."),
 L("A troca para Whirling Slash + Glacial Bolt no 79 é uma escolha deste guia: o autor não dá o nível. Ela segue as duas variantes de endgame dele.", "Switching to Whirling Slash + Glacial Bolt at 79 is this guide's choice: the author gives no level. It follows his two endgame variants."),
 L("A ordem dos Trials e os níveis 28/40/65/75 são aproximados. Os notables 'From Nothing' (Blood Magic) do endgame não aparecem no mapa: veja o PoB.", "Trial order and levels 28/40/65/75 are approximate. The endgame's 'From Nothing' (Blood Magic) notables don't show on the map: see the PoB."),
]
UI = dict(
 setNote=L("rares com + níveis de Attack, dano elemental e Spirit.", "rares with + Attack levels, elemental damage and Spirit."),
 carry=r"^(Permafrost Bolts|Glacial Bolt)$", box=L("BALAS", "BOLTS"), spiritWhat=L("(buffs persistentes)", "(persistent buffs)"),
 mechBtn=L("Abrir Gelo & Ciclone", "Open Ice & Cyclone"), dmg2="Fragmentation", dmgBar=L("Dano da Permafrost / Fragmentation (aprox.)", "Permafrost / Fragmentation damage (approx.)"),
 dmgLegend=L("dano da Fragmentation (proporção aproximada)", "Fragmentation damage (approximate ratio)"),
 earlyGone=L("As skills iniciais já saíram da barra: você passou do nível {u}.", "Starting skills already left the bar: you're past level {u}."),
 earlyNote=L("Skills de começo; saem no nível ~{u}.", "Early skills; they leave around level {u}."),
 treeIntro=L("Árvore real do guia do Phylaris POE. A variante Leveling do autor (87 pontos) é cortada por fases: Ato 1 projétil, Atos 2–3 velocidade e Vile Wounds, Ato 4 recarga e penetração, Mapas Freeze. No Endgame (79+) você faz respec para a árvore dele, com 30 pontos no Weapon Set 1 e 31 no Set 2.", "Real tree from Phylaris POE's guide. The author's Leveling variant (87 points) is cut into phases: Act 1 projectile, Acts 2–3 speed and Vile Wounds, Act 4 reload and penetration, Maps Freeze. At Endgame (79+) you respec into his tree, with 30 points on Weapon Set 1 and 31 on Set 2."),
 set1=L("spear (Whirling Slash)", "spear (Whirling Slash)"), set2=L("besta (Glacial Bolt)", "crossbow (Glacial Bolt)"), asc="Gemling Legionnaire", cls="Mercenary",
 respecTip=L("Na troca do 79, compare com a fase anterior: nós sem contorno verde já eram seus. Weapon Set 1 = spear; Set 2 = besta.", "At the 79 switch, compare with the previous phase: nodes without a green outline were already yours. Weapon Set 1 = spear; Set 2 = crossbow."),
 routeIntro=L("Sete fases do nível 1 ao 100. Do 1 ao 78 a build é Permafrost + Fragmentation com a Rampart Raptor; a partir do 79 vira Whirling Slash + Glacial Bolt do autor.", "Seven phases from level 1 to 100. From 1 to 78 the build is Permafrost + Fragmentation with the Rampart Raptor; from 79 it becomes the author's Whirling Slash + Glacial Bolt."),
 socketPrio=["Permafrost Bolts", "Fragmentation Rounds", "Herald of Ice", "War Banner", "Scavenged Plating"],
 permIntro=L("Nada disso volta depois. Spirit paga Herald, Banner e Plating. Os pontos de Weapon Set alimentam o Set 1 e o Set 2 no endgame.", "None of this comes back later. Spirit pays for Herald, Banner and Plating. Weapon Set points fuel Set 1 and Set 2 in endgame."),
 atlasCards=[[L("Mapas que atrapalham", "Maps that hurt"), L("Evite mapas com Freeze/Chill imunes ou less Recovery: a build vive de congelar.", "Avoid maps with Freeze/Chill immunity or less Recovery: the build lives on freezing.")],
             [L("Farm", "Farming"), L("Guarde bases de besta ilvl 82 para a Desolate Crossbow e procure Winged Spear para a Skysliver.", "Keep ilvl 82 crossbow bases for the Desolate Crossbow and look for a Winged Spear for Skysliver.")]],
 foot=L("Guia baseado no build do Phylaris POE (Mobalytics), dados de jogo do Path of Building e preços do poe.ninja", "Guide based on Phylaris POE's build (Mobalytics), Path of Building game data and poe.ninja prices"),
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
  ["tree", "reload", "Rapid Reload"], ["tree", "pressure", "Pressure Points"], ["tree", "iron", "Iron Reflexes"],
  ["asc", "eov", "Essence of Virtue"], ["asc", "gs", "Gem Studded"], ["asc", "at", "Advanced Thaumaturgy"], ["asc", "mi", "Motoric Implants"],
 ],
 rules=[
  dict(when=dict(lvMin=1, notOwn=["Rampart Raptor"]), lvl="bad", t=L("Falta a Rampart Raptor", "Rampart Raptor missing"), d=L("Tense Crossbow sem requisito de nível, ~0,005 Divine: é a arma do nível 1 ao 75.", "Tense Crossbow with no level requirement, ~0.005 Divine: it's your weapon from level 1 to 75."), tab="gear"),
  dict(when=dict(lvMin=5, notOwn=["Tabula Rasa"]), lvl="warn", t=L("Tabula Rasa", "Tabula Rasa"), d=L("~0,5 Divine: sockets para runas de dano.", "~0.5 Divine: sockets for damage runes."), tab="gear"),
  dict(when=dict(lvMin=11, notOwn=["Wanderlust"]), lvl="warn", t=L("Wanderlust", "Wanderlust"), d=L("Botas com 20% de movimento, nível 11.", "Boots with 20% movement, level 11."), tab="gear"),
  dict(when=dict(lvMin=27, notOwn=["Thrillsteel"]), lvl="tip", t=L("Thrillsteel", "Thrillsteel"), d=L("Capacete de leveling, nível 27, quase de graça.", "Leveling helmet, level 27, nearly free."), tab="gear"),
  dict(when=dict(lvMin=14, notOwn=["herald"]), lvl="warn", t=L("Herald of Ice", "Herald of Ice"), d=L("Uncut nível 4 com os 30 Spirit do King in the Mists.", "Level 4 Uncut with the 30 Spirit from King in the Mists."), tab="skills"),
  dict(when=dict(lvMin=40, notOwn=["banner"]), lvl="warn", t=L("War Banner", "War Banner"), d=L("Precisa dos +30 Spirit do Ignagduk (~38).", "Needs Ignagduk's +30 Spirit (~38)."), tab="skills"),
  dict(when=dict(lvMin=64, notOwn=["plating"]), lvl="warn", t=L("Scavenged Plating", "Scavenged Plating"), d=L("Precisa dos +40 Spirit do Lythara (~62).", "Needs Lythara's +40 Spirit (~62)."), tab="skills"),
  dict(when=dict(lvMin=40, notOwn=["gs"]), lvl="warn", t=L("Gem Studded", "Gem Studded"), d=L("2º Trial: bônus pela cor de suporte mais comum.", "2nd Trial: bonus for the most common support colour."), tab="asc"),
  dict(when=dict(lvMin=75, notOwn=["mi"]), lvl="bad", t=L("Motoric Implants", "Motoric Implants"), d=L("+2 níveis em todas as skills de Dex: o maior salto de dano.", "+2 levels on all Dex skills: the biggest damage jump."), tab="asc"),
  dict(when=dict(lvMin=79, notOwn=["Skysliver"]), lvl="warn", t=L("Sem Skysliver", "No Skysliver"), d=L("A Whirling Slash exige spear. Winged Spear nível 16, ~0,1 Divine.", "Whirling Slash requires a spear. Level 16 Winged Spear, ~0.1 Divine."), tab="gear"),
  dict(when=dict(lvMin=79, notOwn=["Morior Invictus"]), lvl="tip", t=L("Morior Invictus", "Morior Invictus"), d=L("Armour, vida e Spirit por socket (~6 Divines, nível 65).", "Armour, life and Spirit per socket (~6 Divines, level 65)."), tab="gear"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["endgame", "max"], when=dict(notOwn=["Skysliver"]), gemsFrom="maps", note=L("Sem Skysliver: mostrando o setup de Permafrost + Fragmentation.", "No Skysliver: showing the Permafrost + Fragmentation setup.")),
]
TREE_RULES = [
 dict(when=dict(lvMin=46, notOwn=["reload"]), t=L("Rapid Reload: +40% de recarga compensa a Rampart Raptor.", "Rapid Reload: +40% reload offsets the Rampart Raptor."), node="Rapid Reload"),
 dict(when=dict(lvMin=65, notOwn=["pressure"]), t=L("Pressure Points: +35% de Freeze buildup.", "Pressure Points: +35% Freeze buildup."), node="Pressure Points"),
 dict(when=dict(lvMin=79, notOwn=["iron"]), t=L("Iron Reflexes converte Evasion em Armour.", "Iron Reflexes converts Evasion to Armour."), node="Iron Reflexes"),
]
TIMING_KEY = {"Rampart Raptor": "Rampart Raptor", "Tabula Rasa": "Tabula Rasa", "Wanderlust": "Wanderlust", "Thrillsteel": "Thrillsteel", "Skysliver": "Skysliver", "Morior Invictus": "Morior Invictus",
              "Herald of Ice": "herald", "War Banner": "banner", "Scavenged Plating": "plating", "Arctic Armour": "arctic", "Glacial Bolt": "glacial", "Whirling Slash": "whirl", "Motoric Implants": "mi", "Gem Studded": "gs"}

T("item", "Rampart Raptor", 1, L("Tense Crossbow, nível 0; ~0,005 Divine", "Tense Crossbow, level 0; ~0.005 Divine"), L("Nível 1.", "Level 1."), L("Toda a sua ofensiva do 1 ao 75.", "All your offence from 1 to 75."), "—", L("Sem ela o Ato 1 fica lento.", "Without it Act 1 is slow."), [L("Runeforged no 38, Runemastered no 55.", "Runeforged at 38, Runemastered at 55.")])
T("item", "Wanderlust", 11, L("Wrapped Sandals nível 11; ~0,01 Divine", "Level 11 Wrapped Sandals; ~0.01 Divine"), L("Ato 1.", "Act 1."), L("20% de movimento e imunidade à lentidão.", "20% movement and Slow immunity."), L("Botas com movimento até lá.", "Boots with movement until then."), "—")
T("item", "Thrillsteel", 27, L("Spired Greathelm nível 27; ~0,03 Divine", "Level 27 Spired Greathelm; ~0.03 Divine"), L("Ato 2.", "Act 2."), L("Capacete de vida.", "A life helmet."), "—", "—")
T("item", "Skysliver", 16, L("Winged Spear nível 16; ~0,1 Divine", "Level 16 Winged Spear; ~0.1 Divine"), L("Compre nos mapas.", "Buy in the maps."), L("Libera a Whirling Slash.", "Unlocks Whirling Slash."), L("Não use antes do 79.", "Don't use before 79."), "—")
T("item", "Morior Invictus", 65, L("Nível 65; ~6 Divines", "Level 65; ~6 Divines"), L("Endgame.", "Endgame."), L("Armour, vida e Spirit por socket.", "Armour, life and Spirit per socket."), "—", "—")
T("skill", "Herald of Ice", 12, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Depois do King in the Mists.", "After King in the Mists."), L("Explosão de gelo ao matar congelados.", "Ice explosion on killing frozen enemies."), L("Não ligue sem 30 Spirit livres.", "Don't turn on without 30 free Spirit."), "—")
T("skill", "War Banner", 38, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Depois do Ignagduk.", "After Ignagduk."), L("Buff de dano e velocidade de ataque.", "Attack damage and speed buff."), "—", "—")
T("skill", "Scavenged Plating", 62, L("Tier 4, 30 Spirit", "Tier 4, 30 Spirit"), L("Depois do Lythara.", "After Lythara."), L("Armour e Thorns ao quebrar Armour.", "Armour and Thorns on breaking Armour."), "—", "—")
T("skill", "Whirling Slash", 79, L("Uncut nível 1 (spear)", "Level 1 Uncut (spear)"), L("Na troca do 79.", "At the 79 switch."), L("Movimento e quebra dos cristais.", "Movement and crystal breaking."), "—", "—")
T("asc", "Gem Studded", 40, L("2º Trial", "2nd Trial"), L("Ato 3.", "Act 3."), L("Bônus pela cor de suporte mais comum.", "Bonus for the most common support colour."), "—", "—")
T("asc", "Motoric Implants", 75, L("4º Trial", "4th Trial"), L("Mapas.", "Maps."), L("+2 níveis em skills de Dex.", "+2 levels on Dex skills."), "—", "—")

MECH = dict(
 title=L("Gelo & Ciclone", "Ice & Cyclone"),
 intro=L("A build inteira é uma ideia só: congelar e estilhaçar. Do nível 1 ao 78 você faz isso com duas balas; no endgame, o Glacial Bolt planta o gelo e a Whirling Slash o quebra andando.", "The whole build is one idea: freeze and shatter. From level 1 to 78 you do it with two bolts; in endgame Glacial Bolt plants the ice and Whirling Slash breaks it while moving."),
 sections=[
  dict(type="cards", cards=[
   [L("1. Congelar", "1. Freeze"), L("Permafrost Bolts dispara balas de gelo que se fragmentam e são muito boas em Congelar. Freezing Mark marca o boss e dá dano de frio extra quando ele congela. Pressure Points (+35%) e Emboldened Avatar (+25%) somam Freeze buildup.", "Permafrost Bolts fires ice bolts that fragment and are very good at Freezing. Freezing Mark marks the boss and gives extra cold damage when it freezes. Pressure Points (+35%) and Emboldened Avatar (+25%) add Freeze buildup.")],
   [L("2. Estilhaçar", "2. Shatter"), L("Fragmentation Rounds acerta o Congelado, gasta o Freeze e explode em estilhaços; se acertar um Ice Crystal, ele explode. Herald of Ice solta uma explosão quando você mata um congelado. Vile Wounds dá +33% contra alvos com ailment.", "Fragmentation Rounds hits the Frozen enemy, spends the Freeze and explodes into shrapnel; if it hits an Ice Crystal, it explodes. Herald of Ice releases an explosion when you kill a frozen enemy. Vile Wounds gives +33% against ailed targets.")],
   [L("3. Ciclone (endgame)", "3. Cyclone (endgame)"), L("O Glacial Bolt cria duas paredes de Ice Crystals. A Whirling Slash (melee) gira, Desacelera e Cega, gera Rage e quebra os cristais com Biting Frost II/Morrigan's Insight. Você anda atacando, e as explosões saem sozinhas.", "Glacial Bolt creates two walls of Ice Crystals. Whirling Slash (melee) spins, Slows and Blinds, generates Rage and breaks the crystals with Biting Frost II/Morrigan's Insight. You move while attacking and the explosions happen on their own.")],
   [L("4. Cores e Spirit", "4. Colours and Spirit"), L("Gem Studded (2º Trial) dá bônus pela cor de suporte mais comum: verde = menos penalidade de movimento, azul = skills 30% mais baratas, vermelho = hits sem dano crítico bônus contra você. Só conta o Weapon Set ativo. Spirit vem de quests: 30, +30 (Ignagduk), +40 (Lythara).", "Gem Studded (2nd Trial) gives a bonus for the most common support colour: green = less movement penalty, blue = skills 30% cheaper, red = hits without critical bonus against you. It only counts the active Weapon Set. Spirit comes from quests: 30, +30 (Ignagduk), +40 (Lythara).")],
  ]),
  dict(type="rotation", blocks=[
   [L("Leveling (1–78)", "Leveling (1–78)"), [L("Permafrost Bolts para limpar e congelar", "Permafrost Bolts to clear and freeze"), L("Boss: Freezing Mark → Permafrost até congelar", "Boss: Freezing Mark → Permafrost until frozen"), L("Boss congelado: Fragmentation Rounds", "Frozen boss: Fragmentation Rounds"), L("Emergency Reload quando o pente acabar", "Emergency Reload when the clip runs out")]],
   [L("Endgame (79+)", "Endgame (79+)"), [L("Set 1: Whirling Slash para andar", "Set 1: Whirling Slash to move"), L("Set 2: Glacial Bolt planta as paredes", "Set 2: Glacial Bolt plants the walls"), L("Boss: Seismic Cry, Pounce e Berserk", "Boss: Seismic Cry, Pounce and Berserk")]],
  ]),
  dict(type="table", h=L("Weapon sets por fase", "Weapon sets per phase"), cols=[L("Fase", "Phase"), "Weapon Set 1", "Weapon Set 2"], rows=[
   [L("1–78", "1–78"), L("Rampart Raptor: Permafrost Bolts", "Rampart Raptor: Permafrost Bolts"), L("Fragmentation Rounds (confira se pede 2ª besta)", "Fragmentation Rounds (check whether it needs a 2nd crossbow)")],
   [L("79+", "79+"), L("Spear (Skysliver): Whirling Slash, Seismic Cry", "Spear (Skysliver): Whirling Slash, Seismic Cry"), L("Desolate Crossbow: Glacial Bolt, Emergency Reload", "Desolate Crossbow: Glacial Bolt, Emergency Reload")],
   [L("Sempre", "Always"), L("Buffs persistentes nos dois sets", "Persistent buffs on both sets"), L("Buffs persistentes nos dois sets", "Persistent buffs on both sets")],
  ]),
  dict(type="spirit", h=L("Spirit dos buffs", "Buff Spirit"), p=L("Marque o que você usa. Custos do Path of Building.", "Tick what you use. Costs from Path of Building."),
       note=L("Ordem: Herald → War Banner → Scavenged Plating → Arctic Armour → Verisium → Berserk. Se faltar, desligue o último.", "Order: Herald → War Banner → Scavenged Plating → Arctic Armour → Verisium → Berserk. If short, turn off the last one.")),
  dict(type="timeline", h=L("Peças-chave por nível", "Key pieces by level"), items=[
   dict(lv=1, t="Rampart Raptor + Permafrost + Fragmentation", d=L("A build inteira desde o primeiro nível.", "The whole build from the first level.")),
   dict(lv=12, t="Herald of Ice", d=L("Depois do King in the Mists (+30 Spirit).", "After King in the Mists (+30 Spirit).")),
   dict(lv=38, t=L("Rampart Raptor Runeforged + War Banner", "Runeforged Rampart Raptor + War Banner"), d=L("Ignagduk: +30 Spirit.", "Ignagduk: +30 Spirit.")),
   dict(lv=62, t="Scavenged Plating", d=L("Lythara: +40 Spirit.", "Lythara: +40 Spirit.")),
   dict(lv=75, t="Motoric Implants", d=L("+2 níveis em skills de Dex.", "+2 levels on Dex skills.")),
   dict(lv=79, t="Skysliver + Whirling Slash + Glacial Bolt", d=L("A troca para o endgame do autor.", "The switch to the author's endgame.")),
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
