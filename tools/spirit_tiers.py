# -*- coding: utf-8 -*-
"""Classifica as gems de cada fase pelo custo de Spirit, na ordem em que devem entrar.

sp = "core" (reserva Spirit — ative nesta ordem), "free" (não reserva Spirit), "opt" (só se sobrar Spirit)
pr = prioridade dentro de "core"/"opt" · cost = texto curto do custo
Referência real (jogador, nível 49, ~210 Spirit, set completo): Silverfist + 1 beast de aura (Haste) +
Withering Presence + 1 esqueleto (Arsonist) cabem; um Skeletal Warrior a mais já não cabe.
"""

FREE = "Sem Spirit"

def tag(g, sp, pr=0, cost=FREE):
    g["sp"] = sp; g["pr"] = pr; g["cost"] = cost

def apply(PH, MILESTONES, TROUBLESHOOT, CURRENT_SETUP, TRICKS, OPTS=(), UNIQ=()):
    def find(pid, start):
        return next(g for g in PH[pid]["gems"] if g["skill"].startswith(start))

    # ---------------------------------------------------------------- Ato 3
    p = PH["a3"]
    tag(find("a3", "Tame Beast (Mighty"), "core", 1, "~47% do Spirit")
    tag(find("a3", "Wild Protector"), "free", 0, "Ascendência")
    sk = find("a3", "Skeletal Warrior")
    sk["skill"] = "Skeletal Warrior (1 esqueleto)"
    sk["why"] = "Vem como gem do Rattling Sceptre. Você só precisa de UM esqueleto vivo: ele é o alvo que o Pain Offering espeta. Não é para dar dano. Sacrificial Lamb garante que o espinho pegue ele (e nunca o macaco) e Meat Shield mantém ele vivo."
    tag(sk, "core", 2, "Pouco Spirit (1 minion)")
    po = find("a3", "Pain Offering")
    po["sup"] = ["Prolonged Duration II", "Sacrificial Offering"]
    po["why"] = "Espeta 1 esqueleto: minions a até 6 m ganham até +29% attack speed e +58% dano. Não reserva Spirit, só gasta mana. Danse Macabre só entra quando você tiver 2 esqueletos vivos (Interlúdios em diante); com 1 esqueleto ele não funciona."
    tag(po, "free")
    tag(find("a3", "Unearth"), "free")
    tag(find("a3", "Raise Shield"), "free")
    aura = find("a3", "Tame Beast (2º")
    tag(aura, "opt", 1, "~21–25% do Spirit")
    aura["why"] = "Entra quando o Spirit deixar (depois do Ignagduk, +30 Spirit, no nível ~40). Escolha pelo modificador de aura (Haste/Physical), não pelo dano. Last Gasp mantém a aura viva, Loyalty faz ele tomar parte do seu dano."
    tag(find("a3", "Tame Beast (vazia)"), "free", 0, "Só reserva quando capturar")
    for g in p["gems"]:
        if g.get("until"): tag(g, "free")
    p["spiritNote"] = "Ordem do Spirit no Ato 3: 1) Mighty Silverfist → 2) 1 Skeletal Warrior (alvo do Pain Offering) → 3) 2º beast de aura só depois do Ignagduk (+30 Spirit). Pain Offering, Unearth e Raise Shield não reservam nada."

    # ---------------------------------------------------------------- Ato 4
    p = PH["a4"]
    tag(find("a4", "Tame Beast (Mighty"), "core", 1, "~47% do Spirit")
    aura = find("a4", "Tame Beast (2º")
    tag(aura, "core", 2, "~21–25% do Spirit")
    aura["skill"] = "Tame Beast (2º beast: aura Haste)"
    aura["why"] = "O beast de aura vem logo depois do macaco: a aura de Haste acelera o zoo inteiro. Loyalty faz ele absorver parte do seu dano e Last Gasp mantém a aura ativa mesmo depois de morrer."
    wp = find("a4", "Withering Presence")
    tag(wp, "core", 3, "Reserva fixa")
    sk = find("a4", "Skeletal Warrior")
    sk["skill"] = "Skeletal Warrior (ou 1 Arsonist)"
    sk["why"] = "Só UM esqueleto: ele é o alvo do Pain Offering. Pode ser o Skeletal Warrior do Rattling Sceptre OU um Skeletal Arsonist — se você já usa o Arsonist, NÃO ative o Warrior também, porque os dois não cabem no Spirit do Ato 4. Sacrificial Lamb I garante que o Pain Offering espete esse esqueleto."
    tag(sk, "core", 4, "Pouco Spirit (1 minion)")
    po = find("a4", "Pain Offering")
    po["sup"] = ["Prolonged Duration II", "Sacrificial Offering"]
    po["why"] = "Continua sendo o botão de boss e não reserva Spirit. Com 1 esqueleto use Prolonged Duration II + Sacrificial Offering; Danse Macabre só quando tiver 2 esqueletos vivos."
    tag(po, "free")
    for s in ("Sniper's Mark", "Unearth", "Raise Shield"):
        tag(find("a4", s), "free")
    tag(find("a4", "Wild Protector"), "free", 0, "Ascendência")
    third = find("a4", "Tame Beast (3º")
    tag(third, "opt", 1, "~21–25% do Spirit")
    third["why"] = "Só quando ganhar mais Spirit (Lythara +40 nos Interlúdios, capacete/amuleto com Spirit). Até lá, deixe a gem vazia só para capturar: Quill Crab e Coconut Crab aparecem no Whakapanu Island (Ato 4); Haste neles é sorte."
    p["gems"].append({"skill": "Skeletal Warrior (2º esqueleto)", "set": "—", "sup": ["Sacrificial Lamb I"], "role": "Só se sobrar Spirit",
                      "why": "Um 2º esqueleto libera o Danse Macabre no Pain Offering (+30% efeito). Com ~210 Spirit no nível 49 ele NÃO cabe junto com Silverfist + aura + Withering Presence + 1 esqueleto. Deixe para os Interlúdios.",
                      "sp": "opt", "pr": 2, "cost": "Pouco Spirit (1 minion)"})
    p["spiritNote"] = "Com ~210 Spirit (nível ~49, set completo) cabem exatamente: 1) Mighty Silverfist → 2) 1 beast de aura (Haste) → 3) Withering Presence → 4) 1 esqueleto (Warrior OU Arsonist). Pain Offering, Sniper's Mark, Unearth e Raise Shield não reservam Spirit. 3º beast e 2º esqueleto só depois do Lythara (+40 Spirit)."

    # ---------------------------------------------------------------- Interlúdios
    p = PH["int"]
    tag(find("int", "Tame Beast (Mighty"), "core", 1, "~47% do Spirit")
    tag(find("int", "Tame Beast (2º"), "core", 2, "~21–25% do Spirit")
    tag(find("int", "Withering Presence"), "core", 3, "Reserva fixa")
    sk = find("int", "Skeletal Warrior")
    sk["why"] = "O esqueleto alvo do Pain Offering (Sacrificial Lamb II alcança 6 m). Se você usa Arsonist como esqueleto principal, ele ocupa esta vaga."
    tag(sk, "core", 4, "Pouco Spirit (1 minion)")
    order = [("Skeletal Arsonist", 1), ("Skeletal Sniper", 2), ("Skeletal Frost Mage", 3), ("Skeletal Reaver", 4)]
    for name, pr in order:
        g = find("int", name)
        g["role"] = "Tipo extra (Muster) · opcional"
        g["why"] = "Cada TIPO diferente de minion dá +7% more dano ao macaco com Muster e o 2º esqueleto libera o Danse Macabre. Ative um por vez e só enquanto couber no Spirit: se o painel de skills mostrar Spirit negativo, desligue o último que entrou."
        tag(g, "opt", pr, "Pouco Spirit (1 minion)")
    po = find("int", "Pain Offering")
    po["why"] = "Com 2 esqueletos vivos (o Warrior + um tipo extra), o Danse Macabre funciona: +30% no buff. Com só 1 esqueleto, troque Danse Macabre por Sacrificial Offering."
    tag(po, "free")
    tag(find("int", "Vulnerability"), "free")
    tag(find("int", "Wild Protector"), "free", 0, "Ascendência")
    p["spiritNote"] = "Ordem do Spirit nos Interlúdios: 1) Silverfist → 2) beast de aura → 3) Withering Presence → 4) 1 esqueleto. Depois do Lythara (+40 Spirit), adicione tipos de esqueleto UM POR VEZ (Arsonist → Sniper → Frost Mage → Reaver) enquanto couber. Não precisa ter todos: cada um é +7% more dano com Muster."

    # ---------------------------------------------------------------- Início do Atlas
    p = PH["ea"]
    tag(find("ea", "Tame Beast (Mighty"), "core", 1, "~47% do Spirit")
    tag(find("ea", "Tame Beast (2º"), "core", 2, "~21–25% do Spirit")
    tag(find("ea", "Skeletal Warrior"), "core", 3, "Pouco Spirit (1 minion)")
    cl = find("ea", "Skeletal Cleric"); tag(cl, "core", 4, "Pouco Spirit (1 minion)")
    for name, pr in (("Skeletal Sniper", 1), ("Skeletal Reaver", 2)):
        g = find("ea", name); g["role"] = "Tipo extra (Muster) · opcional"; tag(g, "opt", pr, "Pouco Spirit (1 minion)")
    for s in ("Pain Offering", "Despair", "Sniper's Mark", "Refutation"):
        tag(find("ea", s), "free")
    tag(find("ea", "Wild Protector"), "free", 0, "Ascendência")
    p["spiritNote"] = "Ordem do Spirit no início do Atlas: 1) macaco → 2) beast de aura → 3) Skeletal Warrior → 4) Skeletal Cleric (revive e cura). Sniper e Reaver só se sobrar. Curses, marks, Pain Offering e Refutation não reservam Spirit."

    # ---------------------------------------------------------------- Endgame (Effigy): só marca o que é grátis
    for pid in ("t15", "mm"):
        for g in PH[pid]["gems"]:
            base = g["skill"]
            if base.startswith(("Pain Offering", "Voltaic Mark", "Mace Strike", "Refutation")):
                tag(g, "free")
            elif base.startswith("Wild Protector"):
                tag(g, "free", 0, "Ascendência")


    # ---------------------------------------------------------------- quantos esqueletos usar
    SK = {
     "a1": ("0", [], "Ainda sem minions: Twister faz o dano."),
     "a2": ("0", [], "Ainda sem esqueletos. Só o urso da ascendência (Wild Protector)."),
     "a3": ("1", ["Skeletal Warrior"], "Só 1 esqueleto vivo: ele existe para o Pain Offering espetar. Mais esqueletos não aumentam o dano do macaco nesta fase e tiram Spirit do 2º beast."),
     "a4": ("1", ["Skeletal Warrior OU Skeletal Arsonist"], "Continua 1 só. Com ~210 Spirit não cabe o segundo junto com Silverfist + aura + Withering Presence. Se você já usa o Arsonist, deixe o Warrior desligado."),
     "int": ("2 → até 5", ["Skeletal Warrior", "+ Skeletal Arsonist", "+ Skeletal Sniper", "+ Skeletal Frost Mage", "+ Skeletal Reaver"], "Comece com 2 (Warrior + Arsonist) depois do Lythara: libera o Danse Macabre. Depois adicione 1 de cada tipo, um por vez, enquanto couber no Spirit. O Muster conta TIPOS: 1 de cada tipo basta, repetir o mesmo tipo não dá mais dano."),
     "ea": ("2 → até 4", ["Skeletal Warrior", "Skeletal Cleric", "+ Skeletal Sniper (se couber)", "+ Skeletal Reaver (se couber)"], "Warrior e Cleric são obrigatórios (alvo do Pain Offering + cura/revive). Sniper e Reaver só se sobrar Spirit, 1 de cada."),
     "t15": ("1", ["Skeletal Cleric"], "O Rattling Sceptre sai para o Effigy, então sai o Warrior. Fica só o Cleric como alvo do Pain Offering (Sacrificial Lamb II + Tecrod's Revenge)."),
     "mm": ("1", ["Skeletal Cleric"], "Igual ao T15: só o Cleric. O resto do Spirit vai para companions."),
    }
    for pid, (n, types, note) in SK.items():
        PH[pid]["skeletons"] = {"n": n, "types": types, "note": note}

    # ---------------------------------------------------------------- limpeza de textos antigos (esqueletos)
    PH["a3"]["tag"] = "A troca: macaco + urso"
    PH["a3"]["carry"] = "Mighty Silverfist (+ urso + 1 esqueleto)"
    PH["a3"]["goal"] = "Capturar o Mighty Silverfist com The Natural Order e trocar a build inteira para minions no mesmo dia: Twister sai, entram macaco, urso, 1 Skeletal Warrior e Pain Offering."
    PH["int"]["goal"] = "Depois do Lythara (+40 Spirit), somar TIPOS de esqueleto para o Muster, um por vez e só enquanto couber no Spirit: cada tipo diferente = +7% more dano no macaco, e o 2º esqueleto libera o Danse Macabre. Vulnerability tira Armour."
    PH["int"]["exit"] = ["2+ tipos de esqueleto (quantos couberem no Spirit)" if x == "5 tipos de esqueleto ativos" else x for x in PH["int"]["exit"]]
    po = next(g for g in PH["t15"]["gems"] if g["skill"].startswith("Pain Offering"))
    po["why"] = "Brutus' Brain: o espinho não pode ser destruído, então o buff nunca cai. Danse Macabre só funciona com 2 esqueletos vivos: se você tiver só 1 Skeletal Cleric vivo, tire o Danse Macabre (os outros supports continuam valendo)."
    for t in TRICKS:
        if t["title"] == "Os 2 primeiros Skeletal Warriors são grátis":
            t["title"] = "Rattling Sceptre já traz o esqueleto"
    for o in OPTS:
        if o["t"] == "Esqueletos existem para o Muster e para o Pain Offering":
            o["ev"] = "Mattjestic (Ato 5) usa Warrior, Arsonist, Sniper, Frost Mage e Reaver sem supports de dano — mas só com Spirit sobrando. Entre um por vez."
            o["why"] = "Muster: +7% more dano para CADA tipo diferente de minion que revive. Cada tipo de esqueleto que couber no Spirit soma +7% no macaco e ainda serve de alvo do Pain Offering. 1 de cada tipo basta."
    for u in UNIQ:
        if u["n"] == "Enfolding Dawn":
            u["why"] = u["why"].replace("cabe mais um companion ou vários esqueletos", "cabe mais um companion (ou o beast de aura mais cedo)")

    # ---------------------------------------------------------------- textos que dependiam de 2 esqueletos
    MILESTONES[35] = "TROCA: tire Twister/Whirling. Entram 1 Skeletal Warrior (alvo do Pain Offering) + Pain Offering + Unearth."
    MILESTONES[40] = "Azak Bog: Ignagduk (+30 Spirit). Agora cabe o 2º beast (aura)."
    MILESTONES[46] = "Evergrasping Ring ×2 + Withering Presence. Spirit: Silverfist → aura → Withering Presence → 1 esqueleto."
    MILESTONES[56] = "Muster no macaco. Tipos de esqueleto extras (Arsonist, Sniper…) UM POR VEZ, só se couber no Spirit."
    MILESTONES[62] = "Kriar Village: Lythara (+40 Spirit). Agora cabem o 2º esqueleto (Danse Macabre) e mais tipos."
    for i, (q, a) in enumerate(TROUBLESHOOT):
        if q == "Pain Offering não dá buff":
            TROUBLESHOOT[i] = (q, "Ele precisa de um esqueleto vivo por perto (Warrior, Arsonist, Sniper ou Cleric) com Sacrificial Lamb. Danse Macabre precisa de 2 esqueletos: com 1 só, troque por Sacrificial Offering.")
    TROUBLESHOOT.append(("Não cabe tudo no Spirit", "Ative na ordem da aba Skills: macaco → beast de aura → Withering Presence → 1 esqueleto. Curses, marks, Pain Offering e Unearth não reservam Spirit. Se o painel mostrar Spirit negativo, desligue o último minion que entrou."))
    for it in CURRENT_SETUP["items"]:
        if it["what"].startswith("Pain Offering"):
            it["verdict"] = "Central na rota. Danse Macabre só funciona com 2 esqueletos vivos; com 1 esqueleto (Ato 3–4) use Sacrificial Offering no lugar. Brutus' Brain entra no endgame (o espinho não morre)."
    for t in TRICKS:
        if t["title"] == "Pain Offering sem cair no boss":
            t["body"] = "Brutus' Brain no Pain Offering deixa o espinho imune a dano, então o buff não some quando o boss acerta a área. Danse Macabre precisa de 2 esqueletos vivos: só coloque quando o Spirit permitir o 2º esqueleto (Interlúdios). Depois do Effigy, o Skeletal Cleric com Sacrificial Lamb II vira o alvo."


def cleanup(DATA):
    """Remove restos de rotas antigas (spear/Tyranny's Grip/Entangle) que contradiziam a rota Chober."""
    g = DATA["gear"]
    for row in g:
        if row["slot"] == "Main-hand":
            row["cheap"] = "Atos 1–2: spear rare (Twister). Ato 3: Rattling Sceptre (main) + Trenchtimbre. Início do Atlas: Chober Chaber Runeforged (~0,04 div)."
            row["value"] = "Chober Chaber Runeforged + Treefingers + The Vertex"
        if row["slot"] == "Offhand":
            row["cheap"] = "Atos 1–2: qualquer offhand. Ato 3+: Rattling Sceptre (base rare, traz Skeletal Warrior) com +Minion Skills"
        if row["slot"] == "Luvas":
            row["full"] = "Treefingers até ter Giant's Blood na árvore; depois rare de Evasion/Deflection com vida e resist"
    for t in DATA["tricks"]:
        if t["title"] == "Compre uniques já runeforged":
            t["body"] = "Chober Chaber Runeforged sai ≈ 0,04 div: bem mais barato do que juntar Verisium para fazer você mesmo."
        if t["title"] == "Catha's Balance: dano por golpe":
            t["body"] = "Companions ganham 60% do dano da main-hand. Compare armas pelo dano mínimo–máximo por golpe, não pelo DPS: a Chober Chaber bate devagar, mas tem o maior dano por golpe e ainda dá +Minion Skills e Spirit."
        if t["title"] == "Caçar sem matar sem querer":
            t["body"] = "Quando for capturar um beast raro, desligue temporariamente os companions e o urso (Wild Protector) — senão eles matam o beast antes do Tame Beast pegar."
        if t["title"] == "Compre o Tyranny's Grip cedo":
            t["title"] = "Compre a Chober Chaber cedo"
            t["body"] = "A Chober Chaber costuma custar poucos Exalts. Compre já Runeforged no Ato 3–4 e guarde: com a Catha's Balance ela vira a principal fonte de dano do zoo."
    DATA["tricks"] = [t for t in DATA["tricks"] if t["title"] != "Entangle é o seu botão principal"]
    for t in DATA["troubleshoot"]:
        if t["q"] == "Silverfist fraco no Ato 4":
            t["a"] = "Confira os supports do macaco: Feeding Frenzy II · Rage II · Rapid Attacks II · Heft (Muster só entra nos Interlúdios, quando tiver vários tipos de minion). Suba o nível da gem Tame Beast e use Sniper's Mark no boss."
    for a in DATA["atlasCheck"]:
        if "Tyranny" in a.get("gear", ""):
            a["gear"] = "Chober Chaber + Rattling Sceptre (ou Sylvan's Effigy)"
    for u in DATA["uniques"]:
        if u["n"] == "Tyranny's Grip":
            u["why"] = "Arma barata popular da Catha's Balance em OUTRAS builds de zoo (spear de 1 mão). NÃO é usada nesta rota: aqui a Chober Chaber faz esse papel e ainda dá +Minion Skills e Spirit."
            u["how"] = "Só considere se não usar a rota Chober Chaber."
            u["alt"] = "Chober Chaber (rota deste guia)."
            u["p"] = "mm"
    for p in DATA["phases"]:
        for gm in p["gems"]:
            if gm["skill"] == "Raise Shield":
                gm["why"] = "Só funciona com escudo ou buckler equipado. Com sceptre + maça (o set desta rota) ele não pode ser usado: deixe fora da barra se não tiver escudo."


def companion_limit(DATA):
    """Limite de companions confirmado no texto do jogo (tree.json 0.5 + poe.ninja):
    base 1 · Trusted Kinship ou Yriel's Fostering: 2 de tipos diferentes · Sylvan's Effigy: qualquer número."""
    ph = {p["id"]: p for p in DATA["phases"]}
    a4 = ph["a4"]
    a4["tag"] = "2 companions + chaos"
    a4["goal"] = "Macaco + 1 beast de aura (o limite do Trusted Kinship é 2 companions), marks e curse. Entram Evergrasping Ring (aliados ganham dano de chaos) e Withering Presence (inimigos recebem mais chaos): as duas peças se multiplicam."
    a4["exit"] = ["2 companions (macaco + aura)" if x == "3 companions" else x for x in a4["exit"]]
    for g in a4["gems"]:
        if g["skill"].startswith("Tame Beast (3º"):
            g["skill"] = "Tame Beast (3º beast: só com Sylvan's Effigy)"
            g["role"] = "Captura / guardar para o Effigy"
            g["why"] = "Com Trusted Kinship o limite é 2 companions de tipos diferentes (texto do keystone). O 3º só pode ficar ativo com o Sylvan's Effigy (\"any number of Companions\"). Até lá, use esta gem vazia só para capturar e guardar um Swarming Wisp / Plague Swarm com aura Physical."
            g["cost"] = "Só com Sylvan's Effigy"
    a4["spiritNote"] = a4["spiritNote"].replace("3º beast e 2º esqueleto só depois do Lythara (+40 Spirit).", "2º esqueleto só depois do Lythara (+40 Spirit). 3º beast só com Sylvan's Effigy: o Trusted Kinship limita a 2 companions.")
    for t in DATA["tricks"]:
        if t["title"] == "Rota de aura bots do Mattjestic":
            t["body"] = "Antes do Sylvan's Effigy só cabe 1 beast de aura (limite de 2 companions com Trusted Kinship). " + t["body"] + " Os beasts extras entram quando você equipar o Effigy."
    DATA["tricks"].insert(0, {"cat": "Captura", "lvl": "Fácil", "title": "Limite de companions",
        "body": "Base: 1 companion. Trusted Kinship (keystone) ou Yriel's Fostering (body): 2 companions de TIPOS diferentes — não somam entre si. Sylvan's Effigy: qualquer número de tipos diferentes. O urso do Wild Protector não conta no limite."})
    for o in DATA["optimizations"]:
        if "2–3 auras T1" in o.get("why", ""):
            o["why"] = o["why"].replace("O objetivo são 2–3 auras T1", "Com Sylvan's Effigy, o objetivo são 2–3 auras T1 (antes dele só cabe 1)")
    DATA["milestones"][86] = "Com Sylvan's Effigy: 3 aura bots (Haste/Physical/ES)."
    for x in ph["t15"]["exit"]:
        pass
    ph["t15"]["exit"] = ["3 aura bots (com Sylvan's Effigy)" if x == "3 aura bots" else x for x in ph["t15"]["exit"]]
    DATA["companionLimit"] = {"base": 1, "tk": 2, "effigy": None}
