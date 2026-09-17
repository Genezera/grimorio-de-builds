# -*- coding: utf-8 -*-
"""Acolyte of Chayula: Poisonburst Arrow + Toxic Growth + Archon of Chayula. Base: planner do Goratha (Maxroll: Campaign, Mapping, Min Max),
convertido por kit/maxroll.py; textos do Path of Building, bases do RePoE2 e preços do poe.ninja (Forbidden Rites)."""
import copy, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("acolyte")
# fase Archon: itens e gems do Mapping, ascendência completa do Min Max
_arch = copy.deepcopy(VAR["Mapping"]); _arch["name"] = "Archon"; _arch["tree"]["a"] = list(VAR["Min Max"]["tree"]["a"])
V["variants"].append(_arch); VAR["Archon"] = _arch

PLANNER_URL = "https://maxroll.gg/poe2/planner/w675g80h"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "17/09/2026"

CONFIG = dict(dir="acolyte", build="acolyte", store="acolyte1", emoji="🌀", pill="Monk · Acolyte of Chayula",
              fonts="family=Cinzel+Decorative:wght@700;900&family=Cinzel:wght@500;700&family=Cormorant+SC:wght@500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400")
TXT = {
 "pt": dict(TITLE="Sonho de Chayula", DESC="Guia interativo Acolyte of Chayula Poisonburst Arrow + Archon of Chayula (Monk) — PoE 2 Forbidden Rites",
            H1S="Poisonburst Arrow · Toxic Growth · Chamas de Chayula · Archon — planner do Goratha explicado", H1="O Sonho de Chayula",
            LEAD="Uma flecha envenena o pack, os heralds fazem tudo explodir em cadeia e as chamas roxas de Chayula transformam o dano em caos. No fim, você vira o Archon: tornados de caos que detonam as pústulas no boss. Diga seu nível e o que você tem."),
 "en": dict(TITLE="Chayula's Dream", DESC="Interactive Acolyte of Chayula Poisonburst Arrow + Archon of Chayula (Monk) guide — PoE 2 Forbidden Rites",
            H1S="Poisonburst Arrow · Toxic Growth · Flames of Chayula · Archon — Goratha's planner explained", H1="Chayula's Dream",
            LEAD="One arrow poisons the pack, the heralds chain-explode everything and Chayula's purple flames turn your damage into chaos. At the end you become the Archon: chaos tornadoes that detonate the pustules on the boss. Tell it your level and what you have."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["skills", "Skills", "Skills"],
        ["gear", "Itens", "Items"], ["arvore", "Árvore", "Tree"], ["rota", "Níveis 1→100", "Levels 1→100"], ["asc", "Ascendência", "Ascendancy"], ["quests", "Quests", "Quests"],
        ["mech", "Como funciona", "How it works"], ["quando", "Desbloqueios", "Unlocks"], ["uniques", "Uniques", "Uniques"], ["tricks", "Min-max", "Min-max"], ["atlas", "Atlas", "Atlas"],
        ["diag", "Problemas", "Problems"], ["fontes", "Fontes", "Sources"]]
TAB_GROUPS = [[L("Jogar", "Play"), ["agora", "meu", "skills"]], [L("Evoluir", "Upgrade"), ["gear", "arvore", "rota", "asc", "quests"]], [L("Dominar", "Master"), ["mech", "quando", "uniques", "tricks", "atlas", "diag", "fontes"]]]

CLASS, ASC, START = "Monk", "Acolyte of Chayula", 44683
ORDER = ["a1", "a2", "a3", "a4", "maps", "archon", "max"]
VMAP = {"a1": "A1", "a2": "A2", "a3": "Campaign", "a4": "Interlude", "maps": "Mapping", "archon": "Archon", "max": "Min Max"}
FULLMAP = {k: k for k in ORDER}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a4", "maps": "a4", "archon": "maps", "max": "archon"}
PHASE_ACT = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "maps": 6, "archon": 6, "max": 6}
ITEM_NOTE = {"Familial Talisman": L("Set 2: snapshot", "Set 2: snapshot"), "Hysseg's Claw": L("Set 2: snapshot", "Set 2: snapshot")}
EXTRA_ICONS = {"Contagion": "Art/2DItems/Gems/New/WitchContagionSkillGem.dds"}
BOW_RUNE = L("Countess Seske's Rune of Archery (+flecha) + Idol of Thruldana (+1 veneno)", "Countess Seske's Rune of Archery (+arrow) + Idol of Thruldana (+1 poison)")

def socket_hint(slot, name):
    if "Bow" in name or name == "Splinterheart": return [BOW_RUNE]
    if slot == "Capacete": return [L("Rune of Reach (efeito das Remnants)", "Rune of Reach (remnant effect)")]
    if slot == "Body Armour": return [L("Craiceann's Rune of Warding + runa de resistência que faltar", "Craiceann's Rune of Warding + whatever resistance rune you're missing")]
    return None

SUPWHY = {
 "Bleed I": L("Faz o alvo sangrar: liga o Herald of Blood.", "Makes the target bleed: enables Herald of Blood."), "Bleed II": L("Mais sangramento para o Herald of Blood.", "More bleeding for Herald of Blood."), "Bleed III": L("Sangramento forte: explosões do Herald of Blood em cadeia.", "Strong bleed: chained Herald of Blood explosions."),
 "Bursting Plague": L("Inimigos envenenados explodem ao morrer — a explosão também pode sangrar (auto-corrente).", "Poisoned enemies explode on death — the explosion can also bleed (self-chaining)."),
 "Escalating Poison": L("Aplica um veneno extra no alvo, com duração menor.", "Applies an extra poison to the target, with shorter duration."),
 "Deadly Poison II": L("Veneno mais forte, menos dano de hit.", "Stronger poison, less hit damage."),
 "Poison II": L("Chance de envenenar.", "Poison chance."), "Poison III": L("Chance de envenenar e veneno mais forte contra inimigos sangrando (combina com o Bleed); no Archon, o veneno detona as pústulas.", "Poison chance and stronger poison against bleeding enemies (pairs with Bleed); on Archon, the poison detonates the pustules."),
 "Fork": L("As flechas se dividem: clear fora da tela.", "Arrows fork: off-screen clear."),
 "Concentrated Area": L("OBRIGATÓRIO na Toxic Growth: as pústulas se sobrepõem no boss.", "MANDATORY on Toxic Growth: pustules overlap on the boss."),
 "Long Fuse I": L("Pústulas com pavio maior e mais dano.", "Longer fuse and more damage on pustules."), "Long Fuse II": L("Pavio maior, muito mais dano.", "Longer fuse, much more damage."),
 "Arakaali's Lust": L("Lineage barata: muito dano na Toxic Growth com +5 venenos.", "Cheap lineage: huge Toxic Growth damage with +5 poisons."),
 "Garukhan's Resolve": L("Lineage cara: limita a chance máxima de crítico e rola o crítico duas vezes (Bifurcate). Só vale com ~50% de crítico.", "Expensive lineage: caps max crit chance and rolls crits twice (Bifurcate). Only worth it at ~50% crit."),
 "Prolonged Duration I": L("Planta da Vine Arrow dura mais.", "Vine Arrow plant lasts longer."), "Prolonged Duration II": L("Mais duração: tornados do Archon duram mais.", "More duration: Archon tornadoes last longer."),
 "Swift Affliction I": L("Dano no tempo mais rápido.", "Faster damage over time."), "Swift Affliction II": L("Dano no tempo bem mais rápido.", "Much faster damage over time."),
 "Deliberation": L("Mais dano.", "More damage."), "Stoicism II": L("O dano da skill sobe aos poucos até um limite; zera se você der dodge ou usar skill de movimento.", "The skill's damage ramps up to a cap; it resets if you dodge roll or use a travel skill."),
 "Magnified Area I": L("Área maior.", "Larger area."), "Magnified Area II": L("Área maior.", "Larger area."),
 "Chaos Mastery": L("+1 nível em skills de caos.", "+1 level to chaos skills."),
 "Astral Projection": L("Plague Bearer vira à distância.", "Makes Plague Bearer ranged."),
 "Exploit Weakness": L("Mais dano contra Armour quebrada (Corrosion no Archon).", "More damage against broken Armour (Corrosion on Archon)."),
 "Tacati's Ire": L("Lineage: o veneno causa dano mais rápido quanto mais Rage você tem (Rage do Absent Amulet).", "Lineage: poison deals damage faster the more Rage you have (Rage from Absent Amulet)."), "Vorana's Siege": L("Lineage: área maior e hits fortes em alvo isolado.", "Lineage: larger area and strong hits on isolated targets."),
 "Harmonic Remnants II": L("Chamas de Chayula de mais longe.", "Flames of Chayula from further away."), "Remnant Potency III": L("Chamas mais fortes (mais caos da roxa), com um pequeno atraso no efeito.", "Stronger flames (more chaos from purple), with a small delay on the effect."),
 "Khatal's Rejuvenation": L("Lineage: pegar Remnants reduz cooldown (Ghost Dance).", "Lineage: picking Remnants reduces cooldowns (Ghost Dance)."),
 "Persistent Ground II": L("A nuvem da Gas Arrow dura bem mais e não termina por outras condições: mantém veneno sobre boss e pústulas com menos recasts.", "Gas Arrow's cloud lasts much longer and cannot end through other conditions: it keeps poison on the boss and pustules with fewer recasts."),
 "Repulsion": L("Curse dentro do Blasphemy: explosões ao acertar.", "Curse inside Blasphemy: explosions on hit."),
 "Living Lightning": L("Qualquer hit de raio cria minions que ativam a Repulsion.", "Any lightning hit creates minions that proc Repulsion."), "Living Lightning II": L("Minions de raio ativam a Repulsion sozinhos.", "Lightning minions proc Repulsion by themselves."),
 "Admixture": L("Sangramento mais efetivo em inimigos envenenados e veneno mais efetivo em inimigos sangrando: a build aplica os dois.", "Bleeding is more effective against poisoned enemies and poison more effective against bleeding ones: the build applies both."),
 "Withering Touch": L("Chance de Wither ao acertar: mais dano de caos.", "Chance to Wither on hit: more chaos damage."), "Corrosion": L("O veneno que a skill aplica também quebra a Armour do alvo (para o Exploit Weakness).", "The poison the skill applies also breaks the target's Armour (for Exploit Weakness)."),
 "Uul-Netol's Embrace": L("Lineage: caos extra e o dano de caos quebra Armour.", "Lineage: extra chaos damage, and chaos damage breaks Armour."),
 "Rage II": L("Rage ao acertar ataques melee (Wind Dancer no setup do Goratha).", "Rage on melee attack hits (Wind Dancer in Goratha's setup)."), "Maim": L("Maim nos inimigos repelidos.", "Maims knocked-back enemies."), "Blind II": L("Blind: defesa.", "Blind: defence."), "Life Leech III": L("Leech de vida com o dano físico dos ataques; não para com a vida cheia.", "Life leech from attack physical damage; not removed at full life."),
 "Cooldown Recovery II": L("Ghost Dance volta mais rápido.", "Ghost Dance recovers faster."), "Her Declaration": L("Intimidate na Presence. Reduz o custo quando no Ghost Dance.", "Intimidate in Presence. Cheaper when on Ghost Dance."),
}

SP30 = L("30 Spirit", "30 Spirit")
PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Poisonburst + Herald of Blood", "Poisonburst + Herald of Blood"),
  carry=L("Você: Poisonburst Arrow", "You: Poisonburst Arrow"), dmgSplit=[100, 0],
  goal=L("Monk com arco desde o nível 1. O Poisonburst Arrow limpa bem mas falta dano em alvo único até a Toxic Growth (nível 14): use Vine Arrow nos rares e Contagion no começo. Primeiro Spirit (King in the Mists): Herald of Blood com Bleed I e Bursting Plague — a explosão do herald não sangra, mas a do Bursting Plague sim, e a corrente se alimenta sozinha. Se o Ato 1 estiver lento, o Goratha sugere subir com granadas ou Twister até o 14.",
         "Monk with a bow from level 1. Poisonburst Arrow clears well but lacks single target until Toxic Growth (level 14): use Vine Arrow on rares and Contagion early. First Spirit (King in the Mists): Herald of Blood with Bleed I and Bursting Plague — the herald's explosion doesn't bleed, but Bursting Plague's does, so the chain feeds itself. If Act 1 is slow, Goratha suggests leveling with grenades or Twister until 14."),
  rotation=[L("Poisonburst Arrow no pack", "Poisonburst Arrow into the pack"), L("Vine Arrow no rare/boss", "Vine Arrow on the rare/boss"), L("Poisonburst Arrow em volta da planta", "Poisonburst Arrow around the plant")],
  gems=[
   G("Poisonburst Arrow", ["Bleed I", "Bursting Plague"], L("Clear", "Clear"), L("Flecha que solta uma explosão de veneno em área.", "Arrow that releases an area poison burst."), "free"),
   G("Vine Arrow", ["Prolonged Duration I", "Swift Affliction I"], L("Alvo único (começo)", "Single target (early)"), L("Planta que prende e causa caos no tempo.", "Plant that latches and deals chaos over time."), "free"),
   G("Contagion", [], L("Clear (começo)", "Clear (early)"), L("Só no começo do Ato 1.", "Early Act 1 only."), "free", until=10),
   G("Herald of Blood", ["Poison II", "Bursting Plague", "Bleed I"], L("Explosões em cadeia", "Chain explosions"), L("Matar inimigo sangrando causa explosão física. Mantenha o nível baixo se faltar atributo.", "Killing a bleeding enemy causes a physical explosion. Keep it low level if attributes are short."), "core", 1, SP30),
  ],
  cheap=["Plaguefinger", "Luminous Pace", "Asphyxia's Wrath", L("Arco com dano físico", "Bow with physical damage")],
  full=["Meginord's Girdle", "Blackheart", "Surefooted Sigil"],
  stats=[L("Dano plano de ataque", "Flat attack damage"), L("% dano físico no arco", "% physical damage on the bow"), L("Atributos (apertados)", "Attributes (tight)")],
  tree=L("Nós de 'increased Damage' baratos: Concussive Attack, Blinding Strike, Killer Instinct.", "Cheap 'increased Damage' nodes: Concussive Attack, Blinding Strike, Killer Instinct."),
  avoid=[L("Herald of Blood nível alto sem atributos", "High-level Herald of Blood without attributes")],
  exit=[L("King in the Mists: Herald of Blood", "King in the Mists: Herald of Blood"), L("Nível 14: Toxic Growth", "Level 14: Toxic Growth")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 29], tag=L("Toxic Growth + Waking Dream", "Toxic Growth + Waking Dream"),
  carry=L("Você: Poisonburst · Toxic Growth", "You: Poisonburst · Toxic Growth"), dmgSplit=[100, 0],
  goal=L("A Toxic Growth vira o dano de boss: SEMPRE com Concentrated Area (as pústulas se sobrepõem). Lance uma vez e só lance de novo depois que as primeiras explodirem — relançar destrói as antigas. 1ª ascendência: Waking Dream (Into the Breach) — chamas vermelhas (vida), azuis (mana) e roxas (7% do dano ganho como caos) nascem em volta de você.",
         "Toxic Growth becomes your boss damage: ALWAYS with Concentrated Area (pustules overlap). Cast it once and only recast after the first ones explode — recasting destroys the old ones. 1st ascendancy: Waking Dream (Into the Breach) — red (life), blue (mana) and purple (7% of damage gained as chaos) flames spawn around you."),
  rotation=[L("Vine Arrow no boss (a planta também aceita veneno)", "Vine Arrow on the boss (the plant takes poison too)"), L("Toxic Growth EM CIMA do boss (uma vez só)", "Toxic Growth ON TOP of the boss (once only)"), L("Poisonburst Arrow no boss, de perto: a área do veneno carrega as pústulas", "Poisonburst Arrow at the boss, up close: the poison area charges the pustules"), L("Só relance a Toxic Growth depois que as pústulas explodirem", "Only recast Toxic Growth after the pustules explode")],
  gems=[
   G("Poisonburst Arrow", ["Bleed II", "Bursting Plague", "Escalating Poison"], L("Clear", "Clear"), L("3 links.", "3 links."), "free"),
   G("Toxic Growth", ["Concentrated Area", "Escalating Poison", "Long Fuse I"], L("Alvo único", "Single target"), L("Chuva de pústulas; envenenadas, detonam antes e mais forte.", "Rain of pustules; when poisoned, they detonate sooner and harder."), "free"),
   G("Vine Arrow", ["Prolonged Duration I", "Swift Affliction I", "Deliberation"], L("Alvo único", "Single target"), L("Abre a rotação.", "Opens the rotation."), "free"),
   G("Herald of Blood", ["Poison II", "Bursting Plague", "Bleed I"], L("Explosões", "Explosions"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Into the Breach", ["Harmonic Remnants II", "Remnant Potency III"], L("Chamas de Chayula", "Flames of Chayula"), L("Da ascendência Waking Dream.", "From the Waking Dream ascendancy."), "free", since=24),
   G("Despair", [], L("Curse de boss", "Boss curse"), L("Lançada na mão: reduz a Chaos Resistance do boss. Todo o seu dano (veneno incluso) é caos, então é o maior ganho por gem no leveling. Uncut Skill Gem nível 9.", "Self-cast: lowers the boss's Chaos Resistance. All your damage (poison included) is chaos, so it's the biggest per-gem gain while leveling. Level 9 Uncut Skill Gem."), "free", since=24),
   G("Pounce", [], L("Mobilidade", "Mobility"), L("Talisman no Weapon Set 2.", "Talisman on Weapon Set 2."), "free"),
  ],
  cheap=["Goldrim", "Wanderlust", L("Aljava com dano plano", "Quiver with flat damage")],
  full=["Splinterheart", "The Lethal Draw", "Ghostmarch", L("Amor Mandragora (Set 2)", "Amor Mandragora (Set 2)")],
  stats=[L("Dano plano", "Flat damage"), L("Vida e resistências", "Life and resistances")],
  tree=L("Ainda dano genérico; comece a ir para os nós de veneno.", "Still generic damage; start heading to poison nodes."),
  avoid=[L("Toxic Growth sem Concentrated Area", "Toxic Growth without Concentrated Area"), L("Relançar a Toxic Growth antes das pústulas explodirem", "Recasting Toxic Growth before pustules explode")],
  exit=[L("1ª ascendência: Waking Dream", "1st ascendancy: Waking Dream")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[30, 44], tag=L("Plague Bearer + Choice of Power", "Plague Bearer + Choice of Power"),
  carry=L("Você: veneno + Plague Bearer", "You: poison + Plague Bearer"), dmgSplit=[100, 0],
  goal=L("Segundo Spirit (Azak Bog): Plague Bearer — guarda o veneno causado e, ao ativar com 100%, solta tudo e explode as pústulas de uma vez. Agora pegue todos os notables de veneno (Crippling, Stacking, Lasting, Leeching, Escalating e Building Toxins). 2ª ascendência: Lucid Dreaming → Choice of Power (todas as chamas roxas: triplica o DPS segundo o Goratha). No nível 40, runeforge o Splinterheart com Medved's Crest of the Circle.",
         "Second Spirit (Azak Bog): Plague Bearer — stores the poison you deal and, when activated at 100%, releases it all and pops the pustules at once. Now take every poison notable (Crippling, Stacking, Lasting, Leeching, Escalating and Building Toxins). 2nd ascendancy: Lucid Dreaming → Choice of Power (all flames purple: triples DPS according to Goratha). At level 40, runeforge Splinterheart with Medved's Crest of the Circle."),
  rotation=[L("Clear: Poisonburst até o Plague Bearer chegar a 100%", "Clear: Poisonburst until Plague Bearer hits 100%"), L("Ative o Plague Bearer", "Activate Plague Bearer"), L("Boss: Vine Arrow → Toxic Growth em cima dele → Poisonburst para encher o Plague Bearer → Plague Bearer a 100% (estoura as pústulas) → Toxic Growth de novo", "Boss: Vine Arrow → Toxic Growth on top of it → Poisonburst to fill Plague Bearer → Plague Bearer at 100% (pops the pustules) → Toxic Growth again")],
  gems=[
   G("Poisonburst Arrow", ["Bleed II", "Bursting Plague", "Escalating Poison"], L("Clear + carga do Plague Bearer", "Clear + Plague Bearer charge"), L("Mesmo papel.", "Same role."), "free"),
   G("Toxic Growth", ["Concentrated Area", "Escalating Poison", "Deadly Poison II", "Long Fuse I"], L("Alvo único", "Single target"), L("4 links.", "4 links."), "free"),
   G("Vine Arrow", ["Prolonged Duration I", "Swift Affliction I", "Deliberation"], L("Abre o boss", "Opens the boss"), L("Mesmo papel.", "Same role."), "free"),
   G("Herald of Blood", ["Poison II", "Bursting Plague", "Bleed I"], L("Explosões", "Explosions"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Plague Bearer", ["Magnified Area I", "Chaos Mastery"], L("Burst de veneno", "Poison burst"), L("30 Spirit. Use o ativo com 100%.", "30 Spirit. Use the active at 100%."), "core", 2, SP30),
   G("Into the Breach", ["Harmonic Remnants II", "Remnant Potency III"], L("Chamas roxas", "Purple flames"), L("Choice of Power.", "Choice of Power."), "free"),
   G("Despair", [], L("Curse de boss", "Boss curse"), L("Antes de cada boss: menos Chaos Resistance = mais dano de veneno.", "Before every boss: less Chaos Resistance = more poison damage."), "free"),
   G("Pounce", [], L("Mobilidade", "Mobility"), L("Set 2.", "Set 2."), "free"),
  ],
  cheap=["Atsak's Sight", "Snakebite", "Sanguis Heroum"],
  full=["Death's Harp", "Icefang Orbit", L("Splinterheart runeforged (40)", "Runeforged Splinterheart (40)")],
  stats=[L("Dano plano", "Flat damage"), L("Spirit no peito/amuleto", "Spirit on chest/amulet"), L("Atributos", "Attributes")],
  tree=L("Notables de veneno; First Teachings of the Keeper e First Principle of the Hollow (liberam The Hollowkeeper).", "Poison notables; First Teachings of the Keeper and First Principle of the Hollow (unlock The Hollowkeeper)."),
  avoid=[L("Ativar Plague Bearer antes de 100%", "Activating Plague Bearer before 100%")],
  exit=[L("2ª ascendência: Choice of Power", "2nd ascendancy: Choice of Power"), L("Azak Bog (+30 Spirit)", "Azak Bog (+30 Spirit)")]),

 dict(id="a4", name=L("Ato 4 + Interlúdios", "Act 4 + Interludes"), lv=[45, 64], tag=L("Herald of Plague + Blasphemy", "Herald of Plague + Blasphemy"),
  carry=L("Você: cadeia de explosões", "You: explosion chain"), dmgSplit=[100, 0],
  goal=L("Terceiro Spirit: Herald of Plague (matar inimigo envenenado espalha o veneno). Com Spirit no equipamento e Inteligência, Blasphemy + Repulsion com Living Lightning — qualquer hit de raio cria minions que ativam a Repulsion. A Repulsion não usa o dano da arma, mas usa o dano plano de anéis, aljava e luvas. Wind Dancer para defesa.",
         "Third Spirit: Herald of Plague (killing a poisoned enemy spreads its poison). With Spirit on gear and Intelligence, Blasphemy + Repulsion with Living Lightning — any lightning hit creates minions that proc Repulsion. Repulsion doesn't use weapon damage, but it does use flat damage from rings, quiver and gloves. Wind Dancer for defence."),
  rotation=[L("Poisonburst Arrow: veneno + sangramento", "Poisonburst Arrow: poison + bleed"), L("Heralds + Repulsion explodem o resto", "Heralds + Repulsion blow up the rest"), L("Plague Bearer a 100%", "Plague Bearer at 100%")],
  gems=[
   G("Poisonburst Arrow", ["Bleed III", "Bursting Plague", "Escalating Poison", "Deadly Poison II"], L("Clear", "Clear"), L("Mesmo papel.", "Same role."), "free"),
   G("Toxic Growth", ["Concentrated Area", "Escalating Poison", "Deadly Poison II", "Long Fuse I"], L("Alvo único", "Single target"), L("Mesmo papel.", "Same role."), "free"),
   G("Vine Arrow", ["Prolonged Duration II", "Swift Affliction II", "Deliberation"], L("Abre o boss", "Opens the boss"), L("Mesmo papel.", "Same role."), "free"),
   G("Herald of Blood", ["Poison III", "Bursting Plague", "Bleed III"], L("Explosões", "Explosions"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Plague Bearer", ["Magnified Area I", "Chaos Mastery", "Deadly Poison II"], L("Burst de veneno", "Poison burst"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Herald of Plague", ["Chaos Mastery"], L("Espalha veneno", "Spreads poison"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Blasphemy", ["Repulsion", "Magnified Area I", "Living Lightning"], L("Repulsion em aura", "Repulsion aura"), L("Precisa de Spirit no equipamento e Inteligência. Reserva conforme a curse.", "Needs Spirit on gear and Intelligence. Reserves based on the curse."), "opt", 1, L("Confira no jogo", "Check in game")),
   G("Wind Dancer", [], L("Defesa", "Defence"), L("Evasão por estágio; repele ao ser atingido. 30 Spirit.", "Evasion per stage; knocks back when hit. 30 Spirit."), "opt", 2, SP30),
   G("Into the Breach", ["Harmonic Remnants II", "Remnant Potency III"], L("Chamas roxas", "Purple flames"), L("Mesmo papel.", "Same role."), "free"),
  ],
  cheap=["Slivertongue", "Quatl's Molt", L("Aljava com físico + raio", "Quiver with physical + lightning")],
  full=[L("Peito de Evasão com Spirit", "Evasion chest with Spirit"), L("Amuleto com Spirit", "Amulet with Spirit")],
  stats=[L("Spirit", "Spirit"), L("Dano plano (Repulsion também usa)", "Flat damage (Repulsion uses it too)"), L("Inteligência", "Intelligence")],
  tree=L("Notables de veneno e primeiro caminho de Evasion/ES.", "Poison notables and first Evasion/ES path."),
  avoid=[L("Blasphemy sem Inteligência", "Blasphemy without Intelligence")],
  exit=[L("Lythara (+40 Spirit)", "Lythara (+40 Spirit)"), L("Três heralds/buffs ativos", "Three heralds/buffs active")]),

 dict(id="maps", name=L("Mapas", "Maps"), lv=[65, 79], tag=L("Snapshot do Set 2 + Chayula's Gift", "Set 2 snapshot + Chayula's Gift"),
  carry=L("Você: veneno em cadeia", "You: chained poison"), dmgSplit=[100, 0],
  goal=L("O truque dos mapas: o Weapon Set 2 tem SÓ nós de Remnant. Entre em qualquer área com o Set 2 (Talisman em Wolf Form deixa óbvio) e troque para o Set 1 — os nós ficam 'snapshotados' a área inteira. Esqueceu? Relog ou saia e entre. 3ª ascendência: Chayula's Gift (Chaos Resistance dobrada, +10% máxima). Ghost Dance substitui o Pounce quando sobrar Spirit. Fork no Poisonburst. Peito de Evasão alta e capacete de ES pura para Subterfuge Mask.",
         "The maps trick: Weapon Set 2 has ONLY Remnant nodes. Enter any area with Set 2 (a Talisman in Wolf Form makes it obvious) and swap to Set 1 — the nodes stay 'snapshotted' for the whole area. Forgot? Relog or leave and re-enter. 3rd ascendancy: Chayula's Gift (Chaos Resistance doubled, +10% max). Ghost Dance replaces Pounce when Spirit allows. Fork on Poisonburst. High Evasion chest and pure ES helmet for Subterfuge Mask."),
  rotation=[L("Entre na área com o Set 2 → troque para o Set 1", "Enter the area on Set 2 → swap to Set 1"), L("Poisonburst Arrow até o Plague Bearer encher", "Poisonburst Arrow until Plague Bearer fills"), L("Boss: Vine Arrow → Toxic Growth → Plague Bearer → Toxic Growth", "Boss: Vine Arrow → Toxic Growth → Plague Bearer → Toxic Growth")],
  gems=[
   G("Poisonburst Arrow", ["Bleed III", "Bursting Plague", "Escalating Poison", "Deadly Poison II", "Fork"], L("Clear fora da tela", "Off-screen clear"), L("Fork.", "Fork."), "free"),
   G("Toxic Growth", ["Concentrated Area", "Escalating Poison", "Deadly Poison II", "Long Fuse II", "Arakaali's Lust"], L("Alvo único", "Single target"), L("Arakaali's Lust: lineage barata.", "Arakaali's Lust: cheap lineage."), "free"),
   G("Vine Arrow", ["Prolonged Duration II", "Deliberation", "Swift Affliction II", "Magnified Area II", "Stoicism II"], L("Abre o boss", "Opens the boss"), L("Mesmo papel.", "Same role."), "free"),
   G("Plague Bearer", ["Chaos Mastery", "Astral Projection", "Deadly Poison II", "Exploit Weakness", "Magnified Area II"], L("Burst à distância", "Ranged burst"), L("Astral Projection: à distância.", "Astral Projection: ranged."), "core", 1, SP30),
   G("Herald of Blood", ["Poison III", "Bursting Plague", "Bleed III", "Magnified Area II", "Admixture"], L("Explosões", "Explosions"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Herald of Plague", ["Chaos Mastery"], L("Espalha veneno", "Spreads poison"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Wind Dancer", ["Rage II", "Maim", "Blind II", "Life Leech III"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Ghost Dance", ["Cooldown Recovery II"], L("Recuperação", "Recovery"), L("Ghost Shrouds recuperam ES pela Evasão. Qualidade reduz o custo.", "Ghost Shrouds recover ES based on Evasion. Quality lowers the cost."), "opt", 1, SP30),
   G("Blasphemy", ["Repulsion", "Magnified Area II", "Bleed III", "Living Lightning II"], L("Repulsion", "Repulsion"), L("Boss: troque Repulsion por Despair.", "Bosses: swap Repulsion for Despair."), "opt", 2, L("Confira no jogo", "Check in game")),
   G("Into the Breach", ["Harmonic Remnants II", "Remnant Potency III", "Khatal's Rejuvenation"], L("Chamas roxas", "Purple flames"), L("Khatal's: cooldown do Ghost Dance.", "Khatal's: Ghost Dance cooldown."), "free"),
  ],
  cheap=[L("Talisman no Set 2 (Hysseg's Claw)", "Talisman on Set 2 (Hysseg's Claw)"), "Nascent Hope", "Ngamahu's Chosen"],
  full=[L("Obliterator Bow + Countess Seske's Rune of Archery + Idol of Thruldana", "Obliterator Bow + Countess Seske's Rune of Archery + Idol of Thruldana"), L("Primed Quiver", "Primed Quiver"), L("Remnant effect em anéis/amuleto (Omen of the Liege)", "Remnant effect on rings/amulet (Omen of the Liege)")],
  stats=[L("+ nível de projéteis", "+ projectile levels"), L("Dano plano em anéis, luvas e aljava", "Flat damage on rings, gloves and quiver"), L("Remnant effect", "Remnant effect"), L("Evasão/ES e Spirit", "Evasion/ES and Spirit")],
  tree=L("Set 2: só nós de Remnant (Remnant Attraction primeiro). Set 1: dano (Master Fletching). Defesa: Subterfuge Mask.", "Set 2: only Remnant nodes (Remnant Attraction first). Set 1: damage (Master Fletching). Defence: Subterfuge Mask."),
  avoid=[L("Entrar no mapa com o Set 1", "Entering the map on Set 1")],
  exit=[L("3ª ascendência: Chayula's Gift", "3rd ascendancy: Chayula's Gift"), L("Breach: matar Tul e Esh", "Breach: kill Tul and Esh")]),

 dict(id="archon", name=L("Archon de Chayula", "Archon of Chayula"), lv=[80, 89], tag=L("Tornados de caos", "Chaos tornadoes"),
  carry=L("Você + tornados do Archon", "You + Archon tornadoes"), dmgSplit=[70, 30],
  goal=L("Complete a questline do Breach (Tul e Esh) e pegue Archon of Chayula no último Trial. Ganhe Glory causando caos (100 de Glory, cerca de 1 segundo atacando) e vire o Archon: 20% more dano físico e de caos, 25% de chance de Wither por acerto e um tornado de caos a cada 3 s — cada tornado dura 8 s, persegue, bate 5×/s e detona as pústulas da Toxic Growth assim que nascem. Depois do buff há 20 s de bloqueio — o instill oculto Dominion remove o bloqueio (buff menor). Capacete com Cyclonic Alloy melhora o uptime.",
         "Finish the Breach questline (Tul and Esh) and take Archon of Chayula on the last Trial. Build Glory by dealing chaos (100 Glory, about a second of attacking) and become the Archon: 20% more physical and chaos damage, 25% chance to Wither on hit and one chaos tornado every 3 s — each lasts 8 s, chases, hits 5×/s and pops Toxic Growth pustules as they spawn. After the buff there's a 20 s lockout — the hidden Dominion instill removes it (smaller buff). A Cyclonic Alloy helmet improves uptime."),
  rotation=[L("Archon of Chayula sempre que disponível", "Archon of Chayula whenever available"), L("Vine Arrow algumas vezes", "Vine Arrow a few times"), L("Toxic Growth a cada dois ataques (os tornados detonam)", "Toxic Growth every other attack (tornadoes detonate)"), L("Plague Bearer", "Plague Bearer"), L("Muito dano no Archon: spam de Toxic Growth", "Very high Archon damage: spam Toxic Growth")],
  gems=[
   G("Archon of Chayula", ["Prolonged Duration II", "Magnified Area II", "Poison III", "Withering Touch", "Corrosion"], L("Buff + tornados", "Buff + tornadoes"), L("Precisa de 100 de Glory (~1 s acertando com caos). Ativo: 20% more físico/caos, Wither por acerto e um tornado a cada 3 s; o Poison III faz os tornados detonarem as pústulas.", "Needs 100 Glory (~1 s of chaos hits). Active: 20% more physical/chaos, Wither on hit and a tornado every 3 s; Poison III makes the tornadoes detonate pustules."), "free"),
   G("Poisonburst Arrow", ["Bleed III", "Bursting Plague", "Escalating Poison", "Deadly Poison II", "Fork"], L("Clear", "Clear"), L("Mesmo papel.", "Same role."), "free"),
   G("Toxic Growth", ["Concentrated Area", "Escalating Poison", "Deadly Poison II", "Long Fuse II", "Arakaali's Lust"], L("Alvo único", "Single target"), L("Mesmo papel.", "Same role."), "free"),
   G("Vine Arrow", ["Prolonged Duration II", "Deliberation", "Swift Affliction II", "Magnified Area II", "Stoicism II"], L("Abre o boss", "Opens the boss"), L("Mesmo papel.", "Same role."), "free"),
   G("Plague Bearer", ["Chaos Mastery", "Astral Projection", "Deadly Poison II", "Exploit Weakness", "Magnified Area II"], L("Burst", "Burst"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Herald of Blood", ["Poison III", "Bursting Plague", "Bleed III", "Magnified Area II", "Admixture"], L("Explosões", "Explosions"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Herald of Plague", ["Chaos Mastery"], L("Espalha veneno", "Spreads poison"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Wind Dancer", ["Rage II", "Maim", "Blind II", "Life Leech III"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Ghost Dance", ["Cooldown Recovery II"], L("Recuperação", "Recovery"), L("30 Spirit.", "30 Spirit."), "core", 5, SP30),
   G("Blasphemy", ["Repulsion", "Magnified Area II", "Bleed III", "Living Lightning II"], L("Repulsion", "Repulsion"), L("Boss: Despair.", "Bosses: Despair."), "opt", 1, L("Confira no jogo", "Check in game")),
   G("Into the Breach", ["Harmonic Remnants II", "Remnant Potency III", "Khatal's Rejuvenation"], L("Chamas roxas", "Purple flames"), L("Mesmo papel.", "Same role."), "free"),
  ],
  cheap=[L("Capacete de ES com Cyclonic Alloy", "ES helmet with Cyclonic Alloy"), L("Rune of Reach no capacete", "Rune of Reach in the helmet")],
  full=[L("Instill Dominion no amuleto", "Dominion instill on the amulet"), "The Fall of the Axe"],
  stats=[L("Dano de caos", "Chaos damage"), L("Duração (tornados)", "Duration (tornadoes)"), L("Chaos Resistance (dobrada)", "Chaos Resistance (doubled)")],
  tree=L("4ª ascendência: Archon of Chayula. Spectral Ward com Evasão/ES.", "4th ascendancy: Archon of Chayula. Spectral Ward with Evasion/ES."),
  avoid=[L("Lançar Toxic Growth sem parar fora do Archon", "Nonstop Toxic Growth outside Archon")],
  exit=[L("Archon + rotação de boss", "Archon + boss rotation"), L("~40% de crítico para o min-max", "~40% crit for min-max")]),

 dict(id="max", name=L("Min-max: crítico", "Min-max: crit"), lv=[90, 100], tag=L("Garukhan's Resolve + Mageblood", "Garukhan's Resolve + Mageblood"),
  carry=L("Você crítico + Archon", "Crit you + Archon"), dmgSplit=[65, 35],
  goal=L("Para o min-max a build vira crítico: meta de 50% de chance (capacete, aljava, amuleto e jewels) para Garukhan's Resolve na Toxic Growth. Absent Amulet com implicit de Eternal Rage libera Tacati's Ire; Her Declaration no Ghost Dance. Time-Lost Emerald de raio grande perto de Dizzying Hits/Stupefy com crítico. Craiceann's Rune of Warding + The Hollowkeeper = imune a curses. Mageblood (ou Headhunter) e Rite of Passage (Cat; Serpent é a alternativa barata).",
         "For min-max the build goes crit: 50% chance goal (helmet, quiver, amulet and jewels) for Garukhan's Resolve on Toxic Growth. An Absent Amulet with the Eternal Rage implicit enables Tacati's Ire; Her Declaration on Ghost Dance. A large-radius Time-Lost Emerald near Dizzying Hits/Stupefy with crit. Craiceann's Rune of Warding + The Hollowkeeper = curse immune. Mageblood (or Headhunter) and Rite of Passage (Cat; Serpent is the cheap alternative)."),
  rotation=[L("Archon of Chayula", "Archon of Chayula"), L("Vine Arrow x2", "Vine Arrow x2"), L("Toxic Growth → Plague Bearer → Toxic Growth", "Toxic Growth → Plague Bearer → Toxic Growth")],
  gems=[
   G("Archon of Chayula", ["Prolonged Duration II", "Magnified Area II", "Poison III", "Withering Touch", "Uul-Netol's Embrace"], L("Buff + tornados", "Buff + tornadoes"), L("Uul-Netol's: Armour Break.", "Uul-Netol's: Armour Break."), "free"),
   G("Toxic Growth", ["Concentrated Area", "Deadly Poison II", "Long Fuse II", "Arakaali's Lust", "Garukhan's Resolve"], L("Alvo único crítico", "Crit single target"), L("Garukhan's só com ~50% de crítico.", "Garukhan's only at ~50% crit."), "free"),
   G("Poisonburst Arrow", ["Bleed III", "Bursting Plague", "Escalating Poison", "Deadly Poison II", "Fork"], L("Clear", "Clear"), L("Mesmo papel.", "Same role."), "free"),
   G("Vine Arrow", ["Prolonged Duration II", "Deliberation", "Swift Affliction II", "Magnified Area II", "Stoicism II"], L("Abre o boss", "Opens the boss"), L("Mesmo papel.", "Same role."), "free"),
   G("Plague Bearer", ["Astral Projection", "Tacati's Ire", "Vorana's Siege", "Deadly Poison II", "Exploit Weakness"], L("Burst", "Burst"), L("Tacati's Ire com Rage do Absent Amulet.", "Tacati's Ire with Rage from Absent Amulet."), "core", 1, SP30),
   G("Herald of Blood", ["Poison III", "Bursting Plague", "Bleed III", "Magnified Area II", "Admixture"], L("Explosões", "Explosions"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Herald of Plague", ["Chaos Mastery"], L("Espalha veneno", "Spreads poison"), L("30 Spirit.", "30 Spirit."), "core", 3, SP30),
   G("Wind Dancer", ["Rage II", "Maim", "Blind II", "Life Leech III"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Ghost Dance", ["Cooldown Recovery II", "Her Declaration"], L("Recuperação", "Recovery"), L("Her Declaration fica mais barata aqui.", "Her Declaration is cheaper here."), "core", 5, SP30),
   G("Blasphemy", ["Repulsion", "Magnified Area II", "Bleed III", "Living Lightning II", "Poison III"], L("Repulsion", "Repulsion"), L("Mesmo papel.", "Same role."), "opt", 1, L("Confira no jogo", "Check in game")),
   G("Into the Breach", ["Harmonic Remnants II", "Remnant Potency III", "Khatal's Rejuvenation"], L("Chamas roxas", "Purple flames"), L("Mesmo papel.", "Same role."), "free"),
  ],
  cheap=[L("Absent Amulet (Eternal Rage) com Spirit e + projéteis", "Absent Amulet (Eternal Rage) with Spirit and + projectiles"), "The Fall of the Axe", "Nascent Hope"],
  full=["Mageblood", "Rite of Passage", L("Time-Lost Emerald (raio grande)", "Time-Lost Emerald (large radius)")],
  stats=[L("Chance de crítico até 50%", "Crit chance up to 50%"), L("Onslaught ao matar no arco", "Onslaught on kill on the bow"), L("Movement speed", "Movement speed")],
  tree=L("Notables de crítico: Heartstopping, Heartbreaking, Struck Through, True Strike, For the Jugular. Defesa: Enhanced Reflexes, Beastial Skin.", "Crit notables: Heartstopping, Heartbreaking, Struck Through, True Strike, For the Jugular. Defence: Enhanced Reflexes, Beastial Skin."),
  avoid=[L("Garukhan's Resolve abaixo de 50% de crítico", "Garukhan's Resolve below 50% crit"), L("Mageblood sem Diamond Flask sem 50% de crítico", "Mageblood without Diamond Flask when under 50% crit")],
  exit=[L("Pinnacles e mapas juiced", "Pinnacles and juiced maps")]),
]
PH = {p["id"]: p for p in PHASES}

# Alternativa real de alvo único a partir da Uncut Skill Gem de tier 7. A explosão
# de fogo não é necessária: o papel nesta build é manter a nuvem envenenando as
# pústulas da Toxic Growth e o boss.
GAS_ARROW = G("Gas Arrow", ["Persistent Ground II"], L("Boss: nuvem sobre as pústulas", "Boss: cloud over the pustules"),
              L("A nuvem dura 4 s, aplica veneno sem hit e pode manter boss e pústulas sendo envenenados. Não detone: a explosão converte físico em fogo e não é o foco da build.",
                "The cloud lasts 4s, poisons without hitting and can keep both boss and pustules poisoned. Do not detonate it: the explosion converts physical to fire and is not this build's focus."), "free", since=22)
for _phase in PHASES:
    if _phase["id"] in ("a2", "a3", "a4", "maps", "archon", "max"):
        _phase["gems"].append(copy.deepcopy(GAS_ARROW))

BOX = {
 "a2": ("1", [L("Toxic Growth por vez", "Toxic Growth at a time")], L("Relançar antes das pústulas explodirem destrói as antigas.", "Recasting before the pustules explode destroys the old ones.")),
 "a3": ("100%", [L("Plague Bearer", "Plague Bearer")], L("Ative o Plague Bearer só com 100% guardado.", "Activate Plague Bearer only at 100% stored.")),
 "maps": ("Set 2", [L("ao entrar na área", "when entering the area")], L("Entre com o Set 2, troque para o Set 1: os nós de Remnant ficam ativos.", "Enter on Set 2, swap to Set 1: Remnant nodes stay active.")),
 "archon": ("20 s", [L("bloqueio do Archon", "Archon lockout")], L("Depois do buff, 20 s até poder usar de novo (Dominion remove).", "After the buff, 20 s before reuse (Dominion removes it).")),
 "max": ("50%", [L("chance de crítico", "crit chance")], L("Meta para Garukhan's Resolve.", "Goal for Garukhan's Resolve.")),
}
SPIRIT_NOTE = {
 "a1": L("Herald of Blood (30).", "Herald of Blood (30)."),
 "a3": L("Herald of Blood (30) + Plague Bearer (30).", "Herald of Blood (30) + Plague Bearer (30)."),
 "a4": L("+ Herald of Plague (30), Wind Dancer (30); Blasphemy com Spirit do equipamento.", "+ Herald of Plague (30), Wind Dancer (30); Blasphemy with gear Spirit."),
 "maps": L("Ordem: Plague Bearer → Herald of Blood → Herald of Plague → Wind Dancer → Ghost Dance → Blasphemy.", "Order: Plague Bearer → Herald of Blood → Herald of Plague → Wind Dancer → Ghost Dance → Blasphemy."),
 "archon": L("Cinco buffs de 30 (150) + Blasphemy: peito e amuleto com Spirit alto.", "Five 30-Spirit buffs (150) + Blasphemy: chest and amulet with high Spirit."),
 "max": L("+ Her Declaration no Ghost Dance.", "+ Her Declaration on Ghost Dance."),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in SPIRIT_NOTE.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Poisonburst Arrow + Vine Arrow.", "Poisonburst Arrow + Vine Arrow."),
 10: L("King in the Mists (+30): Herald of Blood com Bleed I e Bursting Plague.", "King in the Mists (+30): Herald of Blood with Bleed I and Bursting Plague."),
 8: L("Surefooted Sigil e Blackheart: vida, dodge e caos plano.", "Surefooted Sigil and Blackheart: life, dodge and flat chaos."),
 11: L("Goldrim (resistências) e Wanderlust (20% MS).", "Goldrim (resistances) and Wanderlust (20% MS)."),
 14: L("Toxic Growth + Concentrated Area.", "Toxic Growth + Concentrated Area."),
 16: L("Splinterheart + The Lethal Draw; Ghostmarch nas botas.", "Splinterheart + The Lethal Draw; Ghostmarch on boots."),
 28: L("Atsak's Sight (crítico envenena) e Death's Harp (flecha extra).", "Atsak's Sight (crits poison) and Death's Harp (extra arrow)."),
 33: L("Snakebite: +1 veneno simultâneo.", "Snakebite: +1 simultaneous poison."),
 36: L("Icefang Orbit e Quatl's Molt.", "Icefang Orbit and Quatl's Molt."),
 39: L("Slivertongue: Fork e Pierce no arco.", "Slivertongue: Fork and Pierce on the bow."),
 24: L("1ª ascendência: Waking Dream (chamas de Chayula).", "1st ascendancy: Waking Dream (Flames of Chayula)."),
 24: L("Despair (Uncut lv 9): curse de boss, todo o seu dano é caos.", "Despair (level 9 Uncut): boss curse, all your damage is chaos."),
 35: L("Azak Bog (+30): Plague Bearer. Notables de veneno.", "Azak Bog (+30): Plague Bearer. Poison notables."),
 40: L("2ª ascendência: Choice of Power. Runeforge o Splinterheart.", "2nd ascendancy: Choice of Power. Runeforge Splinterheart."),
 50: L("Herald of Plague; Blasphemy + Repulsion com Spirit no equipamento.", "Herald of Plague; Blasphemy + Repulsion with gear Spirit."),
 62: L("Lythara (+40 Spirit). Wind Dancer.", "Lythara (+40 Spirit). Wind Dancer."),
 65: L("Talisman no Set 2: snapshot dos nós de Remnant.", "Talisman on Set 2: Remnant node snapshot."),
 68: L("3ª ascendência: Chayula's Gift. Fork no Poisonburst.", "3rd ascendancy: Chayula's Gift. Fork on Poisonburst."),
 72: L("Ghost Dance no lugar do Pounce. Obliterator Bow + runas.", "Ghost Dance instead of Pounce. Obliterator Bow + runes."),
 80: L("Breach (Tul e Esh) → Archon of Chayula.", "Breach (Tul and Esh) → Archon of Chayula."),
 90: L("Min-max crítico: Garukhan's Resolve, Absent Amulet, Mageblood.", "Crit min-max: Garukhan's Resolve, Absent Amulet, Mageblood."),
}

ASCENDANCY = [
 dict(order=1, key="waking", node="Waking Dream", when=L("1º Trial (~nível 24)", "1st Trial (~level 24)"), text=L("Concede Into the Breach: chamas de Chayula nascem em volta de você como Remnants.", "Grants Into the Breach: Flames of Chayula spawn around you as Remnants."), why=L("Roxa = 7% do dano como caos; vermelha = leech de vida; azul = leech de mana.", "Purple = 7% of damage as chaos; red = life leech; blue = mana leech.")),
 dict(order=2, key="power", node=L("Lucid Dreaming → Choice of Power", "Lucid Dreaming → Choice of Power"), when=L("2º Trial (~nível 40)", "2nd Trial (~level 40)"), text=L("Lucid Dreaming é o nó de escolha: selecione Choice of Power. As Remnants ficam 50% mais fortes, são coletadas 50% mais longe e todas as chamas passam a ser roxas.", "Lucid Dreaming is the choice node: select Choice of Power. Remnants become 50% stronger, are collected from 50% farther away and every flame becomes purple."), why=L("É uma única escolha de ascendência, não dois pontos separados.", "This is one ascendancy choice, not two separate points.")),
 dict(order=3, key="gift", node="Chayula's Gift", when=L("3º Trial (~nível 68)", "3rd Trial (~level 68)"), text=L("+10% Chaos Resistance máxima; Chaos Resistance dobrada.", "+10% maximum Chaos Resistance; Chaos Resistance doubled."), why=L("Caos no cap fácil e caminho para o Archon.", "Easy chaos cap and path to Archon.")),
 dict(order=4, key="archon", node="Archon of Chayula", when=L("4º Trial + Breach (~nível 80)", "4th Trial + Breach (~level 80)"), text=L("Concede a skill Archon of Chayula: com 100 de Glory você vira o Archon por alguns segundos e invoca um tornado de caos a cada 3 s (8 s cada, 5 acertos por segundo).", "Grants the Archon of Chayula skill: at 100 Glory you become the Archon for a few seconds and summon a chaos tornado every 3 s (8 s each, 5 hits per second)."), why=L("20% more físico e caos, 25% de Wither por acerto e tornados que envenenam/detonam as pústulas com Poison III. Só libera depois de matar Tul e Esh no Breach.", "20% more physical and chaos, 25% Wither on hit and tornadoes that poison/pop pustules with Poison III. Only unlocks after killing Tul and Esh in Breach.")),
]
ASC_UNLOCK = [24, 40, 68, 80]
ASC_PHASE = {"a2": ["Waking Dream"], "a3": ["Waking Dream", "Choice of Power"], "a4": ["Waking Dream", "Choice of Power"]}

KEY_PASSIVES = [
 dict(node="Choice of Power", type=L("Ascendência", "Ascendancy"), text=L("Todas as chamas roxas, 50% mais efeito.", "All flames purple, 50% more effect."), when="40+", why=L("Dano como caos multiplicado.", "Multiplied damage as chaos.")),
 dict(node="Subterfuge Mask", type="Notable", text=L("Defesa com capacete de ES pura.", "Defence with a pure ES helmet."), when="65+", why=L("Pede capacete só de ES.", "Needs an ES-only helmet.")),
 dict(node="Master Fletching", type="Notable", text=L("Dano de arco no Set 1.", "Bow damage on Set 1."), when="65+", why=L("Set 1 = dano.", "Set 1 = damage.")),
 dict(node="The Hollowkeeper", type="Notable", text=L("Com Craiceann's Rune of Warding: imune a curses.", "With Craiceann's Rune of Warding: curse immune."), when="45+", why=L("Pede First Teachings of the Keeper e First Principle of the Hollow.", "Requires First Teachings of the Keeper and First Principle of the Hollow.")),
]
TREE_STAGES = [
 dict(lv="1–29", focus=L("increased Damage", "increased Damage"), dmg="Poisonburst + Toxic Growth", **{"def": L("Vida + resist", "Life + resist")}, spirit="Herald of Blood", dont=L("Relançar Toxic Growth", "Recasting Toxic Growth")),
 dict(lv="30–64", focus=L("Notables de veneno", "Poison notables"), dmg="Plague Bearer + Heralds", **{"def": L("Evasão/ES", "Evasion/ES")}, spirit="PB, HoB, HoP", dont=L("Blasphemy sem Int", "Blasphemy without Int")),
 dict(lv="65–89", focus=L("Set 2 = Remnants", "Set 2 = Remnants"), dmg="Archon of Chayula", **{"def": "Subterfuge Mask · Spectral Ward"}, spirit="+ Wind Dancer, Ghost Dance", dont=L("Entrar no mapa no Set 1", "Entering maps on Set 1")),
 dict(lv="90–100", focus=L("Crítico", "Crit"), dmg="Garukhan's Resolve", **{"def": "Enhanced Reflexes · Beastial Skin"}, spirit="Her Declaration", dont=L("Crítico abaixo de 50%", "Crit below 50%")),
]

UNIQUES = [
 U("Plaguefinger", L("Luvas", "Gloves"), L("Armadura", "Armour"), "a1", L("Evasão/ES, attack speed, 20–30% de chance de envenenar e TODO o dano do hit conta para a força do veneno (não aplica ailments elementais).", "Evasion/ES, attack speed, 20–30% chance to poison and ALL hit damage counts towards poison magnitude (can't inflict elemental ailments)."), L("A melhor unique de nível 1 para a build: some dano de veneno desde o Ato 1 e custa quase nada.", "The best level 1 unique for this build: it adds poison damage from Act 1 and costs almost nothing."), L("Luvas com dano plano.", "Gloves with flat damage.")),
 U("Luminous Pace", L("Botas", "Boots"), L("Armadura", "Armour"), "a1", L("10% Movement Speed, ES e recarga de ES bem mais rápida.", "10% Movement Speed, ES and much faster ES recharge start."), L("Primeiras botas; troque pela Wanderlust no nível 11.", "First boots; swap to Wanderlust at level 11."), L("Botas com Movement Speed.", "Boots with Movement Speed.")),
 U("Meginord's Girdle", L("Cinto", "Belt"), L("Acessório", "Accessory"), "a1", L("+40–50 Força, resistência a frio e o dobro de cargas de flask.", "+40–50 Strength, cold resistance and double flask charges."), L("Resolve a Força que falta para equipar peito/capacete no começo.", "Solves the Strength you're missing for early chest/helmet."), L("Cinto com vida.", "Belt with life.")),
 U("Blackheart", L("Anel", "Ring"), L("Acessório", "Accessory"), "a1", L("Regen de vida, caos adicionado a ataques, Armour aplica a caos.", "Life regen, added chaos to attacks, Armour applies to chaos."), L("Anel barato do leveling.", "Cheap leveling ring."), L("Anel com dano plano.", "Ring with flat damage.")),
 U("Asphyxia's Wrath", L("Aljava", "Quiver"), L("Arma", "Weapon"), "a1", L("Frio plano, frio extra nos ataques, attack speed e inimigos com Chill tomam mais dano.", "Flat cold, extra cold on attacks, attack speed and chilled enemies take more damage."), L("Aljava de nível 1; qualquer aljava com dano plano serve.", "Level 1 quiver; any quiver with flat damage works."), "Blackgleam"),
 U("Blackgleam", L("Aljava", "Quiver"), L("Arma", "Weapon"), "a1", L("Fogo plano, fogo extra nos ataques, mana e projéteis perfuram inimigos em Ignite.", "Flat fire, extra fire on attacks, mana and projectiles pierce ignited enemies."), L("Aljava do nível 8 até a The Lethal Draw (16).", "Level 8 quiver until The Lethal Draw (16)."), "Asphyxia's Wrath"),
 U("Surefooted Sigil", L("Amuleto", "Amulet"), L("Acessório", "Accessory"), "a1", L("+40–60 vida, Destreza, +1 m de Dodge Roll e evasão depois do dodge.", "+40–60 life, Dexterity, +1 m Dodge Roll and evasion after dodging."), L("Vida e mobilidade baratas até o amuleto com Spirit.", "Cheap life and mobility until the Spirit amulet."), L("Amuleto com vida e atributos.", "Amulet with life and attributes.")),
 U("Goldrim", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a2", L("+25–33% em TODAS as resistências elementais e raridade.", "+25–33% to ALL elemental resistances and rarity."), L("Segura suas resistências sozinho do 10 até uns 40 — o capacete mais tranquilo da campanha.", "Holds your resistances by itself from 10 to about 40 — the easiest campaign helmet."), L("Capacete com vida e resistências.", "Helmet with life and resistances.")),
 U("Wanderlust", L("Botas", "Boots"), L("Armadura", "Armour"), "a2", L("20% Movement Speed, ES e imunidade a Slow.", "20% Movement Speed, ES and immunity to slows."), L("Dobro de velocidade das Luminous Pace no nível 11.", "Double the movement of Luminous Pace at level 11."), "Ghostmarch"),
 U("Splinterheart", L("Arco", "Bow"), L("Arma", "Weapon"), "a2", L("% dano físico, precisão, velocidade de projétil e projéteis se dividem para +2 alvos.", "% physical damage, accuracy, projectile speed and projectiles split towards +2 targets."), L("Melhor arco do leveling; runeforge no 40 e dura até os mapas.", "Best leveling bow; runeforge at 40 and it lasts into maps."), L("Arco rare com físico.", "Rare physical bow.")),
 U("The Lethal Draw", L("Aljava", "Quiver"), L("Arma", "Weapon"), "a2", L("Attack speed, vida por inimigo acertado, chance de perfurar e ataques de arco consomem 10% das cargas máximas do Life Flask para ganhar físico igual a 5–10% da recuperação do flask.", "Attack speed, life per enemy hit, pierce chance, and bow attacks consume 10% of maximum Life Flask charges to gain physical damage equal to 5–10% of the flask's recovery."), L("É dano de leveling muito alto enquanto há cargas. Em boss longo, vigie o flask: sem cargas você perde o físico extra e parte do sustain.", "It is very high levelling damage while charges remain. On long bosses, watch the flask: without charges you lose the added physical and part of your sustain."), L("Aljava com dano plano e sem consumo de flask.", "Flat-damage quiver without flask consumption.")),
 U("Ghostmarch", L("Botas", "Boots"), L("Armadura", "Armour"), "a2", L("15% Movement Speed, Evasão/ES alta, mana, resistência a caos e Dodge Roll atravessa inimigos.", "15% Movement Speed, high Evasion/ES, mana, chaos resistance and Dodge Roll passes through enemies."), L("Atravessar inimigos no dodge salva muita morte boba na campanha.", "Dodging through enemies prevents a lot of silly campaign deaths."), L("Botas com 25–30% MS.", "Boots with 25–30% MS.")),
 U("Amor Mandragora", L("Talisman (Set 2)", "Talisman (Set 2)"), L("Arma", "Weapon"), "a2", L("Físico adicionado, Inteligência, duração de skill, Hinder na Presence.", "Added physical, Intelligence, skill duration, Hinder in Presence."), L("Talisman do Set 2 no leveling (Pounce).", "Set 2 leveling talisman (Pounce)."), "Hysseg's Claw"),
 U("Atsak's Sight", L("Capacete", "Helmet"), L("Armadura", "Armour"), "a3", L("Evasão/ES dobrada, +30–40% de chance de crítico, Destreza, Inteligência e críticos envenenam.", "Doubled Evasion/ES, +30–40% crit chance, Dexterity, Intelligence and critical hits poison."), L("Troca do Goldrim quando as resistências já vêm dos rares: crítico + veneno de graça.", "Replaces Goldrim once rares cover resistances: crit + poison for free."), L("Capacete de ES.", "ES helmet.")),
 U("Death's Harp", L("Arco", "Bow"), L("Arma", "Weapon"), "a3", L("Dano crítico, vida e mana por inimigo morto, +50% implícito e +250–330% de Surpassing chance de disparar flecha adicional.", "Crit damage, life and mana per enemy killed, +50% implicit and +250–330% Surpassing chance to fire an additional arrow."), L("O total de 300–380% gera três flechas adicionais garantidas e chance para a quarta. Excelente cobertura, mas o físico base é baixo: compare o dano de Toxic Growth com a Splinterheart runeforged antes de trocar.", "The 300–380% total grants three guaranteed additional arrows and a chance for a fourth. Excellent coverage, but base physical is low: compare Toxic Growth damage with a runeforged Splinterheart before swapping."), "Splinterheart"),
 U("Snakebite", L("Luvas", "Gloves"), L("Armadura", "Armour"), "a3", L("Evasão, resistência a caos, regen e 20–30% de chance de envenenar; alvos podem ter +1 dos seus venenos ao mesmo tempo.", "Evasion, chaos resistance, regen and 20–30% chance to poison; targets can be affected by +1 of your poisons at once."), L("+1 veneno simultâneo no boss — a build empilha veneno, então isso é dano direto.", "+1 simultaneous poison on bosses — the build stacks poison, so it's direct damage."), "Plaguefinger"),
 U("Icefang Orbit", L("Anel", "Ring"), L("Acessório", "Accessory"), "a3", L("Físico plano em ataques, +20–30 Destreza, chance de envenenar e +15–25% de magnitude do veneno.", "Flat physical on attacks, +20–30 Dexterity, poison chance and +15–25% poison magnitude."), L("Substitui o Blackheart: dano plano e veneno mais forte, e a Destreza ajuda no requisito do arco.", "Replaces Blackheart: flat damage and stronger poison, and the Dexterity helps with bow requirements."), "Blackheart"),
 U("Quatl's Molt", "Body Armour", L("Armadura", "Armour"), "a4", L("Evasão, +60–79 vida, resistência a caos, Deflection pela Evasão, regen e imune a veneno.", "Evasion, +60–79 life, chaos resistance, Deflection from Evasion, regen and can't be poisoned."), L("Peito de campanha completo: vida, caos e defesa. Sai quando você precisar de Spirit no peito.", "A complete campaign chest: life, chaos and defence. It leaves when you need Spirit on the chest."), L("Peito de Evasão com Spirit.", "Evasion chest with Spirit.")),
 U("Slivertongue", L("Arco", "Bow"), L("Arma", "Weapon"), "a4", L("Físico alto, +4–6% de crítico, leech de vida e mana e as flechas se dividem (Fork) e perfuram tudo depois de dividir.", "High physical, +4–6% crit, life and mana leech, and arrows Fork and pierce everything after forking."), L("Fork de graça no arco: o clear do Ato 4 e dos primeiros mapas fica parecido com o do endgame.", "Free Fork on the bow: Act 4 and early maps clear like the endgame setup."), L("Splinterheart runeforged.", "Runeforged Splinterheart.")),
 U("Sanguis Heroum", "Charm", "Charm", "a3", L("Ganha cargas sozinho e cria Consecrated Ground ao usar.", "Gains charges on its own and creates Consecrated Ground on use."), L("Charm de cura barato para a campanha.", "Cheap healing charm for the campaign."), "Nascent Hope"),
 U("Hysseg's Claw", L("Talisman (Set 2)", "Talisman (Set 2)"), L("Arma", "Weapon"), "maps", L("% físico, 5% movement speed, atributos.", "% physical, 5% movement speed, attributes."), L("Set 2 do snapshot (Wolf Form).", "Snapshot Set 2 (Wolf Form)."), L("Qualquer Talisman.", "Any Talisman.")),
 U("Nascent Hope", "Charm", "Charm", "maps", L("Recarga de ES ao usar; chance de carga ao matar.", "ES recharge on use; charge chance on kill."), L("Defesa de ES.", "ES defence."), "Thawing Charm"),
 U("Ngamahu's Chosen", "Charm", "Charm", "maps", L("Rage máxima ao usar.", "Maximum Rage on use."), L("Rage barata.", "Cheap Rage."), "Ruby Charm"),
 U("The Fall of the Axe", "Charm", "Charm", "archon", L("Onslaught durante o efeito.", "Onslaught during effect."), L("Velocidade.", "Speed."), "Silver Charm"),
 U("Rite of Passage", "Charm", "Charm", "max", L("Possessão por espíritos (Cat, Stag, Boar, Serpent).", "Spirit possession (Cat, Stag, Boar, Serpent)."), L("Cat é o melhor; Serpent é mais barato.", "Cat is best; Serpent is cheaper."), "The Fall of the Axe"),
 U("Mageblood", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Legados de flask permanentes.", "Permanent flask legacies."), L("Min-max; Diamond Flask se não tiver 50% de crítico.", "Min-max; Diamond Flask if not at 50% crit."), "Headhunter"),
 U("Headhunter", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Ao matar rare, ganha os mods dele por 60 s.", "Killing a rare grants its modifiers for 60 s."), L("Alternativa de luxo para mapas.", "Luxury maps alternative."), L("Cinto rare com vida/resist.", "Rare life/resist belt.")),
]
GEAR = [
 dict(slot=L("Arco", "Bow"), cheap="Splinterheart · Death's Harp (16–28)", value=L("Slivertongue normal (39) ou Splinterheart runeforged (40)", "Normal Slivertongue (39) or runeforged Splinterheart (40)"), full=L("Obliterator Bow: físico, crítico, Onslaught ao matar", "Obliterator Bow: physical, crit, Onslaught on kill"), affix=L("% físico; físico plano; + projéteis; flecha adicional", "% physical; flat physical; + projectiles; additional arrow"), lvls=[dict(lv=1, n=L("Arco magic com físico", "Magic bow with physical")), dict(lv=16, n="Splinterheart"), dict(lv=28, n="Death's Harp"), dict(lv=39, n="Slivertongue"), dict(lv=40, n=L("Splinterheart runeforged (Medved)", "Runeforged Splinterheart (Medved)")), dict(lv=78, n="Obliterator Bow")], note=BOW_RUNE),
 dict(slot=L("Aljava", "Quiver"), cheap="Asphyxia's Wrath · The Lethal Draw", value=L("Rare com físico + raio planos", "Rare with flat physical + lightning"), full=L("Primed Quiver: físico + raio + bow damage + crítico", "Primed Quiver: physical + lightning + bow damage + crit"), affix=L("Dano plano; attack speed", "Flat damage; attack speed"), lvls=[dict(lv=1, n="Asphyxia's Wrath"), dict(lv=8, n="Blackgleam"), dict(lv=16, n="The Lethal Draw"), dict(lv=45, n=L("Rare: físico + raio planos", "Rare: flat physical + lightning")), dict(lv=75, n="Primed Quiver")], note=""),
 dict(slot=L("Talisman (Set 2)", "Talisman (Set 2)"), cheap="Amor Mandragora", value="Hysseg's Claw", full="Hysseg's Claw", affix=L("Só para o snapshot", "Snapshot only"), note=L("Wolf Form.", "Wolf Form.")),
 dict(slot=L("Capacete", "Helmet"), cheap="Goldrim (10) · Atsak's Sight (28)", value=L("Rare de ES pura (Subterfuge Mask)", "Pure ES rare (Subterfuge Mask)"), full=L("ES + crítico + Cyclonic Alloy", "ES + crit + Cyclonic Alloy"), affix=L("% ES; crítico", "% ES; crit"), lvls=[dict(lv=10, n="Goldrim"), dict(lv=28, n="Atsak's Sight"), dict(lv=65, n=L("Rare de ES pura (Subterfuge Mask)", "Pure ES rare (Subterfuge Mask)"))], note="Rune of Reach"),
 dict(slot="Body Armour", cheap=L("Peito de Evasão com vida · Quatl's Molt (36)", "Evasion chest with life · Quatl's Molt (36)"), value=L("Rare: Evasão alta + Spirit", "Rare: high Evasion + Spirit"), full=L("Evasão + Spirit 55+ + Chaos Resistance", "Evasion + 55+ Spirit + Chaos Resistance"), affix=L("Spirit; % Evasão; Deflection", "Spirit; % Evasion; Deflection"), lvls=[dict(lv=1, n=L("Peito de Evasão com vida", "Evasion chest with life")), dict(lv=36, n="Quatl's Molt"), dict(lv=45, n=L("Rare: Evasão + Spirit", "Rare: Evasion + Spirit"))], note="Craiceann's Rune of Warding"),
 dict(slot=L("Luvas", "Gloves"), cheap="Plaguefinger (1) · Snakebite (33)", value=L("Rare: físico + raio planos", "Rare: flat physical + lightning"), full=L("Físico + raio + attack speed ('Marksman': + projéteis)", "Physical + lightning + attack speed ('Marksman': + projectiles)"), affix=L("Dano plano; attack speed", "Flat damage; attack speed"), lvls=[dict(lv=1, n="Plaguefinger"), dict(lv=33, n="Snakebite"), dict(lv=65, n=L("Rare: físico + raio + attack speed", "Rare: physical + lightning + attack speed"))], note=""),
 dict(slot=L("Botas", "Boots"), cheap="Luminous Pace · Wanderlust · Ghostmarch", value=L("Rare: 30% MS + Evasão/ES", "Rare: 30% MS + Evasion/ES"), full=L("30% MS + Deflection", "30% MS + Deflection"), affix=L("MS; ES; resist", "MS; ES; resist"), lvls=[dict(lv=1, n="Luminous Pace"), dict(lv=11, n="Wanderlust"), dict(lv=16, n="Ghostmarch"), dict(lv=60, n=L("Rare: 30% MS + Evasão/ES", "Rare: 30% MS + Evasion/ES"))], note="Farrul's Rune of the Chase"),
 dict(slot=L("Amuleto", "Amulet"), cheap="Surefooted Sigil (8)", value=L("Rare: Spirit + remnant effect", "Rare: Spirit + remnant effect"), full=L("Absent Amulet: Spirit, +3 projéteis, crítico", "Absent Amulet: Spirit, +3 projectiles, crit"), affix=L("Spirit; + projéteis; remnant effect", "Spirit; + projectiles; remnant effect"), lvls=[dict(lv=8, n="Surefooted Sigil"), dict(lv=45, n=L("Rare com Spirit", "Rare with Spirit")), dict(lv=90, n="Absent Amulet")], note=L("Instill: Serrated Edges (barato) ou Dominion.", "Instill: Serrated Edges (cheap) or Dominion.")),
 dict(slot=L("Anéis", "Rings"), cheap="Blackheart (1) · Icefang Orbit (36)", value=L("Rare: físico plano + resist", "Rare: flat physical + resist"), full=L("Físico plano + remnant effect (Liege)", "Flat physical + remnant effect (Liege)"), affix=L("Dano plano; remnant effect; resist", "Flat damage; remnant effect; resist"), lvls=[dict(lv=1, n="Blackheart"), dict(lv=36, n="Icefang Orbit"), dict(lv=60, n=L("Rare: físico plano + resist", "Rare: flat physical + resist"))], note=""),
 dict(slot=L("Cinto", "Belt"), cheap=L("Meginord's Girdle (Força)", "Meginord's Girdle (Strength)"), value=L("Rare: vida + duas resistências", "Rare: life + two resistances"), full="Mageblood · Headhunter", affix=L("Vida; resist", "Life; resist"), lvls=[dict(lv=1, n="Meginord's Girdle"), dict(lv=45, n=L("Rare: vida + resistências", "Rare: life + resistances")), dict(lv=90, n="Mageblood")], note=""),
 dict(slot="Charms", cheap="Nascent Hope · Sanguis Heroum", value="Ngamahu's Chosen · The Fall of the Axe", full="Rite of Passage · The Fall of the Axe", affix="", lvls=[dict(lv=12, n="Nascent Hope"), dict(lv=18, n="Sanguis Heroum"), dict(lv=65, n="Ngamahu's Chosen"), dict(lv=90, n="Rite of Passage")], note=""),
]
BUY_ORDER = [
 dict(p=1, item="Plaguefinger", phase="1+", cost=L("Barato", "Cheap"), impact=L("Veneno desde o nível 1", "Poison from level 1")),
 dict(p=2, item="Goldrim · Wanderlust", phase="10–11", cost=L("Barato", "Cheap"), impact=L("Resistências e velocidade", "Resistances and speed")),
 dict(p=3, item="Splinterheart · The Lethal Draw", phase="16–39", cost=L("Barato", "Cheap"), impact=L("Dano do leveling", "Leveling damage")),
 dict(p=4, item="Snakebite · Icefang Orbit", phase="33–39", cost=L("Barato", "Cheap"), impact=L("Veneno mais forte", "Stronger poison")),
 dict(p=5, item="Slivertongue", phase="39–65", cost=L("Barato", "Cheap"), impact=L("Fork no arco", "Fork on the bow")),
 dict(p=6, item=L("Dano plano em anéis/luvas/aljava", "Flat damage on rings/gloves/quiver"), phase="1+", cost=L("Barato", "Cheap"), impact=L("Todo o dano", "All damage")),
 dict(p=7, item=L("Spirit no peito e amuleto", "Spirit on chest and amulet"), phase="45+", cost=L("Valor", "Value"), impact=L("Heralds + Blasphemy", "Heralds + Blasphemy")),
 dict(p=8, item="Hysseg's Claw", phase="65+", cost=L("Barato", "Cheap"), impact="Snapshot"),
 dict(p=9, item=L("Obliterator Bow + Seske + Thruldana", "Obliterator Bow + Seske + Thruldana"), phase="70+", cost=L("Valor", "Value"), impact=L("Clear e boss", "Clear and boss")),
 dict(p=10, item=L("Absent Amulet", "Absent Amulet"), phase="90+", cost=L("Valor", "Value"), impact="Tacati's Ire"),
 dict(p=11, item="Mageblood · Rite of Passage", phase="90+", cost=L("Luxo", "Luxury"), impact="Min-max"),
]

TRICKS = [
 {"cat": "Snapshot", "lvl": L("Médio", "Medium"), "title": L("Nós de Remnant de graça", "Free Remnant nodes"), "body": L("Coloque só nós de Remnant no Weapon Set 2. Entrar numa área com o Set 2 fixa esses nós para a área inteira; troque para o Set 1 e jogue. Faça uma tecla só para trocar de set.", "Put only Remnant nodes on Weapon Set 2. Entering an area on Set 2 locks those nodes for the whole area; swap to Set 1 and play. Bind a key just for swapping sets.")},
 {"cat": "Toxic Growth", "lvl": L("Fácil", "Easy"), "title": L("Uma de cada vez", "One at a time"), "body": L("Relançar a Toxic Growth destrói as pústulas antigas. Espere explodirem — exceto no Archon com muito dano, quando os tornados detonam na hora.", "Recasting Toxic Growth destroys the old pustules. Wait for them to explode — except on Archon with high damage, when tornadoes detonate them instantly.")},
 {"cat": "Herald of Blood", "lvl": L("Médio", "Medium"), "title": L("Corrente que se alimenta", "Self-feeding chain"), "body": L("A explosão do Herald of Blood não sangra, mas a do Bursting Plague sim. Com Bleed nos dois, cada morte gera outra.", "Herald of Blood's explosion doesn't bleed, but Bursting Plague's does. With Bleed on both, every kill creates another.")},
 {"cat": "Repulsion", "lvl": L("Médio", "Medium"), "title": L("Living Lightning ativa sozinho", "Living Lightning triggers itself"), "body": L("Qualquer hit de raio cria minions de Living Lightning, que ativam a Repulsion. Dano plano de raio em aljava/luvas faz tudo funcionar.", "Any lightning hit creates Living Lightning minions, which proc Repulsion. Flat lightning damage on quiver/gloves makes it all work.")},
 {"cat": "Archon", "lvl": L("Avançado", "Advanced"), "title": L("Dominion", "Dominion"), "body": L("O instill oculto Dominion no amuleto remove o bloqueio de 20 s do Archon (buff menor): uptime de 100%.", "The hidden Dominion instill on the amulet removes Archon's 20 s lockout (smaller buff): 100% uptime.")},
 {"cat": "Remnants", "lvl": L("Médio", "Medium"), "title": L("Efeito das chamas", "Flame effect"), "body": L("Remnant effect em anéis/amuleto (Omen of the Liege + Preserved Collarbone: prefixo do Amanamu), Rune of Reach no capacete e Remnant Potency III somam no buff roxo.", "Remnant effect on rings/amulet (Omen of the Liege + Preserved Collarbone: Amanamu prefix), Rune of Reach in the helmet and Remnant Potency III all add to the purple buff.")},
 {"cat": L("Boss", "Boss"), "lvl": L("Fácil", "Easy"), "title": L("Despair no boss", "Despair on bosses"), "body": L("Para bosses difíceis, troque Repulsion por Despair no Blasphemy.", "For hard bosses, swap Repulsion for Despair in Blasphemy.")},
 {"cat": L("Arco", "Bow"), "lvl": L("Médio", "Medium"), "title": L("Terceira flecha", "Third arrow"), "body": L("Countess Seske's Rune of Archery dá uma flecha; busque 100% de Surpassing chance (arco + árvore) para a terceira — mira muito melhor.", "Countess Seske's Rune of Archery gives one arrow; aim for 100% Surpassing chance (bow + tree) for a third — much better targeting.")},
]

TROUBLESHOOT = [
 (L("Boss difícil no leveling (clear está bom)", "Bosses are hard while leveling (clear is fine)"), L("É quase sempre a pústula sem veneno. Sem veneno guardado ela tem pavio de 15 s e explode fraca; com veneno, explode antes, com raio maior e até +300% de dano — e quem carrega é o veneno que cai NA ÁREA dela, não uma mira. Faça nesta ordem: 1) Concentrated Area na Toxic Growth (as 5 pústulas se sobrepõem no boss); 2) lance a Toxic Growth EM CIMA do boss, uma vez só; 3) fique perto e continue atirando Poisonburst Arrow no boss — a explosão de veneno é em área e carrega as pústulas; se você se afastar para kitar, elas ficam vazias; 4) no nível 35, o Plague Bearer a 100% estoura todas de uma vez (é o maior salto de dano em boss da campanha); 5) Despair antes de começar, porque todo o seu dano é caos; 6) Vine Arrow para abrir, já que a planta também aceita veneno. Antes do Plague Bearer e dos notables de veneno do Ato 3, o boss é naturalmente lento — não é você jogando errado.", "It's almost always an uncharged pustule. With no stored poison it has a 15 s fuse and a weak blast; with poison it detonates sooner, with a larger radius and up to +300% damage — and what charges it is poison landing IN ITS AREA, not aiming at it. Do it in this order: 1) Concentrated Area on Toxic Growth (the 5 pustules overlap on the boss); 2) cast Toxic Growth ON TOP of the boss, once only; 3) stay close and keep shooting Poisonburst Arrow at the boss — the poison burst is an area and charges the pustules; if you kite away they stay empty; 4) at level 35, Plague Bearer at 100% pops them all at once (the biggest boss damage jump in the campaign); 5) Despair before you start, since all your damage is chaos; 6) Vine Arrow to open, as the plant also takes poison. Before Plague Bearer and the Act 3 poison notables, bosses are naturally slow — it isn't you playing badly.")),
 (L("Pouco dano no boss nos mapas", "Low boss damage in maps"), L("Concentrated Area na Toxic Growth? Está relançando antes de explodirem? Falta dano plano em anéis/aljava/luvas? Esses são os três culpados segundo o Goratha.", "Concentrated Area on Toxic Growth? Recasting before they explode? Missing flat damage on rings/quiver/gloves? Those are the three culprits according to Goratha.")),
 (L("Chamas roxas fracas no mapa", "Weak purple flames in maps"), L("Você entrou com o Set 1. Relog ou saia e entre com o Set 2.", "You entered on Set 1. Relog or leave and re-enter on Set 2.")),
 (L("Não consigo usar o Archon", "I can't use Archon"), L("Precisa matar Tul e Esh na questline do Breach, ter o nó e Glory cheia. Depois do buff, 20 s de bloqueio.", "You need to kill Tul and Esh in the Breach questline, own the node and have full Glory. After the buff, 20 s lockout.")),
 (L("Herald of Blood não explode nada", "Herald of Blood explodes nothing"), L("Os inimigos precisam morrer sangrando: Bleed nos supports do Poisonburst e do herald.", "Enemies must die while bleeding: Bleed on Poisonburst's and the herald's supports.")),
 (L("Faltam atributos", "Short on attributes"), L("Abaixe o nível do Herald of Blood e pegue +atributos em anéis/amuleto.", "Lower Herald of Blood's level and get +attributes on rings/amulet.")),
]

ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("3 buffs de Spirit · Choice of Power", "3 Spirit buffs · Choice of Power"), gear="Splinterheart"),
 dict(stage="T1–T10", goal=L("Snapshot do Set 2 · Chayula's Gift", "Set 2 snapshot · Chayula's Gift"), gear="Hysseg's Claw"),
 dict(stage="T11–T15", goal=L("Breach: Tul e Esh", "Breach: Tul and Esh"), gear=L("Obliterator Bow + runas", "Obliterator Bow + runes")),
 dict(stage="Pinnacle", goal=L("Archon + crítico 50%", "Archon + 50% crit"), gear="Absent Amulet · Mageblood"),
]

CRAFT = [
 L("Remnant effect: Omen of the Liege + Preserved Collarbone em anéis/amuleto (prefixo do Amanamu).", "Remnant effect: Omen of the Liege + Preserved Collarbone on rings/amulet (Amanamu prefix)."),
 L("Capacete: craft com Cyclonic Alloy para mais uptime do Archon.", "Helmet: craft with Cyclonic Alloy for more Archon uptime."),
 L("Arco: Idol of Thruldana (+1 limite de veneno) e Countess Seske's Rune of Archery.", "Bow: Idol of Thruldana (+1 poison cap) and Countess Seske's Rune of Archery."),
]

T("item", "Splinterheart", 1, L("Confira o nível no item", "Check the level on the item"), L("Leveling; runeforge no 40.", "Leveling; runeforge at 40."), L("Projéteis se dividem.", "Projectiles split."), "—", L("Arco rare com físico.", "Rare physical bow."))
T("asc", "Choice of Power", 40, L("2º Trial", "2nd Trial"), L("Assim que possível.", "As soon as possible."), L("Todas as chamas roxas.", "All flames purple."), "—", "—")
T("item", "Hysseg's Claw", 1, L("Confira o nível no item", "Check the level on the item"), L("Mapas (Set 2).", "Maps (Set 2)."), L("Snapshot dos nós de Remnant.", "Remnant node snapshot."), "—", L("Qualquer Talisman.", "Any Talisman."))
T("asc", "Archon of Chayula", 80, L("4º Trial + Breach", "4th Trial + Breach"), L("Depois de Tul e Esh.", "After Tul and Esh."), L("Tornados e 20% more.", "Tornadoes and 20% more."), "—", "—")
T("skill", "Garukhan's Resolve", 90, L("Lineage", "Lineage"), L("Com ~50% de crítico.", "At ~50% crit."), L("Muito dano na Toxic Growth.", "Huge Toxic Growth damage."), L("Abaixo de 50% não compensa.", "Below 50% it's not worth it."), "—")
T("item", "Mageblood", 1, L("Confira o nível no item", "Check the level on the item"), L("Min-max.", "Min-max."), L("Legados permanentes.", "Permanent legacies."), "—", "Headhunter")

CASES = [
 (L("Gas Arrow ou Poisonburst no boss?", "Gas Arrow or Poisonburst on bosses?"), L("Gas Arrow é uma rota de boss válida a partir da gem tier 7: a nuvem causa 70–218% do dano de ataque, dura 4 s, cresce até +80% de raio, tem limite de 6 nuvens e aplica veneno sem hit. Isso combina diretamente com a Toxic Growth, cujas pústulas guardam o dano esperado dos venenos aplicados nelas. Deixe a nuvem sobre o boss e as pústulas; Persistent Ground aumenta a janela. Não monte a build para a explosão: ela exige Detonator/Ignite e converte o físico em fogo. Poisonburst continua superior como botão único de clear porque sustenta Bleed, Bursting Plague e os heralds, e continua sendo o fallback simples de boss. A aba Skills permite alternar entre Boss · Gas e Boss · Poisonburst. O que os dados não publicam é a frequência interna de reaplicação da nuvem; por isso a vantagem exata de DPS depende do seu limite de venenos, arma e tempo que o boss fica dentro da área.", "Gas Arrow is a valid boss route from tier 7 gems onward: its cloud deals 70–218% attack damage, lasts 4s, grows to +80% radius, has a limit of 6 clouds and poisons without hitting. This directly matches Toxic Growth, whose pustules store expected damage from poisons inflicted on them. Keep the cloud over the boss and pustules; Persistent Ground extends the window. Do not build around the explosion: it requires a Detonator/Ignite and converts physical to fire. Poisonburst remains the better single-button clear engine because it sustains Bleed, Bursting Plague and the heralds, and remains the simpler boss fallback. The Skills tab lets you switch between Boss · Gas and Boss · Poisonburst. Published data does not expose the cloud's internal reapplication frequency, so its exact DPS advantage depends on your poison limit, weapon and boss uptime inside the area.")),
 (L("Ato 1 muito lento", "Act 1 too slow"), L("Suba com granadas ou Twister até o 14 e troque quando pegar a Toxic Growth.", "Level with grenades or Twister until 14 and swap once you get Toxic Growth.")),
 (L("E se o snapshot for corrigido?", "What if snapshotting gets fixed?"), L("Pegue 'remnant pickup further' no equipamento e na árvore: a build continua funcionando, com menos dano.", "Get 'remnant pickup further' on gear and tree: the build still works, with less damage.")),
 (L("Sem crítico no min-max", "No crit for min-max"), L("Fique na fase Archon (não crítica) e use Diamond Flask com Mageblood.", "Stay on the Archon (non-crit) phase and use Diamond Flask with Mageblood.")),
]

SOURCES = [
 dict(name="Goratha — Poisonburst Arrow Acolyte of Chayula (Maxroll planner)", use=L("Três perfis (Campaign, Mapping, Min Max), rotações, notas e FAQ", "Three profiles (Campaign, Mapping, Min Max), rotations, notes and FAQ"), url=PLANNER_URL),
 dict(name="poe.ninja — Acolyte of Chayula (Forbidden Rites)", use=L("Preços e meta", "Prices and meta"), url="https://poe.ninja/poe2/builds/forbiddenrites?class=Acolyte+of+Chayula"),
 dict(name="Path of Building (PoE2)", use=L("Descrições, Spirit e textos de mods", "Descriptions, Spirit and mod texts"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name="RePoE2", use=L("Nomes e ícones das bases", "Base names and icons"), url="https://repoe-fork.github.io/poe2/"),
]
FIXES = [
 L("As árvores de ascendência de algumas variantes do guia tinham mais pontos do que os Trials dão naquele nível; o app mostra só o que dá para alocar em cada fase (2 pontos por Trial).", "Some guide variants had more ascendancy points than the Trials grant at that level; the app only shows what you can allocate in each phase (2 points per Trial)."),
 L("O planner tem três perfis; as fases dos Atos 1–2 e dos Interlúdios são cortes da ordem de alocação real do Goratha, e a fase Archon usa o perfil Mapping com a ascendência completa.", "The planner has three profiles; the Act 1–2 and Interlude phases are cuts of Goratha's real allocation order, and the Archon phase uses the Mapping profile with the full ascendancy."),
 L("O planner foi criado no patch 0.5.4 e está atualizado para 0.5.5; o snapshot do Set 2 é um bug — o app mostra o plano B se for corrigido.", "The planner was created in patch 0.5.4 and updated for 0.5.5; the Set 2 snapshot is a bug — the app shows plan B if it gets fixed."),
 L("Spirit do Blasphemy depende da curse e não está nos dados: confira no jogo.", "Blasphemy's Spirit depends on the curse and isn't in the data: check in game."),
]

UI = dict(
 carry=r"^(Poisonburst Arrow|Toxic Growth|Archon of Chayula)$", box=L("CHAVE", "KEY"), spiritWhat=L("(heralds e buffs)", "(heralds and buffs)"),
 mechBtn=L("Abrir Chamas & Archon", "Open Flames & Archon"), dmg2=L("Tornados", "Tornadoes"), dmgBar=L("Seu dano / tornados do Archon (aprox.)", "Your damage / Archon tornadoes (approx.)"),
 dmgLegend=L("Tornados do Archon (proporção aproximada)", "Archon tornadoes (approximate ratio)"),
 earlyGone=L("Contagion já saiu: passou do nível {u}.", "Contagion is gone: you're past level {u}."),
 earlyNote=L("Só no começo; sai no nível ~{u}.", "Early only; leaves around level {u}."),
 treeIntro=L("Árvore real do planner do Goratha. Campanha: dano e veneno. Mapas: Set 2 só com Remnants (snapshot). Min-max: crítico.", "Real tree from Goratha's planner. Campaign: damage and poison. Maps: Set 2 with only Remnants (snapshot). Min-max: crit."),
 set1=L("dano (arco)", "damage (bow)"), set2=L("Remnants (snapshot)", "Remnants (snapshot)"), asc="Acolyte of Chayula", cls="Monk",
 respecTip=L("Ao entrar no min-max, a árvore ganha notables de crítico: compare com a fase anterior.", "When entering min-max, the tree gains crit notables: compare with the previous phase."),
 routeIntro=L("Sete fases: Poisonburst e Herald of Blood no Ato 1, Toxic Growth e chamas de Chayula, Plague Bearer e Choice of Power, heralds e Blasphemy, snapshot nos mapas, Archon e o min-max crítico.", "Seven phases: Poisonburst and Herald of Blood in Act 1, Toxic Growth and Flames of Chayula, Plague Bearer and Choice of Power, heralds and Blasphemy, maps snapshot, Archon and crit min-max."),
 socketPrio=["Poisonburst Arrow", "Toxic Growth", "Archon of Chayula", "Plague Bearer", "Herald of Blood"],
 permIntro=L("Nada disso volta depois. Spirit paga os heralds, Plague Bearer, Wind Dancer e Ghost Dance — todos de 30.", "None of this comes back later. Spirit pays for the heralds, Plague Bearer, Wind Dancer and Ghost Dance — all 30 each."),
 atlasCards=[[L("Breach", "Breach"), L("A questline do Breach (Tul e Esh) libera o Archon of Chayula: priorize no atlas.", "The Breach questline (Tul and Esh) unlocks Archon of Chayula: prioritize it on the atlas.")],
             [L("Mapas ruins", "Bad maps"), L("Monstros com muita resistência a caos ou reflexo de veneno atrasam o clear. Relog se entrar com o Set errado.", "Monsters with high chaos resistance or poison reflect slow the clear. Relog if you entered on the wrong Set.")]],
 foot=L("Guia baseado no planner do Goratha (Maxroll), dados do Path of Building e do RePoE2 e preços do poe.ninja", "Guide based on Goratha's planner (Maxroll), Path of Building and RePoE2 data and poe.ninja prices"),
)

CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens, Árvore e Chamas & Archon se adaptam na hora. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items, Tree and Flames & Archon tabs adapt instantly. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit máximo", "Max Spirit"), L("ex.: 150", "e.g. 150")], ["crit", L("Chance de crítico (%)", "Crit chance (%)"), L("ex.: 35", "e.g. 35")], ["chaos", L("Chaos Resistance (%)", "Chaos Resistance (%)"), ""]],
 tiles=[[L("Spirit reservado", "Spirit reserved"), "used"], [L("Spirit livre", "Spirit free"), "free"], [L("Crítico (%)", "Crit (%)"), "crit"]],
 buffs=[dict(key="hob", name="Herald of Blood", cost=30), dict(key="pb", name="Plague Bearer", cost=30), dict(key="hop", name="Herald of Plague", cost=30), dict(key="wd", name="Wind Dancer", cost=30), dict(key="gd", name="Ghost Dance", cost=30)],
 sections=[
  ["active", L("Skills ativas que já liberei", "Active skills I have unlocked"), L("Marque a gem quando ela estiver no seu inventário e puder ser usada. A aba Skills monta a barra a partir daqui.", "Tick a gem when it is in your inventory and usable. The Skills tab builds your bar from here.")],
  ["persistent", L("Skills persistentes e reservas", "Persistent skills and reservations"), L("Marque as que você possui; o Spirit decide quais cabem juntas.", "Tick the ones you own; Spirit decides which fit together.")],
  ["support", L("Supports que mudam a build", "Build-defining supports"), L("Somente os supports que alteram clear, boss ou a troca para crítico.", "Only supports that change clear, bossing or the crit transition.")],
  ["gear", L("Itens que eu tenho", "Items I have"), L("Leveling e endgame no mesmo histórico. Itens antigos deixam de ser prioridade quando a fase muda.", "Levelling and endgame in one history. Old items stop being priorities as phases change.")],
  ["tree", L("Árvore e desbloqueios", "Tree and unlocks"), ""], ["asc", L("Ascendência", "Ascendancy"), ""],
 ],
 skillInfo={
  "poisonburst": dict(name="Poisonburst Arrow"), "gas": dict(name="Gas Arrow"), "toxic": dict(name="Toxic Growth"), "vine": dict(name="Vine Arrow"), "contagion": dict(name="Contagion"),
  "breachSkill": dict(name="Into the Breach"), "despair": dict(name="Despair"), "pounce": dict(name="Pounce"), "archonSkill": dict(name="Archon of Chayula"),
  "hob": dict(name="Herald of Blood"), "pb": dict(name="Plague Bearer"), "hop": dict(name="Herald of Plague"), "wd": dict(name="Wind Dancer"), "gd": dict(name="Ghost Dance"), "blasph": dict(name="Blasphemy"),
 },
 skillMap={"Poisonburst Arrow":"poisonburst", "Gas Arrow":"gas", "Toxic Growth":"toxic", "Vine Arrow":"vine", "Contagion":"contagion", "Into the Breach":"breachSkill", "Despair":"despair", "Pounce":"pounce", "Archon of Chayula":"archonSkill", "Herald of Blood":"hob", "Plague Bearer":"pb", "Herald of Plague":"hop", "Wind Dancer":"wd", "Ghost Dance":"gd", "Blasphemy":"blasph"},
 phaseSkills={
  "a1": dict(clear=["poisonburst", "hob"], boss=["poisonburst", "vine"], gasboss=["poisonburst", "vine"]),
  "a2": dict(clear=["poisonburst", "hob", "pounce"], boss=["toxic", "vine", "despair", "poisonburst"], gasboss=["toxic", "vine", "despair", "gas"]),
  "a3": dict(clear=["poisonburst", "hob", "pb"], boss=["toxic", "vine", "despair", "pb", "poisonburst"], gasboss=["toxic", "vine", "despair", "pb", "gas"]),
  "a4": dict(clear=["poisonburst", "hob", "hop", "pb"], boss=["toxic", "vine", "pb", "poisonburst"], gasboss=["toxic", "vine", "pb", "gas"]),
  "maps": dict(clear=["poisonburst", "hob", "hop", "pb"], boss=["toxic", "vine", "pb", "poisonburst"], gasboss=["toxic", "vine", "pb", "gas"]),
  "archon": dict(clear=["poisonburst", "hob", "hop", "pb", "archonSkill"], boss=["toxic", "vine", "pb", "archonSkill", "poisonburst"], gasboss=["toxic", "vine", "pb", "archonSkill", "gas"]),
  "max": dict(clear=["poisonburst", "hob", "hop", "pb", "archonSkill"], boss=["toxic", "vine", "pb", "archonSkill", "poisonburst"], gasboss=["toxic", "vine", "pb", "archonSkill", "gas"]),
 },
 own=[
  ["gear", "Splinterheart", "Splinterheart"], ["gear", "The Lethal Draw", "The Lethal Draw"], ["gear", "Ghostmarch", "Ghostmarch"], ["gear", "Death's Harp", "Death's Harp"], ["gear", "Slivertongue", "Slivertongue"],
  ["gear", "Hysseg's Claw", L("Hysseg's Claw / Talisman no Set 2", "Hysseg's Claw / Talisman on Set 2")], ["gear", "Obliterator Bow", "Obliterator Bow"], ["gear", "Countess Seske's Rune of Archery", "Countess Seske's Rune of Archery"], ["gear", "Idol of Thruldana", "Idol of Thruldana"],
  ["gear", "Absent Amulet", "Absent Amulet"], ["gear", "Mageblood", "Mageblood"], ["gear", "Rite of Passage", "Rite of Passage"],
  ["active", "poisonburst", "Poisonburst Arrow"], ["active", "gas", "Gas Arrow"], ["active", "toxic", "Toxic Growth"], ["active", "vine", "Vine Arrow"], ["active", "contagion", "Contagion"], ["active", "breachSkill", "Into the Breach"], ["active", "despair", "Despair"], ["active", "pounce", "Pounce"], ["active", "archonSkill", "Archon of Chayula"],
  ["persistent", "hob", "Herald of Blood (30)"], ["persistent", "pb", "Plague Bearer (30)"], ["persistent", "hop", "Herald of Plague (30)"], ["persistent", "wd", "Wind Dancer (30)"], ["persistent", "gd", "Ghost Dance (30)"], ["persistent", "blasph", "Blasphemy + Repulsion"],
  ["support", "conc", L("Concentrated Area na Toxic Growth", "Concentrated Area on Toxic Growth")], ["support", "fork", L("Fork no Poisonburst", "Fork on Poisonburst")], ["support", "gasground", L("Persistent Ground na Gas Arrow", "Persistent Ground on Gas Arrow")], ["support", "garukhan", "Garukhan's Resolve"],
  ["tree", "snapshot", L("Set 2 só com nós de Remnant", "Set 2 with only Remnant nodes")], ["tree", "breach", L("Breach: Tul e Esh mortos", "Breach: Tul and Esh killed")],
  ["asc", "waking", "Waking Dream"], ["asc", "power", "Lucid Dreaming → Choice of Power"], ["asc", "gift", "Chayula's Gift"], ["asc", "archon", "Archon of Chayula"],
 ],
 rules=[
  dict(when=dict(lvMin=14, skillsConfigured=True, own=["toxic"], notOwn=["conc"]), lvl="bad", t=L("Toxic Growth sem Concentrated Area", "Toxic Growth without Concentrated Area"), d=L("As pústulas não se sobrepõem: principal causa de pouco dano no boss.", "Pustules don't overlap: the main cause of low boss damage."), tab="skills"),
  dict(when=dict(own=["garukhan"], numLt=["crit", 50]), lvl="bad", t=L("Garukhan's Resolve abaixo de 50% de crítico", "Garukhan's Resolve below 50% crit"), d=L("Não compensa o custo: volte para a fase Archon.", "Not worth the cost: go back to the Archon phase."), tab="mech"),
  dict(when=dict(own=["Mageblood"], numLt=["crit", 50]), lvl="tip", t=L("Mageblood sem 50% de crítico", "Mageblood without 50% crit"), d=L("Use Diamond Flask.", "Use a Diamond Flask."), tab="gear"),
  dict(when=dict(lvMin=65, notOwn=["snapshot"]), lvl="warn", t=L("Monte o snapshot do Set 2", "Set up the Set 2 snapshot"), d=L("Só nós de Remnant no Set 2 e entre nas áreas com ele.", "Only Remnant nodes on Set 2 and enter areas with it."), tab="mech"),
  dict(when=dict(lvMin=75, notOwn=["breach"]), lvl="tip", t=L("Questline do Breach", "Breach questline"), d=L("Tul e Esh liberam o Archon of Chayula.", "Tul and Esh unlock Archon of Chayula."), tab="atlas"),
  dict(when=dict(own=["gift"], numLt=["chaos", 75]), lvl="tip", t=L("Chaos Resistance baixa com Chayula's Gift", "Low Chaos Resistance with Chayula's Gift"), d=L("A resistência é dobrada: um pouco no equipamento já leva ao cap.", "Resistance is doubled: a little on gear reaches the cap."), tab="gear"),
  dict(when=dict(lvMin=42, notOwn=["power"]), lvl="warn", t=L("Choice of Power pendente", "Choice of Power pending"), d=L("O maior multiplicador da build.", "The build's biggest multiplier."), tab="asc"),
  dict(when=dict(lvMin=26, notOwn=["waking"]), lvl="warn", t=L("1ª ascendência pendente", "1st ascendancy pending"), d="Waking Dream.", tab="asc"),
  dict(when=dict(lvMin=16, lvMax=29, notOwn=["The Lethal Draw"]), lvl="tip", t="The Lethal Draw", d=L("Aljava forte do Ato 2: físico extra ao consumir cargas do Life Flask. Em boss longo, monitore as cargas.", "Strong Act 2 quiver: added physical by consuming Life Flask charges. Watch charges on long bosses."), tab="gear"),
  dict(when=dict(lvMin=16, lvMax=29, notOwn=["Ghostmarch"]), lvl="tip", t="Ghostmarch", d=L("Mobilidade e segurança; o dodge atravessa inimigos. Troque depois por botas rare de 25–30% MS.", "Mobility and safety; dodge passes through enemies. Later replace with 25–30% MS rare boots."), tab="gear"),
  dict(when=dict(lvMin=45, notOwn=["hop"]), lvl="tip", t="Herald of Plague", d=L("Espalha o veneno ao matar: clear muito melhor.", "Spreads poison on kill: much better clear."), tab="skills"),
 dict(when=dict(lvMin=68, notOwn=["fork"]), lvl="tip", t="Fork", d=L("Clear fora da tela no Poisonburst.", "Off-screen clear on Poisonburst."), tab="skills"),
  dict(when=dict(lvMin=22, skillsConfigured=True, own=["gas"], notOwn=["gasground"]), lvl="tip", t=L("Gas Arrow: prolongue a nuvem", "Gas Arrow: extend the cloud"), d=L("Persistent Ground aumenta a janela que reaplica veneno nas pústulas; a explosão de fogo não é o objetivo deste setup.", "Persistent Ground extends the window that reapplies poison to the pustules; the fire explosion is not the goal of this setup."), tab="skills"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["archon", "max"], when=dict(notOwn=["archon"]), gemsFrom="maps", note=L("Sem Archon of Chayula: mostrando o setup dos mapas.", "No Archon of Chayula: showing the maps setup.")),
 dict(pids=["max"], when=dict(own=["archon"], notOwn=["garukhan"]), gemsFrom="archon", note=L("Sem Garukhan's Resolve: mostrando o setup não crítico do Archon.", "No Garukhan's Resolve: showing the non-crit Archon setup.")),
]
TREE_RULES = [
 dict(when=dict(lvMin=65, notOwn=["snapshot"]), t=L("Weapon Set 2: coloque só nós de Remnant (Remnant Attraction primeiro).", "Weapon Set 2: put only Remnant nodes (Remnant Attraction first)."), node=None),
]
TIMING_KEY = {"Splinterheart": "Splinterheart", "The Lethal Draw": "The Lethal Draw", "Ghostmarch": "Ghostmarch", "Death's Harp": "Death's Harp", "Slivertongue": "Slivertongue", "Choice of Power": "power", "Archon of Chayula": "archon", "Garukhan's Resolve": "garukhan", "Mageblood": "Mageblood"}

MECH = dict(
 title=L("Chamas & Archon", "Flames & Archon"),
 intro=L("Como o Acolyte de veneno funciona: explosões em cadeia no clear, chamas roxas de Chayula multiplicando o dano e o Archon detonando as pústulas no boss.", "How the poison Acolyte works: chained explosions for clear, Chayula's purple flames multiplying damage and the Archon detonating pustules on bosses."),
 sections=[
  dict(type="cards", cards=[
   [L("1. Cadeia de explosões", "1. Explosion chain"), L("Poisonburst Arrow envenena e faz sangrar em área. Inimigo envenenado morre → Herald of Plague espalha o veneno e Bursting Plague explode; inimigo sangrando morre → Herald of Blood explode. As explosões matam o próximo, que explode de novo.", "Poisonburst Arrow poisons and bleeds in an area. A poisoned enemy dies → Herald of Plague spreads the poison and Bursting Plague explodes; a bleeding enemy dies → Herald of Blood explodes. The explosions kill the next one, which explodes again.")],
   [L("2. Chamas de Chayula", "2. Flames of Chayula"), L("Into the Breach (Waking Dream) faz chamas nascerem como Remnants: roxa = % do dano como caos, vermelha = vida, azul = mana. Choice of Power deixa todas roxas, 50% mais fortes e coletadas de mais longe.", "Into the Breach (Waking Dream) spawns flames as Remnants: purple = % of damage as chaos, red = life, blue = mana. Choice of Power makes them all purple, 50% stronger and collected from further away.")],
   [L("3. Pústulas: bombas que se carregam com veneno", "3. Pustules: bombs charged by poison"), L("Toxic Growth joga 5 pústulas (o máximo ao mesmo tempo). Sozinhas elas têm pavio de 15 SEGUNDOS e explodem fraco. Veneno guardado nelas faz a explosão vir mais cedo, com raio maior e até +300% de dano. Você não mira nas pústulas: elas se carregam com o veneno que cai NA ÁREA delas. Por isso a regra é lutar EM CIMA das pústulas — lance a Toxic Growth no boss e continue atirando Poisonburst Arrow nele (a explosão de veneno é em área e alcança as pústulas). Quem estoura todas de uma vez é o Plague Bearer no 100% e, no endgame, os tornados do Archon.", "Toxic Growth throws 5 pustules (the maximum at once). On their own they have a 15 SECOND fuse and explode weakly. Poison stored in them makes the blast come sooner, with a larger radius and up to +300% damage. You don't aim at pustules: they are charged by poison landing IN THEIR AREA. So the rule is to fight ON TOP of the pustules — cast Toxic Growth on the boss and keep shooting Poisonburst Arrow at it (the poison burst is an area and reaches the pustules). What pops them all at once is Plague Bearer at 100% and, in endgame, the Archon tornadoes.")],
   [L("4. Archon of Chayula: onde, quando e como", "4. Archon of Chayula: where, when and how"), L("ONDE: 4º ponto de ascendência, no último Trial — ele só aparece depois de matar Tul e Esh na questline do Breach (endgame). QUANDO: a barra de Glory precisa de 100, e você ganha Glory a cada acerto de caos (cerca de 1 segundo atacando). COMO: aperte a skill e vire o Archon por alguns segundos: 20% more dano físico e de caos, 25% de chance de aplicar Wither (4 s) por acerto e UM TORNADO A CADA 3 SEGUNDOS. Cada tornado dura 8 s, persegue inimigos, bate 5 vezes por segundo, deixa o alvo até 30% mais lento e detona as pústulas da Toxic Growth. No início da transformação você anda 70% mais devagar e vai acelerando. Quando acaba: 20 s de bloqueio (o instill Dominion tira o bloqueio, com buff menor).", "WHERE: 4th ascendancy point, on the last Trial — it only appears after killing Tul and Esh in the endgame Breach questline. WHEN: the Glory bar needs 100, and you gain Glory on every chaos hit (about one second of attacking). HOW: press the skill and become the Archon for a few seconds: 20% more physical and chaos damage, 25% chance to apply Wither (4 s) on hit and ONE TORNADO EVERY 3 SECONDS. Each tornado lasts 8 s, chases enemies, hits 5 times per second, slows them by up to 30% and detonates Toxic Growth pustules. You start the transformation moving 70% slower and speed up. When it ends: 20 s lockout (the Dominion instill removes it, with a smaller buff).")],
  ]),
  dict(type="steps", h=L("Snapshot do Weapon Set 2", "Weapon Set 2 snapshot"), steps=[
   [L("Árvore", "Tree"), L("Weapon Set 2 só com nós de Remnant (Remnant Attraction primeiro); Set 1 com dano.", "Weapon Set 2 with only Remnant nodes (Remnant Attraction first); Set 1 with damage.")],
   [L("Talisman", "Talisman"), L("Talisman no Set 2 em Wolf Form: dá movement speed e deixa óbvio em qual set você está.", "Talisman on Set 2 in Wolf Form: grants movement speed and makes it obvious which set you're on.")],
   [L("Tecla", "Key"), L("Configure uma tecla só para trocar de set.", "Bind a key just for swapping sets.")],
   [L("Entrar", "Enter"), L("Entre em toda área/mapa com o Set 2.", "Enter every area/map on Set 2.")],
   [L("Trocar", "Swap"), L("Troque para o Set 1: os nós de Remnant continuam valendo até sair da área.", "Swap to Set 1: Remnant nodes keep working until you leave the area.")],
   [L("Errou?", "Mistake?"), L("Entrou no Set 1: relog ou saia e entre de novo.", "Entered on Set 1: relog or leave and re-enter.")],
  ]),
  dict(type="rotation", blocks=[
   [L("Clear", "Clear"), [L("Poisonburst Arrow até o Plague Bearer chegar a 100%", "Poisonburst Arrow until Plague Bearer hits 100%"), L("Ative o Plague Bearer", "Activate Plague Bearer"), L("Pouco dano: Vine Arrow e Toxic Growth em packs mágicos", "Low damage: Vine Arrow and Toxic Growth on magic packs"), L("Archon quando disponível", "Archon when available")]],
   [L("Boss", "Boss"), [L("Archon of Chayula", "Archon of Chayula"), L("Vine Arrow algumas vezes", "Vine Arrow a few times"), L("Toxic Growth a cada dois ataques", "Toxic Growth every other attack"), L("Plague Bearer", "Plague Bearer"), L("Alterne Toxic Growth e Plague Bearer", "Alternate Toxic Growth and Plague Bearer")]],
  ]),
  dict(type="spirit", h=L("Spirit dos heralds e buffs", "Herald and buff Spirit"), p=L("Marque o que você usa. Custos do Path of Building.", "Tick what you use. Costs from Path of Building."),
       note=L("Blasphemy reserva conforme a curse: confira no jogo.", "Blasphemy reserves based on the curse: check in game.")),
  dict(type="timeline", h=L("Arco por nível", "Bow by level"), items=[
   dict(lv=1, t=L("Arco branco do vendor", "White vendor bow"), d=L("Transmutation/Augmentation até físico.", "Transmutation/Augmentation until physical.")),
   dict(lv=16, t="Splinterheart", d=L("Projéteis se dividem: clear enorme no leveling.", "Projectiles split: huge leveling clear.")),
   dict(lv=28, t="Death's Harp", d=L("Flecha adicional e vida/mana por kill; compare com a Splinterheart.", "Additional arrow and life/mana per kill; compare with Splinterheart.")),
   dict(lv=39, t="Slivertongue", d=L("Físico alto, crítico, leech e flechas com Fork + Pierce.", "High physical, crit, leech and arrows with Fork + Pierce.")),
   dict(lv=40, t=L("Splinterheart runeforged", "Runeforged Splinterheart"), d=L("Com Medved's Crest of the Circle: dura até os mapas.", "With Medved's Crest of the Circle: lasts into maps.")),
   dict(lv=78, t="Obliterator Bow", d=L("Físico alto + Countess Seske's Rune of Archery + Idol of Thruldana.", "High physical + Countess Seske's Rune of Archery + Idol of Thruldana.")),
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
        if q["boss"] == 'Great White One':
            q["reward"] = L('ESCOLHA: +30% Armour, Evasion e Energy Shield (Shark Fin): Evasion e ES são a defesa da build', "CHOICE: +30% Armour, Evasion and Energy Shield (Shark Fin): Evasion and ES are the build's defence"); q["prio"] = 'Alta'
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="15/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=PLANNER_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=BOOK.TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None,
                ui=UI, char=CHAR, mech=MECH, adaptSwaps=ADAPT_SWAPS, treeRules=TREE_RULES, timingKey=TIMING_KEY, phaseAct=PHASE_ACT, treeOrder=ORDER + ["uber"], tabGroups=TAB_GROUPS, craftKit=CRAFT_KIT)
