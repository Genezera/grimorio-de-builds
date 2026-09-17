# -*- coding: utf-8 -*-
"""Blocos de crafting (mesmos textos do shared/craft-detail.js) para montar D.craftKit de qualquer build.
Cada função recebe o Book da build para registrar os pares PT→EN."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(HERE, "..", "dl", "web")


class Kit:
    def __init__(self, book):
        self.b = book; L = book.L
        self.P, self.X, self.D, self.DP, self.C = L("Prefixo", "Prefix"), L("Sufixo", "Suffix"), L("Sufixo (desecrate)", "Suffix (desecrated)"), L("Prefixo (desecrate)", "Prefix (desecrated)"), L("Mod crafted", "Crafted mod")
        self.divine = self.S(L("Divine Orb nos valores", "Divine Orb for values"),
            L("Divine Orb rerrola os valores dos mods dentro dos respectivos intervalos; não troca o tier nem o tipo de mod. Faça isso antes de qualquer etapa que possa corromper ou santificar o item.", "A Divine Orb rerolls modifier values within their ranges; it does not change the tier or modifier type. Do this before any step that can corrupt or sanctify the item."),
            L("Rolou pior: outro Divine. Pare quando o ganho for pequeno perto do preço.", "Rolled worse: another Divine. Stop when the gain is small compared to the price."))

    @staticmethod
    def S(t, d, f=""):
        return {"t": t, "d": d, "f": f}

    def ess_start(self, ess, mod_pt, mod_en, base_pt, base_en):
        L = self.b.L
        return self.S(L(f"Base Magic → {ess}", f"Magic base → {ess}"),
            L(f"{base_pt}. Use Orb of Transmutation (Greater = mod nível 44+, Perfect = 70+) e, se o mod servir, Orb of Augmentation. Com o item Magic, use {ess}: ele vira Rare com {mod_pt} garantido. Essa essence ocupa o único mod crafted do item — não planeje Alloy ou outra essence depois.",
              f"{base_en}. Use an Orb of Transmutation (Greater = modifier level 44+, Perfect = 70+) and, if the modifier helps, an Orb of Augmentation. On the Magic item, use {ess}: it becomes Rare with {mod_en} guaranteed. That essence takes the item’s only crafted modifier — do not plan an Alloy or another essence afterwards."),
            L("Annulment pode remover um mod de um item Magic, inclusive um mod bom. Compare esse custo com outra base; Transmutation exige Normal e Augmentation exige um slot Magic livre.", "Annulment can remove a modifier from a Magic item, including a good one. Compare that cost with another base; Transmutation requires Normal and Augmentation requires a free Magic slot."))

    def side_exalt(self, side, what_pt, what_en):
        L = self.b.L; om = "Sinistral" if side == "p" else "Dextral"; lado = "prefixo" if side == "p" else "sufixo"; sideen = "prefix" if side == "p" else "suffix"
        return self.S(L(f"Exalted com lado travado: {what_pt}", f"Side-locked Exalted: {what_en}"),
            L(f"Deixe o Omen of {om} Exaltation ativo no inventário e use um Exalted Orb: o mod novo sai só como {lado}. Greater Exalted (mod nível 35+) corta os tiers baixos; Perfect Exalted (50+) corta ainda mais, mas nenhum dos dois garante T1 nem a família certa.",
              f"Keep an Omen of {om} Exaltation active in your inventory and use an Exalted Orb: the new modifier can only be a {sideen}. Greater Exalted (modifier level 35+) removes low tiers; Perfect Exalted (50+) removes more, but neither guarantees T1 or the right family."),
            L(f"Mod errado nesse lado: Omen of {om} Annulment + Orb of Annulment remove só um {lado} aleatório — com mais de um mod bom nesse lado, você pode perder o bom. Se o item já resolve a fase, pare aqui.",
              f"Wrong modifier on that side: Omen of {om} Annulment + Orb of Annulment removes one random {sideen} — with more than one good modifier on that side you can lose a good one. If the item already solves your stage, stop here."))

    def desecrate(self, bone, lich, want_pt, want_en):
        L = self.b.L
        lp = f" com {lich} ativo (força um mod desse Lich; só funciona em arma e joalheria)" if lich else ""
        le = f" with {lich} active (forces that Lich’s modifier; weapons and jewellery only)" if lich else ""
        return self.S(L(f"Desecrate: {bone}{' + ' + lich if lich else ''}", f"Desecrate: {bone}{' + ' + lich if lich else ''}"),
            L(f"Deixe um espaço livre no lado do alvo. Use {bone} no Rare{lp}. O mod fica escondido: revele no Well of Souls com Omen of Abyssal Echoes ativo (permite rerrolar as opções uma vez) e escolha {want_pt}. O item aceita só 1 mod desecrated.",
              f"Leave a free slot on the target side. Use {bone} on the Rare{le}. The modifier stays hidden: reveal it at the Well of Souls with an Omen of Abyssal Echoes active (lets you reroll the options once) and pick {want_en}. An item holds only 1 desecrated modifier."),
            L("Não apareceu: Omen of Light + Orb of Annulment remove só o mod desecrated. Use outro osso e repita. Some Light + Annulment + osso + Echoes e todos os Omens de Lich/lado consumidos ao custo de cada nova tentativa.", "Not offered: Omen of Light + Orb of Annulment removes only the desecrated modifier. Use another bone and retry. Include Light + Annulment + bone + Echoes and every consumed Lich/side Omen in each retry cost."))

    def alloy(self, name, mod_pt, mod_en):
        L = self.b.L
        return self.S(L(f"{name} (mod crafted)", f"{name} (crafted modifier)"),
            L(f"{name} remove um mod aleatório e adiciona {mod_pt}. Use quando o item ainda não tem essence/alloy (limite de 1 crafted) e quando perder qualquer um dos mods atuais for aceitável — ou aplique cedo, com 3–4 mods baratos.",
              f"{name} removes a random modifier and adds {mod_en}. Use it when the item has no essence/alloy yet (1 crafted limit) and when losing any current modifier is acceptable — or apply it early, with 3–4 cheap modifiers."),
            L("Levou um mod importante: complete de novo com Exalted de lado travado; não use um segundo Alloy.", "It removed an important modifier: refill it with a side-locked Exalted; do not use a second Alloy."))

    def quality(self, scrap, infuser=""):
        L = self.b.L
        ip = f" Só depois de terminar os mods, Divines e sockets, considere {infuser}: é opcional, pode corromper e permite até 10% além da qualidade máxima." if infuser else ""
        ie = f" Only after finishing modifiers, Divines and sockets, consider {infuser}: it is optional, can corrupt and allows up to 10% above maximum quality." if infuser else ""
        return self.S(L("Qualidade, sockets e augments", "Quality, sockets and augments"),
            L(f"{scrap} até 20% de qualidade. Artificer’s Orb adiciona socket de augment (armas, wands, staves e armaduras). Coloque a rune/soul core indicada na aba Itens.{ip}",
              f"{scrap} up to 20% quality. Artificer’s Orb adds an augment socket (weapons, wands, staves and armour). Insert the rune/soul core listed on the Items tab.{ie}"),
            L("Corrompeu: o item não aceita mais crafting. Por isso isso fica por último.", "It corrupted: the item accepts no more crafting. That is why this comes last."))

    def runeforge(self, base, cost):
        L = self.b.L
        return self.S(L(f"Runeforging na Verisium Anvil ({cost})", f"Runeforging at the Verisium Anvil ({cost})"),
            L(f"{base}: {cost}. Liberada pela quest The Runeseeker (Ato 4). Armaduras acima do nível 55 trocam parte da defesa base por Runic Ward (a perda caiu ~20% no 0.5.3). Confira a prévia na Anvil antes de confirmar.",
              f"{base}: {cost}. Unlocked by The Runeseeker quest (Act 4). Armour above level 55 trades part of its base defence for Runic Ward (the loss was reduced ~20% in 0.5.3). Check the Anvil preview before confirming."),
            L("Se você não usa skills que gastam Runic Ward, a perda de defesa pode não valer.", "If you use no skills that spend Runic Ward, the defence loss may not be worth it."))

    def trade(self, filters, extra_pt="", extra_en=""):
        L = self.b.L
        return self.S(L("Comprar pronto no trade", "Buy it finished on trade"),
            L(f"Filtros: {filters}. {extra_pt} Ordene por preço e compare 3–5 opções: compare o preço pronto com o orçamento total do craft; a melhor opção depende do mercado e dos mods.",
              f"Filters: {filters}. {extra_en} Sort by price and compare 3–5 listings: compare the finished price with your total crafting budget; the better option depends on the market and modifiers."),
            L("Poucos resultados: tire o filtro do mod menos importante ou aceite o tier abaixo.", "Few results: drop the filter for the least important modifier or accept the tier below."))

    def item(self, id, name, page, goal, base, stop, trap, patterns, owned=()):
        return dict(id=id, name=name, page=page, goal=goal, base=base, stop=stop, trap=trap, patterns=list(patterns), owned=list(owned))


def tiers(page, pattern, n=2, kind="normal"):
    """Tiers mais altos de uma família (texto, nível, lado) direto do cache do PoE2DB — para escrever os alvos."""
    rows = json.load(open(os.path.join(WEB, f"mods_{page}.json"), encoding="utf-8"))[0]["mods"]
    rx = re.compile(pattern, re.I)
    hit = sorted([m for m in rows if m["kind"] == kind and rx.search(m["text"])], key=lambda m: -m["level"])
    return [(m["text"], m["level"], m["gen"], m["name"]) for m in hit[:n]]


if __name__ == "__main__":
    import sys
    page = sys.argv[1]
    for pat in sys.argv[2:]:
        for t in tiers(page, pat, 3):
            print(f"{page} | {pat} | {t}")
