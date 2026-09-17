# -*- coding: utf-8 -*-
"""Aba "Quando usar": requisitos reais, momento ideal e o que fazer se conseguir cedo ou tarde.

Níveis de requisito vêm do texto do item no poe.ninja (Forbidden Rites, 0.5.5) — dl/eco_Unique*.json.
Cada texto é (pt, en); build_site registra os pares na tradução.
"""
import json, glob

def _levels():
    """Nível exigido por unique, do Path of Building (PoE2): linha 'Requires Level' do unique ou, sem ela, o requisito do tipo base.
    (O campo levelRequired do poe.ninja NÃO é confiável: dizia 78 para o Sylvan's Effigy, que no jogo pede 62.)"""
    import re
    bases = {}
    for f in glob.glob("dl/pob/pob_*.lua"):
        for m in re.finditer(r'itemBases\["([^"]+)"\] = \{(.*?)\n\}', open(f, encoding="utf-8").read(), re.S):
            r = re.search(r"req = \{[^}]*level = (\d+)", m.group(2)); bases[m.group(1)] = int(r.group(1)) if r else 1
    out = {}
    for f in glob.glob("dl/pob/pobu_*.lua"):
        for blk in re.findall(r"\[\[(.*?)\]\]", open(f, encoding="utf-8").read(), re.S):
            lines = [l.strip() for l in blk.strip().splitlines() if l.strip()]
            if len(lines) < 2: continue
            name, base = lines[0], lines[1]
            rq = next((int(re.search(r"\d+", l).group()) for l in lines if l.startswith("Requires Level")), None)
            if name not in out:
                out[name] = {"base": rq or bases.get(base), "src": "unique" if rq else "base", "type": base}
    return out

LV = _levels()

def req(name, extra=("", "")):
    d = LV.get(name, {})
    b = d.get("base")
    pt = f"Nível {b}" if b else "Requisito não confirmado — confira no item"
    en = f"Level {b}" if b else "Requirement not confirmed — check the item"
    if b and d.get("src") == "base":
        pt += " (do tipo base — confira no item)"; en += " (from the base type — check the item)"
    if extra[0]:
        pt += " · " + extra[0]; en += " · " + extra[1]
    return (pt, en)

E = []
def add(kind, n, lvl, req_, when, gives, early, late, steps, watch=()):
    E.append(dict(kind=kind, n=n, lvl=lvl, req=req_, when=when, gives=gives, early=early, late=late, steps=list(steps), watch=list(watch)))

# ------------------------------------------------------------------ ITENS
add("item", "Sylvan's Effigy", (LV.get("Sylvan's Effigy") or {}).get("base") or 62,
    req("Sylvan's Effigy", ("Stoic Sceptre (1 mão)", "Stoic Sceptre (one-handed)")),
    ("A partir do nível 62 (requisito do item). Entra assim que você conseguir — normalmente no início do Atlas. Substitui o Rattling Sceptre.", "From level 62 (item requirement). Put it on as soon as you get it — usually early Atlas. Replaces the Rattling Sceptre."),
    ("Companions ilimitados (de tipos diferentes), 50–68% increased Spirit, atributos, regen de vida para aliados e mais dano dos companions em alvos marcados. Concede as skills Discipline e Azmerian Wolf.",
     "Unlimited companions (of different types), 50–68% increased Spirit, attributes, life regen for allies and more companion damage vs marked targets. Grants the Discipline and Azmerian Wolf skills."),
    ("Conseguiu antes do nível 62? Guarde até o 62. Já está no 62+? Equipe agora. Antes de trocar, deixe prontos: (1) beasts de aura de tipos diferentes capturados — Haste (Quill/Coconut Crab) e Physical (Swarming Wisp / Plague Swarm); (2) Primate Idol + Rabbit Idol para os sockets; (3) um Skeletal Cleric para ser o alvo do Pain Offering, porque a gem Skeletal Warrior sai junto com o Rattling Sceptre.",
     "Got it before level 62? Keep it until 62. Already 62+? Equip it now. Before swapping, have ready: (1) captured aura beasts of different types — Haste (Quill/Coconut Crab) and Physical (Swarming Wisp / Plague Swarm); (2) Primate Idol + Rabbit Idol for the sockets; (3) a Skeletal Cleric to be the Pain Offering target, because the Skeletal Warrior gem leaves with the Rattling Sceptre."),
    ("Ainda não tem? A rota continua funcionando com Rattling Sceptre e 2 companions. O Effigy é o maior upgrade de Spirit e de companions: priorize antes de Idolatry e de itens de luxo.",
     "Don't have it yet? The route still works with Rattling Sceptre and 2 companions. The Effigy is the biggest Spirit and companion upgrade: prioritize it over Idolatry and luxury items."),
    [("Tire o Rattling Sceptre: a gem Skeletal Warrior some. O alvo do Pain Offering passa a ser o Skeletal Cleric (Sacrificial Lamb II + Tecrod's Revenge).", "Remove the Rattling Sceptre: the Skeletal Warrior gem disappears. The Pain Offering target becomes the Skeletal Cleric (Sacrificial Lamb II + Tecrod's Revenge)."),
     ("Com Chober Chaber você ainda precisa de Giant's Blood (Treefingers ou keystone) para usar maça de 2 mãos + sceptre.", "With Chober Chaber you still need Giant's Blood (Treefingers or keystone) to use a two-handed mace + sceptre."),
     ("Ative os companions nesta ordem, olhando o Spirit: Silverfist/Zekoa → beast Haste → Azmerian Wolf → beast Physical → beast ES.", "Activate companions in this order, watching Spirit: Silverfist/Zekoa → Haste beast → Azmerian Wolf → Physical beast → ES beast."),
     ("Mantenha o Trusted Kinship: os 30% more de eficiência de reserva continuam valendo com companions ilimitados.", "Keep Trusted Kinship: its 30% more reservation efficiency still applies with unlimited companions."),
     ("Coloque Primate Idol + Rabbit Idol nos sockets.", "Socket Primate Idol + Rabbit Idol."),
     ("Supports do Azmerian Wolf: Feeding Frenzy II · Rapid Attacks II · Rage III · Hulking Minions (ou Muster) · Loyalty.", "Azmerian Wolf supports: Feeding Frenzy II · Rapid Attacks II · Rage III · Hulking Minions (or Muster) · Loyalty.")],
    [("Tipos iguais não contam: todos os companions precisam ser de tipos diferentes.", "Same types don't count: every companion must be a different type."),
     ("Se o Spirit ficar negativo, desligue o último beast de aura antes de mexer no macaco.", "If Spirit goes negative, turn off the last aura beast before touching the monkey.")])

add("item", "Chober Chaber", (LV.get("Chober Chaber") or {}).get("base") or 33,
    req("Chober Chaber", ("+100 de Intelligence exigido (triplica com Giant's Blood)", "+100 Intelligence required (tripled with Giant's Blood)")),
    ("Ato 3 no modo completo; início do Atlas no modo barato (quando pegar a Catha's Balance).", "Act 3 in full mode; early Atlas in budget mode (when you get Catha's Balance)."),
    ("Maça de 2 mãos: +2 Minion Skills, +50 Spirit, +80–100 mana e dano físico alto. Com The Catha's Balance, 60% do dano dela vai para cada golpe dos companions.", "Two-handed mace: +2 Minion Skills, +50 Spirit, +80–100 mana and high physical damage. With The Catha's Balance, 60% of its damage goes into every companion hit."),
    ("Antes da Catha's Balance ela já vale pelos +2 Minion Skills e +50 Spirit. Para usar junto com o Rattling Sceptre você precisa de Giant's Blood (Treefingers) e, por causa dos requisitos triplicados, da The Vertex.",
     "Before Catha's Balance it's already worth it for +2 Minion Skills and +50 Spirit. To use it with Rattling Sceptre you need Giant's Blood (Treefingers) and, because of tripled requirements, The Vertex."),
    ("Sem ela: Trenchtimbre (main) + Rattling Sceptre. Depois da Catha's Balance, cada nível sem a Chober é dano perdido: ela é a primeira compra do Atlas.", "Without it: Trenchtimbre (main) + Rattling Sceptre. After Catha's Balance, every level without Chober is lost damage: it's the first Atlas purchase."),
    [("Equipe Treefingers (Giant's Blood) antes, senão o sceptre sai da offhand.", "Equip Treefingers (Giant's Blood) first, otherwise the sceptre leaves the offhand."),
     ("Confira os atributos: sem The Vertex, 100 de Intelligence vira 300.", "Check attributes: without The Vertex, 100 Intelligence becomes 300."),
     ("Fique no weapon set dela: a Catha's Balance lê a main-hand do set ativo.", "Stay on its weapon set: Catha's Balance reads the active set's main hand.")],
    [("Julgue arma de Catha pelo dano por golpe, não pelo DPS.", "Judge Catha weapons by damage per hit, not DPS.")])

add("item", "Treefingers", (LV.get("Treefingers") or {}).get("base") or 11, req("Treefingers"),
    ("Junto com a Chober Chaber (Ato 3 no modo completo).", "Together with Chober Chaber (Act 3 in full mode)."),
    ("Luvas com Giant's Blood: armas de 2 mãos em uma mão, mas requisitos de atributo das armas triplicados.", "Gloves with Giant's Blood: two-handed weapons in one hand, but weapon attribute requirements are tripled."),
    ("Barata e de nível baixo: pode comprar assim que tiver a Chober Chaber.", "Cheap and low level: buy it as soon as you have Chober Chaber."),
    ("Quando pegar o keystone Giant's Blood na árvore (fase T15+), as luvas ficam livres para um rare de Evasion/Deflection com vida e resist.", "Once you take the Giant's Blood keystone on the tree (T15+ phase), the gloves slot frees up for a rare with Evasion/Deflection, life and resists."),
    [("Equipe antes de colocar o sceptre na offhand.", "Equip before putting the sceptre in the offhand.")],
    [("Não use Treefingers e o keystone ao mesmo tempo: é redundante.", "Don't use Treefingers and the keystone at the same time: it's redundant.")])

add("item", "The Vertex", (LV.get("The Vertex") or {}).get("base") or 33, req("The Vertex"),
    ("Logo depois de Chober Chaber + Giant's Blood.", "Right after Chober Chaber + Giant's Blood."),
    ("Capacete que zera requisitos de atributo de gems e de equipamento: resolve os requisitos triplicados do Giant's Blood.", "Helmet that removes attribute requirements from gems and equipment: fixes the tripled requirements from Giant's Blood."),
    ("Se ainda não usa Giant's Blood, ela não é urgente: um capacete com +Minion Skills ou Spirit rende mais.", "If you don't use Giant's Blood yet it isn't urgent: a helmet with +Minion Skills or Spirit is better."),
    ("Sem ela, compense com atributos na árvore (Polymathy), Soul Cores de atributo ou itens com Strength/Intelligence.", "Without it, compensate with tree attributes (Polymathy), attribute Soul Cores or items with Strength/Intelligence."),
    [("Confira no trade se o item tem 'Equipment has no Attribute Requirements'.", "Check on trade that the item has 'Equipment has no Attribute Requirements'.")],
    [("Trocar a The Vertex por Alpha's Howl (+100 Spirit) traz os requisitos triplicados de volta.", "Swapping The Vertex for Alpha's Howl (+100 Spirit) brings the tripled requirements back.")])

add("item", "Enfolding Dawn", (LV.get("Enfolding Dawn") or {}).get("base") or 1, req("Enfolding Dawn"),
    ("Ato 3 até trocar pela Forgotten Warden.", "Act 3 until you swap to Forgotten Warden."),
    ("Body com +100 Spirit. Custo: você não ganha o bônus inerente de Intelligence (menos mana).", "Body armour with +100 Spirit. Cost: you gain no inherent bonus from Intelligence (less mana)."),
    ("Quanto antes, melhor: é o maior ganho de Spirit da campanha.", "The earlier the better: it's the biggest Spirit gain of the campaign."),
    ("Sem ela, você perde espaço para o beast de aura ou para o esqueleto. Um body rare com Spirit é o substituto.", "Without it you lose room for the aura beast or the skeleton. A rare body with Spirit is the replacement."),
    [("Ao trocar pela Forgotten Warden você perde +100 Spirit: faça a troca depois do Sylvan's Effigy (increased Spirit) e confira o painel.", "When swapping to Forgotten Warden you lose +100 Spirit: do it after Sylvan's Effigy (increased Spirit) and check the panel.")])

add("item", "Evergrasping Ring", (LV.get("Evergrasping Ring") or {}).get("base") or 32, req("Evergrasping Ring"),
    ("Ato 4 (nível 32+), os dois anéis.", "Act 4 (level 32+), both rings."),
    ("Aliados na sua Presence ganham 15–25% do dano como chaos extra, +mana.", "Allies in your Presence gain 15–25% of damage as extra chaos, +mana."),
    ("Pode usar assim que tiver o nível. Combine com Withering Presence.", "Use it as soon as you have the level. Pair it with Withering Presence."),
    ("Sem os anéis, o Withering Presence quase não faz nada: não use o Withering Presence e feche resist com anéis rare.", "Without the rings Withering Presence does almost nothing: skip Withering Presence and cap resists with rare rings."),
    [("Mantenha os companions dentro da Presence.", "Keep companions inside your Presence.")],
    [("Os anéis não dão resist: feche resist em outros slots.", "The rings give no resists: cap resists elsewhere.")])

add("item", "Yriel's Fostering", (LV.get("Yriel's Fostering") or {}).get("base") or 52, req("Yriel's Fostering"),
    ("Só se você ainda NÃO tem o Trusted Kinship.", "Only if you do NOT have Trusted Kinship yet."),
    ("Body com 'You can have two Companions of different types', vida e um pouco de Spirit.", "Body armour with 'You can have two Companions of different types', life and a bit of Spirit."),
    ("Útil se chegou ao Ato 4 sem o keystone. Assim que pegar o Trusted Kinship, volte para Enfolding Dawn (+100 Spirit).", "Useful if you reached Act 4 without the keystone. As soon as you take Trusted Kinship, go back to Enfolding Dawn (+100 Spirit)."),
    ("Não faz falta nesta rota: o Trusted Kinship já dá o mesmo limite.", "Not needed in this route: Trusted Kinship already gives the same limit."),
    [],
    [("NÃO soma com o Trusted Kinship: continua 2 companions.", "Does NOT stack with Trusted Kinship: still 2 companions.")])

add("item", "Forgotten Warden", (LV.get("Forgotten Warden") or {}).get("base") or 70, req("Forgotten Warden"),
    ("Depois do Sylvan's Effigy, quando o requisito do item permitir.", "After Sylvan's Effigy, once the item's requirement allows."),
    ("Companions com 30–50% mais vida, parte do dano Deflected vai para eles, Evasion/ES alto. Concede a skill Spirit Vessel.", "Companions get 30–50% more life, part of Deflected damage goes to them, high Evasion/ES. Grants the Spirit Vessel skill."),
    ("Se o requisito do item for maior que o seu nível, guarde e siga com Enfolding Dawn.", "If the item's requirement is above your level, keep it and stay on Enfolding Dawn."),
    ("Sem ela, continue com Enfolding Dawn; é o upgrade de defesa do zoo no endgame.", "Without it, stay on Enfolding Dawn; it's the zoo's endgame defensive upgrade."),
    [("Você perde os +100 Spirit da Enfolding Dawn: confira se o zoo ainda cabe.", "You lose Enfolding Dawn's +100 Spirit: check the zoo still fits."),
     ("Spirit Vessel até o nível 90: Loyalty + Furious Slam + Arctic Howl + Rapid Attacks II + Rage III. No endgame 90+: Loyalty + Devour + Oil Barrage + Salvo + Living Lightning II.", "Spirit Vessel until level 90: Loyalty + Furious Slam + Arctic Howl + Rapid Attacks II + Rage III. At endgame 90+: Loyalty + Devour + Oil Barrage + Salvo + Living Lightning II.")])

add("item", "Trenchtimbre", (LV.get("Trenchtimbre") or {}).get("base") or 16, req("Trenchtimbre"),
    ("Ato 3 no modo barato, até a Chober Chaber.", "Act 3 in budget mode, until Chober Chaber."),
    ("Maça de 1 mão com +1 Minion Skills e attack speed.", "One-handed mace with +1 Minion Skills and attack speed."),
    ("Barata: compre já no Ato 2–3.", "Cheap: buy it already in Acts 2–3."),
    ("Sem ela, use qualquer arma com +Minion Skills.", "Without it, use any weapon with +Minion Skills."),
    [("Troque pela Chober Chaber assim que pegar a Catha's Balance.", "Swap to Chober Chaber as soon as you get Catha's Balance.")])

add("item", "Rattling Sceptre", 1, ("Tipo base (não é unique)", "Base type (not a unique)"),
    ("Ato 3 até o Sylvan's Effigy.", "Act 3 until Sylvan's Effigy."),
    ("Sceptre que dá a gem Skeletal Warrior. Rare com +Minion Skills e Spirit é o ideal.", "Sceptre that grants the Skeletal Warrior gem. A rare with +Minion Skills and Spirit is ideal."),
    ("Pode usar desde cedo como offhand.", "Usable early as offhand."),
    ("Sem ele, use um Skeletal Arsonist (gem) como alvo do Pain Offering.", "Without it, use a Skeletal Arsonist (gem) as the Pain Offering target."),
    [], [("Sai quando entrar o Sylvan's Effigy.", "Leaves when Sylvan's Effigy comes in.")])

add("item", "Alpha's Howl", (LV.get("Alpha's Howl") or {}).get("base") or 65, req("Alpha's Howl"),
    ("Só se faltar Spirit no início do Atlas.", "Only if you're short on Spirit in early Atlas."),
    ("Capacete com +100 Spirit, resist a frio e Presence com raio dobrado.", "Helmet with +100 Spirit, cold resistance and doubled Presence radius."),
    ("Nível 65: útil para caber o 2º esqueleto ou o Withering Presence antes do Effigy.", "Level 65: useful to fit the 2nd skeleton or Withering Presence before the Effigy."),
    ("Não é obrigatório.", "Not required."),
    [], [("Tira a The Vertex: com Giant's Blood os requisitos triplicados voltam.", "Replaces The Vertex: with Giant's Blood the tripled requirements come back.")])

add("item", "Spiteful Floret", (LV.get("Spiteful Floret") or {}).get("base") or 1, req("Spiteful Floret"),
    ("Weapon set 2 no endgame.", "Weapon set 2 in endgame."),
    ("Pelo guia do Mattjestic, dá o Sanguine Revelry quando está no weapon set 2.", "Per Mattjestic's guide it grants Sanguine Revelry while in weapon set 2."),
    ("Confira o requisito no item antes de comprar.", "Check the requirement on the item before buying."),
    ("Opcional.", "Optional."),
    [], [("Não fique com o set 2 ativo: a Catha's Balance lê a main-hand do set ATIVO.", "Don't stay on set 2: Catha's Balance reads the ACTIVE set's main hand.")])

add("item", "Lavianga's Spirits", (LV.get("Lavianga's Spirits") or {}).get("base") or 49, req("Lavianga's Spirits"),
    ("Junto com o Mind Over Matter (nível 90+).", "Together with Mind Over Matter (level 90+)."),
    ("Flask de mana com efeito constante.", "Mana flask with a constant effect."),
    ("Antes do Mind Over Matter ela ajuda pouco.", "Before Mind Over Matter it helps little."),
    ("Sem ela, o Mind Over Matter fica perigoso.", "Without it, Mind Over Matter is risky."), [])

add("item", "Darkness Enthroned", (LV.get("Darkness Enthroned") or {}).get("base") or 62, req("Darkness Enthroned"),
    ("Charm Slots extras no endgame.", "Extra Charm Slots for endgame."),
    ("Cinto com até 3 Charm Slots e 2 sockets escondidos (50–100% mais efeito): Greater Body Rune + a rune da resist que faltar. Idols não entram (são só de Capacete ou Sceptre).", "Belt with up to 3 Charm Slots and 2 hidden sockets (50–100% more effect): Greater Body Rune + a rune for the resist you lack. Idols don't fit (Helmet or Sceptre only)."),
    ("Nível 62; rende mais com roll alto de efeito.", "Level 62; best with a high effect roll."),
    ("Opcional.", "Optional."), [])

# ------------------------------------------------------------------ ASCENDÊNCIA
add("asc", "Wild Protector", 20, ("1º Trial of the Sekhemas (Ato 2)", "1st Trial of the Sekhemas (Act 2)"),
    ("Ato 2.", "Act 2."),
    ("Urso que tanka, não conta no limite de companions.", "A tanking bear that doesn't count toward the companion limit."),
    ("—", "—"),
    ("Sem ele, a campanha fica bem mais perigosa e você perde um tipo de minion para o Muster.", "Without it the campaign is much more dangerous and you lose a minion type for Muster."),
    [("Supports iniciais: Magnified Area I + Rage II.", "Starting supports: Magnified Area I + Rage II.")])
add("asc", "The Natural Order", 33, ("2º Trial (Trial of Chaos, Ato 3)", "2nd Trial (Trial of Chaos, Act 3)"),
    ("Ato 3, ANTES de matar o Silverfist.", "Act 3, BEFORE killing Silverfist."),
    ("Tame Beast captura unique beasts (1 por vez).", "Tame Beast can capture unique beasts (1 at a time)."),
    ("—", "—"),
    ("Se matou o Silverfist sem ela: ele é o boss dos mapas Riverside/Rupture (Zekoa). Capture lá.", "If you killed Silverfist without it: it's the boss of Riverside/Rupture maps (Zekoa). Capture it there."),
    [("Capture o Silverfist e faça o respec para minions.", "Capture Silverfist and respec to minions.")])
add("asc", "The Catha's Balance", 60, ("3º Trial (área de nível 60+)", "3rd Trial (area level 60+)"),
    ("Assim que chegar ao Atlas (nível ~60–65).", "As soon as you reach the Atlas (level ~60–65)."),
    ("Companions causam dano de ataque adicional igual a 60% do dano da sua main-hand.", "Companions deal extra attack damage equal to 60% of your main-hand damage."),
    ("Pegou cedo (logo no 60)? Ótimo: a partir daqui a arma é o maior multiplicador. Troque Trenchtimbre pela Chober Chaber já.", "Got it early (right at 60)? Great: from here the weapon is the biggest multiplier. Swap Trenchtimbre for Chober Chaber now."),
    ("Sem ela, o zoo fica sem dano nos mapas. Faça o 3º Trial em área 65+ (dropa itens Exceptional).", "Without it the zoo lacks damage in maps. Do the 3rd Trial in an area 65+ (drops Exceptional items)."),
    [("Main-hand com maior dano por golpe no set ativo.", "Highest per-hit main hand on the active set.")])
add("asc", "Idolatry", 75, ("4º Trial (área 75+)", "4th Trial (area 75+)"),
    ("Endgame, só com resist no cap sem depender de runas.", "Endgame, only with capped resists without relying on runes."),
    ("+10% dano de companions e +2% reservation efficiency por Idol; −4% em todas as resists por Augment que não é Idol.", "+10% companion damage and +2% reservation efficiency per Idol; −4% all resists per non-Idol Augment."),
    ("Se pegar cedo com runas de resist nos itens, suas resists caem.", "If taken early with resist runes in your items, your resists drop."),
    ("Opcional no modo barato.", "Optional in budget mode."),
    [("Troque runas por Idols só depois de capar resist pelo gear.", "Replace runes with Idols only after capping resists through gear.")])

# ------------------------------------------------------------------ KEYSTONES
add("key", "Trusted Kinship", 33, ("Keystone da árvore", "Tree keystone"),
    ("Ato 3, no respec para minions — e para sempre.", "Act 3, at the minion respec — and forever."),
    ("2 companions de tipos diferentes; 30% more eficiência de reserva de Companion; 20% less para as demais skills.", "2 companions of different types; 30% more Companion reservation efficiency; 20% less for other skills."),
    ("—", "—"),
    ("Sem ele: limite de 1 companion.", "Without it: 1-companion limit."),
    [], [("Não tire com o Effigy: os 30% more continuam valendo.", "Don't remove it with the Effigy: the 30% more still applies."),
         ("O 20% less deixa Withering Presence e esqueletos mais caros.", "The 20% less makes Withering Presence and skeletons more expensive.")])
add("key", "Giant's Blood", 78, ("Keystone da árvore (ou Treefingers antes)", "Tree keystone (or Treefingers before)"),
    ("Treefingers no Ato 3 → keystone na fase T15+.", "Treefingers in Act 3 → keystone in the T15+ phase."),
    ("Armas de 2 mãos em uma mão; requisitos de atributo das armas triplicados.", "Two-handed weapons in one hand; weapon attribute requirements tripled."),
    ("Pegar o keystone cedo custa pontos que fariam falta na campanha: use Treefingers.", "Taking the keystone early costs points you need in the campaign: use Treefingers."),
    ("—", "—"), [("Ao pegar o keystone, tire a Treefingers.", "When you take the keystone, remove Treefingers.")])
add("key", "Mind Over Matter", 90, ("Keystone da árvore", "Tree keystone"),
    ("Nível 90+.", "Level 90+."),
    ("Todo dano sai da mana antes da vida; 50% less recuperação de mana.", "All damage is taken from mana before life; 50% less mana recovery."),
    ("Sem mana alta (Chober Chaber + Lavianga's Spirits), é perigoso.", "Without high mana (Chober Chaber + Lavianga's Spirits) it's dangerous."),
    ("Opcional.", "Optional."), [])

# ------------------------------------------------------------------ SKILLS
add("skill", "Pain Offering", 31, ("Gem de skill (não reserva Spirit)", "Skill gem (reserves no Spirit)"),
    ("Ato 3 em diante.", "Act 3 onward."),
    ("Espeta um esqueleto: minions próximos ganham attack speed e dano.", "Skewers a skeleton: nearby minions gain attack speed and damage."),
    ("—", "—"), ("—", "—"),
    [("1 esqueleto: Prolonged Duration II + Sacrificial Offering.", "1 skeleton: Prolonged Duration II + Sacrificial Offering."),
     ("2+ esqueletos: adicione Danse Macabre.", "2+ skeletons: add Danse Macabre."),
     ("Sem Rattling Sceptre: Skeletal Cleric como alvo + Brutus' Brain.", "Without Rattling Sceptre: Skeletal Cleric as target + Brutus' Brain.")])
add("skill", "Withering Presence", 46, ("Gem (reserva Spirit fixo)", "Gem (flat Spirit reservation)"),
    ("Ato 4, com 2× Evergrasping Ring.", "Act 4, with 2× Evergrasping Ring."),
    ("Inimigos na Presence recebem Wither (mais dano de chaos).", "Enemies in your Presence get Wither (more chaos damage taken)."),
    ("Sem os anéis, não use.", "Without the rings, don't use it."), ("—", "—"), [])
add("skill", "Muster", 56, ("Support", "Support"),
    ("Interlúdios, quando tiver 3+ tipos de minion.", "Interludes, once you have 3+ minion types."),
    ("7% more dano por TIPO diferente de minion que revive.", "7% more damage per different reviving minion TYPE."),
    ("Com só macaco + urso + aura, Rapid Attacks rende mais.", "With only monkey + bear + aura, Rapid Attacks is better."), ("—", "—"), [])
add("skill", "Skeletal Cleric", 65, ("Gem de minion", "Minion gem"),
    ("Início do Atlas; vira o alvo do Pain Offering quando o Rattling Sceptre sai.", "Early Atlas; becomes the Pain Offering target when Rattling Sceptre leaves."),
    ("Cura o zoo e revive esqueletos.", "Heals the zoo and revives skeletons."),
    ("Pode entrar antes como 2º esqueleto (libera Danse Macabre) se couber no Spirit.", "Can come in earlier as the 2nd skeleton (unlocks Danse Macabre) if it fits your Spirit."), ("—", "—"), [])
add("skill", "Azmerian Wolf", 62, ("Vem do Sylvan's Effigy", "Comes from Sylvan's Effigy"),
    ("Junto com o Effigy (nível 62).", "Together with the Effigy (level 62)."),
    ("Segundo companion de dano.", "Second damage companion."),
    ("Sem Effigy não existe.", "Doesn't exist without the Effigy."), ("—", "—"), [])
add("skill", "Refutation", 65, ("Gem (precisa de Runic Ward)", "Gem (needs Runic Ward)"),
    ("Início do Atlas, com armaduras Runeforged.", "Early Atlas, with Runeforged armour."),
    ("Gasta o Runic Ward para bloquear todos os hits por um tempo.", "Spends Runic Ward to block all hits for a while."),
    ("Sem itens Runeforged/Runemastered você não tem Runic Ward: não adianta.", "Without Runeforged/Runemastered items you have no Runic Ward: it does nothing."), ("—", "—"), [])
add("skill", "Tame Beast (Zekoa)", 65, ("Mapas Riverside / Rupture", "Riverside / Rupture maps"),
    ("Atlas, quando achar um com mods melhores que o seu Silverfist.", "Atlas, when you find one with better mods than your Silverfist."),
    ("Versão de Atlas do Silverfist, pode ter mais modificadores (Extra Crits, Hasted).", "Atlas version of Silverfist, can have more modifiers (Extra Crits, Hasted)."),
    ("—", "—"), ("—", "—"),
    [("Tablets com 'Unique Monsters have 1 additional Rare Modifier' + Cruel Hegemony.", "Tablets with 'Unique Monsters have 1 additional Rare Modifier' + Cruel Hegemony.")])

# ------------------------------------------------------------------ CASOS
CASES = [
 (("Cheguei ao Atlas ainda no nível 60–65", "I reached the Atlas still at level 60–65"),
  ("Normal. Selecione 'Início do Atlas' em 'Onde você está' no topo: o guia passa a mostrar a fase do Atlas, e a árvore continua usando os pontos do seu nível. Já dá para usar: The Catha's Balance (3º Trial em área 60+), Chober Chaber, The Vertex, Evergrasping Ring e o Sylvan's Effigy (nível 62). Se tiver o Effigy, siga o cartão dele: tire o Rattling Sceptre, use Skeletal Cleric no Pain Offering e ative mais beasts de aura conforme o Spirit.",
   "Normal. Pick 'Early Atlas' in 'Where are you' at the top: the guide switches to the Atlas phase and the tree keeps using your level's points. Already usable: The Catha's Balance (3rd Trial in area 60+), Chober Chaber, The Vertex, Evergrasping Ring and Sylvan's Effigy (level 62). If you have the Effigy, follow its card: remove the Rattling Sceptre, use Skeletal Cleric for Pain Offering and activate more aura beasts as Spirit allows.")),
 (("Consegui um item antes do nível exigido", "I got an item before its level requirement"),
  ("Guarde. Veja o cartão do item nesta aba: ele diz o nível exato e o que preparar enquanto isso.",
   "Keep it. Check the item's card on this tab: it shows the exact level and what to prepare meanwhile.")),
 (("Estou mais atrasado que o nível (ex.: nível 70 ainda nos Interlúdios)", "I'm behind my level (e.g. level 70 still in the Interludes)"),
  ("Selecione a fase em que você realmente está. Os itens e skills seguem a fase; a árvore usa os pontos do nível e continua para a próxima fase quando sobrarem pontos.",
   "Select the phase you're actually in. Items and skills follow the phase; the tree uses your level's points and continues into the next phase when you have spare points.")),
 (("Tenho o Effigy mas não tenho Giant's Blood", "I have the Effigy but no Giant's Blood"),
  ("Você pode usar Effigy + arma de 1 mão (Trenchtimbre) sem Giant's Blood. Para Chober Chaber (2 mãos) + Effigy, precisa de Treefingers ou do keystone.",
   "You can use Effigy + a one-handed weapon (Trenchtimbre) without Giant's Blood. For Chober Chaber (two-handed) + Effigy you need Treefingers or the keystone.")),
]

EN_PAIRS = {}
def _reg(v):
    if isinstance(v, tuple) and len(v) == 2 and all(isinstance(x, str) for x in v):
        EN_PAIRS[v[0]] = v[1]; return v[0]
    if isinstance(v, list): return [_reg(x) for x in v]
    if isinstance(v, dict): return {k: _reg(x) for k, x in v.items()}
    return v

TIMING = [_reg(e) for e in E]
TIMING_CASES = [{"q": _reg(q), "a": _reg(a)} for q, a in CASES]

def unique_levels(UNIQUES):
    """Nível exigido dos uniques pelo Path of Building (ver _levels)."""
    for u in UNIQUES:
        u.pop("lvlRf", None)
        d = LV.get(u["n"])
        if d and d.get("base"):
            u["lvl"] = d["base"]; u["lvlSrc"] = d["src"]
        else:
            u["lvl"] = None
        if u.get("rf"):
            import re as _re
            u["rf"] = _re.sub(r"\s*\(nv \d+\)", "", u["rf"])


def effigy_62(DATA):
    """O Sylvan's Effigy pede nível 62 (texto do item no jogo), não 78."""
    m = DATA["milestones"]
    m.pop(78, None)
    m[63] = "Sylvan's Effigy liberado (requer nível 62, ~1 div): tire o Rattling Sceptre, Skeletal Cleric vira o alvo do Pain Offering e ative mais beasts de aura conforme o Spirit."
    for b in DATA["buyOrder"]:
        if "Sylvan's Effigy" in b["item"]:
            b["phase"] = "Nv 62+"
    DATA["fixes"] = ["Sylvan's Effigy é um Stoic Sceptre e requer nível 62 (texto do item no jogo)." if "Sylvan's Effigy é Stoic Sceptre" in f else f for f in DATA["fixes"]]
