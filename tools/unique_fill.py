# -*- coding: utf-8 -*-
"""Completa 'Como' e 'Sem ele' dos cards de uniques do Silverfist que estavam vazios (revisão 17/09/2026)."""
EN_PAIRS = {}

def L(pt, en):
    EN_PAIRS[pt] = en
    return pt

FILL = {
 "Starkonja's Head": (L("Equipe no Ato 4 com o companion já capturado; se ele morrer, o dano volta todo para você.", "Equip it in Act 4 with the companion already captured; if it dies, all the damage comes back to you."),
                      L("Capacete rare com vida, resistências e +1 Minion Skills.", "Rare helmet with life, resistances and +1 Minion Skills.")),
 "Horror's Flight": (L("Só depois de fechar resistências em outros slots: as luvas não dão resistência.", "Only after capping resistances in other slots: the gloves give no resistance."),
                     L("Luvas rare com Evasion, vida e resistências.", "Rare gloves with Evasion, life and resistances.")),
 "Mageblood": (L("Só quando o resto do equipamento estiver pronto: é luxo e não muda a rotação.", "Only once the rest of your gear is done: it's luxury and doesn't change the rotation."), None),
 "Meginord's Girdle": (L("Use enquanto faltar Strength para gems e supports; troque quando o requisito estiver fechado.", "Use it while you lack Strength for gems and supports; swap once the requirement is met."),
                       L("Cinto rare com Strength e vida.", "Rare belt with Strength and life.")),
 "Kalandra's Touch": (L("Coloque um anel rare excelente na outra mão: o Kalandra copia os mods dele.", "Put an excellent rare ring in the other slot: Kalandra's copies its mods."),
                      L("Dois anéis rare.", "Two rare rings.")),
 "Eshtera's Path": (L("Encaixe uma Sapphire jewel com dano ou crítico de minion.", "Socket a Sapphire jewel with minion damage or crit."),
                    L("Anel rare com resistências e atributos.", "Rare ring with resistances and attributes.")),
 "Grip of Kulemak": (L("Confira o roll no trade antes de comprar: o efeito muda com o mod sorteado.", "Check the roll on trade before buying: the effect changes with the rolled mod."),
                     L("Anel rare com vida e resistências.", "Rare ring with life and resistances.")),
 "From Nothing": (None, L("Controlled Metamorphosis, ou pegue os nós pelo caminho normal da árvore.", "Controlled Metamorphosis, or take the nodes through the normal tree path.")),
 "Prism of Belief": (None, L("Jewel rare com dano de minion.", "Rare jewel with minion damage.")),
 "Heart of the Well": (L("Compre só com resistência física ou regeneração de minions entre os mods.", "Only buy one with minion physical resistance or regeneration among its mods."),
                       L("Jewel rare com vida ou dano de minion.", "Rare jewel with minion life or damage.")),
 "Megalomaniac": (L("Leia os notables no anúncio e ignore os que não são de minion ou defesa.", "Read the notables in the listing and skip any that aren't minion or defence."),
                  L("Jewel rare de minion.", "Rare minion jewel.")),
 "Nascent Hope": (L("Usa sozinho quando você é congelado; ótimo com Energy Shield.", "Triggers by itself when you're frozen; great with Energy Shield."), None),
 "Beira's Anguish": (L("Usa sozinho quando você sofre Ignite.", "Triggers by itself when you're ignited."), None),
 "Sanguis Heroum": (L("Usa sozinho quando você sangra.", "Triggers by itself when you bleed."), None),
 "Arakaali's Gift": (L("Usa sozinho quando você é envenenado.", "Triggers by itself when you're poisoned."), None),
 "The Fall of the Axe": (L("Usa sozinho quando você é desacelerado (Slow).", "Triggers by itself when you're slowed."),
                         L("Silver Charm mágico.", "Magic Silver Charm.")),
 "Rite of Passage": (L("Ativa ao matar rare ou unique; a possessão de Cat é a melhor para velocidade.", "Triggers when you kill a rare or unique; the Cat possession is best for speed."),
                     L("The Fall of the Axe.", "The Fall of the Axe.")),
 "Lavianga's Spirits": (L("Mantenha o efeito sempre ativo; combina com a mana do Mind Over Matter.", "Keep the effect up at all times; it pairs with Mind Over Matter's mana."), None),
 "Midnight Braid": (L("Use na campanha quando faltar mana para Pain Offering e marks.", "Use it in the campaign when you lack mana for Pain Offering and marks."), None),
 "Bushwhack": (L("Use do Ato 4 até achar botas rare com 30% de Movement Speed.", "Use it from Act 4 until you find rare boots with 30% Movement Speed."), None),
 "Umbilicus Immortalis": (L("Beba o life flask antes do golpe forte do boss: os minions não morrem durante o efeito.", "Drink the life flask before the boss's big hit: minions can't die during the effect."),
                          L("Midnight Braid, se o problema for mana e não a morte do macaco.", "Midnight Braid, if your problem is mana rather than the monkey dying.")),
 "Spiteful Floret": (None, L("Deixe o set 2 vazio e abra mão do Sanguine Revelry.", "Leave set 2 empty and give up Sanguine Revelry.")),
 "Controlled Metamorphosis": (L("Confira no anúncio quais nós ele aloca e o tamanho das resistências negativas; feche resist em outros slots.", "Check in the listing which nodes it allocates and how large the negative resistances are; cap resists in other slots."), None),
 "Undying Hate": (L("Opcional: confira no raio se os nós conquistados ficam perto dos notables de companion.", "Optional: check in the radius that the conquered nodes sit near the companion notables."),
                  L("Jewel rare de minion.", "Rare minion jewel.")),
 "Foxshade": (L("Use na campanha: o Movement Speed só vale com a vida cheia.", "Use it in the campaign: the Movement Speed only applies at full life."),
              L("Body Armour rare com Evasion e vida.", "Rare Body Armour with Evasion and life.")),
 "Blackheart": (L("Use dois, um em cada anel, até achar anéis com resistência.", "Use two, one per ring slot, until you find rings with resistances."),
                L("Anéis rare com dano ou resistência.", "Rare rings with damage or resistance.")),
 "Goldrim": (L("Use na campanha até ter resistências no resto do equipamento.", "Use it in the campaign until the rest of your gear has resistances."),
             L("Capacete rare com resistências.", "Rare helmet with resistances.")),
 "Wanderlust": (L("Use até achar botas com 25%+ de Movement Speed.", "Use them until you find boots with 25%+ Movement Speed."),
                L("Botas rare com Movement Speed.", "Rare boots with Movement Speed.")),
 "Surefooted Sigil": (L("Use na campanha e troque por amuleto com +Minion Skills.", "Use it in the campaign and swap for an amulet with +Minion Skills."),
                      L("Amuleto rare com vida e Dexterity.", "Rare amulet with life and Dexterity.")),
 "Skysliver": (L("Equipe no nível 16 para o Twister do Ato 2.", "Equip it at level 16 for Act 2 Twister."), None),
 "Splinter of Lorrata": (L("Equipe no nível 1 e troque pelo Skysliver no 16.", "Equip it at level 1 and swap for Skysliver at 16."),
                         L("Spear branca do vendor.", "White vendor spear.")),
}
# textos que estavam no campo errado
MOVE = {"Umbilicus Immortalis": "how", "Undying Hate": "how"}


def apply(uniques):
    for u in uniques:
        how, alt = FILL.get(u["n"], (None, None))
        if u["n"] in MOVE:
            u["how"] = ""
        if how and not u.get("how"): u["how"] = how
        if alt and not u.get("alt"): u["alt"] = alt
