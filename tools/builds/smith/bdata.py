# -*- coding: utf-8 -*-
"""Smith of Kitava Shield Wall + Avatar of Fire — dados da página (PT com pares EN). Base: guia do Lexd (Mobalytics, 0.5.5),
árvore/gems/itens das variantes do guia, textos do jogo pelo Path of Building e preços do poe.ninja (Forbidden Rites)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "kit"))
import common

BOOK = common.Book(); L, G, U, T = BOOK.L, BOOK.G, BOOK.U, BOOK.T; EN_PAIRS = BOOK.EN_PAIRS; BOOK.common_pairs()
V, VAR = common.variants("smith")

GUIDE_URL = "https://mobalytics.gg/poe-2/builds/avatar-of-fire-smith-of-kitava-lexd"
LEAGUE = "Forbidden Rites"
PATCH = L("0.5.5 · Liga Forbidden Rites", "0.5.5 · Forbidden Rites league")
UPDATED = "17/09/2026"

CONFIG = dict(dir="smith", build="smith", store="smith1", emoji="🛡️", pill="Warrior · Smith of Kitava",
              fonts="family=Cinzel:wght@500;700;900&family=Barlow+Condensed:wght@500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400")
TXT = {
 "pt": dict(TITLE="Forja de Kitava", DESC="Guia interativo Smith of Kitava Shield Wall + Avatar of Fire (Warrior) — PoE 2 Forbidden Rites",
            H1S="Shield Wall + Avatar of Fire · escudo, fogo e armadura · guia do Lexd explicado", H1="A Forja de Kitava",
            LEAD="O Warrior mais tanque do jogo: muros de terra que explodem em fogo, Ignite no boss e uma body armour forjada pela ascendência. Diga seu nível e o que você tem: o guia mostra skills, escudo e maça da fase, passivas e o Spirit das suas auras."),
 "en": dict(TITLE="Kitava's Forge", DESC="Interactive Smith of Kitava Shield Wall + Avatar of Fire (Warrior) guide — PoE 2 Forbidden Rites",
            H1S="Shield Wall + Avatar of Fire · shield, fire and armour · Lexd's guide explained", H1="Kitava's Forge",
            LEAD="The tankiest Warrior in the game: walls of earth that explode into fire, Ignite on bosses and a body armour forged by your ascendancy. Tell it your level and what you have: the guide shows skills, the shield and mace for your phase, passives and your auras' Spirit."),
}
TABS = [["agora", "Agora", "Now"], ["meu", "Meu personagem", "My character"], ["quando", "Quando usar", "When to use"], ["mech", "Escudo & Fogo", "Shield & Fire"],
        ["uniques", "Uniques", "Uniques"], ["arvore", "Árvore de Passivas", "Passive Tree"], ["rota", "Rota 1→100", "Route 1→100"], ["skills", "Skills & Supports", "Skills & Supports"],
        ["gear", "Itens", "Items"], ["asc", "Ascendência", "Ascendancy"], ["quests", "Quests", "Quests"], ["tricks", "Tricks Pro", "Pro Tricks"], ["atlas", "Atlas", "Atlas"],
        ["diag", "Diagnóstico", "Troubleshooting"], ["fontes", "Fontes", "Sources"]]

CLASS, ASC, START = "Warrior", "Smith of Kitava", 47175
ORDER = ["a1", "a2", "a3", "a4", "int", "maps", "t10", "t15", "max"]
VMAP = {"a1": "Act 1", "a2": "Act 2", "a3": "Act 3", "a4": "Act 4", "int": "Interludes", "maps": "Mapping Start (Tiers 1-5, SSF Friendly)",
        "t10": "Mapping Endgame (5-10, SSF Friendly)", "t15": "Mapping Endgame (10 - 15)", "max": "Nebuloch + Constricting Command Optimized"}
VITEMS = {"a3": ["Act 2", "Act 3"], "a4": ["Act 2", "Act 4"], "int": ["Act 2", "Act 4", "Interludes"]}
CHEAPMAP = {"a1": "a1", "a2": "a2", "a3": "a3", "a4": "a4", "int": "int", "maps": "maps", "t10": "maps", "t15": "t10", "max": "t15"}
FULLMAP = {k: k for k in ORDER}
PHASE_ACT = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "int": 5, "maps": 6, "t10": 6, "t15": 6, "max": 6}
SHIELD_RUNE = L("Iron Rune (% Armour) ou Body Rune (vida)", "Iron Rune (% Armour) or Body Rune (life)")
MACE_RUNE = L("Storm Rune (raio para Shock) até o Avatar of Fire; depois Desert Rune (fogo)", "Storm Rune (lightning for Shock) until Avatar of Fire; then Desert Rune (fire)")

def socket_hint(slot, name):
    if "Shield" in name: return [SHIELD_RUNE]
    if "Mace" in name or "Hammer" in name: return [MACE_RUNE]
    if slot in ("Capacete", "Body Armour", "Luvas", "Botas"):
        return [L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio) · resist no cap: Body Rune (vida)", "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning) · resists capped: Body Rune (life)")]
    return None

SUPWHY = {
 "Rage I": L("Ataques corpo a corpo dão Rage ao acertar. Rage = mais dano de ataque.", "Melee attacks grant Rage on hit. Rage = more attack damage."),
 "Rage II": L("Mais Rage por hit.", "More Rage per hit."),
 "Rage III": L("Rage por hit e muito mais attack speed enquanto você não está no máximo de Rage.", "Rage per hit and much more attack speed while you're not at maximum Rage."),
 "Rapid Attacks I": L("Ataca mais rápido.", "Attacks faster."),
 "Rapid Attacks II": L("Versão mais forte do Rapid Attacks.", "Stronger Rapid Attacks."),
 "Rapid Attacks III": L("Ataca bem mais rápido em troca de dano: bom em skills de utilidade (Shield Charge, Sunder).", "Attacks much faster at the cost of damage: good on utility skills (Shield Charge, Sunder)."),
 "Steadfast I": L("Mais Stun Threshold enquanto você segura o Raise Shield.", "More Stun Threshold while holding Raise Shield."),
 "Steadfast II": L("Stun e Ailment Threshold maiores enquanto canaliza o escudo.", "Higher Stun and Ailment Threshold while channelling the shield."),
 "Brink I": L("O Shield Bash acumula Heavy Stun muito mais rápido (mas não dá o Heavy Stun sozinho): deixa o pack pronto para o Boneshatter.", "Shield Bash builds Heavy Stun much faster (but can't Heavy Stun by itself): primes the pack for Boneshatter."),
 "Impact Shockwave": L("Boneshatter cria um Aftershock em volta do alvo quando dá Heavy Stun: limpa o pack.", "Boneshatter creates an Aftershock around the target on Heavy Stun: clears the pack."),
 "Fire Attunement": L("Ganha dano de fogo extra. A build inteira vira fogo com Avatar of Fire.", "Gains extra fire damage. The whole build turns to fire with Avatar of Fire."),
 "Magnified Area I": L("Área maior.", "Larger area."),
 "Magnified Area II": L("Área ainda maior.", "Even larger area."),
 "Stun I": L("Acumula Stun mais rápido.", "Builds Stun faster."),
 "Stun II": L("Stun mais rápido ainda.", "Even faster Stun."),
 "Stun III": L("Stun bem mais rápido em troca de dano.", "Much faster Stun at the cost of damage."),
 "Armour Demolisher I": L("Armour Break mais forte: Fully Broken Armour chega antes.", "Stronger Armour Break: Fully Broken Armour comes sooner."),
 "Armour Demolisher II": L("Versão mais forte do Armour Demolisher.", "Stronger Armour Demolisher."),
 "Armour Break III": L("Quebra Armour com dano físico e dá chance de Endurance Charge ao quebrar tudo — alimenta Nebuloch e Fortifying Cry.", "Breaks Armour with physical damage and gives a chance for an Endurance Charge on full break — feeds Nebuloch and Fortifying Cry."),
 "Raging Cry": L("Warcry dá Rage conforme o Power dos monstros por perto.", "Warcries grant Rage based on nearby monster Power."),
 "Tireless": L("Ataques empoderados pelo warcry têm chance de não gastar o empower: mais Shield Walls fortes por grito.", "Attacks empowered by the warcry may not consume the empower: more strong Shield Walls per shout."),
 "Enduring Impact I": L("Chance de Endurance Charge ao dar Heavy Stun.", "Chance to gain an Endurance Charge on Heavy Stun."),
 "Enduring Impact II": L("Mais chance de Endurance Charge no Heavy Stun.", "Higher chance of an Endurance Charge on Heavy Stun."),
 "Charge Profusion I": L("Chance de gerar uma charge extra: mais Endurance Charges do Magma Barrier.", "Chance to generate an extra charge: more Endurance Charges from Magma Barrier."),
 "Charge Profusion II": L("Mais charges extras, inclusive de tipo aleatório.", "More extra charges, including a random type."),
 "Close Combat I": L("Mais dano quanto mais perto o inimigo.", "More damage the closer the enemy is."),
 "Close Combat II": L("Versão mais forte do Close Combat.", "Stronger Close Combat."),
 "Scavenged Plating": L("", ""),
 "Prolonged Duration I": L("Mais duração (Scavenged Plating, Sundered Armour).", "Longer duration (Scavenged Plating, Sundered Armour)."),
 "Prolonged Duration II": L("Versão mais forte do Prolonged Duration.", "Stronger Prolonged Duration."),
 "Elemental Armament I": L("More dano elemental nos ataques.", "More elemental damage on attacks."),
 "Elemental Armament II": L("Versão mais forte do Elemental Armament.", "Stronger Elemental Armament."),
 "Fire Exposure": L("Ao dar Ignite, aplica Fire Exposure: o boss perde resistência a fogo.", "On Ignite, applies Fire Exposure: the boss loses fire resistance."),
 "Enraged Warcry I": L("Gasta Rage para ignorar o cooldown do warcry.", "Spends Rage to bypass the warcry's cooldown."),
 "Enraged Warcry II": L("Versão mais forte: mais gritos por luta gastando Rage.", "Stronger version: more shouts per fight by spending Rage."),
 "Lifetap": L("Troca o custo de mana por vida. Some quando você pega Blood Magic.", "Turns mana cost into life cost. Goes away once you take Blood Magic."),
 "Vitality I": L("Regeneração de vida enquanto a skill persistente está ativa.", "Life regeneration while the persistent skill is active."),
 "Vitality II": L("Mais regeneração de vida.", "More life regeneration."),
 "Fire Penetration II": L("Ignora a resistência a fogo do inimigo — resolve os monstros com resistência a fogo alta.", "Ignores enemy fire resistance — solves monsters with high fire resistance."),
 "Deadly Resolve": L("Enquanto canaliza o Resonating Shield, acumula stages; quando você é atingido, dispara um golpe que escala com sua Armour.", "While channelling Resonating Shield you gain stages; when hit, you trigger a slash that scales with your Armour."),
 "Precision I": L("Mais Accuracy enquanto a skill persistente está ativa.", "More Accuracy while the persistent skill is active."),
 "Precision II": L("Mais Accuracy.", "More Accuracy."),
 "Ahn's Citadel": L("Support de Lineage: o Shield Wall nasce ao longo de uma fissura, cobrindo muito mais área.", "Lineage support: Shield Wall is created along a fissure, covering much more area."),
 "Kaom's Madness": L("Support de Lineage: cria várias fissuras extras (menos dano e área cada). Com Ahn's Citadel vira muros em todas as direções.", "Lineage support: creates many extra fissures (less damage and area each). With Ahn's Citadel it becomes walls in every direction."),
 "Supercritical": L("Mais dano crítico, menos chance de crítico. Com Nebuloch o crítico é garantido gastando Endurance Charge, então o 'menos chance' não pesa.", "More critical damage, less crit chance. With Nebuloch crits are guaranteed by spending an Endurance Charge, so the lower chance doesn't matter."),
 "Scouring Flame": L("Ignites mais fortes; o skill passa a custar Runic Ward (peças Runeforged).", "Stronger Ignites; the skill now costs Runic Ward (Runeforged pieces)."),
 "Ignite III": L("Mais chance de Ignite e Ignite causando o dano mais rápido.", "More Ignite chance and Ignites deal damage faster."),
 "Mobility": L("Anda mais rápido enquanto canaliza o Resonating Shield.", "Move faster while channelling Resonating Shield."),
 "Herbalism II": L("Mais recuperação de vida por flask enquanto a aura está ativa.", "More life recovery from flasks while the aura is active."),
 "Strong Hearted": L("Shock em você dura menos.", "Shock on you lasts shorter."),
 "Eternal Flame II": L("Ignites duram mais.", "Ignites last longer."),
 "Cannibalism II": L("Vida ao matar enquanto a skill persistente está ativa.", "Life on kill while the persistent skill is active."),
 "Efficiency II": L("Custa menos (de vida, com Blood Magic).", "Costs less (life, with Blood Magic)."),
 "Fire Mastery": L("+1 nível em skills de fogo.", "+1 level to fire skills."),
 "Styrn's Mountain": L("Support de Lineage: ao bloquear com o escudo levantado, seus outros ataques corpo a corpo causam mais dano.", "Lineage support: blocking with your shield raised makes your other melee attacks deal more damage."),
 "Physical Mastery": L("+1 nível em skills físicas.", "+1 level to physical skills."),
}
SUPWHY = {k: v for k, v in SUPWHY.items() if v}

MB = L("30 Spirit", "30 Spirit")
PHASES = [
 dict(id="a1", name=L("Ato 1", "Act 1"), lv=[1, 15], tag=L("Maças duplas + Boneshatter", "Dual maces + Boneshatter"),
  carry=L("Você: Mace Strike com duas maças + Boneshatter", "You: dual-wield Mace Strike + Boneshatter"), dmgSplit=[100, 0],
  goal=L("Escudo no Weapon Set 1 e duas maças de uma mão no Weapon Set 2. O Shield Bash do Raise Shield (com Brink I) prepara o pack para Heavy Stun; o Boneshatter dá o Heavy Stun e o Aftershock limpa. A Mace Strike com duas maças é seu melhor DPS por muito tempo. Olhe os vendors toda hora: maça forte vale mais que qualquer outra peça agora.",
         "Shield in Weapon Set 1 and two one-handed maces in Weapon Set 2. Raise Shield's Shield Bash (with Brink I) primes the pack for Heavy Stun; Boneshatter lands the Heavy Stun and its Aftershock clears. Dual-wield Mace Strike is your best DPS for a long time. Check vendors constantly: a strong mace is worth more than any other piece right now."),
  rotation=[L("Raise Shield → solte o Shield Bash no pack", "Raise Shield → release the Shield Bash on the pack"), L("Boneshatter nos inimigos prontos (Heavy Stun)", "Boneshatter on primed enemies (Heavy Stun)"), L("Mace Strike (duas maças) no boss durante o Heavy Stun", "Mace Strike (dual maces) on the boss during Heavy Stun"), L("Resonating Shield para quebrar Armour no fim do ato", "Resonating Shield to break Armour at the end of the act")],
  gems=[
   G("Mace Strike", ["Rage I", "Rapid Attacks I"], L("DPS principal", "Main DPS"), L("Com duas maças no Weapon Set 2 bate quase como uma de duas mãos, mas bem mais rápido.", "With two maces in Weapon Set 2 it hits almost like a two-hander, but much faster."), "free"),
   G("Boneshatter", ["Impact Shockwave", "Fire Attunement"], L("Clear + Heavy Stun", "Clear + Heavy Stun"), L("Dá Heavy Stun em inimigos prontos e cria uma onda de choque que limpa o pack.", "Heavy Stuns primed enemies and creates a shockwave that clears the pack."), "free"),
   G("Raise Shield", ["Steadfast I", "Brink I"], L("Prepara o Stun", "Stun primer"), L("Bloqueie e solte: o Shield Bash com Brink I deixa quase tudo pronto para Heavy Stun num golpe, mesmo com escudo fraco.", "Block and release: Shield Bash with Brink I primes almost anything for Heavy Stun in one hit, even with a weak shield."), "free"),
   G("Resonating Shield", ["Rage I", "Rapid Attacks I"], L("Armour Break", "Armour Break"), L("Chega no fim do ato. Quebra Armour e prepara Stun enquanto você bloqueia.", "Arrives at the end of the act. Breaks Armour and primes Stun while you block."), "free"),
   G("Infernal Cry", [], L("Empower", "Empower"), L("Empodera os próximos ataques corpo a corpo e faz inimigos explodirem ao morrer.", "Empowers your next melee attacks and makes enemies Combust on death."), "free"),
   G("Shield Charge", ["Rapid Attacks I"], L("Mobilidade no boss", "Mobility on bosses"), L("Fecha distância e acumula Stun.", "Closes distance and builds Stun."), "free"),
   G("Magma Barrier", ["Fire Attunement"], L("Block + Endurance", "Block + Endurance"), L("Aumenta o Block e enche o escudo de lava; ao bloquear com o escudo levantado solta Magma Spray e dá Endurance Charge. Ligue depois do King in the Mists.", "Raises Block and fills your shield with lava; blocking with the shield raised releases Magma Spray and grants an Endurance Charge. Turn it on after the King in the Mists."), "core", 1, MB),
  ],
  cheap=[L("Duas maças de uma mão com + nível de melee ou dano físico", "Two one-handed maces with + melee levels or physical damage"), L("Botas com Movement Speed", "Boots with Movement Speed")],
  full=[L("Uma maça com dano de raio (ou Storm Rune) para aplicar Shock no boss", "One mace with lightning damage (or a Storm Rune) to Shock bosses")],
  stats=[L("+ nível de melee e dano físico nas maças", "+ melee levels and physical damage on maces"), L("Armour no escudo", "Armour on the shield"), L("Vida", "Life"), L("Resistência a frio (boss do Ato 1)", "Cold resistance (Act 1 boss)")],
  tree=L("Brutal e Smash (dano contra Heavy Stun), Impair e Reaving (arma de uma mão).", "Brutal and Smash (damage vs Heavy Stun), Impair and Reaving (one-handed weapons)."),
  avoid=[L("Ignorar vendors de maça", "Ignoring mace vendors"), L("Usar Boneshatter em quem não está pronto para Stun", "Using Boneshatter on enemies not primed for Stun")],
  exit=[L("Brink I no Raise Shield", "Brink I on Raise Shield"), L("King in the Mists (+30 Spirit) → Magma Barrier", "King in the Mists (+30 Spirit) → Magma Barrier")]),

 dict(id="a2", name=L("Ato 2", "Act 2"), lv=[16, 31], tag=L("Coal Stoker + Shield Wall", "Coal Stoker + Shield Wall"),
  carry=L("Você: maças duplas + Resonating Shield", "You: dual maces + Resonating Shield"), dmgSplit=[100, 0],
  goal=L("O clear continua igual: prepare Stun com o Resonating Shield e bata com as maças. O Shield Wall aparece, mas o único detonador confiável agora é o Infernal Cry (cooldown alto) — use no boss. Primeira ascendência: Coal Stoker (resistência a fogo também dá frio e raio pela metade), que facilita muito capar resistências. Leap Slam vira sua skill de viagem.",
         "Clear stays the same: prime Stun with Resonating Shield and hit with the maces. Shield Wall shows up, but the only reliable detonator for now is Infernal Cry (long cooldown) — use it on bosses. First ascendancy: Coal Stoker (fire resistance also grants cold and lightning at half value), which makes capping resistances much easier. Leap Slam becomes your travel skill."),
  rotation=[L("Resonating Shield (Rage + Armour Break + Stun)", "Resonating Shield (Rage + Armour Break + Stun)"), L("Mace Strike / Boneshatter no Heavy Stun", "Mace Strike / Boneshatter on Heavy Stun"), L("Boss: Shield Wall e Infernal Cry para detonar", "Boss: Shield Wall and Infernal Cry to detonate")],
  gems=[
   G("Mace Strike", ["Rapid Attacks I", "Fire Attunement"], L("DPS principal", "Main DPS"), L("Fire Attunement no lugar do Rage: o Resonating Shield já gera Rage.", "Fire Attunement replaces Rage: Resonating Shield already generates Rage."), "free"),
   G("Resonating Shield", ["Rage I", "Stun I", "Armour Demolisher I"], L("Rage + Armour Break + Stun", "Rage + Armour Break + Stun"), L("Recebe o 3º socket: gera Rage, quebra Armour e prepara Stun. Dá para cancelar a animação e bater em dobro.", "Gets the 3rd socket: generates Rage, breaks Armour and primes Stun. You can animation-cancel it to hit twice as fast."), "free"),
   G("Boneshatter", ["Impact Shockwave", "Fire Attunement", "Magnified Area I"], L("Clear", "Clear"), L("Com o Lesser Jeweller's Orb, Magnified Area para mais área.", "With a Lesser Jeweller's Orb, Magnified Area for more area."), "free"),
   G("Leap Slam", ["Rapid Attacks I"], L("Viagem + Stun", "Travel + Stun"), L("Buffado no 0.5: rápido, pula obstáculos e prepara Stun.", "Buffed in 0.5: fast, jumps obstacles and primes Stun."), "free"),
   G("Infernal Cry", ["Raging Cry", "Tireless"], L("Empower + Rage", "Empower + Rage"), L("Um toque mantém a Rage no boss. Detona o Shield Wall.", "One tap keeps Rage up on bosses. Detonates Shield Wall."), "free"),
   G("Shield Wall", ["Fire Attunement"], L("Boss", "Boss"), L("Levanta um muro de terra; slams, warcries e Shield Charge quebram os segmentos, que explodem. Ainda sem detonador rápido.", "Raises a wall of earth; slams, warcries and Shield Charge shatter the segments, which explode. No fast detonator yet."), "free"),
   G("Magma Barrier", ["Fire Attunement"], L("Block + Endurance", "Block + Endurance"), L("30 Spirit.", "30 Spirit."), "core", 1, MB),
  ],
  cheap=[L("Maças novas a cada tier; escudo com Armour alta", "New maces at each tier; high-Armour shield"), L("Anéis Ruby (fogo) para o Coal Stoker", "Ruby rings (fire) for Coal Stoker")],
  full=[L("Abyss / Lightless Passage (Mastodon Badlands): Gnawed Jawbone/Rib para dano e Armour", "Abyss / Lightless Passage (Mastodon Badlands): Gnawed Jawbone/Rib for damage and Armour")],
  stats=[L("+ nível de melee", "+ melee levels"), L("Armour no escudo", "Armour on the shield"), L("Resistência a fogo (Coal Stoker)", "Fire resistance (Coal Stoker)"), L("Movement Speed", "Movement Speed")],
  tree=L("Crushing Verdict (+50% dano de ataque), Sturdy Metal, Relentless, Reverberating Impact e Blood Rush.", "Crushing Verdict (+50% attack damage), Sturdy Metal, Relentless, Reverberating Impact and Blood Rush."),
  avoid=[L("Spammar Shield Wall sem detonador", "Spamming Shield Wall without a detonator")],
  exit=[L("1ª ascendência: Coal Stoker", "1st ascendancy: Coal Stoker"), L("Resonating Shield com 3 links", "Resonating Shield with 3 links")]),

 dict(id="a3", name=L("Ato 3", "Act 3"), lv=[32, 43], tag=L("Fortifying Cry detona o Shield Wall", "Fortifying Cry detonates Shield Wall"),
  carry=L("Você: maças no clear · Shield Wall + Fortifying Cry no boss", "You: maces for clear · Shield Wall + Fortifying Cry on bosses"), dmgSplit=[100, 0],
  goal=L("Fortifying Cry é o detonador: dá Guard e dispara Shield Waves quando seus ataques de escudo acertam, quebrando os muros. No boss: Infernal Cry (empower) → Shield Wall → Fortifying Cry. Um escudo com ~350 de Armour já apaga bosses do ato. Scavenged Plating com os +30 do Azak Bog. Pode pular o Trial of Chaos por enquanto.",
         "Fortifying Cry is the detonator: it grants Guard and fires Shield Waves when your shield attacks hit, shattering the walls. On bosses: Infernal Cry (empower) → Shield Wall → Fortifying Cry. A ~350 Armour shield already deletes act bosses. Scavenged Plating with Azak Bog's +30. You can skip the Trial of Chaos for now."),
  rotation=[L("Resonating Shield até Fully Broken Armour", "Resonating Shield until Fully Broken Armour"), L("Infernal Cry (empower)", "Infernal Cry (empower)"), L("Shield Wall", "Shield Wall"), L("Fortifying Cry: as Shield Waves explodem os muros", "Fortifying Cry: Shield Waves shatter the walls"), L("Boneshatter/Mace Strike entre os cooldowns", "Boneshatter/Mace Strike between cooldowns")],
  gems=[
   G("Shield Wall", ["Fire Attunement", "Rapid Attacks I"], L("Boss", "Boss"), L("Empoderado pelo Infernal Cry e detonado pelo Fortifying Cry.", "Empowered by Infernal Cry and detonated by Fortifying Cry."), "free"),
   G("Fortifying Cry", ["Fire Attunement"], L("Detonador + Guard", "Detonator + Guard"), L("Guard + Shield Waves nos próximos ataques de escudo. O cooldown pode ser pulado gastando Endurance Charge.", "Guard + Shield Waves on your next shield attacks. Its cooldown can be bypassed by spending an Endurance Charge."), "free"),
   G("Resonating Shield", ["Rage I", "Stun I", "Armour Demolisher I"], L("Rage + Armour Break", "Rage + Armour Break"), L("Mantém Fully Broken Armour no boss.", "Keeps Fully Broken Armour on the boss."), "free"),
   G("Mace Strike", ["Rapid Attacks II", "Fire Attunement", "Close Combat I"], L("Clear", "Clear"), L("Continua limpando os packs.", "Still clears packs."), "free"),
   G("Boneshatter", ["Impact Shockwave", "Enduring Impact I", "Magnified Area I"], L("Clear + Endurance", "Clear + Endurance"), L("Enduring Impact I: Endurance Charge no Heavy Stun para pular o cooldown dos gritos.", "Enduring Impact I: Endurance Charge on Heavy Stun to bypass shout cooldowns."), "free"),
   G("Infernal Cry", ["Raging Cry", "Tireless"], L("Empower", "Empower"), L("Três ataques empoderados com a árvore.", "Three empowered attacks with the tree."), "free"),
   G("Leap Slam", ["Rapid Attacks I"], L("Viagem", "Travel"), L("Também quebra os muros (é slam).", "Also shatters walls (it's a slam)."), "free"),
   G("Magma Barrier", ["Fire Attunement", "Charge Profusion I"], L("Block + Endurance", "Block + Endurance"), L("Charge Profusion: charges extras.", "Charge Profusion: extra charges."), "core", 1, MB),
   G("Scavenged Plating", ["Prolonged Duration I"], L("Armour", "Armour"), L("Fully Broken Armour dá stacks de Armour e Thorns. +30 Spirit do Azak Bog.", "Fully Broken Armour grants Armour and Thorns stacks. +30 Spirit from Azak Bog."), "core", 2, MB),
  ],
  cheap=[L("Escudo com ~350 de Armour", "Shield with ~350 Armour"), L("Maças com + nível de melee", "Maces with + melee levels")],
  full=[L("Escudo de Armour alta (Abyss para gamblar Armour)", "High-Armour shield (Abyss to gamble Armour)"), L("+ nível de melee nas luvas/amuleto", "+ melee levels on gloves/amulet")],
  stats=[L("Armour do escudo", "Shield Armour"), L("+ nível de melee", "+ melee levels"), L("Vida, Armour, resistência a fogo", "Life, Armour, fire resistance")],
  tree=L("The Molten One's Gift (Fully Broken Armour aumenta o fogo recebido), Battle Trance e Ignore Pain. Caminho até Avatar of Fire.", "The Molten One's Gift (Fully Broken Armour increases fire taken), Battle Trance and Ignore Pain. Pathing towards Avatar of Fire."),
  avoid=[L("Negligenciar o escudo: ele é o dano do Shield Wall", "Neglecting the shield: it's Shield Wall's damage")],
  exit=[L("Fortifying Cry", "Fortifying Cry"), L("Azak Bog (+30 Spirit) → Scavenged Plating", "Azak Bog (+30 Spirit) → Scavenged Plating"), L("The Molten One's Gift", "The Molten One's Gift")]),

 dict(id="a4", name=L("Ato 4", "Act 4"), lv=[44, 53], tag=L("Avatar of Fire + weapon sets", "Avatar of Fire + weapon sets"),
  carry=L("Você: Shield Wall (Set 2) + warcries", "You: Shield Wall (Set 2) + warcries"), dmgSplit=[100, 0],
  goal=L("Hora do Avatar of Fire (75% do dano vira fogo, sem dano não-fogo) — só depois do The Molten One's Gift, que faz a Fully Broken Armour aumentar o fogo recebido. Aposente as maças duplas: o escudo fica travado nos DOIS weapon sets (passe o mouse nos números romanos acima do escudo). Weapon Set 1 = clear/utilidade (warcries, Resonating Shield, Sunder); Set 2 = boss (Shield Wall, Infernal Cry). Sunder aplica Sundered Armour: com The Molten One's Gift são ~40% mais dano de fogo recebido.",
         "Time for Avatar of Fire (75% of damage becomes fire, no non-fire damage) — only after The Molten One's Gift, which makes Fully Broken Armour increase fire taken. Retire the dual maces: the shield is locked to BOTH weapon sets (hover the roman numerals above the shield). Weapon Set 1 = clear/utility (warcries, Resonating Shield, Sunder); Set 2 = boss (Shield Wall, Infernal Cry). Sunder applies Sundered Armour: with The Molten One's Gift that's ~40% more fire damage taken."),
  rotation=[L("Set 1: Resonating Shield até Fully Broken Armour", "Set 1: Resonating Shield until Fully Broken Armour"), L("Set 1: Sunder (Sundered Armour)", "Set 1: Sunder (Sundered Armour)"), L("Set 2: Infernal Cry → Shield Wall", "Set 2: Infernal Cry → Shield Wall"), L("Fortifying Cry detona; Resonating Shield quebra os muros restantes", "Fortifying Cry detonates; Resonating Shield shatters the remaining walls")],
  gems=[
   G("Shield Wall", ["Fire Attunement", "Rapid Attacks I", "Elemental Armament I", "Fire Exposure"], L("Boss · Set 2", "Boss · Set 2"), L("Fire Exposure no Ignite corta a resistência a fogo.", "Fire Exposure on Ignite cuts fire resistance."), "free"),
   G("Fortifying Cry", ["Fire Attunement", "Enraged Warcry I", "Close Combat I"], L("Detonador", "Detonator"), L("Enraged Warcry I gasta Rage para pular o cooldown.", "Enraged Warcry I spends Rage to bypass the cooldown."), "free"),
   G("Infernal Cry", ["Tireless", "Lifetap"], L("Empower · Set 2", "Empower · Set 2"), L("Lifetap alivia a mana até o Blood Magic.", "Lifetap relieves mana until Blood Magic."), "free"),
   G("Resonating Shield", ["Rage I", "Stun II", "Armour Demolisher I"], L("Armour Break · Set 1", "Armour Break · Set 1"), L("Toques rápidos também quebram muros seguintes com as Shield Waves guardadas.", "Quick taps also shatter later walls using stored Shield Waves."), "free"),
   G("Sunder", ["Rapid Attacks I", "Prolonged Duration I"], L("Sundered Armour · Set 1", "Sundered Armour · Set 1"), L("Só pelo debuff (não pelo dano): alvo com Fully Broken Armour recebe mais dano; com The Molten One's Gift vale para fogo.", "Only for the debuff (not damage): a Fully Broken Armour target takes more damage; with The Molten One's Gift it applies to fire."), "free"),
   G("Leap Slam", ["Rapid Attacks I"], L("Viagem", "Travel"), L("Viagem e quebra de muros.", "Travel and wall shattering."), "free"),
   G("Magma Barrier", ["Fire Attunement", "Charge Profusion I", "Elemental Armament II"], L("Block + Endurance", "Block + Endurance"), L("30 Spirit.", "30 Spirit."), "core", 1, MB),
   G("Scavenged Plating", ["Prolonged Duration I", "Vitality I"], L("Armour + regen", "Armour + regen"), L("30 Spirit.", "30 Spirit."), "core", 2, MB),
  ],
  cheap=[L("Maça com % dano elemental de ataques (mais forte que +2 melee agora)", "Mace with % elemental attack damage (stronger than +2 melee now)"), L("Anéis Ruby", "Ruby rings")],
  full=[L("Escudo de Armour alta travado nos dois sets", "High-Armour shield locked to both sets"), L("Runeshaping: runa de mana para aliviar o custo", "Runeshaping: a mana rune to ease costs")],
  stats=[L("% dano elemental de ataques", "% elemental attack damage"), L("Armour do escudo", "Shield Armour"), L("Resistência a fogo", "Fire resistance"), L("Mana", "Mana")],
  tree=L("Avatar of Fire, Momentum. Set 1: Vocal Empowerment, Admonisher, Urgent Call. Set 2: Fulmination, Lasting Trauma, Overheating Blow.", "Avatar of Fire, Momentum. Set 1: Vocal Empowerment, Admonisher, Urgent Call. Set 2: Fulmination, Lasting Trauma, Overheating Blow."),
  avoid=[L("Pegar Avatar of Fire antes do The Molten One's Gift", "Taking Avatar of Fire before The Molten One's Gift"), L("Deixar o escudo só no Set 1", "Leaving the shield only on Set 1")],
  exit=[L("Avatar of Fire", "Avatar of Fire"), L("Escudo travado nos dois weapon sets", "Shield locked to both weapon sets")]),

 dict(id="int", name=L("Interlúdios", "Interludes"), lv=[54, 64], tag=L("Smith's Masterwork + Blood Magic", "Smith's Masterwork + Blood Magic"),
  carry=L("Você: Shield Wall + Ignite", "You: Shield Wall + Ignite"), dmgSplit=[100, 0],
  goal=L("Tudo vira fogo e Ignite no boss. A mana começa a apertar: faça o Trial de nível 60 cedo para os 5º e 6º pontos e pegue Blood Magic (sem mana; skills custam vida) — a ascendência dá vida e regen de sobra. Ascendência da Smith: Smith's Masterwork (só body armour Normal; +200 Armour por notable conectado), Kitavan Engraving (+15% vida), Leather Bindings (3% regen), Heatproofing (imune a dano de ailments). Com gems nível 5, Fire Penetration II no Shield Wall.",
         "Everything becomes fire and Ignite on bosses. Mana gets tight: do the level 60 Trial early for your 5th and 6th points and take Blood Magic (no mana; skills cost life) — the ascendancy gives plenty of life and regen. Smith ascendancy: Smith's Masterwork (Normal body armour only; +200 Armour per connected notable), Kitavan Engraving (+15% life), Leather Bindings (3% regen), Heatproofing (unaffected by damaging ailments). With level 5 gems, Fire Penetration II on Shield Wall."),
  rotation=[L("Resonating Shield (Fully Broken Armour)", "Resonating Shield (Fully Broken Armour)"), L("Sunder", "Sunder"), L("Infernal Cry → Shield Wall", "Infernal Cry → Shield Wall"), L("Fortifying Cry detona; Ignites fazem o resto", "Fortifying Cry detonates; Ignites do the rest")],
  gems=[
   G("Shield Wall", ["Fire Attunement", "Rapid Attacks I", "Elemental Armament II", "Fire Penetration II"], L("Boss · Set 2", "Boss · Set 2"), L("Fire Penetration II resolve os monstros 'gold' de resistência a fogo.", "Fire Penetration II solves 'gold' fire-resistant monsters."), "free"),
   G("Fortifying Cry", ["Fire Attunement", "Close Combat I", "Enraged Warcry I"], L("Detonador", "Detonator"), L("Mesmo papel.", "Same role."), "free"),
   G("Infernal Cry", ["Lifetap", "Tireless", "Enraged Warcry I"], L("Empower", "Empower"), L("Sempre antes do Shield Wall.", "Always before Shield Wall."), "free"),
   G("Resonating Shield", ["Armour Demolisher II", "Deadly Resolve", "Rage II"], L("Armour Break + dano", "Armour Break + damage"), L("Deadly Resolve dá golpes baseados na Armour quando você é atingido: começa a limpar sozinho.", "Deadly Resolve fires Armour-based slashes when you're hit: it starts clearing on its own."), "free"),
   G("Sunder", ["Rapid Attacks II", "Prolonged Duration II"], L("Sundered Armour", "Sundered Armour"), L("Só debuff no boss.", "Boss debuff only."), "free"),
   G("Leap Slam", ["Rapid Attacks II"], L("Viagem", "Travel"), L("Mais rápido.", "Faster."), "free"),
   G("Magma Barrier", ["Fire Attunement", "Charge Profusion I"], L("Block + Endurance", "Block + Endurance"), L("30 Spirit.", "30 Spirit."), "core", 1, MB),
   G("Scavenged Plating", ["Prolonged Duration I", "Precision I"], L("Armour", "Armour"), L("30 Spirit.", "30 Spirit."), "core", 2, MB),
  ],
  cheap=[L("Body armour NORMAL (branca) com Armour alta para o Smith's Masterwork", "NORMAL (white) body armour with high Armour for Smith's Masterwork"), L("Maça com + nível de melee e % dano elemental", "Mace with + melee levels and % elemental damage")],
  full=[L("Body Normal de base alta + Artificer's Orb + runas", "High-tier Normal body + Artificer's Orb + runes"), L("Anéis Ruby com vida", "Ruby rings with life")],
  stats=[L("Armour do escudo", "Shield Armour"), L("Resistência a fogo", "Fire resistance"), L("Vida", "Life"), L("% dano elemental de ataques", "% elemental attack damage")],
  tree=L("Blood Magic, Greatest Defence (dano por Armour do escudo), Roaring Cries. Set 1: Primal Growth. Set 2: In Your Face.", "Blood Magic, Greatest Defence (damage per shield Armour), Roaring Cries. Set 1: Primal Growth. Set 2: In Your Face."),
  avoid=[L("Usar body Rare com Smith's Masterwork (só aceita Normal)", "Using a Rare body with Smith's Masterwork (Normal only)"), L("Blood Magic antes dos 5º/6º pontos de ascendência", "Blood Magic before the 5th/6th ascendancy points")],
  exit=[L("Smith's Masterwork + Leather Bindings + Heatproofing", "Smith's Masterwork + Leather Bindings + Heatproofing"), L("Blood Magic", "Blood Magic"), L("Fire Penetration II", "Fire Penetration II")]),

 dict(id="maps", name=L("Mapas T1–T5", "Maps T1–T5"), lv=[65, 72], tag=L("Herald of Ash + Berserk", "Herald of Ash + Berserk"),
  carry=L("Você: Shield Wall detonado pelo Fortifying Cry", "You: Shield Wall detonated by Fortifying Cry"), dmgSplit=[100, 0],
  goal=L("Clear: spam de Shield Wall detonado pelo Fortifying Cry; canalize o Resonating Shield no caminho para Rage e stacks de Plating. Boss: quebre toda a Armour com o Resonating Shield, Rage cheia, Infernal Cry → Shield Wall → Fortifying Cry. Trade: compre peças baratas com resistência a fogo para capar tudo e busque Chaos Resistance em cinto, capacete e botas. Dedication to Kitava (Armour também contra Chaos) entra na ascendência.",
         "Clear: spam Shield Wall detonated by Fortifying Cry; channel Resonating Shield while moving for Rage and Plating stacks. Boss: fully break Armour with Resonating Shield, full Rage, Infernal Cry → Shield Wall → Fortifying Cry. Trade: buy cheap fire-resistance pieces to cap everything and look for Chaos Resistance on belt, helmet and boots. Dedication to Kitava (Armour also vs Chaos) joins the ascendancy."),
  rotation=[L("Clear: Shield Wall → Fortifying Cry", "Clear: Shield Wall → Fortifying Cry"), L("Boss: Resonating Shield até Fully Broken Armour", "Boss: Resonating Shield until Fully Broken Armour"), L("Rage cheia → Infernal Cry → Shield Wall → Fortifying Cry", "Full Rage → Infernal Cry → Shield Wall → Fortifying Cry")],
  gems=[
   G("Shield Wall", ["Fire Attunement", "Fire Penetration II", "Rapid Attacks II", "Elemental Armament II"], L("Clear + boss · Set 2", "Clear + boss · Set 2"), L("Seu tudo: dano de fogo e animação mais rápida.", "Your everything: fire damage and faster animation."), "free"),
   G("Fortifying Cry", ["Raging Cry", "Fire Attunement", "Enraged Warcry II"], L("Detonador · Set 1", "Detonator · Set 1"), L("Enraged Warcry II: detona mais vezes gastando Rage.", "Enraged Warcry II: detonate more often by spending Rage."), "free"),
   G("Resonating Shield", ["Rage III", "Rapid Attacks I", "Armour Demolisher II"], L("Rage + Armour Break · Set 1", "Rage + Armour Break · Set 1"), L("Rage III dá attack speed enquanto a Rage não está cheia.", "Rage III grants attack speed while Rage isn't full."), "free"),
   G("Infernal Cry", ["Tireless"], L("Empower · Set 1", "Empower · Set 1"), L("Não precisa mais de Raging Cry.", "No longer needs Raging Cry."), "free"),
   G("Herald of Ash", ["Magnified Area I"], L("Clear em cadeia · Set 2", "Chain clear · Set 2"), L("Inimigos mortos com overkill explodem e dão Ignite nos vizinhos. Precisa estar ativo no set do Shield Wall.", "Enemies killed with overkill explode and Ignite nearby enemies. Must be active on the Shield Wall set."), "core", 3, MB),
   G("Scavenged Plating", ["Prolonged Duration I", "Vitality I"], L("Armour · Set 1", "Armour · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 2, MB),
   G("Berserk", [], L("Rage mais forte · Set 2", "Stronger Rage · Set 2"), L("Só depois de regen de sobra (Leather Bindings + Vitality).", "Only with plenty of regen (Leather Bindings + Vitality)."), "opt", 1, MB),
   G("Leap Slam", [], L("Viagem · Set 1", "Travel · Set 1"), L("Viagem.", "Travel."), "free"),
  ],
  cheap=[L("Escudo com 800–900 de Armour", "Shield with 800–900 Armour"), L("Maça +3 melee com % dano elemental", "+3 melee mace with % elemental damage"), L("Charms: Thawing, Stone, Silver", "Charms: Thawing, Stone, Silver")],
  full=[L("Maça +4 melee", "+4 melee mace"), L("Luvas com attack speed (+2 melee é caro)", "Gloves with attack speed (+2 melee is pricey)")],
  stats=[L("Armour do escudo", "Shield Armour"), L("+ nível de melee e % dano elemental na maça", "+ melee levels and % elemental damage on the mace"), L("Resistências (fogo + Chaos)", "Resistances (fire + Chaos)"), L("Attack speed nas luvas", "Attack speed on gloves")],
  tree=L("Blazing Arms, Ichlotl's Inferno (Rage vira dano de fogo), Unyielding. Set 2: Sand in the Eyes.", "Blazing Arms, Ichlotl's Inferno (Rage becomes fire damage), Unyielding. Set 2: Sand in the Eyes."),
  avoid=[L("Charms contra ailments de dano (Heatproofing já te imuniza)", "Charms against damaging ailments (Heatproofing already makes you immune)")],
  exit=[L("Resistências no cap (inclusive Chaos, se der)", "Resistances capped (Chaos too, if possible)"), L("Dedication to Kitava", "Dedication to Kitava")]),

 dict(id="t10", name=L("Mapas T5–T10", "Maps T5–T10"), lv=[73, 84], tag=L("Nebuloch + Kaom's Madness", "Nebuloch + Kaom's Madness"),
  carry=L("Você: Shield Wall com Ahn's Citadel + Kaom's Madness", "You: Shield Wall with Ahn's Citadel + Kaom's Madness"), dmgSplit=[100, 0],
  goal=L("A virada do clear: Ahn's Citadel faz o Shield Wall nascer em fissuras e Kaom's Madness cria fissuras extras — muros explodindo em todas as direções. Nebuloch no Weapon Set 2: ataques gastam uma Endurance Charge para dar crítico garantido (Supercritical transforma isso em dano crítico enorme). As charges vêm do Magma Barrier, Armour Break III e Endurance (+2 máximo); a degeneração de Chaos por charge é paga pela Dedication to Kitava. Na ascendência: Forged in Flame (máxima de fogo também dá frio/raio) e Molten Symbol (25% do físico recebido como fogo). Purity of Fire sobe ainda mais a resistência a fogo.",
         "The clear turning point: Ahn's Citadel makes Shield Wall spawn along fissures and Kaom's Madness creates extra fissures — walls exploding in every direction. Nebuloch in Weapon Set 2: attacks spend an Endurance Charge for a guaranteed crit (Supercritical turns that into huge crit damage). Charges come from Magma Barrier, Armour Break III and Endurance (+2 maximum); the Chaos degeneration per charge is paid by Dedication to Kitava. Ascendancy: Forged in Flame (max fire resistance also grants cold/lightning) and Molten Symbol (25% of physical taken as fire). Purity of Fire pushes fire resistance even higher."),
  rotation=[L("Clear: Shield Wall (fissuras) → Fortifying Cry / Shield Charge", "Clear: Shield Wall (fissures) → Fortifying Cry / Shield Charge"), L("Rares teimosos: troque para o Set 2 e acerte com crítico do Nebuloch", "Stubborn rares: swap to Set 2 and crit with Nebuloch"), L("Boss: Resonating Shield → Infernal Cry → Shield Wall → Fortifying Cry → Raise Shield (Ignite)", "Boss: Resonating Shield → Infernal Cry → Shield Wall → Fortifying Cry → Raise Shield (Ignite)")],
  gems=[
   G("Shield Wall", ["Ahn's Citadel", "Kaom's Madness", "Supercritical", "Fire Attunement", "Fire Penetration II"], L("Clear + boss · Set 2", "Clear + boss · Set 2"), L("Lineage: muros em fissuras múltiplas. Supercritical com o crítico garantido do Nebuloch.", "Lineage: walls along multiple fissures. Supercritical with Nebuloch's guaranteed crit."), "free"),
   G("Raise Shield", ["Elemental Armament II", "Scouring Flame", "Ignite III"], L("Ignite no boss", "Ignite on bosses"), L("Scouring Flame deixa o Ignite muito mais forte e custa Runic Ward (body/luvas Runeforged).", "Scouring Flame makes Ignite much stronger and costs Runic Ward (Runeforged body/gloves)."), "free"),
   G("Resonating Shield", ["Rage III", "Armour Demolisher II", "Armour Break III", "Mobility"], L("Rage + Endurance · Set 1", "Rage + Endurance · Set 1"), L("Armour Break III gera Endurance Charges para o Nebuloch.", "Armour Break III generates Endurance Charges for Nebuloch."), "free"),
   G("Fortifying Cry", ["Fire Attunement", "Raging Cry", "Enraged Warcry II"], L("Detonador · Set 1", "Detonator · Set 1"), L("Mesmo papel.", "Same role."), "free"),
   G("Infernal Cry", ["Tireless", "Raging Cry", "Enraged Warcry II"], L("Empower · Set 1", "Empower · Set 1"), L("Mesmo papel.", "Same role."), "free"),
   G("Shield Charge", ["Rage III", "Rapid Attacks III"], L("Viagem + detonador · Set 1", "Travel + detonator · Set 1"), L("Quebra os muros ao atravessar.", "Shatters walls as you pass through."), "free"),
   G("Magma Barrier", ["Charge Profusion II", "Eternal Flame II", "Fire Attunement"], L("Block + Endurance (sets 1 e 2)", "Block + Endurance (sets 1 and 2)"), L("A fonte principal de Endurance Charge.", "The main Endurance Charge source."), "core", 1, MB),
   G("Scavenged Plating", ["Vitality II", "Cannibalism II", "Prolonged Duration I"], L("Armour + vida · Set 1", "Armour + life · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 2, MB),
   G("Herald of Ash", ["Magnified Area II", "Prolonged Duration II"], L("Clear em cadeia · Set 2", "Chain clear · Set 2"), L("30 Spirit.", "30 Spirit."), "core", 3, MB),
   G("Purity of Fire", ["Herbalism II", "Strong Hearted"], L("Resistência a fogo · Set 1", "Fire resistance · Set 1"), L("Aura que aumenta sua resistência a fogo; com Coal Stoker/Forged in Flame vira resistência para tudo.", "Aura that raises your fire resistance; with Coal Stoker/Forged in Flame it becomes resistance to everything."), "core", 4, L("Reserva Spirit (confira no jogo)", "Reserves Spirit (check in game)")),
   G("Berserk", [], L("Rage mais forte · Set 2", "Stronger Rage · Set 2"), L("Com regen de sobra.", "With plenty of regen."), "opt", 1, MB),
  ],
  cheap=["Nebuloch", L("Runeforged Ornate Plate (Normal)", "Runeforged Ornate Plate (Normal)"), L("Tower Shield de Armour altíssima", "Very high-Armour Tower Shield")],
  full=[L("Guiding Palm of the Heart no Weapon Set 1", "Guiding Palm of the Heart in Weapon Set 1"), L("Amuleto com anoint Thaumaturgic Generator (Endurance)", "Amulet anointed with Thaumaturgic Generator (Endurance)")],
  stats=[L("Armour do escudo", "Shield Armour"), L("Endurance Charges", "Endurance Charges"), L("Resistência máxima a fogo", "Maximum fire resistance"), L("Vida", "Life")],
  tree=L("Surrounded (Thrill of Battle, Frantic Fighter, Tactical Retreat), Tempered Defences, Endurance. Set 1: Punctured Lung, Irreparable, Inherited Strength. Set 2: Barbaric Strength, Overwhelming Strike.", "Surrounded (Thrill of Battle, Frantic Fighter, Tactical Retreat), Tempered Defences, Endurance. Set 1: Punctured Lung, Irreparable, Inherited Strength. Set 2: Barbaric Strength, Overwhelming Strike."),
  avoid=[L("Nebuloch sem fonte de Endurance Charge (sem crítico)", "Nebuloch without an Endurance Charge source (no crits)"), L("Esquecer a degeneração de Chaos por charge", "Forgetting the Chaos degeneration per charge")],
  exit=[L("Ahn's Citadel + Kaom's Madness", "Ahn's Citadel + Kaom's Madness"), L("Nebuloch com Endurance Charges estáveis", "Nebuloch with steady Endurance Charges"), L("Forged in Flame + Molten Symbol", "Forged in Flame + Molten Symbol")]),

 dict(id="t15", name=L("Mapas T10–T15", "Maps T10–T15"), lv=[85, 91], tag=L("Constricting Command + For Utopia", "Constricting Command + For Utopia"),
  carry=L("Você: Shield Wall com Ahn's Citadel + Kaom's Madness", "You: Shield Wall with Ahn's Citadel + Kaom's Madness"), dmgSplit=[100, 0],
  goal=L("Mesmas gems do T5–T10 com dois uniques baratos: Constricting Command (vida, regen e menos inimigos para ficar Surrounded — ativa os notables de Surrounded quase sempre) e For Utopia (charm: defende com 200% da Armour durante o efeito). Suba o escudo e a maça; a build já faz 200% Delirium e Grand Expeditions.",
         "Same gems as T5–T10 with two cheap uniques: Constricting Command (life, regen and fewer enemies needed to be Surrounded — turns on the Surrounded notables almost always) and For Utopia (charm: defend with 200% of Armour during its effect). Upgrade the shield and mace; the build already handles 200% Delirium and Grand Expeditions."),
  rotation=[L("Igual ao T5–T10", "Same as T5–T10")],
  gems=[],
  cheap=["Constricting Command", "For Utopia", "Nebuloch"], full=[L("Escudo de 1000+ Armour", "1000+ Armour shield"), L("Breach Ring", "Breach Ring")],
  stats=[L("Armour do escudo", "Shield Armour"), L("Vida", "Life"), L("Resistências", "Resistances")],
  tree=L("Mesma do T5–T10.", "Same as T5–T10."), avoid=[L("Trocar vida por dano", "Trading life for damage")], exit=[L("T15 confortável", "Comfortable T15")]),

 dict(id="max", name=L("Pinnacle / Luxo", "Pinnacle / Luxury"), lv=[92, 100], tag=L("Sacred Flame + Styrn's Mountain", "Sacred Flame + Styrn's Mountain"),
  carry=L("Você: Shield Wall · Ignite · Sunder", "You: Shield Wall · Ignite · Sunder"), dmgSplit=[100, 0],
  goal=L("Setup otimizado do Lexd: Sacred Flame no Weapon Set 1 (40–60% do dano como fogo extra e inimigos resistem pela resistência elemental mais baixa), Styrn's Mountain no Resonating Shield (bloquear aumenta o dano corpo a corpo), Sunder volta no Set 2 e Arsonist acelera os Ignites. The Fall of the Axe e Rite of Passage completam. Thrillsteel (Onslaught no capacete) é a alternativa ao Constricting Command.",
         "Lexd's optimized setup: Sacred Flame in Weapon Set 1 (40–60% of damage as extra fire and enemies resist using their lowest elemental resistance), Styrn's Mountain on Resonating Shield (blocking raises melee damage), Sunder returns on Set 2 and Arsonist speeds up Ignites. The Fall of the Axe and Rite of Passage complete it. Thrillsteel (Onslaught helmet) is the alternative to Constricting Command."),
  rotation=[L("Resonating Shield (bloqueie: Styrn's Mountain)", "Resonating Shield (block: Styrn's Mountain)"), L("Sunder (Set 2)", "Sunder (Set 2)"), L("Infernal Cry → Shield Wall → Fortifying Cry", "Infernal Cry → Shield Wall → Fortifying Cry"), L("Ignites queimam enquanto você desvia", "Ignites burn while you dodge")],
  gems=[
   G("Shield Wall", ["Ahn's Citadel", "Kaom's Madness", "Fire Attunement", "Supercritical", "Rapid Attacks II"], L("Clear + boss · Set 2", "Clear + boss · Set 2"), L("Rapid Attacks II no lugar do Fire Penetration: a Sacred Flame já usa a menor resistência.", "Rapid Attacks II replaces Fire Penetration: Sacred Flame already uses the lowest resistance."), "free"),
   G("Fortifying Cry", ["Magnified Area II", "Elemental Armament II", "Fire Attunement", "Raging Cry", "Enraged Warcry II"], L("Detonador · Set 1", "Detonator · Set 1"), L("Mais área e dano.", "More area and damage."), "free"),
   G("Infernal Cry", ["Tireless", "Raging Cry", "Efficiency II", "Fire Mastery", "Enraged Warcry II"], L("Empower · Set 1", "Empower · Set 1"), L("Fire Mastery: +1 nível.", "Fire Mastery: +1 level."), "free"),
   G("Resonating Shield", ["Styrn's Mountain", "Armour Break III", "Mobility", "Rage III", "Armour Demolisher II"], L("Block → dano · Set 1", "Block → damage · Set 1"), L("Styrn's Mountain: bloquear com o escudo levantado aumenta o dano dos outros ataques.", "Styrn's Mountain: blocking with your shield raised increases your other attacks' damage."), "free"),
   G("Sunder", ["Rapid Attacks III", "Rage III", "Prolonged Duration II"], L("Sundered Armour · Set 2", "Sundered Armour · Set 2"), L("Debuff de boss.", "Boss debuff."), "free"),
   G("Shield Charge", ["Rage III", "Rapid Attacks II", "Stun III", "Fire Attunement", "Enduring Impact II"], L("Viagem + Endurance · Set 1", "Travel + Endurance · Set 1"), L("Enduring Impact II: charges no Heavy Stun.", "Enduring Impact II: charges on Heavy Stun."), "free"),
   G("Magma Barrier", ["Charge Profusion II", "Fire Attunement", "Elemental Armament II", "Eternal Flame II", "Close Combat II"], L("Block + Endurance", "Block + Endurance"), L("30 Spirit.", "30 Spirit."), "core", 1, MB),
   G("Scavenged Plating", ["Prolonged Duration II", "Physical Mastery", "Cannibalism II", "Vitality II"], L("Armour + vida · Set 1", "Armour + life · Set 1"), L("30 Spirit.", "30 Spirit."), "core", 2, MB),
   G("Berserk", ["Precision II", "Strong Hearted"], L("Rage mais forte", "Stronger Rage"), L("30 Spirit.", "30 Spirit."), "core", 3, MB),
   G("Purity of Fire", [], L("Resistência a fogo", "Fire resistance"), L("Reserva Spirit (confira no jogo).", "Reserves Spirit (check in game)."), "core", 4, L("Reserva Spirit (confira no jogo)", "Reserves Spirit (check in game)")),
  ],
  cheap=["Sacred Flame", "Nebuloch", "Constricting Command"], full=["The Fall of the Axe · Rite of Passage", L("Breach Rings · Runeforged Ornate Mitts", "Breach Rings · Runeforged Ornate Mitts")],
  stats=[L("Armour do escudo", "Shield Armour"), L("Attack/skill speed", "Attack/skill speed"), L("Vida", "Life")],
  tree=L("Mass Hysteria, Engineered Blaze, Favourable Odds, Blazing Arms, Ichlotl's Inferno. Set 2: Sundering, Arsonist.", "Mass Hysteria, Engineered Blaze, Favourable Odds, Blazing Arms, Ichlotl's Inferno. Set 2: Sundering, Arsonist."),
  avoid=[L("Herald of Ash com sceptre no Set 1 fora do set do Shield Wall", "Herald of Ash with a sceptre on Set 1 outside the Shield Wall set")],
  exit=[L("Pinnacle bosses", "Pinnacle bosses")]),
]
PH = {p["id"]: p for p in PHASES}
PH["t15"]["gems"] = PH["t10"]["gems"]

BOX = {
 "a1": ("~500", [L("Armour do escudo", "Shield Armour")], L("Escudo ainda é bônus: as maças dão o dano. Qualquer Armour ajuda o Shield Bash a preparar Stun.", "The shield is still a bonus: maces deal the damage. Any Armour helps Shield Bash prime Stun.")),
 "a3": ("350+", [L("Armour do escudo", "Shield Armour")], L("Com ~350 de Armour o Shield Wall + Fortifying Cry apaga bosses do Ato 3.", "With ~350 Armour, Shield Wall + Fortifying Cry deletes Act 3 bosses.")),
 "a4": ("≈40%", [L("fogo recebido no boss", "fire taken on bosses")], L("Fully Broken Armour (~20%) + Sundered Armour (~20%) com The Molten One's Gift = ~40% mais dano de fogo recebido.", "Fully Broken Armour (~20%) + Sundered Armour (~20%) with The Molten One's Gift = ~40% more fire damage taken.")),
 "int": ("+15%", [L("vida (Kitavan Engraving)", "life (Kitavan Engraving)"), L("3% regen", "3% regen")], L("A body Normal recebe os bônus da ascendência: vida, regen e imunidade a dano de ailments.", "The Normal body receives the ascendancy bonuses: life, regen and immunity to ailment damage.")),
 "maps": ("800+", [L("Armour do escudo", "Shield Armour")], L("800–900 de Armour no escudo bastam para os primeiros mapas.", "800–900 shield Armour is enough for early maps.")),
 "t10": ("3–5", [L("Endurance Charges", "Endurance Charges")], L("Cada ataque do Nebuloch gasta uma charge para dar crítico; cada charge causa 100 de Chaos por segundo em você.", "Each Nebuloch attack spends a charge to crit; each charge deals 100 Chaos per second to you.")),
 "t15": ("1000+", [L("Armour do escudo", "Shield Armour")], L("Suba o escudo: ele é o dano do Shield Wall, do Fortifying Cry e do Greatest Defence.", "Upgrade the shield: it's the damage of Shield Wall, Fortifying Cry and Greatest Defence.")),
 "max": ("1000+", [L("Armour do escudo", "Shield Armour")], L("Mesmo foco: escudo e velocidade.", "Same focus: shield and speed.")),
}
SPIRIT_NOTE = {
 "a1": L("Magma Barrier reserva 30 Spirit: ligue depois do King in the Mists.", "Magma Barrier reserves 30 Spirit: turn it on after the King in the Mists."),
 "a3": L("Magma Barrier (30) + Scavenged Plating (30) com os +30 do Azak Bog.", "Magma Barrier (30) + Scavenged Plating (30) with Azak Bog's +30."),
 "maps": L("Ordem: Magma Barrier (30) → Scavenged Plating (30) → Herald of Ash (30) → Berserk (30, se couber).", "Order: Magma Barrier (30) → Scavenged Plating (30) → Herald of Ash (30) → Berserk (30, if it fits)."),
 "t10": L("Ordem: Magma Barrier → Scavenged Plating → Herald of Ash → Purity of Fire → Berserk. Itens com Spirit pagam a Purity e o Berserk.", "Order: Magma Barrier → Scavenged Plating → Herald of Ash → Purity of Fire → Berserk. Spirit items pay for Purity and Berserk."),
 "max": L("Magma Barrier, Scavenged Plating, Berserk e Purity of Fire. Sacred Flame no Set 1 abre espaço no amuleto.", "Magma Barrier, Scavenged Plating, Berserk and Purity of Fire. Sacred Flame on Set 1 frees up the amulet."),
}
for pid, (n, types, note) in BOX.items():
    PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}
for pid, note in SPIRIT_NOTE.items():
    PH[pid]["spiritNote"] = note

MILESTONES = {
 1: L("Escudo no Set 1, duas maças no Set 2. Mace Strike + Boneshatter.", "Shield on Set 1, two maces on Set 2. Mace Strike + Boneshatter."),
 4: L("Raise Shield com Brink I: Shield Bash prepara Stun.", "Raise Shield with Brink I: Shield Bash primes Stun."),
 10: L("Freythorn: King in the Mists (+30 Spirit) → Magma Barrier.", "Freythorn: King in the Mists (+30 Spirit) → Magma Barrier."),
 13: L("Resonating Shield (Armour Break + Stun).", "Resonating Shield (Armour Break + Stun)."),
 20: L("Leap Slam (viagem) e Shield Wall.", "Leap Slam (travel) and Shield Wall."),
 28: L("1ª ascendência: Coal Stoker. Anéis Ruby.", "1st ascendancy: Coal Stoker. Ruby rings."),
 34: L("Fortifying Cry: detonador do Shield Wall.", "Fortifying Cry: Shield Wall's detonator."),
 38: L("Azak Bog: Ignagduk (+30 Spirit) → Scavenged Plating.", "Azak Bog: Ignagduk (+30 Spirit) → Scavenged Plating."),
 42: L("The Molten One's Gift na árvore.", "The Molten One's Gift on the tree."),
 45: L("Avatar of Fire. Escudo travado nos dois weapon sets. Sunder.", "Avatar of Fire. Shield locked to both weapon sets. Sunder."),
 55: L("Trial nível 60: Smith's Masterwork + Kitavan Engraving + Leather Bindings + Heatproofing. Body armour NORMAL.", "Level 60 Trial: Smith's Masterwork + Kitavan Engraving + Leather Bindings + Heatproofing. NORMAL body armour."),
 58: L("Blood Magic (sem mana). Fire Penetration II no Shield Wall.", "Blood Magic (no mana). Fire Penetration II on Shield Wall."),
 62: L("Kriar Village: Lythara (+40 Spirit).", "Kriar Village: Lythara (+40 Spirit)."),
 66: L("Herald of Ash no set do Shield Wall. Resistências (fogo + Chaos) no cap.", "Herald of Ash on the Shield Wall set. Resistances (fire + Chaos) capped."),
 68: L("Dedication to Kitava (Armour também contra Chaos).", "Dedication to Kitava (Armour also vs Chaos)."),
 74: L("Ahn's Citadel + Kaom's Madness no Shield Wall. Nebuloch no Set 2.", "Ahn's Citadel + Kaom's Madness on Shield Wall. Nebuloch on Set 2."),
 76: L("Forged in Flame + Molten Symbol. Purity of Fire.", "Forged in Flame + Molten Symbol. Purity of Fire."),
 85: L("Constricting Command + For Utopia.", "Constricting Command + For Utopia."),
 92: L("Sacred Flame (Set 1) + Styrn's Mountain.", "Sacred Flame (Set 1) + Styrn's Mountain."),
}

ASCENDANCY = [
 dict(order=1, key="coal", node="Coal Stoker", when=L("1º Trial (~nível 28)", "1st Trial (~level 28)"), text=L("Mods de resistência a fogo também dão resistência a frio e raio com 50% do valor.", "Fire Resistance modifiers also grant Cold and Lightning Resistance at 50% of their value."), why=L("Capar resistências vira fácil: Ruby Rings e fogo em tudo.", "Capping resistances becomes easy: Ruby Rings and fire on everything.")),
 dict(order=2, key="master", node="Smith's Masterwork", when=L("Trial nível 60", "Level 60 Trial"), text=L("Só pode usar body armour Normal; +200 de Armour por notable conectado.", "Can only use a Normal Body Armour; +200 Armour for each connected notable."), why=L("Libera os bônus que a ascendência 'forja' na body armour.", "Unlocks the bonuses the ascendancy 'forges' into your body armour.")),
 dict(order=3, key="engraving", node="Kitavan Engraving", when=L("Trial nível 60", "Level 60 Trial"), text=L("A body armour dá 15% increased vida máxima.", "Body Armour grants 15% increased maximum Life."), why=L("Vida para o Blood Magic.", "Life for Blood Magic.")),
 dict(order=4, key="bindings", node="Leather Bindings", when=L("Trial nível 60", "Level 60 Trial"), text=L("A body armour dá regeneração de 3% da vida por segundo.", "Body Armour grants regenerate 3% of maximum Life per second."), why=L("Paga o custo de vida das skills e o Berserk.", "Pays for skill life costs and Berserk.")),
 dict(order=5, key="heat", node="Heatproofing", when=L("Trial nível 60", "Level 60 Trial"), text=L("A body armour dá Unaffected by Damaging Ailments.", "Body Armour grants Unaffected by Damaging Ailments."), why=L("Ignite, Bleed e Poison não causam dano em você.", "Ignite, Bleed and Poison deal no damage to you.")),
 dict(order=6, key="dedication", node="Dedication to Kitava", when=L("Mapas", "Maps"), text=L("A body armour dá +100% da Armour também contra dano de Chaos.", "Body Armour grants +100% of Armour also applies to Chaos Damage."), why=L("Chaos Resistance deixa de ser urgente e paga a degeneração do Nebuloch.", "Chaos Resistance stops being urgent and pays for Nebuloch's degeneration.")),
 dict(order=7, key="forged", node="Forged in Flame", when=L("Mapas T5+", "Maps T5+"), text=L("Mods de resistência máxima a fogo também dão máxima de frio e raio.", "Modifiers to Maximum Fire Resistance also grant Maximum Cold and Lightning Resistance."), why=L("Purity of Fire e Unnatural Resilience sobem todas as máximas.", "Purity of Fire and Unnatural Resilience raise every maximum.")),
 dict(order=8, key="symbol", node="Molten Symbol", when=L("Mapas T5+", "Maps T5+"), text=L("A body armour dá 25% do dano físico recebido como fogo.", "Body Armour grants 25% of Physical Damage from Hits taken as Fire Damage."), why=L("Hits físicos batem na sua resistência a fogo enorme.", "Physical hits run into your huge fire resistance.")),
]
ASC_UNLOCK = [28, 58, 58, 62, 62, 68, 76, 76]

KEY_PASSIVES = [
 dict(node="Avatar of Fire", type="Keystone", text=L("75% do dano convertido em fogo; não causa dano não-fogo.", "75% of Damage Converted to Fire Damage; Deal no Non-Fire Damage."), when=L("Ato 4 → sempre", "Act 4 → forever"), why=L("Tudo escala com fogo e Ignite; a Fully Broken Armour (The Molten One's Gift) compensa a perda.", "Everything scales with fire and Ignite; Fully Broken Armour (The Molten One's Gift) offsets the loss.")),
 dict(node="The Molten One's Gift", type="Notable", text=L("+10% resistência a fogo; 15% increased efeito de Fully Broken Armour, que também aumenta o dano de fogo recebido.", "+10% fire resistance; 15% increased effect of Fully Broken Armour, which also increases fire damage taken."), when=L("Ato 3 → sempre", "Act 3 → forever"), why=L("Pré-requisito do Avatar of Fire.", "Prerequisite for Avatar of Fire.")),
 dict(node="Blood Magic", type="Keystone", text=L("Você não tem mana; custos de mana viram custo de vida.", "You have no Mana; skill mana costs converted to life costs."), when=L("Interlúdios → sempre", "Interludes → forever"), why=L("Resolve a mana; a ascendência dá vida e regen.", "Solves mana; the ascendancy gives life and regen.")),
 dict(node="Greatest Defence", type="Notable", text=L("4% increased dano de ataque por 75 de Armour/Evasion no escudo.", "4% increased Attack Damage per 75 Item Armour and Evasion on Equipped Shield."), when=L("Interlúdios → sempre", "Interludes → forever"), why=L("Escudo de 1000 de Armour = +53% de dano de ataque.", "A 1000 Armour shield = +53% attack damage.")),
 dict(node="Ichlotl's Inferno", type="Notable", text=L("Cada Rage dá 1% increased dano de fogo.", "Every Rage also grants 1% increased Fire Damage."), when=L("Mapas", "Maps"), why=L("Rage cheia = muito dano de fogo.", "Full Rage = lots of fire damage.")),
 dict(node="Endurance", type="Notable", text=L("+2 Endurance Charges máximas.", "+2 to Maximum Endurance Charges."), when=L("Mapas T5+", "Maps T5+"), why=L("Mais críticos do Nebuloch e mais Fortifying Cry sem cooldown.", "More Nebuloch crits and more cooldown-free Fortifying Cry.")),
]
TREE_STAGES = [
 dict(lv="1–31", focus=L("Melee e arma de uma mão", "Melee and one-handed"), dmg="Mace Strike / Boneshatter", **{"def": L("Vida", "Life")}, spirit="Magma Barrier", dont=L("Ignorar maças novas", "Ignoring new maces")),
 dict(lv="32–53", focus=L("Armour Break + warcries", "Armour Break + warcries"), dmg="Shield Wall + Fortifying Cry", **{"def": L("Armour + Coal Stoker", "Armour + Coal Stoker")}, spirit=L("Magma Barrier, Plating", "Magma Barrier, Plating"), dont=L("Avatar of Fire antes do Molten One's Gift", "Avatar of Fire before Molten One's Gift")),
 dict(lv="54–72", focus=L("Fogo, Ignite, Blood Magic", "Fire, Ignite, Blood Magic"), dmg=L("Shield Wall + Herald of Ash", "Shield Wall + Herald of Ash"), **{"def": L("Smith's Masterwork", "Smith's Masterwork")}, spirit="Herald of Ash", dont=L("Body Rare com Smith's Masterwork", "Rare body with Smith's Masterwork")),
 dict(lv="73–100", focus=L("Surrounded, Endurance, crítico", "Surrounded, Endurance, crit"), dmg="Ahn's Citadel + Kaom's Madness + Nebuloch", **{"def": L("Forged in Flame + Molten Symbol", "Forged in Flame + Molten Symbol")}, spirit="Purity of Fire, Berserk", dont=L("Nebuloch sem Endurance", "Nebuloch without Endurance")),
]

UNIQUES = [
 U("Nebuloch", L("Maça (Set 2)", "Mace (Set 2)"), L("Arma", "Weapon"), "t10", L("Ataques gastam uma Endurance Charge para dar crítico garantido; dano físico e Chaos adicionados e bônus de dano crítico. Cada charge causa 100 de Chaos por segundo em você.", "Attacks consume an Endurance Charge to Critically Hit; added physical and Chaos damage and critical damage bonus. Each charge deals 100 Chaos per second to you."), L("Weapon Set 2 com Shield Wall + Supercritical.", "Weapon Set 2 with Shield Wall + Supercritical."), L("Maça rare com + nível de melee e % dano elemental.", "Rare mace with + melee levels and % elemental damage.")),
 U("Constricting Command", L("Capacete", "Helmet"), L("Armadura", "Armour"), "t15", L("Vida, atributos, regeneração e exige 2–4 inimigos a menos para ficar Surrounded.", "Life, attributes, regeneration and requires 2–4 fewer enemies to be Surrounded."), L("Liga os notables de Surrounded quase sempre.", "Turns the Surrounded notables on almost always."), L("Capacete rare de vida/resistência; ou Thrillsteel (Onslaught).", "Rare life/resistance helmet; or Thrillsteel (Onslaught).")),
 U("For Utopia", "Charm", "Charm", "t15", L("Defende com 200% da Armour durante o efeito.", "Defend with 200% of Armour during its effect."), L("No slot de charm; ativa no gatilho da base (Stone Charm).", "In a charm slot; triggers on its base's condition (Stone Charm)."), L("Stone Charm normal.", "Normal Stone Charm.")),
 U("Guiding Palm of the Heart", L("Sceptre (Set 1)", "Sceptre (Set 1)"), L("Arma", "Weapon"), "t10", L("25% do dano como fogo extra, fogo para aliados e Força.", "25% of damage as extra fire, fire for allies and Strength."), L("Weapon Set 1 (utilidade).", "Weapon Set 1 (utility)."), L("Maça rare de dano elemental.", "Rare elemental damage mace.")),
 U("Sacred Flame", L("Sceptre (Set 1)", "Sceptre (Set 1)"), L("Arma", "Weapon"), "max", L("40–60% do dano como fogo extra; inimigos na Presence resistem usando a menor resistência elemental.", "40–60% of damage as extra fire; enemies in your Presence resist using their lowest elemental resistance."), L("Weapon Set 1 do setup otimizado.", "Weapon Set 1 of the optimized setup."), L("Guiding Palm of the Heart.", "Guiding Palm of the Heart.")),
 U("Thrillsteel", L("Capacete", "Helmet"), L("Armadura", "Armour"), "max", L("Onslaught permanente (mais velocidade de ataque e movimento).", "Permanent Onslaught (more attack and movement speed)."), L("Alternativa ao Constricting Command.", "Alternative to Constricting Command."), "Constricting Command"),
 U("The Fall of the Axe", "Charm", "Charm", "max", L("Onslaught durante o efeito.", "Onslaught during its effect."), L("Luxo.", "Luxury."), L("Silver Charm normal.", "Normal Silver Charm.")),
 U("Rite of Passage", "Charm", "Charm", "max", L("Espíritos animais aleatórios ao usar.", "Random animal spirits on use."), L("Luxo do setup otimizado.", "Luxury of the optimized setup."), L("Golden Charm.", "Golden Charm.")),
]

GEAR = [
 dict(slot=L("Escudo", "Shield"), cheap=L("Tower Shield com Armour alta (~350 no Ato 3, 800–900 nos mapas)", "Tower Shield with high Armour (~350 in Act 3, 800–900 in maps)"), value=L("1000+ de Armour + vida/resistência", "1000+ Armour + life/resistance"), full=L("Armour altíssima + Block", "Very high Armour + Block"), affix=L("% Armour; Armour; vida; resistência a fogo", "% Armour; Armour; life; fire resistance"), note=L("É o dano do Shield Wall e do Greatest Defence. Trave nos DOIS weapon sets.", "It's Shield Wall's and Greatest Defence's damage. Lock it to BOTH weapon sets.")),
 dict(slot=L("Maça", "Mace"), cheap=L("Duas maças de uma mão até o Ato 4", "Two one-handed maces until Act 4"), value=L("+3 melee + % dano elemental de ataques", "+3 melee + % elemental attack damage"), full=L("Nebuloch (Set 2) + Sacred Flame (Set 1)", "Nebuloch (Set 2) + Sacred Flame (Set 1)"), affix=L("+ nível de melee; % dano elemental; attack speed", "+ melee levels; % elemental damage; attack speed"), note=""),
 dict(slot=L("Capacete", "Helmet"), cheap=L("Vida + resistência a fogo", "Life + fire resistance"), value=L("Vida + Chaos Res", "Life + Chaos Res"), full="Constricting Command", affix=L("Vida; resist; Armour", "Life; resist; Armour"), note=""),
 dict(slot="Body Armour", cheap=L("Rare com Armour e vida (até o nível 58)", "Rare with Armour and life (until level 58)"), value=L("NORMAL de Armour alta (Smith's Masterwork)", "High-Armour NORMAL (Smith's Masterwork)"), full=L("Runeforged Ornate Plate (Normal) com runas", "Runeforged Ornate Plate (Normal) with runes"), affix=L("Base: Armour; sockets e qualidade", "Base: Armour; sockets and quality"), note=L("Com Smith's Masterwork a body precisa ser Normal: os mods vêm da ascendência.", "With Smith's Masterwork the body must be Normal: the mods come from the ascendancy.")),
 dict(slot=L("Luvas", "Gloves"), cheap=L("Attack speed + vida", "Attack speed + life"), value=L("+2 melee (caro) ou attack speed", "+2 melee (pricey) or attack speed"), full=L("Runeforged Ornate Mitts", "Runeforged Ornate Mitts"), affix=L("Attack speed; + melee; vida; resist", "Attack speed; + melee; life; resist"), note=""),
 dict(slot=L("Botas", "Boots"), cheap=L("Movement Speed", "Movement Speed"), value=L("30% MS + vida + resist", "30% MS + life + resist"), full=L("35% MS + vida + Chaos Res", "35% MS + life + Chaos Res"), affix=L("Movement Speed primeiro", "Movement Speed first"), note=""),
 dict(slot=L("Amuleto", "Amulet"), cheap=L("+ melee se tiver sorte; vida", "+ melee if lucky; life"), value=L("Vida + resist + Spirit", "Life + resist + Spirit"), full=L("Anoint Thaumaturgic Generator (Endurance)", "Thaumaturgic Generator anoint (Endurance)"), affix=L("+ melee; vida; Spirit", "+ melee; life; Spirit"), note=""),
 dict(slot=L("Anéis", "Rings"), cheap="Ruby Ring", value=L("Ruby com vida/fogo adicionado", "Ruby with life/added fire"), full="Breach Ring", affix=L("Resistência a fogo; vida; Chaos Res", "Fire resistance; life; Chaos Res"), note=L("Ruby Rings alimentam o Coal Stoker.", "Ruby Rings feed Coal Stoker.")),
 dict(slot=L("Cinto", "Belt"), cheap=L("Vida + Chaos Res", "Life + Chaos Res"), value=L("Vida + resists", "Life + resists"), full=L("Vida + resists + Força", "Life + resists + Strength"), affix=L("Vida; resist", "Life; resist"), note=""),
 dict(slot="Charms", cheap=L("Thawing + Stone + Silver", "Thawing + Stone + Silver"), value="For Utopia", full="The Fall of the Axe · Rite of Passage", affix=L("Freeze, Stun e Slow (Heatproofing já cobre ailments de dano)", "Freeze, Stun and Slow (Heatproofing already covers damaging ailments)"), note=""),
 dict(slot="Flasks", cheap=L("Vida", "Life"), value="Ultimate Life Flask", full=L("Ultimate Life Flask com qualidade", "Ultimate Life Flask with quality"), affix=L("Recuperação", "Recovery"), note=L("Blood Magic: sem mana, o flask de mana some.", "Blood Magic: no mana, the mana flask goes away.")),
]
BUY_ORDER = [
 dict(p=1, item=L("Maças com + nível de melee", "Maces with + melee levels"), phase=L("Atos 1–3", "Acts 1–3"), cost=L("Barato", "Cheap"), impact=L("Dano da campanha", "Campaign damage")),
 dict(p=2, item=L("Escudo de Armour alta", "High-Armour shield"), phase=L("Ato 3+", "Act 3+"), cost=L("Barato", "Cheap"), impact=L("Dano do Shield Wall", "Shield Wall damage")),
 dict(p=3, item=L("Peças com resistência a fogo", "Fire-resistance pieces"), phase=L("Mapas", "Maps"), cost=L("Barato", "Cheap"), impact=L("Resistências no cap (Coal Stoker)", "Resistances capped (Coal Stoker)")),
 dict(p=4, item="Nebuloch", phase="T5+", cost=L("Barato", "Cheap"), impact=L("Crítico garantido", "Guaranteed crit")),
 dict(p=5, item=L("Ahn's Citadel + Kaom's Madness", "Ahn's Citadel + Kaom's Madness"), phase="T5+", cost=L("Valor", "Value"), impact=L("Clear em todas as direções", "Clear in every direction")),
 dict(p=6, item="Constricting Command + For Utopia", phase="T10+", cost=L("Barato", "Cheap"), impact=L("Surrounded + defesa", "Surrounded + defence")),
 dict(p=7, item="Sacred Flame", phase="Pinnacle", cost=L("Valor", "Value"), impact=L("Fogo extra + menor resistência", "Extra fire + lowest resistance")),
]

TRICKS = [
 {"cat": L("Escudo", "Shield"), "lvl": L("Fácil", "Easy"), "title": L("Trave o escudo nos dois sets", "Lock the shield to both sets"), "body": L("Passe o mouse nos números romanos acima do escudo na tela de equipamento e use a tecla indicada para travá-lo nos Weapon Sets 1 e 2. Sem isso, metade das skills fica sem escudo.", "Hover the roman numerals above your shield on the equipment screen and use the shown key to lock it to Weapon Sets 1 and 2. Without it, half your skills have no shield.")},
 {"cat": L("Escudo", "Shield"), "lvl": L("Médio", "Medium"), "title": L("Cancelar a animação do Resonating Shield", "Animation-cancel Resonating Shield"), "body": L("Toques curtos no Resonating Shield batem quase o dobro de rápido: quebra Armour e prepara Stun muito mais depressa.", "Short taps on Resonating Shield hit almost twice as fast: breaks Armour and primes Stun much sooner.")},
 {"cat": L("Escudo", "Shield"), "lvl": L("Fácil", "Easy"), "title": L("Shield Bash prepara Stun", "Shield Bash primes Stun"), "body": L("Com Brink I, o Shield Bash do Raise Shield deixa quase todo inimigo não-unique pronto para Heavy Stun num golpe. Depois, Boneshatter.", "With Brink I, Raise Shield's Shield Bash primes almost every non-unique enemy for Heavy Stun in one hit. Then Boneshatter.")},
 {"cat": L("Dano", "Damage"), "lvl": L("Médio", "Medium"), "title": L("Quem quebra o Shield Wall", "What shatters Shield Wall"), "body": L("Slams (Leap Slam, Sunder), warcries (Infernal/Fortifying Cry) e Shield Charge quebram todos os segmentos de uma vez. As Shield Waves do Fortifying Cry saem de duas em duas: toques no Resonating Shield usam as que sobraram.", "Slams (Leap Slam, Sunder), warcries (Infernal/Fortifying Cry) and Shield Charge shatter every segment at once. Fortifying Cry's Shield Waves come out two at a time: Resonating Shield taps use the leftovers.")},
 {"cat": L("Dano", "Damage"), "lvl": L("Fácil", "Easy"), "title": L("Infernal Cry sempre antes", "Infernal Cry always first"), "body": L("O Infernal Cry empodera os próximos ataques: Shield Wall empoderado bate muito mais e o Ignite fica mais forte.", "Infernal Cry empowers your next attacks: an empowered Shield Wall hits much harder and its Ignite is stronger.")},
 {"cat": L("Dano", "Damage"), "lvl": L("Médio", "Medium"), "title": L("~40% de fogo recebido", "~40% fire taken"), "body": L("Fully Broken Armour (~20%) e Sundered Armour do Sunder (~20%) contam para fogo com The Molten One's Gift. Aplique os dois antes do nuke.", "Fully Broken Armour (~20%) and Sunder's Sundered Armour (~20%) count for fire with The Molten One's Gift. Apply both before the nuke.")},
 {"cat": L("Dano", "Damage"), "lvl": L("Avançado", "Advanced"), "title": L("Nebuloch + Supercritical", "Nebuloch + Supercritical"), "body": L("Nebuloch gasta uma Endurance Charge por ataque para dar crítico garantido; Supercritical troca chance por dano crítico (a chance não importa). Mantenha charges com Magma Barrier, Armour Break III e o anoint Thaumaturgic Generator.", "Nebuloch spends an Endurance Charge per attack for a guaranteed crit; Supercritical trades chance for crit damage (chance doesn't matter). Keep charges with Magma Barrier, Armour Break III and the Thaumaturgic Generator anoint.")},
 {"cat": L("Defesa", "Defence"), "lvl": L("Fácil", "Easy"), "title": L("Resistências com fogo", "Resistances through fire"), "body": L("Coal Stoker converte resistência a fogo em frio e raio (50%); Forged in Flame faz o mesmo com a máxima. Encha de Ruby Rings e fogo.", "Coal Stoker turns fire resistance into cold and lightning (50%); Forged in Flame does the same for the maximum. Stack Ruby Rings and fire.")},
 {"cat": L("Defesa", "Defence"), "lvl": L("Médio", "Medium"), "title": L("Body armour Normal", "Normal body armour"), "body": L("Smith's Masterwork só aceita body Normal (branca). Escolha a base de maior Armour, coloque qualidade, sockets e runas (Runeforged dá Runic Ward para o Scouring Flame).", "Smith's Masterwork only accepts a Normal (white) body. Pick the highest-Armour base and add quality, sockets and runes (Runeforged gives Runic Ward for Scouring Flame).")},
 {"cat": L("Defesa", "Defence"), "lvl": L("Fácil", "Easy"), "title": L("Charms certos", "Right charms"), "body": L("Heatproofing te deixa imune ao dano de Ignite/Bleed/Poison: use charms contra Freeze (Thawing), Stun (Stone) e Slow (Silver).", "Heatproofing makes you immune to Ignite/Bleed/Poison damage: use charms against Freeze (Thawing), Stun (Stone) and Slow (Silver).")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Warbringer para upar mais rápido", "Warbringer levels faster"), "body": L("O Lexd admite: Warbringer upa mais rápido (warcries sem cooldown). Dá para ascender Warbringer e trocar para Smith of Kitava no endgame refazendo o Trial.", "Lexd admits it: Warbringer levels faster (cooldown-free warcries). You can ascend Warbringer and swap to Smith of Kitava in endgame by redoing the Trial.")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Shock no boss", "Shock on bosses"), "body": L("Até o Avatar of Fire, uma maça com raio (ou Storm Rune) aplica Shock: mais dano em tudo.", "Until Avatar of Fire, a mace with lightning (or a Storm Rune) applies Shock: more damage on everything.")},
 {"cat": L("Leveling", "Leveling"), "lvl": L("Fácil", "Easy"), "title": L("Ruby Rings no Volcanic Warrens", "Ruby Rings in the Volcanic Warrens"), "body": L("Na luta dupla de golems do Volcanic Warrens, mate o Fire Golem por último para os anéis de fogo.", "In the Volcanic Warrens double golem fight, kill the Fire Golem last for the fire rings.")},
]

TROUBLESHOOT = [
 (L("Shield Wall bate fraco", "Shield Wall hits weakly"), L("Confira a Armour do escudo, se usou Infernal Cry antes e se o boss está com Fully Broken Armour + Sundered Armour.", "Check shield Armour, whether you used Infernal Cry first and whether the boss has Fully Broken Armour + Sundered Armour.")),
 (L("Metade das skills diz 'precisa de escudo'", "Half the skills say 'requires a shield'"), L("O escudo não está travado nos dois weapon sets.", "The shield isn't locked to both weapon sets.")),
 (L("Não dá crítico com Nebuloch", "No crits with Nebuloch"), L("Sem Endurance Charge não há crítico. Magma Barrier (bloqueando com o escudo levantado), Armour Break III e o anoint Thaumaturgic Generator.", "No Endurance Charge means no crit. Magma Barrier (block with the shield raised), Armour Break III and the Thaumaturgic Generator anoint.")),
 (L("Perco vida com Nebuloch", "I lose life with Nebuloch"), L("Cada charge causa 100 de Chaos por segundo. Dedication to Kitava (Armour contra Chaos) e regen (Leather Bindings) seguram.", "Each charge deals 100 Chaos per second. Dedication to Kitava (Armour vs Chaos) and regen (Leather Bindings) hold it.")),
 (L("Mana acaba nos Interlúdios", "Mana runs out in the Interludes"), L("Lifetap no Infernal Cry, rolls de mana e o Trial nível 60 cedo para pegar Blood Magic com a ascendência completa.", "Lifetap on Infernal Cry, mana rolls and the level 60 Trial early to take Blood Magic with the full ascendancy.")),
 (L("Monstros com muita resistência a fogo", "Monsters with high fire resistance"), L("Fire Penetration II no Shield Wall e Fire Exposure; no endgame a Sacred Flame usa a menor resistência do alvo.", "Fire Penetration II on Shield Wall and Fire Exposure; in endgame Sacred Flame uses the target's lowest resistance.")),
 (L("Herald of Ash não explode", "Herald of Ash doesn't explode"), L("Ele precisa estar ativo no weapon set do Shield Wall (Set 2) e de uma arma marcial nesse set.", "It must be active on the Shield Wall weapon set (Set 2) with a martial weapon in that set.")),
]

ATLAS_CHECK = [
 dict(stage=L("Antes do T1", "Before T1"), goal=L("Resists no cap · Blood Magic · Heatproofing", "Resists capped · Blood Magic · Heatproofing"), gear=L("Escudo 800+ · body Normal", "800+ shield · Normal body")),
 dict(stage="T1–T5", goal=L("Herald of Ash · Dedication to Kitava", "Herald of Ash · Dedication to Kitava"), gear=L("Maça +3 melee", "+3 melee mace")),
 dict(stage="T5–T15", goal=L("Ahn's Citadel + Kaom's Madness · Nebuloch", "Ahn's Citadel + Kaom's Madness · Nebuloch"), gear="Constricting Command · For Utopia"),
 dict(stage="Pinnacle", goal=L("Sacred Flame · Styrn's Mountain", "Sacred Flame · Styrn's Mountain"), gear="Rite of Passage"),
]

CRAFT = [
 L("Escudo: base de maior Armour, % Armour e Armour flat nos prefixos; vida e resistência a fogo nos sufixos.", "Shield: highest-Armour base, % Armour and flat Armour prefixes; life and fire resistance suffixes."),
 L("Body armour fica Normal (Smith's Masterwork): só qualidade, Artificer's Orb e runas — ou Runeforging na Verisium Anvil.", "Body armour stays Normal (Smith's Masterwork): only quality, Artificer's Orb and runes — or Runeforging at the Verisium Anvil."),
 L("Maça: + nível de melee e % dano elemental de ataques; Gnawed/Preserved Jawbone para um mod de Abyss.", "Mace: + melee levels and % elemental attack damage; Gnawed/Preserved Jawbone for an Abyss mod."),
]

T("item", L("Escudo de Armour alta", "High-Armour shield"), 1, L("Tower Shield", "Tower Shield"), L("Sempre: é o dano do Shield Wall.", "Always: it's Shield Wall's damage."), L("Mais Armour = mais dano de Shield Wall, Fortifying Cry e Greatest Defence.", "More Armour = more Shield Wall, Fortifying Cry and Greatest Defence damage."), "—", "—")
T("item", "Nebuloch", 1, L("Confira o nível no item", "Check the level on the item"), L("Mapas T5+.", "Maps T5+."), L("Crítico garantido gastando Endurance Charge.", "Guaranteed crit by spending an Endurance Charge."), L("Sem Endurance Charges estáveis ele atrapalha.", "Without steady Endurance Charges it hurts."), L("Maça rare.", "Rare mace."), watch=[L("100 de Chaos por segundo por charge.", "100 Chaos per second per charge.")])
T("item", "Constricting Command", 1, L("Confira o nível no item", "Check the level on the item"), L("T10+.", "T10+."), L("Surrounded quase sempre + vida e regen.", "Surrounded almost always + life and regen."), "—", "Thrillsteel")
T("item", "Sacred Flame", 1, L("Confira o nível no item", "Check the level on the item"), L("Pinnacle.", "Pinnacle."), L("Fogo extra e menor resistência elemental.", "Extra fire and lowest elemental resistance."), "—", "Guiding Palm of the Heart")
T("skill", "Shield Wall", 20, L("Gem tier 7", "Tier 7 gem"), L("Ato 2 (boss) → carry do Ato 3 em diante.", "Act 2 (boss) → carry from Act 3 on."), L("Muros que explodem.", "Walls that explode."), L("Sem detonador rápido, só no boss.", "Without a fast detonator, bosses only."), "—")
T("skill", "Fortifying Cry", 34, L("Gem tier 9", "Tier 9 gem"), L("Ato 3.", "Act 3."), L("Detona o Shield Wall e dá Guard.", "Detonates Shield Wall and grants Guard."), "—", "—")
T("key", "Avatar of Fire", 45, L("Keystone da árvore", "Tree keystone"), L("Ato 4, depois do The Molten One's Gift.", "Act 4, after The Molten One's Gift."), L("75% do dano vira fogo.", "75% of damage becomes fire."), L("Antes do Molten One's Gift você perde dano.", "Before Molten One's Gift you lose damage."), "—")
T("key", "Blood Magic", 58, L("Keystone da árvore", "Tree keystone"), L("Interlúdios, com a ascendência completa.", "Interludes, with the full ascendancy."), L("Sem mana; custos em vida.", "No mana; costs in life."), L("Sem regen/vida da ascendência fica perigoso.", "Without the ascendancy's regen/life it's dangerous."), "—")
T("asc", "Smith's Masterwork", 58, L("Ascendência Smith of Kitava", "Smith of Kitava ascendancy"), L("Trial nível 60.", "Level 60 Trial."), L("Body Normal ganha os bônus da ascendência.", "A Normal body gains the ascendancy bonuses."), L("Exige trocar a body rare por uma Normal.", "Requires swapping the rare body for a Normal one."), "—")

CASES = [
 (L("Achei Nebuloch cedo", "I found Nebuloch early"), L("Guarde até ter Endurance Charges estáveis (Magma Barrier + Armour Break III); antes disso uma maça rare rende mais.", "Keep it until you have steady Endurance Charges (Magma Barrier + Armour Break III); before that a rare mace is better.")),
 (L("Quero upar mais rápido", "I want to level faster"), L("Ascenda Warbringer na campanha e troque para Smith of Kitava refazendo o Trial no endgame (dica do Lexd).", "Ascend Warbringer in the campaign and swap to Smith of Kitava by redoing the Trial in endgame (Lexd's tip).")),
 (L("Sou SSF e não acho os uniques", "I'm SSF and can't find the uniques"), L("As variantes T1–T10 são SSF friendly: maça rare, escudo de Armour alta e body Normal resolvem.", "The T1–T10 variants are SSF friendly: a rare mace, a high-Armour shield and a Normal body do the job.")),
]

SOURCES = [
 dict(name="Lexd — 0.5.5 Shield Wall + Avatar of Fire Smith of Kitava (Mobalytics)", use=L("Build base: 11 variantes, gems, itens, árvore e notas por ato", "Base build: 11 variants, gems, items, tree and notes per act"), url=GUIDE_URL),
 dict(name="poe.ninja — Smith of Kitava (Forbidden Rites)", use=L("Meta (Shield Wall e Infernal Cry lideram) e preços", "Meta (Shield Wall and Infernal Cry lead) and prices"), url="https://poe.ninja/poe2/builds/forbiddenrites?class=Smith+of+Kitava"),
 dict(name="Path of Building (PoE2) — Gems.lua, Skills", use=L("Descrições das gems, custos de Spirit e tiers", "Gem descriptions, Spirit costs and tiers"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
 dict(name=L("Árvore 0.5 (Path of Building)", "0.5 tree (Path of Building)"), use=L("Nós, ascendência Smith of Kitava e keystones", "Nodes, Smith of Kitava ascendancy and keystones"), url="https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2"),
]
FIXES = [
 L("As variantes 'Lategame' e 'Thrillsteel' não entram na rota: a 'Optimized' substitui a primeira e o Thrillsteel aparece como alternativa de capacete.", "The 'Lategame' and 'Thrillsteel' variants aren't in the route: 'Optimized' replaces the first and Thrillsteel appears as a helmet alternative."),
 L("O custo de Spirit da Purity of Fire não está nos dados do Path of Building: confira no jogo.", "Purity of Fire's Spirit cost isn't in Path of Building's data: check in game."),
 L("A ordem e os níveis da ascendência seguem as variantes do guia; os Trials podem ser feitos antes ou depois.", "Ascendancy order and levels follow the guide's variants; Trials can be done earlier or later."),
]

UI = dict(
 carry=r"^(Shield Wall|Mace Strike)$", box=L("ESCUDO", "SHIELD"), spiritWhat=L("(buffs persistentes)", "(persistent buffs)"),
 mechBtn=L("Abrir Escudo & Fogo", "Open Shield & Fire"), dmg2="Herald of Ash", dmgBar=L("Dano seu (aprox.)", "Your damage (approx.)"),
 dmgLegend=L("explosões do Herald of Ash (proporção aproximada)", "Herald of Ash explosions (approximate ratio)"),
 earlyGone=L("Skills iniciais já saíram da barra: você passou do nível {u}.", "Starting skills already left the bar: you're past level {u}."),
 earlyNote=L("Skills de começo; saem no nível ~{u}.", "Early skills; they leave around level {u}."),
 treeIntro=L("Árvore real do patch 0.5.5 com o caminho do guia do Lexd em cada fase. Atos 1–2: melee de uma mão. Atos 3–4: Armour Break, warcries e Avatar of Fire. Endgame: Surrounded, Endurance e crítico.", "Real patch 0.5.5 tree with Lexd's guide path for each phase. Acts 1–2: one-handed melee. Acts 3–4: Armour Break, warcries and Avatar of Fire. Endgame: Surrounded, Endurance and crit."),
 set1=L("clear e utilidade", "clear and utility"), set2=L("boss e Ignite", "boss and Ignite"), asc="Smith of Kitava", cls="Warrior",
 respecTip=L("No Ato 4 as maças duplas saem: os pontos de arma de uma mão viram Weapon Set Points. Set 1 = clear/warcries; Set 2 = boss/Ignite.", "In Act 4 the dual maces go: one-handed points become Weapon Set Points. Set 1 = clear/warcries; Set 2 = boss/Ignite."),
 routeIntro=L("Nove fases do guia do Lexd: maças duplas até o Ato 3, Shield Wall + Fortifying Cry a partir daí e Avatar of Fire no Ato 4.", "Nine phases from Lexd's guide: dual maces until Act 3, Shield Wall + Fortifying Cry from there and Avatar of Fire in Act 4."),
 socketPrio=["Shield Wall (Perfect Jeweller's Orb)", "Resonating Shield", "Fortifying Cry · Infernal Cry", "Magma Barrier", "Scavenged Plating"],
 permIntro=L("Nada disso volta depois. Spirit paga Magma Barrier, Scavenged Plating, Herald of Ash, Purity of Fire e Berserk. Weapon Set Points alimentam o Set 1 (clear) e o Set 2 (boss).", "None of this comes back later. Spirit pays for Magma Barrier, Scavenged Plating, Herald of Ash, Purity of Fire and Berserk. Weapon Set Points fuel Set 1 (clear) and Set 2 (boss)."),
 atlasCards=[[L("200% Delirium e Grand Expeditions", "200% Delirium and Grand Expeditions"), L("Com Ahn's Citadel + Kaom's Madness o Lexd faz 200% Delirium e Grand Expeditions juiced: é o motivo da troca para esse clear.", "With Ahn's Citadel + Kaom's Madness Lexd runs 200% Delirium and juiced Grand Expeditions: it's why he switched to this clear.")],
             [L("Monstros de resistência a fogo", "Fire-resistant monsters"), L("Mods 'gold' de resistência a fogo são o ponto fraco: Fire Penetration II, Fire Exposure e, no endgame, Sacred Flame.", "'Gold' fire-resistance mods are the weak point: Fire Penetration II, Fire Exposure and, in endgame, Sacred Flame.")]],
 foot=L("Guia baseado no build do Lexd (Mobalytics), dados de jogo do Path of Building e preços do poe.ninja", "Guide based on Lexd's build (Mobalytics), Path of Building game data and poe.ninja prices"),
)

CHAR = dict(
 intro=L("Marque o que você tem. As recomendações e as abas Skills, Itens, Árvore e Escudo & Fogo se adaptam na hora. Tudo fica salvo neste navegador.", "Tick what you have. Recommendations and the Skills, Items, Tree and Shield & Fire tabs adapt instantly. Everything is saved in this browser."),
 nums=[["spirit", L("Spirit máximo", "Max Spirit"), L("ex.: 120", "e.g. 120")], ["shield", L("Armour do escudo", "Shield Armour"), L("ex.: 900", "e.g. 900")], ["life", L("Vida máxima", "Max life"), ""]],
 tiles=[[L("Spirit reservado", "Spirit reserved"), "used"], [L("Spirit livre", "Spirit free"), "free"], [L("Armour do escudo", "Shield Armour"), "shield"]],
 buffs=[dict(key="magma", name="Magma Barrier", cost=30), dict(key="plating", name="Scavenged Plating", cost=30), dict(key="herald", name="Herald of Ash", cost=30), dict(key="berserk", name="Berserk", cost=30)],
 own=[
  ["gear", "dual", L("Duas maças de uma mão (Set 2)", "Two one-handed maces (Set 2)")], ["gear", "normalbody", L("Body armour Normal", "Normal body armour")], ["gear", "lockshield", L("Escudo travado nos dois sets", "Shield locked to both sets")],
  ["gear", "Nebuloch", "Nebuloch"], ["gear", "Constricting Command", "Constricting Command"], ["gear", "For Utopia", "For Utopia"], ["gear", "Sacred Flame", "Sacred Flame"], ["gear", "Guiding Palm of the Heart", "Guiding Palm of the Heart"], ["gear", "Thrillsteel", "Thrillsteel"],
  ["gem", "magma", "Magma Barrier (30)"], ["gem", "plating", "Scavenged Plating (30)"], ["gem", "herald", "Herald of Ash (30)"], ["gem", "berserk", "Berserk (30)"], ["gem", "wall", "Shield Wall"], ["gem", "fort", "Fortifying Cry"], ["gem", "ahn", "Ahn's Citadel"], ["gem", "kaom", "Kaom's Madness"], ["gem", "firepen", "Fire Penetration II"],
  ["tree", "molten", "The Molten One's Gift"], ["tree", "avatar", "Avatar of Fire"], ["tree", "blood", "Blood Magic"], ["tree", "greatest", "Greatest Defence"], ["tree", "endurance", "Endurance"],
  ["asc", "coal", "Coal Stoker"], ["asc", "master", "Smith's Masterwork"], ["asc", "engraving", "Kitavan Engraving"], ["asc", "bindings", "Leather Bindings"], ["asc", "heat", "Heatproofing"], ["asc", "dedication", "Dedication to Kitava"], ["asc", "forged", "Forged in Flame"], ["asc", "symbol", "Molten Symbol"],
 ],
 rules=[
  dict(when=dict(own=["avatar"], notOwn=["molten"]), lvl="bad", t=L("Avatar of Fire sem The Molten One's Gift", "Avatar of Fire without The Molten One's Gift"), d=L("Sem ele a Fully Broken Armour não aumenta o fogo recebido e você perde dano.", "Without it Fully Broken Armour doesn't increase fire taken and you lose damage."), tab="arvore"),
  dict(when=dict(own=["master"], notOwn=["normalbody"]), lvl="bad", t=L("Smith's Masterwork com body não-Normal", "Smith's Masterwork with a non-Normal body"), d=L("Ele só aceita body armour Normal (branca).", "It only accepts a Normal (white) body armour."), tab="gear"),
  dict(when=dict(lvMin=45, notOwn=["lockshield"]), lvl="warn", t=L("Trave o escudo nos dois weapon sets", "Lock the shield to both weapon sets"), d=L("Passe o mouse nos números romanos acima do escudo.", "Hover the roman numerals above the shield."), tab="mech"),
  dict(when=dict(own=["blood"], notOwn=["bindings"]), lvl="warn", t=L("Blood Magic sem Leather Bindings", "Blood Magic without Leather Bindings"), d=L("As skills custam vida: pegue a regen da ascendência.", "Skills cost life: take the ascendancy's regen."), tab="asc"),
  dict(when=dict(own=["Nebuloch"], notOwn=["magma"]), lvl="bad", t=L("Nebuloch sem Magma Barrier", "Nebuloch without Magma Barrier"), d=L("Sem Endurance Charges não há crítico.", "No Endurance Charges means no crits."), tab="skills"),
  dict(when=dict(own=["Nebuloch"], notOwn=["dedication"]), lvl="warn", t=L("Nebuloch sem Dedication to Kitava", "Nebuloch without Dedication to Kitava"), d=L("Cada charge dá 100 de Chaos por segundo em você.", "Each charge deals 100 Chaos per second to you."), tab="asc"),
  dict(when=dict(lvMin=36, notOwn=["fort"]), lvl="warn", t=L("Sem Fortifying Cry", "No Fortifying Cry"), d=L("É o detonador do Shield Wall.", "It's Shield Wall's detonator."), tab="skills"),
  dict(when=dict(lvMin=60, notOwn=["firepen"]), lvl="tip", t="Fire Penetration II", d=L("Resolve os monstros com resistência a fogo alta.", "Solves high fire-resistance monsters."), tab="skills"),
  dict(when=dict(lvMin=74, notOwn=["ahn", "kaom"]), lvl="tip", t=L("Ahn's Citadel + Kaom's Madness", "Ahn's Citadel + Kaom's Madness"), d=L("A grande virada do clear no endgame.", "The big endgame clear upgrade."), tab="skills"),
  dict(when=dict(numLt=["shield", 800], lvMin=65), lvl="warn", t=L("Escudo com pouca Armour", "Low-Armour shield"), d=L("800–900 de Armour para os primeiros mapas; é o dano da build.", "800–900 Armour for early maps; it's the build's damage."), tab="gear"),
  dict(when=dict(lvMin=46, own=["dual"]), lvl="tip", t=L("Aposente as maças duplas", "Retire the dual maces"), d=L("No Ato 4 o escudo vai para os dois sets.", "In Act 4 the shield goes to both sets."), tab="mech"),
  dict(when=dict(own=["berserk"], notOwn=["bindings"]), lvl="warn", t=L("Berserk sem regen", "Berserk without regen"), d=L("Pegue Leather Bindings e Vitality antes.", "Take Leather Bindings and Vitality first."), tab="asc"),
 ],
)
ADAPT_SWAPS = [
 dict(pids=["t10", "t15", "max"], when=dict(notOwn=["Nebuloch"]), gemsFrom="maps", note=L("Sem Nebuloch: mostrando o setup dos mapas T1–T5.", "No Nebuloch: showing the T1–T5 maps setup.")),
 dict(pids=["a4", "int"], when=dict(notOwn=["avatar"]), gemsFrom="a3", note=L("Sem Avatar of Fire: mostrando o setup do Ato 3.", "No Avatar of Fire: showing the Act 3 setup.")),
]
TREE_RULES = [
 dict(when=dict(lvMin=40, notOwn=["molten"]), t=L("The Molten One's Gift antes do Avatar of Fire.", "The Molten One's Gift before Avatar of Fire."), node="The Molten One's Gift"),
 dict(when=dict(own=["molten"], notOwn=["avatar"], lvMin=44), t=L("Pronto para o Avatar of Fire.", "Ready for Avatar of Fire."), node="Avatar of Fire"),
 dict(when=dict(lvMin=56, own=["bindings"], notOwn=["blood"]), t=L("Com a regen da ascendência, pegue Blood Magic.", "With the ascendancy regen, take Blood Magic."), node="Blood Magic"),
]
TIMING_KEY = {"Nebuloch": "Nebuloch", "Constricting Command": "Constricting Command", "Sacred Flame": "Sacred Flame", "Shield Wall": "wall", "Fortifying Cry": "fort", "Avatar of Fire": "avatar", "Blood Magic": "blood", "Smith's Masterwork": "master"}

MECH = dict(
 title=L("Escudo & Fogo", "Shield & Fire"),
 intro=L("Como a Smith mata e aguenta: muros de terra que explodem, Armour quebrada que vira dano de fogo e uma body armour forjada pela ascendência.", "How the Smith kills and tanks: walls of earth that explode, broken Armour that becomes fire damage and a body armour forged by the ascendancy."),
 sections=[
  dict(type="cards", cards=[
   [L("1. Shield Wall", "1. Shield Wall"), L("Crava o escudo no chão e levanta segmentos de muro. Slams, warcries e Shield Charge quebram todos; cada segmento explode em volta. O dano escala com a Armour do escudo.", "Rams the shield into the ground and raises wall segments. Slams, warcries and Shield Charge shatter them all; each segment explodes around it. Damage scales with shield Armour.")],
   [L("2. Detonação", "2. Detonation"), L("Infernal Cry empodera antes; Fortifying Cry dá Guard e solta Shield Waves nos ataques de escudo, quebrando os muros. Enraged Warcry gasta Rage para pular o cooldown; Endurance Charge também pula o do Fortifying Cry.", "Infernal Cry empowers first; Fortifying Cry grants Guard and fires Shield Waves on shield attacks, shattering the walls. Enraged Warcry spends Rage to skip the cooldown; an Endurance Charge also skips Fortifying Cry's.")],
   [L("3. Armour quebrada vira fogo", "3. Broken Armour becomes fire"), L("Resonating Shield leva o boss a Fully Broken Armour; Sunder aplica Sundered Armour. Com The Molten One's Gift os dois aumentam o dano de FOGO recebido (~40% somados) — e com Avatar of Fire todo o seu dano é fogo.", "Resonating Shield takes the boss to Fully Broken Armour; Sunder applies Sundered Armour. With The Molten One's Gift both increase FIRE damage taken (~40% together) — and with Avatar of Fire all your damage is fire.")],
   [L("4. A forja", "4. The forge"), L("Smith's Masterwork exige body armour Normal e a ascendência 'grava' bônus nela: +15% vida, 3% regen, imunidade a dano de ailments, Armour contra Chaos, 25% do físico como fogo. Coal Stoker e Forged in Flame transformam fogo em todas as resistências.", "Smith's Masterwork requires a Normal body armour and the ascendancy 'engraves' bonuses into it: +15% life, 3% regen, immunity to ailment damage, Armour vs Chaos, 25% of physical as fire. Coal Stoker and Forged in Flame turn fire into every resistance.")],
  ]),
  dict(type="rotation", blocks=[
   [L("Boss", "Boss"), [L("Resonating Shield (toques rápidos) até Fully Broken Armour", "Resonating Shield (quick taps) until Fully Broken Armour"), L("Sunder: Sundered Armour", "Sunder: Sundered Armour"), L("Rage cheia", "Full Rage"), L("Infernal Cry → Shield Wall", "Infernal Cry → Shield Wall"), L("Fortifying Cry detona; Raise Shield com Scouring Flame mantém o Ignite", "Fortifying Cry detonates; Raise Shield with Scouring Flame keeps Ignite up")]],
   [L("Clear", "Clear"), [L("Shield Wall no pack", "Shield Wall on the pack"), L("Fortifying Cry ou Shield Charge para detonar", "Fortifying Cry or Shield Charge to detonate"), L("Canalize Resonating Shield andando (Rage + Plating)", "Channel Resonating Shield while moving (Rage + Plating)"), L("Rares teimosos: Set 2 com crítico do Nebuloch", "Stubborn rares: Set 2 with Nebuloch crits")]],
  ]),
  dict(type="table", h=L("Weapon sets", "Weapon sets"), cols=[L("Fase", "Phase"), "Weapon Set 1", "Weapon Set 2"], rows=[
   [L("Atos 1–3", "Acts 1–3"), L("Maça + escudo", "Mace + shield"), L("Duas maças (Mace Strike)", "Two maces (Mace Strike)")],
   [L("Ato 4 → mapas", "Act 4 → maps"), L("Maça + escudo: warcries, Resonating Shield, Sunder", "Mace + shield: warcries, Resonating Shield, Sunder"), L("Maça + escudo: Shield Wall, Infernal Cry, Herald of Ash", "Mace + shield: Shield Wall, Infernal Cry, Herald of Ash")],
   ["T5+", L("Guiding Palm/Sacred Flame + escudo", "Guiding Palm/Sacred Flame + shield"), L("Nebuloch + escudo: Shield Wall (Supercritical)", "Nebuloch + shield: Shield Wall (Supercritical)")],
   [L("Sempre", "Always"), L("Escudo travado nos dois sets", "Shield locked to both sets"), L("Escudo travado nos dois sets", "Shield locked to both sets")],
  ]),
  dict(type="table", h=L("O que a ascendência grava na body armour", "What the ascendancy engraves on the body armour"), cols=[L("Nó", "Node"), L("Efeito", "Effect"), L("Quando", "When")], rows=[
   ["Kitavan Engraving", L("+15% vida máxima", "+15% maximum life"), L("Nível ~58", "Level ~58")],
   ["Leather Bindings", L("Regenera 3% da vida/s", "Regenerate 3% life/s"), L("Nível ~62", "Level ~62")],
   ["Heatproofing", L("Imune a dano de Ignite/Bleed/Poison", "Unaffected by damaging ailments"), L("Nível ~62", "Level ~62")],
   ["Dedication to Kitava", L("+100% da Armour contra Chaos", "+100% of Armour vs Chaos"), L("Mapas", "Maps")],
   ["Molten Symbol", L("25% do físico recebido como fogo", "25% of physical taken as fire"), "T5+"],
  ]),
  dict(type="spirit", h=L("Spirit dos buffs", "Buff Spirit"), p=L("Marque o que você usa. Custos do Path of Building.", "Tick what you use. Costs from Path of Building."),
       note=L("Ordem: Magma Barrier → Scavenged Plating → Herald of Ash → Berserk. Purity of Fire reserva à parte (confira no jogo).", "Order: Magma Barrier → Scavenged Plating → Herald of Ash → Berserk. Purity of Fire reserves separately (check in game).")),
  dict(type="timeline", h=L("Escudo e arma por nível", "Shield and weapon by level"), items=[
   dict(lv=1, t=L("Escudo + duas maças", "Shield + two maces"), d=L("Maças com + melee e físico; olhe vendors toda hora.", "Maces with + melee and physical; check vendors constantly.")),
   dict(lv=32, t=L("Escudo ~350 de Armour", "~350 Armour shield"), d=L("Shield Wall + Fortifying Cry apagam bosses.", "Shield Wall + Fortifying Cry delete bosses.")),
   dict(lv=45, t=L("Avatar of Fire", "Avatar of Fire"), d=L("Maça com % dano elemental; escudo nos dois sets.", "Mace with % elemental damage; shield on both sets.")),
   dict(lv=58, t=L("Body Normal", "Normal body"), d=L("Smith's Masterwork + Blood Magic.", "Smith's Masterwork + Blood Magic.")),
   dict(lv=65, t=L("Escudo 800–900", "800–900 shield"), d=L("Maça +3 melee e resistências no cap.", "+3 melee mace and capped resistances.")),
   dict(lv=74, t="Nebuloch", d=L("Set 2 com Ahn's Citadel + Kaom's Madness.", "Set 2 with Ahn's Citadel + Kaom's Madness.")),
   dict(lv=92, t="Sacred Flame", d=L("Set 1 do setup otimizado.", "Set 1 of the optimized setup.")),
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
            q["reward"] = L("ESCOLHA: 30% increased Armour, Evasion e ES", "CHOICE: 30% increased Armour, Evasion and ES"); q["prio"] = "Alta"
        if q["boss"] == "Venom Draught":
            q["reward"] = L("ESCOLHA: 25% Stun Threshold (ajuda o Raise Shield)", "CHOICE: 25% Stun Threshold (helps Raise Shield)"); q["prio"] = "Média"
        quests.append(q)
    return dict(league=LEAGUE, patch=PATCH, updated=UPDATED, snap="15/09/2026", phases=PHASES, milestones=MILESTONES, gear=GEAR, uniques=UNIQUES, idols=[],
                sets={}, jewelSets={}, optimizations=[], tricks=TRICKS, fixes=FIXES, sources=SOURCES, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
                buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=GUIDE_URL, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT], quests=quests,
                atlas={}, atlasCheck=ATLAS_CHECK, ascendancy=ASCENDANCY, ascUnlock=ASC_UNLOCK, timing=BOOK.TIMING, timingCases=[dict(q=a, a=b) for a, b in CASES],
                craft=CRAFT, current={"note": "", "items": []}, meta=None, beasts=[], auraPriority=[], hunt=None,
                ui=UI, char=CHAR, mech=MECH, adaptSwaps=ADAPT_SWAPS, treeRules=TREE_RULES, timingKey=TIMING_KEY, phaseAct=PHASE_ACT, treeOrder=ORDER + ["uber"], craftKit=CRAFT_KIT)
