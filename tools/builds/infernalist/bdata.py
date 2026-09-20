# -*- coding: utf-8 -*-
"""Infernalist: Spark no leveling → Cast on Critical Comet no endgame → CoA Comet (luxo). Base: guia do Ignatius (Mobalytics, 0.5.5)
e variante 'Cheaper' do kingkongor; árvore/gems/itens das variantes, textos do Path of Building e preços do poe.ninja (Forbidden Rites)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("infernalist")

GUIDE_URL = "https://mobalytics.gg/poe-2/builds/coc-spark-comet-recoup-infernalist-by-ignatius"
COA_URL = "https://mobalytics.gg/poe-2/builds/infernalist-auto-spark-coa-comet-kingkongor"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "17/09/2026"

CONFIG = dict(dir="infernalist", build="infernalist", store="infernalist1", emoji="🔥", pill="Witch · Infernalist",
              fonts="family=Cinzel+Decorative:wght@700;900&family=Cinzel:wght@500;700&family=Cormorant+SC:wght@500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400")
TXT = {
 "pt": dict(TITLE="Infernal Pact", DESC="Guia interativo Infernalist Spark → Cast on Critical Comet (Witch) — PoE 2 Forbidden Rites",
            H1S="Spark no leveling · Cast on Critical Comet no endgame · guias do Ignatius e do kingkongor explicados", H1="The Infernal Pact",
            LEAD="Faíscas e infusões na campanha, Comets caindo a cada crítico nos mapas e o Pyromantic Pact transformando o próprio dano em regeneração. Diga seu nível e o que você tem: o guia mostra a rotação, as infusões, o Spirit das metas e cada passiva."),
 "en": dict(TITLE="Infernal Pact", DESC="Interactive Infernalist Spark → Cast on Critical Comet (Witch) guide — PoE 2 Forbidden Rites",
            H1S="Spark while leveling · Cast on Critical Comet in endgame · Ignatius's and kingkongor's guides explained", H1="The Infernal Pact",
            LEAD="Sparks and infusions in the campaign, Comets falling on every crit in maps and Pyromantic Pact turning self-damage into regeneration. Tell it your level and what you have: the guide shows the rotation, infusions, meta skill Spirit and every passive."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["quando", "Quando usar", "When to use"], ["mech", "Infusões & Chama", "Infusions & Flame"],
        ["uniques", "Uniques", "Uniques"], ["arvore", "Árvore de Passivas", "Passive Tree"], ["rota", "Rota 1→100", "Route 1→100"], ["skills", "Skills & Supports", "Skills & Supports"],
        ["gear", "Itens", "Items"], ["asc", "Ascendência", "Ascendancy"], ["quests", "Quests", "Quests"], ["tricks", "Tricks Pro", "Pro Tricks"], ["atlas", "Atlas", "Atlas"],
        ["diag", "Diagnóstico", "Troubleshooting"], ["fontes", "Fontes", "Sources"]]

CLASS, ASC, START = "Witch", "Infernalist", 54447
ORDER = ["a1", "a2", "a3", "a4", "maps", "recoup", "frost", "max"]
VMAP = {"a1": "infernalist: 1-16 (A1)", "a2": "infernalist: 14-29 (A2)", "a3": "infernalist: 30-42 (A3)", "a4": "infernalist: 42-60 (A4+IL)",
        "maps": "infernalist: Early Maps (T1-T9)", "recoup": "infernalist: End Game (Cheap)", "frost": "infernalist: End Game (Expensive)", "max": "inf_coa: Cheaper"}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a4", "maps": "maps", "recoup": "recoup", "frost": "recoup", "max": "frost"}
FULLMAP = {k: k for k in ORDER}
PHASE_ACT = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "maps": 6, "recoup": 6, "frost": 6, "max": 6}
ITEM_NOTE = {"Dueling Wand": "Spellslinger"}
EXTRA_ICONS = {"Unleash": "https://cdn.mobalytics.gg/assets/poe-2/images/game/Art/2DItems/Gems/New/NewSupport/UnleashSupportGem.webp"}
WAND_RUNE = L("Storm Rune (raio) ou runa de Spell Damage", "Storm Rune (lightning) or a Spell Damage rune")

def socket_hint(slot, name):
    if any(w in name for w in ("Wand", "Staff", "Focus")): return [WAND_RUNE]
    if slot in ("Capacete", "Body Armour", "Luvas", "Botas"):
        return [L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio) · resist no cap: Body Rune (vida)", "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning) · resists capped: Body Rune (life)")]
    return None

SUPWHY = {
 "Unleash": L("O Spark acumula Seals e, ao lançar, repete várias vezes: muito mais faíscas de uma vez.", "Spark builds Seals and, when cast, repeats several times: many more sparks at once."),
 "Rapid Casting I": L("Conjura mais rápido.", "Casts faster."), "Rapid Casting II": L("Conjura mais rápido.", "Casts faster."),
 "Rapid Casting III": L("Mais cast speed para cada spell diferente lançado nos últimos 8 s.", "More cast speed for each different spell cast in the last 8 s."),
 "Overabundance I": L("Aumenta o limite (mais Frost Bombs/Orbs ao mesmo tempo) em troca de duração.", "Raises the limit (more Frost Bombs/Orbs at once) at the cost of duration."),
 "Spell Cascade": L("O spell cai também dos dois lados do alvo: mais área e mais chance de acertar infusões.", "The spell also lands on both sides of the target: more area and more chance to hit."),
 "Spell Echo": L("O spell repete: mais Exposure e mais infusões da Frost Bomb.", "The spell echoes: more Exposure and more Frost Bomb infusions."),
 "Short Fuse I": L("A Frost Bomb detona antes: Cold Infusion mais cedo.", "Frost Bomb detonates sooner: earlier Cold Infusion."),
 "Short Fuse II": L("Detona muito mais cedo, com menos dano — só queremos a infusão.", "Detonates much sooner with less damage — we only want the infusion."),
 "Pierce I": L("As faíscas atravessam um inimigo.", "Sparks pierce one enemy."), "Pierce III": L("Atravessam inimigos ilimitados, perdendo dano a cada um.", "Pierce unlimited enemies, losing damage each time."),
 "Blind I": L("Cega inimigos: defesa sem depender de equipamento.", "Blinds enemies: defence that doesn't depend on gear."), "Blind II": L("Blind mais forte.", "Stronger Blind."),
 "Prolonged Duration I": L("Mais duração (Flame Wall, Sigil).", "Longer duration (Flame Wall, Sigil)."), "Prolonged Duration II": L("Mais duração.", "Longer duration."),
 "Arcane Surge": L("Gastar muita mana dá um burst de regeneração e cast speed (o Mana Tempest drena tudo e ativa na hora).", "Spending lots of mana grants a burst of mana regen and cast speed (Mana Tempest drains everything and triggers it instantly)."),
 "Magnified Area I": L("Área maior.", "Larger area."), "Magnified Area II": L("Área maior.", "Larger area."),
 "Heightened Curse": L("Elemental Weakness mais forte.", "Stronger Elemental Weakness."), "Ritualistic Curse": L("Curse com área maior.", "Larger curse area."),
 "Harmonic Remnants I": L("Remnants de mais longe.", "Remnants from further away."), "Harmonic Remnants II": L("Remnants de mais longe e às vezes um extra.", "Remnants from further away and sometimes an extra one."),
 "Remnant Potency I": L("Remnants mais fortes.", "Stronger remnants."),
 "Cooldown Recovery I": L("Demon Form volta mais rápido.", "Demon Form comes back faster."), "Cooldown Recovery II": L("Cooldowns mais curtos.", "Shorter cooldowns."),
 "Efficiency I": L("Custa menos.", "Costs less."), "Efficiency II": L("Custa menos.", "Costs less."),
 "Compressed Duration I": L("Duração menor.", "Shorter duration."),
 "Pinpoint Critical": L("Crítico mais frequente com menos dano crítico — alimenta o Cast on Critical.", "More frequent crits with less crit damage — feeds Cast on Critical."),
 "Ignite III": L("Mais Ignite e Ignite mais rápido.", "More Ignite and faster Ignite."),
 "Boundless Energy I": L("Meta skill ganha energia bem mais rápido.", "The meta skill gains energy much faster."), "Boundless Energy II": L("Energia muito mais rápida: mais Comets.", "Much faster energy: more Comets."),
 "Comet": L("Gem de SKILL dentro do Cast on Critical/Ailment: cai sozinha quando a energia enche; consome Fire Infusion para uma explosão de gelo e fogo.", "SKILL gem inside Cast on Critical/Ailment: it falls by itself when energy fills; consumes a Fire Infusion for an ice-and-fire blast."),
 "Spark": L("Gem de SKILL dentro do Spellslinger/Cast on Dodge.", "SKILL gem inside Spellslinger/Cast on Dodge."),
 "Flame Wall": L("Gem de SKILL dentro do Spellslinger.", "SKILL gem inside Spellslinger."),
 "Living Bomb": L("Gem de SKILL dentro do Spellslinger: deixa Fire Infusion.", "SKILL gem inside Spellslinger: leaves a Fire Infusion."),
 "Hulking Minions": L("Hellhound maior, com mais vida e dano — mas custa bem mais Spirit.", "Bigger Hellhound with more life and damage — but it costs much more Spirit."), "Meat Shield II": L("Hellhound toma menos dano (e causa menos).", "Hellhound takes less damage (and deals less)."), "Elemental Army": L("Resistências elementais para o Hellhound.", "Elemental resistances for the Hellhound."),
 "Fortress II": L("O muro vira um círculo em volta de você: fique dentro e atire através.", "The wall becomes a circle around you: stand inside and shoot through it."),
 "Rising Tempest": L("Mais dano elemental para cada skill de elemento diferente usada.", "More elemental damage per skill of a different element used."),
 "Potent Exposure": L("Exposure da Frost Bomb mais forte.", "Stronger Frost Bomb Exposure."),
 "Considered Casting": L("Mais dano, menos cast speed.", "More damage, less cast speed."),
 "Doedre's Undoing": L("Lineage: a curse vira uma área no chão com sapos explosivos.", "Lineage: the curse becomes a ground area with exploding toads."),
 "Vilenta's Propulsion": L("Lineage: cast speed também aumenta a velocidade dos projéteis.", "Lineage: cast speed also increases projectile speed."),
 "Energy Retention": L("Chance de devolver parte da energia ao disparar: mais Comets seguidos.", "Chance to refund some energy on trigger: more Comets in a row."),
 "Atalui's Bloodletting": L("Lineage: parte do custo vira vida e ganha dano físico extra.", "Lineage: part of the cost becomes life and gains extra physical damage."),
 "Lightning Mastery": L("+1 nível em skills de raio.", "+1 level to lightning skills."), "Cold Mastery": L("+1 nível em skills de frio.", "+1 level to cold skills."), "Fire Mastery": L("+1 nível em skills de fogo.", "+1 level to fire skills."),
 "Living Lightning II": L("Cria minions de raio que encadeiam.", "Creates chaining lightning minions."),
 "Arbiter's Ignition": L("Lineage: Ignite com spells de fogo dá Elemental Archon.", "Lineage: Igniting with fire spells grants Elemental Archon."),
 "Sione's Temper": L("Lineage: chance crescente de disparar muitos projéteis em círculo.", "Lineage: growing chance to fire many projectiles in a circle."),
 "Trickster's Shard": L("Lineage: cria um Mimic que lança o spell.", "Lineage: creates a Mimic that casts the spell."),
 "Blindside": L("Mais crítico e dano crítico contra inimigos cegos.", "More crit chance and crit damage against blinded enemies."),
 "Execute III": L("Mais dano contra inimigos em Low Life e enquanto você está em Low Life.", "More damage against Low Life enemies and while you're on Low Life."),
 "Second Wind II": L("Usos extras de cooldown no Frost Wall.", "Extra cooldown uses on Frost Wall."),
 "Uhtred's Omen": L("Lineage: níveis extras com exatamente 1 outro support.", "Lineage: extra levels with exactly 1 other support."),
 "Uhtred's Augury": L("Lineage: níveis extras com exatamente 2 outros supports.", "Lineage: extra levels with exactly 2 other supports."),
 "Atziri's Impatience": L("Lineage: cooldown muito mais rápido, custando vida/mana/ES.", "Lineage: much faster cooldown, costing life/mana/ES."),
 "Cannibalism I": L("Vida ao matar.", "Life on kill."), "Herbalism I": L("Mais cura de flask.", "More flask healing."), "Herbalism II": L("Mais cura de flask.", "More flask healing."),
 "Mobility": L("Anda mais rápido enquanto conjura.", "Move faster while casting."),
 "Heightened Charges": L("Chance de dobrar o benefício ao consumir charges.", "Chance to double the benefit when consuming charges."),
 "Uhtred's Rite": L("Lineage: Overflowing Chalice e mais dano durante o flask de vida.", "Lineage: Overflowing Chalice and more damage during the life flask."),
 "Uhtred's Constellation": L("Lineage: dois usos extras de cooldown e dano por skill de cooldown diferente.", "Lineage: two extra cooldown uses and damage per different cooldown skill."),
 "Fork": L("Projéteis se dividem.", "Projectiles fork."), "Runic Extraction": L("Inimigos mortos podem soltar Verisium Infusion (substitui qualquer infusão).", "Killed enemies may drop a Verisium Infusion (replaces any infusion)."),
 "Projectile Acceleration III": L("Projéteis mais rápidos e velocidade vira dano.", "Faster projectiles and speed becomes damage."),
 "Multishot II": L("Mais projéteis.", "More projectiles."), "Concentrated Area": L("Área menor, mais dano.", "Smaller area, more damage."),
 "Morrigan's Insight": L("Lineage: consumir Freeze dá dano e dispara Nature's Exchange.", "Lineage: consuming Freeze grants damage and triggers Nature's Exchange."),
 "Vorana's Siege": L("Lineage: área maior e hits fortes em alvo isolado.", "Lineage: larger area and strong hits on isolated targets."),
 "Ice Bite II": L("Congelar infunde dano de frio.", "Freezing infuses cold damage."), "Innervate": L("Matar inimigo Shocked infunde raio.", "Killing a Shocked enemy infuses lightning."),
 "Khatal's Rejuvenation": L("Lineage: pegar Remnants dá Khatal's Rejuvenation.", "Lineage: picking up Remnants grants Khatal's Rejuvenation."),
 "Wildshards II": L("Chance de muitos projéteis em círculo.", "Chance of many projectiles in a circle."),
 "Rakiata's Flow": L("Lineage: resistências elementais do alvo invertidas.", "Lineage: target's elemental resistances inverted."),
 "Esh's Prowess": L("Lineage: +1 nível e raio só no mínimo ou no máximo.", "Lineage: +1 level and lightning only rolls min or max."),
 "Helbrym's Hide": L("Lineage: Helbrym's Composure ao virar demônio.", "Lineage: Helbrym's Composure on shapeshifting."),
}

SP30 = L("30 Spirit", "30 Spirit"); SP100 = L("100 Spirit", "100 Spirit")
PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Spark + infusões", "Spark + infusions"),
  carry=L("Você: Spark com infusões", "You: Spark with infusions"), dmgSplit=[100, 0],
  goal=L("A Witch do Ignatius não usa Essence Drain/Contagion no leveling (atrapalha a transição). No boss: antes dele nascer, lance Frost Bomb e Orb of Storms (geram Cold e Lightning Infusion) e não lance mais nada; quando nascer, Flame Wall na frente dele (com a Lightning Infusion) e Spark ATRAVÉS do muro; repita Frost Bomb em cima do boss para Exposure. A Cold Infusion faz o Spark soltar faíscas em círculo — mais que o dobro do dano. Clear: deixe o pack juntar, um Contagion e algumas faíscas. Aviso do próprio Ignatius: se Spark e infusões são novidade para você, suba com ED/Contagion e troque nos mapas.",
         "Ignatius's Witch doesn't use Essence Drain/Contagion while leveling (it hurts the transition). On bosses: before it spawns, cast Frost Bomb and Orb of Storms (they create Cold and Lightning Infusions) and cast nothing else; when it spawns, Flame Wall in front of it (with the Lightning Infusion) and Spark THROUGH the wall; repeat Frost Bomb on the boss for Exposure. The Cold Infusion makes Spark fire sparks in a circle — more than double damage. Clear: let the pack group up, one Contagion and a few sparks. Ignatius's own warning: if Spark and infusions are new to you, level with ED/Contagion and swap in maps."),
  rotation=[L("Antes do boss: Frost Bomb + Orb of Storms (infusões) e mais nada", "Before the boss: Frost Bomb + Orb of Storms (infusions) and nothing else"), L("Flame Wall na frente do boss", "Flame Wall in front of the boss"), L("Spark através do muro", "Spark through the wall"), L("Frost Bomb no boss (Exposure) → Spark → Orb → Flame Wall, em ciclo", "Frost Bomb on the boss (Exposure) → Spark → Orb → Flame Wall, in a loop")],
  gems=[
   G("Spark", ["Unleash", "Rapid Casting I"], L("Dano principal", "Main damage"), L("Faíscas que correm pelo chão. Consome Cold Infusion para soltar muitas faíscas em círculo.", "Sparks that travel along the ground. Consumes a Cold Infusion to fire many sparks in a circle."), "free"),
   G("Frost Bomb", ["Overabundance I", "Spell Cascade"], L("Exposure + Cold Infusion", "Exposure + Cold Infusion"), L("Orb que aplica Exposure e deixa uma Cold Infusion ao detonar.", "An orb that applies Exposure and leaves a Cold Infusion on detonation."), "free"),
   G("Orb of Storms", ["Overabundance I", "Unleash"], L("Lightning Infusion", "Lightning Infusion"), L("Orb que dispara raios e deixa Lightning Infusion ao acabar.", "An orb that fires bolts and leaves a Lightning Infusion when it expires."), "free"),
   G("Flame Wall", ["Prolonged Duration I", "Rapid Casting I"], L("Dano extra nos projéteis", "Extra projectile damage"), L("Projéteis que passam pelo muro ganham fogo; com Lightning Infusion, também raio.", "Projectiles passing through gain fire; with a Lightning Infusion, lightning too."), "free"),
   G("Contagion", [], L("Clear (começo)", "Clear (early)"), L("Só no começo: um Contagion no pack e faíscas no alvo.", "Early only: one Contagion on the pack and sparks on the target."), "free", until=12),
   G("Essence Drain", [], L("Dano (começo)", "Damage (early)"), L("Só nos primeiros níveis.", "Only for the first levels."), "free", until=12),
   G("Mana Remnants", [], L("Mana", "Mana"), L("Remnants de mana ao matar/critar inimigos com ailments. 30 Spirit (King in the Mists).", "Mana remnants from killing/critting enemies with ailments. 30 Spirit (King in the Mists)."), "core", 1, SP30),
  ],
  cheap=[L("Wand/staff com + nível de spells, spell damage, cast speed", "Wand/staff with + spell levels, spell damage, cast speed"), L("Botas com Movement Speed", "Boots with Movement Speed")],
  full=[L("Foco com os mesmos mods se estiver de wand", "A focus with the same mods if you're on a wand")],
  stats=[L("+ nível de spells / raio", "+ spell / lightning levels"), L("Spell damage e cast speed", "Spell damage and cast speed"), L("Vida/ES", "Life/ES"), L("Resistências", "Resistances")],
  tree=L("Nós de spell e crítico perto do início da Witch.", "Spell and crit nodes near the Witch start."),
  avoid=[L("Lançar outro spell antes do boss nascer (gasta as infusões)", "Casting another spell before the boss spawns (wastes the infusions)")],
  exit=[L("Rotação de infusões dominada", "Infusion rotation mastered"), L("King in the Mists: Mana Remnants", "King in the Mists: Mana Remnants")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 29], tag=L("Mana Tempest + Arcane Surge", "Mana Tempest + Arcane Surge"),
  carry=L("Você: Spark + Mana Tempest", "You: Spark + Mana Tempest"), dmgSplit=[100, 0],
  goal=L("A rotação ganha o Mana Tempest com Arcane Surge: ele drena sua mana inteira e ativa o Arcane Surge (15 s de regen e cast speed) — ative e SAIA da tempestade, depois recrie para renovar o empower. Elemental Weakness nos alvos resistentes. Demon Form chega com a ascendência (Demonic Possession). Movimento ideal: circule em volta do boss.",
         "The rotation gains Mana Tempest with Arcane Surge: it drains your whole mana and triggers Arcane Surge (15 s of regen and cast speed) — activate it and STEP OUT of the storm, then recast to refresh the empower. Elemental Weakness on tough targets. Demon Form arrives with the ascendancy (Demonic Possession). Ideal movement: circle around the boss."),
  rotation=[L("Frost Bomb + Orb of Storms (infusões)", "Frost Bomb + Orb of Storms (infusions)"), L("Elemental Weakness no boss/rare", "Elemental Weakness on bosses/rares"), L("Mana Tempest → ative o Arcane Surge e saia", "Mana Tempest → trigger Arcane Surge and step out"), L("Flame Wall + Spark em ciclo, renovando as infusões", "Flame Wall + Spark in a loop, refreshing infusions")],
  gems=[
   G("Spark", ["Unleash", "Rapid Casting I", "Pierce I"], L("Dano principal", "Main damage"), L("3 links: Unleash, Rapid Casting e Pierce.", "3 links: Unleash, Rapid Casting and Pierce."), "free"),
   G("Frost Bomb", ["Overabundance I", "Spell Echo", "Short Fuse I"], L("Exposure + Cold Infusion", "Exposure + Cold Infusion"), L("Spell Echo gera Cold Infusions bem mais vezes.", "Spell Echo generates Cold Infusions much more often."), "free"),
   G("Orb of Storms", ["Overabundance I", "Unleash", "Blind I"], L("Lightning Infusion + Blind", "Lightning Infusion + Blind"), L("Blind é defesa que não depende de item.", "Blind is defence that doesn't depend on gear."), "free"),
   G("Flame Wall", ["Prolonged Duration II", "Rapid Casting II"], L("Dano nos projéteis", "Projectile damage"), L("Pode sair no fim do Ato 2 se a rotação ficar pesada.", "Can leave late in Act 2 if the rotation gets too heavy."), "free"),
   G("Mana Tempest", ["Arcane Surge", "Rapid Casting I"], L("Empower + Arcane Surge", "Empower + Arcane Surge"), L("Empodera spells que custam mana dentro dela; drena mana e por isso ativa o Arcane Surge.", "Empowers mana-costing spells inside it; drains mana and so triggers Arcane Surge."), "free"),
   G("Elemental Weakness", ["Magnified Area I", "Heightened Curse"], L("Curse", "Curse"), L("Menos resistência elemental.", "Less elemental resistance."), "free"),
   G("Mana Remnants", ["Harmonic Remnants I", "Remnant Potency I"], L("Mana", "Mana"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Siphon Elements", ["Harmonic Remnants I", "Remnant Potency I"], L("Infusões extras", "Extra infusions"), L("Chance de Infusion Remnant ao dar Freeze/Shock/Ignite. 30 Spirit: só cabe com Spirit no equipamento até o Azak Bog (Ato 3).", "Chance of an Infusion Remnant on Freeze/Shock/Ignite. 30 Spirit: only fits with gear Spirit until Azak Bog (Act 3)."), "opt", 1, SP30),
   G("Demon Form", ["Cooldown Recovery I", "Efficiency I"], L("Burst de spell", "Spell burst"), L("Vira demônio: spells muito mais fortes, mas a vida vai drenando cada vez mais rápido.", "Become a demon: much stronger spells, but life drains faster and faster."), "free"),
  ],
  cheap=[L("Wand/staff com + nível de spells e raio", "Wand/staff with + spell and lightning levels")],
  full=[L("Mesmo; foque resistências e vida/ES", "Same; focus resistances and life/ES")],
  stats=[L("+ nível de spells", "+ spell levels"), L("Resistências", "Resistances"), L("Vida/ES", "Life/ES")],
  tree=L("Crítico e spell damage; primeira ascendência Demonic Possession.", "Crit and spell damage; first ascendancy Demonic Possession."),
  avoid=[L("Ficar parado dentro do Mana Tempest até a mana acabar", "Standing inside Mana Tempest until mana runs out")],
  exit=[L("1ª ascendência: Demonic Possession", "1st ascendancy: Demonic Possession"), L("Supports das 3 primeiras skills com 3 links", "3-link supports on the first 3 skills")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[30, 42], tag=L("Rotação travada", "Locked rotation"),
  carry=L("Você: Spark + infusões", "You: Spark + infusions"), dmgSplit=[100, 0],
  goal=L("A rotação fica igual daqui até os Interlúdios: progressão de gems, supports e equipamento carregam. Com Spell Echo na Frost Bomb você tem Cold Infusion quase na hora (2x+ no Spark). Clear: Frost Bomb (2 infusões) → Orb of Storms → Spark em sequência. Com 30 Spirit num body, Time of Need (útil em Hardcore). Comece a olhar os mods que a troca do endgame pede.",
         "The rotation stays the same until the Interludes: gem progression, supports and gear carry you. With Spell Echo on Frost Bomb you get a Cold Infusion almost immediately (2x+ on Spark). Clear: Frost Bomb (2 infusions) → Orb of Storms → Spark in a row. With 30 Spirit on a body, Time of Need (useful in Hardcore). Start watching for the mods the endgame swap needs."),
  rotation=[L("Frost Bomb (2 infusões)", "Frost Bomb (2 infusions)"), L("Orb of Storms", "Orb of Storms"), L("Spark em sequência", "Spark on repeat")],
  gems=[
   G("Spark", ["Unleash", "Rapid Casting I", "Pierce III"], L("Dano principal", "Main damage"), L("Pierce III: atravessa ilimitados.", "Pierce III: pierces unlimited."), "free"),
   G("Frost Bomb", ["Overabundance I", "Spell Echo", "Short Fuse I"], L("Exposure + Cold Infusion", "Exposure + Cold Infusion"), L("Mesmo papel.", "Same role."), "free"),
   G("Orb of Storms", ["Overabundance I", "Unleash", "Blind I"], L("Lightning Infusion + Blind", "Lightning Infusion + Blind"), L("Mesmo papel.", "Same role."), "free"),
   G("Flame Wall", ["Prolonged Duration II", "Rapid Casting II"], L("Dano nos projéteis", "Projectile damage"), L("Opcional.", "Optional."), "free"),
   G("Mana Tempest", ["Arcane Surge", "Prolonged Duration I", "Rapid Casting I"], L("Empower", "Empower"), L("Mesmo uso.", "Same use."), "free"),
   G("Elemental Weakness", ["Magnified Area I", "Heightened Curse", "Ritualistic Curse"], L("Curse", "Curse"), L("Mesmo uso.", "Same use."), "free"),
   G("Mana Remnants", ["Harmonic Remnants I", "Remnant Potency I"], L("Mana", "Mana"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Siphon Elements", ["Harmonic Remnants I"], L("Infusões extras", "Extra infusions"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Time of Need", ["Compressed Duration I"], L("Defesa", "Defence"), L("Cura e remove curses/ailments periodicamente. 30 Spirit (Azak Bog). Nota: Compressed Duration não afeta mais o intervalo — pode tirar.", "Periodically heals and removes curses/ailments. 30 Spirit (Azak Bog). Note: Compressed Duration no longer affects the interval — you can drop it."), "opt", 1, SP30),
   G("Demon Form", ["Cooldown Recovery I", "Efficiency I"], L("Burst", "Burst"), L("Mesmo uso.", "Same use."), "free"),
  ],
  cheap=[L("Wand/staff melhor a cada tier", "Better wand/staff each tier")],
  full=[L("Comece a guardar peças do endgame barato (veja 'Recoup')", "Start saving pieces for the cheap endgame (see 'Recoup')")],
  stats=[L("+ nível de spells", "+ spell levels"), L("Resistências", "Resistances"), L("Vida/ES", "Life/ES")],
  tree=L("Crítico, spell damage e ES.", "Crit, spell damage and ES."),
  avoid=[L("Mana extra em itens do endgame (mana atrapalha o Pyromantic Pact)", "Extra mana on endgame items (mana hurts Pyromantic Pact)")],
  exit=[L("Azak Bog (+30 Spirit)", "Azak Bog (+30 Spirit)"), L("Spark com Pierce III", "Spark with Pierce III")]),

 dict(id="a4", name=L("Ato 4 + Interlúdios", "Act 4 + Interludes"), lv=[43, 59], tag=L("Preparar Cast on Critical", "Prepare Cast on Critical"),
  carry=L("Você: Spark · Comet começando", "You: Spark · Comet starting"), dmgSplit=[100, 0],
  goal=L("Fase de preparação para o endgame: monte Cast on Critical com Comet (100 Spirit — pode deixar pronto mesmo sem ligar) e Spellslinger com Flame Wall + Spark (Dueling Wand, nível 65). Itens: mana extra é RUIM no endgame; recoup no amuleto é ótimo; pegue o flask Blood of the Warrior, uma Dueling Wand e guarde uma Perfect Essence of Insulation para o cinto.",
         "Endgame prep phase: set up Cast on Critical with Comet (100 Spirit — you can have it ready even if not turned on) and Spellslinger with Flame Wall + Spark (Dueling Wand, level 65). Items: extra mana is BAD in endgame; recoup on the amulet is great; get the Blood of the Warrior flask, a Dueling Wand and save a Perfect Essence of Insulation for the belt."),
  rotation=[L("Igual ao Ato 3", "Same as Act 3"), L("Com Spirit: ligue Cast on Critical e deixe os Comets caírem nos críticos", "With Spirit: turn on Cast on Critical and let Comets fall on crits")],
  gems=[
   G("Spark", ["Unleash", "Rapid Casting III", "Pierce III", "Pinpoint Critical"], L("Dano + críticos", "Damage + crits"), L("Pinpoint Critical: mais críticos para encher o Cast on Critical.", "Pinpoint Critical: more crits to fill Cast on Critical."), "free"),
   G("Cast on Critical", ["Comet", "Spell Cascade", "Boundless Energy II", "Efficiency II"], L("Comets automáticos", "Automatic Comets"), L("Ganha energia com críticos e lança o Comet socketado. A energia depende do DANO do crítico, não só da chance.", "Gains energy on crits and casts the socketed Comet. Energy depends on crit DAMAGE, not just chance."), "opt", 1, SP100),
   G("Spellslinger", ["Flame Wall", "Ignite III", "Spark", "Blind I"], L("Invocação (Dueling Wand)", "Invocation (Dueling Wand)"), L("Vem da Dueling Wand (nível 65). Junta energia ao lançar spells e dispara Flame Wall + Spark.", "Comes from the Dueling Wand (level 65). Gathers energy while casting and triggers Flame Wall + Spark."), "free"),
   G("Frost Bomb", ["Overabundance I", "Spell Echo", "Short Fuse II"], L("Exposure + Cold Infusion", "Exposure + Cold Infusion"), L("Short Fuse II.", "Short Fuse II."), "free"),
   G("Orb of Storms", ["Overabundance I", "Unleash", "Blind I"], L("Lightning Infusion + Blind", "Lightning Infusion + Blind"), L("Mesmo papel.", "Same role."), "free"),
   G("Flame Wall", ["Prolonged Duration II", "Rapid Casting II"], L("Dano nos projéteis", "Projectile damage"), L("Mesmo papel.", "Same role."), "free"),
   G("Elemental Weakness", ["Magnified Area I", "Heightened Curse", "Ritualistic Curse"], L("Curse", "Curse"), L("Mesmo papel.", "Same role."), "free"),
   G("Mana Remnants", ["Harmonic Remnants I", "Remnant Potency I"], L("Mana", "Mana"), L("30 Spirit.", "30 Spirit."), "core", 1, SP30),
   G("Siphon Elements", ["Harmonic Remnants I"], L("Infusões extras", "Extra infusions"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Time of Need", ["Compressed Duration I"], L("Defesa", "Defence"), L("30 Spirit.", "30 Spirit."), "opt", 2, SP30),
   G("Demon Form", ["Cooldown Recovery I", "Efficiency I"], L("Burst", "Burst"), L("Mesmo uso.", "Same use."), "free"),
  ],
  cheap=[L("Pyrophyte Staff", "Pyrophyte Staff"), "Blood of the Warrior", "Beira's Anguish"],
  full=[L("Dueling Wand (65) + Tasalian Focus", "Dueling Wand (65) + Tasalian Focus"), L("Amuleto com recoup", "Amulet with recoup"), L("Perfect Essence of Insulation guardada", "Saved Perfect Essence of Insulation")],
  stats=[L("+ nível de spells", "+ spell levels"), L("Crítico de spell", "Spell crit"), L("Vida/ES e resistências", "Life/ES and resistances"), L("SEM mana extra", "NO extra mana")],
  tree=L("Caminho até os nós de crítico e recoup do endgame.", "Pathing to endgame crit and recoup nodes."),
  avoid=[L("Mana extra em itens", "Extra mana on items"), L("Achar que só chance de crítico enche o Cast on Critical", "Thinking crit chance alone fills Cast on Critical")],
  exit=[L("Cast on Critical + Comet montados", "Cast on Critical + Comet set up"), L("Lythara (+40 Spirit)", "Lythara (+40 Spirit)")]),

 dict(id="maps", name=L("Mapas T1–T9", "Maps T1–T9"), lv=[60, 72], tag=L("Sigil of Power + Comet", "Sigil of Power + Comet"),
  carry=L("Você: Spark · Cast on Critical: Comet", "You: Spark · Cast on Critical: Comet"), dmgSplit=[60, 40],
  goal=L("Não troque para o recoup cedo demais: fique aqui até ter 100% de recoup, 6 links no Comet ou no Spark, muito cast speed, gems nível 19+ com níveis no equipamento e nível ~83. Rotação: Frost Bomb → Orb of Storms → Flame Wall → Spark → Sigil of Power, parado dentro do Sigil. Loyal Hellhound e Demonic Possession na ascendência enquanto junta currency. Rares: vida, Força, SEM mana, ES e resistências.",
         "Don't swap to recoup too early: stay here until you have 100% recoup, 6 links on Comet or Spark, lots of cast speed, level 19+ gems with levels on gear and level ~83. Rotation: Frost Bomb → Orb of Storms → Flame Wall → Spark → Sigil of Power, standing inside the Sigil. Loyal Hellhound and Demonic Possession on the ascendancy while you save currency. Rares: life, Strength, NO mana, ES and resistances."),
  rotation=[L("Frost Bomb → Orb of Storms", "Frost Bomb → Orb of Storms"), L("Flame Wall (com Lightning Infusion) → Spark", "Flame Wall (with Lightning Infusion) → Spark"), L("Sigil of Power: fique dentro (até 4 estágios)", "Sigil of Power: stand inside (up to 4 stages)"), L("Maximize Sparks com Cold Infusion e o buff de 30% do Rising Tempest", "Maximize Cold-infused Sparks and Rising Tempest's 30% buff")],
  gems=[
   G("Spark", ["Pierce III", "Rising Tempest", "Vilenta's Propulsion", "Unleash"], L("Dano principal", "Main damage"), L("Rising Tempest: mais dano elemental por elemento diferente usado.", "Rising Tempest: more elemental damage per different element used."), "free"),
   G("Cast on Critical", ["Comet", "Spell Cascade", "Boundless Energy I"], L("Comets automáticos", "Automatic Comets"), L("100 Spirit.", "100 Spirit."), "core", 1, SP100),
   G("Sigil of Power", ["Magnified Area II", "Prolonged Duration II"], L("Buff de spell damage", "Spell damage buff"), L("Vem do Chiming Staff no Weapon Set 2. Ganha estágios com a mana gasta dentro dele.", "Comes from the Chiming Staff on Weapon Set 2. Gains stages from mana spent inside it."), "free"),
   G("Flame Wall", ["Prolonged Duration II", "Fortress II", "Rapid Casting II", "Arcane Surge"], L("Muro em círculo", "Circular wall"), L("Fortress II: muro em círculo — fique no centro e todas as faíscas passam por ele.", "Fortress II: a circular wall — stand in the centre and every spark passes through it."), "free"),
   G("Frost Bomb", ["Spell Echo", "Overabundance I", "Short Fuse II", "Potent Exposure"], L("Exposure + Cold Infusion", "Exposure + Cold Infusion"), L("Potent Exposure.", "Potent Exposure."), "free"),
   G("Elemental Weakness", ["Heightened Curse", "Magnified Area I", "Doedre's Undoing"], L("Curse no chão", "Ground curse"), L("Doedre's Undoing: curse persistente no chão (rares e bosses).", "Doedre's Undoing: persistent ground curse (rares and bosses)."), "free"),
   G("Orb of Storms", ["Overabundance I", "Unleash", "Considered Casting"], L("Lightning Infusion", "Lightning Infusion"), L("Mesmo papel.", "Same role."), "free"),
   G("Mana Remnants", ["Harmonic Remnants I", "Remnant Potency I"], L("Mana", "Mana"), L("Não é essencial: tire se faltar Spirit.", "Not essential: drop it if short on Spirit."), "opt", 1, SP30),
   G("Siphon Elements", ["Harmonic Remnants II"], L("Infusões extras", "Extra infusions"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Summon Infernal Hound", ["Hulking Minions", "Meat Shield II", "Elemental Army"], L("Defesa (Hellhound)", "Defence (Hellhound)"), L("Loyal Hellhound: companion que dá Ignite em volta. Qualidade reduz o Spirit.", "Loyal Hellhound: a companion that Ignites nearby enemies. Quality lowers its Spirit."), "opt", 2, L("Confira no jogo", "Check in game")),
   G("Demon Form", [], L("Burst", "Burst"), L("Mesmo uso.", "Same use."), "free"),
  ],
  cheap=[L("Staff 6 stats de 1–2 Exalted + Perfect Essence of Sorcery (+5 spells)", "1–2 Exalted 6-stat staff + Perfect Essence of Sorcery (+5 spells)"), "Sacrosanctum"],
  full=[L("Dueling Wand boa (espere até achar uma boa)", "A good Dueling Wand (wait for a good one)"), L("Chiming Staff no Set 2 (Sigil of Power)", "Chiming Staff on Set 2 (Sigil of Power)")],
  stats=[L("Níveis de gem (19+ base e níveis no equipamento)", "Gem levels (19+ base and levels on gear)"), L("Cast speed", "Cast speed"), L("Vida, Força, ES, resistências — SEM mana", "Life, Strength, ES, resistances — NO mana")],
  tree=L("Ascendência: Loyal Hellhound + Demonic Possession + Bringer of Flame.", "Ascendancy: Loyal Hellhound + Demonic Possession + Bringer of Flame."),
  avoid=[L("Trocar para o recoup sem 100% de recoup e gems altas", "Swapping to recoup without 100% recoup and high gems"), L("Comprar Dueling Wand ruim", "Buying a bad Dueling Wand")],
  exit=[L("100% de recoup", "100% recoup"), L("6 links no Comet ou Spark", "6 links on Comet or Spark"), L("Nível ~83", "Level ~83")]),

 dict(id="recoup", name=L("Endgame: Recoup", "Endgame: Recoup"), lv=[73, 84], tag=L("Pyromantic Pact + Demon Form infinito", "Pyromantic Pact + infinite Demon Form"),
  carry=L("Você em Demon Form · Comets do Cast on Critical", "You in Demon Form · Cast on Critical Comets"), dmgSplit=[55, 45],
  goal=L("Aqui as mecânicas abusadas ligam: Pyromantic Pact troca a mana por Infernal Flame (você ENCHE ao gastar) e, quando enche, você toma a vida e o ES máximos como dano de fogo — o recoup (Sacrosanctum, amuleto, cinto) devolve tudo e mais. Com 4000+ de recoup por segundo, você fica infinito em Demon Form; Mastered Darkness tira o limite de Demonflame = dano crescente sem fim. No mapa: spam de Spark até o recoup encher os globos, ative Demon Form e mantenha com Spark e Cast on Critical. Se a vida começar a cair, volte a spammar Spark (normal ao nascer o boss).",
         "This is where the abused mechanics come online: Pyromantic Pact replaces mana with Infernal Flame (you FILL it by spending) and, when it fills, you take your maximum life and ES as fire damage — recoup (Sacrosanctum, amulet, belt) gives it all back and more. With 4000+ recoup per second you stay in Demon Form indefinitely; Mastered Darkness removes the Demonflame cap = endlessly growing damage. In maps: spam Spark until recoup fills your globes, activate Demon Form and keep it up with Spark and Cast on Critical. If life starts dropping, go back to spamming Spark (normal as the boss spawns)."),
  rotation=[L("Spam de Spark até o recoup encher os globos", "Spam Spark until recoup fills your globes"), L("Demon Form", "Demon Form"), L("Spark + Cast on Critical pelo mapa inteiro", "Spark + Cast on Critical for the whole map"), L("Vida caindo: Spark normal até estabilizar", "Life dropping: normal Spark until it stabilizes")],
  gems=[
   G("Spark", ["Pierce III", "Vilenta's Propulsion", "Pinpoint Critical", "Rapid Casting II", "Unleash"], L("Dano + gatilho", "Damage + trigger"), L("Críticos que alimentam o Cast on Critical.", "Crits that feed Cast on Critical."), "free"),
   G("Cast on Critical", ["Comet", "Spell Cascade", "Boundless Energy II", "Energy Retention", "Atalui's Bloodletting"], L("Comets automáticos", "Automatic Comets"), L("Energy Retention: Comets em sequência.", "Energy Retention: Comets back to back."), "core", 1, SP100),
   G("Spellslinger", ["Flame Wall", "Spark", "Arbiter's Ignition", "Ignite III", "Blind II"], L("Invocação", "Invocation"), L("Dueling Wand. Arbiter's Ignition dá Elemental Archon ao Ignitar.", "Dueling Wand. Arbiter's Ignition grants Elemental Archon on Ignite."), "free"),
   G("Orb of Storms", ["Overabundance I", "Unleash", "Lightning Mastery", "Living Lightning II"], L("Lightning Infusion", "Lightning Infusion"), L("Mesmo papel.", "Same role."), "free"),
   G("Frost Bomb", ["Spell Echo", "Magnified Area II", "Overabundance I", "Short Fuse II", "Potent Exposure"], L("Exposure + Cold Infusion", "Exposure + Cold Infusion"), L("Mesmo papel.", "Same role."), "free"),
   G("Elemental Weakness", ["Heightened Curse", "Prolonged Duration II", "Ritualistic Curse", "Cold Mastery", "Doedre's Undoing"], L("Curse", "Curse"), L("Mesmo papel.", "Same role."), "free"),
   G("Siphon Elements", ["Harmonic Remnants II", "Remnant Potency I"], L("Infusões extras", "Extra infusions"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Sigil of Power", ["Prolonged Duration II", "Magnified Area II", "Rapid Casting II"], L("Buff de spell damage", "Spell damage buff"), L("Mesmo papel (Chiming Staff).", "Same role (Chiming Staff)."), "free"),
   G("Demon Form", ["Efficiency II", "Cooldown Recovery II"], L("Dano infinito", "Infinite damage"), L("Com Mastered Darkness e recoup, fica ativo o mapa inteiro.", "With Mastered Darkness and recoup it stays up the whole map."), "free"),
  ],
  cheap=["Sacrosanctum", "Blood of the Warrior", "Maligaro's Virtuosity", L("Cinto com recoup como fogo (Perfect Essence of Insulation)", "Belt with recoup as fire (Perfect Essence of Insulation)")],
  full=[L("Dueling Wand + Runed Focus", "Dueling Wand + Runed Focus"), L("Amuleto com recoup e crítico", "Amulet with recoup and crit")],
  stats=[L("Recoup (amuleto, cinto, Sacrosanctum)", "Recoup (amulet, belt, Sacrosanctum)"), L("Resistência máxima a fogo", "Maximum fire resistance"), L("Vida/Força/cast speed — SEM mana", "Life/Strength/cast speed — NO mana")],
  tree=L("Pyromantic Pact + Mastered Darkness + Demonic Possession + Bringer of Flame.", "Pyromantic Pact + Mastered Darkness + Demonic Possession + Bringer of Flame."),
  avoid=[L("Mapas com less recovery (você se mata)", "Maps with less recovery (you kill yourself)"), L("Mana nos itens (enche a chama mais devagar)", "Mana on items (fills the flame more slowly)")],
  exit=[L("Recoup estável em Demon Form", "Stable recoup in Demon Form"), L("T15", "T15")]),

 dict(id="frost", name=L("Endgame: Low Life", "Endgame: Low Life"), lv=[85, 91], tag=L("Frostbolt + Comet crítico", "Frostbolt + crit Comet"),
  carry=L("Cast on Critical: 2 Comets · você: Frostbolt", "Cast on Critical: 2 Comets · you: Frostbolt"), dmgSplit=[35, 65],
  goal=L("A versão cara troca tudo, mas mantém a casca de recoup. Sai o Demon Form infinito, entra dano próprio: Coward's Legacy te deixa sempre em Low Life, a ascendência vira Altered Flesh + Beidat's Will + Pyromantic Pact + Grinning Immolation (se incendeia ao critar: 50% more dano crítico), 2 Comets no Cast on Critical e Snakepit no anel esquerdo (Frostbolt explode ao acertar). Blink substitui o dodge demoníaco. Bossing muito mais consistente.",
         "The expensive version swaps everything but keeps the recoup shell. Infinite Demon Form leaves, your own damage comes in: Coward's Legacy keeps you permanently on Low Life, the ascendancy becomes Altered Flesh + Beidat's Will + Pyromantic Pact + Grinning Immolation (self-ignite on crit: 50% more crit damage), 2 Comets in Cast on Critical and Snakepit in the left ring (Frostbolt explodes on hit). Blink replaces the demonic dodge. Much more consistent bossing."),
  rotation=[L("Sigil of Power", "Sigil of Power"), L("Frost Bomb (Exposure)", "Frost Bomb (Exposure)"), L("Frost Wall + Spellslinger", "Frost Wall + Spellslinger"), L("Frostbolt: os críticos disparam os Comets", "Frostbolt: crits trigger the Comets")],
  gems=[
   G("Frostbolt", ["Sione's Temper", "Vilenta's Propulsion", "Trickster's Shard", "Blindside", "Execute III"], L("Dano + gatilho", "Damage + trigger"), L("Projétil lento que explode; Execute III em Low Life.", "Slow projectile that explodes; Execute III on Low Life."), "free"),
   G("Cast on Critical", ["Comet", "Comet", "Boundless Energy II", "Uhtred's Omen", "Atalui's Bloodletting"], L("2 Comets", "2 Comets"), L("Dois Comets por disparo.", "Two Comets per trigger."), "core", 1, SP100),
   G("Spellslinger", ["Flame Wall", "Living Bomb", "Spark", "Blind II", "Arbiter's Ignition"], L("Invocação", "Invocation"), L("Living Bomb deixa Fire Infusion para o Comet (explosão de gelo e fogo).", "Living Bomb leaves a Fire Infusion for Comet (ice and fire blast)."), "free"),
   G("Frost Wall", ["Fortress II", "Spell Cascade", "Rapid Casting II", "Second Wind II", "Blindside"], L("Muro de gelo", "Ice wall"), L("Muro em círculo; explode com Lightning Infusion.", "Circular wall; explodes with a Lightning Infusion."), "free"),
   G("Frost Bomb", ["Spell Echo", "Overabundance I", "Prolonged Duration II", "Potent Exposure", "Blind II"], L("Exposure", "Exposure"), L("Mesmo papel.", "Same role."), "free"),
   G("Elemental Weakness", ["Heightened Curse", "Ritualistic Curse", "Doedre's Undoing"], L("Curse", "Curse"), L("Mesmo papel.", "Same role."), "free"),
   G("Blink", ["Atziri's Impatience", "Rapid Casting II", "Uhtred's Augury"], L("Mobilidade", "Mobility"), L("Substitui o dodge por um teleporte. 60 Spirit.", "Replaces dodge with a teleport. 60 Spirit."), "core", 3, L("60 Spirit", "60 Spirit")),
   G("Sigil of Power", ["Magnified Area II", "Prolonged Duration II", "Rapid Casting II"], L("Buff", "Buff"), L("Mesmo papel.", "Same role."), "free"),
   G("Siphon Elements", ["Harmonic Remnants II", "Khatal's Rejuvenation"], L("Infusões", "Infusions"), L("30 Spirit.", "30 Spirit."), "core", 2, SP30),
   G("Charge Regulation", ["Cannibalism I"], L("Buffs por charge", "Charge buffs"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Combat Frenzy", [], L("Frenzy Charges", "Frenzy Charges"), L("Frenzy Charge ao congelar. 30 Spirit.", "Frenzy Charge on Freeze. 30 Spirit."), "opt", 1, SP30),
  ],
  cheap=["Coward's Legacy", "Snakepit", "Sacrosanctum", "Blood of the Warrior"],
  full=[L("Kamasan Tiara com anoint", "Anointed Kamasan Tiara"), L("Line of Olroth (timeless) + keystone convertido", "Line of Olroth (timeless) + converted keystone")],
  stats=[L("Dano crítico de spell", "Spell crit damage"), L("Níveis de gem", "Gem levels"), L("Força, vida, ES, resistências", "Strength, life, ES, resistances")],
  tree=L("Altered Flesh, Beidat's Will, Pyromantic Pact, Grinning Immolation; nós de dano crítico permanente.", "Altered Flesh, Beidat's Will, Pyromantic Pact, Grinning Immolation; permanent crit damage nodes."),
  avoid=[L("Mapas com less recovery", "Maps with less recovery")],
  exit=[L("Bosses de 4–5 milhões de vida em ~10 s", "4–5 million HP bosses in ~10 s")]),

 dict(id="max", name=L("Luxo: CoA Comet", "Luxury: CoA Comet"), lv=[92, 100], tag=L("Auto Spark + Cast on Elemental Ailment", "Auto Spark + Cast on Elemental Ailment"),
  carry=L("Cast on Elemental Ailment: Comets · Cast on Dodge: Spark", "Cast on Elemental Ailment: Comets · Cast on Dodge: Spark"), dmgSplit=[20, 80],
  goal=L("A versão do kingkongor (build do Bladezero): o Earthbound no Weapon Set 2 faz o snapshot de 'dispara Spark ao matar inimigo Shocked' e, junto do buff Pinnacle of Power do Adonia's Ego, você só anda em Demon Form dando dodge enquanto tudo explode fora da tela. No boss: Powered by Verisium e algumas Ball Lightning criam fogo no chão, que ativa o Cast on Elemental Ailment sem parar = tapete de Comets. Defesa: matar antes, regen enorme do Reverie e Mageblood com Legacy of Ruby (+Topaz/Bismuth) para ter resistência máxima a fogo contra o próprio Pyromantic Pact. Muito caro e precisa de setup a cada mapa; não roda mapas com menos recuperação/resistência.",
         "kingkongor's version (Bladezero's build): Earthbound on Weapon Set 2 snapshots 'trigger Spark on killing a Shocked enemy' and, together with Adonia's Ego's Pinnacle of Power buff, you just walk in Demon Form dodging while everything explodes off-screen. Bosses: Powered by Verisium and a few Ball Lightnings create floor fire, which triggers Cast on Elemental Ailment nonstop = a carpet of Comets. Defence: kill first, Reverie's huge regen and Mageblood with Legacy of Ruby (+Topaz/Bismuth) for enough max fire resistance against your own Pyromantic Pact. Very expensive and needs a setup every map; can't run reduced recovery/resistance maps."),
  rotation=[L("1. Troque para o Weapon Set 2 (Earthbound)", "1. Swap to Weapon Set 2 (Earthbound)"), L("2. Powered by Verisium", "2. Powered by Verisium"), L("3. Ball Lightning", "3. Ball Lightning"), L("4. Lightning Warp em cima da Ball Lightning (Elemental Equilibrium: vira Cold Infusion)", "4. Lightning Warp onto the Ball Lightning (Elemental Equilibrium: it becomes a Cold Infusion)"), L("5. Spam de Spark até as Power Charges máximas", "5. Spam Spark up to max Power Charges"), L("6. Powered by Verisium de novo (opcional)", "6. Powered by Verisium again (optional)"), L("7. Rite of Restoration — força a volta para o Set 1 (Adonia's Ego)", "7. Rite of Restoration — forces the swap back to Set 1 (Adonia's Ego)"), L("8. Pinnacle of Power — se esquecer, você morre", "8. Pinnacle of Power — forget it and you die"), L("9. Demon Form e dodge pelo mapa; o buff dura 2 (às vezes 4) minutos, depois recomece", "9. Demon Form and dodge through the map; the buff lasts 2 (sometimes 4) minutes, then start over")],
  gems=[
   G("Cast on Elemental Ailment", ["Comet", "Comet", "Spell Cascade", "Efficiency II", "Energy Retention"], L("Comets automáticos", "Automatic Comets"), L("Energia ao dar Freeze/Shock/Ignite.", "Energy on Freeze/Shock/Ignite."), "core", 1, SP100),
   G("Cast on Dodge", ["Spark", "Runic Extraction", "Wildshards II", "Projectile Acceleration III", "Energy Retention"], L("Spark no dodge", "Spark on dodge"), L("100 Spirit.", "100 Spirit."), "core", 2, SP100),
   G("Pinnacle of Power", ["Prolonged Duration II", "Heightened Charges", "Cooldown Recovery II"], L("Buff de charges", "Charge buff"), L("Consome as Power Charges máximas para dominar os elementos.", "Consumes max Power Charges to master the elements."), "free"),
   G("Power Siphon", ["Rapid Casting III", "Living Lightning II", "Mobility"], L("Power Charges", "Power Charges"), L("Está no setup do kingkongor, mas a rotação dele gera as Power Charges com Spark: opcional.", "It's in kingkongor's setup, but his rotation builds Power Charges with Spark: optional."), "free"),
   G("Lightning Warp", ["Vorana's Siege", "Khatal's Rejuvenation", "Ice Bite II", "Innervate", "Prolonged Duration II"], L("Infusão + teleporte", "Infusion + teleport"), L("Teleporta e cria infusão.", "Teleports and creates an infusion."), "free"),
   G("Rite of Restoration", ["Uhtred's Rite", "Prolonged Duration II", "Uhtred's Constellation", "Magnified Area II"], L("Regen", "Regen"), L("Regeneração enorme — obrigatório.", "Huge regeneration — mandatory."), "free"),
   G("Ball Lightning", ["Unleash", "Multishot II", "Prolonged Duration II", "Ignite III", "Mobility"], L("Boss", "Boss"), L("Com Fire Infusion cria chão em chamas: Ignites em série = Comets em série.", "With a Fire Infusion it creates burning ground: chained Ignites = chained Comets."), "free"),
   G("Lightning Bolt", ["Trickster's Shard", "Spell Cascade", "Concentrated Area", "Mobility", "Rapid Casting II"], L("Self-cast", "Self-cast"), L("Apaga o que chegar perto.", "Deletes whatever gets close."), "free"),
   G("Spark", ["Rapid Casting III", "Projectile Acceleration III", "Pinpoint Critical", "Fork", "Mobility"], L("Spark manual", "Manual Spark"), L("Opcional.", "Optional."), "free"),
   G("Explosive Transmutation", ["Runic Extraction", "Cooldown Recovery II", "Morrigan's Insight", "Fire Mastery", "Spell Cascade"], L("Guard + explosões", "Guard + explosions"), L("Com Mórrigan's Insight, as infusões do Runic Extraction consomem Freeze e dão Guard (~2800 no guia). 30 Spirit.", "With Mórrigan's Insight, Runic Extraction's infusions consume Freeze and grant Guard (~2800 in the guide). 30 Spirit."), "core", 3, SP30),
   G("Remnants of Kalguur", ["Harmonic Remnants II"], L("Runic Ward", "Runic Ward"), L("30 Spirit.", "30 Spirit."), "core", 4, SP30),
   G("Powered by Verisium", ["Atziri's Impatience", "Efficiency II"], L("Verisium Infusion", "Verisium Infusion"), L("Gasta Ward para gerar infusões coringa.", "Spends Ward to generate wildcard infusions."), "free"),
   G("Demon Form", ["Cooldown Recovery II"], L("Forma demoníaca", "Demon form"), L("Ande e dê dodge.", "Walk and dodge."), "free"),
  ],
  cheap=["Earthbound", "Choir of the Storm", "Threaded Light", "Decree of Flight"],
  full=["Mageblood", "Reverie", "Alpha's Howl", "Grip of Kulemak", "Adonia's Ego", "Rite of Passage · For Utopia · Nascent Hope"],
  stats=[L("Spirit (Alpha's Howl, Grip of Kulemak)", "Spirit (Alpha's Howl, Grip of Kulemak)"), L("Movement speed 72%+ e dodge 30%+", "72%+ movement speed and 30%+ dodge"), L("Resistência máxima a fogo", "Maximum fire resistance")],
  tree=L("Altered Flesh, Pyromantic Pact, Grinning Immolation, Demonic Possession.", "Altered Flesh, Pyromantic Pact, Grinning Immolation, Demonic Possession."),
  avoid=[L("Esquecer o Rite of Restoration", "Forgetting Rite of Restoration"), L("Mapas com less recovery/resistência", "Maps with less recovery/resistance")],
  exit=[L("Delirium 200% e carry de grupo", "200% Delirium and group carry")]),
]
PH = {p["id"]: p for p in PHASES}

BOX = {
 "a1": ("2", [L("Cold + Lightning", "Cold + Lightning")], L("Frost Bomb dá Cold Infusion (Spark em círculo) e Orb of Storms dá Lightning Infusion (Flame Wall com raio).", "Frost Bomb gives a Cold Infusion (Spark in a circle) and Orb of Storms gives a Lightning Infusion (Flame Wall with lightning).")),
 "a3": ("2+", [L("Spell Echo", "Spell Echo")], L("Spell Echo na Frost Bomb: Cold Infusion quase na hora.", "Spell Echo on Frost Bomb: Cold Infusion almost immediately.")),
 "maps": ("4", [L("estágios do Sigil", "Sigil stages")], L("Gaste mana dentro do Sigil of Power até 4 estágios (50%+ more spell damage).", "Spend mana inside Sigil of Power up to 4 stages (50%+ more spell damage).")),
 "recoup": ("∞", [L("Demonflame (Mastered Darkness)", "Demonflame (Mastered Darkness)")], L("Sem limite de Demonflame enquanto o recoup segurar a vida.", "No Demonflame cap while recoup holds your life.")),
 "frost": ("2", [L("Comets por disparo", "Comets per trigger")], L("Dois Comets no Cast on Critical.", "Two Comets in Cast on Critical.")),
 "max": ("2–4 min", [L("buff do Pinnacle", "Pinnacle buff")], L("O buff dura 2 a 4 minutos (4 minutos = 4x o dano). Quando acabar, refaça o setup.", "The buff lasts 2 to 4 minutes (4 minutes = 4x damage). When it ends, redo the setup.")),
}
SPIRIT_NOTE = {
 "a2": L("Mana Remnants (30) do King in the Mists; Siphon Elements (30) só com Spirit no equipamento.", "Mana Remnants (30) from King in the Mists; Siphon Elements (30) only with gear Spirit."),
 "a4": L("Cast on Critical (100) só quando couber: King 30 + Azak 30 + Lythara 40 + itens.", "Cast on Critical (100) only when it fits: King 30 + Azak 30 + Lythara 40 + items."),
 "maps": L("Ordem: Cast on Critical (100) → Siphon Elements (30) → Mana Remnants/Hellhound se sobrar.", "Order: Cast on Critical (100) → Siphon Elements (30) → Mana Remnants/Hellhound if spare."),
 "recoup": L("Cast on Critical (100) + Siphon Elements (30). Sem mana, sem Mana Remnants.", "Cast on Critical (100) + Siphon Elements (30). No mana, no Mana Remnants."),
 "frost": L("Cast on Critical (100) → Siphon (30) → Blink (60) → Charge Regulation (30) → Combat Frenzy (30). Beidat's Will dá Spirit por vida.", "Cast on Critical (100) → Siphon (30) → Blink (60) → Charge Regulation (30) → Combat Frenzy (30). Beidat's Will grants Spirit per life."),
 "max": L("Cast on Elemental Ailment (100) + Cast on Dodge (100) + Explosive Transmutation (30) + Remnants of Kalguur (30): Spirit altíssimo (Alpha's Howl +100).", "Cast on Elemental Ailment (100) + Cast on Dodge (100) + Explosive Transmutation (30) + Remnants of Kalguur (30): very high Spirit (Alpha's Howl +100)."),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in SPIRIT_NOTE.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Spark + Frost Bomb + Orb of Storms. Rotação de infusões.", "Spark + Frost Bomb + Orb of Storms. Infusion rotation."),
 10: L("King in the Mists (+30 Spirit) → Mana Remnants.", "King in the Mists (+30 Spirit) → Mana Remnants."),
 16: L("Mana Tempest + Arcane Surge. Elemental Weakness.", "Mana Tempest + Arcane Surge. Elemental Weakness."),
 26: L("1ª ascendência: Demonic Possession (Demon Form).", "1st ascendancy: Demonic Possession (Demon Form)."),
 30: L("Pierce III no Spark; Spell Echo na Frost Bomb.", "Pierce III on Spark; Spell Echo on Frost Bomb."),
 38: L("Azak Bog (+30 Spirit). 2ª ascendência: Bringer of Flame.", "Azak Bog (+30 Spirit). 2nd ascendancy: Bringer of Flame."),
 45: L("Monte Cast on Critical + Comet (100 Spirit).", "Set up Cast on Critical + Comet (100 Spirit)."),
 50: L("Blood of the Warrior e Beira's Anguish.", "Blood of the Warrior and Beira's Anguish."),
 55: L("Guarde Perfect Essence of Insulation para o cinto.", "Save a Perfect Essence of Insulation for the belt."),
 62: L("Lythara (+40 Spirit).", "Lythara (+40 Spirit)."),
 65: L("Dueling Wand (Spellslinger) e Chiming Staff (Sigil of Power) no Set 2.", "Dueling Wand (Spellslinger) and Chiming Staff (Sigil of Power) on Set 2."),
 68: L("Staff 6 stats + Perfect Essence of Sorcery (se não tiver Dueling Wand boa).", "6-stat staff + Perfect Essence of Sorcery (if you lack a good Dueling Wand)."),
 75: L("TROCA para o recoup: Pyromantic Pact + Mastered Darkness. Sacrosanctum.", "SWAP to recoup: Pyromantic Pact + Mastered Darkness. Sacrosanctum."),
 85: L("Low Life: Coward's Legacy, Snakepit, Grinning Immolation, 2 Comets.", "Low Life: Coward's Legacy, Snakepit, Grinning Immolation, 2 Comets."),
 92: L("Luxo: Earthbound (Set 2), Cast on Elemental Ailment + Cast on Dodge.", "Luxury: Earthbound (Set 2), Cast on Elemental Ailment + Cast on Dodge."),
}

ASCENDANCY = [
 dict(order=1, key="possession", node="Demonic Possession", when=L("1º Trial (~nível 26)", "1st Trial (~level 26)"), text=L("Concede o skill Demon Form.", "Grants Skill: Demon Form."), why=L("Burst de spell e, com recoup, dano infinito.", "Spell burst and, with recoup, infinite damage.")),
 dict(order=2, key="bringer", node="Bringer of Flame", when=L("2º Trial (~nível 38)", "2nd Trial (~level 38)"), text=L("Todo dano seu e de aliados contribui para Flammability e Ignite.", "All damage from you and allies contributes to Flammability and Ignite magnitudes."), why=L("Ignite com raio e frio: alimenta infusões e Siphon Elements.", "Ignite with lightning and cold: feeds infusions and Siphon Elements.")),
 dict(order=3, key="hellhound", node="Loyal Hellhound", when=L("Mapas (temporário)", "Maps (temporary)"), text=L("Concede Summon Infernal Hound.", "Grants Skill: Summon Infernal Hound."), why=L("Defesa enquanto você junta currency para a troca.", "Defence while you save currency for the swap.")),
 dict(order=4, key="pact", node="Pyromantic Pact", when=L("Troca para o recoup (~73)", "Recoup swap (~73)"), text=L("Mana vira Infernal Flame em dobro; gastar ENCHE a chama; cheia, você toma vida+ES máximos como fogo e zera.", "Mana becomes twice as much Infernal Flame; spending FILLS it; when full you take max life+ES as fire and it resets."), why=L("Mana infinita; com recoup o dano em você vira cura.", "Infinite mana; with recoup the self-damage becomes healing.")),
 dict(order=5, key="darkness", node="Mastered Darkness", when=L("Troca para o recoup (~73)", "Recoup swap (~73)"), text=L("Demonflame não tem máximo.", "Demonflame has no maximum."), why=L("Demon Form escala sem limite.", "Demon Form scales without limit.")),
 dict(order=6, key="immolation", node="Grinning Immolation", when=L("Low Life (~85)", "Low Life (~85)"), text=L("Ao critar você se incendeia (15% de vida+ES por segundo); 50% more dano crítico.", "Critting ignites you (15% of life+ES per second); 50% more Critical Damage Bonus."), why=L("Dano crítico enorme; o recoup paga a queima.", "Huge crit damage; recoup pays the burn.")),
 dict(order=7, key="altered", node="Altered Flesh", when=L("Low Life (~85)", "Low Life (~85)"), text=L("20% do físico recebido como Chaos; 20% de raio e frio recebidos como fogo.", "20% of physical taken as Chaos; 20% of lightning and cold taken as fire."), why=L("Converte dano para a resistência a fogo alta.", "Converts damage into your high fire resistance.")),
 dict(order=8, key="beidat", node="Beidat's Will", when=L("Low Life (~85)", "Low Life (~85)"), text=L("Reserva 25% da vida; +1 Spirit por 25 de vida máxima.", "Reserves 25% of life; +1 Spirit per 25 maximum life."), why=L("Spirit para Blink e charges; ajuda o Low Life.", "Spirit for Blink and charges; helps Low Life.")),
]
ASC_UNLOCK = [26, 38, 60, 73, 73, 85, 85, 85]
ASC_PHASE = {"a2": ["Demonic Possession"], "a3": ["Demonic Possession", "Bringer of Flame"], "a4": ["Demonic Possession", "Bringer of Flame"]}

KEY_PASSIVES = [
 dict(node="Pyromantic Pact", type=L("Ascendência", "Ascendancy"), text=L("Infernal Flame no lugar da mana.", "Infernal Flame instead of mana."), when="73+", why=L("Menos mana e custos maiores = recoup mais frequente.", "Less mana and higher costs = more frequent recoup.")),
 dict(node="Grinning Immolation", type=L("Ascendência", "Ascendancy"), text=L("Auto-Ignite no crítico; 50% more dano crítico.", "Self-ignite on crit; 50% more crit damage."), when="85+", why=L("Dano de boss da versão cara.", "Boss damage of the expensive version.")),
 dict(node="Mastered Darkness", type=L("Ascendência", "Ascendancy"), text=L("Demonflame sem máximo.", "No Demonflame maximum."), when="73–84", why=L("Demon Form infinito.", "Infinite Demon Form.")),
]
TREE_STAGES = [
 dict(lv="1–42", focus=L("Spell, crítico, raio", "Spell, crit, lightning"), dmg="Spark + infusões", **{"def": L("Vida/ES + Blind", "Life/ES + Blind")}, spirit="Mana Remnants, Siphon", dont=L("Gastar infusões antes do boss", "Wasting infusions before the boss")),
 dict(lv="43–72", focus=L("Crítico + cast speed", "Crit + cast speed"), dmg="Spark + Cast on Critical Comet", **{"def": L("ES, resistências", "ES, resistances")}, spirit="Cast on Critical", dont=L("Mana nos itens", "Mana on items")),
 dict(lv="73–84", focus="Recoup", dmg=L("Demon Form infinito", "Infinite Demon Form"), **{"def": L("Recoup 100%+", "100%+ recoup")}, spirit="CoC + Siphon", dont=L("Mapas sem recovery", "No-recovery maps")),
 dict(lv="85–100", focus=L("Low Life + dano crítico", "Low Life + crit damage"), dmg=L("Frostbolt/Comet ou CoA Comet", "Frostbolt/Comet or CoA Comet"), **{"def": L("Altered Flesh, recoup", "Altered Flesh, recoup")}, spirit=L("Beidat's Will / Alpha's Howl", "Beidat's Will / Alpha's Howl"), dont=L("Esquecer Rite of Restoration (CoA)", "Forgetting Rite of Restoration (CoA)")),
]

UNIQUES = [
 U("Sacrosanctum", "Body Armour", L("Armadura", "Armour"), "maps", L("Armour/ES, Força, Inteligência, Chaos Resistance e 10–19% do dano recebido recuperado como vida — e também como ES.", "Armour/ES, Strength, Intelligence, Chaos Resistance and 10–19% of damage taken recouped as life — and also as ES."), L("O único requisito do endgame barato: o roll não importa, a última linha (recoup em ES) sim.", "The cheap endgame's only requirement: the roll doesn't matter, the last line (ES recoup) does."), L("Não há substituto para o recoup.", "No substitute for the recoup.")),
 U("Blood of the Warrior", "Flask", "Flask", "a4", L("15–30% do dano recebido durante o efeito recuperado como vida (o Ignatius usa ~30%); o efeito não sai com a vida cheia.", "15–30% of damage taken during effect recouped as life (Ignatius uses ~30%); the effect isn't removed at full life."), L("Complementa o recoup sem custo.", "Complements recoup at no cost."), L("Flask de vida normal.", "Normal life flask.")),
 U("Beira's Anguish", "Charm", "Charm", "a4", L("Chão em chamas que ignita inimigos baseado na sua vida.", "Burning ground that ignites enemies based on your life."), L("Ignite = energia/infusões.", "Ignite = energy/infusions."), L("Dousing Charm.", "Dousing Charm.")),
 U("Maligaro's Virtuosity", L("Luvas", "Gloves"), L("Armadura", "Armour"), "recoup", L("Chance de crítico aumentada, crítico não pode ser rerolado e Critical Damage Bonus fixo em 250%.", "Increased crit chance, crit chance can't be rerolled and Critical Damage Bonus fixed at 250%."), L("Início do endgame, se barata.", "Early endgame, if cheap."), L("Luvas rare de ES.", "Rare ES gloves.")),
 U("Coward's Legacy", L("Cinto", "Belt"), L("Acessório", "Accessory"), "frost", L("Você é considerado em Low Life com 75% da vida ou menos.", "You are considered on Low Life at 75% of maximum life or below."), L("Base do Low Life (Execute III).", "Base of Low Life (Execute III)."), L("Cinto com recoup.", "Belt with recoup.")),
 U("Snakepit", L("Anel", "Ring"), L("Acessório", "Accessory"), "frost", L("Spell damage, cast speed; no anel esquerdo, projéteis de spell se dividem em vez de encadear.", "Spell damage, cast speed; in the left ring slot, spell projectiles fork instead of chaining."), L("Anel esquerdo (Frostbolt explode ao acertar).", "Left ring (Frostbolt explodes on hit)."), L("Anel rare.", "Rare ring.")),
 U("Earthbound", L("Cajado (Set 2)", "Staff (Set 2)"), L("Arma", "Weapon"), "max", L("Spell damage, cast speed e dispara Spark ao matar inimigo Shocked.", "Spell damage, cast speed and triggers Spark on killing a Shocked enemy."), L("Weapon Set 2 do setup CoA (snapshot).", "Weapon Set 2 of the CoA setup (snapshot)."), L("Também é um cajado de leveling barato.", "Also a cheap leveling staff.")),
 U("Choir of the Storm", L("Amuleto", "Amulet"), L("Acessório", "Accessory"), "max", L("Críticos ignoram resistência a raio e disparam Lightning Bolt.", "Crits ignore lightning resistance and trigger Lightning Bolt."), L("Variante 'Cheaper' do kingkongor.", "kingkongor's 'Cheaper' variant."), L("Amuleto de Spirit.", "Spirit amulet.")),
 U("Alpha's Howl", L("Capacete", "Helmet"), L("Armadura", "Armour"), "max", L("+100 Spirit, Evasion, resistência a frio, Presence dobrada.", "+100 Spirit, Evasion, cold resistance, doubled Presence."), L("Paga as duas meta skills de 100.", "Pays for both 100-Spirit meta skills."), L("Capacete rare de Spirit.", "Rare Spirit helmet.")),
 U("Reverie", "Body Armour", L("Armadura", "Armour"), "max", L("Armour/ES, Chaos Resistance; -10% resistência a fogo e menos recuperação de life flask.", "Armour/ES, Chaos Resistance; -10% fire resistance and less life flask recovery."), L("No setup do kingkongor dá a regen de vida enorme (~1900 vida/s no guia).", "In kingkongor's setup it provides the huge life regen (~1900 life/s in the guide)."), "Sacrosanctum"),
 U("Decree of Flight", L("Botas", "Boots"), L("Armadura", "Armour"), "max", L("30% Movement Speed, dodge mais rápido e Guard no dodge.", "30% Movement Speed, faster dodge and Guard on dodge."), L("Dodge é o gatilho do Cast on Dodge.", "Dodge is Cast on Dodge's trigger."), L("Botas rare 30%+.", "Rare 30%+ boots.")),
 U("Grip of Kulemak", L("Anel", "Ring"), L("Acessório", "Accessory"), "max", L("Anel do Abyss: no setup CoA precisa de % increased Spirit, +1 Maximum Power Charges e cast speed por 20 Spirit (os três entre os dois anéis).", "Abyss ring: the CoA setup needs % increased Spirit, +1 Maximum Power Charges and cast speed per 20 Spirit (all three across the two rings)."), L("Obrigatório nos dois anéis; talvez precise farmar (ordem do kingkongor: Kurgal > Kurgal > Amanamu).", "Mandatory in both rings; you may need to farm them (kingkongor's order: Kurgal > Kurgal > Amanamu)."), L("Sem ele o setup perde Spirit e Power Charges.", "Without it the setup loses Spirit and Power Charges.")),
 U("Adonia's Ego", L("Wand (Set 1)", "Wand (Set 1)"), L("Arma", "Weapon"), "max", L("+3 spells, cast speed e mana; -10% resistência elemental por Power Charge.", "+3 spells, cast speed and mana; -10% elemental resistance per Power Charge."), L("Weapon Set 1 do CoA, runemastered com +1 Power Charge. O Pinnacle of Power usa as Power Charges.", "CoA Weapon Set 1, runemastered with +1 Power Charge. Pinnacle of Power uses the Power Charges."), L("Dueling Wand rare com + spells.", "Rare Dueling Wand with + spells.")),
 U("Threaded Light", L("Foco (Set 1)", "Focus (Set 1)"), L("Arma", "Weapon"), "max", L("% ES, regen de mana e spell damage por 10 Spirit.", "% ES, mana regen and spell damage per 10 Spirit."), L("Offhand do Adonia's Ego; com o Spirit altíssimo do setup vira muito dano (runemastered: quanto mais spell damage por Spirit, melhor).", "Adonia's Ego's off-hand; with the setup's very high Spirit it becomes lots of damage (runemastered: the more spell damage per Spirit, the better)."), L("Foco rare com + spells.", "Rare focus with + spells.")),
 U("Nascent Hope", "Charm", "Charm", "max", L("Recarga de ES ao usar; chance de carga ao matar.", "ES recharge on use; charge chance on kill."), L("Usa sozinho quando você é congelado.", "Triggers by itself when you're frozen."), "Thawing Charm"),
 U("Rite of Passage", "Charm", "Charm", "max", L("Possessão por espíritos (Cat, Stag, Boar, Serpent, Primate) ao matar rare/unique; o guia usa Cat.", "Spirit possession (Cat, Stag, Boar, Serpent, Primate) when killing a rare/unique; the guide uses Cat."), L("Luxo do setup CoA.", "CoA setup luxury."), "Golden Charm"),
 U("For Utopia", "Charm", "Charm", "max", L("Defende com 200% da Armour durante o efeito.", "Defend with 200% of Armour during effect."), L("Luxo do setup CoA.", "CoA setup luxury."), "Stone Charm"),
 U("Mageblood", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Legados de flask permanentes — o kingkongor usa Legacy of Ruby para a resistência máxima a fogo.", "Permanent flask legacies — kingkongor uses Legacy of Ruby for max fire resistance."), L("Obrigatório no CoA para aguentar o próprio dano.", "Mandatory in CoA to survive self-damage."), "Coward's Legacy"),
]

GEAR = [
 dict(slot=L("Arma", "Weapon"), cheap=L("Wand/staff com + spells, spell damage e cast speed", "Wand/staff with + spells, spell damage and cast speed"), value=L("Staff 6 stats + Perfect Essence of Sorcery (+5)", "6-stat staff + Perfect Essence of Sorcery (+5)"), full=L("Dueling Wand (Spellslinger) + Tasalian/Runed Focus", "Dueling Wand (Spellslinger) + Tasalian/Runed Focus"), affix=L("+ nível de spells; crítico de spell; cast speed", "+ spell levels; spell crit; cast speed"), note=L("Weapon Set 2: Chiming Staff (Sigil of Power) ou Earthbound (CoA).", "Weapon Set 2: Chiming Staff (Sigil of Power) or Earthbound (CoA).")),
 dict(slot=L("Capacete", "Helmet"), cheap=L("ES + resistências", "ES + resistances"), value=L("Ancestral/Sorcerous Tiara com socket de recoup", "Ancestral/Sorcerous Tiara with a recoup socket"), full=L("Kamasan Tiara com anoint", "Anointed Kamasan Tiara"), affix=L("ES; vida; resist", "ES; life; resist"), note=""),
 dict(slot="Body Armour", cheap=L("ES + resist", "ES + resist"), value="Sacrosanctum", full="Sacrosanctum", affix=L("Recoup em ES (Sacrosanctum)", "ES recoup (Sacrosanctum)"), note=L("Pode rolar resistência máxima a fogo e duração de skill.", "Can roll max fire resistance and skill duration.")),
 dict(slot=L("Luvas", "Gloves"), cheap=L("ES + resist", "ES + resist"), value="Maligaro's Virtuosity", full=L("Sirenscale Gloves Runeforged (Ward)", "Runeforged Sirenscale Gloves (Ward)"), affix=L("Crítico; ES; resist", "Crit; ES; resist"), note=""),
 dict(slot=L("Botas", "Boots"), cheap=L("Movement Speed + ES", "Movement Speed + ES"), value=L("Dunerunner/Lattice Sandals", "Dunerunner/Lattice Sandals"), full=L("Sandsworn Sandals (10% MS permanente)", "Sandsworn Sandals (permanent 10% MS)"), affix=L("Movement Speed; ES; resist", "Movement Speed; ES; resist"), note=""),
 dict(slot=L("Amuleto", "Amulet"), cheap="Solar Amulet", value=L("Recoup + crítico + ES", "Recoup + crit + ES"), full=L("Recoup, crítico, % ES e + spells", "Recoup, crit, % ES and + spells"), affix=L("Recoup como vida; crítico; Spirit", "Recoup as life; crit; Spirit"), note=L("SEM mana.", "NO mana.")),
 dict(slot=L("Anéis", "Rings"), cheap=L("Resistências + mods de spell", "Resistances + spell mods"), value=L("Prismatic Ring", "Prismatic Ring"), full=L("Snakepit (esquerdo) + Prismatic", "Snakepit (left) + Prismatic"), affix=L("Resist; cast speed; spell damage", "Resist; cast speed; spell damage"), note=""),
 dict(slot=L("Cinto", "Belt"), cheap=L("Vida + resist", "Life + resist"), value=L("Heavy Belt com recoup como fogo (Perfect Essence of Insulation)", "Heavy Belt with recoup as fire (Perfect Essence of Insulation)"), full="Coward's Legacy · Mageblood", affix=L("Recoup; resist", "Recoup; resist"), note=""),
 dict(slot="Charms", cheap=L("Thawing + Dousing + Golden", "Thawing + Dousing + Golden"), value="Beira's Anguish", full="Rite of Passage · For Utopia · Nascent Hope", affix=L("Freeze/Ignite", "Freeze/Ignite"), note=""),
 dict(slot="Flasks", cheap=L("Vida + mana (leveling)", "Life + mana (leveling)"), value="Blood of the Warrior", full="Blood of the Warrior", affix=L("Recoup", "Recoup"), note=L("Com Pyromantic Pact não existe mana.", "With Pyromantic Pact there is no mana.")),
]
BUY_ORDER = [
 dict(p=1, item=L("Wand/staff com + spells", "Wand/staff with + spells"), phase="1–59", cost=L("Barato", "Cheap"), impact=L("Dano do leveling", "Leveling damage")),
 dict(p=2, item="Blood of the Warrior + Beira's Anguish", phase="45+", cost=L("Barato", "Cheap"), impact=L("Recoup e Ignite", "Recoup and Ignite")),
 dict(p=3, item="Sacrosanctum", phase="60+", cost=L("Barato", "Cheap"), impact=L("Liga o recoup", "Enables recoup")),
 dict(p=4, item=L("Dueling Wand boa", "Good Dueling Wand"), phase="65+", cost=L("Valor", "Value"), impact="Spellslinger"),
 dict(p=5, item=L("Staff 6 stats + Perfect Essence of Sorcery", "6-stat staff + Perfect Essence of Sorcery"), phase="65+", cost=L("Barato", "Cheap"), impact=L("+5 níveis de spell", "+5 spell levels")),
 dict(p=6, item="Coward's Legacy + Snakepit", phase="85+", cost=L("Barato", "Cheap"), impact="Low Life"),
 dict(p=7, item="Mageblood", phase="92+", cost=L("Luxo", "Luxury"), impact=L("Setup CoA", "CoA setup")),
]

TRICKS = [
 {"cat": L("Infusões", "Infusions"), "lvl": L("Médio", "Medium"), "title": L("Não gaste infusões antes do boss", "Don't waste infusions before the boss"), "body": L("Frost Bomb e Orb of Storms antes do boss nascer; depois não lance mais nada até ele aparecer — qualquer spell consumiria as infusões.", "Frost Bomb and Orb of Storms before the boss spawns; then cast nothing else until it appears — any spell would consume the infusions.")},
 {"cat": L("Infusões", "Infusions"), "lvl": L("Fácil", "Easy"), "title": L("Spark atravessando o muro", "Spark through the wall"), "body": L("Projéteis que passam pela Flame Wall ganham fogo; com Lightning Infusion, raio também. Com Fortress II o muro vira círculo: fique no centro.", "Projectiles passing through Flame Wall gain fire; with a Lightning Infusion, lightning too. With Fortress II the wall becomes a circle: stand in the centre.")},
 {"cat": L("Infusões", "Infusions"), "lvl": L("Fácil", "Easy"), "title": L("Cold Infusion = 2x Spark", "Cold Infusion = 2x Spark"), "body": L("Spark consumindo Cold Infusion solta faíscas em círculo — mais que o dobro do dano em várias arenas de boss.", "Spark consuming a Cold Infusion fires sparks in a circle — more than double damage in many boss arenas.")},
 {"cat": "Mana Tempest", "lvl": L("Médio", "Medium"), "title": L("Ative e saia", "Trigger and step out"), "body": L("O Arcane Surge só ativa quando 100% da mana é gasta por uma skill — o Mana Tempest faz isso. Entre, ative o Arcane Surge e saia; recrie para renovar o empower.", "Arcane Surge only triggers when 100% of your mana is spent by one skill — Mana Tempest does that. Enter, trigger Arcane Surge and step out; recast to refresh the empower.")},
 {"cat": "Cast on Critical", "lvl": L("Médio", "Medium"), "title": L("Dano crítico > chance", "Crit damage > chance"), "body": L("A energia do Cast on Critical depende do dano do crítico. 80% de chance sem bônus é pior que 50% com muito dano crítico. Enfraqueça o boss (curse/Exposure) para ganhar mais energia.", "Cast on Critical energy depends on crit damage. 80% chance with no bonus is worse than 50% with lots of crit damage. Weaken the boss (curse/Exposure) to gain more energy.")},
 {"cat": "Recoup", "lvl": L("Avançado", "Advanced"), "title": L("Mana é ruim", "Mana is bad"), "body": L("Com Pyromantic Pact, quanto menor a mana e maior o custo, mais rápido a chama enche e mais vezes o recoup cura. Evite mana e eficiência de custo; suba cast speed e níveis de gem.", "With Pyromantic Pact, the lower your mana and the higher your costs, the faster the flame fills and the more often recoup heals. Avoid mana and cost efficiency; raise cast speed and gem levels.")},
 {"cat": "Recoup", "lvl": L("Avançado", "Advanced"), "title": L("Line of Olroth", "Line of Olroth"), "body": L("A timeless jewel 'line of Olroth' converte um keystone e desliga a mana vinda de Inteligência: a Infernal Flame cai pela metade e o recoup acontece 2x mais.", "The 'line of Olroth' timeless jewel converts a keystone and disables Intelligence mana: Infernal Flame halves and recoup happens twice as often.")},
 {"cat": L("Mapas", "Maps"), "lvl": L("Fácil", "Easy"), "title": L("Mods perigosos", "Dangerous mods"), "body": L("Mapas com recuperação reduzida desligam o recoup: você se mata. Monstros Amanamu do Abyss também bloqueiam recuperação — o Culling Strike do setup final resolve.", "Maps with reduced recovery switch off recoup: you kill yourself. Amanamu Abyss monsters also block recovery — the final setup's Culling Strike handles them.")},
 {"cat": L("Economia", "Economy"), "lvl": L("Fácil", "Easy"), "title": L("Regex de vendor", "Vendor regex"), "body": "\"mov|rare|st spe|ll d|extr|ed light|^\\+.*ills$\""},
 {"cat": L("Economia", "Economy"), "lvl": L("Fácil", "Easy"), "title": L("Regex de mapas", "Map regex"), "body": "\"!% ma|% mon|less r|s coo|ed ai|ed el|trates\""},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Quests (Ignatius)", "Quests (Ignatius)"), "body": L("A2 Charm Duration, A3 Ailment Threshold, A4 resistências e Life Recovery from Flasks, 30% Armour/Evasion/ES (Shark Fin). NÃO pegue a mana do Eye of Hinekora.", "A2 Charm Duration, A3 Ailment Threshold, A4 resistances and Life Recovery from Flasks, 30% Armour/Evasion/ES (Shark Fin). DON'T take the Eye of Hinekora mana.")},
]

TROUBLESHOOT = [
 (L("Dano baixo no boss", "Low boss damage"), L("As infusões foram gastas antes? Frost Bomb em cima do boss para Exposure, Spark através da Flame Wall e Cold Infusion antes de cada Spark forte.", "Were infusions spent early? Frost Bomb on the boss for Exposure, Spark through Flame Wall and a Cold Infusion before each big Spark.")),
 (L("Cast on Critical quase não dispara", "Cast on Critical barely triggers"), L("Falta dano crítico (não só chance). Suba níveis de gem, dano crítico e enfraqueça o alvo com Elemental Weakness e Exposure.", "Missing crit damage (not just chance). Raise gem levels and crit damage and weaken the target with Elemental Weakness and Exposure.")),
 (L("Demon Form me mata", "Demon Form kills me"), L("O recoup não está segurando. Volte a spammar Spark até estabilizar e só então reative. Confira o Sacrosanctum e o recoup total.", "Recoup isn't holding. Go back to spamming Spark until stable and only then reactivate. Check Sacrosanctum and total recoup.")),
 (L("Morro ao encher a Infernal Flame", "I die when Infernal Flame fills"), L("Você toma vida+ES máximos como fogo: precisa de resistência máxima a fogo alta e recoup. Sem isso, não use Pyromantic Pact.", "You take max life+ES as fire: you need high max fire resistance and recoup. Without them, don't use Pyromantic Pact.")),
 (L("Time of Need com Compressed Duration não funciona", "Time of Need with Compressed Duration doesn't work"), L("O intervalo das bênçãos não é mais duração de skill: tire o support.", "The blessing interval is no longer skill duration: remove the support.")),
 (L("Dueling Wand antes do 65", "Dueling Wand before 65"), L("O Spellslinger vem da Dueling Wand (nível 65). Antes disso, siga as outras skills da fase.", "Spellslinger comes from the Dueling Wand (level 65). Before that, follow the phase's other skills.")),
]

ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Cast on Critical + Comet · resists no cap", "Cast on Critical + Comet · resists capped"), gear=L("Staff/Dueling Wand · Sacrosanctum", "Staff/Dueling Wand · Sacrosanctum")),
 dict(stage="T1–T9", goal=L("Sigil of Power · gems 19+", "Sigil of Power · 19+ gems"), gear="Blood of the Warrior"),
 dict(stage="T10–T15", goal=L("Recoup 100% · Demon Form infinito", "100% recoup · infinite Demon Form"), gear=L("Cinto com recoup", "Recoup belt")),
 dict(stage="Pinnacle", goal=L("Low Life + 2 Comets ou CoA", "Low Life + 2 Comets or CoA"), gear="Coward's Legacy · Snakepit · Mageblood"),
]

CRAFT = [
 L("Staff barato do Ignatius: compre um de 6 stats (dano como extra, spell damage, cast speed, raio) por 1–2 Exalted e aplique Perfect Essence of Sorcery (+5 spells) — sem jogar fora o cast speed.", "Ignatius's cheap staff: buy a 6-stat one (damage as extra, spell damage, cast speed, lightning) for 1–2 Exalted and apply Perfect Essence of Sorcery (+5 spells) — without losing cast speed."),
 L("Cinto: Perfect Essence of Insulation para o recoup como fogo.", "Belt: Perfect Essence of Insulation for recoup as fire."),
 L("Amuleto: recoup como vida, crítico e % ES; nada de mana.", "Amulet: recoup as life, crit and % ES; no mana."),
]

T("skill", "Cast on Critical", 43, L("100 Spirit · gem tier 14", "100 Spirit · tier 14 gem"), L("Monte nos Interlúdios, ligue quando couber.", "Set it up in the Interludes, turn on when it fits."), L("Comets automáticos nos críticos.", "Automatic Comets on crits."), L("Sem Spirit fica só montado.", "Without Spirit it just stays set up."), "—")
T("item", "Dueling Wand", 65, L("Nível 65 (base)", "Level 65 (base)"), L("Mapas.", "Maps."), L("Concede Spellslinger.", "Grants Spellslinger."), L("Espere uma boa.", "Wait for a good one."), L("Staff + Perfect Essence of Sorcery.", "Staff + Perfect Essence of Sorcery."))
T("item", "Sacrosanctum", 1, L("Confira o nível no item", "Check the level on the item"), L("Antes do recoup.", "Before recoup."), L("Recoup em vida e ES.", "Recoup to life and ES."), "—", "—")
T("asc", "Pyromantic Pact", 73, L("Ascendência Infernalist", "Infernalist ascendancy"), L("Com 100% de recoup.", "With 100% recoup."), L("Mana infinita; auto-dano vira cura.", "Infinite mana; self-damage becomes healing."), L("Sem recoup te mata.", "Without recoup it kills you."), "—")
T("item", "Coward's Legacy", 1, L("Confira o nível no item", "Check the level on the item"), L("Versão Low Life (85+).", "Low Life version (85+)."), L("Low Life com 75% da vida.", "Low Life at 75% life."), "—", "—")
T("item", "Mageblood", 1, L("Confira o nível no item", "Check the level on the item"), L("Setup CoA (92+).", "CoA setup (92+)."), L("Legacy of Ruby para resistência máxima a fogo.", "Legacy of Ruby for max fire resistance."), "—", "—")

CASES = [
 (L("Sou novo em infusões", "I'm new to infusions"), L("O próprio Ignatius recomenda: suba com um build de Essence Drain/Contagion e troque para esta build nos mapas (fase 'Mapas T1–T9').", "Ignatius himself recommends: level with an Essence Drain/Contagion build and swap to this build in maps ('Maps T1–T9' phase).")),
 (L("Não tenho recoup suficiente", "I don't have enough recoup"), L("Fique no setup 'Mapas T1–T9' (Mana Remnants, sem Pyromantic Pact) até ter 100%.", "Stay on the 'Maps T1–T9' setup (Mana Remnants, no Pyromantic Pact) until you reach 100%.")),
 (L("Quero o CoA mas não tenho Mageblood", "I want CoA but have no Mageblood"), L("Não troque: sem Legacy of Ruby a resistência máxima a fogo não aguenta o próprio dano. Fique no Low Life.", "Don't swap: without Legacy of Ruby your max fire resistance can't survive the self-damage. Stay on Low Life.")),
]

SOURCES = [
 dict(name="Ignatius — [0.5.5] Comprehensive CoC Frostbolt/Spark Comet Recoup Infernalist (Mobalytics)", use=L("Leveling a endgame: 10 variantes, rotações, notas e crafts", "Leveling to endgame: 10 variants, rotations, notes and crafts"), url=GUIDE_URL),
 dict(name="kingkongor — [0.5.5] Infernalist Auto Spark CoA Comet (Mobalytics)", use=L("Setup de luxo (Cast on Elemental Ailment)", "Luxury setup (Cast on Elemental Ailment)"), url=COA_URL),
 dict(name="poe.ninja — Infernalist (Forbidden Rites)", use=L("Meta: Comet e Spark lideram; preços", "Meta: Comet and Spark lead; prices"), url="https://poe.ninja/poe2/builds/forbiddenrites?class=Infernalist"),
 dict(name="Path of Building (PoE2) — Gems.lua, Skills", use=L("Descrições, custos de Spirit e tiers", "Descriptions, Spirit costs and tiers"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
]
FIXES = [
 L("As árvores de ascendência de algumas variantes do guia tinham mais pontos do que os Trials dão naquele nível; o app mostra só o que dá para alocar em cada fase (2 pontos por Trial).", "Some guide variants had more ascendancy points than the Trials grant at that level; the app only shows what you can allocate in each phase (2 points per Trial)."),
 L("A variante 'Ward-Stacking' do Ignatius e a 'Final Form (Spark)' não entram na rota; a fase de luxo usa a variante 'Cheaper' do kingkongor, que é o que o topo do ladder joga.", "Ignatius's 'Ward-Stacking' and 'Final Form (Spark)' variants aren't in the route; the luxury phase uses kingkongor's 'Cheaper' variant, which is what the top of the ladder plays."),
 L("Comentários do guia apontam que a build é difícil no começo dos mapas: por isso o app segura a troca para o recoup até ter 100% de recoup e gems altas.", "Guide comments point out the build is hard in early maps: that's why the app holds the recoup swap until you have 100% recoup and high gems."),
 L("Custos de Spirit conferidos no Path of Building: Cast on Critical, Cast on Elemental Ailment e Cast on Dodge 100; Blink 60; Siphon Elements, Mana Remnants, Time of Need, Charge Regulation, Combat Frenzy, Explosive Transmutation e Remnants of Kalguur 30.", "Spirit costs checked in Path of Building: Cast on Critical, Cast on Elemental Ailment and Cast on Dodge 100; Blink 60; Siphon Elements, Mana Remnants, Time of Need, Charge Regulation, Combat Frenzy, Explosive Transmutation and Remnants of Kalguur 30."),
]

UI = dict(
 setNote=L("rares com dano de spell, crítico e vida/ES.", "rares with spell damage, crit and life/ES."),
 carry=r"^(Spark|Cast on Critical|Cast on Elemental Ailment|Frostbolt)$", box=L("INFUSÕES", "INFUSIONS"), spiritWhat=L("(metas e buffs)", "(metas and buffs)"),
 mechBtn=L("Abrir Infusões & Chama", "Open Infusions & Flame"), dmg2="Comet", dmgBar=L("Dano seu / dos Comets automáticos (aprox.)", "Your damage / automatic Comets (approx.)"),
 dmgLegend=L("Comets disparados (proporção aproximada)", "Triggered Comets (approximate ratio)"),
 earlyGone=L("Essence Drain e Contagion já saíram: você passou do nível {u} e o Spark assumiu.", "Essence Drain and Contagion are gone: you're past level {u} and Spark took over."),
 earlyNote=L("Só nos primeiros níveis; o Spark assume no nível ~{u}.", "First levels only; Spark takes over around level {u}."),
 treeIntro=L("Árvore real do patch 0.5.5 com o caminho do guia do Ignatius (e do kingkongor no luxo). Leveling: spell e crítico. Mapas: cast speed e recoup. Endgame: dano crítico e Low Life.", "Real patch 0.5.5 tree with Ignatius's guide path (and kingkongor's for luxury). Leveling: spell and crit. Maps: cast speed and recoup. Endgame: crit damage and Low Life."),
 set1=L("setup principal", "main setup"), set2=L("Chiming Staff (Sigil) / Earthbound", "Chiming Staff (Sigil) / Earthbound"), asc="Infernalist", cls="Witch",
 respecTip=L("Nas trocas (recoup, Low Life, CoA) a ascendência muda: refaça o Trial para respec. Compare com a fase anterior.", "At the swaps (recoup, Low Life, CoA) the ascendancy changes: redo the Trial to respec. Compare with the previous phase."),
 routeIntro=L("Oito fases: Spark com infusões até os Interlúdios, Cast on Critical Comet nos mapas, recoup com Demon Form, Low Life e o CoA de luxo.", "Eight phases: Spark with infusions until the Interludes, Cast on Critical Comet in maps, recoup with Demon Form, Low Life and luxury CoA."),
 socketPrio=["Spark", "Cast on Critical (Comet)", "Frost Bomb · Orb of Storms", "Flame Wall · Spellslinger", "Elemental Weakness"],
 permIntro=L("Nada disso volta depois. Spirit paga Mana Remnants e Siphon Elements no leveling e as meta skills de 100 (Cast on Critical/Ailment/Dodge) no endgame. NÃO pegue a mana do Eye of Hinekora.", "None of this comes back later. Spirit pays for Mana Remnants and Siphon Elements while leveling and the 100-Spirit meta skills (Cast on Critical/Ailment/Dodge) in endgame. DON'T take the Eye of Hinekora mana."),
 atlasCards=[[L("Mapas proibidos", "Forbidden maps"), L("Recuperação reduzida e resistência reduzida matam a build (auto-dano). Regex: \"!% ma|% mon|less r|s coo|ed ai|ed el|trates\".", "Reduced recovery and reduced resistance kill the build (self-damage). Regex: \"!% ma|% mon|less r|s coo|ed ai|ed el|trates\".")],
             [L("Juiced", "Juiced"), L("O setup CoA do kingkongor faz 200% Delirium e Expedition juiced; para mobs que refletem freeze, um segundo capacete com anoint.", "kingkongor's CoA setup runs 200% Delirium and juiced Expedition; for freeze-reflecting mobs, a second anointed helmet.")]],
 foot=L("Guia baseado nos builds do Ignatius e do kingkongor (Mobalytics), dados de jogo do Path of Building e preços do poe.ninja", "Guide based on Ignatius's and kingkongor's builds (Mobalytics), Path of Building game data and poe.ninja prices"),
)

CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens, Árvore e Infusões & Chama se adaptam na hora. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items, Tree and Infusions & Flame tabs adapt instantly. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit máximo", "Max Spirit"), L("ex.: 160", "e.g. 160")], ["recoup", L("Recoup total (%)", "Total recoup (%)"), L("ex.: 100", "e.g. 100")], ["life", L("Vida máxima", "Max life"), ""]],
 tiles=[[L("Spirit reservado", "Spirit reserved"), "used"], [L("Spirit livre", "Spirit free"), "free"], [L("Recoup (%)", "Recoup (%)"), "recoup"]],
 buffs=[dict(key="coc", name="Cast on Critical", cost=100), dict(key="siphon", name="Siphon Elements", cost=30), dict(key="remnants", name="Mana Remnants", cost=30), dict(key="blink", name="Blink", cost=60), dict(key="coa", name="Cast on Elemental Ailment", cost=100), dict(key="cod", name="Cast on Dodge", cost=100)],
 own=[
  ["gear", "Sacrosanctum", "Sacrosanctum"], ["gear", "Blood of the Warrior", "Blood of the Warrior"], ["gear", "dueling", L("Dueling Wand", "Dueling Wand")], ["gear", "chiming", L("Chiming Staff (Set 2)", "Chiming Staff (Set 2)")],
  ["gear", "Coward's Legacy", "Coward's Legacy"], ["gear", "Snakepit", "Snakepit"], ["gear", "Earthbound", "Earthbound"], ["gear", "Mageblood", "Mageblood"], ["gear", "Alpha's Howl", "Alpha's Howl"],
  ["gem", "coc", "Cast on Critical (100)"], ["gem", "siphon", "Siphon Elements (30)"], ["gem", "remnants", "Mana Remnants (30)"], ["gem", "blink", "Blink (60)"], ["gem", "coa", "Cast on Elemental Ailment (100)"], ["gem", "cod", "Cast on Dodge (100)"], ["gem", "comet", "Comet"], ["gem", "tempest", "Mana Tempest"],
  ["tree", "olroth", L("Timeless jewel (line of Olroth)", "Timeless jewel (line of Olroth)")],
  ["asc", "possession", "Demonic Possession"], ["asc", "bringer", "Bringer of Flame"], ["asc", "hellhound", "Loyal Hellhound"], ["asc", "pact", "Pyromantic Pact"], ["asc", "darkness", "Mastered Darkness"], ["asc", "immolation", "Grinning Immolation"], ["asc", "altered", "Altered Flesh"], ["asc", "beidat", "Beidat's Will"],
 ],
 rules=[
  dict(when=dict(own=["pact"], numLt=["recoup", 100]), lvl="bad", t=L("Pyromantic Pact sem 100% de recoup", "Pyromantic Pact without 100% recoup"), d=L("Quando a chama enche você toma vida+ES máximos como fogo. Volte ao setup dos mapas até ter 100%.", "When the flame fills you take max life+ES as fire. Go back to the maps setup until you reach 100%."), tab="mech"),
  dict(when=dict(own=["pact"], notOwn=["Sacrosanctum"]), lvl="bad", t=L("Pyromantic Pact sem Sacrosanctum", "Pyromantic Pact without Sacrosanctum"), d=L("O recoup do Sacrosanctum é a base da troca.", "Sacrosanctum's recoup is the base of the swap."), tab="gear"),
  dict(when=dict(own=["remnants", "pact"]), lvl="tip", t=L("Mana Remnants com Pyromantic Pact", "Mana Remnants with Pyromantic Pact"), d=L("Sem mana, os 30 Spirit rendem mais em outra coisa.", "With no mana, those 30 Spirit are better spent elsewhere."), tab="skills"),
  dict(when=dict(own=["darkness"], notOwn=["pact"]), lvl="warn", t=L("Mastered Darkness sem recoup", "Mastered Darkness without recoup"), d=L("Demonflame sem limite só funciona com o recoup segurando a vida.", "Uncapped Demonflame only works with recoup holding your life."), tab="asc"),
  dict(when=dict(own=["coa"], notOwn=["Mageblood"]), lvl="warn", t=L("CoA sem Mageblood", "CoA without Mageblood"), d=L("O setup do kingkongor depende do Legacy of Ruby para aguentar o auto-dano.", "kingkongor's setup relies on Legacy of Ruby to survive self-damage."), tab="gear"),
  dict(when=dict(lvMin=45, notOwn=["coc", "coa"]), lvl="tip", t=L("Monte o Cast on Critical", "Set up Cast on Critical"), d=L("Pode deixar montado com Comet mesmo sem Spirit para ligar.", "You can keep it set up with Comet even without the Spirit to turn it on."), tab="skills"),
  dict(when=dict(lvMin=66, notOwn=["dueling"]), lvl="tip", t=L("Dueling Wand", "Dueling Wand"), d=L("Spellslinger com Flame Wall + Spark. Espere uma boa ou use staff + Perfect Essence of Sorcery.", "Spellslinger with Flame Wall + Spark. Wait for a good one or use a staff + Perfect Essence of Sorcery."), tab="gear"),
  dict(when=dict(own=["immolation"], notOwn=["Coward's Legacy"]), lvl="tip", t="Low Life", d=L("A versão cara usa Coward's Legacy para Low Life permanente (Execute III).", "The expensive version uses Coward's Legacy for permanent Low Life (Execute III)."), tab="gear"),
  dict(when=dict(lvMin=28, notOwn=["possession"]), lvl="warn", t=L("1ª ascendência pendente", "1st ascendancy pending"), d="Demonic Possession.", tab="asc"),
  dict(when=dict(lvMin=18, lvMax=45, notOwn=["tempest"]), lvl="tip", t="Mana Tempest", d=L("Com Arcane Surge: entre, ative e saia.", "With Arcane Surge: enter, trigger and step out."), tab="mech"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["recoup", "frost", "max"], when=dict(notOwn=["pact"]), gemsFrom="maps", note=L("Sem Pyromantic Pact: mostrando o setup dos mapas T1–T9.", "No Pyromantic Pact: showing the T1–T9 maps setup.")),
 dict(pids=["max"], when=dict(own=["pact"], notOwn=["Mageblood"]), gemsFrom="frost", note=L("Sem Mageblood: mostrando o setup Low Life.", "No Mageblood: showing the Low Life setup.")),
]
TREE_RULES = [
 dict(when=dict(own=["pact"], notOwn=["olroth"], lvMin=80), t=L("Uma timeless jewel 'line of Olroth' dobra a frequência do recoup (desliga a mana da Inteligência).", "A 'line of Olroth' timeless jewel doubles recoup frequency (disables Intelligence mana)."), node=None),
]
TIMING_KEY = {"Cast on Critical": "coc", "Dueling Wand": "dueling", "Sacrosanctum": "Sacrosanctum", "Pyromantic Pact": "pact", "Coward's Legacy": "Coward's Legacy", "Mageblood": "Mageblood"}

MECH = dict(
 title=L("Infusões & Chama", "Infusions & Flame"),
 intro=L("Como a Infernalist funciona: infusões que dobram o Spark, meta skills que lançam Comets sozinhas e o Pyromantic Pact que transforma o próprio dano em cura.", "How the Infernalist works: infusions that double Spark, meta skills that cast Comets on their own and Pyromantic Pact turning self-damage into healing."),
 sections=[
  dict(type="table", h=L("Infusões: quem cria, quem consome", "Infusions: who creates, who consumes"), cols=[L("Infusão", "Infusion"), L("Criada por", "Created by"), L("Consumida por", "Consumed by"), L("Efeito", "Effect")], rows=[
   ["Cold", "Frost Bomb", "Spark", L("Faíscas em círculo (2x+ dano)", "Sparks in a circle (2x+ damage)")],
   ["Lightning", "Orb of Storms · Lightning Warp", "Flame Wall · Frost Wall · Arc", L("Muro com raio / explosão extra", "Wall with lightning / extra explosion")],
   ["Fire", "Living Bomb", "Comet · Ball Lightning", L("Comet de gelo e fogo / chão em chamas", "Ice-and-fire Comet / burning ground")],
   ["Verisium", "Powered by Verisium · Runic Extraction", L("Qualquer skill", "Any skill"), L("Coringa: vale como qualquer infusão", "Wildcard: counts as any infusion")],
  ]),
  dict(type="rotation", blocks=[
   [L("Boss (campanha)", "Boss (campaign)"), [L("Antes de nascer: Frost Bomb + Orb of Storms", "Before it spawns: Frost Bomb + Orb of Storms"), L("Não lance mais nada", "Cast nothing else"), L("Flame Wall na frente dele", "Flame Wall in front of it"), L("Spark através do muro", "Spark through the wall"), L("Frost Bomb nele → Spark → Orb → Flame Wall", "Frost Bomb on it → Spark → Orb → Flame Wall")]],
   [L("Boss (mapas)", "Boss (maps)"), [L("Sigil of Power (fique dentro)", "Sigil of Power (stay inside)"), L("Frost Bomb → Orb of Storms", "Frost Bomb → Orb of Storms"), L("Flame Wall com Fortress II", "Flame Wall with Fortress II"), L("Spark: críticos disparam Comets", "Spark: crits trigger Comets")]],
  ]),
  dict(type="cards", cards=[
   [L("Cast on Critical", "Cast on Critical"), L("Ganha energia a cada crítico — proporcional ao dano do crítico — e lança o Comet socketado ao encher. Pinpoint Critical e Boundless Energy aceleram; curses e Exposure aumentam o dano e, por tabela, a energia.", "Gains energy on each crit — proportional to crit damage — and casts the socketed Comet when full. Pinpoint Critical and Boundless Energy speed it up; curses and Exposure raise damage and therefore energy.")],
   [L("Pyromantic Pact", "Pyromantic Pact"), L("Sua mana vira Infernal Flame em dobro e gastar ENCHE a barra. Cheia: você toma vida e ES máximos como fogo e a barra zera. Com recoup alto (Sacrosanctum, amuleto, cinto, Blood of the Warrior) esse dano volta como cura — e quanto mais vezes enche, mais você cura.", "Your mana becomes twice as much Infernal Flame and spending FILLS the bar. Full: you take max life and ES as fire and it resets. With high recoup (Sacrosanctum, amulet, belt, Blood of the Warrior) that damage comes back as healing — and the more often it fills, the more you heal.")],
   [L("Demon Form", "Demon Form"), L("Spells muito mais fortes, mas Demonflame acumula e drena vida cada vez mais rápido. Mastered Darkness tira o limite: com recoup segurando, o dano cresce o mapa inteiro. Volta à forma humana com 1 de vida ou ao usar skill que não é spell.", "Much stronger spells, but Demonflame stacks and drains life faster and faster. Mastered Darkness removes the cap: with recoup holding, damage grows the whole map. You revert at 1 life or when using a non-spell skill.")],
   [L("Mana Tempest + Arcane Surge", "Mana Tempest + Arcane Surge"), L("A tempestade empodera spells que custam mana e drena sua mana inteira — o que ativa o Arcane Surge (15 s). Ative e saia; recrie para renovar.", "The storm empowers mana-costing spells and drains all your mana — which triggers Arcane Surge (15 s). Trigger it and step out; recast to refresh.")],
  ]),
  dict(type="spirit", h=L("Spirit das metas e buffs", "Meta and buff Spirit"), p=L("Marque o que você usa. Custos do Path of Building.", "Tick what you use. Costs from Path of Building."),
       note=L("Hellhound e Purity of Fire não têm custo nos dados: confira no jogo.", "Hellhound and Purity of Fire have no cost in the data: check in game.")),
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
            q["reward"] = L('+1 Charm Slot · ESCOLHA: 30% increased Charm Effect Duration (Ignatius)', '+1 Charm Slot · CHOICE: 30% increased Charm Effect Duration (Ignatius)'); q["prio"] = 'Alta'
        if q["boss"] == 'Venom Draught':
            q["reward"] = L('ESCOLHA: 30% increased Elemental Ailment Threshold (Ignatius)', 'CHOICE: 30% increased Elemental Ailment Threshold (Ignatius)'); q["prio"] = 'Média'
        if q["boss"] == "Navali's Rest":
            q["reward"] = L('NÃO pegue a mana (Ignatius): mana atrapalha o endgame', "DON'T take the mana (Ignatius): mana hurts the endgame"); q["prio"] = 'Média'
        if q["boss"] == 'Goddess of Justice':
            q["reward"] = L('ESCOLHA: 30% increased Life Recovery from Flasks (Ignatius)', 'CHOICE: 30% increased Life Recovery from Flasks (Ignatius)'); q["prio"] = 'Média'
        if q["boss"] == 'Great White One':
            q["reward"] = L('ESCOLHA: +30% Armour, Evasion e Energy Shield (Shark Fin, Ignatius)', 'CHOICE: +30% Armour, Evasion and Energy Shield (Shark Fin, Ignatius)'); q["prio"] = 'Alta'
        if q["boss"] == "Tabana's Pillar":
            q["reward"] = L('ESCOLHA: +5% todas as resistências elementais (Ignatius)', 'CHOICE: +5% to all Elemental Resistances (Ignatius)'); q["prio"] = 'CRÍTICA'
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="15/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=GUIDE_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=BOOK.TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None,
                ui=UI, char=CHAR, mech=MECH, adaptSwaps=ADAPT_SWAPS, treeRules=TREE_RULES, timingKey=TIMING_KEY, phaseAct=PHASE_ACT, treeOrder=ORDER + ["uber"], craftKit=CRAFT_KIT)
