# -*- coding: utf-8 -*-
"""Forbidden Rites challenges (PoE2 0.5.5) — bilingual data.

Sources
- Challenge list, counts and sub-objectives: PoE2DB "Forbidden_Rites_challenges" (game data).
- League mechanics and reward thresholds: official 0.5.5 patch notes (pathofexile.com/forum/view-thread/4000864).
- Endgame Ritual rewards = Uniques or Omens; crafted/catalyst notes: official 0.5.0 patch notes (view-thread/3932540).
- Rite bosses/areas/rewards, rare monster locations, trial requirements, Atlas regions, Ritual nodes: Game8 (618597, 618598).
- Omen texts: PoE2DB Omen page. Prices: poe.ninja exchange, league Forbidden Rites, fetched 2026-09-16.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DL = os.path.join(HERE, "..", "dl")
REVIEWED = "2026-09-16"


def L(pt, en):
    return {"pt": pt, "en": en}


# ---------------------------------------------------------------- prices
def _prices():
    out = {}
    for t in ("Currency", "Ritual", "Essences"):
        p = os.path.join(DL, "ex_%s.json" % t)
        if not os.path.exists(p):
            continue
        d = json.load(open(p, encoding="utf-8"))
        names = {i["id"]: i["name"] for i in d.get("items", []) + d.get("core", {}).get("items", [])}
        for l in d.get("lines", []):
            if l["id"] in names:
                out[names[l["id"]]] = l["primaryValue"]
    return out


PRICE = _prices()

# ---------------------------------------------------------------- rewards
REWARDS = [
    dict(n=2, img="mtx-footprints", name="Locust Footprints Effect", d=L("Pegadas de gafanhotos em qualquer bota equipada.", "Locust footprints on any equipped boots.")),
    dict(n=4, img="mtx-finisher", name="Locust Swarm Rare Finisher Effect", d=L("Enxame de gafanhotos amplifica a morte de monstros Rare que você mata.", "A locust swarm amplifies the deaths of Rare monsters you kill.")),
    dict(n=6, img="mtx-pet", name="Wildwood Guardian Pet", d=L("Pet que avisa quando há um inimigo unique por perto.", "A pet that alerts you when a unique enemy is nearby.")),
    dict(n=8, img="mtx-levelup", name="Wildwood Affliction Level-up Effect", d=L("Efeito do Wildwood ao subir de nível.", "A Wildwood affliction effect when you level up.")),
]

# ---------------------------------------------------------------- 1. Riteseeker
RITES = [
    dict(id="r1", act=L("Ato 1", "Act 1"), name="Grim Portents", bosses=[
        ("Beira of the Rotten Pack", "Clearfell", "Orb of Transmutation"),
        ("The Devourer", "Mud Burrow", "Orb of Augmentation"),
        ("The Brambleghast", "The Grelwood", "Orb of Transmutation"),
        ("The Rotten Druid", "The Grim Tangle", L("Uncut Skill Gem (nível 3)", "Uncut Skill Gem (level 3)"))]),
    dict(id="r2", act=L("Ato 1", "Act 1"), name="Grave Tidings", bosses=[
        ("Lachlann of Endless Lament", "Cemetery of the Eternals", "Regal Orb"),
        ("Draven, the Eternal Praetor", "Mausoleum of the Praetor", "Lesser Rune"),
        ("Asinia, Praetor Consort", "Tomb of the Consort", "Lapis Amulet"),
        ("The Executioner", "Ogham Village", "Artificer's Orb")]),
    dict(id="r3", act=L("Ato 2", "Act 2"), name="Desert Omens", bosses=[
        ("Rathbreaker", "Vastiri Outskirts", "Exalted Orb"),
        ("Rudja, Dread Engineer", "Mawdun Mine", L("Uncut Support Gem (nível 2)", "Uncut Support Gem (level 2)")),
        ("Balbala, The Traitor", "Traitor's Passage", "Artificer's Orb"),
        ("Jamanra, the Risen King", "The Halani Gates", "Exalted Orb")]),
    dict(id="r4", act=L("Ato 2", "Act 2"), name="Ash and Bone", bosses=[
        ("Azarian, the Forsaken Son", "Buried Shrines", "Lesser Jeweller's Orb"),
        ("Ekbab, Ancient Steed", "The Bone Pits", "Exalted Orb"),
        ("Zalmarath, the Colossus", "The Titan Grotto", "Chance Shard"),
        ("Tor Gul, the Defiler", "The Spires of Deshar", "Gemcutter's Prism")]),
    dict(id="r5", act=L("Ato 3", "Act 3"), name="Savage Wilds", bosses=[
        ("Rootdredge", "Sandswept Marsh", L("Uncut Support Gem (nível 3)", "Uncut Support Gem (level 3)")),
        ("Mighty Silverfist", "Jungle Ruins", "Orb of Alchemy"),
        ("Xyclucian, the Chimera", "Chimeral Wetlands", "Chance Shard"),
        ("Blackjaw, the Remnant", "Jiquani's Machinarium", "Artificer's Orb")]),
    dict(id="r6", act=L("Ato 3", "Act 3"), name="Blood Offerings", bosses=[
        ("Zicoatl, Warden of the Core", "Jiquani's Sanctum", "Exalted Orb"),
        ("Ignagduk, the Bog Witch", "The Azak Bog", "Desert Rune"),
        ("Queen of Filth", "Apex of Filth", "Vaal Orb"),
        ("Ketzuli, High Priest of the Sun", "Temple of Kopec", L("Uncut Spirit Gem (nível 11)", "Uncut Spirit Gem (level 11)"))]),
    dict(id="r7", act=L("Ato 4", "Act 4"), name="Blood in the Water", bosses=[
        ("Scourge of the Skies", "Shrike Island", L("Uncut Support Gem (nível 4)", "Uncut Support Gem (level 4)")),
        ("The Blind Beast", "Isle of Kin", "Gemcutter's Prism"),
        ("Krutog, Lord of Kin", "Volcanic Warrens", L("Uncut Support Gem (nível 4)", "Uncut Support Gem (level 4)")),
        ("Captain Hartlin", "Journey's End", "Orb of Alchemy")]),
    dict(id="r8", act=L("Ato 4", "Act 4"), name="Tidal Omens", bosses=[
        ("The Great White One", "Whakapanu Island", L("Uncut Support Gem (nível 4)", "Uncut Support Gem (level 4)")),
        ("Diamora, Song of Death", "Singing Caverns", L("Charm aleatório", "Random Charm")),
        ("Yama the White", "Halls of the Dead", L("Rune básica aleatória", "Random basic Rune")),
        ("The Prisoner", "Solitary Confinement", L("Rune básica aleatória", "Random basic Rune"))]),
    dict(id="r9", act="Interlude 1", name="Shadow Over Ogham", bosses=[
        ("Isolde and Heldra", "Scorched Farmlands", "Artificer's Orb"),
        ("Sigbert and Godwin", "Holten", L("Rune básica aleatória", "Random basic Rune")),
        ("Oswin, the Dread Warden", "Wolvenhold", "Greater Orb of Augmentation")]),
    dict(id="r10", act="Interlude 2", name="Sands of Ruin", bosses=[
        ("Akthi and Anundr", "The Khari Crossing", "Gemcutter's Prism"),
        ("Elzarah, the Cobra Lord", "Sel Khari Sanctuary", "Orb of Chance"),
        ("Vornas, the Fell Flame", "The Galai Gates", "Greater Orb of Augmentation")]),
    dict(id="r11", act="Interlude 3", name="Death in the Ranges", bosses=[
        ("Lythara, the Wayward Spear", "Kriar Village / Glacial Tarn / Howling Caves", L("Greater Rune básica aleatória", "Random basic Greater Rune")),
        ("Rakkar, the Frozen Talon", "Kriar Village / Glacial Tarn / Howling Caves", "Greater Orb of Augmentation"),
        ("The Abominable Yeti", "Kriar Village / Glacial Tarn / Howling Caves", "Chaos Orb")]),
]

# ---------------------------------------------------------------- 2. Hunter
RARES = [
    ("Areagne, Forgotten Witch", L("Ato 1", "Act 1"), "The Grelwood", "Witch Hut"),
    ("Vargir, the Feral Mutt", L("Ato 1", "Act 1"), "Ogham Farmlands", "Crop Circle"),
    ("The Ninth Treasure of Keth", L("Ato 2", "Act 2"), "The Lost City", "The Galleria"),
    ("Ranbu the Pale Shaman", L("Ato 3", "Act 3"), "Sandswept Marsh", "Orok Campsite"),
    ("The Brood Queen", L("Ato 3", "Act 3"), "Infested Barrens", "Larva Hollow"),
    ("The Noxious Behemoth", L("Ato 3", "Act 3"), "Chimeral Wetlands", "Toxic Bloom"),
    ("Narag of the Vile Word", L("Ato 3", "Act 3"), "Matlan Waterways", "Narag's Hut"),
    ("Magmanore, the Molten", L("Ato 4", "Act 4"), "Volcanic Warrens", "Magma Twins"),
    ("Clawcrunch", L("Ato 4", "Act 4"), "Whakapanu Island", "Dread Crab"),
    ("Fallen Quartermaster", L("Ato 4", "Act 4"), "Abandoned Prison", "The Armoury"),
    ("Adelina, Guardian of the Pearl", L("Ato 4", "Act 4"), "Singing Caverns", "Beckoning Clam"),
    ("Forael, the Soulkeeper", L("Ato 4", "Act 4"), "Abandoned Prison", "Goddess of Justice"),
    ("Harano, the Meat Carver", L("Ato 4", "Act 4"), "Ngakanu", L("depois da quest principal de Arastas", "after the Arastas main quest")),
    ("Mimbok, the Enslaved", L("Ato 4", "Act 4"), "Isle of Kin", "Beast Pen"),
    ("Moltenmettle", "Interlude 2", "The Khari Crossing", "Skullmaw Stairway"),
    ("Bloodgulp", "Interlude 2", "The Khari Crossing", "Torbik"),
    ("Fleshpierce", "Interlude 2", "The Khari Crossing", "—"),
    ("Bloodbilge", "Interlude 3", "Qimah Reservoir", "—"),
    ("Ashen Arachnid", "Interlude 3", "Ashen Forest", "—"),
    ("Frozen Mandibles", "Interlude 3", "Ashen Forest", "—"),
]

# ---------------------------------------------------------------- 3. Ascendant
TRIALS = [
    dict(id="t1", name=L("Primeira prova", "First Trial"), pts=2, img="trial-sekhemas",
         how=L("Complete o Trial of the Sekhemas no Ato 2.", "Complete the Trial of the Sekhemas in Act 2.")),
    dict(id="t2", name=L("Segunda prova", "Second Trial"), pts=2, img="trial-chaos",
         how=L("Complete o Trial of Chaos no Ato 3.", "Complete the Trial of Chaos in Act 3.")),
    dict(id="t3", name=L("Terceira prova", "Third Trial"), pts=2, img="djinn-barya",
         how=L("Trial of the Sekhemas nível 60+ com pelo menos 3 andares (Djinn Barya) OU Trial of Chaos nível 65+ com pelo menos 10 provas (Inscribed Ultimatum).",
               "A level 60+ Trial of the Sekhemas with at least 3 floors (Djinn Barya) OR a level 65+ Trial of Chaos with at least 10 trials (Inscribed Ultimatum).")),
    dict(id="t4", name=L("Prova final", "Final Trial"), pts=2, img="inscribed-ultimatum",
         how=L("Trial of the Sekhemas nível 75+ com pelo menos 4 andares OU Trial of Chaos nível 75+ com pelo menos 10 provas.",
               "A level 75+ Trial of the Sekhemas with at least 4 floors OR a level 75+ Trial of Chaos with at least 10 trials.")),
]
CHAOS_055 = [
    L("Agora dá para sair do Trial of Chaos no meio e continuar depois da mesma sala.", "You can now leave the Trial of Chaos at any point and resume later from the same room."),
    L("Cada sala tem um baú de recompensa no final: morrer não faz perder tudo.", "Every room has a reward chest at the end: dying no longer loses everything."),
    L("Os modificadores de dificuldade agora mostram os valores reais e ficaram bem mais leves.", "Difficulty modifiers now show real values and apply much less difficulty."),
    L("Nas provas 'Survive', matar os Rares reduz o tempo necessário.", "In 'Survive' encounters, killing Rares reduces the required time."),
    L("O Trialmaster só para o tempo no começo da run, não em toda sala.", "The Trialmaster only stops time at the very start of the run, not every room."),
]

# ---------------------------------------------------------------- 6. Nameless (omens)
# trigger cost: extra currency consumed to make the omen fire
OMENS = [
    ("Omen of Gambling", "OmenGambleNoGoldCost", L("Fazer uma compra na aba Gamble de um vendedor.", "Make a Gamble purchase at a vendor."), None, "safe"),
    ("Omen of Bartering", "OmenSellVendorRandomise", L("Vender um item a um vendedor.", "Sell an item to a vendor."), None, "safe"),
    ("Omen of Greater Exaltation", "VoodooOmens1Yellow", L("Usar um Exalted Orb em um item Rare (adiciona 2 mods).", "Use an Exalted Orb on a Rare item (adds 2 modifiers)."), "Exalted Orb", "safe"),
    ("Omen of Refreshment", "VoodooOmens1Blue", L("Chegar a Low Life com ele ativo (recupera cargas de flasks e charms).", "Reach Low Life while it is active (refills flask and charm charges)."), None, "risk"),
    ("Omen of Amelioration", "VoodooOmens3Blue", L("Morrer com ele ativo (evita 75% da perda de experiência).", "Die while it is active (prevents 75% of experience loss)."), None, "death"),
    ("Omen of Resurgence", "VoodooOmens2Blue", L("Chegar a Low Life com ele ativo (recupera vida, mana e ES).", "Reach Low Life while it is active (recovers life, mana and ES)."), None, "risk"),
    ("Omen of Sinistral Exaltation", "VoodooOmens2Yellow", L("Usar um Exalted Orb em um Rare (só prefixo).", "Use an Exalted Orb on a Rare (prefix only)."), "Exalted Orb", "safe"),
    ("Omen of Dextral Exaltation", "VoodooOmens3Yellow", L("Usar um Exalted Orb em um Rare (só sufixo).", "Use an Exalted Orb on a Rare (suffix only)."), "Exalted Orb", "safe"),
    ("Omen of Sinistral Erasure", "VoodooOmens2Dark", L("Usar um Chaos Orb em um Rare (remove só prefixo).", "Use a Chaos Orb on a Rare (removes a prefix only)."), "Chaos Orb", "safe"),
    ("Omen of Dextral Erasure", "VoodooOmens3Dark", L("Usar um Chaos Orb em um Rare (remove só sufixo).", "Use a Chaos Orb on a Rare (removes a suffix only)."), "Chaos Orb", "safe"),
    ("Omen of Sinistral Annulment", "VoodooOmens2Purple", L("Usar um Orb of Annulment (remove só prefixo).", "Use an Orb of Annulment (removes a prefix only)."), "Orb of Annulment", "safe"),
    ("Omen of Dextral Annulment", "VoodooOmens3Purple", L("Usar um Orb of Annulment (remove só sufixo).", "Use an Orb of Annulment (removes a suffix only)."), "Orb of Annulment", "safe"),
    ("Omen of Sinistral Crystallisation", "OmenOnPerfectEssencePrefix", L("Usar uma Perfect ou Corrupted Essence em um Rare (remove só prefixo).", "Use a Perfect or Corrupted Essence on a Rare (removes a prefix only)."), "Perfect Essence of the Body", "safe"),
    ("Omen of Dextral Crystallisation", "OmenOnPerfectEssenceSuffix", L("Usar uma Perfect ou Corrupted Essence em um Rare (remove só sufixo).", "Use a Perfect or Corrupted Essence on a Rare (removes a suffix only)."), "Perfect Essence of the Body", "safe"),
    ("Omen of the Ancients", "OmenOnChanceAncientOrb", L("Usar um Orb of Chance em item Normal: vira um unique aleatório da mesma classe.", "Use an Orb of Chance on a Normal item: it becomes a random unique of the same class."), "Orb of Chance", "safe"),
    ("Omen of Whittling", "VoodooOmens1Dark", L("Usar um Chaos Orb (remove o mod de menor nível).", "Use a Chaos Orb (removes the lowest-level modifier)."), "Chaos Orb", "safe"),
    ("Omen of Catalysing Exaltation", "OmenOnExaltConsumeQuality", L("Usar um Exalted Orb em anel/amuleto com qualidade de Catalyst.", "Use an Exalted Orb on a ring/amulet with Catalyst quality."), "Exalted Orb", "safe"),
    ("Omen of the Blessed", "OmenOnDivineRerollImplicits", L("Usar um Divine Orb (rerrola só os implícitos).", "Use a Divine Orb (rerolls implicits only)."), "Divine Orb", "safe"),
    ("Omen of Sanctification", "OmenOnDivineSanctify", L("Usar um Divine Orb em um Rare (o item fica Sanctified).", "Use a Divine Orb on a Rare (the item becomes Sanctified)."), "Divine Orb", "safe"),
    ("Omen of Chance", "OmenOnChanceNotDestroy", L("Usar um Orb of Chance (o item não é destruído).", "Use an Orb of Chance (the item is not destroyed)."), "Orb of Chance", "safe"),
    ("Omen of Answered Prayers", "VoodooOmens4Blue", L("Clicar em um Shrine (efeito extra).", "Click a Shrine (extra effect)."), None, "safe"),
    ("Omen of Secret Compartments", "VoodooOmens4Dark", L("Abrir um Strongbox (ele pode ser reaberto).", "Open a Strongbox (it becomes reopenable)."), None, "safe"),
    ("Omen of the Hunt", "VoodooOmens4Green", L("Matar um monstro Possessed (libera todos os Azmeri Spirits).", "Kill a Possessed monster (releases all Azmeri Spirits)."), None, "safe"),
    ("Omen of Reinforcements", "VoodooOmens4Purple", L("Encontrar um Rogue Exile (ele invoca um aliado).", "Encounter a Rogue Exile (it summons an ally)."), None, "safe"),
]

# ---------------------------------------------------------------- 7. Cartographer
TREES = [
    dict(id="ritual", name="Ritual", max=36, img="atlas-ritual", where=L("Caer Tarth — bem a oeste do início do Atlas, depois do The Withered Willow.", "Caer Tarth — far west of your Atlas start, past The Withered Willow.")),
    dict(id="delirium", name="Delirium", max=31, img="atlas-delirium", where=L("The Withered Willow — perto, a oeste do início do Atlas.", "The Withered Willow — near west of your Atlas start.")),
    dict(id="abyss", name="Abyss", max=35, img="atlas-abyss", where=L("Well of Souls — perto, a leste do início do Atlas.", "Well of Souls — near east of your Atlas start.")),
]

# ---------------------------------------------------------------- 8. Vanquisher
BOSSES = [
    dict(id="xesht", name="Xesht, We That Are One", mech="Breach", img="atlas-breach", key="breachstone", drop="xesht-drop",
         steps=[L("Jogue Breaches nos mapas e junte Breach Splinters.", "Run Breaches in maps and collect Breach Splinters."),
                L("Com a pilha completa, os splinters viram um Wombgift especial.", "A full stack of splinters turns into a special Wombgift."),
                L("Leve o Wombgift à Genesis Tree (Monastery of the Keepers) para criar um Breachstone.", "Hand the Wombgift in at the Genesis Tree (Monastery of the Keepers) to create a Breachstone."),
                L("Use o Breachstone e siga a linha de quests do Breach até o confronto com o Xesht.", "Use the Breachstone and follow the Breach questline to the Xesht encounter.")],
         tip=L("Arena que encolhe e golpes de tentáculo pesados: dano consistente e mobilidade. Drop marcante: Hand of Wisdom and Action.", "Shrinking arena and heavy tentacle slams: bring steady damage and mobility. Notable drop: Hand of Wisdom and Action.")),
    dict(id="atziri", name="Atziri, the Red Queen", mech="Vaal Temple", img="atziri-core", key="atziri-core", drop="atziri-drop",
         steps=[L("Vá a Lira Vaal, a nordeste do início do Atlas.", "Travel to Lira Vaal, north-east of your Atlas start."),
                L("Construa o Temple of Atziri colocando salas e avance pelo templo.", "Build the Temple of Atziri by placing rooms and push through the temple."),
                L("Derrote o Royal Architect e abra o acesso à câmara real.", "Defeat the Royal Architect and open access to the royal chamber."),
                L("Enfrente Atziri na câmara final.", "Fight Atziri in the final chamber.")],
         tip=L("É a fonte das Orbs of Sacrifice (Yaomac's, Kopec's, Kamasa's, Yugul's).", "It is the source of the Orbs of Sacrifice (Yaomac's, Kopec's, Kamasa's, Yugul's).")),
    dict(id="aberration", name="The Aberration", mech="Expedition", img="atlas-expedition", key="triskelion", drop="aberration-drop",
         steps=[L("Faça a quest The Starlit Rite: fale com Farrow do lado de fora das Lost Catacombs.", "Complete The Starlit Rite: talk to Farrow outside the Lost Catacombs."),
                L("Use Expedition Logbooks de nível 79+ e derrote Uhtred.", "Run level 79+ Expedition Logbooks and defeat Uhtred."),
                L("Rode o Logbook de Olroth, mate Olroth e pegue o Shattered Triskelion.", "Run Olroth's Logbook, kill Olroth and take the Shattered Triskelion."),
                L("Reforje na Verisium Anvil (The Triskelion Reforged) e abra a Verisium Crater.", "Reforge it at the Verisium Anvil (The Triskelion Reforged) and open the Verisium Crater.")],
         tip=L("Duas fases: aos 75% de vida ela se cura e ganha mobilidade; lasers que seguem você. Dropa Starlit Ore (vira uniques no Runeforging).", "Two phases: at 75% life it heals and gains mobility; tracking lasers. Drops Starlit Ore (runeforged into uniques).")),
]

# ---------------------------------------------------------------- league mechanics
MECHANICS = [
    dict(img="tile-campaign", t=L("Rituais em toda a campanha", "Rituals across the campaign"),
         d=L("Cada área da campanha tem um Ritual que dá currency de crafting e equipamento para o leveling. Duas vezes por ato (e uma por Interlude) aparecem clusters de Ritual Effigies no mapa-múndi: a efígie fica em cima do chefe da área. O chefe derrotado é levado para o próximo Ritual do cluster, somando ondas de chefes cada vez mais perigosas. No fim da série você gasta Tribute em Uniques.",
             "Every campaign area has a Ritual that gives crafting currency and levelling gear. Twice per act (once per Interlude) clusters of Ritual Effigies appear on the World Map: the effigy sits on the area boss. A defeated boss is carried into the next Ritual of the cluster, stacking ever more dangerous boss waves. At the end of the series you spend Tribute on Uniques.")),
    dict(img="tile-wildwood", t=L("Sacred Bloom e Viridian Wildwood", "Sacred Bloom and the Viridian Wildwood"),
         d=L("Sacred Blooms saem como recompensa de Ritual (só nesta liga) e adicionam o Viridian Wildwood a um grupo de mapas. Lá dentro você segue trilhas de Wisps e coleta; ao sair, os monstros do mapa ficam mais fortes e mais recompensadores conforme os Wisps coletados. Usar mais de um Ritual Tablet aumenta os Azmeri Wisps coletados.",
             "Sacred Blooms drop as Ritual rewards (this league only) and add the Viridian Wildwood to a cluster of maps. Inside you follow and collect Wisp trails; when you leave, map monsters become stronger and more rewarding based on the Wisps collected. Using more than one Ritual Tablet increases Azmeri Wisps collected.")),
    dict(img="tile-cores", t=L("Novas Soul Cores", "New Soul Cores"),
         d=L("Jiquani's Soul Cores dão +1 nível a um tipo de skill na arma (Totem, Curse, Mark, Warcry, Herald, Strike, Nova, Slam, Grenade, Hazard, Plant, Wind, Storm). Atziri's Soul Cores escalam com itens corrompidos equipados.",
             "Jiquani's Soul Cores grant +1 level to a skill type on weapons (Totem, Curse, Mark, Warcry, Herald, Strike, Nova, Slam, Grenade, Hazard, Plant, Wind, Storm). Atziri's Soul Cores scale with equipped corrupted items.")),
    dict(img="tile-chaos", t=L("Trial of Chaos refeito", "Trial of Chaos rework"),
         d=L("Dá para sair e voltar, cada sala tem baú, modificadores mais leves e explícitos, e as recompensas finais agora são só Currency e Soul Cores.",
             "You can leave and come back, every room has a chest, modifiers are lighter and explicit, and final rewards are now only Currency and Soul Cores.")),
]

SOURCES = [
    ("PoE2DB — Forbidden Rites challenges", "https://poe2db.tw/us/Forbidden_Rites_challenges"),
    ("GGG — 0.5.5 Patch Notes", "https://www.pathofexile.com/forum/view-thread/4000864"),
    ("GGG — 0.5.0 Patch Notes", "https://www.pathofexile.com/forum/view-thread/3932540"),
    ("Game8 — Forbidden Rites Challenges", "https://game8.co/games/Path-of-Exile-2/archives/618598"),
    ("Game8 — Forbidden Rites Walkthrough", "https://game8.co/games/Path-of-Exile-2/archives/618597"),
    ("PoE2DB — Omens", "https://poe2db.tw/us/Omen"),
    ("poe.ninja — Forbidden Rites economy", "https://poe.ninja/poe2/economy"),
]


def resolve(o, lang):
    if isinstance(o, dict):
        if set(o.keys()) == {"pt", "en"}:
            return o[lang]
        return {k: resolve(v, lang) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [resolve(v, lang) for v in o]
    return o


def data(lang):
    trig_price = {n: PRICE.get(n) for n in ("Exalted Orb", "Chaos Orb", "Orb of Annulment", "Divine Orb", "Orb of Chance", "Perfect Essence of the Body")}
    omens = [dict(name=n, img="omen-" + img, how=how, price=PRICE.get(n), trig=trig, trigPrice=trig_price.get(trig) if trig else 0, risk=risk) for n, img, how, trig, risk in OMENS]
    d = dict(reviewed=REVIEWED, rewards=REWARDS, rites=RITES,
             rares=[dict(name=n, act=a, area=ar, poi=p) for n, a, ar, p in RARES],
             trials=TRIALS, chaos055=CHAOS_055, omens=omens, trees=TREES, bosses=BOSSES,
             mechanics=MECHANICS, sources=SOURCES, leagueEnd="2026-12-11T20:00:00Z")
    return resolve(d, lang)
