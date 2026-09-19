# -*- coding: utf-8 -*-
# Opções por slot com nível mínimo, custo e nota de encaixe na build (executado dentro de bdata.py: usa L e common.ECO).
# Nível = requisito da base do item (RePoE); preço = poe.ninja (Divines); mods = poe.ninja. A nota (s) é o meu julgamento de encaixe para Twister + Whirling Slash
# (Armour/Evasion e vida, Spirit, movimento, velocidade e dano do que a build usa) — não é um número do jogo. Barato = Grátis + Barato; Completo = todos.
# Custo: free < 0,05 Div · cheap < 1 · value < 30 · lux (ou item do PoB do autor sem preço).
import common as _c, glob as _g, json as _j, os as _os, re as _re

# nível exigido do unique = o que o poe.ninja mostra no item (levelRequired); o menor entre as variantes (Tense/Runeforged/Runemastered...). 0 vira 1.
_REQ = {}
for _f in _g.glob(_os.path.join(_os.path.dirname(_c.__file__), "..", "dl", "eco_Unique*.json")):
    for _l in _j.load(open(_f, encoding="utf-8"))["lines"]:
        if _l.get("levelRequired") not in (None, ""):
            _REQ.setdefault(_l["name"], set()).add(int(_l["levelRequired"]))
_LV = _re.compile(r"\s*\((?:[^()]*?, )?(?:nível|level) \d+\)|, (?:nível|level) \d+(?=\))")


def O(n, kind, lv, s, why, cost=None, tip=None):
    """n = nome (unique) ou descrição (rare); kind 'u'|'r'; lv = nível mínimo; s = nota de encaixe 0-100; why = (pt, en)."""
    price = None
    if kind == "u":
        e = _c.ECO.get(n) or {}
        price = e.get("price")
        if n in _REQ:
            lv = max(1, min(_REQ[n]))
            why = tuple(_re.sub(r"\s*\((?:([^()]*?), )?(?:nível|level) \d+\)", lambda m: f" ({m.group(1)})" if m.group(1) else "", w) for w in why)     # o nível já aparece no selo
        cost = cost or ("free" if price is not None and price < .05 else "cheap" if price is not None and price < 1 else "value" if price is not None and price < 30 else "lux")
    return dict(n=n, k=kind, lv=lv, c=cost or "free", s=s, p=round(price, 3) if price is not None else None, w=L(*why), tip=tip)


GEAR_OPTS = {
 "spear": [
  O(L("Spear branca do vendor (Hardwood Spear)", "White vendor spear (Hardwood Spear)"), "r", 1, 25, ("Só para o Twister e a Whirling Slash funcionarem: dano baixo. Vale até o nível 15.", "Just so Twister and Whirling Slash work: low damage. Good until level 15.")),
  O(L("Spear rare com dano elemental e velocidade", "Rare spear with elemental damage and speed"), "r", 5, 50, ("Suba a base com o nível: Ironhead (5) → Hunting (10) → Winged (16) → War (21). Procure dano elemental adicionado e velocidade de ataque; a spear também dá a skill Spear Throw.", "Move the base up with your level: Ironhead (5) → Hunting (10) → Winged (16) → War (21). Look for added elemental damage and attack speed; the spear also grants Spear Throw.")),
  O("Skysliver", "u", 16, 82, ("Winged Spear: dano de raio, +15–30% de velocidade de ataque e chance de Shock (alimenta o Herald of Thunder). Sua spear do 16 ao ~40.", "Winged Spear: lightning damage, +15–30% attack speed and Shock chance (feeds Herald of Thunder). Your spear from 16 to ~40.")),
  O(L("Skysliver Runeforged", "Runeforged Skysliver"), "u", 40, 90, ("A mesma Skysliver na base Runeforged: mais slots de runa (Thrud's Might do PoB) (nível 40).", "The same Skysliver on the Runeforged base: more rune slots (the PoB's Thrud's Might) (level 40)."), cost="cheap"),
  O(L("Soaring Spear rare ilvl 82 (Armageddon Edge)", "Rare Soaring Spear ilvl 82 (Armageddon Edge)"), "r", 70, 94, ("A spear do Set 1 do PoB (base nível 70): +36% de velocidade de ataque, dano físico adicionado, Spear Throw e mods de velocidade explícitos.", "The PoB's Set 1 spear (base level 70): +36% attack speed, added physical damage, Spear Throw and explicit-speed mods."), cost="value"),
 ],
 "set2": [
  O(L("Akoyan Spear rare (Mind Edge)", "Rare Akoyan Spear (Mind Edge)"), "r", 78, 90, ("A spear do Set 2 do PoB (base nível 78): dano de raio e fogo adicionados, +4,4% de chance de crítico e Spear Throw.", "The PoB's Set 2 spear (base level 78): added lightning and fire damage, +4.4% crit chance and Spear Throw."), cost="value"),
  O("Sacred Flame", "u", 84, 96, ("O sceptre do Set 2: +Spirit (138 no PoB), Ganha 60% do dano como fogo extra e a skill Purity of Fire. ~5 Divines.", "The Set 2 sceptre: +Spirit (138 in the PoB), gain 60% of damage as extra fire and the Purity of Fire skill. ~5 Divines."), cost="value"),
 ],
 "helmet": [
  O(L("Ancestral Tiara rare ilvl 80+ (Energy Shield)", "Rare Ancestral Tiara ilvl 80+ (Energy Shield)"), "r", 80, 90, ("A base do PoB (Foe Keep, nível 80): Energy Shield, Armour/Evasion/ES aumentados e resistências.", "The PoB's base (Foe Keep, level 80): Energy Shield, increased Armour/Evasion/ES and resistances."), cost="value"),
  O(L("Capacete rare de Força com vida e resistências", "Strength rare helmet with life and resistances"), "r", 1, 55, ("Vida primeiro, depois resistências. Base de Armour (Rusted → Soldier → Elite → Imperial Greathelm).", "Life first, then resistances. Armour base (Rusted → Soldier → Elite → Imperial Greathelm).")),
  O("Ezomyte Peak", "u", 12, 68, ("50–100% de Armour, +50–80 de vida e regeneração (Soldier Greathelm, nível 12).", "50–100% Armour, +50–80 life and regeneration (Soldier Greathelm, level 12).")),
  O("Thrillsteel", "u", 27, 77, ("Onslaught (mais velocidade de ataque e movimento) na base Spired Greathelm (nível 27); é o do autor para o leveling. Runemastered no 40.", "Onslaught (more attack and movement speed) on the Spired Greathelm (level 27); the author's leveling pick. Runemastered at 40.")),
  O("Corona of the Red Sun", "u", 36, 70, ("+60–80 de vida e 20–25% de resistência a fogo (Warrior Greathelm, nível 36).", "+60–80 life and 20–25% fire resistance (Warrior Greathelm, level 36).")),
  O(L("Capacete rare de Armour ilvl 65+ com vida e resistência a frio", "Rare Armour helmet ilvl 65+ with life and cold resistance"), "r", 60, 82, ("Crafte na base do seu nível: vida, Armour e resistências (aba Crafting).", "Craft on a base of your level: life, Armour and resistances (Crafting tab)."), cost="cheap"),
 ],
 "body": [
  O("Enfolding Dawn", "u", 1, 80, ("+100 de Spirit: liga Herald, Banner e Plating assim que você tiver as gems, sem esperar as quests. Base Str/Int (Armour + ES) e 5–15% de resistências.", "+100 Spirit: run Herald, Banner and Plating as soon as you have the gems, without waiting for quests. Str/Int base (Armour + ES) and 5–15% resistances.")),
  O("Coat of Red", "u", 1, 72, ("80–100% de Armour e Evasion e +80–99 de vida em base Str/Dex (Chain Mail): a melhor defesa barata do Ato 1.", "80–100% Armour and Evasion and +80–99 life on a Str/Dex base (Chain Mail): the best cheap defence of Act 1.")),
  O("Tabula Rasa", "u", 1, 62, ("Sem defesa própria, mas com muitos sockets para runas de dano (escolha do autor). Vale quando vida e resistências vêm de outras peças.", "No defences of its own but many sockets for damage runes (the author's pick). Worth it when life and resistances come from other pieces.")),
  O(L("Body rare Str/Dex com vida e resistências", "Str/Dex rare body with life and resistances"), "r", 1, 58, ("Armour e Evasion com vida e resistências; suba a base com o nível: Chain Mail → Vagabond → Explorer → Knight Armour.", "Armour and Evasion with life and resistances; move up the base with your level: Chain Mail → Vagabond → Explorer → Knight Armour.")),
  O("Irongrasp", "u", 16, 74, ("100–146% de Armour e Evasion, +20–29 de Força e Stun Threshold (Vagabond Armour, nível 16).", "100–146% Armour and Evasion, +20–29 Strength and Stun Threshold (Vagabond Armour, level 16).")),
  O("Pariah's Embrace", "u", 26, 84, ("+50 de Spirit, Armour e Evasion e +10–15 em todos os atributos (Cloaked Mail, nível 26).", "+50 Spirit, Armour and Evasion and +10–15 to all attributes (Cloaked Mail, level 26).")),
  O("Belly of the Beast", "u", 33, 82, ("100–148% de Armour e Evasion e +100–149 de vida (Explorer Armour, nível 33).", "100–148% Armour and Evasion and +100–149 life (Explorer Armour, level 33).")),
  O("Soul Mantle", "u", 36, 85, ("+75 de Spirit e Armour + ES (Sacrificial Mantle, nível 36). A base exige 33 de Força e 33 de Inteligência: confira os atributos.", "+75 Spirit and Armour + ES (Sacrificial Mantle, level 36). The base needs 33 Strength and 33 Intelligence: check your attributes.")),
  O("Widow's Reign", "u", 45, 90, ("101–149% de Armour e Evasion, +100–150 de vida e 17–23% de resistência a caos (Knight Armour, nível 45): a melhor defesa barata do meio do jogo.", "101–149% Armour and Evasion, +100–150 life and 17–23% chaos resistance (Knight Armour, level 45): the best cheap defence of the mid game.")),
  O("Lightning Coil", "u", 50, 80, ("80–120% de Armour e Evasion, +80–100 de vida e +Destreza (Ancestral Mail, nível 50).", "80–120% Armour and Evasion, +80–100 life and +Dexterity (Ancestral Mail, level 50).")),
  O("Morior Invictus", "u", 65, 96, ("O do autor: +300–400% de Armour, Evasion e ES e vida, atributos, resistências e regeneração por socket cheio (o mod de Spirit, +10–14 por socket, é um dos que ele pode rolar). ~6 Divines.", "The author's: +300–400% Armour, Evasion and ES and life, attributes, resistances and regeneration per filled socket (the Spirit mod, +10–14 per socket, is one it can roll). ~6 Divines.")),
 ],
 "gloves": [
  O(L("Secured Wraps rare ilvl 80+ com +2 de nível de projétil", "Rare Secured Wraps ilvl 80+ with +2 projectile levels"), "r", 80, 90, ("As luvas do PoB (Phoenix Claw): dano de raio adicionado, +2 de nível de skills de projétil e velocidade de projétil. Evite 'projétil extra'.", "The PoB's gloves (Phoenix Claw): added lightning damage, +2 projectile skill levels and projectile speed. Avoid 'extra projectile'."), cost="value"),
  O(L("Luvas rare de Armour com vida e resistências", "Armour rare gloves with life and resistances"), "r", 1, 55, ("Vida e resistências primeiro. NUNCA aceite 'chance de projétil extra' (o autor diz que está bugada).", "Life and resistances first. NEVER accept 'chance for an extra projectile' (the author says it's bugged).")),
  O("Lochtonial Caress", "u", 16, 77, ("10–15% de velocidade de skill e +40–60 de vida (Tempered Mitts): acelera o Twister e a Whirling Slash.", "10–15% skill speed and +40–60 life (Tempered Mitts, level 16): speeds up Twister and Whirling Slash.")),
  O("Atziri's Acuity", "u", 33, 82, ("150–199% de Armour, +100–149 de vida e leech de vida (Moulded Mitts, nível 33).", "150–199% Armour, +100–149 life and life leech (Moulded Mitts, level 33).")),
  O("Empire's Grasp", "u", 52, 74, ("150–199% de Armour, +20–30 de Força e vida por morte (Titan Mitts, nível 52).", "150–199% Armour, +20–30 Strength and life per kill (Titan Mitts, level 52).")),
  O(L("Luvas rare de Armour ilvl 78+ com vida e dano de frio adicionado", "Rare Armour gloves ilvl 78+ with life and added cold damage"), "r", 60, 84, ("Vida, Armour e dano de frio adicionado a ataques (aba Crafting).", "Life, Armour and added cold damage to attacks (Crafting tab)."), cost="cheap"),
 ],
 "boots": [
  O(L("Daggerfoot Shoes rare ilvl 80+ com movimento", "Rare Daggerfoot Shoes ilvl 80+ with movement"), "r", 80, 90, ("As botas do PoB (Armageddon Pace): movimento, Evasion e ES aumentados e resistências.", "The PoB's boots (Armageddon Pace): movement, increased Evasion and ES and resistances."), cost="value"),
  O(L("Botas rare com movimento e vida", "Rare boots with movement and life"), "r", 1, 58, ("Movimento primeiro (a build gira o tempo todo), depois vida e resistências.", "Movement first (the build spins all the time), then life and resistances.")),
  O("Corpsewade", "u", 11, 60, ("10% de movimento, 30–50% de Armour e Força (Iron Greaves, nível 11).", "10% movement, 30–50% Armour and Strength (Iron Greaves, level 11).")),
  O("Wanderlust", "u", 11, 73, ("20% de movimento e imunidade à lentidão (Wrapped Sandals; a base exige 17 de Inteligência).", "20% movement and immunity to Slow (Wrapped Sandals; the base needs 17 Intelligence).")),
  O("The Infinite Pursuit", "u", 16, 74, ("10% de movimento, 100–150% de Armour e +80–100 de vida (Bronze Greaves, nível 16).", "10% movement, 100–150% Armour and +80–100 life (Bronze Greaves, level 16).")),
  O("Trampletoe", "u", 27, 68, ("15% de movimento e 50–100% de Armour (Trimmed Greaves, nível 27); a base exige mais atributos.", "15% movement and 50–100% Armour (Trimmed Greaves, level 27); it raises attribute requirements.")),
  O("Birth of Fury", "u", 33, 84, ("20% de movimento, +40–60 de vida e 20–30% de resistência a fogo (Stone Greaves, nível 33).", "20% movement, +40–60 life and 20–30% fire resistance (Stone Greaves, level 33).")),
 ],
 "amulet": [
  O(L("Absent Amulet rare: +3 de nível de projétil e Spirit", "Rare Absent Amulet: +3 projectile levels and Spirit"), "r", 50, 92, ("O amuleto do PoB (Gale Gorget): +3 de nível de skills de projétil, +50 de Spirit, qualidade de skills e a Cast on Critical de brinde.", "The PoB's amulet (Gale Gorget): +3 projectile skill levels, +50 Spirit, skill quality and a free Cast on Critical."), cost="value"),
  O(L("Amuleto rare com vida e resistências", "Rare amulet with life and resistances"), "r", 1, 55, ("Vida e resistências que faltarem.", "Whatever life and resistances you're missing.")),
  O("Idol of Uldurn", "u", 1, 66, ("+60–80 de vida e +Destreza (Crimson Amulet): vida por quase nada no Ato 2 e 3.", "+60–80 life and +Dexterity (Crimson Amulet): life for almost nothing in Acts 2 and 3.")),
  O("Ligurium Talisman", "u", 8, 70, ("+25–35 de Spirit e ES (Lapis Amulet): Spirit extra por quase nada.", "+25–35 Spirit and ES (Lapis Amulet): extra Spirit for almost nothing.")),
  O("Beacon of Azis", "u", 30, 74, ("+30 de Spirit e +60–99 de mana (Solar Amulet, nível 30).", "+30 Spirit and +60–99 mana (Solar Amulet, level 30).")),
  O(L("Amuleto rare com Spirit, vida e resistências", "Rare amulet with Spirit, life and resistances"), "r", 30, 80, ("Spirit paga as reservas; procure +Spirit e vida (aba Crafting).", "Spirit pays for the reservations; look for +Spirit and life (Crafting tab)."), cost="cheap"),
 ],
 "rings": [
  O("The Taming", "u", 42, 92, ("Aumenta o dano a cada tipo de ailment elemental no inimigo e deixa as skills de Wind (o Twister!) usarem VÁRIAS superfícies elementais ao mesmo tempo. ~4 Divines.", "Increases damage per type of Elemental Ailment on the enemy and lets Wind skills (Twister!) use MULTIPLE elemental ground surfaces at once. ~4 Divines."), cost="value"),
  O("Blackheart", "u", 1, 70, ("Regeneração de vida, dano de caos adicionado e Armour também aplicada a caos (Iron Ring). O do autor para o leveling: dois por ~0,01 Divine.", "Life regeneration, added chaos damage and Armour also applied to chaos (Iron Ring). The author's leveling pick: two for ~0.01 Divine.")),
  O("Blistering Bond", "u", 8, 58, ("+40–60 de vida e 20–30% de fogo, mas −10–15% de frio (Ruby Ring, nível 8).", "+40–60 life and 20–30% fire, but −10–15% cold (Ruby Ring, level 8).")),
  O("Whisper of the Brotherhood", "u", 12, 66, ("5–10% de velocidade de skill e +Destreza (Sapphire Ring, nível 12).", "5–10% skill speed and +Dexterity (Sapphire Ring, level 12).")),
  O(L("Anéis rare com dano adicionado, vida e resistências", "Rare rings with added damage, life and resistances"), "r", 28, 80, ("O upgrade do guia aos ~30: dano adicionado a ataques, vida e a resistência que faltar.", "The guide's upgrade at ~30: added attack damage, life and whatever resistance is missing."), cost="cheap"),
  O(L("Anéis rare de dano adicionado ilvl 65+", "Rare rings with added damage ilvl 65+"), "r", 48, 86, ("O upgrade dos ~50: dano de frio/fogo/raio adicionado alto, vida e resistências.", "The ~50 upgrade: high added cold/fire/lightning damage, life and resistances."), cost="cheap"),
 ],
 "belt": [
  O("Headhunter", "u", 50, 98, ("O cinto do PoB (luxo, ~246 Divines): os mods dos Rares que você mata.", "The PoB's belt (luxury, ~246 Divines): the mods of the Rares you kill."), cost="lux"),
  O(L("Cinto rare com vida e resistências", "Rare belt with life and resistances"), "r", 1, 55, ("Vida e resistências que faltarem.", "Whatever life and resistances you're missing.")),
  O("Meginord's Girdle", "u", 1, 70, ("+40–50 de Força, +10–15% de resistência a frio e os flasks gastam 50% mais cargas (desvantagem) (Rawhide Belt).", "+40–50 Strength, +10–15% cold resistance and flasks use 50% more charges (a drawback) (Rawhide Belt).")),
  O("Goregirdle", "u", 25, 78, ("+20–30 de Força, 10–20 de regeneração de vida e defende com 200% da Armour (Plate Belt, nível 25).", "+20–30 Strength, 10–20 life regeneration and defends with 200% of Armour (Plate Belt, level 25).")),
  O("Ryslatha's Coil", "u", 31, 76, ("+80–100 de vida, 30–50% de recuperação de flask e 30–40% mais dano físico máximo (Ornate Belt, nível 31).", "+80–100 life, 30–50% flask recovery and 30–40% more maximum physical attack damage (Ornate Belt, level 31).")),
  O("Waistgate", "u", 50, 72, ("+50–80 de vida e de mana e 20–30% de recuperação de flask (Heavy Belt, nível 50).", "+50–80 life and mana and 20–30% flask recovery (Heavy Belt, level 50).")),
  O("Cat O' Nine Tails", "u", 55, 84, ("+120–199 de vida e regeneração ao ser atingido (Utility Belt, nível 55).", "+120–199 life and regeneration when hit (Utility Belt, level 55).")),
  O("Mageblood", "u", 55, 100, ("O cinto do PoB final do autor (luxo, ~570 Divines): efeitos de flask permanentes.", "The belt of the author's final PoB (luxury, ~570 Divines): permanent flask effects.")),
 ],
}
GEAR_OPTS["charms"] = [
  O("Silver Charm", "r", 10, 55, ("Charm mágico (nível 10): recupera vida quando você sofre lentidão. O slot vem da quest do Medallion.", "Magic charm (level 10): recovers life when you're Slowed. The slot comes from the Medallion quest.")),
  O("Dousing Charm", "r", 32, 62, ("Charm mágico (nível 32): dá Guard quando você é incendiado; cobre o dano de fogo dos bosses.", "Magic charm (level 32): grants Guard when you're Ignited; covers boss fire damage.")),
  O("Rite of Passage", "u", 50, 95, ("Ao matar Rare ou Unique você fica possuído por espíritos animais (o autor usa o Lobo: velocidade de ataque). Luxo (~15 Divines).", "On killing a Rare or Unique you're possessed by animal spirits (the author uses the Wolf: attack speed). Luxury (~15 Divines).")),
]
GEAR_OPTS["flasks"] = [
  O("Lesser Life Flask", "r", 1, 40, ("Base de vida do começo: use a melhor que cair.", "Early life base: use the best that drops.")),
  O("Greater Life Flask", "r", 10, 46, ("Base de nível 10.", "Level 10 base.")),
  O("Grand Life Flask", "r", 16, 52, ("Base de nível 16.", "Level 16 base.")),
  O("Giant Life Flask", "r", 23, 58, ("Base de nível 23.", "Level 23 base.")),
  O("Colossal Life Flask", "r", 30, 64, ("Base de nível 30: mais vida por carga. Hard to Kill (árvore) aumenta a recuperação em 40%.", "Level 30 base: more life per charge. Hard to Kill (tree) adds 40% recovery.")),
  O("Transcendent Life Flask", "r", 50, 74, ("Base de nível 50.", "Level 50 base.")),
  O("Ultimate Life Flask", "r", 60, 84, ("A base do autor no endgame (nível 60): vida recuperada e cargas ganhas altas.", "The author's endgame base (level 60): high life recovered and charges gained."), cost="cheap"),
  O("Lavianga's Spirits", "u", 49, 88, ("Flask de mana que não se usa: o efeito fica sempre ativo (~0,1 Divine, nível 49). Base Gargantuan Mana Flask.", "A mana flask you don't use: its effect is always on (~0.1 Divine, level 49). Gargantuan Mana Flask base.")),
]
SLOT_OPTS = ["spear", "set2", "helmet", "body", "gloves", "boots", "amulet", "rings", "belt", "charms", "flasks"]
