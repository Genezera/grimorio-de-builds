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

def apply(PH, MILESTONES, TROUBLESHOOT, CURRENT_SETUP, TRICKS):
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
    third["why"] = "Só quando ganhar mais Spirit (Lythara +40 nos Interlúdios, capacete/amuleto com Spirit). Até lá, deixe a gem vazia só para capturar: Quill Crab e Coconut Crab aparecem no Whakapanu Island (Ato 4)."
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
