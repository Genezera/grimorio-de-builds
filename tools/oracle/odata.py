# -*- coding: utf-8 -*-
"""Oracle Spell Totem (Lowepe, Mobalytics 0.5.5) — dados da build em PT com tradução EN embutida.

Toda string traduzível é escrita como L("pt", "en"): devolve o PT e registra o par em EN_PAIRS.
Fontes: guia do Lowepe (dl/oracle_variants.json, notas das variantes) + dados de jogo do Path of Building
(dl/pob: Gems.lua, skills_*.lua, ModCache.lua) + tree.json 0.5 + preços poe.ninja (dl/eco_*.json).
"""
import json, os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
EN_PAIRS = {}

def L(pt, en):
    EN_PAIRS[pt] = en
    return pt

V = json.load(open(os.path.join(ROOT, "dl/oracle_variants.json"), encoding="utf-8"))
VAR = {v["name"]: v for v in V["variants"]}
GUIDE_URL = "https://mobalytics.gg/poe-2/builds/oracle-spell-totem-lowepe"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "16/09/2026"

# ------------------------------------------------------------------ explicação de cada support (texto do jogo → por que usar)
SUPWHY = {
 "Rapid Casting I": L("Conjura mais rápido. No leveling, deixa o Entangle e o Bonestorm saírem antes.", "Faster casting. While leveling it gets Entangle and Bonestorm out sooner."),
 "Rapid Casting II": L("Versão mais forte do Rapid Casting: Entangle sai mais rápido no endgame.", "Stronger Rapid Casting: Entangle comes out faster in endgame."),
 "Brutality I": L("Só dano físico, mas bem mais forte. Serve no Entangle do Ato 1 porque o cajado dá +níveis de Physical Spells.", "Physical damage only, but much stronger. Fits Act 1 Entangle because the staff gives +levels to Physical Spells."),
 "Burgeon I": L("Skills canalizadas causam mais dano quanto mais tempo você canaliza. Por isso o Volcano e o Bonestorm precisam ficar segurados alguns segundos.", "Channelled skills deal more damage the longer you channel. That's why Volcano and Bonestorm must be held for a few seconds."),
 "Controlled Destruction": L("Mais dano, mas o spell não dá crítico. Bom no começo, antes da ascendência de crítico.", "More damage, but the spell can't crit. Good early, before the crit ascendancy."),
 "Corrosion": L("O Poison do Ravenous Swarm também quebra Armour dos inimigos.", "Ravenous Swarm's Poison also breaks enemy Armour."),
 "Armour Demolisher I": L("Armour Break mais forte: o dano físico (Bonestorm/Entangle) passa mais.", "Stronger Armour Break: physical damage (Bonestorm/Entangle) goes through more."),
 "Zenith I": L("Mais dano enquanto você está acima de 90% da mana máxima.", "More damage while you are above 90% of maximum mana."),
 "Zenith II": L("Mais dano acima de 90% de mana e melhor eficiência de custo de mana. Por isso a build acumula mana e regeneração.", "More damage above 90% mana and better mana cost efficiency. That's why the build stacks mana and regeneration."),
 "Considered Casting": L("Mais dano em troca de cast speed. No Bonestorm (skill de boss) vale a troca.", "More damage at the cost of cast speed. On Bonestorm (boss skill) the trade is worth it."),
 "Living Lightning": L("Cria minions de raio que encadeiam ataques quando o skill causa dano de raio. Dano extra grátis no Thunderstorm e no Orb of Storms.", "Creates lightning minions that chain attacks when the skill deals lightning damage. Free extra damage on Thunderstorm and Orb of Storms."),
 "Accelerated Growth": L("Cria uma flor que cresce e explode: mais dano em área no Entangle.", "Spawns a flower that grows and explodes: more area damage on Entangle."),
 "Branching Fissures I": L("O Entangle cria fissuras secundárias: limpa packs bem maiores.", "Entangle creates secondary fissures: clears much larger packs."),
 "Concentrated Area": L("Área menor, dano maior. No Thrashing Vines para bosses.", "Smaller area, higher damage. On Thrashing Vines for bosses."),
 "Prolonged Duration I": L("Mais duração (Thrashing Vines, Flame Wall, curse).", "Longer duration (Thrashing Vines, Flame Wall, curse)."),
 "Prolonged Duration II": L("Versão mais forte do Prolonged Duration.", "Stronger Prolonged Duration."),
 "Deliberation": L("Você anda mais devagar enquanto usa o skill, mas ele causa mais dano. No Spell Totem só afeta o momento de colocar o totem.", "You move slower while using the skill, but it deals more damage. On Spell Totem it only affects the moment you place the totem."),
 "Urgent Totems III": L("Coloca os totems muito mais rápido e eles ganham attack/cast speed. É o support mais importante do Spell Totem.", "Places totems much faster and they gain attack/cast speed. It's the most important Spell Totem support."),
 "Projectile Acceleration III": L("Projéteis mais rápidos e o aumento de velocidade também vira dano. Combina com o Spark.", "Faster projectiles and speed increases also become damage. Pairs with Spark."),
 "Overabundance I": L("Aumenta o limite de Orb of Storms em troca de duração.", "Raises Orb of Storms' limit at the cost of duration."),
 "Potent Exposure": L("A Exposure do Frost Bomb fica mais forte: os inimigos perdem mais resistência elemental.", "Frost Bomb's Exposure gets stronger: enemies lose more elemental resistance."),
 "Magnified Area I": L("Área maior (Frost Bomb, Grim Pillars).", "Larger area (Frost Bomb, Grim Pillars)."),
 "Magnified Area II": L("Área ainda maior: mais clear speed com Grim Pillars.", "Even larger area: more clear speed with Grim Pillars."),
 "Efficiency I": L("Custa menos mana. Não funciona em skills que reservam Spirit.", "Costs less mana. Doesn't work on skills that reserve Spirit."),
 "Efficiency II": L("Versão mais forte do Efficiency: o Mana Tempest drena menos.", "Stronger Efficiency: Mana Tempest drains less."),
 "Harmonic Remnants II": L("Os Remnants de mana podem ser coletados de mais longe e às vezes criam um Remnant extra.", "Mana Remnants can be collected from further away and sometimes create an extra Remnant."),
 "Remnant Potency II": L("Remnants mais fortes (mais mana), com um pequeno atraso no efeito.", "Stronger Remnants (more mana), with a small delay on the effect."),
 "Remnant Potency III": L("Versão mais forte do Remnant Potency.", "Stronger Remnant Potency."),
 "Advancing Storm": L("O Mana Tempest aparece em você e anda até o alvo: não precisa ficar parado dentro dele.", "Mana Tempest appears on you and moves towards the target: you don't need to stand still inside it."),
 "Lightning Mastery": L("+1 nível em skills de raio. No Archmage, aumenta o dano de raio extra baseado na mana.", "+1 level to lightning skills. On Archmage it raises the extra mana-based lightning damage."),
 "Clarity II": L("Mais regeneração de mana enquanto a skill persistente está ativa. Mantém a mana acima de 90% para o Zenith.", "More mana regeneration while the persistent skill is active. Keeps mana above 90% for Zenith."),
 "Her Declaration": L("Inimigos que entram na sua Presence ficam Intimidated (recebem mais dano). Custa Spirit extra.", "Enemies entering your Presence become Intimidated (take more damage). Costs extra Spirit."),
 "Unleash": L("O próximo spell repetível é repetido várias vezes. No Entangle e no Orb of Storms, mais cobertura de uma vez.", "The next repeatable spell repeats several times. On Entangle and Orb of Storms, more coverage at once."),
 "Elemental Discharge": L("Consome ailments elementais nos inimigos para disparar uma descarga elemental: o Entangle vira fonte de dano extra.", "Consumes elemental ailments on enemies to trigger an Elemental Discharge: Entangle becomes extra damage."),
 "Biting Frost II": L("Mais dano em inimigos Frozen, mas consome o Freeze (deixa Chilled).", "More damage against Frozen enemies, but consumes the Freeze (leaves them Chilled)."),
 "Cold Mastery": L("+1 nível em skills de frio: Grim Pillars e Bitter Dead ficam mais fortes.", "+1 level to cold skills: Grim Pillars and Bitter Dead get stronger."),
 "Rakiata's Flow": L("Os hits tratam as resistências elementais do inimigo como invertidas: resistência positiva vira negativa. Support de luxo do endgame final.", "Hits treat enemy elemental resistances as inverted: positive resistance becomes negative. Luxury support of the final endgame."),
 "Pierce II": L("Projéteis perfuram um inimigo. Opção do Lowepe no Spark — mas então NÃO pegue Branching Bolts.", "Projectiles pierce an enemy. Lowepe's option on Spark — but then do NOT take Branching Bolts."),
 "Spark": L("Gem de SKILL (não é support) socketada no Spell Totem: é o spell que o totem lança.", "SKILL gem (not a support) socketed in Spell Totem: it's the spell the totem casts."),
 "Grim Pillars": L("Gem de SKILL socketada no Spell Totem: pilares de gelo que explodem. Gasta Runic Ward, não mana.", "SKILL gem socketed in Spell Totem: ice pillars that explode. Spends Runic Ward, not mana."),
 "Bitter Dead": L("Gem de SKILL socketada no Spell Totem junto com Grim Pillars: transforma corpos em núcleos que dão Chill e explodem. Gasta Runic Ward.", "SKILL gem socketed in Spell Totem together with Grim Pillars: turns corpses into cores that Chill and explode. Spends Runic Ward."),
}

# ------------------------------------------------------------------ gems
def G(skill, sup, role, why, sp=None, pr=0, cost=None, until=None):
    g = {"skill": skill, "set": "—", "sup": sup, "role": role, "why": why}
    if sp: g.update(sp=sp, pr=pr, cost=cost or L("Sem Spirit", "No Spirit"))
    if until: g["until"] = until
    return g

FREE = L("Sem Spirit", "No Spirit")
TOTEM_COST = L("75 Spirit por totem (Ancestral Bond)", "75 Spirit per totem (Ancestral Bond)")

PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 14], tag=L("Volcano → Entangle + Bonestorm", "Volcano → Entangle + Bonestorm"),
  carry=L("Você: Entangle (clear) + Volcano/Bonestorm (boss)", "You: Entangle (clear) + Volcano/Bonestorm (boss)"), dmgSplit=[100, 0],
  goal=L("Druid de spells físicos com cajado: Volcano é o skill inicial, Entangle limpa os packs e o Bonestorm substitui Volcano e Frost Bomb antes do boss do Ato 1.", "Physical-spell Druid with a staff: Volcano is the starting skill, Entangle clears packs and Bonestorm replaces Volcano and Frost Bomb before the Act 1 boss."),
  rotation=[L("Entangle no pack (clear)", "Entangle on the pack (clear)"), L("Volcano: SEGURE alguns segundos (é canalizado)", "Volcano: HOLD it a few seconds (it's channelled)"), L("Frost Bomb (pode ficar nível 1) para Exposure", "Frost Bomb (can stay level 1) for Exposure"), L("Antes do boss do Ato 1: troque Volcano/Frost Bomb pelo Bonestorm", "Before the Act 1 boss: swap Volcano/Frost Bomb for Bonestorm")],
  gems=[
   G("Entangle", ["Rapid Casting I", "Brutality I"], L("Clear", "Clear"), L("O skill de limpar packs da build inteira até a troca para totem: uma fissura que anda e prende os inimigos com vinhas.", "The pack-clearing skill all the way to the totem swap: a moving fissure that binds enemies with vines."), "free"),
   G("Volcano", ["Burgeon I", "Controlled Destruction"], L("Single target (início)", "Single target (start)"), L("Skill inicial. É canalizado: segure alguns segundos, senão o dano é baixo. Sai antes do boss do Ato 1.", "Starting skill. It's channelled: hold it a few seconds or damage is low. Leaves before the Act 1 boss."), "free", until=12),
   G("Frost Bomb", [], L("Exposure", "Exposure"), L("Aplica Elemental Exposure (menos resistência). Pode ficar no nível 1.", "Applies Elemental Exposure (less resistance). It can stay at level 1."), "free", until=12),
   G("Ravenous Swarm", ["Corrosion"], L("Dano passivo", "Passive damage"), L("Insetos que perseguem e envenenam enquanto está ativo. Reserva 30 Spirit.", "Insects that chase and poison while active. Reserves 30 Spirit."), "core", 1, L("30 Spirit", "30 Spirit")),
   G("Bonestorm", ["Burgeon I", "Rapid Casting I"], L("Boss", "Boss"), L("Canalize para juntar espinhos de osso e solte: substitui Volcano e Frost Bomb antes do boss do Ato 1.", "Channel to gather bone spikes and release: replaces Volcano and Frost Bomb before the Act 1 boss."), "free"),
  ],
  cheap=[L("Cajado com +níveis de Physical Spells e % Spell Damage", "Staff with +levels to Physical Spells and % Spell Damage"), L("Botas com 10–15% de Movement Speed", "Boots with 10–15% Movement Speed")],
  full=[L("Mesmo do barato: nada caro faz diferença no Ato 1", "Same as budget: nothing expensive matters in Act 1")],
  stats=[L("+Physical ou All Spell Skills", "+Physical or All Spell Skills"), L("% Spell/Physical Damage", "% Spell/Physical Damage"), L("Vida", "Life"), L("Resistência a frio (boss do Ato 1)", "Cold resistance (Act 1 boss)")],
  tree=L("Nós de spell e área perto do início da Druid.", "Spell and area nodes near the Druid start."),
  avoid=[L("Soltar o Volcano cedo demais (ele precisa ser canalizado)", "Releasing Volcano too early (it needs to be channelled)"), L("Gastar gold à toa: a troca para totem no Ato 4 custa caro", "Wasting gold: the totem swap in Act 4 is expensive")],
  exit=[L("Bonestorm no lugar do Volcano", "Bonestorm replacing Volcano"), L("King in the Mists (+30 Spirit)", "King in the Mists (+30 Spirit)")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[15, 27], tag=L("Wildsurge: Storm + Plant", "Wildsurge: Storm + Plant"),
  carry=L("Você: Bonestorm + Thunderstorm + Entangle", "You: Bonestorm + Thunderstorm + Entangle"), dmgSplit=[100, 0],
  goal=L("Pegue o keystone Wildsurge Incantation (Storm e Plant spells: 50% more dano, 50% less custo, 75% less duração). Thunderstorm dá Shock e, segundo o Lowepe, aumenta a duração do Entangle.", "Take the Wildsurge Incantation keystone (Storm and Plant spells: 50% more damage, 50% less cost, 75% less duration). Thunderstorm applies Shock and, per Lowepe, extends Entangle's duration."),
  rotation=[L("Thunderstorm no pack", "Thunderstorm on the pack"), L("Entangle", "Entangle"), L("Bonestorm no boss", "Bonestorm on the boss")],
  gems=[
   G("Bonestorm", ["Burgeon I", "Zenith I"], L("Boss", "Boss"), L("Dano principal em boss. Zenith I: mais dano acima de 90% de mana.", "Main boss damage. Zenith I: more damage above 90% mana."), "free"),
   G("Thunderstorm", ["Rapid Casting I", "Living Lightning"], L("Shock + clear", "Shock + clear"), L("Tempestade que dá Shock/Freeze mais fácil e deixa plantas Overgrown. Living Lightning adiciona minions de raio.", "Storm that makes Shock/Freeze easier and turns plants Overgrown. Living Lightning adds lightning minions."), "free"),
   G("Entangle", ["Accelerated Growth", "Rapid Casting I"], L("Clear", "Clear"), L("Accelerated Growth adiciona uma flor que explode.", "Accelerated Growth adds an exploding flower."), "free"),
   G("Ravenous Swarm", ["Corrosion", "Armour Demolisher I"], L("Dano passivo + Armour Break", "Passive damage + Armour Break"), L("Quebra Armour para o dano físico do Bonestorm.", "Breaks Armour for Bonestorm's physical damage."), "core", 1, L("30 Spirit", "30 Spirit")),
  ],
  cheap=[L("Cajado com +níveis de Physical/All Spell Skills", "Staff with +levels to Physical/All Spell Skills")],
  full=[L("Mesmo do barato. Comece a olhar vendors atrás de sceptre com 130+ Spirit e wand com +níveis de Lightning", "Same as budget. Start checking vendors for a 130+ Spirit sceptre and a wand with +levels to Lightning")],
  stats=[L("+Level Physical/All Spell Skills", "+Level Physical/All Spell Skills"), L("% Spell/Physical Damage", "% Spell/Physical Damage"), L("Vida", "Life"), L("Resistência a raio/fogo (boss do Ato 2)", "Lightning/Fire resistance (Act 2 boss)")],
  tree=L("Wildsurge Incantation e nós de spell.", "Wildsurge Incantation and spell nodes."),
  avoid=[L("Pular o Wildsurge Incantation: é o salto de dano do Ato 2", "Skipping Wildsurge Incantation: it's the Act 2 damage jump")],
  exit=[L("Wildsurge Incantation", "Wildsurge Incantation"), L("Medallion (+1 Charm Slot)", "Medallion (+1 Charm Slot)")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[28, 39], tag=L("Thrashing Vines + crítico", "Thrashing Vines + crit"),
  carry=L("Você: Thunderstorm > Entangle > Thrashing Vines > Bonestorm", "You: Thunderstorm > Entangle > Thrashing Vines > Bonestorm"), dmgSplit=[100, 0],
  goal=L("Thrashing Vines entra para bosses. Ascendência: The Lesser Harm e Forced Outcome (críticos inevitáveis). Guarde gold: a troca para totem precisa de respec.", "Thrashing Vines comes in for bosses. Ascendancy: The Lesser Harm and Forced Outcome (inevitable crits). Save gold: the totem swap needs a respec."),
  rotation=[L("Thunderstorm", "Thunderstorm"), L("Entangle", "Entangle"), L("Thrashing Vines (boss)", "Thrashing Vines (boss)"), L("Bonestorm", "Bonestorm")],
  gems=[
   G("Bonestorm", ["Burgeon I", "Zenith II", "Considered Casting"], L("Boss", "Boss"), L("Considered Casting troca cast speed por dano: boss parado.", "Considered Casting trades cast speed for damage: stationary bosses."), "free"),
   G("Entangle", ["Accelerated Growth", "Rapid Casting I", "Branching Fissures I"], L("Clear", "Clear"), L("Branching Fissures: fissuras secundárias, clear muito maior.", "Branching Fissures: secondary fissures, much bigger clear."), "free"),
   G("Thunderstorm", ["Rapid Casting I", "Living Lightning"], L("Shock", "Shock"), L("Primeiro da rotação: prepara os inimigos.", "First in the rotation: sets enemies up."), "free"),
   G("Ravenous Swarm", ["Corrosion", "Armour Demolisher I"], L("Dano passivo", "Passive damage"), L("Continua quebrando Armour.", "Keeps breaking Armour."), "core", 2, L("30 Spirit", "30 Spirit")),
   G("Thrashing Vines", ["Concentrated Area", "Zenith II", "Prolonged Duration I"], L("Boss", "Boss"), L("Vinhas gigantes na área alvo. Concentrated Area: área menor, mais dano no boss.", "Huge vines in the target area. Concentrated Area: smaller area, more boss damage."), "free"),
   G("Mana Remnants", [], L("Mana", "Mana"), L("Inimigos com ailment elemental que morrem soltam Remnants de mana. Reserva 30 Spirit. Vira peça central depois dos totems.", "Enemies with elemental ailments that die drop mana Remnants. Reserves 30 Spirit. Becomes central after the totems."), "core", 1, L("30 Spirit", "30 Spirit")),
  ],
  cheap=[L("Cajado com +níveis de spell", "Staff with +spell levels"), L("Guarde rares identificados para vender: gold para o respec", "Keep identified rares to sell: gold for the respec")],
  full=[L("Compre já o sceptre com 130+ Spirit e a wand com +níveis de Lightning/All Spells para a troca", "Buy the 130+ Spirit sceptre and the wand with +levels to Lightning/All Spells for the swap now")],
  stats=[L("+Physical/All Spell Skills", "+Physical/All Spell Skills"), L("% Spell/Physical Damage", "% Spell/Physical Damage"), L("% Cast Speed", "% Cast Speed"), L("Vida", "Life"), L("Resistências (elemental bom? então chaos)", "Resistances (elemental fine? then chaos)")],
  tree=L("Nós de spell/crítico e caminho para o lado de totem.", "Spell/crit nodes and a path towards the totem side."),
  avoid=[L("Gastar todo o gold", "Spending all your gold")],
  exit=[L("The Lesser Harm + Forced Outcome", "The Lesser Harm + Forced Outcome"), L("Ignagduk (+30 Spirit)", "Ignagduk (+30 Spirit)")]),

 dict(id="a4", name=L("Ato 4", "Act 4"), lv=[40, 50], tag=L("Juntar Spirit para a troca", "Gather Spirit for the swap"),
  carry=L("Você: mesma rotação do Ato 3", "You: same rotation as Act 3"), dmgSplit=[100, 0],
  goal=L("Mesmo setup do Ato 3. O objetivo real é juntar: 210+ Spirit, sceptre 130+ Spirit, wand com +níveis de Lightning/All Spells e gold/pontos para Ancestral Bond e Efficient Inscriptions. Quanto mais tempo com este setup, melhor a troca.", "Same setup as Act 3. The real goal is to gather: 210+ Spirit, a 130+ Spirit sceptre, a wand with +levels to Lightning/All Spells and gold/points for Ancestral Bond and Efficient Inscriptions. The longer you stay on this setup, the better the swap."),
  rotation=[L("Thunderstorm > Entangle > Thrashing Vines > Bonestorm", "Thunderstorm > Entangle > Thrashing Vines > Bonestorm")],
  gems=[
   G("Bonestorm", ["Burgeon I", "Zenith II", "Considered Casting"], L("Boss", "Boss"), L("Igual ao Ato 3.", "Same as Act 3."), "free"),
   G("Entangle", ["Accelerated Growth", "Rapid Casting I", "Branching Fissures I"], L("Clear", "Clear"), L("Igual ao Ato 3.", "Same as Act 3."), "free"),
   G("Thunderstorm", ["Rapid Casting I", "Living Lightning"], L("Shock", "Shock"), L("Igual ao Ato 3.", "Same as Act 3."), "free"),
   G("Ravenous Swarm", ["Corrosion", "Armour Demolisher I"], L("Dano passivo", "Passive damage"), L("Igual ao Ato 3.", "Same as Act 3."), "core", 2, L("30 Spirit", "30 Spirit")),
   G("Thrashing Vines", ["Concentrated Area", "Zenith II", "Prolonged Duration I"], L("Boss", "Boss"), L("Igual ao Ato 3.", "Same as Act 3."), "free"),
   G("Mana Remnants", [], L("Mana", "Mana"), L("Igual ao Ato 3.", "Same as Act 3."), "core", 1, L("30 Spirit", "30 Spirit")),
  ],
  cheap=[L("Sceptre com 130+ Spirit (guarde para a troca)", "Sceptre with 130+ Spirit (keep it for the swap)"), L("Wand de 1 mão com +níveis de Lightning ou All Spell Skills", "One-handed wand with +levels to Lightning or All Spell Skills"), L("Venda rares identificados: gold para o respec", "Sell identified rares: gold for the respec")],
  full=[L("Amuleto e body com Spirit para chegar a 255 sem depender do Efficient Inscriptions", "Amulet and body armour with Spirit to reach 255 without relying on Efficient Inscriptions")],
  stats=[L("Spirit (sceptre, amuleto, body)", "Spirit (sceptre, amulet, body)"), L("+Lightning/All Spell Skills na wand", "+Lightning/All Spell Skills on the wand"), L("% Cast Speed", "% Cast Speed"), L("Vida", "Life"), L("Resistências", "Resistances")],
  tree=L("Igual ao Ato 3 + pontos guardados para o respec da troca.", "Same as Act 3 + points kept for the swap respec."),
  avoid=[L("Trocar para totem antes de ter 210+ Spirit", "Swapping to totems before having 210+ Spirit")],
  exit=[L("210+ Spirit com o sceptre", "210+ Spirit with the sceptre"), L("Gold para o respec", "Gold for the respec"), L("Testes de resistência do Ato 4", "Act 4 resistance trials")]),

 dict(id="sw", name=L("Troca para totem", "Totem swap"), lv=[51, 56], tag=L("Spell Totem com Spark", "Spell Totem with Spark"),
  carry=L("Totems: Spark", "Totems: Spark"), dmgSplit=[15, 85],
  goal=L("Final do Ato 4: respec para Spell Totem. Só troque com 210+ Spirit (60 da campanha + sceptre com 130+), pontos para Ancestral Bond e, se não tiver 255 Spirit, também para Efficient Inscriptions. Ascendência: Unnamed Heartwood (+1 totem).", "End of Act 4: respec to Spell Totem. Only swap with 210+ Spirit (60 from the campaign + a 130+ sceptre), points for Ancestral Bond and, if you don't have 255 Spirit, also for Efficient Inscriptions. Ascendancy: Unnamed Heartwood (+1 totem)."),
  rotation=[L("Coloque os totems perto do pack/boss", "Place the totems near the pack/boss"), L("Frost Bomb (Exposure) + Elemental Weakness (curse)", "Frost Bomb (Exposure) + Elemental Weakness (curse)"), L("Orb of Storms e Flame Wall", "Orb of Storms and Flame Wall"), L("Recolha os Remnants de mana", "Collect the mana Remnants")],
  gems=[
   G("Spell Totem", ["Spark", "Zenith II", "Deliberation"], L("CARRY", "CARRY"), L("Meta skill: o totem lança o Spark por você. Com Ancestral Bond não precisa de charges, cada totem reserva 75 Spirit e você só paga a mana do totem, não do spell. O Lowepe mostra um 2º setup com Urgent Totems III + Projectile Acceleration III para quando tiver mais links.", "Meta skill: the totem casts Spark for you. With Ancestral Bond it needs no charges, each totem reserves 75 Spirit and you only pay the totem's mana, not the spell's. Lowepe shows a 2nd setup with Urgent Totems III + Projectile Acceleration III for when you have more links."), "core", 1, TOTEM_COST),
   G("Orb of Storms", ["Overabundance I", "Living Lightning"], L("Dano extra", "Extra damage"), L("Orb que dispara raios encadeados e deixa uma Lightning Infusion. Overabundance aumenta o limite de orbs.", "Orb that fires chaining lightning and leaves a Lightning Infusion. Overabundance raises the orb limit."), "free"),
   G("Frost Bomb", ["Potent Exposure", "Magnified Area I"], L("Exposure", "Exposure"), L("Tira resistência elemental e deixa uma Cold Infusion — o Spark consome Cold Infusion para lançar muitas faíscas em círculo.", "Removes elemental resistance and leaves a Cold Infusion — Spark consumes Cold Infusion to fire many sparks in a circle."), "free"),
   G("Flame Wall", ["Efficiency I", "Prolonged Duration I"], L("Dano extra", "Extra damage"), L("Projéteis que passam pelo muro ganham dano de fogo — o Spark do totem atravessa a Flame Wall.", "Projectiles passing through the wall gain fire damage — the totem's Spark passes through Flame Wall."), "free"),
   G("Elemental Weakness", ["Prolonged Duration I"], L("Curse", "Curse"), L("Curse que reduz resistências elementais.", "Curse that lowers elemental resistances."), "free"),
   G("Mana Remnants", ["Harmonic Remnants II", "Remnant Potency II"], L("Mana", "Mana"), L("Sustenta a mana (o Zenith II precisa de mana acima de 90%). Reserva 30 Spirit. Dica do Lowepe: nos bosses dá para desligar para caber mais um totem.", "Sustains mana (Zenith II needs mana above 90%). Reserves 30 Spirit. Lowepe's tip: on bosses you can turn it off to fit one more totem."), "core", 2, L("30 Spirit", "30 Spirit")),
  ],
  cheap=[L("Attuned Wand com +níveis de Lightning/All Spells", "Attuned Wand with +levels to Lightning/All Spells"), L("Omen Sceptre com 130+ Spirit", "Omen Sceptre with 130+ Spirit"), L("Amuleto e body com Spirit (Solar Amulet, Avian Robe)", "Amulet and body armour with Spirit (Solar Amulet, Avian Robe)")],
  full=[L("Mesmos slots com mais Spirit e +níveis de spell", "Same slots with more Spirit and +spell levels")],
  stats=[L("+Level Lightning/All Spell Skills", "+Level Lightning/All Spell Skills"), L("Spirit", "Spirit"), L("% Spell/Lightning", "% Spell/Lightning"), L("% Cast Speed", "% Cast Speed"), L("Vida", "Life"), L("Resistências", "Resistances")],
  tree=L("Respec: Ancestral Bond, Efficient Inscriptions (se < 255 Spirit), Branching Bolts. Weapon Set 1 = nós de totem; Weapon Set 2 = o resto.", "Respec: Ancestral Bond, Efficient Inscriptions (if < 255 Spirit), Branching Bolts. Weapon Set 1 = totem nodes; Weapon Set 2 = everything else."),
  avoid=[L("Trocar sem 210 Spirit: poucos totems e dano menor que o setup anterior", "Swapping without 210 Spirit: few totems and less damage than the previous setup"), L("Pierce II junto com Branching Bolts", "Pierce II together with Branching Bolts")],
  exit=[L("3+ totems colocados", "3+ totems placed"), L("Unnamed Heartwood", "Unnamed Heartwood"), L("Mana sustentada com Mana Remnants", "Mana sustained with Mana Remnants")]),

 dict(id="int", name=L("Interlúdios", "Interludes"), lv=[57, 64], tag=L("Totems + mana", "Totems + mana"),
  carry=L("Totems: Spark", "Totems: Spark"), dmgSplit=[10, 90],
  goal=L("Um Spell Totem só, com os supports melhores (Urgent Totems III + Projectile Acceleration III). Ascendência: The Unseen Path. Suba mana e Spirit.", "A single Spell Totem gem with the better supports (Urgent Totems III + Projectile Acceleration III). Ascendancy: The Unseen Path. Raise mana and Spirit."),
  rotation=[L("Totems → Frost Bomb → Elemental Weakness → Orb/Flame Wall", "Totems → Frost Bomb → Elemental Weakness → Orb/Flame Wall")],
  gems=[
   G("Spell Totem", ["Spark", "Zenith II", "Urgent Totems III", "Projectile Acceleration III"], L("CARRY", "CARRY"), L("Urgent Totems III coloca os totems muito mais rápido e dá cast speed. Projectile Acceleration III transforma velocidade do Spark em dano. Opcional do Lowepe: Pierce II no lugar de um support — mas aí sem Branching Bolts na árvore.", "Urgent Totems III places totems much faster and adds cast speed. Projectile Acceleration III turns Spark speed into damage. Lowepe's option: Pierce II instead of a support — but then no Branching Bolts on the tree."), "core", 1, TOTEM_COST),
   G("Orb of Storms", ["Overabundance I", "Living Lightning"], L("Dano extra", "Extra damage"), L("Igual à troca.", "Same as the swap."), "free"),
   G("Frost Bomb", ["Potent Exposure", "Magnified Area I"], L("Exposure", "Exposure"), L("Cold Infusion para o Spark.", "Cold Infusion for Spark."), "free"),
   G("Flame Wall", ["Efficiency I", "Prolonged Duration I"], L("Dano extra", "Extra damage"), L("Igual à troca.", "Same as the swap."), "free"),
   G("Elemental Weakness", ["Prolonged Duration I"], L("Curse", "Curse"), L("Igual à troca.", "Same as the swap."), "free"),
   G("Mana Remnants", ["Remnant Potency II", "Harmonic Remnants II"], L("Mana", "Mana"), L("Igual à troca.", "Same as the swap."), "core", 2, L("30 Spirit", "30 Spirit")),
  ],
  cheap=[L("Attuned Wand + Omen Sceptre", "Attuned Wand + Omen Sceptre"), L("Solar Amulet e Avian Robe com Spirit", "Solar Amulet and Avian Robe with Spirit")],
  full=[L("Waveshaper (Spirit + ES + mana vira Armour)", "Waveshaper (Spirit + ES + mana becomes Armour)"), L("Peças Runeforged para Runic Ward (Grim Pillars depois)", "Runeforged pieces for Runic Ward (Grim Pillars later)")],
  stats=[L("Spirit", "Spirit"), L("Mana máxima e regeneração", "Maximum mana and regeneration"), L("+Level Lightning/All Spells", "+Level Lightning/All Spells"), L("Vida", "Life"), L("Resistências", "Resistances")],
  tree=L("Mais nós de totem (Weapon Set 1), mana e spell.", "More totem nodes (Weapon Set 1), mana and spell."),
  avoid=[L("Pular Lythara (+40 Spirit): é mais um totem", "Skipping Lythara (+40 Spirit): it's one more totem")],
  exit=[L("Lythara (+40 Spirit)", "Lythara (+40 Spirit)"), L("The Unseen Path", "The Unseen Path"), L("Resistências no cap", "Resistances capped")]),

 dict(id="ea", name=L("Início do Atlas", "Early Atlas"), lv=[65, 74], tag=L("Spark + Mana Tempest", "Spark + Mana Tempest"),
  carry=L("Totems: Spark", "Totems: Spark"), dmgSplit=[10, 90],
  goal=L("Setup de início de endgame do Lowepe: Waveshaper, peças Runeforged e Mana Tempest para bosses (use depois de colocar tudo). Grim Pillars ainda não é obrigatório.", "Lowepe's early endgame setup: Waveshaper, Runeforged pieces and Mana Tempest for bosses (use it after placing everything). Grim Pillars isn't required yet."),
  rotation=[L("Totems", "Totems"), L("Frost Bomb + Elemental Weakness", "Frost Bomb + Elemental Weakness"), L("Orb of Storms + Flame Wall", "Orb of Storms + Flame Wall"), L("Mana Tempest por último, no boss", "Mana Tempest last, on the boss")],
  gems=[
   G("Spell Totem", ["Spark", "Urgent Totems III", "Zenith II", "Projectile Acceleration III"], L("CARRY", "CARRY"), L("Mesmo setup de Spark dos Interlúdios.", "Same Spark setup as the Interludes."), "core", 1, TOTEM_COST),
   G("Frost Bomb", ["Potent Exposure", "Magnified Area I"], L("Exposure", "Exposure"), L("Cold Infusion + Exposure.", "Cold Infusion + Exposure."), "free"),
   G("Elemental Weakness", ["Prolonged Duration I"], L("Curse", "Curse"), L("Curse.", "Curse."), "free"),
   G("Flame Wall", ["Prolonged Duration II", "Efficiency I"], L("Dano extra", "Extra damage"), L("Dura mais.", "Lasts longer."), "free"),
   G("Orb of Storms", ["Living Lightning", "Overabundance I", "Unleash"], L("Dano extra", "Extra damage"), L("Unleash repete o Orb várias vezes.", "Unleash repeats the Orb several times."), "free"),
   G("Mana Remnants", [], L("Mana", "Mana"), L("Sustento de mana.", "Mana sustain."), "core", 2, L("30 Spirit", "30 Spirit")),
   G("Mana Tempest", ["Advancing Storm"], L("Boss", "Boss"), L("Empower nos spells que custam mana enquanto você fica dentro da tempestade; drena mana. Use DEPOIS de colocar todo o resto, no boss. Advancing Storm faz a tempestade andar até o alvo.", "Empowers mana-costing spells while you stay inside the storm; drains mana. Use it AFTER placing everything else, on the boss. Advancing Storm makes the storm move to the target."), "free"),
  ],
  cheap=[L("Attuned Wand + Stoic Sceptre", "Attuned Wand + Stoic Sceptre"), L("Waveshaper", "Waveshaper"), L("Helmet/gloves/boots Runeforged", "Runeforged helmet/gloves/boots")],
  full=[L("Soul Mantle (+75 Spirit e +1 totem)", "Soul Mantle (+75 Spirit and +1 totem)"), L("Dueling Wand (dá Spellslinger)", "Dueling Wand (grants Spellslinger)"), L("Comece a procurar/craftar o amuleto de Archmage", "Start looking for/crafting the Archmage amulet")],
  stats=[L("Spirit", "Spirit"), L("Mana máxima", "Maximum mana"), L("+Level Lightning/All Spells", "+Level Lightning/All Spells"), L("Runic Ward (Runeforged)", "Runic Ward (Runeforged)"), L("Resistências", "Resistances")],
  tree=L("Mana, totem e spell; weapon sets como antes.", "Mana, totem and spell; weapon sets as before."),
  avoid=[L("Usar Mana Tempest antes de colocar os totems (drena a mana)", "Using Mana Tempest before placing the totems (it drains mana)")],
  exit=[L("T1–T10 sem mortes", "T1–T10 without deaths"), L("Grim Pillars/Bitter Dead no inventário", "Grim Pillars/Bitter Dead in inventory"), L("Runic Ward nas armaduras", "Runic Ward on armour")]),

 dict(id="w1", name=L("Atlas: Grim Pillars", "Atlas: Grim Pillars"), lv=[75, 87], tag=L("Grim Pillars + Bitter Dead", "Grim Pillars + Bitter Dead"),
  carry=L("Totems: Grim Pillars + Bitter Dead", "Totems: Grim Pillars + Bitter Dead"), dmgSplit=[5, 95],
  goal=L("\"Semana 1\" do Lowepe: Grim Pillars + Bitter Dead no Spell Totem (muito mais clear speed), Soul Mantle, Archmage e Malice. Grim Pillars e Bitter Dead gastam Runic Ward, então as armaduras precisam ser Runeforged. Entangle ativa os Grim Pillars: build de 2 botões.", "Lowepe's \"Week 1\": Grim Pillars + Bitter Dead in Spell Totem (much more clear speed), Soul Mantle, Archmage and Malice. Grim Pillars and Bitter Dead spend Runic Ward, so armour must be Runeforged. Entangle sets off the Grim Pillars: 2-button build."),
  rotation=[L("Weapon Set 1: Spell Totem + Archmage", "Weapon Set 1: Spell Totem + Archmage"), L("Weapon Set 2: Entangle, Frost Bomb, Elemental Weakness", "Weapon Set 2: Entangle, Frost Bomb, Elemental Weakness"), L("Nos dois sets: Mana Tempest e Mana Remnants", "On both sets: Mana Tempest and Mana Remnants")],
  gems=[
   G("Spell Totem", ["Grim Pillars", "Magnified Area II", "Urgent Totems III", "Cold Mastery", "Bitter Dead"], L("CARRY", "CARRY"), L("Grim Pillars (pilares de gelo que explodem) + Bitter Dead (corpos viram núcleos de Chill). Os dois gastam Runic Ward em vez de mana. Cold Mastery: +1 nível nos dois. O Lowepe diz que dá para trocar uma gem nos bosses, mas não precisou.", "Grim Pillars (exploding ice pillars) + Bitter Dead (corpses become Chill cores). Both spend Runic Ward instead of mana. Cold Mastery: +1 level to both. Lowepe says you can swap a gem for bosses, but he didn't need to."), "core", 1, TOTEM_COST),
   G("Entangle", ["Branching Fissures I", "Biting Frost II", "Unleash", "Rapid Casting II"], L("Ativa os pilares", "Sets off the pillars"), L("Weapon Set 2. A fissura passa pelos Grim Pillars e faz eles explodirem: é o 2º botão da build.", "Weapon Set 2. The fissure runs into the Grim Pillars and makes them explode: it's the build's 2nd button."), "free"),
   G("Frost Bomb", ["Potent Exposure", "Magnified Area II", "Prolonged Duration II"], L("Exposure", "Exposure"), L("Weapon Set 2.", "Weapon Set 2."), "free"),
   G("Mana Tempest", ["Advancing Storm", "Efficiency II"], L("Boss", "Boss"), L("Nos dois weapon sets.", "On both weapon sets."), "free"),
   G("Elemental Weakness", ["Prolonged Duration II"], L("Curse", "Curse"), L("Weapon Set 2.", "Weapon Set 2."), "free"),
   G("Malice", ["Prolonged Duration II", "Her Declaration"], L("Aura", "Aura"), L("Aura que aplica Critical Weakness em inimigos na Presence — combina com Forced Outcome (críticos inevitáveis). O custo de Spirit não está nos dados do Path of Building: confira no jogo.", "Aura that applies Critical Weakness to enemies in your Presence — pairs with Forced Outcome (inevitable crits). Its Spirit cost isn't in Path of Building's data: check in game."), "core", 4, L("Reserva Spirit (confira no jogo)", "Reserves Spirit (check in game)")),
   G("Archmage", ["Lightning Mastery", "Clarity II"], L("Dano da mana", "Damage from mana"), L("Weapon Set 1. Spells não canalizados custam mana extra e causam dano de raio extra baseado na mana máxima. Reserva 100 Spirit.", "Weapon Set 1. Non-channelled spells cost extra mana and deal extra lightning damage based on maximum mana. Reserves 100 Spirit."), "core", 3, L("100 Spirit", "100 Spirit")),
   G("Mana Remnants", ["Harmonic Remnants II", "Remnant Potency III"], L("Mana", "Mana"), L("Nos dois weapon sets.", "On both weapon sets."), "core", 2, L("30 Spirit", "30 Spirit")),
  ],
  cheap=[L("Dueling Wand + Omen Sceptre", "Dueling Wand + Omen Sceptre"), L("Soul Mantle", "Soul Mantle"), L("Luvas Runeforged (Runic Ward)", "Runeforged gloves (Runic Ward)"), L("Breath of the Mountains (charm)", "Breath of the Mountains (charm)")],
  full=[L("Amuleto de Archmage craftado (ver aba Crafting)", "Crafted Archmage amulet (see the Crafting tab)"), L("Lavianga's Spirits", "Lavianga's Spirits")],
  stats=[L("Mana máxima (Archmage + Mind Over Matter)", "Maximum mana (Archmage + Mind Over Matter)"), L("Spirit", "Spirit"), L("Runic Ward", "Runic Ward"), L("+Level All Spells", "+Level All Spells"), L("Resistências", "Resistances")],
  tree=L("Mind Over Matter e nós de mana. Ascendência: The Unseen Path + Harmony Within + The Lesser Harm + Forced Outcome (a Soul Mantle dá o +1 totem do Heartwood).", "Mind Over Matter and mana nodes. Ascendancy: The Unseen Path + Harmony Within + The Lesser Harm + Forced Outcome (Soul Mantle provides Heartwood's +1 totem)."),
  avoid=[L("Grim Pillars sem Runic Ward (não lança)", "Grim Pillars without Runic Ward (it won't cast)"), L("Tirar o Unnamed Heartwood sem ter a Soul Mantle ou gem do Spell Totem nível 14+", "Removing Unnamed Heartwood without Soul Mantle or a level 14+ Spell Totem gem")],
  exit=[L("Grim Pillars + Bitter Dead nos totems", "Grim Pillars + Bitter Dead in the totems"), L("Archmage ativo", "Archmage active"), L("T15+ sem mortes", "T15+ without deaths")]),

 dict(id="fin", name=L("Endgame final", "Final endgame"), lv=[88, 100], tag=L("Rakiata's Flow + Spellslinger", "Rakiata's Flow + Spellslinger"),
  carry=L("Totems: Grim Pillars + Bitter Dead", "Totems: Grim Pillars + Bitter Dead"), dmgSplit=[5, 95],
  goal=L("Versão final do Lowepe: Rakiata's Flow no totem (resistências do inimigo invertidas), Spellslinger (vem da Dueling Wand), Repulsion, Entangle com Elemental Discharge, amuleto de Archmage craftado e Lavianga's Spirits. Ascendência troca Harmony Within por Entwined Realities.", "Lowepe's final version: Rakiata's Flow in the totem (enemy resistances inverted), Spellslinger (from the Dueling Wand), Repulsion, Entangle with Elemental Discharge, a crafted Archmage amulet and Lavianga's Spirits. Ascendancy swaps Harmony Within for Entwined Realities."),
  rotation=[L("Totems", "Totems"), L("Entangle (ativa os pilares e descarrega ailments)", "Entangle (sets off pillars and discharges ailments)"), L("Repulsion em pack perigoso", "Repulsion on dangerous packs"), L("Mana Tempest no boss", "Mana Tempest on the boss")],
  gems=[
   G("Spell Totem", ["Grim Pillars", "Magnified Area II", "Urgent Totems III", "Bitter Dead", "Rakiata's Flow"], L("CARRY", "CARRY"), L("Rakiata's Flow substitui Cold Mastery: os hits tratam resistências elementais do inimigo como invertidas.", "Rakiata's Flow replaces Cold Mastery: hits treat enemy elemental resistances as inverted."), "core", 1, TOTEM_COST),
   G("Mana Remnants", ["Harmonic Remnants II", "Remnant Potency III"], L("Mana", "Mana"), L("Sustento de mana.", "Mana sustain."), "core", 2, L("30 Spirit", "30 Spirit")),
   G("Archmage", ["Lightning Mastery"], L("Dano da mana", "Damage from mana"), L("Reserva 100 Spirit.", "Reserves 100 Spirit."), "core", 3, L("100 Spirit", "100 Spirit")),
   G("Malice", ["Prolonged Duration II", "Her Declaration", "Clarity II"], L("Aura", "Aura"), L("Clarity II passa para o Malice. Custo de Spirit: confira no jogo.", "Clarity II moves to Malice. Spirit cost: check in game."), "core", 4, L("Reserva Spirit (confira no jogo)", "Reserves Spirit (check in game)")),
   G("Spellslinger", [], L("Trigger", "Trigger"), L("Vem da Dueling Wand (não é gem que você compra). Acumula energia quando você lança spells e dispara os spells socketados.", "Comes from the Dueling Wand (not a gem you buy). Builds energy when you cast spells and triggers the socketed spells."), "opt", 1, L("Reserva Spirit (confira no jogo)", "Reserves Spirit (check in game)")),
   G("Entangle", ["Branching Fissures I", "Elemental Discharge", "Unleash", "Rapid Casting II"], L("Ativa os pilares", "Sets off the pillars"), L("Elemental Discharge consome os ailments para uma descarga elemental.", "Elemental Discharge consumes ailments for an elemental discharge."), "free"),
   G("Repulsion", [], L("Defesa/controle", "Defence/control"), L("Gasta Runic Ward para amaldiçoar com Fragility; ao acertar, explode e empurra os inimigos.", "Spends Runic Ward to curse with Fragility; hitting them explodes and knocks enemies back."), "free"),
   G("Mana Tempest", ["Advancing Storm", "Efficiency II"], L("Boss", "Boss"), L("Igual à semana 1.", "Same as week 1."), "free"),
  ],
  cheap=[L("Setup da semana 1 com Soul Mantle", "Week 1 setup with Soul Mantle")],
  full=[L("Amuleto de Archmage craftado (custo variável)", "Crafted Archmage amulet (variable cost)"), L("Body rare Feathered Raiment com Spirit/mana", "Rare Feathered Raiment body with Spirit/mana"), L("Charms: The Fall of the Axe, Nascent Hope, Arakaali's Gift", "Charms: The Fall of the Axe, Nascent Hope, Arakaali's Gift"), L("Lavianga's Spirits", "Lavianga's Spirits")],
  stats=[L("Mana máxima", "Maximum mana"), L("Spirit", "Spirit"), L("+Level All Spells", "+Level All Spells"), L("Runic Ward", "Runic Ward"), L("Resistências", "Resistances")],
  tree=L("Ascendência: The Unseen Path + Entwined Realities + The Lesser Harm + Forced Outcome. Sem Soul Mantle e sem Heartwood: o limite vem da gem de Spell Totem nível 14+ (2 base) dobrada pelo Ancestral Bond.", "Ascendancy: The Unseen Path + Entwined Realities + The Lesser Harm + Forced Outcome. No Soul Mantle and no Heartwood: the limit comes from the level 14+ Spell Totem gem (2 base) doubled by Ancestral Bond."),
  avoid=[L("Começar o craft do amuleto sem limite de gastos e sem comparar uma peça pronta", "Starting the amulet craft without a spending limit or comparing a finished item")],
  exit=[L("Pinnacle bosses", "Pinnacle bosses")]),
]
PH = {p["id"]: p for p in PHASES}
VMAP = {"a1": "Akt 1", "a2": "Akt 2", "a3": "Akt 3", "a4": "Akt 4", "sw": "Akt 4 - Totem Swap", "int": "Interludes", "ea": "Endgame Start (Import)", "w1": "Endgame (Woche 1)", "fin": "Endgame (Final)"}

# caixa "quantos totems" por fase (usa o mesmo componente da caixa de esqueletos)
BOX = {
 "a1": ("0", [], L("Ainda sem totems: você lança os spells.", "No totems yet: you cast the spells.")),
 "a2": ("0", [], L("Ainda sem totems.", "No totems yet.")),
 "a3": ("0", [], L("Ainda sem totems. Guarde gold e procure o sceptre de Spirit.", "No totems yet. Save gold and look for the Spirit sceptre.")),
 "a4": ("0", [], L("Ainda sem totems. Só troque com 210+ Spirit.", "No totems yet. Only swap with 210+ Spirit.")),
 "sw": ("3 → 4", [L("Limite: (1 base + 1 Heartwood) × 2 Ancestral Bond = 4", "Limit: (1 base + 1 Heartwood) × 2 Ancestral Bond = 4")], L("Cada totem reserva 75 Spirit (62,5 com Efficient Inscriptions). 3 totems + Mana Remnants ≈ 255 sem Efficient Inscriptions.", "Each totem reserves 75 Spirit (62.5 with Efficient Inscriptions). 3 totems + Mana Remnants ≈ 255 without Efficient Inscriptions.")),
 "int": ("3 → 4", [L("Gem do Spell Totem nível 14+ = 2 base", "Spell Totem gem level 14+ = 2 base")], L("Com a gem no nível 14+ o limite base vira 2: (2 + 1 Heartwood) × 2 = 6, mas o Spirit decide quantos cabem.", "With the gem at level 14+ the base limit becomes 2: (2 + 1 Heartwood) × 2 = 6, but Spirit decides how many fit.")),
 "ea": ("4", [], L("Quantos couberem no Spirit, deixando 30 para o Mana Remnants.", "As many as fit your Spirit, leaving 30 for Mana Remnants.")),
 "w1": ("4+", [L("Soul Mantle: +1 totem", "Soul Mantle: +1 totem")], L("Archmage (100) e Malice também reservam: confira quantos totems ainda cabem.", "Archmage (100) and Malice also reserve: check how many totems still fit.")),
 "fin": ("4", [L("(2 base + 0) × 2 = 4", "(2 base + 0) × 2 = 4")], L("Sem Heartwood e sem Soul Mantle na variante final.", "No Heartwood and no Soul Mantle in the final variant.")),
}
SPIRIT_NOTE = {
 "sw": L("Ordem do Spirit: 1) Spell Totem (cada totem 75, ou 62,5 com Efficient Inscriptions) → 2) Mana Remnants (30). Guia do Lowepe: 210 Spirit com Efficient Inscriptions, 255 sem.", "Spirit order: 1) Spell Totem (each totem 75, or 62.5 with Efficient Inscriptions) → 2) Mana Remnants (30). Lowepe's guide: 210 Spirit with Efficient Inscriptions, 255 without."),
 "int": L("Ordem do Spirit: totems → Mana Remnants (30). Cada +75 Spirit é mais um totem.", "Spirit order: totems → Mana Remnants (30). Every +75 Spirit is one more totem."),
 "ea": L("Ordem do Spirit: totems → Mana Remnants (30). Mana Tempest não reserva Spirit (drena mana).", "Spirit order: totems → Mana Remnants (30). Mana Tempest reserves no Spirit (it drains mana)."),
 "w1": L("Ordem do Spirit: totems → Mana Remnants (30) → Archmage (100) → Malice (confira). Se faltar Spirit no boss, o Lowepe desliga o Mana Remnants para caber mais um totem (no boss não caem Remnants).", "Spirit order: totems → Mana Remnants (30) → Archmage (100) → Malice (check). If short on Spirit for a boss, Lowepe turns off Mana Remnants to fit one more totem (bosses don't drop Remnants)."),
 "fin": L("Ordem do Spirit: totems → Mana Remnants (30) → Archmage (100) → Malice → Spellslinger (confira no jogo).", "Spirit order: totems → Mana Remnants (30) → Archmage (100) → Malice → Spellslinger (check in game)."),
 "a1": L("Ravenous Swarm reserva 30 Spirit; o resto não reserva.", "Ravenous Swarm reserves 30 Spirit; the rest reserve none."),
 "a3": L("Mana Remnants (30) e Ravenous Swarm (30) reservam Spirit. Guarde Spirit de item para a troca.", "Mana Remnants (30) and Ravenous Swarm (30) reserve Spirit. Keep Spirit items for the swap."),
 "a4": L("Mana Remnants (30) e Ravenous Swarm (30). Na troca, o Ravenous Swarm sai e o Spirit vai para os totems.", "Mana Remnants (30) and Ravenous Swarm (30). At the swap, Ravenous Swarm leaves and Spirit goes to the totems."),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in SPIRIT_NOTE.items():
    PH[pid]["spiritNote"] = note

# ------------------------------------------------------------------ marcos
MILESTONES = {
 1: L("Volcano (segure para canalizar) + Entangle.", "Volcano (hold to channel) + Entangle."),
 10: L("Freythorn: King in the Mists (+30 Spirit).", "Freythorn: King in the Mists (+30 Spirit)."),
 12: L("Bonestorm no lugar de Volcano/Frost Bomb antes do boss do Ato 1.", "Bonestorm replaces Volcano/Frost Bomb before the Act 1 boss."),
 16: L("Wildsurge Incantation na árvore. Thunderstorm entra.", "Wildsurge Incantation on the tree. Thunderstorm comes in."),
 22: L("1ª ascendência: The Lesser Harm.", "1st ascendancy: The Lesser Harm."),
 28: L("Thrashing Vines para bosses. Comece a olhar vendors: sceptre 130+ Spirit e wand +Lightning/All Spells.", "Thrashing Vines for bosses. Start checking vendors: 130+ Spirit sceptre and +Lightning/All Spells wand."),
 34: L("2ª ascendência: Forced Outcome (críticos inevitáveis).", "2nd ascendancy: Forced Outcome (inevitable crits)."),
 38: L("Azak Bog: Ignagduk (+30 Spirit).", "Azak Bog: Ignagduk (+30 Spirit)."),
 44: L("Venda rares identificados: gold para o respec da troca.", "Sell identified rares: gold for the swap respec."),
 50: L("Checklist da troca: 210+ Spirit, wand, pontos para Ancestral Bond (+ Efficient Inscriptions se < 255).", "Swap checklist: 210+ Spirit, wand, points for Ancestral Bond (+ Efficient Inscriptions if < 255)."),
 52: L("TROCA: Spell Totem + Spark. Unnamed Heartwood na ascendência.", "SWAP: Spell Totem + Spark. Unnamed Heartwood on the ascendancy."),
 58: L("Gem do Spell Totem nível 14+: limite base de totems vira 2.", "Spell Totem gem level 14+: base totem limit becomes 2."),
 62: L("Kriar Village: Lythara (+40 Spirit) = mais um totem.", "Kriar Village: Lythara (+40 Spirit) = one more totem."),
 64: L("3ª ascendência: The Unseen Path.", "3rd ascendancy: The Unseen Path."),
 66: L("Mana Tempest para bosses (depois de colocar tudo).", "Mana Tempest for bosses (after placing everything)."),
 72: L("Peças Runeforged (Runic Ward) e Grim Pillars/Bitter Dead no inventário.", "Runeforged pieces (Runic Ward) and Grim Pillars/Bitter Dead in inventory."),
 76: L("Grim Pillars + Bitter Dead nos totems. Soul Mantle. Archmage.", "Grim Pillars + Bitter Dead in totems. Soul Mantle. Archmage."),
 80: L("4ª ascendência: Harmony Within. Mind Over Matter na árvore.", "4th ascendancy: Harmony Within. Mind Over Matter on the tree."),
 88: L("Dueling Wand (Spellslinger), Rakiata's Flow, Lavianga's Spirits.", "Dueling Wand (Spellslinger), Rakiata's Flow, Lavianga's Spirits."),
 92: L("Amuleto de Archmage craftado. Entwined Realities no lugar de Harmony Within.", "Crafted Archmage amulet. Entwined Realities instead of Harmony Within."),
}

# ------------------------------------------------------------------ ascendência (textos do tree.json)
ASCENDANCY = [
 dict(order=1, node="The Lesser Harm", when=L("1º Trial", "1st Trial"), text=L("Crítico inimigo contra você é Unlucky; dano de inimigos que te acertam é Unlucky.", "Enemy Critical Hit Chance against you is Unlucky; damage of enemies hitting you is Unlucky."), why=L("Defesa grátis durante toda a build.", "Free defence for the whole build.")),
 dict(order=2, node="Forced Outcome", when=L("2º Trial", "2nd Trial"), text=L("Inevitable Critical Hits.", "Inevitable Critical Hits."), why=L("Crítico garantido do jeito do jogo; combina com Malice (Critical Weakness) no endgame.", "Guaranteed crit mechanics; pairs with Malice (Critical Weakness) in endgame.")),
 dict(order=3, node="Unnamed Heartwood", when=L("Na troca para totem (respec da ascendência)", "At the totem swap (ascendancy respec)"), text=L("+1 ao número máximo de totems; totems morrem 6 s depois da vida chegar a 0.", "+1 to maximum number of Summoned Totems; totems die 6 seconds after their Life reaches 0."), why=L("Com Ancestral Bond o +1 vira +2. Sai quando a Soul Mantle dá o +1 ou quando a gem nível 14+ já basta.", "With Ancestral Bond the +1 becomes +2. Leaves once Soul Mantle provides the +1 or the level 14+ gem is enough.")),
 dict(order=4, node="The Unseen Path", when=L("3º Trial", "3rd Trial"), text=L("Walk the Paths Not Taken (texto do jogo).", "Walk the Paths Not Taken (game text)."), why=L("Usado pelo Lowepe do Interlúdio ao final. O Path of Building não detalha o efeito: leia o tooltip no jogo.", "Used by Lowepe from Interludes to the end. Path of Building doesn't detail the effect: read the in-game tooltip.")),
 dict(order=5, node="Harmony Within", when=L("4º Trial (semana 1)", "4th Trial (week 1)"), text=L("Dano de hit sai da mana antes da vida se a mana atual for maior que a vida atual; 15% less vida e mana máximas.", "Hit damage is taken from mana before life if current mana is higher than current life; 15% less maximum life and mana."), why=L("Defesa de mana-stacking antes do Mind Over Matter completo.", "Mana-stacking defence before a full Mind Over Matter setup.")),
 dict(order=6, node="Entwined Realities", when=L("Endgame final (troca pelo Harmony Within)", "Final endgame (replaces Harmony Within)"), text=L("Passivas não-keystone no raio médio de keystones alocados podem ser pegas sem conexão com a árvore.", "Non-keystone passives in medium radius of allocated keystones can be allocated without being connected."), why=L("Economiza pontos de caminho no endgame final.", "Saves pathing points in the final endgame.")),
]
ASC_UNLOCK = [20, 33, 52, 64, 78, 90]

KEY_PASSIVES = [
 dict(node="Wildsurge Incantation", type="Keystone", text=L("Storm e Plant spells: 50% more dano, custam 50% less, 75% less duração.", "Storm and Plant spells: 50% more damage, cost 50% less, 75% less duration."), when=L("Ato 2 → até a troca", "Act 2 → until the swap"), why=L("Thunderstorm, Entangle e Thrashing Vines são Storm/Plant.", "Thunderstorm, Entangle and Thrashing Vines are Storm/Plant.")),
 dict(node="Ancestral Bond", type="Keystone", text=L("Limite de totems dobrado; sem charges para colocar totems; cada totem reserva 75 Spirit.", "Totem limit doubled; no charges to place totems; each totem reserves 75 Spirit."), when=L("Troca para totem → sempre", "Totem swap → forever"), why=L("A base da build.", "The build's foundation.")),
 dict(node="Efficient Inscriptions", type="Notable", text=L("Meta skills: 20% increased eficiência de reserva.", "Meta Skills have 20% increased Reservation Efficiency."), when=L("Troca (se < 255 Spirit)", "Swap (if < 255 Spirit)"), why=L("75 → 62,5 Spirit por totem.", "75 → 62.5 Spirit per totem.")),
 dict(node="Branching Bolts", type="Notable", text=L("60% de chance de skills de raio encadearem mais uma vez.", "60% chance for Lightning Skills to Chain an additional time."), when=L("Com Spark", "With Spark"), why=L("Não use junto com Pierce II.", "Don't use together with Pierce II.")),
 dict(node="Mind Over Matter", type="Keystone", text=L("Todo dano sai da mana antes da vida; 50% less recuperação de mana.", "All damage is taken from mana before life; 50% less mana recovery."), when=L("Endgame (opcional desde a troca)", "Endgame (optional from the swap)"), why=L("Com Archmage a mana vira dano E defesa.", "With Archmage, mana becomes damage AND defence.")),
 dict(node="Mental Perseverance", type="Notable", text=L("10% do dano sai da mana antes da vida; +15 Intelligence.", "10% of damage is taken from mana before life; +15 Intelligence."), when=L("Alternativa leve ao Mind Over Matter", "Light alternative to Mind Over Matter"), why=L("Sugestão do Lowepe para testar depois da troca.", "Lowepe's suggestion to try after the swap.")),
]
TREE_STAGES = [
 dict(lv="1–14", focus=L("Spells físicos e área", "Physical spells and area"), dmg="Entangle/Volcano/Bonestorm", **{"def": L("Vida", "Life")}, spirit="—", dont=L("Soltar o canalizado cedo", "Releasing channelled skills early")),
 dict(lv="15–50", focus="Wildsurge Incantation", dmg="Thunderstorm/Entangle/Thrashing Vines", **{"def": L("Vida + resists", "Life + resists")}, spirit=L("Guardar itens de Spirit", "Keep Spirit items"), dont=L("Gastar o gold do respec", "Spending respec gold")),
 dict(lv="51–74", focus="Ancestral Bond, Efficient Inscriptions, Branching Bolts", dmg=L("Spark nos totems", "Spark in totems"), **{"def": L("Mana + vida", "Mana + life")}, spirit=L("Totems 75 cada", "Totems 75 each"), dont=L("Pierce II com Branching Bolts", "Pierce II with Branching Bolts")),
 dict(lv="75–100", focus="Mind Over Matter, mana", dmg="Grim Pillars + Bitter Dead", **{"def": L("Mana (MoM + Harmony Within)", "Mana (MoM + Harmony Within)")}, spirit=L("Totems + Archmage 100", "Totems + Archmage 100"), dont=L("Grim Pillars sem Runic Ward", "Grim Pillars without Runic Ward")),
]

# ------------------------------------------------------------------ uniques (preço poe.ninja, níveis PoB)
def _eco():
    out = {}
    for f in glob.glob(os.path.join(ROOT, "dl/eco_*.json")):
        for l in json.load(open(f, encoding="utf-8")).get("lines", []):
            bt = l["baseType"]
            if l["name"] in out and bt.startswith(("Runemastered", "Runeforged")):
                continue
            out[l["name"]] = {"price": l.get("primaryValue"), "icon": l.get("icon"), "base": bt.replace("Runemastered ", "").replace("Runeforged ", ""),
                              "mods": [re.sub(r"\[([^|\]]+\|)?([^\]]+)\]", r"\2", m["text"]) for m in l.get("explicitModifiers", []) if "\n" not in m["text"]][:7]}
    return out
ECO = _eco()

def U(n, slot, cat, p, why, how, alt):
    e = ECO.get(n, {})
    price = round(e["price"], 3) if e.get("price") is not None else None
    return dict(n=n, slot=slot, cat=cat, lvl=None, p=p, use=None, rf="", why=why, how=how, alt=alt, price=price, base=e.get("base", ""), mods=e.get("mods", []), iconUrl=e.get("icon"),
                tier="Barato" if (price or 0) < 0.1 else "Valor" if (price or 0) < 3 else "Luxo")

UNIQUES = [
 U("Soul Mantle", L("Body Armour", "Body Armour"), L("Armadura", "Armour"), "w1", L("+75 Spirit e +1 ao número máximo de totems. É o que deixa o Lowepe tirar o Unnamed Heartwood na semana 1.", "+75 Spirit and +1 to maximum totems. It's what lets Lowepe drop Unnamed Heartwood in week 1."), L("Cuidado: quando um totem morre, você recebe uma curse aleatória (ignora limite de curse).", "Careful: when a totem dies you get a random curse (ignores curse limit)."), L("Body rare com Spirit + Unnamed Heartwood na ascendência.", "Rare body with Spirit + Unnamed Heartwood on the ascendancy.")),
 U("Waveshaper", L("Body Armour", "Body Armour"), L("Armadura", "Armour"), "ea", L("Spirit, ES, resistências a fogo e frio, e ganha 30–50% da mana máxima como Armour. Body do início do endgame do Lowepe.", "Spirit, ES, fire and cold resistance, and gains 30–50% of maximum mana as Armour. Lowepe's early endgame body."), L("Barato e bom para mana-stacking.", "Cheap and good for mana stacking."), L("Body rare com Spirit.", "Rare body with Spirit.")),
 U("Lavianga's Spirits", L("Flask", "Flask"), "Flask", "fin", L("Flask de mana com efeito constante. Sustenta a mana com Mind Over Matter e Archmage.", "Mana flask with a constant effect. Sustains mana with Mind Over Matter and Archmage."), L("Use no slot de flask de mana.", "Use it in the mana flask slot."), L("Flask de mana normal de qualidade alta.", "A normal high-quality mana flask.")),
 U("Breath of the Mountains", "Charm", "Charm", "w1", L("Charm que ativa ao tomar dano de frio e dá Power Charge.", "Charm that triggers on taking cold damage and grants a Power Charge."), L("Semana 1 do Lowepe.", "Lowepe's week 1."), L("Sapphire Charm normal.", "Normal Sapphire Charm.")),
 U("The Fall of the Axe", "Charm", "Charm", "fin", L("Ativa quando você é Slowed e dá Onslaught.", "Triggers when you are Slowed and grants Onslaught."), L("Endgame final.", "Final endgame."), L("Silver Charm normal.", "Normal Silver Charm.")),
 U("Nascent Hope", "Charm", "Charm", "fin", L("Ativa quando você fica Frozen, chance de ganhar charge ao matar e começa a recarga de ES.", "Triggers when Frozen, chance to gain a charge on kill and starts ES recharge."), L("Endgame final.", "Final endgame."), L("Thawing Charm normal.", "Normal Thawing Charm.")),
 U("Arakaali's Gift", "Charm", "Charm", "fin", L("Ativa quando você é envenenado e recupera vida/mana baseado nos flasks.", "Triggers when poisoned and recovers life/mana based on your flasks."), L("Endgame final.", "Final endgame."), L("Antidote Charm normal.", "Normal Antidote Charm.")),
 U("Earthbound", L("Cajado", "Staff"), L("Arma", "Weapon"), "a3", L("Cajado com spell damage e cast speed que dispara Spark ao matar inimigo Shocked. Não está no guia, mas é um upgrade barato de leveling para spells antes da troca.", "Staff with spell damage and cast speed that triggers Spark on killing a Shocked enemy. Not in the guide, but a cheap leveling upgrade for spells before the swap."), L("Só até a troca (depois você usa wand + sceptre).", "Only until the swap (afterwards you use wand + sceptre)."), L("Cajado rare com +níveis de spell.", "Rare staff with +spell levels.")),
 U("Cloak of Defiance", L("Body Armour", "Body Armour"), L("Armadura", "Armour"), "w1", L("50% do dano sai da mana antes da vida, muita mana e regeneração. Não está no guia: alternativa de mana-stacking se ainda não tiver Mind Over Matter.", "50% of damage is taken from mana before life, lots of mana and regeneration. Not in the guide: a mana-stacking alternative if you don't have Mind Over Matter yet."), L("Perde o Spirit/+1 totem da Soul Mantle: compare antes.", "Loses Soul Mantle's Spirit/+1 totem: compare first."), L("Soul Mantle.", "Soul Mantle.")),
]
for u in UNIQUES:
    u["tier"] = {"Barato": L("Barato", "Cheap"), "Valor": L("Valor", "Value"), "Luxo": L("Luxo", "Luxury")}[u["tier"]] if False else u["tier"]

# ------------------------------------------------------------------ itens slot a slot
GEAR = [
 dict(slot=L("Main-hand", "Main-hand"), cheap=L("Atos 1–4: cajado com +Physical Spells. Troca: Attuned Wand com +Lightning/All Spells", "Acts 1–4: staff with +Physical Spells. Swap: Attuned Wand with +Lightning/All Spells"), value=L("Wand com +2/+3 Lightning ou All Spells", "Wand with +2/+3 Lightning or All Spells"), full=L("Dueling Wand (dá Spellslinger)", "Dueling Wand (grants Spellslinger)"), affix=L("+Level de spell > % Spell Damage > Cast Speed", "+Spell level > % Spell Damage > Cast Speed"), note=L("Depois da troca, é a wand que carrega os níveis de spell dos totems.", "After the swap, the wand carries the totems' spell levels.")),
 dict(slot="Offhand", cheap=L("Omen/Stoic Sceptre com 130+ Spirit", "Omen/Stoic Sceptre with 130+ Spirit"), value=L("Sceptre com mais Spirit", "Sceptre with more Spirit"), full=L("Sceptre com Spirit alto + mods de spell", "Sceptre with high Spirit + spell mods"), affix=L("Spirit > tudo", "Spirit > everything"), note=L("É a principal fonte de Spirit para os totems.", "It's the main Spirit source for the totems.")),
 dict(slot=L("Capacete", "Helmet"), cheap=L("Vida + resists", "Life + resists"), value=L("Runeforged (Runic Ward)", "Runeforged (Runic Ward)"), full=L("Rare com mana, Spirit e resists", "Rare with mana, Spirit and resists"), affix=L("Mana; vida; resist", "Mana; life; resist"), note=L("Runic Ward alimenta Grim Pillars, Bitter Dead e Repulsion.", "Runic Ward fuels Grim Pillars, Bitter Dead and Repulsion.")),
 dict(slot="Body Armour", cheap=L("Avian Robe com Spirit", "Avian Robe with Spirit"), value="Waveshaper", full="Soul Mantle", affix=L("Spirit; mana; ES", "Spirit; mana; ES"), note=L("Soul Mantle: +75 Spirit e +1 totem.", "Soul Mantle: +75 Spirit and +1 totem.")),
 dict(slot=L("Luvas", "Gloves"), cheap=L("Vida/resists", "Life/resists"), value=L("Runeforged (Runic Ward)", "Runeforged (Runic Ward)"), full=L("Rare com mana e resists", "Rare with mana and resists"), affix=L("Mana; resist", "Mana; resist"), note=""),
 dict(slot=L("Botas", "Boots"), cheap=L("10–15% MS", "10–15% MS"), value=L("25–30% MS + vida", "25–30% MS + life"), full=L("30% MS + mana + resists", "30% MS + mana + resists"), affix=L("Movement Speed primeiro", "Movement Speed first"), note=""),
 dict(slot=L("Amuleto", "Amulet"), cheap=L("Solar Amulet com Spirit", "Solar Amulet with Spirit"), value=L("Spirit ou +níveis de spell", "Spirit or +spell levels"), full=L("Amuleto de Archmage craftado (Spirit/Spell Level fracturado + mana + Kurgal)", "Crafted Archmage amulet (fractured Spirit/Spell Level + mana + Kurgal)"), affix=L("Spirit; +Spell Level; mana", "Spirit; +Spell Level; mana"), note=L("O custo depende da base e das tentativas. Veja as rotas e o simulador na aba Crafting.", "Cost depends on the base and attempts. See routes and the simulator in Crafting.")),
 dict(slot=L("Anéis", "Rings"), cheap=L("Vida/resists/mana", "Life/resists/mana"), value=L("Mana + resists", "Mana + resists"), full=L("Rares com mana e resists", "Rares with mana and resists"), affix=L("Resists; mana", "Resists; mana"), note=""),
 dict(slot=L("Cinto", "Belt"), cheap=L("Vida/resists", "Life/resists"), value=L("Heavy Belt com vida/resists", "Heavy Belt with life/resists"), full=L("Rare com mana/vida/resists", "Rare with mana/life/resists"), affix=L("Resists", "Resists"), note=""),
 dict(slot="Charms", cheap=L("Thawing, Antidote, Sapphire", "Thawing, Antidote, Sapphire"), value="Breath of the Mountains", full=L("The Fall of the Axe · Nascent Hope · Arakaali's Gift", "The Fall of the Axe · Nascent Hope · Arakaali's Gift"), affix=L("Cobrir freeze/poison/slow", "Cover freeze/poison/slow"), note=""),
 dict(slot="Flasks", cheap=L("Vida + mana", "Life + mana"), value=L("Ultimate/Transcendent Mana Flask", "Ultimate/Transcendent Mana Flask"), full="Lavianga's Spirits", affix=L("Recuperação de mana", "Mana recovery"), note=""),
]
BUY_ORDER = [
 dict(p=1, item=L("Sceptre com 130+ Spirit", "Sceptre with 130+ Spirit"), phase=L("Ato 3–4", "Acts 3–4"), cost=L("Barato", "Cheap"), impact=L("Libera a troca para totem", "Unlocks the totem swap")),
 dict(p=2, item=L("Wand com +Lightning/All Spells", "Wand with +Lightning/All Spells"), phase=L("Ato 4", "Act 4"), cost=L("Barato", "Cheap"), impact=L("Dano dos totems", "Totem damage")),
 dict(p=3, item=L("Amuleto e body com Spirit", "Amulet and body with Spirit"), phase=L("Troca", "Swap"), cost=L("Barato", "Cheap"), impact=L("Mais um totem", "One more totem")),
 dict(p=4, item="Waveshaper", phase=L("Início do Atlas", "Early Atlas"), cost=L("Barato", "Cheap"), impact=L("Spirit + mana vira Armour", "Spirit + mana becomes Armour")),
 dict(p=5, item=L("Peças Runeforged", "Runeforged pieces"), phase=L("Atlas", "Atlas"), cost=L("Barato", "Cheap"), impact=L("Runic Ward para Grim Pillars", "Runic Ward for Grim Pillars")),
 dict(p=6, item="Soul Mantle", phase=L("Atlas", "Atlas"), cost=L("Valor", "Value"), impact=L("+75 Spirit e +1 totem", "+75 Spirit and +1 totem")),
 dict(p=7, item="Lavianga's Spirits", phase=L("Endgame", "Endgame"), cost=L("Valor", "Value"), impact=L("Mana constante", "Constant mana")),
 dict(p=8, item=L("Amuleto de Archmage craftado", "Crafted Archmage amulet"), phase=L("Endgame final", "Final endgame"), cost=L("Alto; simule o orçamento", "High; model your budget"), impact=L("Teto de dano e Spirit", "Damage and Spirit ceiling")),
]

# ------------------------------------------------------------------ tricks
TRICKS = [
 {"cat": L("Totem", "Totem"), "lvl": L("Fácil", "Easy"), "title": L("Você paga só a mana do totem", "You only pay the totem's mana"), "body": L("Com Ancestral Bond, colocar o Spell Totem custa a mana do totem; os spells que ele lança não custam a sua mana. Por isso dá para usar spells caros nos totems.", "With Ancestral Bond, placing Spell Totem costs the totem's mana; the spells it casts don't cost your mana. That's why expensive spells work in totems.")},
 {"cat": L("Totem", "Totem"), "lvl": L("Médio", "Medium"), "title": L("Limite de totems (dados do jogo)", "Totem limit (game data)"), "body": L("Gem do Spell Totem: 1 totem até o nível 13, 2 a partir do 14. Unnamed Heartwood e Soul Mantle: +1 cada. Ancestral Bond dobra o total. Cada totem reserva 75 Spirit (62,5 com Efficient Inscriptions).", "Spell Totem gem: 1 totem up to level 13, 2 from level 14. Unnamed Heartwood and Soul Mantle: +1 each. Ancestral Bond doubles the total. Each totem reserves 75 Spirit (62.5 with Efficient Inscriptions).")},
 {"cat": L("Totem", "Totem"), "lvl": L("Fácil", "Easy"), "title": L("Boss: desligue o Mana Remnants", "Boss: turn off Mana Remnants"), "body": L("Dica do próprio Lowepe: para mapear 2 totems bastam; no boss você pode desligar o Mana Remnants (30 Spirit) para colocar mais um totem — boss não solta Remnants.", "Lowepe's own tip: 2 totems are enough for mapping; on bosses you can turn off Mana Remnants (30 Spirit) to place one more totem — bosses don't drop Remnants.")},
 {"cat": L("Totem", "Totem"), "lvl": L("Médio", "Medium"), "title": L("Weapon sets", "Weapon sets"), "body": L("Set 1 = Spell Totem + Archmage e as passivas de totem. Set 2 = Entangle, Frost Bomb, Elemental Weakness. Nos dois: Mana Tempest e Mana Remnants. As passivas de weapon set só valem com o set ativo.", "Set 1 = Spell Totem + Archmage and the totem passives. Set 2 = Entangle, Frost Bomb, Elemental Weakness. On both: Mana Tempest and Mana Remnants. Weapon-set passives only apply with that set active.")},
 {"cat": L("Dano", "Damage"), "lvl": L("Fácil", "Easy"), "title": L("Frost Bomb antes do Spark", "Frost Bomb before Spark"), "body": L("Frost Bomb deixa uma Cold Infusion quando explode; o Spark consome Cold Infusion para lançar várias faíscas em círculo.", "Frost Bomb leaves a Cold Infusion when it detonates; Spark consumes Cold Infusion to fire many sparks in a circle.")},
 {"cat": L("Dano", "Damage"), "lvl": L("Fácil", "Easy"), "title": L("Spark pela Flame Wall", "Spark through Flame Wall"), "body": L("Projéteis que passam pela Flame Wall ganham dano de fogo. Coloque o muro entre os totems e os inimigos.", "Projectiles passing through Flame Wall gain fire damage. Put the wall between the totems and the enemies.")},
 {"cat": L("Dano", "Damage"), "lvl": L("Médio", "Medium"), "title": L("Zenith precisa de 90% de mana", "Zenith needs 90% mana"), "body": L("Zenith I/II só dão o dano extra acima de 90% da mana máxima. Mana Remnants, Clarity II e Lavianga's Spirits existem para manter a mana cheia.", "Zenith I/II only grant the extra damage above 90% of maximum mana. Mana Remnants, Clarity II and Lavianga's Spirits exist to keep mana full.")},
 {"cat": L("Dano", "Damage"), "lvl": L("Médio", "Medium"), "title": L("Pierce II x Branching Bolts", "Pierce II vs Branching Bolts"), "body": L("O Lowepe permite Pierce II no Spark, mas aí NÃO pegue Branching Bolts na árvore (60% de chance de encadear mais uma vez).", "Lowepe allows Pierce II on Spark, but then do NOT take Branching Bolts on the tree (60% chance to chain one more time).")},
 {"cat": L("Dano", "Damage"), "lvl": L("Avançado", "Advanced"), "title": L("Grim Pillars gasta Runic Ward", "Grim Pillars spends Runic Ward"), "body": L("Grim Pillars, Bitter Dead e Repulsion custam Runic Ward, não mana. Sem itens Runeforged/Runemastered o totem não consegue lançar.", "Grim Pillars, Bitter Dead and Repulsion cost Runic Ward, not mana. Without Runeforged/Runemastered items the totem can't cast them.")},
 {"cat": L("Dano", "Damage"), "lvl": L("Fácil", "Easy"), "title": L("Entangle ativa os pilares", "Entangle sets off the pillars"), "body": L("Com Grim Pillars, a build vira 2 botões: os totems criam os pilares e o Entangle faz eles explodirem.", "With Grim Pillars the build becomes 2 buttons: totems create the pillars and Entangle makes them explode.")},
 {"cat": L("Mana", "Mana"), "lvl": L("Médio", "Medium"), "title": L("Archmage + Mind Over Matter", "Archmage + Mind Over Matter"), "body": L("Archmage transforma mana máxima em dano de raio extra (e aumenta o custo). Mind Over Matter usa a mesma mana como defesa. Mais mana = mais dano e mais vida efetiva.", "Archmage turns maximum mana into extra lightning damage (and raises cost). Mind Over Matter uses that same mana as defence. More mana = more damage and more effective life.")},
 {"cat": L("Mana", "Mana"), "lvl": L("Fácil", "Easy"), "title": L("Mana Tempest por último", "Mana Tempest last"), "body": L("O Mana Tempest drena mana enquanto está ativo. Coloque totems, curse e Frost Bomb primeiro; a tempestade entra por último no boss.", "Mana Tempest drains mana while active. Place totems, curse and Frost Bomb first; the storm goes in last on the boss.")},
 {"cat": "0.5.5", "lvl": L("Fácil", "Easy"), "title": L("Grim Pillars só a partir do Ato 4", "Grim Pillars only from Act 4"), "body": L("No 0.5.5, Remnants e Expedition só aparecem a partir do Ato 4: antes disso não tem como conseguir Grim Pillars. O Lowepe recomenda adiar a troca e jogar com Spark enquanto isso.", "In 0.5.5, Remnants and Expedition only appear from Act 4: before that there's no way to get Grim Pillars. Lowepe recommends delaying and playing Spark meanwhile.")},
 {"cat": L("Economia", "Economy"), "lvl": L("Fácil", "Easy"), "title": L("Regex de vendor", "Vendor regex"), "body": "\"([32]0|25)% i.+mov|^\\+.*ng sp.*ls$|^\\+.*al sp.*ls$|spiri\""},
 {"cat": L("Economia", "Economy"), "lvl": L("Fácil", "Easy"), "title": L("Gold para o respec", "Gold for the respec"), "body": L("A troca para totem precisa de bastante gold. No Ato 4 venda rares identificados e não gaste à toa.", "The totem swap needs a lot of gold. In Act 4 sell identified rares and don't waste gold.")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Segure os canalizados", "Hold the channelled skills"), "body": L("Volcano e Bonestorm são canalizados e têm Burgeon: soltar cedo demais corta muito o dano.", "Volcano and Bonestorm are channelled and use Burgeon: releasing too early cuts damage a lot.")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Thunderstorm + Entangle", "Thunderstorm + Entangle"), "body": L("Segundo o Lowepe, o Thunderstorm não só dá Shock como também aumenta a duração do Entangle. Use primeiro.", "Per Lowepe, Thunderstorm not only Shocks but also extends Entangle's duration. Cast it first.")},
 {"cat": L("Defesa", "Defence"), "lvl": L("Médio", "Medium"), "title": L("Soul Mantle e curses", "Soul Mantle and curses"), "body": L("Quando um totem morre com a Soul Mantle, você ganha uma curse aleatória. Coloque os totems fora da linha de fogo do boss.", "When a totem dies with Soul Mantle equipped you get a random curse. Place totems out of the boss's line of fire.")},
]

TROUBLESHOOT = [
 (L("Só consigo colocar 2 totems", "I can only place 2 totems"), L("Veja o limite: gem do Spell Totem nível 14+ (2 base) ou Unnamed Heartwood/Soul Mantle (+1), dobrado pelo Ancestral Bond. Depois veja o Spirit: 75 por totem (62,5 com Efficient Inscriptions). Desligue o Mana Remnants no boss para caber mais um.", "Check the limit: Spell Totem gem level 14+ (2 base) or Unnamed Heartwood/Soul Mantle (+1), doubled by Ancestral Bond. Then check Spirit: 75 per totem (62.5 with Efficient Inscriptions). Turn off Mana Remnants on bosses to fit one more.")),
 (L("O totem não aparece / pede charges", "The totem won't place / asks for charges"), L("Sem Ancestral Bond o Spell Totem consome 3 Power/Endurance Charges. Pegue o Ancestral Bond na árvore.", "Without Ancestral Bond, Spell Totem consumes 3 Power/Endurance Charges. Take Ancestral Bond on the tree.")),
 (L("Grim Pillars não sai do totem", "Grim Pillars won't come out of the totem"), L("Grim Pillars e Bitter Dead gastam Runic Ward. Equipe peças Runeforged/Runemastered.", "Grim Pillars and Bitter Dead spend Runic Ward. Equip Runeforged/Runemastered pieces.")),
 (L("Dano caiu depois da troca", "Damage dropped after the swap"), L("Provavelmente faltou Spirit (menos totems) ou a wand não tem +níveis de spell. O Lowepe recomenda ficar o máximo possível no setup anterior.", "Probably not enough Spirit (fewer totems) or the wand lacks +spell levels. Lowepe recommends staying on the previous setup as long as possible.")),
 (L("Mana acaba", "Running out of mana"), L("Mana Remnants ativo, Clarity II, Efficiency nos skills próprios, Lavianga's Spirits. Não abra o Mana Tempest antes de colocar tudo.", "Mana Remnants active, Clarity II, Efficiency on self-cast skills, Lavianga's Spirits. Don't open Mana Tempest before placing everything.")),
 (L("Zenith não dá dano", "Zenith gives no damage"), L("Ele só funciona acima de 90% de mana. Com Archmage o custo sobe: aumente regeneração/mana.", "It only works above 90% mana. With Archmage the cost goes up: raise regeneration/mana.")),
 (L("Morro com Mind Over Matter", "Dying with Mind Over Matter"), L("A mana precisa ser bem maior que a vida e ter recuperação (Mana Remnants, Lavianga's). Harmony Within só protege se a mana atual for maior que a vida atual.", "Mana must be much higher than life and have recovery (Mana Remnants, Lavianga's). Harmony Within only protects when current mana is higher than current life.")),
 (L("Totems morrem no boss", "Totems die on bosses"), L("Coloque longe dos ataques em área. Com Soul Mantle cada totem morto te dá uma curse aleatória.", "Place them away from area attacks. With Soul Mantle every dead totem gives you a random curse.")),
]

ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Resists no cap · 3–4 totems", "Resists capped · 3–4 totems"), gear=L("Waveshaper + sceptre de Spirit", "Waveshaper + Spirit sceptre")),
 dict(stage="T1–T10", goal=L("Runic Ward nas armaduras", "Runic Ward on armour"), gear=L("Peças Runeforged", "Runeforged pieces")),
 dict(stage="T11–T15", goal=L("Grim Pillars + Bitter Dead", "Grim Pillars + Bitter Dead"), gear="Soul Mantle"),
 dict(stage=L("Pinnacle", "Pinnacle"), goal=L("Archmage + Mind Over Matter", "Archmage + Mind Over Matter"), gear=L("Amuleto de Archmage + Lavianga's", "Archmage amulet + Lavianga's")),
]

CRAFT = [
 L("Defina Spirit, mana e níveis de spell necessários para o seu setup; abra Crafting para os tiers e ilvl.", "Set the Spirit, mana and spell levels your setup needs; open Crafting for tiers and item level."),
 L("Compare uma base já fracturada com o custo total de prepará-la. Uma fratura errada exige outra base.", "Compare an already fractured base against the full preparation cost. A wrong fracture requires another base."),
 L("Conte prefixos, sufixos e famílias antes de cada operação. Perfect Exalted e omens não garantem mana T1.", "Count prefixes, suffixes and families before each operation. Perfect Exalted and omens do not guarantee T1 mana."),
 L("Planeje a tentativa de Kurgal, o custo de repetir e um limite de gastos. Confira o roteiro completo na aba Crafting.", "Plan the Kurgal attempt, retry costs and a spending limit. Check the full route in the Crafting tab."),
]

# ------------------------------------------------------------------ quando usar
def req_text(n):
    import importlib.util, sys
    return None

TIMING = []
def T(kind, n, lvl, req, when, gives, early, late, steps=(), watch=()):
    TIMING.append(dict(kind=kind, n=n, lvl=lvl, req=req, when=when, gives=gives, early=early, late=late, steps=list(steps), watch=list(watch)))

T("item", L("Sceptre com 130+ Spirit", "Sceptre with 130+ Spirit"), 1, L("Omen/Stoic Sceptre rare", "Rare Omen/Stoic Sceptre"), L("Compre no Ato 3–4 e guarde para a troca.", "Buy in Acts 3–4 and keep it for the swap."), L("A maior fonte de Spirit para os totems.", "The biggest Spirit source for the totems."),
  L("Conseguiu cedo? Ótimo: guarde. A troca exige 210+ Spirit total.", "Got it early? Great: keep it. The swap needs 210+ total Spirit."), L("Sem ele não faça a troca: poucos totems e dano menor que o leveling.", "Without it don't swap: few totems and less damage than leveling."),
  [L("Equipe na offhand quando fizer a troca (a wand vai na main-hand).", "Equip in the offhand at the swap (the wand goes in the main hand).")])
T("item", L("Wand com +Lightning/All Spells", "Wand with +Lightning/All Spells"), 1, L("Attuned Wand rare (ou Dueling Wand)", "Rare Attuned Wand (or Dueling Wand)"), L("Na troca.", "At the swap."), L("+níveis de spell para o Spark dos totems.", "+spell levels for the totems' Spark."),
  L("Guarde até a troca: antes disso o cajado de Physical Spells rende mais.", "Keep it until the swap: before that the Physical Spells staff is better."), L("Qualquer wand com +níveis de Lightning ou All Spells.", "Any wand with +levels to Lightning or All Spells."))
T("item", "Dueling Wand", 1, L("Tipo base (rare)", "Base type (rare)"), L("Endgame final.", "Final endgame."), L("Concede o Spellslinger.", "Grants Spellslinger."),
  L("Pode usar antes, mas o Spellslinger reserva Spirit: só vale se sobrar depois dos totems.", "Usable earlier, but Spellslinger reserves Spirit: only worth it with spare Spirit after the totems."), L("Attuned Wand continua boa.", "Attuned Wand is still good."))
T("item", "Soul Mantle", 1, L("Confira o nível no item", "Check the level on the item"), L("Semana 1 do Atlas.", "Atlas week 1."), L("+75 Spirit e +1 totem.", "+75 Spirit and +1 totem."),
  L("Conseguiu antes da troca? Guarde: na troca ela vale por um Unnamed Heartwood + 1 totem de Spirit.", "Got it before the swap? Keep it: at the swap it's worth an Unnamed Heartwood + one totem's Spirit."), L("Use Unnamed Heartwood na ascendência.", "Use Unnamed Heartwood on the ascendancy."),
  [L("Com ela, dá para trocar Unnamed Heartwood por Harmony Within.", "With it, you can swap Unnamed Heartwood for Harmony Within.")], [L("Totem morto = curse aleatória em você.", "Dead totem = random curse on you.")])
T("item", "Waveshaper", 1, L("Confira o nível no item", "Check the level on the item"), L("Início do Atlas.", "Early Atlas."), L("Spirit, ES, resists e mana vira Armour.", "Spirit, ES, resists and mana becomes Armour."),
  L("Serve logo na troca se o nível permitir.", "Works right at the swap if the level allows."), L("Avian Robe/body rare com Spirit.", "Avian Robe/rare body with Spirit."))
T("item", L("Peças Runeforged (Runic Ward)", "Runeforged pieces (Runic Ward)"), 1, L("Helmet/gloves/boots Runeforged ou Runemastered", "Runeforged or Runemastered helmet/gloves/boots"), L("Antes de colocar Grim Pillars.", "Before slotting Grim Pillars."), L("Runic Ward: o recurso de Grim Pillars, Bitter Dead e Repulsion.", "Runic Ward: the resource for Grim Pillars, Bitter Dead and Repulsion."),
  L("Sem Grim Pillars ainda não fazem diferença.", "Without Grim Pillars they make no difference yet."), L("Sem elas, fique no Spark.", "Without them, stay on Spark."))
T("item", L("Amuleto de Archmage", "Archmage amulet"), None, L("Requisito para equipar: confira o item. ilvl dos mods: veja Crafting.", "Equip requirement: check the item. Modifier ilvl: see Crafting."), L("Endgame final.", "Final endgame."), L("Spirit/Spell Level + mana + Kurgal + Mana before Life.", "Spirit/Spell Level + mana + Kurgal + Mana before Life."),
  L("Defina o limite de gastos e compare uma peça pronta antes de começar.", "Set a spending limit and compare a finished item before starting."), L("Solar Amulet com Spirit.", "Solar Amulet with Spirit."))
T("item", "Lavianga's Spirits", 49, L("Nível 49", "Level 49"), L("Com Mind Over Matter/Archmage.", "With Mind Over Matter/Archmage."), L("Flask de mana constante.", "Constant mana flask."), L("Antes do MoM ajuda pouco.", "Before MoM it helps little."), "—")
T("skill", "Grim Pillars", 40, L("Skill de Expedition — só a partir do Ato 4 (0.5.5)", "Expedition skill — only from Act 4 (0.5.5)"), L("Atlas, com Runic Ward.", "Atlas, with Runic Ward."), L("Pilares de gelo que explodem; gasta Runic Ward.", "Exploding ice pillars; spends Runic Ward."),
  L("Achou cedo? Guarde até ter Runic Ward nas armaduras; enquanto isso, Spark.", "Found it early? Keep it until you have Runic Ward on armour; meanwhile, Spark."), L("Spark nos totems funciona até o endgame.", "Spark in totems works until endgame."),
  [L("Spell Totem: Grim Pillars + Magnified Area II + Urgent Totems III + Cold Mastery + Bitter Dead.", "Spell Totem: Grim Pillars + Magnified Area II + Urgent Totems III + Cold Mastery + Bitter Dead."), L("Entangle no Weapon Set 2 para ativar os pilares.", "Entangle on Weapon Set 2 to set off the pillars.")])
T("skill", "Bitter Dead", 40, L("Skill de Expedition, gasta Runic Ward", "Expedition skill, spends Runic Ward"), L("Junto com Grim Pillars.", "Together with Grim Pillars."), L("Corpos viram núcleos que dão Chill e explodem.", "Corpses become cores that Chill and explode."), "—", "—")
T("skill", "Archmage", 1, L("Reserva 100 Spirit", "Reserves 100 Spirit"), L("Quando os totems e o Mana Remnants já couberem.", "Once totems and Mana Remnants already fit."), L("Dano de raio extra baseado na mana máxima (e mais custo).", "Extra lightning damage based on maximum mana (and higher cost)."),
  L("Antes de ter mana alta, os 100 Spirit rendem mais como mais um totem.", "Before high mana, those 100 Spirit are worth more as another totem."), "—")
T("skill", "Mana Tempest", 1, L("Não reserva Spirit (drena mana)", "Reserves no Spirit (drains mana)"), L("Início do Atlas, em bosses.", "Early Atlas, on bosses."), L("Empower nos spells que custam mana dentro da tempestade.", "Empowers mana-costing spells inside the storm."), L("Use por último.", "Use it last."), "—")
T("asc", "Unnamed Heartwood", 52, L("Ascendência Oracle", "Oracle ascendancy"), L("Na troca.", "At the swap."), L("+1 totem (vira +2 com Ancestral Bond).", "+1 totem (becomes +2 with Ancestral Bond)."),
  L("Antes da troca não faz nada.", "Before the swap it does nothing."), L("Sem ele e sem Soul Mantle, o limite depende da gem nível 14+.", "Without it and without Soul Mantle, the limit depends on a level 14+ gem."))
T("asc", "Forced Outcome", 34, L("Ascendência Oracle", "Oracle ascendancy"), L("2º Trial.", "2nd Trial."), L("Inevitable Critical Hits.", "Inevitable Critical Hits."), "—", "—")
T("asc", "Harmony Within", 78, L("Ascendência Oracle", "Oracle ascendancy"), L("Semana 1 do Atlas.", "Atlas week 1."), L("Dano de hit sai da mana se mana atual > vida atual; 15% less vida e mana.", "Hit damage from mana if current mana > current life; 15% less life and mana."),
  L("Só vale com mana maior que a vida.", "Only worth it with mana above life."), "—")
T("key", "Ancestral Bond", 51, L("Keystone da árvore", "Tree keystone"), L("Na troca — sempre.", "At the swap — forever."), L("Limite de totems dobrado, sem charges, 75 Spirit por totem.", "Doubled totem limit, no charges, 75 Spirit per totem."),
  L("Sem 210+ Spirit, pegar cedo só deixa 1–2 totems.", "Without 210+ Spirit, taking it early only leaves 1–2 totems."), L("Sem ele o Spell Totem exige 3 charges por totem.", "Without it Spell Totem needs 3 charges per totem."))
T("key", "Efficient Inscriptions", 51, L("Notable da árvore", "Tree notable"), L("Na troca, se tiver menos de 255 Spirit.", "At the swap, if you have under 255 Spirit."), L("Totems 75 → 62,5 Spirit.", "Totems 75 → 62.5 Spirit."), "—", "—")
T("key", "Mind Over Matter", 75, L("Keystone da árvore", "Tree keystone"), L("Endgame (dá para testar depois da troca).", "Endgame (can be tried after the swap)."), L("Todo dano sai da mana antes da vida; 50% less recuperação de mana.", "All damage from mana before life; 50% less mana recovery."),
  L("Com pouca mana, é perigoso: teste Mental Perseverance antes.", "With low mana it's dangerous: try Mental Perseverance first."), "—")

CASES = [
 (L("Tenho Spirit mas ainda estou no Ato 3", "I have Spirit but I'm still in Act 3"), L("Pode trocar mais cedo se tiver 210+ Spirit, a wand e os pontos. Mas o Lowepe recomenda ficar o máximo possível no setup anterior: a troca só é boa quando cabem 3+ totems.", "You can swap earlier with 210+ Spirit, the wand and the points. But Lowepe recommends staying on the previous setup as long as possible: the swap is only good when 3+ totems fit.")),
 (L("Cheguei nos Interlúdios sem Spirit suficiente", "I reached the Interludes without enough Spirit"), L("Continue no setup do Ato 4 (Bonestorm/Entangle). Selecione 'Ato 4' em 'Onde você está' até juntar o Spirit. Lythara (+40) está nos Interlúdios.", "Stay on the Act 4 setup (Bonestorm/Entangle). Pick 'Act 4' in 'Where you are' until you gather the Spirit. Lythara (+40) is in the Interludes.")),
 (L("Achei Grim Pillars antes do Atlas", "I found Grim Pillars before the Atlas"), L("Guarde. Precisa de Runic Ward (peças Runeforged) para lançar; até lá use Spark.", "Keep it. It needs Runic Ward (Runeforged pieces) to cast; until then use Spark.")),
 (L("Tenho Soul Mantle cedo", "I have Soul Mantle early"), L("Na troca, ela dá +75 Spirit e +1 totem: você pode pular o Unnamed Heartwood e pegar outra ascendência.", "At the swap it gives +75 Spirit and +1 totem: you can skip Unnamed Heartwood and take another ascendancy.")),
 (L("Não tenho Efficient Inscriptions", "I don't have Efficient Inscriptions"), L("Então precisa de 255 Spirit para 3 totems + Mana Remnants (3×75 + 30).", "Then you need 255 Spirit for 3 totems + Mana Remnants (3×75 + 30).")),
]

QUEST_PRIO = {"+30 Spirit": "CRÍTICA", "+40 Spirit": "CRÍTICA"}

SOURCES = [
 dict(name="Lowepe — [0.5.5] Oracle Spell-Totem Spark/Grim Pillars (Mobalytics)", use=L("Build base: 9 variantes, gems, itens, árvore, notas e craft", "Base build: 9 variants, gems, items, tree, notes and craft"), url=GUIDE_URL),
 dict(name="Path of Building (PoE2) — Gems.lua, Skills, ModCache", use=L("Nomes, descrições, custos de Spirit e limite de totems", "Names, descriptions, Spirit costs and totem limit"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name=L("Árvore 0.5 (Path of Building)", "0.5 tree (Path of Building)"), use=L("Nós, ascendência Oracle e keystones", "Nodes, Oracle ascendancy and keystones"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name="poe.ninja — Forbidden Rites", use=L("Preços dos uniques", "Unique prices"), url="https://poe.ninja/poe2/economy"),
]
FIXES = [
 L("A variante final não usa Unnamed Heartwood nem Soul Mantle: o limite vem da gem do Spell Totem nível 14+ (2 base) × Ancestral Bond — confirmado nos dados da gem.", "The final variant uses neither Unnamed Heartwood nor Soul Mantle: the limit comes from the level 14+ Spell Totem gem (2 base) × Ancestral Bond — confirmed in the gem data."),
 L("Os custos de Spirit do Malice e do Spellslinger não estão nos dados do Path of Building: o guia manda conferir no jogo.", "Malice and Spellslinger Spirit costs aren't in Path of Building's data: the guide tells you to check in game."),
 L("\"The Unseen Path\" (Walk the Paths Not Taken) não tem efeito detalhado nos dados: leia o tooltip.", "\"The Unseen Path\" (Walk the Paths Not Taken) has no detailed effect in the data: read the tooltip."),
]

TOTEM_MANA = {1: 18, 5: 30, 10: 51, 13: 68, 14: 74, 15: 81, 16: 88, 17: 95, 18: 103, 19: 112, 20: 121}

def build(QUESTS_PT):
    quests = []
    for q in QUESTS_PT:
        q = dict(q)
        if q["boss"] == "Mighty Silverfist":
            q["reward"] = "2 Weapon Set Passive Points"; q["prio"] = "Alta"
        if q["boss"] == "Venom Draught":
            q["reward"] = L("ESCOLHA: 25% increased Mana Regeneration Rate (Lowepe)", "CHOICE: 25% increased Mana Regeneration Rate (Lowepe)"); q["prio"] = "Média"
        if q["boss"] == "Tribal Medicine":
            q["reward"] = L("ESCOLHA (o Lowepe não especifica)", "CHOICE (Lowepe doesn't specify)"); q["prio"] = "Média"
        if q["boss"] == "Tabana's Pillar":
            q["reward"] = L("ESCOLHA: 3% increased Movement Speed (Lowepe)", "CHOICE: 3% increased Movement Speed (Lowepe)")
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="15/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=GUIDE_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, totemMana=TOTEM_MANA, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None)

L("Flask vida", "Life flask"); L("Flask mana", "Mana flask"); L("Barato", "Cheap"); L("Valor", "Value"); L("Luxo", "Luxury")
L("Soul Core/runa de resistência que faltar", "Whatever resistance Soul Core/rune you're missing"); L("Runa de resistência que faltar", "Whatever resistance rune you're missing")
L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio) · resist no cap: Body Rune (vida)", "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning) · resists capped: Body Rune (life)")
