# -*- coding: utf-8 -*-
"""Aba "Caçar companions": como capturar, onde achar cada beast, truques de farm e o que buscar nos mapas.

Fontes (conferidas em 16/09/2026):
- Mattjestic — "NEW 0.5 Rare Beast Companions TIER-LIST: Location & Farming Guide" (Mobalytics, 25/06/2026)
- Mattjestic — "Abyss Monster Mods For 0.5 Taming" (Mobalytics, 25/06/2026)
- Lolcohol — "PoE 2 Companion Guide and Farming Locations" (Mobalytics)
Cada texto é (pt, en).
"""

SOURCES = [
    ("Mattjestic — 0.5 Rare Beast Companions Tier-List", "https://mobalytics.gg/poe-2/profile/mattjestic-multigaming/guides/new-0-4-ultra-rare-beast-companion-farming-guide"),
    ("Mattjestic — Abyss Monster Mods For 0.5 Taming", "https://mobalytics.gg/poe-2/profile/mattjestic-multigaming/guides/abyss-monster-mods-for-0-5-taming"),
    ("Lolcohol — Companion Guide and Farming Locations", "https://mobalytics.gg/poe-2/guides/companions-tame-beast"),
]

# haste: "sim" confirmado nas fontes, "nao" confirmado que não rola, None = fontes não dizem
BEASTS = [
    ("Plague Swarm", 21.0, ("Ato 2 · Mawdun Quarry", "Act 2 · Mawdun Quarry"), ("Essence", "Essence"), None, ""),
    ("Swarming Wisp", 21.0, ("Ato 5 · Ashen Forest", "Act 5 · Ashen Forest"), ("Essence", "Essence"), "nao", ""),
    ("Bloodthief Wasp", 21.0, ("Ato 5 · Qimah / Sandswept Marsh", "Act 5 · Qimah / Sandswept Marsh"), ("Essence (muito raro)", "Essence (very rare)"), None, ("Mattjestic diz que é muito difícil de achar; um comentário do guia aponta o Sandswept Marsh.", "Mattjestic says it's very hard to find; a guide comment points to Sandswept Marsh.")),
    ("Crag Leaper", 23.1, ("Ato 2 · Vastiri Outskirts", "Act 2 · Vastiri Outskirts"), ("Essence", "Essence"), "nao", ("very_fast_movement: nunca rola Haste.", "very_fast_movement: never rolls Haste.")),
    ("Flesh Larva", 23.1, ("Mapas (Atlas)", "Maps (Atlas)"), ("Encontro de Essence aleatório em mapas", "Random Essence encounter in maps"), None, ""),
    ("Quill Crab (Porcupine)", 24.9, ("Ato 4 · Whakapanu Island (praia do início)", "Act 4 · Whakapanu Island (starting beach)"), ("Essence e raros", "Essence and rares"), "sim", ("24,9% vindo de Essence; pode vir com 26%.", "24.9% from Essence; can come at 26%.")),
    ("Coconut Crab", 24.9, ("Ato 4 · Whakapanu Island (praia do início)", "Act 4 · Whakapanu Island (starting beach)"), ("Essence e raros", "Essence and rares"), "sim", ("24,9% vindo de Essence; pode vir com 26%.", "24.9% from Essence; can come at 26%.")),
    ("Bramble Ape", 24.9, ("Ato 5 · Kriar Village", "Act 5 · Kriar Village"), ("Raro", "Rare"), None, ""),
    ("Rasp Scavenger", 26.7, ("Ato 5 · Khari Crossing", "Act 5 · Khari Crossing"), ("Essence (26,7%) · raro normal custa 32,7%", "Essence (26.7%) · normal rare costs 32.7%"), None, ""),
    ("Winged Fiend", 26.7, ("Ato 5 · Qimah", "Act 5 · Qimah"), ("Essence", "Essence"), None, ""),
    ("Sabre Spider", 28.2, ("Ato 5 · Ashen Forest (junto dos Wisps)", "Act 5 · Ashen Forest (alongside the Wisps)"), ("Raro", "Rare"), None, ""),
    ("Hyena Demon", 30.0, ("Ato 2 · Vastiri Outskirts", "Act 2 · Vastiri Outskirts"), ("Essence (raro)", "Essence (rare)"), "nao", ""),
    ("Crustic Crab", 32.1, ("Ato 5 · Whakapanu Island", "Act 5 · Whakapanu Island"), ("Essence e raros", "Essence and rares"), None, ""),
    ("Bane Sapling", 33.3, ("Ato 3 · Jungle Ruins", "Act 3 · Jungle Ruins"), ("Raro, chance baixa", "Rare, low chance"), None, ""),
    ("Diretusk Boar", 39.0, ("Ato 3 · Infested Barrens (Troubled Camp)", "Act 3 · Infested Barrens (Troubled Camp)"), ("Spawn GARANTIDO — reroll pelo checkpoint", "GUARANTEED spawn — reroll via checkpoint"), "sim", ("Mais rápido que a Quadrilla.", "Faster than the Quadrilla.")),
    ("Antlion Charger", 42.3, ("Ato 3 · Infested Barrens (Troubled Camp)", "Act 3 · Infested Barrens (Troubled Camp)"), ("Spawn GARANTIDO — reroll pelo checkpoint", "GUARANTEED spawn — reroll via checkpoint"), "sim", ("Tende a rolar para longe de você: pode sair da sua Presence e a aura não te pega.", "Tends to roll away from you: it can leave your Presence and the aura won't reach you.")),
    ("Quadrilla", 42.3, ("Ato 3 · Jungle Ruins (Troubled Camp)", "Act 3 · Jungle Ruins (Troubled Camp)"), ("Spawn garantido — reroll pelo checkpoint", "Guaranteed spawn — reroll via checkpoint"), "nao", ("Não rola Haste Aura, mas serve para farmar as outras auras T1.", "Can't roll Haste Aura, but good for farming other T1 auras.")),
    ("Zekoa, the Headcrusher", 47.4, ("Mapas Riverside e Rupture (boss)", "Riverside and Rupture maps (boss)"), ("Boss do mapa — precisa de The Natural Order", "Map boss — needs The Natural Order"), None, ("Versão de Atlas do Silverfist. Veja a seção Zekoa abaixo.", "Atlas version of Silverfist. See the Zekoa section below.")),
]

STEPS_CAPTURE = [
    ("Coloque a gem Tame Beast na barra. Passe o mouse em um monstro RARO: aparece o tipo dele embaixo da vida e os modificadores.", "Put the Tame Beast gem on your bar. Hover a RARE monster: its type shows under the health bar, along with its modifiers."),
    ("Antes de começar, DESLIGUE os companions e minions (e o urso do Wild Protector), ou eles matam o beast antes da hora.", "Before starting, TURN OFF companions and minions (and the Wild Protector bear), or they kill the beast too early."),
    ("Tire vida do beast até conseguir matá-lo rápido. A janela de captura dura de 8 s (gem nível 1) a 11,8 s (nível 20).", "Bring the beast's life down until you can kill it quickly. The capture window lasts 8 s (gem level 1) to 11.8 s (level 20)."),
    ("Use Tame Beast: o beast fica envolto em wisps. Mate ENQUANTO os wisps estão nele — sem wisps não captura.", "Cast Tame Beast: the beast gets wrapped in wisps. Kill it WHILE the wisps are on it — no wisps, no capture."),
    ("A gem vira uma gem de Companion com o nome do beast e até 4 modificadores dele. Ative clicando com o botão direito na gem.", "The gem turns into a Companion gem with the beast's name and up to 4 of its modifiers. Activate it by right-clicking the gem."),
    ("Precisa de outra captura? Venda (disenchant) um Companion que não usa no vendor: volta uma gem Tame Beast do mesmo nível.", "Need another capture? Disenchant a Companion you don't use at a vendor: you get back a Tame Beast gem of the same level."),
]

TRICKS = [
    (("Reroll grátis pelo checkpoint (spawns garantidos)", "Free reroll via checkpoint (guaranteed spawns)"),
     ("No Infested Barrens (Ato 3), ao lado do Troubled Camp, sempre nascem 2 beasts raros: um Diretusk Boar e um Antlion. Veja os mods SEM matar. Não gostou? Esc → Respawn at Checkpoint: os modificadores mudam. Repita até vir a aura que você quer. O mesmo vale para a Quadrilla no Troubled Camp do Jungle Ruins (mas ela não rola Haste).",
      "In Infested Barrens (Act 3), next to the Troubled Camp, 2 rare beasts always spawn: a Diretusk Boar and an Antlion. Check the mods WITHOUT killing. Don't like them? Esc → Respawn at Checkpoint: the modifiers change. Repeat until you get the aura you want. Same for the Quadrilla at the Jungle Ruins Troubled Camp (but it can't roll Haste).")),
    (("Matei o beast sem querer", "I killed the beast by accident"),
     ("Depois de morto ele não volta pelo checkpoint. Vá para a cidade, abra o Waypoint e dê Ctrl + clique na área: abre o Instance Manager para criar uma instância NOVA. Aí é só achar o Troubled Camp de novo.",
      "Once dead it won't come back via checkpoint. Go to town, open the Waypoint and Ctrl + click the area: the Instance Manager opens so you can create a NEW instance. Then find the Troubled Camp again.")),
    (("Beasts de Essence: instância nova", "Essence beasts: new instance"),
     ("Os beasts baratos (21–26%) vêm de encontros de Essence, que aparecem aleatoriamente na área. Se a área não tiver a Essence certa, crie uma instância nova (Ctrl + clique no Waypoint) e procure de novo. No Whakapanu Island, as Essences de crab ficam na praia logo no início do mapa, então cada tentativa é rápida.",
      "The cheap beasts (21–26%) come from Essence encounters that spawn randomly in the area. If the area doesn't have the right Essence, create a new instance (Ctrl + click the Waypoint) and look again. On Whakapanu Island the crab Essences are on the beach right at the start of the map, so each attempt is quick.")),
    (("Custo menor vindo de Essence", "Lower cost from Essence"),
     ("Segundo o Mattjestic, beasts que saem de Essence custam menos Spirit que a versão rara comum (ex.: Rasp Scavenger 26,7% de Essence contra 32,7% raro; crabs 24,9%, às vezes 26%).",
      "Per Mattjestic, beasts from Essences cost less Spirit than the normal rare version (e.g. Rasp Scavenger 26.7% from Essence vs 32.7% as a rare; crabs 24.9%, sometimes 26%).")),
    (("Haste Aura NÃO é Hasted", "Haste Aura is NOT Hasted"),
     ("Haste Aura dá aos aliados na Presence 20% increased Attack e Cast Speed e 10% de Movement Speed. 'Hasted' só deixa o próprio beast mais rápido — útil, mas não é o que você procura.",
      "Haste Aura gives allies in your Presence 20% increased Attack and Cast Speed and 10% Movement Speed. 'Hasted' only makes the beast itself faster — useful, but not what you're looking for.")),
    (("Mantenha o beast de aura perto", "Keep the aura beast close"),
     ("A aura só pega em quem está na Presence do beast. O Antlion costuma rolar para longe; Boar e crabs ficam mais perto. O mod 'Hasted' ajuda o companion a te acompanhar.",
      "The aura only affects whoever is in the beast's Presence. The Antlion tends to roll away; Boar and crabs stay closer. The 'Hasted' mod helps a companion keep up with you.")),
    (("Voltar para a campanha estando no Atlas", "Going back to the campaign from the Atlas"),
     ("As áreas da campanha continuam acessíveis pelos Waypoints de cada ato. Os beasts de lá custam o mesmo % de Spirit e são mais fáceis de capturar porque o nível da área é baixo.",
      "Campaign areas are still reachable through each act's Waypoints. Beasts there cost the same Spirit % and are easier to capture because the area level is low.")),
]

ROUTE = [
    (("1. Haste — Ato 4, Whakapanu Island", "1. Haste — Act 4, Whakapanu Island"),
     ("Procure as Essences de crabs raros na praia do início. Alvo: Quill Crab ou Coconut Crab (24,9–26%). Guarde qualquer crab com Haste Aura e também outras auras T1 boas para combinar. É sorte: repita com instâncias novas.",
      "Look for rare crab Essences on the starting beach. Target: Quill Crab or Coconut Crab (24.9–26%). Keep any crab with Haste Aura and also other good T1 auras to combine. It's luck: repeat with new instances.")),
    (("2. Auras T1 baratas — Ato 5, Ashen Forest", "2. Cheap T1 auras — Act 5, Ashen Forest"),
     ("Swarming Wisp (21%, Essence). Guarde QUALQUER aura T1 menos Haste (ele não rola Haste). Fique de olho no Sabre Spider (28%).",
      "Swarming Wisp (21%, Essence). Keep ANY T1 aura except Haste (it can't roll Haste). Watch out for the Sabre Spider (28%) too.")),
    (("3. Mais auras — Ato 2, Vastiri Outskirts", "3. More auras — Act 2, Vastiri Outskirts"),
     ("Crag Leaper (23,1%, Essence). Opcional: Hyena Demon (30%). Nenhum dos dois rola Haste.",
      "Crag Leaper (23.1%, Essence). Optional: Hyena Demon (30%). Neither rolls Haste.")),
    (("4. Combine", "4. Combine"),
     ("Junte auras T1 DIFERENTES. Se tiver duplicadas, fique com as dos passos 2 e 3 e volte a farmar crabs para trocar a aura repetida (crabs são onde é mais fácil achar todas as auras T1).",
      "Collect DIFFERENT T1 auras. If you have duplicates, keep the ones from steps 2 and 3 and farm crabs again to replace the repeated aura (crabs are the easiest place to find every T1 aura).")),
    (("5. Se ainda faltar", "5. If you're still short"),
     ("Rasp Scavenger (26,7%) no Khari Crossing (Ato 5), via Essence.", "Rasp Scavenger (26.7%) at Khari Crossing (Act 5), via Essence.")),
]

MODS = [
    ("primary", ("Haste Aura", "Haste Aura"), ("Aliados na Presence: 20% increased Attack e Cast Speed, 10% Movement Speed. A melhor para dano.", "Allies in Presence: 20% increased Attack and Cast Speed, 10% Movement Speed. The best for damage.")),
    ("primary", ("Physical Damage Aura", "Physical Damage Aura"), ("Aliados na Presence: 20% increased Physical Damage. Ótima para o macaco (dano físico).", "Allies in Presence: 20% increased Physical Damage. Great for the monkey (physical damage).")),
    ("primary", ("Energy Shield Aura", "Energy Shield Aura"), ("Aliados na Presence ganham 12% da vida máxima como Energy Shield extra.", "Allies in Presence gain 12% of maximum Life as extra Energy Shield.")),
    ("primary", ("Invulnerability Aura", "Invulnerability Aura"), ("Ciclo que deixa aliados invulneráveis por alguns segundos (valor aproximado: 5 s a cada 10 s).", "Cycle that makes allies invulnerable for a few seconds (approximate: 5 s every 10 s).")),
    ("primary", ("Temporal Bubble", "Temporal Bubble"), ("Bolha em volta do beast que reduz a Action Speed de inimigos dentro dela.", "Bubble around the beast that reduces enemy Action Speed inside it.")),
    ("primary", ("Elemental Aura", "Elemental Aura"), ("Aliados na Presence: +20% em todas as resistências elementais.", "Allies in Presence: +20% to all Elemental Resistances.")),
    ("secondary", ("Hasted", "Hasted"), ("O próprio beast fica mais rápido e acompanha você.", "The beast itself gets faster and keeps up with you.")),
    ("secondary", ("Heals Allies", "Heals Allies"), ("Cura aliados na Presence e reduz a recuperação de vida dos inimigos.", "Heals allies in Presence and reduces enemy life recovery.")),
    ("secondary", ("All Damage Shocks / Ignites / Chills / Bleeds / Poisons", "All Damage Shocks / Ignites / Chills / Bleeds / Poisons"), ("Os ataques do companion aplicam a ailment (não os seus).", "The companion's attacks apply the ailment (not yours).")),
    ("secondary", ("Periodically Unleashes Fire / Cold / Lightning", "Periodically Unleashes Fire / Cold / Lightning"), ("Explosão elemental a cada poucos segundos.", "Elemental explosion every few seconds.")),
    ("tertiary", ("Detonates Corpses · Elemental Resistance · Proximal Tangibility · Magma Barrier", "Detonates Corpses · Elemental Resistance · Proximal Tangibility · Magma Barrier"), ("Bons de bônus, mas não valem a captura sozinhos.", "Nice bonuses, but not worth capturing on their own.")),
]

ATLAS = [
    (("Zekoa, the Headcrusher (Silverfist do Atlas)", "Zekoa, the Headcrusher (Atlas Silverfist)"),
     ("É o boss dos mapas Riverside e Rupture. Use tablets com 'Unique Monsters have 1 additional Rare Modifier' + Cruel Hegemony para ele vir com mais modificadores. Prioridade: Extra Crits > Hasted > Extra Damage as Chaos/Physical > Soul Eater. Precisa da The Natural Order para capturar.",
      "It's the boss of Riverside and Rupture maps. Use tablets with 'Unique Monsters have 1 additional Rare Modifier' + Cruel Hegemony so it comes with more modifiers. Priority: Extra Crits > Hasted > Extra Damage as Chaos/Physical > Soul Eater. Needs The Natural Order to capture.")),
    (("Flesh Larva (23,1%) nos mapas", "Flesh Larva (23.1%) in maps"),
     ("Aparece em encontros de Essence aleatórios durante o mapping. Se vier com aura T1 boa, é um dos beasts mais baratos do jogo.",
      "Shows up in random Essence encounters while mapping. If it has a good T1 aura, it's one of the cheapest beasts in the game.")),
    (("Mods de Abyss: Undying Will", "Abyss mods: Undying Will"),
     ("Monstros com mods de Abyss têm versões mais fortes dos modificadores normais. 'Undying Will' é a versão Abyss da Periodic Invulnerability: aliados na aura verde ficam invulneráveis. O Mattjestic usa um companion com Undying Will no setup de endgame de 27 companions. Outros mods Abyss (Shade Walker, Amanamu's Void, Meteoric Demise…) são perigosos de enfrentar.",
      "Monsters with Abyss mods have stronger versions of normal modifiers. 'Undying Will' is the Abyss version of Periodic Invulnerability: allies in the green aura become invulnerable. Mattjestic uses a companion with Undying Will in his 27-companion endgame setup. Other Abyss mods (Shade Walker, Amanamu's Void, Meteoric Demise…) are dangerous to fight.")),
    (("Frozen Mandibles (formigas)", "Frozen Mandibles (ants)"),
     ("Um guia antigo ensinava a farmar essas formigas no Ashen Forest, mas jogadores relatam que elas NÃO podem mais ser capturadas. Não perca tempo.",
      "An older guide taught farming these ants in Ashen Forest, but players report they can NO longer be tamed. Don't waste time.")),
]

EN_PAIRS = {}
def P(v):
    if isinstance(v, tuple) and len(v) == 2 and all(isinstance(x, str) for x in v):
        EN_PAIRS[v[0]] = v[1]; return v[0]
    return v

HUNT = {
    "steps": [P(s) for s in STEPS_CAPTURE],
    "tricks": [{"t": P(t), "d": P(d)} for t, d in TRICKS],
    "route": [{"t": P(t), "d": P(d)} for t, d in ROUTE],
    "mods": [{"tier": k, "n": P(n), "d": P(d)} for k, n, d in MODS],
    "atlas": [{"t": P(t), "d": P(d)} for t, d in ATLAS],
    "beasts": [{"n": n, "cost": c, "where": P(w), "how": P(h), "haste": hs, "note": P(nt) if nt else ""} for n, c, w, h, hs, nt in BEASTS],
    "sources": [{"name": n, "url": u} for n, u in SOURCES],
}
