# -*- coding: utf-8 -*-
"""Tactician Pin2Win Grenades — dados da página (PT com pares EN). Base: guia do BlazeworksTV (Mobalytics, 0.5.5),
árvore/gems/itens das variantes do guia, textos do jogo pelo Path of Building e preços do poe.ninja (Forbidden Rites)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("tactician")

GUIDE_URL = "https://mobalytics.gg/poe-2/builds/pin-to-win-blazeworks"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "17/09/2026"

CONFIG = dict(dir="tactician", build="tactician", store="tactician1", emoji="💣", pill="Mercenary · Tactician",
              fonts="family=Cinzel:wght@500;700;900&family=Oswald:wght@500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400")
TXT = {
 "pt": dict(TITLE="Tactician das Granadas", DESC="Guia interativo Tactician Pin2Win Grenades (Mercenary) — PoE 2 Forbidden Rites",
            H1S="Pin2Win Grenades · crossbow do nível 1 ao T15 · guia do BlazeworksTV explicado", H1="O Tactician das Granadas",
            LEAD="Prenda os inimigos no lugar com Pin e exploda tudo com granadas de fogo, gás e óleo. Do Ato 1 ao Trarthan Cannon e à Siege Crossbow: diga seu nível e o que você tem, e o guia mostra skills, crossbow da fase, passivas e o Spirit das suas auras."),
 "en": dict(TITLE="Grenade Tactician", DESC="Interactive Tactician Pin2Win Grenades (Mercenary) guide — PoE 2 Forbidden Rites",
            H1S="Pin2Win Grenades · crossbow from level 1 to T15 · BlazeworksTV's guide explained", H1="The Grenade Tactician",
            LEAD="Pin enemies in place and blow everything up with fire, gas and oil grenades. From Act 1 to the Trarthan Cannon and the Siege Crossbow: tell it your level and what you have, and the guide shows skills, the crossbow for your phase, passives and your buffs' Spirit."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["quando", "Quando usar", "When to use"], ["mech", "Pin & Granadas", "Pin & Grenades"],
        ["uniques", "Uniques", "Uniques"], ["arvore", "Árvore de Passivas", "Passive Tree"], ["rota", "Rota 1→100", "Route 1→100"], ["skills", "Skills & Supports", "Skills & Supports"],
        ["gear", "Itens", "Items"], ["asc", "Ascendência", "Ascendancy"], ["quests", "Quests", "Quests"], ["tricks", "Tricks Pro", "Pro Tricks"], ["atlas", "Atlas", "Atlas"],
        ["diag", "Diagnóstico", "Troubleshooting"], ["fontes", "Fontes", "Sources"]]

CLASS, ASC, START = "Mercenary", "Tactician", 50986
ORDER = ["a1", "a2", "a3", "int", "cannon", "t15", "max"]
VMAP = {"a1": "Act 1", "a2": "Act 2", "a3": "Act 3 & 4", "int": "Interludes (Level 52-60)", "cannon": "Level 65+ Trarthan Cannon Endgame",
        "t15": "Current Endgame Setup (T15)", "max": "Uber Endgame - Aspirational Gear"}
VITEMS = {"cannon": ["Interludes (Level 52-60)", "Level 65+ Trarthan Cannon Endgame"]}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "int": "int", "cannon": "cannon", "t15": "cannon", "max": "t15"}
FULLMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "int": "int", "cannon": "cannon", "t15": "t15", "max": "max"}
SKIP_ITEMS = {"Punch"}
PHASE_ACT = {"a1": 1, "a2": 2, "a3": 3, "int": 5, "cannon": 6, "t15": 6, "max": 6}

XB_RUNE = L("Iron Rune (% dano físico) ou Storm Rune (raio para Shock)", "Iron Rune (% physical damage) or Storm Rune (lightning for Shock)")
def socket_hint(slot, name):
    if "Crossbow" in name or "Cannon" in name:
        return [XB_RUNE]
    if slot in ("Capacete", "Body Armour", "Luvas", "Botas"):
        return [L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio) · resist no cap: Body Rune (vida)", "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning) · resists capped: Body Rune (life)")]
    return None

# ------------------------------------------------------------------ supports
SUPWHY = {
 "Multishot I": L("Dispara projéteis extras. Na granada, são mais granadas por uso — mais área e mais Pin, em troca de um pouco de dano e velocidade.", "Fires extra projectiles. On a grenade that means more grenades per use — more area and more Pin, at the cost of some damage and speed."),
 "Multishot II": L("Versão mais forte do Multishot: mais granadas por uso. É o support que mais aumenta o clear das granadas.", "Stronger Multishot: more grenades per use. It's the support that raises grenade clear the most."),
 "Elemental Armament I": L("More dano elemental nos ataques. As granadas de fogo escalam direto com ele.", "More elemental damage on attacks. Fire grenades scale straight off it."),
 "Elemental Armament II": L("Versão mais forte do Elemental Armament: more dano de fogo nas granadas.", "Stronger Elemental Armament: more fire damage on your grenades."),
 "Pin I": L("O dano físico passa a acumular Pin (prende o inimigo no lugar), mas o skill deixa de dar Stun. Na Flash Grenade, é o Pin do início do jogo.", "Physical damage builds Pin (holds the enemy in place), but the skill can no longer Stun. On Flash Grenade it's your early-game Pin."),
 "Pin II": L("Pin mais forte e chance de crítico extra contra inimigos imobilizados (Pinned conta).", "Stronger Pin plus extra critical chance against Immobilised enemies (Pinned counts)."),
 "Double Barrel II": L("Carrega um virote extra no Explosive Shot, com recarga mais lenta: mais detonações por pente.", "Loads an extra bolt into Explosive Shot at the cost of reload speed: more detonations per clip."),
 "Rapid Attacks II": L("Ataca mais rápido: o Explosive Shot detona suas granadas antes.", "Attacks faster: Explosive Shot detonates your grenades sooner."),
 "Mark for Death": L("O Mark do Pounce faz o dano físico quebrar Armour do alvo. Com Eroding Chains e The Molten One's Gift, Armour quebrada vira dano de fogo extra.", "Pounce's Mark makes physical damage break the target's Armour. With Eroding Chains and The Molten One's Gift, broken Armour becomes extra fire damage."),
 "Mark of Siphoning": L("Inimigos marcados dão Mana Leech quando você acerta ataques neles. Resolve mana no boss.", "Marked enemies give Mana Leech when you hit them with attacks. Solves mana on bosses."),
 "Deliberation": L("Você anda mais devagar enquanto usa o skill, mas ele causa mais dano. Nas granadas o custo é pequeno: você lança e já se move.", "You move slower while using the skill, but it deals more damage. On grenades the cost is small: you throw and keep moving."),
 "Payload": L("Chance de a granada ativar de novo, em troca de cooldown maior. Mais explosões por uso na Explosive Grenade.", "Chance for the grenade to activate again, at the cost of a longer cooldown. More explosions per use on Explosive Grenade."),
 "Potent Exposure": L("Aumenta a Exposure que a Oil Grenade aplica: os inimigos perdem mais resistência elemental.", "Increases the Exposure Oil Grenade applies: enemies lose more elemental resistance."),
 "Persistent Ground I": L("O óleo no chão dura muito mais: dá tempo de colocar as outras granadas e acender tudo.", "Oil on the ground lasts much longer: time to throw your other grenades and light it all up."),
 "Persistent Ground II": L("O óleo só acaba quando a duração termina (não some ao ser aceso).", "Oil only ends when its duration runs out (it doesn't vanish when ignited)."),
 "Persistent Ground III": L("Óleo persistente que também reduz a velocidade de recuperação de cooldown dos inimigos em cima dele.", "Persistent oil that also slows the cooldown recovery of enemies standing in it."),
 "Cooldown Recovery II": L("Recupera o cooldown mais rápido: mais Cluster Grenades por minuto (é a base do clear do endgame).", "Recovers cooldowns faster: more Cluster Grenades per minute (the base of endgame clear)."),
 "Short Fuse I": L("A granada explode mais cedo. Na Cluster Grenade, as mini-granadas saem antes e o clear fica mais fluido.", "The grenade detonates sooner. On Cluster Grenade the mini grenades come out earlier and clear feels smoother."),
 "Fire Attunement": L("Ganha dano de fogo extra (perde um pouco de frio/raio, que a build não usa).", "Gains extra fire damage (loses some cold/lightning, which the build doesn't use)."),
 "Ignite II": L("Muito mais chance de Ignite: a Oil Grenade acende o óleo e queima o pack.", "Much higher Ignite chance: Oil Grenade lights the oil and burns the pack."),
 "Ignite III": L("Mais chance de Ignite e o Ignite causa o dano mais rápido.", "More Ignite chance and Ignites deal their damage faster."),
 "Stun II": L("Acumula Stun mais rápido na Flash Grenade (Stun e Pin são barras separadas).", "Builds Stun faster on Flash Grenade (Stun and Pin are separate bars)."),
 "Stun III": L("Stun muito mais rápido, em troca de dano: a Flash Grenade é utilidade, não dano.", "Much faster Stun at the cost of damage: Flash Grenade is utility, not damage."),
 "Nimble Reload": L("Recarrega o Explosive Shot bem mais rápido.", "Reloads Explosive Shot much faster."),
 "Magnified Area II": L("Área maior nas explosões: mais inimigos em cada granada.", "Larger explosion area: more enemies per grenade."),
 "Heft": L("Aumenta o dano físico máximo dos hits: mais Pin e mais Armour Break por granada.", "Raises the maximum physical damage of hits: more Pin and more Armour Break per grenade."),
 "Fire Penetration II": L("Os hits ignoram a resistência a fogo do inimigo. Grande ganho em bosses.", "Hits ignore enemy fire resistance. A big gain on bosses."),
 "Armour Break III": L("Quebra Armour com o dano físico e dá chance de Endurance Charge ao quebrar tudo.", "Breaks Armour with physical damage and gives a chance for an Endurance Charge on full break."),
 "Searing Flame II": L("Ignites mais fortes, hits mais fracos: a Oil Grenade vira fonte de queima.", "Stronger Ignites, weaker hits: Oil Grenade becomes a burn source."),
 "Ammo Conservation II": L("Chance de não gastar virote ao atirar: mais Explosive Shots sem recarregar.", "Chance not to consume a bolt when firing: more Explosive Shots without reloading."),
 "Ammo Conservation III": L("Mais chance de não gastar virote, com recarga um pouco mais lenta.", "Higher chance not to consume a bolt, with slightly slower reload."),
 "Prolonged Duration II": L("Mais duração: Scavenged Plating fica mais tempo, Oil Grenade cobre o chão por mais tempo.", "Longer duration: Scavenged Plating lasts longer, Oil Grenade covers the ground longer."),
 "Cannibalism I": L("Recupera vida ao matar enquanto a skill persistente está ativa.", "Recovers life on kill while the persistent skill is active."),
 "Clarity I": L("Mais regeneração de mana enquanto a skill persistente está ativa.", "More mana regeneration while the persistent skill is active."),
 "Vitality I": L("Regeneração de vida enquanto a skill persistente está ativa. Compensa a perda de vida do Berserk.", "Life regeneration while the persistent skill is active. Offsets Berserk's life loss."),
 "Vitality II": L("Versão mais forte do Vitality: mais regeneração de vida.", "Stronger Vitality: more life regeneration."),
 "Cluster Grenade": L("Gem de SKILL socketada no Mirage Archer: o Mirage lança Cluster Grenades quando você dá dodge roll.", "SKILL gem socketed in Mirage Archer: the Mirage throws Cluster Grenades when you dodge roll."),
 "Vorana's Siege": L("Support de Lineage: área maior e hits mais fortes em alvos isolados — perfeito para boss.", "Lineage support: bigger area and harder hits on isolated targets — perfect for bosses."),
 "Seraph's Heart": L("Support de Lineage: chance de os inimigos calcularem o hit como se suas resistências fossem 90%.", "Lineage support: chance for enemies to calculate hits as though your resistances were 90%."),
 "Rakiata's Flow": L("Support de Lineage: os hits tratam as resistências elementais do inimigo como invertidas. Luxo do endgame.", "Lineage support: hits treat enemy elemental resistances as inverted. Endgame luxury."),
 "Uruk's Smelting": L("Support de Lineage: Armour Break mais forte e, ao quebrar tudo, o alvo passa a tomar mais dano físico (acumula até um limite).", "Lineage support: stronger Armour Break and, on full break, the target permanently takes more physical damage (stacks up to a cap)."),
 "Ratha's Assault": L("Support de Lineage: carrega vários virotes extras e ataca mais rápido, mas só recarrega quando você dá dodge.", "Lineage support: loads several extra bolts and attacks faster, but only reloads when you dodge."),
}

# ------------------------------------------------------------------ gems e fases
SP30 = L("30 Spirit (15 com A Solid Plan)", "30 Spirit (15 with A Solid Plan)")
PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Explosive + Gas Grenade", "Explosive + Gas Grenade"),
  carry=L("Você: Explosive Grenade + Gas Grenade", "You: Explosive Grenade + Gas Grenade"), dmgSplit=[100, 0],
  goal=L("Mercenary de crossbow desde o nível 1. A Explosive Grenade é o dano; a Gas Grenade deixa uma nuvem de veneno que explode quando pega fogo; a Flash Grenade com Pin I começa a prender inimigos. Frost Bomb no nível 1 aplica Exposure nos bosses. Use só Transmutation e Augmentation na crossbow: Regal, Alchemy e Exalted ficam guardados para a crossbow nível 16 do Ato 2.",
         "A crossbow Mercenary from level 1. Explosive Grenade is the damage; Gas Grenade leaves a poison cloud that explodes when it catches fire; Flash Grenade with Pin I starts pinning enemies. A level 1 Frost Bomb applies Exposure to bosses. Only use Transmutation and Augmentation on the crossbow: save Regal, Alchemy and Exalted for the level 16 crossbow in Act 2."),
  rotation=[L("Frost Bomb no boss (Exposure)", "Frost Bomb on the boss (Exposure)"), L("Flash Grenade: Pin + Blind", "Flash Grenade: Pin + Blind"), L("Gas Grenade: nuvem de veneno", "Gas Grenade: poison cloud"), L("Explosive Grenade em cima da nuvem (ela explode em fogo)", "Explosive Grenade on the cloud (it explodes into fire)"), L("Crossbow Shot enquanto as granadas recarregam", "Crossbow Shot while grenades recharge")],
  gems=[
   G("Explosive Grenade", ["Multishot I", "Elemental Armament I"], L("Dano principal", "Main damage"), L("Granada que quica e explode em fogo quando o pavio acaba. É o seu dano do nível 1 ao endgame e também um Detonator (acende Gas e Oil).", "A bouncing grenade that explodes into fire when its fuse runs out. It's your damage from level 1 to endgame and also a Detonator (lights Gas and Oil)."), "free"),
   G("Gas Grenade", ["Multishot I", "Elemental Armament I"], L("Área + veneno", "Area + poison"), L("Explode em veneno e deixa uma nuvem que cresce. Fogo ou Detonator fazem a nuvem explodir: jogue a Explosive Grenade em cima.", "Bursts into poison and leaves a growing cloud. Fire or a Detonator make the cloud explode: throw Explosive Grenade on top."), "free"),
   G("Flash Grenade", ["Multishot I", "Pin I"], L("Pin + Blind", "Pin + Blind"), L("Cega e atordoa. Com Pin I o dano físico prende os inimigos no lugar.", "Blinds and stuns. With Pin I its physical damage pins enemies in place."), "free"),
   G("Frost Bomb", [], L("Exposure (boss)", "Exposure (boss)"), L("Orb que aplica Elemental Exposure (menos resistência). Pode ficar no nível 1; no nível 3 aplica em mais bosses do Ato 2.", "An orb that applies Elemental Exposure (less resistance). It can stay at level 1; at level 3 it works on more Act 2 bosses."), "free"),
   G("Pounce", [], L("Mobilidade", "Mobility"), L("Pulo de Werewolf até o alvo. Precisa de um Talisman: coloque qualquer um no Weapon Set 2 e deixe a gem no nível 3.", "A Werewolf leap to a target. It needs a Talisman: put any one in Weapon Set 2 and keep the gem at level 3."), "free"),
   G("Attrition", [], L("Dano em rares/bosses", "Damage vs rares/bosses"), L("Mais dano quanto mais tempo você luta contra um rare/unique e dá Culling Strike no fim. Ligue depois do King in the Mists (+30 Spirit).", "More damage the longer you fight a rare/unique, and Culling Strike at the end. Turn it on after the King in the Mists (+30 Spirit)."), "core", 1, L("30 Spirit", "30 Spirit")),
   G("Crossbow Shot", [], L("Ataque básico", "Basic attack"), L("Atira um virote. Serve para completar dano enquanto as granadas estão em cooldown.", "Fires a bolt. Fills damage while grenades are on cooldown."), "free"),
  ],
  cheap=[L("Crossbow com + nível de projéteis ou dano físico/elemental (só Transmutation/Augmentation)", "Crossbow with + projectile levels or physical/elemental damage (Transmutation/Augmentation only)"), L("Botas com Movement Speed", "Boots with Movement Speed")],
  full=[L("Mesmo do barato: guarde Regal/Alchemy/Exalted para a crossbow do Ato 2", "Same as budget: save Regal/Alchemy/Exalted for the Act 2 crossbow")],
  stats=[L("+ nível de projéteis na crossbow", "+ projectile levels on the crossbow"), L("Dano físico/elemental adicionado", "Added physical/elemental damage"), L("Vida", "Life"), L("Resistência a frio (boss do Ato 1)", "Cold resistance (Act 1 boss)")],
  tree=L("Remorseless, Ricochet e Overwhelm: dano de projétil e de arma de duas mãos.", "Remorseless, Ricochet and Overwhelm: projectile and two-handed damage."),
  avoid=[L("Gastar Regal/Exalted na crossbow do Ato 1", "Spending Regal/Exalted on the Act 1 crossbow"), L("Detonar a Gas Grenade longe do pack (a nuvem precisa pegar os inimigos)", "Detonating Gas Grenade away from the pack (the cloud must catch the enemies)")],
  exit=[L("Nível 15 antes do Geonor", "Level 15 before Geonor"), L("King in the Mists (+30 Spirit) e Attrition ligado", "King in the Mists (+30 Spirit) and Attrition on"), L("Currency guardada para a crossbow nível 16", "Currency saved for the level 16 crossbow")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 31], tag=L("Explosive Shot detona as granadas", "Explosive Shot detonates grenades"),
  carry=L("Você: granadas + Explosive Shot", "You: grenades + Explosive Shot"), dmgSplit=[100, 0],
  goal=L("Craft da crossbow nível 16 ao chegar no Ardura Caravan: base branca da Shambrin, Transmutation + Augmentation até ter um mod bom (+ nível de projéteis, dano físico, dano elemental ou attack speed), Regal ou Essence of Abrasion, Exalted para completar, Artificer's Orb e Whetstones. No nível 22 entra o Explosive Shot, que detona as granadas na hora. Primeira ascendência no nível ~28: Suppressing Fire.",
         "Craft the level 16 crossbow when you reach the Ardura Caravan: a white base from Shambrin, Transmutation + Augmentation until you get one good mod (+ projectile levels, physical damage, elemental damage or attack speed), Regal or Essence of Abrasion, Exalted to fill, Artificer's Orb and Whetstones. At level 22 Explosive Shot comes in and detonates your grenades on demand. First ascendancy around level 28: Suppressing Fire."),
  rotation=[L("Frost Bomb (Exposure)", "Frost Bomb (Exposure)"), L("Flash Grenade: Pin + Blind", "Flash Grenade: Pin + Blind"), L("Gas Grenade", "Gas Grenade"), L("Todas as Explosive Grenades", "All your Explosive Grenades"), L("Explosive Shot para detonar tudo de uma vez", "Explosive Shot to detonate everything at once")],
  gems=[
   G("Explosive Grenade", ["Multishot II", "Elemental Armament II"], L("Dano principal", "Main damage"), L("Suba os supports para o nível 2 primeiro nela. Com Grenadier você tem um uso extra de cooldown.", "Level its supports to 2 first. With Grenadier you get an extra cooldown use."), "free"),
   G("Gas Grenade", ["Multishot II", "Elemental Armament II"], L("Área + veneno", "Area + poison"), L("Clear: Gas Grenade no pack e detone com o Explosive Shot.", "Clear: Gas Grenade on the pack and detonate it with Explosive Shot."), "free"),
   G("Flash Grenade", ["Multishot II", "Pin I"], L("Pin + Blind", "Pin + Blind"), L("Jogue a qualquer momento para prender e cegar packs perigosos.", "Throw it any time to pin and blind dangerous packs."), "free"),
   G("Explosive Shot", ["Double Barrel II", "Rapid Attacks II"], L("Detonador", "Detonator"), L("Virotes que explodem ao impacto e fazem as granadas na área explodirem na hora. Entra no nível 22.", "Bolts that explode on impact and make grenades in the area explode instantly. Comes in at level 22."), "free"),
   G("Frost Bomb", [], L("Exposure (boss)", "Exposure (boss)"), L("Continua no nível 1–3 até ser trocada pela Oil Grenade no Ato 3.", "Stays at level 1–3 until Oil Grenade replaces it in Act 3."), "free"),
   G("Pounce", ["Mark for Death", "Mark of Siphoning"], L("Mobilidade + Mark", "Mobility + Mark"), L("Com supports sobrando, o Mark do Pounce quebra Armour e dá mana no boss. Use antes de começar a rotação.", "With spare supports, Pounce's Mark breaks Armour and gives mana on bosses. Use it before starting the rotation."), "free"),
   G("Attrition", [], L("Dano em rares/bosses", "Damage vs rares/bosses"), L("Reserva 30 Spirit.", "Reserves 30 Spirit."), "core", 1, L("30 Spirit", "30 Spirit")),
  ],
  cheap=[L("Crossbow nível 16 craftada (Transmutation → Augmentation → Regal → Exalted)", "Crafted level 16 crossbow (Transmutation → Augmentation → Regal → Exalted)"), L("Anéis/luvas com dano adicionado", "Rings/gloves with added damage")],
  full=[L("Mesma crossbow com Essence of Abrasion no lugar do Regal", "Same crossbow using Essence of Abrasion instead of Regal"), L("Vendor regex: \"!(uiv)\" \"cross|mov|[egdl] da.* to a\"", "Vendor regex: \"!(uiv)\" \"cross|mov|[egdl] da.* to a\"")],
  stats=[L("+ nível de projéteis", "+ projectile levels"), L("% dano físico e dano adicionado", "% physical damage and added damage"), L("Vida e resistências", "Life and resistances"), L("Raio/fogo (boss do Ato 2)", "Lightning/fire (Act 2 boss)")],
  tree=L("Cluster Bombs (+1 projétil de granada), Grenadier (+1 uso de cooldown), Repeating Explosives e Colossal Weapon.", "Cluster Bombs (+1 grenade projectile), Grenadier (+1 cooldown use), Repeating Explosives and Colossal Weapon."),
  avoid=[L("Pular a crossbow nível 16: é o maior salto de dano do Ato 2", "Skipping the level 16 crossbow: it's the biggest damage jump of Act 2"), L("Deixar o Explosive Shot sem Double Barrel", "Running Explosive Shot without Double Barrel")],
  exit=[L("Explosive Shot no nível 22", "Explosive Shot at level 22"), L("1ª ascendência: Suppressing Fire", "1st ascendancy: Suppressing Fire"), L("Supports das granadas no nível 2", "Grenade supports at level 2")]),

 dict(id="a3", name=L("Atos 3–4", "Acts 3–4"), lv=[32, 51], tag=L("Right Where We Want Them", "Right Where We Want Them"),
  carry=L("Você: granadas com Pin em tudo", "You: grenades that Pin everything"), dmgSplit=[100, 0],
  goal=L("Aqui o Pin fica absurdo. Segunda ascendência: Right Where We Want Them — qualquer dano de projétil (todas as granadas) acumula Pin, e inimigos Pinned não conseguem agir. A Oil Grenade substitui a Frost Bomb (Exposure + óleo que pega fogo). No Ziggurat Encampment, craft a crossbow nível 33. Scavenged Plating entra com os +30 Spirit do Azak Bog. Na árvore: Eroding Chains, Cruel Methods e The Molten One's Gift transformam cada Pin em Armour quebrada e dano de fogo extra; Demolitionist dá fogo extra por granada diferente.",
         "This is where Pin gets absurd. Second ascendancy: Right Where We Want Them — any projectile damage (all grenades) builds Pin, and Pinned enemies can't act. Oil Grenade replaces Frost Bomb (Exposure + oil that catches fire). In the Ziggurat Encampment, craft the level 33 crossbow. Scavenged Plating comes in with the +30 Spirit from Azak Bog. On the tree: Eroding Chains, Cruel Methods and The Molten One's Gift turn every Pin into broken Armour and extra fire damage; Demolitionist gives extra fire per different grenade."),
  rotation=[L("Oil Grenade: Exposure + óleo", "Oil Grenade: Exposure + oil"), L("Gas Grenade", "Gas Grenade"), L("Flash Grenade: Pin + Blind", "Flash Grenade: Pin + Blind"), L("Todas as Explosive Grenades", "All your Explosive Grenades"), L("Explosive Shot detona tudo", "Explosive Shot detonates everything")],
  gems=[
   G("Explosive Grenade", ["Multishot II", "Elemental Armament II", "Deliberation", "Payload"], L("Dano principal", "Main damage"), L("Com o Lesser Jeweller's Orb vira 4 links. Payload faz a granada ativar de novo.", "With a Lesser Jeweller's Orb it becomes 4 links. Payload makes the grenade activate again."), "free"),
   G("Oil Grenade", ["Potent Exposure", "Persistent Ground I"], L("Exposure + óleo", "Exposure + oil"), L("Cobre o chão e os inimigos de óleo; Detonators e chão em chamas acendem tudo. Substitui a Frost Bomb e deixa a Exposure mais forte.", "Covers the ground and enemies in oil; Detonators and burning ground light it all. Replaces Frost Bomb with stronger Exposure."), "free"),
   G("Gas Grenade", ["Multishot II", "Elemental Armament II"], L("Área + veneno", "Area + poison"), L("Continua sendo a granada de área do clear.", "Still the area grenade for clear."), "free"),
   G("Flash Grenade", ["Multishot II", "Pin II"], L("Pin + Blind", "Pin + Blind"), L("Pin II: mais Pin e crítico contra inimigos imobilizados.", "Pin II: more Pin and crit against immobilised enemies."), "free"),
   G("Explosive Shot", ["Double Barrel II", "Rapid Attacks II"], L("Detonador", "Detonator"), L("Detone as granadas e o óleo.", "Detonates grenades and oil."), "free"),
   G("Pounce", ["Mark of Siphoning", "Mark for Death"], L("Mobilidade + Mark", "Mobility + Mark"), L("Pulo para reposicionar e Mark no boss.", "Leap to reposition and Mark the boss."), "free"),
   G("Attrition", [], L("Dano em rares/bosses", "Damage vs rares/bosses"), L("Reserva 30 Spirit.", "Reserves 30 Spirit."), "core", 1, L("30 Spirit", "30 Spirit")),
   G("Scavenged Plating", [], L("Armour", "Armour"), L("Quebrar toda a Armour de um inimigo dá stacks de Armour e Thorns. Como cada Pin quebra 50% da Armour (Eroding Chains), você acumula o tempo todo. Ligue com os +30 Spirit do Azak Bog.", "Fully breaking an enemy's Armour grants stacks of Armour and Thorns. Since every Pin breaks 50% Armour (Eroding Chains), you stack it constantly. Turn it on with the +30 Spirit from Azak Bog."), "core", 2, L("30 Spirit", "30 Spirit")),
  ],
  cheap=[L("Crossbow nível 33 craftada (mesma receita)", "Crafted level 33 crossbow (same recipe)"), L("Armaduras de Armour/Evasion com vida", "Armour/Evasion armour pieces with life")],
  full=[L("Crossbow nível 33 com Essence of Abrasion + Gnawed Jawbone (desecrate)", "Level 33 crossbow with Essence of Abrasion + Gnawed Jawbone (desecrate)"), L("Amuleto com + nível de projéteis", "Amulet with + projectile levels")],
  stats=[L("+ nível de projéteis", "+ projectile levels"), L("% dano físico e dano adicionado", "% physical damage and added damage"), L("Vida, Armour e resistências", "Life, Armour and resistances"), L("Força (vida) com o que sobrar", "Strength (life) with what's left")],
  tree=L("Eroding Chains, Cruel Methods, The Molten One's Gift, Demolitionist, Smoke Inhalation, Incendiary, Fearful Paralysis e Feel no Pain.", "Eroding Chains, Cruel Methods, The Molten One's Gift, Demolitionist, Smoke Inhalation, Incendiary, Fearful Paralysis and Feel no Pain."),
  avoid=[L("Usar só uma granada: Demolitionist quer granadas diferentes", "Using only one grenade: Demolitionist wants different grenades"), L("Esquecer o Azak Bog (+30 Spirit)", "Skipping Azak Bog (+30 Spirit)")],
  exit=[L("2ª ascendência: Right Where We Want Them", "2nd ascendancy: Right Where We Want Them"), L("Crossbow nível 33", "Level 33 crossbow"), L("Scavenged Plating ligado", "Scavenged Plating on"), L("Shark Fin (Ato 4): 30% increased Armour, Evasion e ES", "Shark Fin (Act 4): 30% increased Armour, Evasion and ES")]),

 dict(id="int", name=L("Interlúdios", "Interludes"), lv=[52, 64], tag=L("Cluster Grenade", "Cluster Grenade"),
  carry=L("Você: Cluster Grenade + rotação completa", "You: Cluster Grenade + full rotation"), dmgSplit=[100, 0],
  goal=L("A Cluster Grenade entra no nível 52 (gem nível 13, guarde o Greater Jeweller's Orb para ela): uma granada que solta um anel de mini-granadas. Esse setup já aguenta boa parte dos mapas. No nível 59 procure a Cannonade Crossbow no vendor e craft com tudo que juntou nos Atos 3–4.",
         "Cluster Grenade comes in at level 52 (level 13 gem, save the Greater Jeweller's Orb for it): a grenade that drops a ring of mini grenades. This setup already handles much of the maps. At level 59 look for the Cannonade Crossbow at the vendor and craft it with everything you saved in Acts 3–4."),
  rotation=[L("Oil Grenade: Exposure + Ignite", "Oil Grenade: Exposure + Ignite"), L("Cluster Grenade: explosões + Pin", "Cluster Grenade: explosions + Pin"), L("Gas Grenade", "Gas Grenade"), L("Flash Grenade: Pin + Blind", "Flash Grenade: Pin + Blind"), L("Explosive Grenades e Explosive Shot para detonar", "Explosive Grenades and Explosive Shot to detonate")],
  gems=[
   G("Cluster Grenade", ["Multishot II", "Cooldown Recovery II", "Deliberation", "Short Fuse I"], L("Clear + boss", "Clear + boss"), L("Granada que explode e espalha mini-granadas. É o melhor skill de área da build; entra no nível 52.", "A grenade that explodes and scatters mini grenades. The build's best area skill; comes in at level 52."), "free"),
   G("Explosive Grenade", ["Multishot II", "Elemental Armament II", "Deliberation", "Fire Attunement"], L("Dano principal", "Main damage"), L("Fire Attunement no lugar do Payload quando tiver o 5º link.", "Fire Attunement replaces Payload once you have the 5th link."), "free"),
   G("Oil Grenade", ["Potent Exposure", "Persistent Ground II", "Ignite II"], L("Exposure + Ignite", "Exposure + Ignite"), L("Ignite II faz o óleo queimar o pack.", "Ignite II makes the oil burn the pack."), "free"),
   G("Gas Grenade", ["Multishot II", "Elemental Armament II", "Deliberation"], L("Área + veneno", "Area + poison"), L("Continua na rotação para o Demolitionist.", "Stays in the rotation for Demolitionist."), "free"),
   G("Flash Grenade", ["Multishot II", "Stun II", "Pin I"], L("Pin + Stun", "Pin + Stun"), L("Use em rares e no boss.", "Use it on rares and bosses."), "free"),
   G("Explosive Shot", ["Double Barrel II", "Nimble Reload"], L("Detonador", "Detonator"), L("Nimble Reload deixa o detonador sempre pronto.", "Nimble Reload keeps the detonator always ready."), "free"),
   G("Pounce", ["Mark of Siphoning", "Mark for Death"], L("Mobilidade + Mark", "Mobility + Mark"), L("Igual aos Atos 3–4.", "Same as Acts 3–4."), "free"),
   G("Attrition", [], L("Dano em rares/bosses", "Damage vs rares/bosses"), L("Reserva 30 Spirit.", "Reserves 30 Spirit."), "core", 1, L("30 Spirit", "30 Spirit")),
   G("Scavenged Plating", ["Cannibalism I"], L("Armour + vida no kill", "Armour + life on kill"), L("Cannibalism I dá vida ao matar enquanto o Plating está ativo.", "Cannibalism I gives life on kill while Plating is active."), "core", 2, L("30 Spirit", "30 Spirit")),
  ],
  cheap=[L("Cannonade Crossbow nível 59 craftada", "Crafted level 59 Cannonade Crossbow"), L("Lythara (+40 Spirit) em Kriar Village", "Lythara (+40 Spirit) in Kriar Village")],
  full=[L("Cannonade com + nível de projéteis e dano físico alto", "Cannonade with + projectile levels and high physical damage"), L("Greater Jeweller's Orb na Cluster Grenade", "Greater Jeweller's Orb on Cluster Grenade")],
  stats=[L("+ nível de projéteis", "+ projectile levels"), L("% dano físico, dano adicionado, attack speed", "% physical damage, added damage, attack speed"), L("Vida, Armour e resistências", "Life, Armour and resistances")],
  tree=L("Volatile Catalyst (área + cooldown), Hard to Kill e Adrenaline Rush.", "Volatile Catalyst (area + cooldown), Hard to Kill and Adrenaline Rush."),
  avoid=[L("Pegar a Cluster Grenade sem o 4º/5º link", "Taking Cluster Grenade without the 4th/5th link"), L("Mapas com less Cooldown Recovery", "Maps with less Cooldown Recovery")],
  exit=[L("Cluster Grenade com 5 links", "Cluster Grenade with 5 links"), L("Cannonade Crossbow", "Cannonade Crossbow"), L("Resistências no cap para os mapas", "Resistances capped for maps")]),

 dict(id="cannon", name=L("Mapas 65+ (Trarthan Cannon)", "Maps 65+ (Trarthan Cannon)"), lv=[65, 78], tag=L("A Solid Plan + Mirage Archer", "A Solid Plan + Mirage Archer"),
  carry=L("Você: granadas · Mirage Archer: Cluster Grenade", "You: grenades · Mirage Archer: Cluster Grenade"), dmgSplit=[80, 20],
  goal=L("A Trarthan Cannon (crossbow que dropa a partir do T1, nível 65) tem mais dano físico base, mas só carrega granadas. Por isso: Trarthan Cannon no Weapon Set 1 com as granadas, e a Cannonade no Set 2 só com o Explosive Shot. Terceira e quarta ascendências: A Solid Plan (skills persistentes reservam 50% menos Spirit) e Polish That Gear (Deflection = 20% da Armour). O Mirage Archer usa a Cluster Grenade a cada dodge roll e o Eternal Rage entra graças ao A Solid Plan.",
         "The Trarthan Cannon (a crossbow that drops from T1, level 65) has higher base physical damage but can only load grenades. So: Trarthan Cannon in Weapon Set 1 with the grenades, and the Cannonade in Set 2 with only Explosive Shot. Third and fourth ascendancies: A Solid Plan (persistent skills reserve 50% less Spirit) and Polish That Gear (Deflection = 20% of Armour). Mirage Archer uses Cluster Grenade on every dodge roll and Eternal Rage fits thanks to A Solid Plan."),
  rotation=[L("Set 1: Oil Grenade (Exposure + Ignite)", "Set 1: Oil Grenade (Exposure + Ignite)"), L("Set 1: Flash Grenade (Pin + Armour Break)", "Set 1: Flash Grenade (Pin + Armour Break)"), L("Set 1: Cluster e Explosive Grenades", "Set 1: Cluster and Explosive Grenades"), L("Dodge roll: o Mirage Archer joga mais Cluster Grenades", "Dodge roll: Mirage Archer throws more Cluster Grenades"), L("Troque para o Set 2 e detone com Explosive Shot", "Swap to Set 2 and detonate with Explosive Shot")],
  gems=[
   G("Cluster Grenade", ["Multishot II", "Short Fuse I", "Magnified Area II", "Deliberation", "Heft"], L("Clear + boss · Set 1", "Clear + boss · Set 1"), L("Heft aumenta o físico máximo: mais Pin e Armour Break.", "Heft raises max physical: more Pin and Armour Break."), "free"),
   G("Explosive Grenade", ["Multishot I", "Elemental Armament II", "Deliberation", "Fire Penetration II", "Fire Attunement"], L("Dano de boss · Set 1", "Boss damage · Set 1"), L("Fire Penetration II ignora a resistência a fogo.", "Fire Penetration II ignores fire resistance."), "free"),
   G("Flash Grenade", ["Multishot II", "Pin II", "Stun III", "Armour Break III", "Heft"], L("Pin + Armour Break · Set 1", "Pin + Armour Break · Set 1"), L("Setup de utilidade: prende e quebra toda a Armour do boss.", "Utility setup: pins and fully breaks the boss's Armour."), "free"),
   G("Oil Grenade", ["Potent Exposure", "Persistent Ground III", "Searing Flame II", "Ignite III"], L("Exposure + Ignite · Set 1", "Exposure + Ignite · Set 1"), L("Ignite forte e Exposure: abre toda luta de boss.", "Strong Ignite and Exposure: opens every boss fight."), "free"),
   G("Gas Grenade", ["Multishot II", "Elemental Armament II", "Deliberation", "Magnified Area II"], L("Área + veneno", "Area + poison"), L("Mantém o bônus do Demolitionist.", "Keeps the Demolitionist bonus."), "free"),
   G("Explosive Shot", ["Double Barrel II", "Nimble Reload", "Ammo Conservation II", "Rapid Attacks II"], L("Detonador · Set 2 (Cannonade)", "Detonator · Set 2 (Cannonade)"), L("Só no Weapon Set 2: a Trarthan Cannon não carrega virotes normais.", "Only on Weapon Set 2: the Trarthan Cannon can't load regular bolts."), "free"),
   G("Mirage Archer", ["Cluster Grenade", "Multishot II", "Deliberation", "Prolonged Duration II", "Cooldown Recovery II"], L("Dano extra no dodge", "Extra damage on dodge"), L("Cada dodge roll cria um Mirage que lança a Cluster Grenade socketada. 60 Spirit (30 com A Solid Plan).", "Every dodge roll creates a Mirage that throws the socketed Cluster Grenade. 60 Spirit (30 with A Solid Plan)."), "core", 1, L("60 Spirit (30 com A Solid Plan)", "60 Spirit (30 with A Solid Plan)")),
   G("Eternal Rage", ["Cannibalism I", "Vitality I"], L("Rage constante", "Constant Rage"), L("Regenera Rage o tempo todo (mais dano de ataque). 100 Spirit (50 com A Solid Plan).", "Regenerates Rage constantly (more attack damage). 100 Spirit (50 with A Solid Plan)."), "core", 2, L("100 Spirit (50 com A Solid Plan)", "100 Spirit (50 with A Solid Plan)")),
   G("Scavenged Plating", ["Prolonged Duration II", "Clarity I"], L("Armour + mana", "Armour + mana"), L("Clarity I ajuda na mana.", "Clarity I helps with mana."), "core", 3, SP30),
  ],
  cheap=[L("Cannonade (Set 2) + Trarthan Cannon rare (Set 1)", "Cannonade (Set 2) + rare Trarthan Cannon (Set 1)"), L("Perfect Essence of Battle (+3 nível de skills de ataque) se faltar nível na arma", "Perfect Essence of Battle (+3 to Level of all Attack Skills) if the weapon lacks levels")],
  full=[L("Trarthan Cannon com dano físico alto + nível de projéteis + attack speed", "Trarthan Cannon with high physical damage + projectile levels + attack speed"), L("Amuleto com Spirit alto", "Amulet with high Spirit")],
  stats=[L("Dano físico na Trarthan Cannon", "Physical damage on the Trarthan Cannon"), L("Spirit (amuleto)", "Spirit (amulet)"), L("Vida, Armour, resistências", "Life, Armour, resistances"), L("Mana Leech/Mana on Kill", "Mana Leech/Mana on Kill")],
  tree=L("Tempered Defences, Battle Trance, Authority, Giantslayer, Volatile Grenades e o keystone Glancing Blows.", "Tempered Defences, Battle Trance, Authority, Giantslayer, Volatile Grenades and the Glancing Blows keystone."),
  avoid=[L("Colocar Explosive Shot no Set 1 (a Trarthan Cannon não carrega virotes)", "Putting Explosive Shot on Set 1 (the Trarthan Cannon can't load bolts)"), L("Ligar Eternal Rage sem A Solid Plan", "Turning on Eternal Rage without A Solid Plan")],
  exit=[L("3ª e 4ª ascendências: A Solid Plan e Polish That Gear", "3rd and 4th ascendancies: A Solid Plan and Polish That Gear"), L("Mirage Archer + Eternal Rage ligados", "Mirage Archer + Eternal Rage on"), L("Nível 79 para a Siege Crossbow", "Level 79 for the Siege Crossbow")]),

 dict(id="t15", name=L("Endgame T15", "Endgame T15"), lv=[79, 89], tag=L("Siege Crossbow + Berserk", "Siege Crossbow + Berserk"),
  carry=L("Você: granadas · Mirage Archer: Cluster Grenade", "You: grenades · Mirage Archer: Cluster Grenade"), dmgSplit=[75, 25],
  goal=L("A Siege Crossbow (nível 79) vira a arma única. Weapon Set 2 recebe toda a Cooldown Recovery para spammar a Cluster Grenade no clear; o Set 1 fica com dano de boss e fogo. Berserk substitui o Attrition (amuleto com Spirit alto) e Iron Reflexes converte Evasion em Armour: com Polish That Gear, isso vira Deflection alta. Mana: joias com mana cost convertida em vida (Ruby) e Recover % Mana on Kill (Sapphire), Mana Leech na crossbow e Mana on Kill nas luvas. A perda de vida do Berserk é compensada pela regen do body (base com implicit de Life Regeneration) e pelo Vitality.",
         "The Siege Crossbow (level 79) becomes your only weapon. Weapon Set 2 gets all the Cooldown Recovery to spam Cluster Grenade while clearing; Set 1 keeps boss and fire damage. Berserk replaces Attrition (amulet with high Spirit) and Iron Reflexes converts Evasion into Armour: with Polish That Gear that becomes high Deflection. Mana: jewels with mana cost converted to life (Ruby) and Recover % Mana on Kill (Sapphire), Mana Leech on the crossbow and Mana on Kill on gloves. Berserk's life loss is offset by the body's regen (a base with a Life Regeneration implicit) and Vitality."),
  rotation=[L("Oil Grenade: Exposure + Ignite", "Oil Grenade: Exposure + Ignite"), L("Flash Grenade: Pin + Armour Break", "Flash Grenade: Pin + Armour Break"), L("Explosive Grenades no boss", "Explosive Grenades on the boss"), L("Explosive Shot detona", "Explosive Shot detonates"), L("Clear: spam de Cluster Grenade + Explosive Shot, Flash nos rares", "Clear: spam Cluster Grenade + Explosive Shot, Flash on rares")],
  gems=[
   G("Cluster Grenade", ["Multishot II", "Short Fuse I", "Magnified Area II", "Deliberation", "Cooldown Recovery II"], L("Clear · Set 2", "Clear · Set 2"), L("Com os pontos de Cooldown Recovery do Set 2, sai muito mais vezes.", "With Set 2's Cooldown Recovery points, it comes out far more often."), "free"),
   G("Explosive Grenade", ["Multishot II", "Elemental Armament II", "Deliberation", "Fire Penetration II", "Vorana's Siege"], L("Boss · Set 1", "Boss · Set 1"), L("Vorana's Siege: mais área e mais dano em alvo isolado.", "Vorana's Siege: more area and more damage on isolated targets."), "free"),
   G("Flash Grenade", ["Multishot II", "Pin II", "Stun III", "Armour Break III", "Heft"], L("Pin + Armour Break · Set 1", "Pin + Armour Break · Set 1"), L("Prenda o boss antes das granadas de dano.", "Pin the boss before your damage grenades."), "free"),
   G("Oil Grenade", ["Potent Exposure", "Ignite III", "Searing Flame II", "Persistent Ground II"], L("Exposure + Ignite · Set 1", "Exposure + Ignite · Set 1"), L("Abre a luta de boss.", "Opens the boss fight."), "free"),
   G("Explosive Shot", ["Double Barrel II", "Nimble Reload", "Ammo Conservation II", "Rapid Attacks II"], L("Detonador · Set 1", "Detonator · Set 1"), L("Na Siege Crossbow ele volta para o Set 1.", "On the Siege Crossbow it goes back to Set 1."), "free"),
   G("Mirage Archer", ["Cluster Grenade", "Deliberation", "Multishot II", "Magnified Area II", "Cooldown Recovery II"], L("Dano extra no dodge", "Extra damage on dodge"), L("30 Spirit com A Solid Plan.", "30 Spirit with A Solid Plan."), "core", 1, L("60 Spirit (30 com A Solid Plan)", "60 Spirit (30 with A Solid Plan)")),
   G("Eternal Rage", ["Cannibalism I", "Vitality I"], L("Rage constante", "Constant Rage"), L("50 Spirit com A Solid Plan.", "50 Spirit with A Solid Plan."), "core", 2, L("100 Spirit (50 com A Solid Plan)", "100 Spirit (50 with A Solid Plan)")),
   G("Berserk", ["Clarity I", "Seraph's Heart"], L("Rage mais forte", "Stronger Rage"), L("Fortalece a Rage (mais dano, e aumenta o fogo do Ichlotl's Inferno), mas você perde vida enquanto não perde Rage.", "Strengthens Rage (more damage, and boosts Ichlotl's Inferno fire), but you lose life while not losing Rage."), "core", 3, SP30),
   G("Scavenged Plating", ["Prolonged Duration II"], L("Armour", "Armour"), L("15 Spirit com A Solid Plan.", "15 Spirit with A Solid Plan."), "core", 4, SP30),
  ],
  cheap=[L("Siege Crossbow rare com dano físico/elemental alto", "Rare Siege Crossbow with high physical/elemental damage"), L("Beira's Anguish + Sanguis Heroum (charms baratos)", "Beira's Anguish + Sanguis Heroum (cheap charms)"), L("Body com implicit de Life Regeneration", "Body with a Life Regeneration implicit")],
  full=[L("Siege Crossbow com raio alto (Shock sem Stormcaller)", "Siege Crossbow with high lightning (Shock without Stormcaller)"), L("Amuleto Spirit + nível de projéteis", "Amulet with Spirit + projectile levels"), L("Joias: Mana Cost as Life (Ruby) · Mana on Kill (Sapphire)", "Jewels: Mana Cost as Life (Ruby) · Mana on Kill (Sapphire)")],
  stats=[L("Dano adicionado + % físico na Siege Crossbow", "Added damage + % physical on the Siege Crossbow"), L("Spirit no amuleto", "Spirit on the amulet"), L("Vida, Armour, % Armour applies to Elemental", "Life, Armour, % Armour applies to Elemental"), L("Mana Leech/Mana on Kill", "Mana Leech/Mana on Kill")],
  tree=L("Iron Reflexes + Glancing Blows. Set 1: Giantslayer, Blazing Arms, Ichlotl's Inferno. Set 2: Multitasking, Volatile Catalyst, Distracting Presence, Run and Gun.", "Iron Reflexes + Glancing Blows. Set 1: Giantslayer, Blazing Arms, Ichlotl's Inferno. Set 2: Multitasking, Volatile Catalyst, Distracting Presence, Run and Gun."),
  avoid=[L("Mapas com less Recovery of Life/ES (Berserk) e less Cooldown Recovery", "Maps with less Life/ES Recovery (Berserk) and less Cooldown Recovery"), L("Berserk sem regen de vida", "Berserk without life regen")],
  exit=[L("Siege Crossbow", "Siege Crossbow"), L("Mana resolvida (joias + leech)", "Mana solved (jewels + leech)"), L("Deflection alta com Iron Reflexes", "High Deflection with Iron Reflexes")]),

 dict(id="max", name=L("Pinnacle / Luxo", "Pinnacle / Luxury"), lv=[90, 100], tag=L("Lineage supports", "Lineage supports"),
  carry=L("Você: granadas · Mirage Archer: Cluster Grenade", "You: grenades · Mirage Archer: Cluster Grenade"), dmgSplit=[75, 25],
  goal=L("Setup aspiracional do BlazeworksTV para empurrar a build ao máximo: supports de Lineage (Rakiata's Flow e Vorana's Siege na Explosive Grenade, Uruk's Smelting na Flash, Ratha's Assault no Explosive Shot), Constricting Command no capacete, Mageblood e Rite of Passage. Nada disso é necessário para T15: é teto de dano.",
         "BlazeworksTV's aspirational setup to push the build to the max: Lineage supports (Rakiata's Flow and Vorana's Siege on Explosive Grenade, Uruk's Smelting on Flash, Ratha's Assault on Explosive Shot), Constricting Command helmet, Mageblood and Rite of Passage. None of it is required for T15: it's the damage ceiling."),
  rotation=[L("Oil Grenade", "Oil Grenade"), L("Flash Grenade (Uruk's Smelting: Armour quebrada vira dano físico permanente)", "Flash Grenade (Uruk's Smelting: broken Armour becomes permanent physical damage taken)"), L("Explosive e Cluster Grenades", "Explosive and Cluster Grenades"), L("Explosive Shot com Ratha's Assault: recarregue no dodge", "Explosive Shot with Ratha's Assault: reload on dodge")],
  gems=[
   G("Explosive Grenade", ["Multishot II", "Elemental Armament II", "Deliberation", "Rakiata's Flow", "Vorana's Siege"], L("Boss", "Boss"), L("Rakiata's Flow inverte as resistências elementais do alvo.", "Rakiata's Flow inverts the target's elemental resistances."), "free"),
   G("Cluster Grenade", ["Multishot II", "Cooldown Recovery II", "Deliberation", "Magnified Area II", "Short Fuse I"], L("Clear", "Clear"), L("Igual ao T15.", "Same as T15."), "free"),
   G("Flash Grenade", ["Multishot II", "Pin II", "Stun III", "Uruk's Smelting", "Armour Break III"], L("Pin + Armour Break", "Pin + Armour Break"), L("Uruk's Smelting deixa o alvo tomando mais dano físico para sempre (até um limite).", "Uruk's Smelting makes the target take more physical damage permanently (up to a cap)."), "free"),
   G("Oil Grenade", ["Prolonged Duration II", "Potent Exposure", "Persistent Ground II", "Ignite III"], L("Exposure + Ignite", "Exposure + Ignite"), L("Mais duração no óleo.", "Longer oil duration."), "free"),
   G("Explosive Shot", ["Ratha's Assault", "Magnified Area II", "Elemental Armament II", "Ammo Conservation III"], L("Detonador", "Detonator"), L("Ratha's Assault: vários virotes extras, recarga só no dodge (que também solta o Mirage Archer).", "Ratha's Assault: several extra bolts, reload only on dodge (which also triggers Mirage Archer)."), "free"),
   G("Mirage Archer", ["Cluster Grenade", "Deliberation", "Magnified Area II", "Cooldown Recovery II", "Multishot II"], L("Dano extra no dodge", "Extra damage on dodge"), L("30 Spirit com A Solid Plan.", "30 Spirit with A Solid Plan."), "core", 1, L("60 Spirit (30 com A Solid Plan)", "60 Spirit (30 with A Solid Plan)")),
   G("Eternal Rage", ["Clarity I", "Cannibalism I"], L("Rage constante", "Constant Rage"), L("50 Spirit com A Solid Plan.", "50 Spirit with A Solid Plan."), "core", 2, L("100 Spirit (50 com A Solid Plan)", "100 Spirit (50 with A Solid Plan)")),
   G("Berserk", ["Vitality II", "Seraph's Heart"], L("Rage mais forte", "Stronger Rage"), L("Vitality II para segurar a perda de vida.", "Vitality II to hold the life loss."), "core", 3, SP30),
   G("Scavenged Plating", ["Prolonged Duration II"], L("Armour", "Armour"), L("15 Spirit com A Solid Plan.", "15 Spirit with A Solid Plan."), "core", 4, SP30),
  ],
  cheap=[L("Setup do T15 + um support de Lineage por vez (Vorana's Siege primeiro)", "T15 setup + one Lineage support at a time (Vorana's Siege first)")],
  full=[L("Constricting Command · Mageblood · Rite of Passage · Vitalic Rings", "Constricting Command · Mageblood · Rite of Passage · Vitalic Rings")],
  stats=[L("Dano da crossbow", "Crossbow damage"), L("Spirit", "Spirit"), L("Vida e Armour", "Life and Armour")],
  tree=L("Mesma do T15; ajuste Set 1/Set 2 conforme o conteúdo.", "Same as T15; tune Set 1/Set 2 for the content."),
  avoid=[L("Comprar Mageblood antes da crossbow: a crossbow dá mais dano por divine", "Buying Mageblood before the crossbow: the crossbow gives more damage per divine")],
  exit=[L("Pinnacle bosses sem morrer", "Pinnacle bosses without dying")]),
]
PH = {p["id"]: p for p in PHASES}

BOX = {
 "a1": ("3", [L("Explosive · Gas · Flash", "Explosive · Gas · Flash")], L("Três granadas diferentes na rotação. A partir do Demolitionist (Ato 3), cada granada diferente dá 4% do dano como fogo extra.", "Three different grenades in the rotation. From Demolitionist (Act 3), each different grenade gives 4% of damage as extra fire.")),
 "a2": ("3", [L("+1 uso (Grenadier)", "+1 use (Grenadier)")], L("Grenadier dá um uso de cooldown extra em cada granada; Cluster Bombs, um projétil extra.", "Grenadier gives each grenade an extra cooldown use; Cluster Bombs, an extra projectile.")),
 "a3": ("4", [L("Demolitionist +16% fogo", "Demolitionist +16% fire")], L("Explosive, Gas, Flash e Oil: 4 granadas diferentes em 8 s = 16% do dano como fogo extra.", "Explosive, Gas, Flash and Oil: 4 different grenades within 8 s = 16% of damage as extra fire.")),
 "int": ("5", [L("Demolitionist +20% fogo", "Demolitionist +20% fire")], L("Com a Cluster Grenade são 5 granadas diferentes: 20% do dano como fogo extra.", "With Cluster Grenade that's 5 different grenades: 20% of damage as extra fire.")),
 "cannon": ("5", [L("Mirage Archer: Cluster", "Mirage Archer: Cluster")], L("Cinco granadas + o Mirage Archer lançando Cluster Grenade a cada dodge roll.", "Five grenades + Mirage Archer throwing Cluster Grenade on every dodge roll.")),
 "t15": ("4", [L("Set 1 boss · Set 2 clear", "Set 1 boss · Set 2 clear")], L("Oil, Flash, Explosive (Set 1) e Cluster (Set 2). A Gas Grenade sai; o Demolitionist continua com 4.", "Oil, Flash, Explosive (Set 1) and Cluster (Set 2). Gas Grenade leaves; Demolitionist keeps 4.")),
 "max": ("4", [L("Lineage supports", "Lineage supports")], L("Mesmas 4 granadas com supports de Lineage.", "Same 4 grenades with Lineage supports.")),
}
SPIRIT_NOTE = {
 "a1": L("Attrition reserva 30 Spirit: ligue depois do King in the Mists.", "Attrition reserves 30 Spirit: turn it on after the King in the Mists."),
 "a3": L("Ordem do Spirit: Attrition (30) → Scavenged Plating (30). Os +30 do Azak Bog pagam o Plating.", "Spirit order: Attrition (30) → Scavenged Plating (30). Azak Bog's +30 pays for Plating."),
 "int": L("Attrition (30) + Scavenged Plating (30). Lythara (+40) sobra para o endgame.", "Attrition (30) + Scavenged Plating (30). Lythara (+40) is spare for endgame."),
 "cannon": L("Com A Solid Plan (50% less reserva): Mirage Archer 30 → Eternal Rage 50 → Scavenged Plating 15 = 95 Spirit.", "With A Solid Plan (50% less reservation): Mirage Archer 30 → Eternal Rage 50 → Scavenged Plating 15 = 95 Spirit."),
 "t15": L("Com A Solid Plan: Mirage Archer 30 → Eternal Rage 50 → Berserk 15 → Scavenged Plating 15 = 110 Spirit. Amuleto com Spirit alto paga o Berserk.", "With A Solid Plan: Mirage Archer 30 → Eternal Rage 50 → Berserk 15 → Scavenged Plating 15 = 110 Spirit. A high-Spirit amulet pays for Berserk."),
 "max": L("Igual ao T15: 110 Spirit com A Solid Plan.", "Same as T15: 110 Spirit with A Solid Plan."),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in SPIRIT_NOTE.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Explosive Grenade + Crossbow Shot. Só Transmutation/Augmentation na crossbow.", "Explosive Grenade + Crossbow Shot. Only Transmutation/Augmentation on the crossbow."),
 5: L("Gas Grenade assim que cair a gem.", "Gas Grenade as soon as the gem drops."),
 8: L("Flash Grenade com Pin I.", "Flash Grenade with Pin I."),
 10: L("Freythorn: King in the Mists (+30 Spirit) → Attrition.", "Freythorn: King in the Mists (+30 Spirit) → Attrition."),
 15: L("Nível 15 antes do Geonor.", "Level 15 before Geonor."),
 16: L("Ardura Caravan: craft da crossbow nível 16 com toda a currency guardada.", "Ardura Caravan: craft the level 16 crossbow with all saved currency."),
 22: L("Explosive Shot (Double Barrel II + Rapid Attacks II).", "Explosive Shot (Double Barrel II + Rapid Attacks II)."),
 28: L("1ª ascendência: Suppressing Fire.", "1st ascendancy: Suppressing Fire."),
 33: L("Ziggurat Encampment: craft da crossbow nível 33.", "Ziggurat Encampment: craft the level 33 crossbow."),
 36: L("Oil Grenade no lugar da Frost Bomb.", "Oil Grenade replaces Frost Bomb."),
 38: L("Azak Bog: Ignagduk (+30 Spirit) → Scavenged Plating.", "Azak Bog: Ignagduk (+30 Spirit) → Scavenged Plating."),
 40: L("2ª ascendência: Right Where We Want Them (todo projétil dá Pin).", "2nd ascendancy: Right Where We Want Them (every projectile builds Pin)."),
 47: L("Ato 4: Shark Fin → 30% increased Armour, Evasion e ES.", "Act 4: Shark Fin → 30% increased Armour, Evasion and ES."),
 52: L("Cluster Grenade (gem nível 13) com o Greater Jeweller's Orb.", "Cluster Grenade (level 13 gem) with the Greater Jeweller's Orb."),
 59: L("Vendor: Cannonade Crossbow nível 59.", "Vendor: level 59 Cannonade Crossbow."),
 62: L("Kriar Village: Lythara (+40 Spirit).", "Kriar Village: Lythara (+40 Spirit)."),
 65: L("Trarthan Cannon começa a dropar (T1). 3ª ascendência: A Solid Plan.", "Trarthan Cannon starts dropping (T1). 3rd ascendancy: A Solid Plan."),
 68: L("Mirage Archer (Cluster Grenade) + Eternal Rage.", "Mirage Archer (Cluster Grenade) + Eternal Rage."),
 75: L("4ª ascendência: Polish That Gear (Deflection = 20% da Armour).", "4th ascendancy: Polish That Gear (Deflection = 20% of Armour)."),
 79: L("Siege Crossbow. Berserk no lugar do Attrition. Iron Reflexes.", "Siege Crossbow. Berserk replaces Attrition. Iron Reflexes."),
 85: L("Joias de mana (Ruby: Mana Cost as Life · Sapphire: Mana on Kill).", "Mana jewels (Ruby: Mana Cost as Life · Sapphire: Mana on Kill)."),
 90: L("Supports de Lineage: Vorana's Siege → Uruk's Smelting → Rakiata's Flow.", "Lineage supports: Vorana's Siege → Uruk's Smelting → Rakiata's Flow."),
}

ASCENDANCY = [
 dict(order=1, key="sf", node="Suppressing Fire", when=L("1º Trial (~nível 28)", "1st Trial (~level 28)"), text=L("40% more acúmulo de Immobilisation (Pin).", "40% more Immobilisation buildup (Pin)."), why=L("Pin sai muito mais rápido: seu controle de grupo e defesa desde o Ato 2.", "Pin comes much faster: your crowd control and defence from Act 2.")),
 dict(order=2, key="rwwwt", node="Right Where We Want Them", when=L("2º Trial (~nível 40)", "2nd Trial (~level 40)"), text=L("Dano de projétil acumula Pin; inimigos Pinned não podem agir.", "Projectile damage builds Pin; Pinned enemies cannot perform actions."), why=L("O coração da build: toda granada prende e um inimigo preso não ataca.", "The heart of the build: every grenade pins and a pinned enemy can't attack.")),
 dict(order=3, key="asp", node="A Solid Plan", when=L("3º Trial (~nível 65)", "3rd Trial (~level 65)"), text=L("Buffs persistentes têm 50% less reserva.", "Persistent Buffs have 50% less Reservation."), why=L("Paga Mirage Archer, Eternal Rage, Berserk e Scavenged Plating juntos.", "Pays for Mirage Archer, Eternal Rage, Berserk and Scavenged Plating together.")),
 dict(order=4, key="ptg", node="Polish That Gear", when=L("4º Trial (~nível 75)", "4th Trial (~level 75)"), text=L("Deflection Rating igual a 20% da Armour; 100% da Evasion como Ailment Threshold extra.", "Deflection Rating equal to 20% of Armour; 100% of Evasion as extra Ailment Threshold."), why=L("Armour vira Deflection (40% menos dano nos hits defletidos). Com Iron Reflexes fica enorme.", "Armour becomes Deflection (40% less damage from deflected hits). With Iron Reflexes it gets huge.")),
]
ASC_UNLOCK = [28, 40, 65, 75]

KEY_PASSIVES = [
 dict(node="Eroding Chains", type="Notable", text=L("Quebra 50% da Armour ao dar Pin num inimigo.", "Break 50% of Armour on Pinning an Enemy."), when=L("Ato 3 → sempre", "Act 3 → forever"), why=L("Cada Pin vira Armour quebrada: alimenta Scavenged Plating e The Molten One's Gift.", "Every Pin becomes broken Armour: feeds Scavenged Plating and The Molten One's Gift.")),
 dict(node="The Molten One's Gift", type="Notable", text=L("+10% resistência a fogo; 15% increased efeito de Fully Broken Armour; Fully Broken Armour também aumenta o dano de fogo recebido.", "+10% fire resistance; 15% increased effect of Fully Broken Armour; Fully Broken Armour also increases Fire Damage taken."), when=L("Ato 3 → sempre", "Act 3 → forever"), why=L("As granadas são de fogo: Armour quebrada vira dano extra.", "Grenades are fire: broken Armour becomes extra damage.")),
 dict(node="Demolitionist", type="Notable", text=L("4% do dano como fogo extra para cada granada diferente usada nos últimos 8 s.", "Gain 4% of Damage as Extra Fire Damage for every different Grenade fired in the past 8 seconds."), when=L("Ato 3 → sempre", "Act 3 → forever"), why=L("Por isso a rotação usa 4–5 granadas diferentes.", "That's why the rotation uses 4–5 different grenades.")),
 dict(node="Grenadier", type="Notable", text=L("Granadas têm +1 uso de cooldown.", "Grenade Skills have +1 Cooldown Use."), when=L("Ato 2 → sempre", "Act 2 → forever"), why=L("Dobra as granadas no boss.", "Doubles grenades on bosses.")),
 dict(node="Iron Reflexes", type="Keystone", text=L("Converte toda a Evasion em Armour.", "Converts all Evasion Rating to Armour."), when="T15", why=L("Mais Armour = mais Deflection (Polish That Gear).", "More Armour = more Deflection (Polish That Gear).")),
 dict(node="Glancing Blows", type="Keystone", text=L("Evade fica Unlucky; Deflect fica Lucky.", "Chance to Evade is Unlucky; Chance to Deflect is Lucky."), when=L("Mapas 65+", "Maps 65+"), why=L("A build defende com Deflection, não com Evasion.", "The build defends with Deflection, not Evasion.")),
]
TREE_STAGES = [
 dict(lv="1–15", focus=L("Projétil e arma de duas mãos", "Projectile and two-handed"), dmg="Explosive/Gas Grenade", **{"def": L("Vida", "Life")}, spirit="Attrition", dont=L("Gastar Regal/Exalted cedo", "Spending Regal/Exalted early")),
 dict(lv="16–51", focus=L("Granadas + Pin + Armour Break", "Grenades + Pin + Armour Break"), dmg=L("Granadas + Explosive Shot", "Grenades + Explosive Shot"), **{"def": L("Armour + vida", "Armour + life")}, spirit=L("Attrition, Plating", "Attrition, Plating"), dont=L("Usar só uma granada", "Using only one grenade")),
 dict(lv="52–78", focus=L("Cooldown e área", "Cooldown and area"), dmg="Cluster Grenade + Mirage Archer", **{"def": L("Glancing Blows", "Glancing Blows")}, spirit="A Solid Plan", dont=L("Explosive Shot no Set 1 com Trarthan Cannon", "Explosive Shot on Set 1 with the Trarthan Cannon")),
 dict(lv="79–100", focus=L("Set 1 boss · Set 2 clear", "Set 1 boss · Set 2 clear"), dmg="Siege Crossbow", **{"def": L("Iron Reflexes + Deflection", "Iron Reflexes + Deflection")}, spirit=L("Rage (Eternal Rage + Berserk)", "Rage (Eternal Rage + Berserk)"), dont=L("Mapas com less Cooldown/Recovery", "Maps with less Cooldown/Recovery")),
]

UNIQUES = [
 U("Beira's Anguish", "Charm", "Charm", "t15", L("Charm que cria chão em chamas que acende inimigos com base na sua vida máxima, e chance de charge ao matar. Acende o óleo da Oil Grenade.", "A charm that creates Ignited Ground based on your maximum life, and chance to gain a charge on kill. It lights Oil Grenade's oil."), L("Em qualquer slot de charm.", "Any charm slot."), L("Dousing Charm normal.", "Normal Dousing Charm.")),
 U("Sanguis Heroum", "Charm", "Charm", "t15", L("Gera cargas sozinho e cria Consecrated Ground (regeneração) ao usar.", "Generates charges on its own and creates Consecrated Ground (regeneration) on use."), L("Ajuda a segurar a perda de vida do Berserk.", "Helps hold Berserk's life loss."), L("Staunching Charm normal.", "Normal Staunching Charm.")),
 U("Constricting Command", L("Capacete", "Helmet"), L("Armadura", "Armour"), "max", L("Vida, atributos, regeneração de vida e exige menos inimigos para ficar Surrounded.", "Life, attributes, life regeneration and requires fewer enemies to be Surrounded."), L("Aspiracional do BlazeworksTV.", "BlazeworksTV's aspirational pick."), L("Capacete rare de vida/Armour/resists.", "Rare life/Armour/resists helmet.")),
 U("The Fall of the Axe", "Charm", "Charm", "max", L("Dá Onslaught durante o efeito.", "Grants Onslaught during its effect."), L("Luxo.", "Luxury."), L("Silver Charm normal.", "Normal Silver Charm.")),
 U("Rite of Passage", "Charm", "Charm", "max", L("Possui você com espíritos animais aleatórios ao usar (buffs fortes).", "Possesses you with random animal spirits on use (strong buffs)."), L("Luxo do setup máximo.", "Luxury of the max setup."), L("Golden Charm.", "Golden Charm.")),
 U("Mageblood", L("Cinto", "Belt"), L("Acessório", "Accessory"), "max", L("Efeitos de flask permanentes (legados). O cinto mais caro do jogo.", "Permanent flask effects (legacies). The most expensive belt in the game."), L("Só depois da crossbow perfeita.", "Only after a perfect crossbow."), L("Cinto rare de vida/resists/Armour.", "Rare life/resists/Armour belt.")),
]

GEAR = [
 dict(slot=L("Crossbow", "Crossbow"), cheap=L("Craftada em cada salto: nível 16 → 33 → 59 (Cannonade)", "Crafted at each jump: level 16 → 33 → 59 (Cannonade)"), value=L("Trarthan Cannon (Set 1) + Cannonade (Set 2)", "Trarthan Cannon (Set 1) + Cannonade (Set 2)"), full=L("Siege Crossbow (nível 79) com dano alto", "Siege Crossbow (level 79) with high damage"), affix=L("+ nível de projéteis; % físico; dano adicionado; attack speed; Mana Leech", "+ projectile levels; % physical; added damage; attack speed; Mana Leech"), note=L("A arma é 70% do dano da build: invista nela primeiro.", "The weapon is 70% of the build's damage: invest in it first.")),
 dict(slot=L("Capacete", "Helmet"), cheap=L("Vida, Armour, resists", "Life, Armour, resists"), value=L("Rare de vida/Armour", "Rare life/Armour"), full="Constricting Command", affix=L("Vida; Armour; resist", "Life; Armour; resist"), note=""),
 dict(slot="Body Armour", cheap=L("Armour/Evasion com vida", "Armour/Evasion with life"), value=L("Base com implicit de Life Regeneration", "Base with a Life Regeneration implicit"), full=L("Ornate Plate com vida e Armour altas", "Ornate Plate with high life and Armour"), affix=L("Vida; Armour; resist", "Life; Armour; resist"), note=L("A regen do implicit paga a perda de vida do Berserk.", "The implicit's regen pays for Berserk's life loss.")),
 dict(slot=L("Luvas", "Gloves"), cheap=L("Dano adicionado + vida", "Added damage + life"), value=L("Raio adicionado (Shock) + Mana on Kill", "Added lightning (Shock) + Mana on Kill"), full=L("Rare com dano adicionado, vida e resists", "Rare with added damage, life and resists"), affix=L("Dano adicionado; vida; resist", "Added damage; life; resist"), note=""),
 dict(slot=L("Botas", "Boots"), cheap=L("Movement Speed", "Movement Speed"), value=L("30% MS + vida", "30% MS + life"), full=L("35% MS + vida + resists", "35% MS + life + resists"), affix=L("Movement Speed primeiro", "Movement Speed first"), note=""),
 dict(slot=L("Amuleto", "Amulet"), cheap=L("+ nível de projéteis", "+ projectile levels"), value=L("Spirit + vida", "Spirit + life"), full=L("Spirit alto + nível de projéteis", "High Spirit + projectile levels"), affix=L("Spirit; + nível de projéteis; vida", "Spirit; + projectile levels; life"), note=L("Spirit alto libera o Berserk.", "High Spirit unlocks Berserk.")),
 dict(slot=L("Anéis", "Rings"), cheap=L("Dano adicionado + resists", "Added damage + resists"), value=L("Raio adicionado + vida", "Added lightning + life"), full="Vitalic Ring", affix=L("Dano adicionado; vida; resist", "Added damage; life; resist"), note=""),
 dict(slot=L("Cinto", "Belt"), cheap=L("Vida/resists/Força", "Life/resists/Strength"), value=L("Vida + Armour", "Life + Armour"), full="Mageblood", affix=L("Resist; vida; Armour", "Resist; life; Armour"), note=""),
 dict(slot="Charms", cheap=L("Thawing + Dousing + Staunching", "Thawing + Dousing + Staunching"), value="Beira's Anguish · Sanguis Heroum", full="The Fall of the Axe · Rite of Passage", affix=L("Cobrir freeze/ignite/bleed", "Cover freeze/ignite/bleed"), note=""),
 dict(slot="Flasks", cheap=L("Vida + mana", "Life + mana"), value=L("Ultimate Life + Ultimate Mana", "Ultimate Life + Ultimate Mana"), full=L("Mesmo, com qualidade", "Same, with quality"), affix=L("Recuperação", "Recovery"), note=""),
]
BUY_ORDER = [
 dict(p=1, item=L("Crossbow craftada nível 16", "Crafted level 16 crossbow"), phase=L("Ato 2", "Act 2"), cost=L("Barato", "Cheap"), impact=L("Maior salto de dano da campanha", "Biggest damage jump of the campaign")),
 dict(p=2, item=L("Crossbow nível 33", "Level 33 crossbow"), phase=L("Ato 3", "Act 3"), cost=L("Barato", "Cheap"), impact=L("Dano até os Interlúdios", "Damage until the Interludes")),
 dict(p=3, item=L("Cannonade Crossbow nível 59", "Level 59 Cannonade Crossbow"), phase=L("Interlúdios", "Interludes"), cost=L("Barato", "Cheap"), impact=L("Dano para os mapas", "Damage for maps")),
 dict(p=4, item=L("Trarthan Cannon", "Trarthan Cannon"), phase=L("Mapas 65+", "Maps 65+"), cost=L("Barato", "Cheap"), impact=L("Mais físico nas granadas", "More physical on grenades")),
 dict(p=5, item=L("Amuleto com Spirit", "Amulet with Spirit"), phase=L("Mapas", "Maps"), cost=L("Valor", "Value"), impact=L("Eternal Rage + Berserk", "Eternal Rage + Berserk")),
 dict(p=6, item=L("Siege Crossbow", "Siege Crossbow"), phase="T15", cost=L("Valor", "Value"), impact=L("Arma final", "Final weapon")),
 dict(p=7, item="Beira's Anguish + Sanguis Heroum", phase="T15", cost=L("Barato", "Cheap"), impact=L("Ignite + regen", "Ignite + regen")),
 dict(p=8, item=L("Supports de Lineage", "Lineage supports"), phase="Pinnacle", cost=L("Luxo", "Luxury"), impact=L("Teto de dano", "Damage ceiling")),
]

TRICKS = [
 {"cat": "Pin", "lvl": L("Fácil", "Easy"), "title": L("Pin não tem cooldown interno", "Pin has no internal cooldown"), "body": L("Freeze, Stun e Electrocute têm limites; Pin não. Com Right Where We Want Them você prende o mesmo boss de novo e de novo, e inimigo Pinned não age.", "Freeze, Stun and Electrocute have limits; Pin doesn't. With Right Where We Want Them you pin the same boss again and again, and a Pinned enemy can't act.")},
 {"cat": "Pin", "lvl": L("Médio", "Medium"), "title": L("Pin quebra Armour", "Pin breaks Armour"), "body": L("Eroding Chains quebra 50% da Armour em cada Pin. Com Cruel Methods e The Molten One's Gift, Armour totalmente quebrada faz o inimigo tomar mais dano de fogo — e suas granadas são de fogo.", "Eroding Chains breaks 50% Armour on every Pin. With Cruel Methods and The Molten One's Gift, fully broken Armour makes the enemy take more fire damage — and your grenades are fire.")},
 {"cat": L("Granadas", "Grenades"), "lvl": L("Fácil", "Easy"), "title": L("Explosive Shot detona tudo", "Explosive Shot detonates everything"), "body": L("Granadas explodem sozinhas quando o pavio acaba. O Explosive Shot faz todas na área explodirem na hora — use quando não quiser esperar.", "Grenades explode on their own when the fuse ends. Explosive Shot makes all of them in the area explode instantly — use it when you don't want to wait.")},
 {"cat": L("Granadas", "Grenades"), "lvl": L("Fácil", "Easy"), "title": L("Gas + fogo = explosão", "Gas + fire = explosion"), "body": L("A nuvem da Gas Grenade explode quando pega fogo ou quando um Detonator acerta. Jogue a Explosive Grenade em cima da nuvem.", "Gas Grenade's cloud explodes when it catches fire or a Detonator hits it. Throw Explosive Grenade on top of the cloud.")},
 {"cat": L("Granadas", "Grenades"), "lvl": L("Médio", "Medium"), "title": L("Demolitionist: varie as granadas", "Demolitionist: vary your grenades"), "body": L("Cada granada diferente usada nos últimos 8 s dá 4% do dano como fogo extra. Com Explosive, Gas, Flash, Oil e Cluster são 20%.", "Each different grenade used in the last 8 s gives 4% of damage as extra fire. With Explosive, Gas, Flash, Oil and Cluster that's 20%.")},
 {"cat": L("Crossbow", "Crossbow"), "lvl": L("Médio", "Medium"), "title": L("Trarthan Cannon só carrega granadas", "The Trarthan Cannon only loads grenades"), "body": L("Ela tem mais dano físico base, mas não carrega virotes normais. Coloque a Cannonade no Weapon Set 2 com o Explosive Shot e marque cada skill no set certo (tecla G → seta ao lado do dano → Use With Weapon Set).", "It has higher base physical damage but can't load regular bolts. Put the Cannonade in Weapon Set 2 with Explosive Shot and assign each skill to the right set (G key → arrow next to damage → Use With Weapon Set).")},
 {"cat": L("Crossbow", "Crossbow"), "lvl": L("Fácil", "Easy"), "title": L("Perfect Essence of Battle", "Perfect Essence of Battle"), "body": L("Se a crossbow boa não tiver + nível de projéteis, a Perfect Essence of Battle (num item Rare) remove um mod aleatório e adiciona +3 to Level of all Attack Skills garantido — as granadas são ataques, então conta.", "If a good crossbow lacks + projectile levels, Perfect Essence of Battle (on a Rare) removes a random mod and adds a guaranteed +3 to Level of all Attack Skills — grenades are attacks, so it counts.")},
 {"cat": L("Defesa", "Defence"), "lvl": L("Médio", "Medium"), "title": L("Armour vira Deflection", "Armour becomes Deflection"), "body": L("Polish That Gear dá Deflection igual a 20% da Armour. Deflection faz o hit causar 40% menos dano. Glancing Blows deixa o Deflect Lucky; Iron Reflexes converte Evasion em Armour.", "Polish That Gear gives Deflection equal to 20% of Armour. Deflection makes the hit deal 40% less damage. Glancing Blows makes Deflect Lucky; Iron Reflexes converts Evasion into Armour.")},
 {"cat": L("Defesa", "Defence"), "lvl": L("Médio", "Medium"), "title": L("Berserk pede regen", "Berserk needs regen"), "body": L("Berserk fortalece a Rage, mas drena vida enquanto você não perde Rage. Body com implicit de Life Regeneration + Vitality + Sanguis Heroum seguram isso.", "Berserk strengthens Rage but drains life while you don't lose Rage. A body with a Life Regeneration implicit + Vitality + Sanguis Heroum hold it.")},
 {"cat": L("Mana", "Mana"), "lvl": L("Médio", "Medium"), "title": L("Mana sem flask", "Mana without flasks"), "body": L("Joias Ruby com % Skill Mana Costs Converted to Life Costs, Sapphire com Recover % Mana on Kill, Mana Leech na crossbow, Mana on Kill nas luvas e Mark of Siphoning no Pounce.", "Ruby jewels with % Skill Mana Costs Converted to Life Costs, Sapphire with Recover % Mana on Kill, Mana Leech on the crossbow, Mana on Kill on gloves and Mark of Siphoning on Pounce.")},
 {"cat": L("Mapas", "Maps"), "lvl": L("Fácil", "Easy"), "title": L("Regex de mapas perigosos", "Dangerous map regex"), "body": L("Cole na busca do stash para esconder mapas com less Recovery e less Cooldown: \"!less r|s coo\"", "Paste into stash search to hide maps with less Recovery and less Cooldown: \"!less r|s coo\"")},
 {"cat": L("Economia", "Economy"), "lvl": L("Fácil", "Easy"), "title": L("Regex de vendor", "Vendor regex"), "body": "\"!(uiv)\" \"cross|mov|[egdl] da.* to a\""},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Atributos", "Attributes"), "body": L("Coloque Destreza só o bastante para as gems; o resto vai em Força (vida).", "Put only as much Dexterity as your gems need; the rest goes into Strength (life).")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Weapon Set 2 com Talisman", "Weapon Set 2 with a Talisman"), "body": L("O Pounce exige Talisman. Deixe qualquer Talisman no Weapon Set 2 para o pulo; as granadas ficam no Set 1.", "Pounce requires a Talisman. Keep any Talisman in Weapon Set 2 for the leap; grenades stay on Set 1.")},
]

TROUBLESHOOT = [
 (L("Meu dano caiu nos mapas", "My damage dropped in maps"), L("Quase sempre é a crossbow. Veja + nível de projéteis e dano físico/adicionado; craft a próxima base (Cannonade 59, Trarthan Cannon 65, Siege 79).", "It's almost always the crossbow. Check + projectile levels and physical/added damage; craft the next base (Cannonade 59, Trarthan Cannon 65, Siege 79).")),
 (L("Explosive Shot não aparece", "Explosive Shot won't fire"), L("Com a Trarthan Cannon ele precisa estar SÓ no Weapon Set 2 com a Cannonade. Confira na tela de gems (G) → Use With Weapon Set.", "With the Trarthan Cannon it must be ONLY on Weapon Set 2 with the Cannonade. Check in the gem screen (G) → Use With Weapon Set.")),
 (L("Inimigos não ficam presos", "Enemies don't get pinned"), L("Antes de Right Where We Want Them só o dano físico com Pin I/II acumula Pin. Depois dele, qualquer projétil acumula. Suppressing Fire e Heft aceleram.", "Before Right Where We Want Them only physical damage with Pin I/II builds Pin. After it, any projectile builds it. Suppressing Fire and Heft speed it up.")),
 (L("Mana acaba", "Running out of mana"), L("Mark of Siphoning no Pounce, Clarity I, Mana Leech na crossbow, Mana on Kill nas luvas e joias de mana.", "Mark of Siphoning on Pounce, Clarity I, Mana Leech on the crossbow, Mana on Kill on gloves and mana jewels.")),
 (L("Perco vida parado", "I lose life standing still"), L("É o Berserk. Suba a regeneração (body com implicit, Vitality, Sanguis Heroum) ou desligue o Berserk.", "It's Berserk. Raise regeneration (implicit body, Vitality, Sanguis Heroum) or turn Berserk off.")),
 (L("Spirit não fecha", "Spirit doesn't add up"), L("Sem A Solid Plan, Eternal Rage (100) e Mirage Archer (60) não cabem. Pegue a 3ª ascendência antes de ligar os dois.", "Without A Solid Plan, Eternal Rage (100) and Mirage Archer (60) don't fit. Take the 3rd ascendancy before turning both on.")),
 (L("Granadas demoram a explodir", "Grenades take too long to explode"), L("Cluster Bombs aumenta o tempo de detonação. Compense com Volatile Grenades, Short Fuse I e o Explosive Shot.", "Cluster Bombs increases detonation time. Offset it with Volatile Grenades, Short Fuse I and Explosive Shot.")),
]

ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Resists no cap · Cluster Grenade 5L", "Resists capped · Cluster Grenade 5L"), gear="Cannonade Crossbow"),
 dict(stage="T1–T10", goal=L("A Solid Plan · Mirage Archer · Eternal Rage", "A Solid Plan · Mirage Archer · Eternal Rage"), gear="Trarthan Cannon + Cannonade"),
 dict(stage="T11–T15", goal=L("Iron Reflexes · Polish That Gear · mana resolvida", "Iron Reflexes · Polish That Gear · mana solved"), gear="Siege Crossbow + Spirit amulet"),
 dict(stage="Pinnacle", goal=L("Lineage supports · Berserk", "Lineage supports · Berserk"), gear="Constricting Command · Mageblood"),
]

CRAFT = [
 L("Crossbow em cada salto (16, 33, 59, 65, 79): base branca do vendor → Transmutation + Augmentation até sair 1 mod bom → Regal ou Essence of Abrasion → Exalted para completar.", "Crossbow at each jump (16, 33, 59, 65, 79): white vendor base → Transmutation + Augmentation until one good mod → Regal or Essence of Abrasion → Exalted to fill."),
 L("Jawbone (desecrate) adiciona um mod de Abyss: na crossbow, Amanamu tem +1 uso de cooldown e +101–121% dano de granada. Perfect Essence of Battle garante +3 nível de skills de ataque.", "A Jawbone (desecrate) adds an Abyss mod: on a crossbow, Amanamu has +1 cooldown use and +101–121% grenade damage. Perfect Essence of Battle guarantees +3 to Level of all Attack Skills."),
 L("Termine com Artificer's Orb (sockets) e Blacksmith's Whetstone (qualidade). Vaal Orb é aposta: pode melhorar ou estragar.", "Finish with Artificer's Orb (sockets) and Blacksmith's Whetstone (quality). Vaal Orb is a gamble: it can improve or brick the item."),
]

T("item", L("Crossbow nível 16", "Level 16 crossbow"), 16, L("Base do vendor da Shambrin (Ato 2)", "Base from Shambrin's vendor (Act 2)"), L("Ao chegar no Ardura Caravan.", "When you reach the Ardura Caravan."), L("O maior salto de dano da campanha.", "The campaign's biggest damage jump."),
  L("Guarde Regal/Alchemy/Exalted desde o Ato 1 para ela.", "Save Regal/Alchemy/Exalted from Act 1 for it."), L("Sem ela o Ato 2 fica lento.", "Without it Act 2 is slow."), [L("Transmutation + Augmentation até sair um mod bom.", "Transmutation + Augmentation until a good mod shows."), L("Regal ou Essence of Abrasion.", "Regal or Essence of Abrasion."), L("Exalted para completar, Artificer's Orb e Whetstones.", "Exalted to fill, Artificer's Orb and Whetstones.")])
T("item", "Cannonade Crossbow", 59, L("Nível 59 (vendor)", "Level 59 (vendor)"), L("Nível 59 nos Interlúdios.", "Level 59 in the Interludes."), L("Crossbow para os mapas e depois arma do Set 2 (Explosive Shot).", "Crossbow for maps and later the Set 2 weapon (Explosive Shot)."), L("Não compre antes: o nível trava.", "Don't buy early: the level locks it."), L("A crossbow 33 aguenta até lá.", "The level 33 crossbow holds until then."))
T("item", "Trarthan Cannon", 65, L("Nível 65, dropa a partir do T1", "Level 65, drops from T1"), L("Primeiros mapas.", "First maps."), L("Mais dano físico base; só carrega granadas.", "More base physical damage; only loads grenades."), L("Guarde bases boas desde o T1.", "Keep good bases from T1."), L("Se sua Cannonade for excelente, pode pular direto para a Siege.", "If your Cannonade is excellent, you can skip straight to the Siege."), [L("Set 1: Trarthan Cannon + granadas.", "Set 1: Trarthan Cannon + grenades."), L("Set 2: Cannonade + Explosive Shot.", "Set 2: Cannonade + Explosive Shot.")])
T("item", "Siege Crossbow", 79, L("Nível 79 (T15)", "Level 79 (T15)"), L("T15.", "T15."), L("Arma final da build.", "The build's final weapon."), L("Nível 79: guarde até lá.", "Level 79: keep it until then."), "—")
T("skill", "Cluster Grenade", 52, L("Gem nível 13", "Level 13 gem"), L("Nível 52, com Greater Jeweller's Orb.", "Level 52, with a Greater Jeweller's Orb."), L("Granada de área com mini-granadas.", "Area grenade with mini grenades."), L("Sem links fica fraca: espere o 4º/5º link.", "Weak without links: wait for the 4th/5th link."), "—")
T("skill", "Mirage Archer", 65, L("60 Spirit (30 com A Solid Plan)", "60 Spirit (30 with A Solid Plan)"), L("Com A Solid Plan.", "With A Solid Plan."), L("Cluster Grenade extra a cada dodge roll.", "Extra Cluster Grenade on every dodge roll."), L("Antes do A Solid Plan pesa muito no Spirit.", "Before A Solid Plan it weighs heavily on Spirit."), "—")
T("skill", "Eternal Rage", 65, L("100 Spirit (50 com A Solid Plan)", "100 Spirit (50 with A Solid Plan)"), L("Com A Solid Plan.", "With A Solid Plan."), L("Rage constante = mais dano de ataque.", "Constant Rage = more attack damage."), L("Não ligue sem A Solid Plan.", "Don't turn it on without A Solid Plan."), "—")
T("skill", "Berserk", 79, L("30 Spirit (15 com A Solid Plan)", "30 Spirit (15 with A Solid Plan)"), L("T15, com amuleto de Spirit.", "T15, with a Spirit amulet."), L("Rage mais forte.", "Stronger Rage."), L("Precisa de regen de vida.", "Needs life regen."), "—", watch=[L("Mapas com less Recovery of Life.", "Maps with less Life Recovery.")])
T("asc", "Right Where We Want Them", 40, L("Ascendência Tactician", "Tactician ascendancy"), L("2º Trial.", "2nd Trial."), L("Todo projétil dá Pin; Pinned não age.", "Every projectile builds Pin; Pinned enemies can't act."), "—", "—")
T("asc", "A Solid Plan", 65, L("Ascendência Tactician", "Tactician ascendancy"), L("3º Trial.", "3rd Trial."), L("50% less reserva de buffs persistentes.", "50% less reservation on persistent buffs."), "—", "—")
T("key", "Iron Reflexes", 79, L("Keystone da árvore", "Tree keystone"), L("T15.", "T15."), L("Evasion vira Armour.", "Evasion becomes Armour."), L("Antes do Polish That Gear o ganho é menor.", "Before Polish That Gear the gain is smaller."), "—")

CASES = [
 (L("Achei uma Trarthan Cannon ótima antes do nível 65", "I found a great Trarthan Cannon before level 65"), L("Guarde: ela exige nível 65. Até lá, fique na Cannonade.", "Keep it: it requires level 65. Until then, stay on the Cannonade.")),
 (L("Não tenho A Solid Plan ainda", "I don't have A Solid Plan yet"), L("Fique com Attrition + Scavenged Plating (60 Spirit). Mirage Archer e Eternal Rage só depois.", "Stay on Attrition + Scavenged Plating (60 Spirit). Mirage Archer and Eternal Rage only after.")),
 (L("Minha Cannonade é melhor que a Trarthan Cannon", "My Cannonade beats the Trarthan Cannon"), L("Use só a Cannonade no Set 1 com tudo (incluindo Explosive Shot) e pule para a Siege Crossbow no 79.", "Use only the Cannonade on Set 1 with everything (including Explosive Shot) and jump to the Siege Crossbow at 79.")),
]

SOURCES = [
 dict(name="BlazeworksTV — [0.5.5] SSF Pin2Win Grenades Tactician (Mobalytics)", use=L("Build base: 9 variantes, gems, itens, árvore, notas, rotação e craft da crossbow", "Base build: 9 variants, gems, items, tree, notes, rotation and crossbow craft"), url=GUIDE_URL),
 dict(name="poe.ninja — Tactician (Forbidden Rites)", use=L("Conferência do meta e preços dos uniques", "Meta check and unique prices"), url="https://poe.ninja/poe2/builds/forbiddenrites?class=Tactician"),
 dict(name="Path of Building (PoE2) — Gems.lua, Skills", use=L("Descrições das gems, custos de Spirit e tiers", "Gem descriptions, Spirit costs and tiers"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name=L("Árvore 0.5 (Path of Building)", "0.5 tree (Path of Building)"), use=L("Nós, ascendência Tactician e keystones", "Nodes, Tactician ascendancy and keystones"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
]
FIXES = [
 L("As variantes 'Endgame Update 1' (Stormcaller Arrow) e 'Bleed/Crit Siege Cascade (WIP)' não entram na rota: o próprio autor abandonou a primeira e marca a segunda como experimental.", "The 'Endgame Update 1' (Stormcaller Arrow) and 'Bleed/Crit Siege Cascade (WIP)' variants aren't in the route: the author abandoned the first and marks the second as experimental."),
 L("Custos de Spirit conferidos nos dados do Path of Building: Mirage Archer 60, Eternal Rage 100, Berserk 30, Scavenged Plating 30, Attrition 30 (metade com A Solid Plan, arredondado para cima).", "Spirit costs checked in Path of Building data: Mirage Archer 60, Eternal Rage 100, Berserk 30, Scavenged Plating 30, Attrition 30 (half with A Solid Plan, rounded up)."),
 L("Os níveis de ascendência são aproximados (Trials variam por jogador).", "Ascendancy levels are approximate (Trials vary per player)."),
]

UI = dict(
 carry=r"^(Cluster Grenade|Explosive Grenade)$", box=L("GRANADAS", "GRENADES"), spiritWhat=L("(buffs persistentes)", "(persistent buffs)"),
 mechBtn=L("Abrir Pin & Granadas", "Open Pin & Grenades"), dmg2="Mirage Archer", dmgBar=L("Dano seu / do Mirage Archer (aprox.)", "Your damage / Mirage Archer damage (approx.)"),
 dmgLegend=L("dano do Mirage Archer (proporção aproximada)", "Mirage Archer damage (approximate ratio)"),
 earlyGone=L("Skills iniciais já saíram da barra: você passou do nível {u}.", "Starting skills already left the bar: you're past level {u}."),
 earlyNote=L("Skills de começo; saem no nível ~{u}.", "Early skills; they leave around level {u}."),
 treeIntro=L("Árvore real do patch 0.5.5 com o caminho do guia do BlazeworksTV em cada fase. Atos 1–2: projétil e granadas. Ato 3: Pin, Armour Break e fogo. Mapas: cooldown, área e Glancing Blows. T15: Iron Reflexes e weapon sets.", "Real patch 0.5.5 tree with BlazeworksTV's guide path for each phase. Acts 1–2: projectile and grenades. Act 3: Pin, Armour Break and fire. Maps: cooldown, area and Glancing Blows. T15: Iron Reflexes and weapon sets."),
 set1=L("dano de boss e fogo", "boss and fire damage"), set2=L("cooldown para o clear", "cooldown for clear"), asc="Tactician", cls="Mercenary",
 respecTip=L("Na troca para a Trarthan Cannon/Siege Crossbow, compare com a fase anterior: nós sem contorno verde já eram seus. Weapon Set 1 = boss; Set 2 = clear.", "When moving to the Trarthan Cannon/Siege Crossbow, compare with the previous phase: nodes without a green outline were already yours. Weapon Set 1 = boss; Set 2 = clear."),
 routeIntro=L("Sete fases do guia do BlazeworksTV. A crossbow muda em 16, 33, 59, 65 e 79; o Pin vira controle total no Ato 3.", "Seven phases from BlazeworksTV's guide. The crossbow changes at 16, 33, 59, 65 and 79; Pin becomes full control in Act 3."),
 socketPrio=["Explosive Grenade", "Cluster Grenade (Greater Jeweller's Orb)", "Flash Grenade · Oil Grenade", "Explosive Shot · Gas Grenade", "Mirage Archer"],
 permIntro=L("Nada disso volta depois. Spirit paga Attrition, Scavenged Plating e, com A Solid Plan, Mirage Archer, Eternal Rage e Berserk. Os Weapon Set Points alimentam o Set 1 (boss) e o Set 2 (clear).", "None of this comes back later. Spirit pays for Attrition, Scavenged Plating and, with A Solid Plan, Mirage Archer, Eternal Rage and Berserk. Weapon Set Points fuel Set 1 (boss) and Set 2 (clear)."),
 atlasCards=[[L("Mapas que atrapalham", "Maps that hurt"), L("Evite less Cooldown Recovery (granadas) e less Recovery of Life/ES (Berserk). Regex no stash: \"!less r|s coo\".", "Avoid less Cooldown Recovery (grenades) and less Life/ES Recovery (Berserk). Stash regex: \"!less r|s coo\".")],
             [L("Farm de crossbow", "Crossbow farming"), L("A partir do T1 guarde bases de Trarthan Cannon; no T15 (nível 79), Siege Crossbow. A arma é o upgrade que mais rende.", "From T1 keep Trarthan Cannon bases; at T15 (level 79), Siege Crossbow. The weapon is the upgrade that pays off most.")]],
 foot=L("Guia baseado no build do BlazeworksTV (Mobalytics), dados de jogo do Path of Building e preços do poe.ninja", "Guide based on BlazeworksTV's build (Mobalytics), Path of Building game data and poe.ninja prices"),
)

CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens, Árvore e Pin & Granadas se adaptam na hora ao seu Spirit e ao que você marcou. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items, Tree and Pin & Grenades tabs adapt instantly to your Spirit and what you ticked. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit máximo", "Max Spirit"), L("ex.: 110", "e.g. 110")], ["life", L("Vida máxima", "Max life"), ""], ["armour", "Armour", ""]],
 tiles=[[L("Spirit reservado", "Spirit reserved"), "used"], [L("Spirit livre", "Spirit free"), "free"], ["Armour", "armour"]],
 halve="asp", halveLabel=L("A Solid Plan (50% less reserva)", "A Solid Plan (50% less reservation)"), halveTip=L("A Solid Plan corta todas pela metade.", "A Solid Plan halves all of them."),
 buffs=[dict(key="attr", name="Attrition", cost=30), dict(key="plating", name="Scavenged Plating", cost=30), dict(key="mirage", name="Mirage Archer", cost=60), dict(key="rage", name="Eternal Rage", cost=100), dict(key="berserk", name="Berserk", cost=30)],
 own=[
  ["gear", "xb16", L("Crossbow craftada nível 16", "Crafted level 16 crossbow")], ["gear", "xb33", L("Crossbow nível 33", "Level 33 crossbow")], ["gear", "cannonade", "Cannonade Crossbow"],
  ["gear", "trarthan", "Trarthan Cannon"], ["gear", "siege", "Siege Crossbow"], ["gear", "spamu", L("Amuleto com Spirit alto", "High-Spirit amulet")], ["gear", "talisman", L("Talisman no Weapon Set 2", "Talisman in Weapon Set 2")],
  ["gear", "Beira's Anguish", "Beira's Anguish"], ["gear", "Sanguis Heroum", "Sanguis Heroum"], ["gear", "Constricting Command", "Constricting Command"], ["gear", "Mageblood", "Mageblood"],
  ["gem", "attr", "Attrition (30)"], ["gem", "plating", "Scavenged Plating (30)"], ["gem", "mirage", "Mirage Archer (60)"], ["gem", "rage", "Eternal Rage (100)"], ["gem", "berserk", "Berserk (30)"],
  ["gem", "eshot", "Explosive Shot"], ["gem", "oil", "Oil Grenade"], ["gem", "cluster", "Cluster Grenade"],
  ["tree", "eroding", "Eroding Chains"], ["tree", "molten", "The Molten One's Gift"], ["tree", "demo", "Demolitionist"], ["tree", "grenadier", "Grenadier"], ["tree", "glancing", "Glancing Blows"], ["tree", "iron", "Iron Reflexes"],
  ["asc", "sf", "Suppressing Fire"], ["asc", "rwwwt", "Right Where We Want Them"], ["asc", "asp", "A Solid Plan"], ["asc", "ptg", "Polish That Gear"],
 ],
 rules=[
  dict(when=dict(lvMin=16, notOwn=["xb16", "xb33", "cannonade", "trarthan", "siege"]), lvl="bad", t=L("Falta a crossbow craftada", "Crafted crossbow missing"), d=L("No Ardura Caravan (Ato 2) craft a crossbow nível 16 com toda a currency guardada: é o maior salto de dano da campanha.", "At the Ardura Caravan (Act 2) craft the level 16 crossbow with all saved currency: it's the campaign's biggest damage jump."), tab="gear"),
  dict(when=dict(lvMin=36, notOwn=["xb33", "cannonade", "trarthan", "siege"]), lvl="warn", t=L("Hora da crossbow nível 33", "Time for the level 33 crossbow"), d=L("No Ziggurat Encampment (Ato 3), mesma receita.", "In the Ziggurat Encampment (Act 3), same recipe."), tab="gear"),
  dict(when=dict(lvMin=60, notOwn=["cannonade", "trarthan", "siege"]), lvl="warn", t=L("Procure a Cannonade Crossbow", "Look for the Cannonade Crossbow"), d=L("Vendor no nível 59 dos Interlúdios.", "Vendor at level 59 in the Interludes."), tab="gear"),
  dict(when=dict(lvMin=24, notOwn=["eshot"]), lvl="warn", t=L("Sem Explosive Shot", "No Explosive Shot"), d=L("Ele detona as granadas na hora (nível 22).", "It detonates grenades instantly (level 22)."), tab="skills"),
  dict(when=dict(lvMin=40, notOwn=["oil"]), lvl="tip", t=L("Oil Grenade no lugar da Frost Bomb", "Oil Grenade instead of Frost Bomb"), d=L("Exposure mais forte e óleo que pega fogo.", "Stronger Exposure and oil that catches fire."), tab="skills"),
  dict(when=dict(lvMin=55, notOwn=["cluster"]), lvl="warn", t=L("Sem Cluster Grenade", "No Cluster Grenade"), d=L("É o skill de área dos mapas (nível 52).", "It's the map-clearing skill (level 52)."), tab="skills"),
  dict(when=dict(own=["rage"], notOwn=["asp"]), lvl="bad", t=L("Eternal Rage sem A Solid Plan", "Eternal Rage without A Solid Plan"), d=L("São 100 Spirit. Pegue A Solid Plan (3º Trial) antes.", "That's 100 Spirit. Take A Solid Plan (3rd Trial) first."), tab="asc"),
  dict(when=dict(own=["mirage"], notOwn=["cluster"]), lvl="warn", t=L("Mirage Archer sem Cluster Grenade", "Mirage Archer without Cluster Grenade"), d=L("O Mirage usa a Cluster Grenade socketada nele.", "The Mirage uses the Cluster Grenade socketed in it."), tab="skills"),
  dict(when=dict(own=["trarthan"], notOwn=["cannonade"]), lvl="warn", t=L("Trarthan Cannon sem crossbow no Set 2", "Trarthan Cannon without a Set 2 crossbow"), d=L("Ela não carrega virotes: o Explosive Shot precisa da Cannonade no Weapon Set 2.", "It can't load bolts: Explosive Shot needs the Cannonade in Weapon Set 2."), tab="mech"),
  dict(when=dict(own=["berserk"], notOwn=["Sanguis Heroum"]), lvl="tip", t=L("Berserk: cuide da regen", "Berserk: mind the regen"), d=L("Body com implicit de Life Regeneration, Vitality e Sanguis Heroum seguram a perda de vida.", "A body with a Life Regeneration implicit, Vitality and Sanguis Heroum hold the life loss."), tab="gear"),
  dict(when=dict(lvMin=36, notOwn=["eroding"]), lvl="warn", t=L("Eroding Chains não pego", "Eroding Chains not taken"), d=L("Cada Pin quebra 50% da Armour: é o que liga Pin ao dano de fogo.", "Every Pin breaks 50% Armour: it's what ties Pin to fire damage."), tab="arvore"),
  dict(when=dict(lvMin=36, notOwn=["demo"]), lvl="tip", t="Demolitionist", d=L("+4% do dano como fogo por granada diferente.", "+4% of damage as fire per different grenade."), tab="arvore"),
  dict(when=dict(own=["iron"], notOwn=["ptg"]), lvl="tip", t=L("Iron Reflexes antes do Polish That Gear", "Iron Reflexes before Polish That Gear"), d=L("Sem Polish That Gear a Armour não vira Deflection: o ganho é bem menor.", "Without Polish That Gear, Armour doesn't become Deflection: the gain is much smaller."), tab="asc"),
  dict(when=dict(lvMin=10, lvMax=30, notOwn=["talisman"]), lvl="tip", t=L("Talisman para o Pounce", "Talisman for Pounce"), d=L("Qualquer Talisman no Weapon Set 2 libera o pulo.", "Any Talisman in Weapon Set 2 unlocks the leap."), tab="skills"),
 ],
)
ADAPT_SWAPS = [
 dict(pid="t15", when=dict(notOwn=["siege"], own=["trarthan"]), gemsFrom="cannon", note=L("Sem Siege Crossbow: mostrando o setup Trarthan Cannon + Cannonade.", "No Siege Crossbow: showing the Trarthan Cannon + Cannonade setup.")),
 dict(pids=["cannon", "t15", "max"], when=dict(notOwn=["asp"]), gemsFrom="int", note=L("Sem A Solid Plan: mostrando o setup dos Interlúdios (Attrition + Scavenged Plating).", "No A Solid Plan: showing the Interludes setup (Attrition + Scavenged Plating).")),
]
TREE_RULES = [
 dict(when=dict(lvMin=36, notOwn=["eroding"]), t=L("Pegue Eroding Chains: Pin quebra 50% da Armour.", "Take Eroding Chains: Pin breaks 50% Armour."), node="Eroding Chains"),
 dict(when=dict(lvMin=36, notOwn=["molten"]), t=L("The Molten One's Gift transforma Armour quebrada em dano de fogo.", "The Molten One's Gift turns broken Armour into fire damage."), node="The Molten One's Gift"),
 dict(when=dict(own=["ptg"], notOwn=["iron"], lvMin=79), t=L("Com Polish That Gear, Iron Reflexes converte Evasion em Armour/Deflection.", "With Polish That Gear, Iron Reflexes turns Evasion into Armour/Deflection."), node="Iron Reflexes"),
]
TIMING_KEY = {"Siege Crossbow": "siege", "Trarthan Cannon": "trarthan", "Cannonade Crossbow": "cannonade", "Cluster Grenade": "cluster", "Mirage Archer": "mirage", "Eternal Rage": "rage", "Berserk": "berserk",
              "Right Where We Want Them": "rwwwt", "A Solid Plan": "asp", "Iron Reflexes": "iron", "Crossbow nível 16": "xb16", "Level 16 crossbow": "xb16"}

MECH = dict(
 title=L("Pin & Granadas", "Pin & Grenades"),
 intro=L("Como a build mata e se defende: Pin prende, granadas explodem, Armour quebrada vira fogo. Marque suas granadas para ver o bônus do Demolitionist e planeje o Spirit dos buffs.", "How the build kills and defends: Pin holds, grenades explode, broken Armour becomes fire. Tick your grenades to see the Demolitionist bonus and plan your buffs' Spirit."),
 sections=[
  dict(type="cards", cards=[
   [L("1. Pin", "1. Pin"), L("Pin é uma barra que enche com dano (físico com Pin I/II; qualquer projétil depois de Right Where We Want Them). Cheia, o inimigo fica preso e — com essa ascendência — não pode agir. Sem cooldown interno: dá para prender de novo.", "Pin is a bar that fills with damage (physical with Pin I/II; any projectile after Right Where We Want Them). When full, the enemy is held and — with that ascendancy — can't act. No internal cooldown: you can pin again.")],
   [L("2. Armour quebrada", "2. Broken Armour"), L("Eroding Chains quebra 50% da Armour a cada Pin; Flash Grenade com Armour Break III termina o serviço. Fully Broken Armour dá stacks de Scavenged Plating e, com The Molten One's Gift, aumenta o dano de fogo que o alvo recebe.", "Eroding Chains breaks 50% Armour on every Pin; Flash Grenade with Armour Break III finishes the job. Fully Broken Armour grants Scavenged Plating stacks and, with The Molten One's Gift, increases the fire damage the target takes.")],
   [L("3. Detonação", "3. Detonation"), L("Granadas explodem no fim do pavio. Explosive Shot (e a Explosive Grenade) são Detonators: explodem as outras na hora, acendem o óleo da Oil Grenade e fazem a nuvem da Gas Grenade virar uma bola de fogo.", "Grenades explode when the fuse ends. Explosive Shot (and Explosive Grenade) are Detonators: they pop the others instantly, light Oil Grenade's oil and turn Gas Grenade's cloud into a fireball.")],
   [L("4. Cooldown", "4. Cooldown"), L("Granadas têm cooldown com usos. Grenadier dá +1 uso; Cooldown Recovery no Weapon Set 2 deixa a Cluster Grenade quase em spam. Mapas com less Cooldown Recovery são os piores para a build.", "Grenades have cooldowns with uses. Grenadier gives +1 use; Cooldown Recovery on Weapon Set 2 makes Cluster Grenade near-spammable. Maps with less Cooldown Recovery are the worst for the build.")],
  ]),
  dict(type="counter", h=L("Demolitionist: granadas nos últimos 8 segundos", "Demolitionist: grenades in the last 8 seconds"), p=L("Marque as granadas diferentes da sua rotação.", "Tick the different grenades in your rotation."),
       items=[["g_exp", "Explosive Grenade"], ["g_gas", "Gas Grenade"], ["g_flash", "Flash Grenade"], ["g_oil", "Oil Grenade"], ["g_cluster", "Cluster Grenade"]], per=4,
       result=L("{n} granada(s) diferente(s) = {v}% do dano como fogo extra", "{n} different grenade(s) = {v}% of damage as extra fire"),
       text=L("Precisa do notable Demolitionist. Lance todas dentro de 8 segundos no boss.", "Requires the Demolitionist notable. Throw them all within 8 seconds on the boss.")),
  dict(type="rotation", blocks=[
   [L("Boss (T15)", "Boss (T15)"), [L("Oil Grenade: Exposure + Ignite", "Oil Grenade: Exposure + Ignite"), L("Flash Grenade: Pin + Armour Break", "Flash Grenade: Pin + Armour Break"), L("Explosive Grenades (todos os usos)", "Explosive Grenades (every use)"), L("Explosive Shot detona", "Explosive Shot detonates"), L("Dodge roll entre as granadas: Mirage Archer", "Dodge roll between grenades: Mirage Archer")]],
   [L("Clear (mapas)", "Clear (maps)"), [L("Cluster Grenade no pack", "Cluster Grenade into the pack"), L("Explosive Shot para não esperar o pavio", "Explosive Shot so you don't wait for the fuse"), L("Flash Grenade nos rares", "Flash Grenade on rares"), L("Oil Grenade em packs densos", "Oil Grenade on dense packs"), L("Dodge roll para o Mirage jogar mais Cluster", "Dodge roll so the Mirage throws more Cluster")]],
  ]),
  dict(type="table", h=L("Weapon sets por fase", "Weapon sets per phase"), cols=[L("Fase", "Phase"), "Weapon Set 1", "Weapon Set 2"], rows=[
   [L("Atos 1–4", "Acts 1–4"), L("Crossbow + tudo", "Crossbow + everything"), L("Talisman (Pounce)", "Talisman (Pounce)")],
   [L("Mapas 65+", "Maps 65+"), L("Trarthan Cannon + granadas", "Trarthan Cannon + grenades"), L("Cannonade + Explosive Shot", "Cannonade + Explosive Shot")],
   ["T15+", L("Siege Crossbow: boss (Oil, Flash, Explosive, Explosive Shot)", "Siege Crossbow: boss (Oil, Flash, Explosive, Explosive Shot)"), L("Siege Crossbow: Cluster Grenade + Cooldown Recovery", "Siege Crossbow: Cluster Grenade + Cooldown Recovery")],
   [L("Sempre", "Always"), L("Buffs persistentes nos dois sets", "Persistent buffs on both sets"), L("Buffs persistentes nos dois sets", "Persistent buffs on both sets")],
  ]),
  dict(type="spirit", h=L("Spirit dos buffs", "Buff Spirit"), p=L("Marque o que você usa. Custos do Path of Building.", "Tick what you use. Costs from Path of Building."),
       note=L("Ordem: Mirage Archer → Eternal Rage → Berserk → Scavenged Plating. Se faltar, desligue o último.", "Order: Mirage Archer → Eternal Rage → Berserk → Scavenged Plating. If short, turn off the last one.")),
  dict(type="timeline", h=L("Crossbow por nível", "Crossbow by level"), items=[
   dict(lv=16, t=L("Crossbow craftada (Ardura Caravan)", "Crafted crossbow (Ardura Caravan)"), d=L("Transmutation + Augmentation → Regal/Essence of Abrasion → Exalted → Artificer's Orb + Whetstones.", "Transmutation + Augmentation → Regal/Essence of Abrasion → Exalted → Artificer's Orb + Whetstones.")),
   dict(lv=33, t=L("Crossbow nível 33 (Ziggurat Encampment)", "Level 33 crossbow (Ziggurat Encampment)"), d=L("Mesma receita; Gnawed Jawbone se tiver.", "Same recipe; Gnawed Jawbone if you have one.")),
   dict(lv=59, t="Cannonade Crossbow", d=L("Vendor dos Interlúdios. Greater Essence of Abrasion.", "Interludes vendor. Greater Essence of Abrasion.")),
   dict(lv=65, t="Trarthan Cannon", d=L("Dropa a partir do T1. Set 1 com granadas; Cannonade no Set 2.", "Drops from T1. Set 1 with grenades; Cannonade in Set 2.")),
   dict(lv=79, t="Siege Crossbow", d=L("T15. Perfect Essence of Battle (+3 nível de ataque) se faltar nível na arma.", "T15. Perfect Essence of Battle (+3 attack skill levels) if the weapon lacks levels.")),
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
        if q["boss"] == "Tribal Medicine":
            q["reward"] = L("ESCOLHA: 30% increased Armour, Evasion e ES (BlazeworksTV)", "CHOICE: 30% increased Armour, Evasion and ES (BlazeworksTV)"); q["prio"] = "CRÍTICA"
        if q["boss"] == "Venom Draught":
            q["reward"] = L("ESCOLHA: 25% Stun Threshold", "CHOICE: 25% Stun Threshold"); q["prio"] = "Média"
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="15/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=GUIDE_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=BOOK.TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None,
                ui=UI, char=CHAR, mech=MECH, adaptSwaps=ADAPT_SWAPS, treeRules=TREE_RULES, timingKey=TIMING_KEY, phaseAct=PHASE_ACT, treeOrder=ORDER + ["uber"], craftKit=CRAFT_KIT)
