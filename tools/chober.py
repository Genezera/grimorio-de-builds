# -*- coding: utf-8 -*-
"""Rota CHOBER CHABER — baseada no guia do Mattjestic (Mobalytics, 0.5.5 Forbidden Rites), expandida com
explicações de cada skill/support/item, dados do poe.ninja e texto oficial das gems (PoE2DB)."""
import json, re
import meta as M
from meta import *  # noqa

GUIDE_URL = "https://mobalytics.gg/poe-2/builds/1-button-crossbow-amazon-mattjestic"

# ------------------------------------------------------------------ explicação de cada SUPPORT (texto do jogo → por que usar)
SUPWHY = {
 "Muster": "7% more dano para cada TIPO diferente de minion que revive (urso, macaco, cada esqueleto, wolf…). É por isso que a build tem vários tipos de esqueleto: cada tipo aumenta o dano do macaco.",
 "Feeding Frenzy II": "Minions causam 30% more dano e recebem 15% more dano. Só no companion de dano; nos de aura, não.",
 "Feeding Frenzy I": "Versão menor do Feeding Frenzy (menos dano, menos risco). Usado no Wolf Pack.",
 "Rage III": "O minion ganha Rage ao bater e ataca bem mais rápido enquanto não está no máximo de Rage.",
 "Rage II": "Versão de campanha do Rage: attack speed enquanto acumula Rage.",
 "Rage I": "Versão inicial do Rage.",
 "Rapid Attacks II": "+25% attack speed. Mais golpes = mais dano da Catha's Balance (60% da sua arma por golpe).",
 "Rapid Attacks III": "Versão mais forte do Rapid Attacks.",
 "Rapid Attacks I": "Attack speed para o companion no início.",
 "Heft": "30% more dano físico MÁXIMO dos hits. O macaco bate físico e com a Chober Chaber o dano por golpe é enorme — Heft multiplica justamente o topo do dano.",
 "Loyalty": "10% do dano que VOCÊ levaria vai para o companion (que perde 30% da vida). Nos companions de aura: eles viram escudo seu.",
 "Last Gasp": "O minion continua lutando 4 s depois de morrer. Mantém a aura do companion ativa por mais tempo.",
 "Meat Shield I": "Minion recebe menos dano e causa menos. Usado em quem só precisa sobreviver (esqueleto combustível, aura bot).",
 "Meat Shield II": "Minion recebe 40% less dano e causa 40% less. Perfeito para companion de aura: você quer a aura viva, não o dano dele.",
 "Minion Mastery": "+1 nível na gem do minion. Mais vida e dano sem custo extra.",
 "Elemental Army": "+30% resistências elementais para os minions. Aura bots morrem menos para dano elemental no endgame.",
 "Minion Splash II": "Minion ganha Melee Splash e +20% área: o golpe do urso/macaco acerta o pack inteiro.",
 "Magnified Area I": "+área nos golpes do urso. Barato e útil para limpar packs no início.",
 "Magnified Area II": "Mais área (usado no Mace Strike e no urso).",
 "Armour Break III": "Os golpes quebram Armour dos inimigos. Inimigo sem Armour recebe o dano físico inteiro do macaco.",
 "Armour Break I": "Quebra de Armour inicial.",
 "Sacrificial Lamb I": "Suas skills que miram minions (Pain Offering) escolhem ESTE esqueleto primeiro. Garante que o espinho nunca pegue o macaco ou o urso.",
 "Sacrificial Lamb II": "Mesma função com alcance de 6 m e o minion sempre conta como detonável.",
 "Amanamu's Tithe": "Quando um minion deste skill morre, 50% de chance de VOCÊ ganhar um modificador Abyssal por 20 s (até 3). Esqueletos morrem o tempo todo → buffs grátis.",
 "Danse Macabre": "Pain Offering espeta 2 esqueletos: +30% efeito do buff e 30% more dano. Precisa ter 2 esqueletos disponíveis.",
 "Prolonged Duration II": "35% more duração: o buff do Pain Offering / a curse / a mark duram mais.",
 "Prolonged Duration I": "Mais duração no início.",
 "Sacrificial Offering": "O Pain Offering sacrifica 15% da sua vida, mas o buff fica 30% mais forte e causa 30% more dano.",
 "Brutus' Brain": "O minion não recebe nem causa dano. No Pain Offering: o espinho não pode ser destruído, então o buff nunca cai no meio do boss.",
 "Tecrod's Revenge": "O minion luta 20 s depois de morrer, ganha Soul Eater e +40% velocidade. No Skeletal Cleric: ele continua curando e servindo de alvo do Pain Offering.",
 "Hulking Minions": "Minion Gigantic: maior, mais vida e dano, mas custa bem mais Spirit.",
 "Romira's Requital": "10% do dano dos hits vai para o urso e você RECUPERA 200% disso como vida. Defesa enorme de graça.",
 "Catha's Brilliance": "Inimigos perto do urso ficam Blind (erram mais) e pegam Ignite baseado na vida do urso.",
 "Infernal Legion I": "Minion e inimigos próximos pegam Ignite pela vida do minion (o minion toma dano de fogo). Dano de área extra.",
 "Infernal Legion II": "Versão mais forte do Infernal Legion.",
 "Minion Instability": "Minion explode com 15% da vida máxima ao ficar com vida baixa. Wolf Pack vira bombas.",
 "Withering Touch": "Chance de aplicar Wither (inimigo recebe mais dano de chaos). Combina com Evergrasping Ring e Uul-Netol's Embrace, que dão dano de chaos.",
 "Uul-Netol's Embrace": "40% do dano físico vira EXTRA como chaos, e o chaos quebra Armour. Multiplica o macaco com Wither.",
 "Dialla's Desire": "+1 nível e +5% qualidade na gem, e menos custo/reserva. Upgrade genérico de luxo.",
 "Life Leech III": "Leech de 16% do dano físico como vida (no companion).",
 "Einhar's Beastrite": "O Mace Strike só consegue matar inimigos com vida baixa, mas cada raro que ele finaliza te dá 2 modificadores dele por 300 s (ex.: Haste, Extra Damage). Não é dano: é roubar buffs.",
 "Culling Strike II": "Executa inimigos com vida baixa — casa com o Einhar's Beastrite, que só finaliza.",
 "Eternal Mark": "A mark não é consumida na primeira ativação: fica no boss por mais tempo.",
 "Mark for Death": "Hits no alvo marcado quebram Armour (10% do dano físico). Marca o boss e o macaco bate em alvo sem Armour.",
 "Mark for Death II": "Versão mais forte do Mark for Death.",
 "Cooldown Recovery II": "Recarga mais rápida (mark/Refutation disponível mais vezes).",
 "Efficiency II": "Menos custo de mana.",
 "Rapid Casting I": "Conjura mais rápido (curse sai antes).",
 "Rapid Casting II": "Conjura mais rápido.",
 "Heightened Curse": "+25% magnitude da curse (Despair/Vulnerability tiram mais resistência/Armour).",
 "Mobility": "Pode se mover enquanto usa a skill.",
 "Upwelling II": "Melhora a regeneração/recarga ligada à aura.",
 "Upwelling I": "Melhora a regeneração ligada à aura.",
 "Her Declaration": "Inimigos que entram na sua Presence ficam Intimidated (recebem mais dano). Custa 30 Spirit extra.",
 "Seraph's Heart": "20% de chance de o inimigo calcular o hit como se suas resistências fossem 90%. Defesa de luxo (45 Spirit extra).",
 "Clarity I": "Regeneração de mana.",
 "Furious Slam": "Skill de Bear socketada no Spirit Vessel: o Vessel vira urso e dá slams. Cada skill diferente socketada = +20% more dano do Vessel.",
 "Arctic Howl": "Skill de Werewolf socketada no Spirit Vessel: congela e dá dano de frio aos aliados.",
 "Devour": "Skill de Wyvern socketada no Spirit Vessel (versão endgame).",
 "Oil Barrage": "Skill de Wyvern socketada no Spirit Vessel.",
 "Salvo": "Skill socketada no Spirit Vessel.",
 "Living Lightning II": "Skill socketada no Spirit Vessel.",
 "Bleed I": "Chance de Bleed no Whirling Slash (leveling).",
 "Retreat III": "Twister: dano extra enquanto você se afasta (leveling).",
 "Elemental Armament III": "Twister: dano elemental extra (leveling).",
 "Projectile Acceleration I": "Twister mais rápido (leveling).",
 "Cold Attunement": "Herald of Ice com mais dano de frio (leveling).",
 "Concentrated Area": "Área menor, dano maior (leveling).",
 "Fortress I": "Flame Wall mais resistente (leveling minion).",
 "Profanity I": "Contagion com mais chaos (leveling minion).",
 "Fire Attunement": "Mais dano de fogo (leveling minion).",
 "Multishot I": "Mais projéteis (leveling minion).",
 "Multishot II": "Mais projéteis (leveling minion).",
 "Brutality I": "Mais dano físico (leveling).",
}

# ------------------------------------------------------------------ gems por fase (Mattjestic) + por quê
def G(skill, sup, role, why, set_="—", until=None):
    g = {"skill": skill, "set": set_, "sup": sup, "role": role, "why": why}
    if until: g["until"] = until
    return g

PH = {p["id"]: p for p in PHASES}

PH["a1"].update(
 tag="Twister (leveling)", carry="Você: Twister + Whirling Slash", dmgSplit=[100, 0],
 goal="Subir rápido com Twister. Nada de minion ainda: o foco é chegar ao Ato 3 com dinheiro e nível para trocar para o macaco + Chober Chaber.",
 rotation=["Whirling Slash até formar o redemoinho", "Twister atravessando o redemoinho (fica maior e mais forte)", "Parry para bloquear e contra-atacar bosses", "Spear Throw para puxar de longe"],
 gems=[
  G("Twister", ["Retreat III", "Elemental Armament III", "Projectile Acceleration I"], "Dano principal", "Twister é a skill de leveling mais rápida da Huntress: redemoinhos que atravessam packs inteiros."),
  G("Whirling Slash", ["Rapid Attacks I", "Rage II"], "Cria o redemoinho", "Cada Whirling Slash cria/aumenta um redemoinho; o Twister disparado por dentro dele ganha dano e tamanho."),
  G("Herald of Ice", ["Cold Attunement", "Concentrated Area"], "Clear extra", "Inimigos congelados explodem e limpam o resto do pack sem apertar nada."),
  G("Parry", [], "Defesa ativa", "Bloqueia o próximo golpe e deixa o inimigo vulnerável: salva de bosses do Ato 1–2."),
  G("Spear Throw", [], "Puxar de longe", "Vem da própria spear; útil para puxar packs."),
 ],
 cheap=["Rare spear com mais dano que cair", "Botas com Movement Speed", "Qualquer escudo/buckler com Evasion"],
 full=["Kit de uniques baratos do Mattjestic: Splinter of Lorrata → Skysliver (spear), Foxshade (body), 2× Blackheart (anéis), Goldrim (capacete), Wanderlust (botas), Meginord's Girdle, Surefooted Sigil", "Todos custam poucos Exalts no trade e fazem o Ato 1–2 voar"],
 stats=["Movement Speed", "Vida", "Resistências", "Dano da spear"],
 tree="Nós de Twister/projétil perto do início da Huntress. É a única fase em que dano de ataque do jogador faz sentido.",
 avoid=["Gastar pontos em minion agora", "Comprar gear caro para o Twister: ele sai da barra no Ato 3"],
 exit=["King in the Mists (+30 Spirit)", "Candlemass (+20 vida)", "Botas com MS", "Nível ~16"],
)
PH["a2"].update(
 tag="1ª Ascendência", carry="Você: Twister + urso", dmgSplit=[85, 15],
 goal="Wild Protector na 1ª Ascendência e juntar gold/currency para a troca do Ato 3 (Chober Chaber, The Vertex, Treefingers, Rattling Sceptre).",
 rotation=["Mesma rotação de Twister", "O urso segura o aggro dos bosses"],
 gems=[
  G("Wild Protector", ["Magnified Area I", "Rage II"], "Tank + dano extra", "O urso não conta no limite de companions: é um minion grátis que segura bosses e dá Intimidate.", "Asc."),
  G("Twister", ["Retreat III", "Elemental Armament III", "Projectile Acceleration I"], "Dano principal", "Continua sendo o dano até capturar o macaco."),
  G("Whirling Slash", ["Rapid Attacks I", "Bleed I"], "Redemoinho", "Bleed no Whirling ajuda nos bosses."),
  G("Parry", [], "Defesa ativa", "Continua útil até o Ato 3."),
  G("Spear Throw", [], "Puxar de longe", "Vem da spear."),
 ],
 cheap=["Rare spear + botas com MS", "Meginord's Girdle se faltar Strength"],
 full=["Skysliver (spear) · Foxshade · 2× Blackheart · Goldrim · Wanderlust · Surefooted Sigil · Meginord's Girdle", "Comece a guardar para: Chober Chaber (~2 ex), Treefingers (~5 ex), Rattling Sceptre (qualquer), The Vertex versão 'Equipment' (~0,4 div)"],
 stats=["Movement Speed", "Vida", "Resistências", "Spirit"],
 tree="Ainda Twister, mas já caminhe para o lado de companion da árvore para o respec do Ato 3 ficar barato.",
 avoid=["Gastar todo o gold: o respec do Ato 3 é caro"],
 exit=["1ª Ascendência: Wild Protector", "Medallion (+1 Charm Slot)", "Currency guardada para a troca"],
)
PH["a3"].update(
 tag="A troca: macaco + esqueletos", carry="Mighty Silverfist (+ urso + esqueletos)", dmgSplit=[5, 95],
 goal="Capturar o Mighty Silverfist com The Natural Order e trocar a build inteira para minions no mesmo dia: Twister sai, entram macaco, urso, Skeletal Warriors e Pain Offering.",
 rotation=["Entre no pack e deixe o macaco e o urso baterem", "Unearth no chão: cria Bone Constructs e quebra Armour (Armour Break III)", "Pain Offering em cima do boss (espeta um Skeletal Warrior): +velocidade e +dano para todos os minions por 6 s", "Raise Shield se o boss for dar um golpe grande"],
 gems=[
  G("Tame Beast (Mighty Silverfist)", ["Feeding Frenzy II", "Rage II", "Rapid Attacks I", "Heft"], "CARRY", "O macaco é o dano da build inteira: bate físico em área, muito rápido, com 25% de chance de crítico base. Tudo abaixo existe para deixá-lo mais forte ou mais vivo."),
  G("Wild Protector", ["Magnified Area I"], "Tank", "Segura o aggro e conta como mais um TIPO de minion para o Muster.", "Asc."),
  G("Skeletal Warrior", ["Sacrificial Lamb I", "Meat Shield I"], "Combustível do Pain Offering", "Vem como gem do Rattling Sceptre. Não é para dar dano: é o esqueleto que o Pain Offering espeta. Sacrificial Lamb garante que ele seja escolhido e Meat Shield mantém ele vivo."),
  G("Pain Offering", ["Danse Macabre", "Prolonged Duration II"], "Buff de dano dos minions", "Espeta um esqueleto: minions a até 6 m ganham até +29% attack speed e +58% dano. Com Danse Macabre (2 esqueletos) o buff fica 30% mais forte. Não custa Spirit, só mana."),
  G("Unearth", ["Armour Break III"], "Quebra de Armour + corpos", "Spell sua que cria Bone Constructs dos corpos e, com Armour Break III, tira Armour do inimigo: o macaco passa a bater o dano físico inteiro."),
  G("Raise Shield", [], "Defesa ativa", "Bloqueia tudo enquanto segura. Precisa de escudo ou de um item que permita (substitui o Parry)."),
  G("Tame Beast (2º beast: aura)", ["Last Gasp", "Loyalty"], "Aura bot", "Segundo companion permitido pelo Trusted Kinship. Escolha pelo modificador de aura (Haste/Physical), não pelo dano. Last Gasp mantém a aura viva, Loyalty faz ele tomar parte do seu dano."),
  G("Tame Beast (vazia)", [], "Captura", "Deixe uma gem de Tame Beast livre para capturar o próximo beast com mod bom."),
  G("Twister", ["Retreat III", "Elemental Armament III"], "Só até capturar", "Tire da barra no respec.", until=35),
  G("Whirling Slash", ["Rapid Attacks I", "Bleed I"], "Só até capturar", "Tire da barra no respec.", until=35),
 ],
 cheap=["Rattling Sceptre (main) + Trenchtimbre (offhand) — exatamente como o Mattjestic", "Midnight Braid (cinto) · Foxshade/Wanderlust/Blackheart mantidos", "Meginord's Girdle se faltar Strength"],
 full=["Chober Chaber + Rattling Sceptre (com Treefingers dando Giant's Blood)", "The Vertex versão 'Equipment has no Attribute Requirements' para zerar os requisitos triplicados", "Enfolding Dawn (+100 Spirit no body) para caber mais minions"],
 stats=["+Minion Skills", "Spirit", "Movement Speed", "Vida", "Resistências"],
 tree="Árvore do Mattjestic (Ato 3): Trusted Kinship, Bond of the Mamba, Bond of the Cat, Unspoken Bond, e defesa de Evasion (Blur, Catlike Agility, Escape Velocity). Zero nós de ataque.",
 avoid=["Matar o Silverfist antes de ter The Natural Order", "Manter Twister/Whirling depois da troca", "Ball Lightning / Lightning Warp: não fazem nada pelo macaco"],
 exit=["Silverfist capturado", "Twister fora da barra", "Pain Offering + Skeletal Warrior funcionando", "Ignagduk (+30 Spirit)"],
)
PH["a4"].update(
 tag="3 companions + chaos", carry="Silverfist (+ aura bots)", dmgSplit=[0, 100],
 goal="Terceiro companion, marks e curse. Entram Evergrasping Ring (aliados ganham dano de chaos) e Withering Presence (inimigos recebem mais chaos): as duas peças se multiplicam.",
 rotation=["Sniper's Mark no boss (com Mark for Death: quebra Armour)", "Pain Offering em cima do boss", "Unearth para mais corpos/Armour Break", "Deixe o zoo bater"],
 gems=[
  G("Tame Beast (Mighty Silverfist)", ["Feeding Frenzy II", "Rage II", "Rapid Attacks II", "Heft"], "CARRY", "Rapid Attacks sobe para II: mais golpes por segundo."),
  G("Wild Protector", ["Magnified Area I", "Armour Break III"], "Tank + Armour Break", "O urso também passa a quebrar Armour, somando com o Unearth.", "Asc."),
  G("Skeletal Warrior", ["Sacrificial Lamb I", "Amanamu's Tithe"], "Combustível", "Amanamu's Tithe: cada esqueleto que morre pode te dar um modificador Abyssal por 20 s."),
  G("Pain Offering", ["Danse Macabre", "Prolonged Duration II"], "Buff de dano", "Continua sendo o botão de boss."),
  G("Withering Presence", [], "Wither em área", "Inimigos na sua Presence recebem Wither (mais dano de chaos). Sozinha seria fraca, mas com Evergrasping Ring o zoo inteiro bate chaos extra."),
  G("Sniper's Mark", ["Mark for Death", "Prolonged Duration II"], "Marca o boss", "Mark for Death faz os hits no alvo marcado quebrarem Armour."),
  G("Unearth", ["Prolonged Duration I"], "Corpos + controle", "Bone Constructs duram mais."),
  G("Tame Beast (2º beast: aura)", ["Loyalty", "Last Gasp"], "Aura bot", "Aura de Haste/Physical."),
  G("Tame Beast (3º beast)", [], "Aura bot / captura", "Vaga para o próximo beast (Quill Crab e Coconut Crab aparecem no Whakapanu Island, Ato 4, e custam só ~25% de Spirit)."),
  G("Raise Shield", [], "Defesa ativa", "Bloqueio."),
 ],
 cheap=["Rattling Sceptre + Trenchtimbre", "Evergrasping Ring ×2 (aliados ganham 15–25% do dano como chaos)", "Enfolding Dawn (+100 Spirit) · Bushwhack (botas) · Midnight Braid", "Charms contra bleed/ignite"],
 full=["Chober Chaber + Rattling Sceptre + Treefingers + The Vertex", "Evergrasping Ring ×2 · Enfolding Dawn · Bushwhack", "Primeiro Quill/Coconut Crab com Haste Aura"],
 stats=["+Minion Skills", "Spirit", "Vida", "Resistências", "Movement Speed"],
 tree="Árvore do Mattjestic (Ato 4): Easy Going, Inspiring Ally, Bond of the Wolf somam aos Bonds do Ato 3.",
 avoid=["Trocar Evergrasping Ring por rare de resist sem repor o chaos: o Wither perde sentido", "Pegar nós de ataque para você"],
 exit=["3 companions", "Evergrasping Ring ×2 + Withering Presence", "Testes de resistência do Ato 4 feitos"],
)
PH["int"].update(
 tag="Esqueletos para o Muster", carry="Silverfist + zoo", dmgSplit=[0, 100],
 goal="Somar vários TIPOS de esqueleto (Frost Mage, Arsonist, Sniper, Reaver) só para o Muster: cada tipo diferente = +7% more dano no macaco. Vulnerability tira Armour.",
 rotation=["Vulnerability no pack/boss", "Pain Offering", "Deixe o zoo bater"],
 gems=[
  G("Tame Beast (Mighty Silverfist)", ["Feeding Frenzy II", "Rage II", "Rapid Attacks II", "Heft", "Muster"], "CARRY", "Entra o 5º support: Muster. Com urso + macaco + aura bots + 5 tipos de esqueleto, são ~9 tipos → ~+63% more dano."),
  G("Wild Protector", ["Magnified Area I", "Armour Break III", "Minion Splash II"], "Tank + área", "Minion Splash: o urso acerta o pack todo.", "Asc."),
  G("Skeletal Warrior", ["Sacrificial Lamb II", "Amanamu's Tithe"], "Combustível", "Sacrificial Lamb II (6 m)."),
  G("Skeletal Frost Mage", [], "Tipo extra (Muster)", "Não use supports: está aqui para contar como mais um tipo de minion."),
  G("Skeletal Arsonist", [], "Tipo extra (Muster)", "Mais um tipo de minion para o Muster."),
  G("Skeletal Sniper", [], "Tipo extra (Muster)", "Mais um tipo. Reserva pouco Spirit no nível alto (30 no nv 20)."),
  G("Skeletal Reaver", [], "Tipo extra (Muster)", "Mais um tipo; também quebra Armour."),
  G("Vulnerability", ["Prolonged Duration II", "Heightened Curse"], "Curse", "Inimigos amaldiçoados ignoram parte da Armour: o macaco (físico) bate cheio."),
  G("Pain Offering", ["Danse Macabre", "Prolonged Duration II"], "Buff de dano", "Com vários esqueletos, sempre há 2 para o Danse Macabre."),
  G("Withering Presence", [], "Wither", "Continua com Evergrasping Ring."),
  G("Tame Beast (2º beast: aura)", ["Loyalty", "Last Gasp"], "Aura bot", "Aura."),
 ],
 cheap=["Trenchtimbre na main-hand + Rattling Sceptre no offhand", "Enfolding Dawn · Bushwhack · Evergrasping Ring ×2 · Meginord's Girdle", "Capacete Runeforged (Elite Greathelm) para Runic Ward"],
 full=["Chober Chaber + Rattling Sceptre + Treefingers + The Vertex", "Enfolding Dawn · Bushwhack · Evergrasping Ring ×2", "Ventor's Gamble se sobrar dinheiro"],
 stats=["+Minion Skills", "Spirit", "Vida", "Resistências (cap 75%)", "Movement Speed"],
 tree="Árvore do Mattjestic (Ato 5): adiciona Bond of the Owl.",
 avoid=["Colocar supports de dano nos esqueletos: eles existem para o Muster e para o Pain Offering", "Entrar no Atlas com resists abaixo de 75%"],
 exit=["5 tipos de esqueleto ativos", "Muster no macaco", "Lythara (+40 Spirit)", "Resists no cap"],
)
PH["ea"].update(
 tag="Catha's Balance + mapping", carry="Macaco (Silverfist/Zekoa) + zoo", dmgSplit=[0, 100],
 goal="The Catha's Balance transforma o dano da SUA arma em dano dos companions (60% por golpe). É aqui que a Chober Chaber vira o centro: maça de 2 mãos com dano base altíssimo, +Minion Skills e +50 Spirit.",
 rotation=["Despair no pack (tira resistência a chaos)", "Sniper's Mark no boss", "Pain Offering", "Refutation antes de um golpe grande (gasta Runic Ward e bloqueia tudo)"],
 gems=[
  G("Tame Beast (Mighty Silverfist → Zekoa)", ["Feeding Frenzy II", "Rage III", "Rapid Attacks II", "Heft", "Muster"], "CARRY", "Com a Catha, cada golpe do macaco ganha 60% do dano da Chober Chaber. Rage III e Rapid Attacks II = mais golpes; Heft = golpes maiores."),
  G("Wild Protector", ["Magnified Area I", "Armour Break III", "Minion Splash II", "Minion Mastery"], "Tank + Armour Break", "Também recebe a Catha's Balance.", "Asc."),
  G("Skeletal Warrior", ["Amanamu's Tithe", "Sacrificial Lamb II", "Meat Shield I"], "Combustível", "Continua vindo do Rattling Sceptre."),
  G("Pain Offering", ["Danse Macabre", "Prolonged Duration II", "Sacrificial Offering"], "Buff de dano", "Sacrificial Offering: sacrifica 15% da sua vida por +30% efeito e 30% more dano."),
  G("Skeletal Sniper", [], "Tipo extra (Muster)", "Tipo de minion para o Muster."),
  G("Skeletal Reaver", [], "Tipo extra (Muster)", "Tipo de minion para o Muster."),
  G("Skeletal Cleric", [], "Cura + revive esqueletos", "Revive os esqueletos que o Pain Offering consome e cura o zoo. Também é esqueleto: serve de alvo do Pain Offering."),
  G("Despair", ["Prolonged Duration II", "Heightened Curse", "Rapid Casting I"], "Curse de chaos", "Tira até 49% de resistência a chaos: o chaos do Evergrasping Ring bate muito mais."),
  G("Tame Beast (2º beast: aura)", ["Last Gasp", "Magnified Area I", "Meat Shield I"], "Aura bot", "Meat Shield: ele só precisa sobreviver com a aura."),
  G("Sniper's Mark", ["Mark for Death"], "Marca", "Quebra Armour do alvo."),
  G("Refutation", ["Prolonged Duration II", "Cooldown Recovery II", "Efficiency II", "Rapid Casting II"], "Defesa ativa", "Gasta todo o seu Runic Ward para bloquear TODOS os hits por um tempo. Runic Ward vem de itens Runeforged/Runemastered — por isso o Mattjestic usa armaduras Runeforged."),
 ],
 cheap=["Trenchtimbre + Rattling Sceptre até juntar para a Chober Chaber", "Evergrasping Ring ×2 · armaduras Runeforged (Runic Ward para o Refutation)", "Jewels: From Nothing · Undying Hate"],
 full=["Chober Chaber (Runeforged) + Rattling Sceptre + Treefingers + The Vertex", "Sylvan's Effigy assim que tiver ~1 div (substitui o Rattling Sceptre)", "From Nothing · Undying Hate"],
 stats=["Dano base da main-hand (Catha)", "+Minion Skills", "Spirit", "Vida", "Resistências", "Runic Ward"],
 tree="Árvore do Mattjestic (Mapping T1-10): Sturdy Ally, Captivating Companionship, Sic 'Em, The Howling Primate, The Fabled Stag, Enhanced Reflexes.",
 avoid=["Julgar a arma pelo DPS: com Catha vale o dano por golpe (a Chober Chaber bate devagar e é a melhor)", "Tirar os esqueletos antes do Effigy"],
 exit=["Catha's Balance", "Chober Chaber equipada", "T1–T10 sem mortes", "Juntar ~1 div para o Effigy"],
)
PH["t15"].update(
 tag="Chober + Giant's Blood + Effigy", carry="Zekoa + Azmerian Wolf + zoo", dmgSplit=[0, 100],
 goal="Giant's Blood na árvore (maça de 2 mãos + sceptre), Sylvan's Effigy (companions ilimitados + Azmerian Wolf), Forgotten Warden (Spirit Vessel grátis). Os esqueletos saem, porque o Rattling Sceptre dá lugar ao Effigy. O Skeletal Cleric vira o alvo do Pain Offering.",
 rotation=["Mace Strike (Einhar's Beastrite) finalizando raros: rouba 2 modificadores por 300 s", "Voltaic Mark no boss", "Pain Offering (Brutus' Brain: o espinho não morre)", "Refutation antes do golpe grande", "O resto é automático"],
 gems=[
  G("Tame Beast (Zekoa, the Headcrusher)", ["Feeding Frenzy II", "Rage III", "Muster", "Heft", "Rapid Attacks II"], "CARRY", "A versão de Atlas do Silverfist (mapas Riverside/Rupture) pode ter mais modificadores."),
  G("Azmerian Wolf", ["Feeding Frenzy II", "Rapid Attacks II", "Rage III", "Hulking Minions", "Loyalty"], "2º dano", "Vem do Sylvan's Effigy. Hulking Minions deixa o lobo Gigantic (mais vida e dano).", "Effigy"),
  G("Wild Protector", ["Hulking Minions", "Feeding Frenzy II", "Muster", "Romira's Requital", "Catha's Brilliance"], "Tank + sustain", "Romira's Requital: o urso toma 10% do seu dano e você recupera 200% disso como vida. Catha's Brilliance: blind + ignite em volta dele.", "Asc."),
  G("Spirit Vessel", ["Loyalty", "Furious Slam", "Arctic Howl", "Rapid Attacks II", "Rage III"], "Companion grátis", "Vem do Forgotten Warden. Furious Slam (Bear) e Arctic Howl (Werewolf) socketados: +20% more dano por skill diferente."),
  G("Wolf Pack", ["Rapid Attacks II", "Feeding Frenzy II", "Loyalty", "Rage III", "Withering Touch"], "Corpos + Wither", "Vários lobos contam como um companion. Withering Touch aplica Wither para o chaos."),
  G("Pain Offering", ["Danse Macabre", "Prolonged Duration II", "Sacrificial Offering", "Brutus' Brain"], "Buff de dano", "Brutus' Brain: o espinho não pode ser destruído, então o buff nunca cai."),
  G("Skeletal Cleric", ["Sacrificial Lamb II", "Tecrod's Revenge", "Meat Shield II", "Elemental Army"], "Alvo do Pain Offering", "Sem Rattling Sceptre, o Cleric é o esqueleto espetado (Sacrificial Lamb II). Tecrod's Revenge mantém ele lutando 20 s depois de morrer."),
  G("Voltaic Mark", ["Cooldown Recovery II", "Eternal Mark", "Mark for Death II", "Prolonged Duration II"], "Marca o boss", "Eternal Mark: não é consumida na primeira ativação. Mark for Death II: quebra Armour."),
  G("Mace Strike", ["Einhar's Beastrite", "Culling Strike II", "Rage III", "Rapid Attacks II", "Magnified Area II"], "Rouba modificadores", "Vem da Chober Chaber. Não é dano: só finaliza inimigos com vida baixa, e cada raro finalizado te dá 2 modificadores dele (Haste, Extra Damage…) por 5 minutos."),
  G("Tame Beast (auras ×3)", ["Loyalty", "Rage III", "Muster", "Feeding Frenzy II", "Rapid Attacks II"], "Aura bots", "3 beasts de aura (Haste/Physical/ES/Invulnerability). No Tier-list do Mattjestic: Quill/Coconut Crab (24,9%), Swarming Wisp (21%), Crag Leaper (23,1%)."),
  G("Discipline", [], "Aura de ES", "Vem do Effigy.", "Effigy"),
  G("Sanguine Revelry", [], "Rage + vida", "Vem do Spiteful Floret no weapon set 2: Remnants de inimigos com bleed dão Rage e vida."),
  G("Refutation", ["Prolonged Duration II", "Cooldown Recovery II", "Efficiency II", "Rapid Casting II", "Mobility"], "Defesa ativa", "Mobility: pode andar enquanto o buff está ativo."),
 ],
 cheap=["Chober Chaber + Sylvan's Effigy", "Forgotten Warden · Lavianga's Spirits", "Spiteful Floret no weapon set 2 (Sanguine Revelry)", "Jewels: Controlled Metamorphosis · Megalomaniac · From Nothing"],
 full=["Mesmo set + Idolatry com Idols em tudo", "Prism of Belief +2/+3 Tamed Companion", "Morior Invictus se preferir tank"],
 stats=["Dano base da Chober Chaber", "+Minion Skills", "Spirit", "Evasion/Deflection", "Resistências", "Atributos (Giant's Blood triplica requisitos)"],
 tree="Árvore do Mattjestic (Giant's Blood Endgame): Giant's Blood, Polymathy (atributos), Enduring/Avoiding Deflection, Long Distance Relationship, The Winter Owl.",
 avoid=["Tirar Trusted Kinship", "Pegar Idolatry enquanto depende de runas de resistência"],
 exit=["Giant's Blood + Chober + Effigy", "Zekoa com Extra Crits/Haste", "3 aura bots", "Forgotten Warden + Spirit Vessel"],
)
PH["mm"].update(
 tag="Mind Over Matter + 27 companions", carry="Zoo inteiro", dmgSplit=[0, 100],
 goal="Endgame do Mattjestic: Mind Over Matter (dano sai da mana primeiro), Mageblood e até 27 companions. O macaco vira o único DPS 'puro'; os outros são aura bots super defensivos.",
 rotation=["Mace Strike finalizando raros", "Voltaic Mark", "Refutation", "Deixe o zoo"],
 gems=[
  G("Tame Beast (Zekoa, the Headcrusher)", ["Rage III", "Muster", "Heft", "Feeding Frenzy II", "Rapid Attacks II"], "CARRY (bossing)", "Setup de boss. Para mapear, troque Heft/Feeding Frenzy/Rapid Attacks por Minion Splash II + Infernal Legion I + Tecrod's Revenge (dano em área)."),
  G("Azmerian Wolf", ["Loyalty", "Rage III", "Muster", "Feeding Frenzy II", "Rapid Attacks II"], "2º dano", "Loyalty no lugar de Hulking Minions: menos Spirit.", "Effigy"),
  G("Wild Protector", ["Romira's Requital", "Rage III", "Muster", "Rapid Attacks II", "Catha's Brilliance"], "Tank + sustain", "Romira's Requital continua sendo a maior fonte de vida.", "Asc."),
  G("Spirit Vessel", ["Loyalty", "Devour", "Oil Barrage", "Salvo", "Living Lightning II"], "Companion grátis", "4 skills diferentes socketadas = +80% more dano do Vessel."),
  G("Wolf Pack", ["Loyalty", "Elemental Army", "Infernal Legion I", "Withering Touch", "Amanamu's Tithe"], "Corpos + Wither + buffs", "Amanamu's Tithe: lobos morrendo te dão modificadores Abyssal."),
  G("Tame Beast (auras ×5)", ["Loyalty", "Last Gasp", "Elemental Army", "Meat Shield II", "Minion Mastery"], "Aura bots", "Setup 100% defensivo: só precisam manter a aura viva."),
  G("Voltaic Mark", ["Cooldown Recovery II", "Prolonged Duration II", "Mark for Death II", "Eternal Mark"], "Marca", "Igual ao T15."),
  G("Mace Strike", ["Einhar's Beastrite", "Culling Strike II", "Rage III", "Rapid Attacks III", "Magnified Area II"], "Rouba modificadores", "Igual ao T15."),
  G("Discipline", ["Upwelling II"], "Aura de ES", "Vem do Effigy.", "Effigy"),
  G("Sanguine Revelry", [], "Rage + vida", "Vem do Spiteful Floret."),
  G("Refutation", ["Prolonged Duration II", "Cooldown Recovery II", "Efficiency II", "Rapid Casting II", "Mobility"], "Defesa ativa", "Igual ao T15."),
 ],
 cheap=["Setup do T15 + Mind Over Matter (Lavianga's Spirits sustenta)", "Charms: The Fall of the Axe · Nascent Hope · Beira's Anguish"],
 full=["Mageblood · Kalandra's Touch · Rite of Passage", "Runeforged Pariah Mask · Drakeskin Boots · Barbed Bracers (rares/runeforged do Mattjestic)", "Variante 12m: Morior Invictus + 2× Chober Chaber (weapon swap)"],
 stats=["Mana (Mind Over Matter)", "+Minion Skills", "Spirit", "Evasion/Deflection", "Resistências"],
 tree="Árvore do Mattjestic (Endgame Mapping): Mind Over Matter, The Soul Meridian, Beastial Skin, The Wild Cat, Lifelong Friend.",
 avoid=["Mind Over Matter sem mana alta (Chober +100 mana, Lavianga's)"],
 exit=["Arbiter", "Uber Arbiter"],
)

MILESTONES.clear()
MILESTONES.update({
 1: "Twister + Whirling Slash. Spear rare ou Splinter of Lorrata.",
 4: "Twister liberado. Herald of Ice quando tiver Spirit.",
 8: "Hunting Grounds: The Crowbell (2 weapon set points).",
 10: "Freythorn: King in the Mists (+30 Spirit).",
 14: "Ogham Manor: Candlemass (+20 vida).",
 16: "Skysliver (spear) se for no modo completo.",
 20: "Trial of the Sekhemas → Wild Protector.",
 25: "Valley of the Titans: Medallion (+1 Charm Slot).",
 28: "Comece a guardar currency para a troca do Ato 3.",
 30: "Compre: Rattling Sceptre + Trenchtimbre (barato) ou Chober Chaber + Treefingers + The Vertex (completo).",
 32: "Jungle Ruins: NÃO mate o Silverfist ainda.",
 33: "Trial of Chaos → The Natural Order.",
 34: "Capture o Mighty Silverfist. Respec completo para minion.",
 35: "TROCA: tire Twister/Whirling. Entram Skeletal Warrior + Pain Offering + Unearth.",
 40: "Azak Bog: Ignagduk (+30 Spirit). 2º beast de aura.",
 46: "Evergrasping Ring ×2 + Withering Presence (sinergia de chaos).",
 48: "Whakapanu Island: capture Quill/Coconut Crab com aura (~25% Spirit).",
 52: "Sniper's Mark + Mark for Death no boss.",
 55: "Tribal Medicine: Evasion como Deflection.",
 56: "Muster no macaco. Adicione Frost Mage/Arsonist/Sniper/Reaver (tipos para o Muster).",
 58: "Vulnerability (curse) + Heightened Curse.",
 62: "Kriar Village: Lythara (+40 Spirit).",
 65: "The Catha's Balance: o dano da sua arma vira dano dos companions.",
 66: "Chober Chaber na main-hand (se ainda estava na Trenchtimbre).",
 68: "Despair + Skeletal Cleric + Refutation (armaduras Runeforged).",
 72: "Caça ao Zekoa (Riverside/Rupture + tablets de mod extra).",
 75: "Giant's Blood na árvore (ou Flesh Crucible) — solte a Treefingers se quiser outras luvas.",
 78: "Sylvan's Effigy (~1 div): Azmerian Wolf, Discipline, companions ilimitados.",
 80: "Forgotten Warden: Spirit Vessel com Furious Slam + Arctic Howl.",
 82: "Skeletal Cleric vira alvo do Pain Offering (Sacrificial Lamb II + Brutus' Brain no Pain Offering).",
 84: "Mace Strike + Einhar's Beastrite; Spiteful Floret no weapon set 2.",
 86: "3 aura bots (Haste/Physical/ES).",
 90: "Mind Over Matter + Lavianga's Spirits.",
 95: "Mageblood / Kalandra's Touch (luxo).",
 100: "Uber Arbiter.",
})

# ------------------------------------------------------------------ beasts (tier-list Mattjestic)
BEASTS[:] = [
 {"name": "Mighty Silverfist / Zekoa", "where": "Ato 3 Jungle Ruins / mapas Riverside e Rupture", "role": "Único DPS de verdade", "cost": 47.4, "tier": "S+", "mods": "Extra Crits · Hasted · Extra Damage as Chaos/Physical", "sup": "Feeding Frenzy II · Rage III · Muster · Heft · Rapid Attacks II", "req": "Tame Beast + The Natural Order"},
 {"name": "Quill Crab (Porcupine)", "where": "Ato 4 Whakapanu Island (essence e raros na praia)", "role": "Aura bot barato", "cost": 24.9, "tier": "S", "mods": "Haste Aura (o mais fácil de achar)", "sup": "Loyalty · Last Gasp · Elemental Army · Meat Shield II · Minion Mastery", "req": "Tame Beast"},
 {"name": "Coconut Crab", "where": "Ato 4 Whakapanu Island", "role": "Aura bot barato", "cost": 24.9, "tier": "S", "mods": "Haste / Physical Aura", "sup": "Loyalty · Last Gasp · Elemental Army · Meat Shield II · Minion Mastery", "req": "Tame Beast"},
 {"name": "Swarming Wisp", "where": "Ato 5 Ashen Forest (essence)", "role": "Aura bot mais barato", "cost": 21.0, "tier": "S", "mods": "Qualquer aura T1 exceto Haste", "sup": "Loyalty · Last Gasp · Elemental Army · Meat Shield II · Minion Mastery", "req": "Tame Beast"},
 {"name": "Plague Swarm", "where": "Ato 2 Mawdun Quarry (essence)", "role": "Aura bot mais barato", "cost": 21.0, "tier": "A+", "mods": "Aura T1", "sup": "Loyalty · Last Gasp · Elemental Army · Meat Shield II · Minion Mastery", "req": "Tame Beast"},
 {"name": "Crag Leaper", "where": "Ato 2 Vastiri Outskirts (essence)", "role": "Aura bot", "cost": 23.1, "tier": "A+", "mods": "Aura T1 (NUNCA Haste: é very_fast_movement)", "sup": "Loyalty · Last Gasp · Elemental Army · Meat Shield II · Minion Mastery", "req": "Tame Beast"},
 {"name": "Bramble Ape", "where": "Ato 5 Kriar Village", "role": "Aura bot", "cost": 24.9, "tier": "A", "mods": "Aura T1", "sup": "Loyalty · Last Gasp · Elemental Army · Meat Shield II · Minion Mastery", "req": "Tame Beast"},
 {"name": "Rasp Scavenger", "where": "Ato 5 Khari Crossing (essence)", "role": "Aura bot reserva", "cost": 26.7, "tier": "A", "mods": "Aura T1", "sup": "Loyalty · Last Gasp · Elemental Army · Meat Shield II · Minion Mastery", "req": "Tame Beast"},
 {"name": "Diretusk Boar", "where": "Ato 3 Infested Barrens (garantido)", "role": "Companion de campanha", "cost": 39.0, "tier": "A", "mods": "Qualquer", "sup": "Loyalty · Muster · Rapid Attacks II · Minion Mastery", "req": "Tame Beast"},
 {"name": "Antlion Charger", "where": "Ato 3 Infested Barrens (garantido)", "role": "Companion de campanha (setup de 3 do Mattjestic)", "cost": 42.3, "tier": "A", "mods": "Qualquer", "sup": "Loyalty · Last Gasp", "req": "Tame Beast"},
 {"name": "Azmerian Wolf", "where": "Vem no Sylvan's Effigy", "role": "2º dano", "cost": None, "tier": "S", "mods": "—", "sup": "Feeding Frenzy II · Rapid Attacks II · Rage III · Hulking Minions/Muster · Loyalty", "req": "Sylvan's Effigy"},
]
AURA_PRIORITY[:] = ["Extra Physical ou Haste Aura", "Energy Shield ou Invulnerability Aura", "Temporal Bubble", "Elemental Resistance Aura"]

# ------------------------------------------------------------------ uniques extras do guia
EXTRA_U = [
 {"n": "Enfolding Dawn", "slot": "Body Armour", "cat": "Armadura", "lvl": 1, "p": "a4", "use": None, "rf": "",
  "why": "+100 Spirit num body de nível 1. É o maior ganho de Spirit da campanha: cabe mais um companion ou vários esqueletos.", "how": "Use do Ato 2 até o Forgotten Warden.", "alt": "Body rare com Spirit."},
 {"n": "Evergrasping Ring", "slot": "Anel", "cat": "Acessório", "lvl": 32, "p": "a4", "use": None, "rf": "",
  "why": "Aliados na sua Presence ganham 15–25% do dano como chaos EXTRA. Com dois anéis e Withering Presence/Despair, o zoo inteiro bate muito mais.", "how": "Use dois (um em cada mão) do Ato 4 ao mapping.", "alt": "Rare de resist (e tire o Withering Presence)."},
 {"n": "Midnight Braid", "slot": "Cinto", "cat": "Acessório", "lvl": 1, "p": "a3", "use": None, "rf": "",
  "why": "50% do dano recebido é recuperado como mana, +resistências e +mana: sustenta Pain Offering, Unearth e marks.", "how": "", "alt": "Meginord's Girdle."},
 {"n": "Bushwhack", "slot": "Botas", "cat": "Armadura", "lvl": 33, "p": "a4", "use": None, "rf": "",
  "why": "15–25% Movement Speed com Evasion, e seu dano físico dá Pin. Botas baratas com MS para a campanha.", "how": "", "alt": "Rare com MS."},
 {"n": "Umbilicus Immortalis", "slot": "Cinto", "cat": "Acessório", "lvl": 24, "p": "a3", "use": None, "rf": "",
  "why": "Seu life flask também cura os minions, e eles não morrem enquanto o flask estiver ativo. Salva o macaco em bosses difíceis da campanha.", "how": "Alternativa ao Midnight Braid.", "alt": ""},
 {"n": "Spiteful Floret", "slot": "Weapon set 2", "cat": "Arma", "lvl": 5, "p": "t15", "use": 4, "rf": "",
  "why": "Fica no weapon set 2 só para conceder Sanguine Revelry (Remnants dão Rage e vida). Você não troca de set para lutar.", "how": "Equipe no set 2 e ative Sanguine Revelry.", "alt": ""},
 {"n": "Controlled Metamorphosis", "slot": "Jewel", "cat": "Jewel", "lvl": 20, "p": "t15", "use": 1, "rf": "",
  "why": "Aloca nós do anel médio-grande sem conexão (-5 a -20% resists). O Mattjestic usa para pegar nós de companion longe do caminho.", "how": "", "alt": "From Nothing."},
 {"n": "Undying Hate", "slot": "Jewel", "cat": "Jewel", "lvl": 20, "p": "ea", "use": None, "rf": "",
  "why": "Timeless Jewel: conquista nós no raio com bônus Abyssal. Usado no mapping T1–10 do Mattjestic.", "how": "Opcional.", "alt": ""},
 {"n": "Foxshade", "slot": "Body Armour", "cat": "Armadura", "lvl": 4, "p": "a1", "use": None, "rf": "", "why": "Leveling: +Evasion, +Dexterity e Movement Speed com vida cheia.", "how": "", "alt": ""},
 {"n": "Blackheart", "slot": "Anel", "cat": "Acessório", "lvl": 1, "p": "a1", "use": None, "rf": "", "why": "Leveling: dano de chaos nos ataques, regen de vida e Intimidate. Use dois.", "how": "", "alt": ""},
 {"n": "Goldrim", "slot": "Capacete", "cat": "Armadura", "lvl": 10, "p": "a1", "use": None, "rf": "", "why": "Leveling: +25–35% todas as resistências.", "how": "", "alt": ""},
 {"n": "Wanderlust", "slot": "Botas", "cat": "Armadura", "lvl": 11, "p": "a1", "use": None, "rf": "", "why": "Leveling: 20% Movement Speed e imune a Slow.", "how": "", "alt": ""},
 {"n": "Surefooted Sigil", "slot": "Amuleto", "cat": "Acessório", "lvl": 8, "p": "a1", "use": None, "rf": "", "why": "Leveling: vida, Dexterity e dodge roll maior.", "how": "", "alt": ""},
 {"n": "Skysliver", "slot": "Main-hand", "cat": "Arma", "lvl": 16, "p": "a2", "use": None, "rf": "", "why": "Leveling: spear de raio com attack speed para o Twister no Ato 2.", "how": "", "alt": "Rare spear."},
 {"n": "Splinter of Lorrata", "slot": "Main-hand", "cat": "Arma", "lvl": 1, "p": "a1", "use": None, "rf": "", "why": "Leveling nível 1: sempre envenena. Troque pelo Skysliver no 16.", "how": "", "alt": ""},
]
for u in EXTRA_U:
    e = M.ECO.get(u["n"], {})
    u["price"] = round(e["price"], 3) if e.get("price") is not None else None
    u["base"] = e.get("base", ""); u["mods"] = [m for m in e.get("mods", []) if "\n" not in m][:7]; u["iconUrl"] = e.get("icon")
    u["tier"] = "Barato" if (u["price"] or 0) < 0.1 else "Valor" if (u["price"] or 0) < 3 else "Luxo"
UNIQUES[:] = [u for u in UNIQUES if u["n"] not in {x["n"] for x in EXTRA_U}] + EXTRA_U
for u in UNIQUES:
    if u["n"] == "Chober Chaber":
        u.update(p="a3", why="O centro da rota. Maça de 2 mãos: dano base altíssimo (a Catha's Balance passa 60% dele por golpe para os companions), +2 a +4 Minion Skills, +50 Spirit e +100 mana. Custa ~2 Exalts.",
                 how="Para usar com sceptre precisa de Giant's Blood (Treefingers no começo, keystone na árvore depois). Giant's Blood TRIPLICA os requisitos de atributo: resolva com The Vertex (versão 'Equipment has no Attribute Requirements').")
    if u["n"] == "Treefingers":
        u.update(p="a3", why="Luvas de nível 11 que dão Giant's Blood por ~5 Exalts: permitem Chober Chaber + Rattling Sceptre já no Ato 3, sem gastar pontos na árvore.")
    if u["n"] == "The Vertex":
        u.update(p="a3", why="Com Giant's Blood, os requisitos da Chober Chaber triplicam (centenas de Strength/Intelligence). A versão 'Equipment has no Attribute Requirements' zera isso. É a peça que libera a Chober cedo.",
                 how="Compre SÓ a versão com 'Equipment has no Attribute Requirements' (o Mattjestic marca como 'The Vertex (equipment)').")
    if u["n"] == "Trenchtimbre":
        u.update(p="a3", why="Modo barato: +1 Minion Skills na mão enquanto você não compra a trinca Chober + Treefingers + The Vertex. O Mattjestic usa com Rattling Sceptre do Ato 3 ao mapping T1–10.")

# ------------------------------------------------------------------ sets (principal) por fase — Mattjestic
def R(slot, name, mods, r=None, note=""): return {"slot": slot, "n": name, "u": 0, "mods": mods, "r": r or [], "note": note}
def U(slot, name, r=None, note=""): return {"slot": slot, "n": name, "u": 1, "mods": [], "r": r or [], "note": note}
LIFE_RES = ["+Life", "+Resistências", "+Evasion"]
RAT = R("Offhand (Set 1)", "Rattling Sceptre", ["Grants Skill: Skeletal Warrior", "+1/+2 to Level of all Minion Skills", "% increased Spirit"], note="Base rare (não é unique) · qualquer um com +Minion Skills")
RAT_MAIN = R("Arma (Set 1)", "Rattling Sceptre", ["Grants Skill: Skeletal Warrior", "+1/+2 to Level of all Minion Skills", "% increased Spirit"], note="Base rare (não é unique) · qualquer um com +Minion Skills")
HELM = lambda n="Capacete rare": R("Capacete", n, ["+1/+2 to Level of all Minion Skills", "+Life", "+Resistências"])
AMU = lambda lv: R("Amuleto", "Amuleto rare", [f"+{lv} to Level of all Minion Skills", "+Spirit", "+Life", "+Resistências"])
GLOV = R("Luvas", "Luvas rare", LIFE_RES); BOOT = R("Botas", "Botas rare", ["25–30% Movement Speed"] + LIFE_RES)
RING = lambda k: R(k, "Anel rare", LIFE_RES)
CHOBER = U("Arma (Set 1)", "Chober Chaber", ["Runeforged"], "Giant's Blood (Treefingers) + The Vertex para usar com sceptre")
SETS.clear()
SETS.update({
 "a3": {"cheap": [RAT_MAIN, U("Offhand (Set 1)", "Trenchtimbre", note="+1 Minion Skills"), HELM("Capacete rare (Cultist Crown)"), U("Body Armour", "Foxshade"), GLOV, U("Botas", "Wanderlust"), AMU(1), U("Anel E", "Blackheart"), U("Anel D", "Blackheart"), U("Cinto", "Midnight Braid")],
        "full": [CHOBER, RAT, U("Capacete", "The Vertex", note="versão Equipment has no Attribute Requirements"), U("Body Armour", "Enfolding Dawn", note="+100 Spirit"), U("Luvas", "Treefingers", note="Giant's Blood"), U("Botas", "Wanderlust"), AMU(1), U("Anel E", "Blackheart"), U("Anel D", "Blackheart"), U("Cinto", "Midnight Braid")]},
 "a4": {"cheap": [RAT_MAIN, U("Offhand (Set 1)", "Trenchtimbre"), HELM("Capacete rare (Cultist Crown)"), U("Body Armour", "Enfolding Dawn", note="+100 Spirit"), GLOV, U("Botas", "Bushwhack"), AMU(1), U("Anel E", "Evergrasping Ring"), U("Anel D", "Evergrasping Ring"), U("Cinto", "Midnight Braid"), U("Charm", "Beira's Anguish"), U("Charm", "Sanguis Heroum")],
        "full": [CHOBER, RAT, U("Capacete", "The Vertex"), U("Body Armour", "Enfolding Dawn"), U("Luvas", "Treefingers"), U("Botas", "Bushwhack"), AMU(2), U("Anel E", "Evergrasping Ring"), U("Anel D", "Evergrasping Ring"), U("Cinto", "Midnight Braid"), U("Charm", "Beira's Anguish"), U("Charm", "Sanguis Heroum")]},
 "int": {"cheap": [U("Arma (Set 1)", "Trenchtimbre"), RAT, R("Capacete", "Runeforged Elite Greathelm", ["Runic Ward", "+Life", "+Resistências"]), U("Body Armour", "Enfolding Dawn"), GLOV, U("Botas", "Bushwhack"), AMU(1), U("Anel E", "Evergrasping Ring"), U("Anel D", "Evergrasping Ring"), U("Cinto", "Meginord's Girdle"), U("Charm", "Beira's Anguish"), U("Charm", "Sanguis Heroum")],
         "full": [CHOBER, RAT, U("Capacete", "The Vertex"), U("Body Armour", "Enfolding Dawn"), U("Luvas", "Treefingers"), U("Botas", "Bushwhack"), AMU(2), U("Anel E", "Evergrasping Ring"), U("Anel D", "Evergrasping Ring"), U("Cinto", "Midnight Braid"), U("Charm", "Beira's Anguish"), U("Charm", "Sanguis Heroum")]},
 "ea": {"cheap": [U("Arma (Set 1)", "Trenchtimbre", note="até juntar para a Chober"), RAT, R("Capacete", "Runeforged Elite Greathelm", ["Runic Ward (Refutation)", "+Life", "+Resistências"]), R("Body Armour", "Runeforged Layered Vest", ["Runic Ward", "+Evasion", "+Life"]), R("Luvas", "Adorned Wraps", LIFE_RES), R("Botas", "Shamanistic Leggings", ["Movement Speed"] + LIFE_RES), AMU(2), U("Anel E", "Evergrasping Ring"), U("Anel D", "Evergrasping Ring"), R("Cinto", "Linen Belt rare", LIFE_RES), U("Charm", "Beira's Anguish"), U("Charm", "Sanguis Heroum")],
        "full": [CHOBER, RAT, U("Capacete", "The Vertex"), R("Body Armour", "Runeforged Layered Vest", ["Runic Ward", "+Evasion", "+Life"]), U("Luvas", "Treefingers"), R("Botas", "Runeforged Wanderer Shoes", ["Movement Speed", "Runic Ward"] + LIFE_RES), AMU(3), U("Anel E", "Evergrasping Ring"), U("Anel D", "Evergrasping Ring"), R("Cinto", "Heavy Belt rare", LIFE_RES), U("Charm", "Beira's Anguish"), U("Charm", "Sanguis Heroum")]},
 "t15": {"cheap": [U("Arma (Set 1)", "Chober Chaber", ["Runeforged"]), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), U("Arma (Set 2)", "Spiteful Floret", note="só pela Sanguine Revelry"), R("Capacete", "Desert Cap rare", ["+Minion Skills"] + LIFE_RES), U("Body Armour", "Forgotten Warden", ["Fox Idol", "Spirit Vessel: Furious Slam + Arctic Howl"]), R("Luvas", "Runeforged Gold Gloves", ["Runic Ward"] + LIFE_RES), R("Botas", "Runeforged Wanderer Shoes", ["Movement Speed", "Runic Ward"] + LIFE_RES), AMU(3), RING("Anel E"), RING("Anel D"), R("Cinto", "Wide Belt rare", LIFE_RES), U("Flask mana", "Lavianga's Spirits")],
         "full": [U("Arma (Set 1)", "Chober Chaber", ["Runeforged"]), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), U("Arma (Set 2)", "Spiteful Floret"), R("Capacete", "Runeforged Pariah Mask", ["+Minion Skills", "Runic Ward"] + LIFE_RES), U("Body Armour", "Forgotten Warden", ["Fox Idol", "Spirit Vessel: Furious Slam + Arctic Howl"]), R("Luvas", "Barbed Bracers rare", LIFE_RES), R("Botas", "Drakeskin Boots rare", ["30% Movement Speed"] + LIFE_RES), AMU(4), RING("Anel E"), U("Anel D", "Kalandra's Touch"), U("Cinto", "Darkness Enthroned", ["Idols"]), U("Flask mana", "Lavianga's Spirits"), U("Charm", "Nascent Hope"), U("Charm", "The Fall of the Axe")]},
 "mm": {"cheap": [U("Arma (Set 1)", "Chober Chaber", ["Runeforged"]), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), U("Arma (Set 2)", "Spiteful Floret"), R("Capacete", "Runeforged Pariah Mask", ["+Minion Skills", "Runic Ward"] + LIFE_RES), U("Body Armour", "Forgotten Warden", ["Fox Idol", "Spirit Vessel: Devour + Oil Barrage + Salvo + Living Lightning"]), R("Luvas", "Barbed Bracers rare", LIFE_RES), R("Botas", "Drakeskin Boots rare", ["30% Movement Speed"] + LIFE_RES), AMU(4), RING("Anel E"), RING("Anel D"), R("Cinto", "Wide Belt rare", LIFE_RES), U("Flask mana", "Lavianga's Spirits"), U("Charm", "Nascent Hope"), U("Charm", "The Fall of the Axe"), U("Charm", "Beira's Anguish")],
        "full": [U("Arma (Set 1)", "Chober Chaber", ["Runeforged"]), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), U("Arma (Set 2)", "Spiteful Floret"), R("Capacete", "Runeforged Pariah Mask", ["+Minion Skills", "Runic Ward"] + LIFE_RES), U("Body Armour", "Forgotten Warden", ["Fox Idol", "Spirit Vessel: Devour + Oil Barrage + Salvo + Living Lightning"]), R("Luvas", "Barbed Bracers rare", LIFE_RES), R("Botas", "Drakeskin Boots rare", ["30% Movement Speed"] + LIFE_RES), AMU(4), RING("Anel E"), U("Anel D", "Kalandra's Touch"), U("Cinto", "Mageblood"), U("Flask mana", "Lavianga's Spirits"), U("Charm", "The Fall of the Axe"), U("Charm", "Nascent Hope"), U("Charm", "Rite of Passage")]},
})
JEWEL_SETS.clear()
JEWEL_SETS.update({"ea": ["From Nothing (nós de companion fora do caminho)", "Undying Hate (Timeless, opcional)"], "t15": ["Controlled Metamorphosis", "Megalomaniac (notables de minion)", "From Nothing"], "mm": ["Prism of Belief +2/+3 Tamed Companion", "Megalomaniac", "From Nothing"]})

# ------------------------------------------------------------------ explicações da rota (substitui as otimizações antigas)
OPTIMIZATIONS[:] = [
 {"t": "Por que a Chober Chaber é o centro", "ev": "Mattjestic usa do 'Giant's Blood' ao 100m DPS; 24% dos zoos com Effigy no poe.ninja.",
  "why": "A Catha's Balance dá aos companions 60% do dano da sua main-hand por golpe. A Chober é uma maça de 2 mãos com dano base enorme e ainda dá +2 a +4 Minion Skills, +50 Spirit e +100 mana. Nenhuma outra arma entrega tudo isso junto.", "was": "Rotas antigas: Tyranny's Grip / spear rare."},
 {"t": "Giant's Blood: 2 mãos + sceptre", "ev": "Keystone em todas as variantes endgame do Mattjestic; 34% dos zoos com Effigy.",
  "why": "Sem Giant's Blood, a Chober ocuparia as duas mãos e você perderia o sceptre (Skeletal Warrior no começo, Sylvan's Effigy depois). Treefingers dá o keystone cedo; no endgame ele vai para a árvore.", "was": ""},
 {"t": "The Vertex resolve os requisitos triplicados", "ev": "Variante 0.5.5 Mapping: 'The Vertex (equipment)'.",
  "why": "Giant's Blood triplica os requisitos de atributo das armas marciais. A versão do The Vertex com 'Equipment has no Attribute Requirements' zera isso e libera a Chober já no Ato 3.", "was": ""},
 {"t": "Pain Offering é central (não opcional)", "ev": "Presente em quase todas as variantes do Ato 3 ao 21m DPS.",
  "why": "Espeta um esqueleto e dá aos minions próximos até +29% attack speed e +58% dano (mais 30% com Danse Macabre e 30% com Sacrificial Offering). Brutus' Brain impede o espinho de morrer.", "was": "Eu tinha chamado de 'botão opcional' — estava errado."},
 {"t": "Esqueletos existem para o Muster e para o Pain Offering", "ev": "Ato 5: Frost Mage, Arsonist, Sniper, Reaver e Warrior ao mesmo tempo, sem supports de dano.",
  "why": "Muster: +7% more dano para CADA tipo diferente de minion que revive. Cinco tipos de esqueleto baratos = +35% more dano no macaco, e ainda servem de alvo do Pain Offering.", "was": ""},
 {"t": "Skeletal Cleric é alvo válido do Pain Offering", "ev": "Endgame: Cleric com Sacrificial Lamb II + Tecrod's Revenge.",
  "why": "O Cleric é um esqueleto. Quando o Effigy tira o Rattling Sceptre, o Cleric (com Sacrificial Lamb II) vira o esqueleto espetado e ainda cura/revive.", "was": "Eu tinha dito que o Cleric não servia — estava errado."},
 {"t": "Withering Presence + Evergrasping Ring", "ev": "Ato 4–5 do Mattjestic: 2× Evergrasping Ring + Withering Presence.",
  "why": "O anel faz os aliados ganharem 15–25% do dano como chaos extra; o Wither faz os inimigos receberem mais chaos. Juntos se multiplicam. Sem o anel, o Wither é fraco.", "was": "Eu tinha mandado tirar o Withering Presence — só vale tirar se não usar o anel."},
 {"t": "Sem Ball Lightning / Lightning Warp", "ev": "Nenhuma das 26 variantes usa.",
  "why": "Eram mobilidade do jogador e não ajudam o macaco. O espaço vai para curse, marks, Pain Offering e Refutation.", "was": "O guia antigo usava."},
 {"t": "Mace Strike + Einhar's Beastrite não é dano", "ev": "Variantes endgame (13–24).",
  "why": "O Mace Strike vem da própria Chober. Com Einhar's Beastrite ele só finaliza inimigos com vida baixa, e cada raro finalizado te dá 2 modificadores dele por 300 s (Haste, Extra Damage…).", "was": ""},
 {"t": "Refutation + itens Runeforged", "ev": "Do mapping T1–10 ao endgame.",
  "why": "Refutation gasta todo o seu Runic Ward para bloquear todos os hits por um tempo. Runic Ward vem de armaduras Runeforged/Runemastered — é por isso que as armaduras do Mattjestic são Runeforged.", "was": ""},
 {"t": "Aura bots baratos em Spirit", "ev": "Tier-list do Mattjestic (0.5).",
  "why": "O objetivo são 2–3 auras T1 (Physical/Haste > ES/Invulnerability > Temporal Bubble > Elemental Res) em beasts de 21–25% de Spirit: Swarming Wisp, Crag Leaper, Quill/Coconut Crab.", "was": "Beasts de 40%+ de Spirit."},
]

TRICKS[:0] = [
 {"cat": "Captura", "lvl": "Médio", "title": "Rota de aura bots do Mattjestic",
  "body": "1) Ato 4 Whakapanu Island: essence de crabs na praia (Quill/Coconut Crab ~25%) até achar Haste Aura. 2) Ato 5 Ashen Forest: Swarming Wisp (21%) com qualquer aura T1 exceto Haste. 3) Ato 2 Vastiri Outskirts: Crag Leaper (23,1%). Guarde auras T1 diferentes e substitua crabs duplicados."},
 {"cat": "Captura", "lvl": "Fácil", "title": "Haste não aparece em beasts muito rápidos",
  "body": "Beasts com a tag very_fast_movement (ex.: Crag Leaper) nunca rolam Haste Aura. Procure Haste em crabs."},
 {"cat": "Dano", "lvl": "Médio", "title": "Conte os tipos de minion para o Muster",
  "body": "Urso, macaco, cada beast diferente, Azmerian Wolf, Wolf Pack, Spirit Vessel e cada tipo de esqueleto contam como um tipo. Cada um soma 7% more dano nos companions com Muster."},
 {"cat": "Spirit", "lvl": "Fácil", "title": "Os 2 primeiros Skeletal Warriors são grátis",
  "body": "O Rattling Sceptre é uma base comum (não unique) que já traz a gem Skeletal Warrior. Um único esqueleto basta como alvo do Pain Offering até o Effigy; o segundo só quando sobrar Spirit."},
 {"cat": "Economia", "lvl": "Fácil", "title": "The Vertex: confira a versão",
  "body": "Só a versão com 'Equipment has no Attribute Requirements' libera a Chober Chaber com Giant's Blood. Filtre por esse mod no trade."},
]
FIXES += ["Rota refeita em cima do guia do Mattjestic com foco na Chober Chaber.", "Ball Lightning/Lightning Warp removidos (nenhuma variante do Mattjestic usa).", "Corrigido: Pain Offering é central; Skeletal Cleric serve de alvo; Withering Presence vale com Evergrasping Ring."]
SOURCES.insert(0, ("Mattjestic — FASTEST 0.5.5 Spirit Walker (26 variantes)", "Rota Chober Chaber: gems, supports, itens e árvore por fase", GUIDE_URL))
SOURCES.insert(1, ("Mattjestic — 0.5 Rare Beast Companions Tier-List", "Aura bots: custo de Spirit e localização", "https://mobalytics.gg/poe-2/profile/mattjestic-multigaming/guides/new-0-4-ultra-rare-beast-companion-farming-guide"))

KEY_PASSIVES[:] = [
 {"node": "Trusted Kinship", "type": "Keystone", "text": "2 companions de tipos diferentes; 30% more eficiência de reserva de Companion; 20% less para as demais.", "when": "Ato 3 → sempre", "why": "Mesmo com o Effigy, os 30% more de eficiência continuam valendo."},
 {"node": "Giant's Blood", "type": "Keystone", "text": "Maças/machados/espadas de 2 mãos em uma mão; triplica requisitos de atributo das armas.", "when": "Treefingers no Ato 3 → árvore no endgame", "why": "Chober Chaber + sceptre ao mesmo tempo."},
 {"node": "Easy Going", "type": "Notable", "text": "25% increased reservation efficiency de Companion.", "when": "Ato 4", "why": "Mais companions no mesmo Spirit."},
 {"node": "Polymathy", "type": "Notable", "text": "Atributos.", "when": "Giant's Blood", "why": "Ajuda com os requisitos triplicados."},
 {"node": "Mind Over Matter", "type": "Keystone", "text": "Todo dano sai da mana antes da vida; 50% less recuperação de mana.", "when": "Endgame (nv 90+)", "why": "Com +100 mana da Chober e Lavianga's Spirits vira uma camada de defesa enorme."},
]
TREE_STAGES[:] = [
 {"lv": "1–30", "focus": "Twister/projétil", "dmg": "Twister", "def": "Vida + Evasion", "spirit": "—", "dont": "Minion cedo demais"},
 {"lv": "31–45", "focus": "Trusted Kinship + Bonds (Mamba, Cat) + Unspoken Bond", "dmg": "Macaco", "def": "Blur, Catlike Agility, Escape Velocity", "spirit": "Trusted Kinship", "dont": "Nós de ataque"},
 {"lv": "46–64", "focus": "Easy Going, Inspiring Ally, Bond of the Wolf/Owl", "dmg": "Macaco + Muster", "def": "Evasion", "spirit": "Easy Going", "dont": "Sacrificar resists"},
 {"lv": "65–77", "focus": "Sturdy Ally, Captivating Companionship, Sic 'Em, Howling Primate", "dmg": "Catha + Chober", "def": "Enhanced Reflexes", "spirit": "Mais companions", "dont": "Julgar arma por DPS"},
 {"lv": "78–89", "focus": "Giant's Blood, Polymathy, Deflection, Long Distance Relationship", "dmg": "Zekoa + Azmerian Wolf", "def": "Enduring/Avoiding Deflection", "spirit": "Effigy", "dont": "Tirar Trusted Kinship"},
 {"lv": "90+", "focus": "Mind Over Matter, The Soul Meridian, Beastial Skin", "dmg": "Zoo inteiro", "def": "MoM", "spirit": "Idolatry", "dont": "MoM sem mana"},
]
BUY_ORDER[:] = [
 {"p": 1, "item": "Kit de leveling (Foxshade, Blackheart ×2, Goldrim, Wanderlust)", "phase": "Ato 1", "cost": "Barato", "impact": "Campanha rápida"},
 {"p": 2, "item": "Rattling Sceptre + Trenchtimbre", "phase": "Ato 3", "cost": "Barato", "impact": "Troca para minion"},
 {"p": 3, "item": "Chober Chaber + Treefingers", "phase": "Ato 3", "cost": "Barato (~7 ex)", "impact": "O centro da build"},
 {"p": 4, "item": "The Vertex (versão Equipment)", "phase": "Ato 3", "cost": "Valor (~0,4 div)", "impact": "Libera a Chober com sceptre"},
 {"p": 5, "item": "Enfolding Dawn (+100 Spirit)", "phase": "Ato 4", "cost": "Barato", "impact": "Mais minions"},
 {"p": 6, "item": "Evergrasping Ring ×2", "phase": "Ato 4", "cost": "Barato", "impact": "Chaos para o zoo"},
 {"p": 7, "item": "Sylvan's Effigy + Primate/Rabbit Idol", "phase": "Nv 78", "cost": "Valor (~1 div)", "impact": "Zoo ilimitado"},
 {"p": 8, "item": "Forgotten Warden + Lavianga's Spirits", "phase": "Nv 80", "cost": "Valor (~0,3 div)", "impact": "Spirit Vessel + mana"},
 {"p": 9, "item": "Mageblood · Kalandra's Touch · Rite of Passage", "phase": "Endgame", "cost": "Luxo", "impact": "Teto"},
]

TRICKS[:] = [t for t in TRICKS if t["title"] not in ("Warp no Ball Lightning", "Shocked Ground de graça", "Trusted Kinship pune não-companions", "Beasts baratos em reserva")]
TRICKS.insert(5, {"cat": "Dano", "lvl": "Médio", "title": "Pain Offering sem cair no boss",
  "body": "Brutus' Brain no Pain Offering deixa o espinho imune a dano, então o buff não some quando o boss acerta a área. Danse Macabre precisa de 2 esqueletos: com Rattling Sceptre são os Skeletal Warriors; depois do Effigy, o Skeletal Cleric com Sacrificial Lamb II."})
TROUBLESHOOT[:] = [t for t in TROUBLESHOOT if "Mana acaba" not in t[0]] + [
 ("Pain Offering não dá buff", "Com Danse Macabre ele precisa de 2 esqueletos vivos. Confira se os Skeletal Warriors (ou o Cleric no endgame) estão perto e com Sacrificial Lamb."),
 ("Mana acaba no endgame", "Lavianga's Spirits (flask constante) + a mana da Chober Chaber; com Mind Over Matter a mana também é sua defesa."),
]
CURRENT_SETUP["items"] = [
 {"img": "image.png", "what": "Silverfist — Feeding Frenzy II, Rage II, Rapid Attacks II, Heft, Muster",
  "verdict": "Certo: é exatamente o setup do Mattjestic (Act 5 / mapping). Com Rage III no lugar do Rage II a partir do mapping."},
 {"img": "image2.png", "what": "Wild Protector — Magnified Area I, Armour Break III, Minion Splash II",
  "verdict": "Certo para Ato 4 → mapping T1-10 (o Mattjestic usa os mesmos três e adiciona Minion Mastery). No endgame vira Romira's Requital + Catha's Brilliance."},
 {"img": "image4.png", "what": "Pain Offering — Danse Macabre, Prolonged Duration II",
  "verdict": "Central na rota. Adicione Sacrificial Offering no mapping e Brutus' Brain no endgame (o espinho não morre). Precisa de 2 esqueletos vivos por causa do Danse Macabre."},
 {"img": "image5.png", "what": "Skeletal Sniper + Withering Presence",
  "verdict": "Os dois fazem sentido: o Sniper conta como mais um tipo de minion para o Muster e serve de alvo do Pain Offering; o Withering Presence vale com 2× Evergrasping Ring (dano de chaos nos aliados). Sem os anéis, troque o Withering Presence."},
]

import spirit_tiers
spirit_tiers.apply(PH, MILESTONES, TROUBLESHOOT, CURRENT_SETUP, TRICKS, OPTIMIZATIONS, UNIQUES)

DATA.update(phases=PHASES, milestones=MILESTONES, beasts=BEASTS, auraPriority=AURA_PRIORITY, uniques=UNIQUES,
            sets=SETS, jewelSets=JEWEL_SETS, optimizations=OPTIMIZATIONS, tricks=TRICKS, fixes=FIXES,
            sources=[dict(name=a, use=b, url=c) for a, b, c in SOURCES], keyPassives=KEY_PASSIVES,
            treeStages=TREE_STAGES, buyOrder=BUY_ORDER, supWhy=SUPWHY, guideUrl=GUIDE_URL, current=CURRENT_SETUP, troubleshoot=[dict(q=a, a=b) for a, b in TROUBLESHOOT])

spirit_tiers.cleanup(DATA)
import timing
timing.unique_levels(UNIQUES)
DATA.update(timing=timing.TIMING, timingCases=timing.TIMING_CASES)
timing.effigy_62(DATA)
spirit_tiers.companion_limit(DATA)
# mantém as estruturas cruas (usadas pela planilha) iguais ao DATA
TRICKS[:] = DATA["tricks"]
TROUBLESHOOT[:] = [(t["q"], t["a"]) for t in DATA["troubleshoot"]]
ATLAS_CHECK[:] = [tuple(a.values()) if isinstance(a, dict) else a for a in DATA["atlasCheck"]]

if __name__ == "__main__":
    miss = sorted({s for p in PHASES for g in p["gems"] for s in g["sup"]} - set(SUPWHY))
    print("supports sem explicação:", miss)
    print("uniques sem preço:", [u["n"] for u in UNIQUES if u["price"] is None])
