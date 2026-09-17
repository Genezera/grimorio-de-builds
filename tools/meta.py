# -*- coding: utf-8 -*-
"""Camada de otimização: dados reais do poe.ninja (Forbidden Rites, 15/09/2026), uniques com preço/uso
e a rota própria. Importa data.py, ajusta as fases e reexporta tudo."""
import json, glob, re
from data import *          # noqa
import data as _base

SNAP = "15/09/2026"

# ------------------------------------------------------------------ META (poe.ninja)
META = {
 "league": "Forbidden Rites",
 "total_sw": 9651, "effigy_pop": 5649, "zoo_sample": 24,
 "note": "Porcentagens do filtro Spirit Walker + Sylvan's Effigy no poe.ninja (5.649 personagens nível 80+, snapshot de 15/09/2026). A amostra detalhada são 24 zoos nível 98–99 abertos um a um.",
 "charts": [
  {"id": "body", "title": "Body Armour", "rows": [["Forgotten Warden", 80], ["Morior Invictus", 11], ["Rare", 6]]},
  {"id": "weapon", "title": "Main-hand", "rows": [["Tyranny's Grip", 39], ["Trenchtimbre", 26], ["Chober Chaber", 24], ["The Hammer of Faith", 6]]},
  {"id": "config", "title": "Configuração de armas", "rows": [["Arma 1 mão / Sceptre", 62], ["Maça 2 mãos / Sceptre (Giant's Blood)", 32], ["Spear / Sceptre", 2]]},
  {"id": "ks", "title": "Keystones", "rows": [["Trusted Kinship", 99], ["Giant's Blood", 34], ["Mind Over Matter", 27], ["Iron Reflexes", 4], ["Chaos Inoculation", 2]]},
  {"id": "asc", "title": "Ascendência", "rows": [["The Natural Order", 100], ["Wild Protector", 99], ["The Catha's Balance", 97], ["Idolatry", 86]]},
  {"id": "comp", "title": "Companions (skills principais)", "rows": [["Wild Protector", 99], ["Azmerian Wolf", 97], ["Wolf Pack", 84], ["Zekoa, the Headcrusher", 72], ["Diretusk Boar", 40], ["Plague Harvester", 29], ["Quadrilla", 26], ["Mighty Silverfist", 23], ["Quill Crab", 17]]},
  {"id": "spirit", "title": "Skills de Spirit", "rows": [["Discipline", 100], ["Spirit Vessel", 80], ["Skeletal Cleric", 29], ["Ghost Dance", 24]]},
  {"id": "sup", "title": "Supports mais usados", "rows": [["Muster", 98], ["Rapid Attacks II", 97], ["Loyalty", 96], ["Feeding Frenzy II", 93], ["Rage III", 91], ["Romira's Requital", 69]]},
  {"id": "anoint", "title": "Anoints de amuleto", "rows": [["Warlord Leader", 20], ["Gigantic Following", 13], ["The Soul Meridian", 11], ["Relentless Fallen", 5], ["Lord of Horrors", 4], ["Vile Mending", 3]]},
  {"id": "charm", "title": "Charms / Flasks únicos", "rows": [["Beira's Anguish", 43], ["Nascent Hope", 33], ["Sanguis Heroum", 26], ["Lavianga's Spirits", 25], ["Arakaali's Gift", 22], ["The Fall of the Axe", 12], ["Rite of Passage", 10]]},
  {"id": "jewel", "title": "Jewels únicos", "rows": [["From Nothing", 21], ["Prism of Belief", 8], ["Megalomaniac", 7], ["Heart of the Well", 7]]},
  {"id": "ring", "title": "Anéis únicos", "rows": [["Ventor's Gamble", 7], ["Kalandra's Touch", 6], ["Andvarius", 4], ["Eshtera's Path", 3]]},
 ],
 "zekoaLinks": [["Muster", 93], ["Feeding Frenzy II", 86], ["Rapid Attacks II", 86], ["Rage III", 75]],
 "sample": {"spirit_median": 330, "notables": [["Bond of the Wolf", 92], ["Inspiring Ally", 88], ["Bond of the Mamba", 88], ["Long Distance Relationship", 75], ["Lord of Horrors", 75], ["Blur", 75], ["The Soul Meridian", 71], ["Entropic Incarnation", 67], ["Grip of Evil", 67], ["Unspoken Bond", 67], ["Gigantic Following", 67], ["Bond of the Cat", 58], ["Vile Mending", 54], ["Bond of the Ape", 50], ["Crystallised Immunities", 42], ["Sturdy Ally", 42], ["Captivating Companionship", 38], ["Right Hand of Darkness", 33]]},
}

# ------------------------------------------------------------------ UNIQUES
# p = fase em que entra (id), price = div (snapshot), use = % entre os 5.649 zoos com Effigy (quando medido)
UNIQUES = [
 {"n": "Tyranny's Grip", "slot": "Main-hand", "cat": "Arma", "lvl": 5, "p": "ea", "use": 39, "rf": "Runeforged (nv 38) ≈ 0,003 div · Runemastered (nv 55) ≈ 0,41 div",
  "why": "A arma barata padrão da Catha's Balance: +150–238% dano físico. Attack speed reduzido não importa, o companion ganha 60% do dano por golpe.",
  "how": "Compre já Runeforged (sai mais barato que fazer). Runemastered adiciona 'Minions ganham 10% phys como lightning' e +20% dano de minion (bonded).",
  "alt": "Rare spear de dano físico alto."},
 {"n": "Trenchtimbre", "slot": "Main-hand", "cat": "Arma", "lvl": 16, "p": "a3", "use": 26, "rf": "Runeforged (nv 40) ≈ 0,08 div",
  "why": "Maça 1 mão com +1 Minion Skills (+2 Runeforged) e attack speed. Ótima do respec do Ato 3 até a Catha, e ainda competitiva depois se você prefere mais vida no zoo.",
  "how": "Base custa quase nada; equipe logo depois de capturar o Silverfist.",
  "alt": "Qualquer arma com +Minion Skills."},
 {"n": "Chober Chaber", "slot": "Main-hand (2 mãos)", "cat": "Arma", "lvl": 33, "p": "ea", "use": 24, "rf": "Runeforged (nv 55) ≈ 0,04 div",
  "why": "O melhor da build: +2 a +4 Minion Skills, +47–50 Spirit, +80–100 mana e dano físico alto para a Catha's Balance. Com Giant's Blood você segura o Sylvan's Effigy junto.",
  "how": "Precisa de Giant's Blood (Treefingers ou keystone) para usar com sceptre. Os requisitos triplicam: resolva com Soul Core of Cholotl (40% vira Dex), The Vertex, ou atributos na árvore.",
  "alt": "The Hammer of Faith (mais dano bruto, sem +levels)."},
 {"n": "The Hammer of Faith", "slot": "Main-hand (2 mãos)", "cat": "Arma", "lvl": 65, "p": "t15", "use": 6, "rf": "≈ 0,10 div",
  "why": "Giant Maul com 300–342% dano físico: muito dano por golpe para a Catha. Runeforged dá 30% phys como lightning e +60% dano de minion (bonded).",
  "how": "Também exige Giant's Blood para usar com sceptre.", "alt": "Chober Chaber."},
 {"n": "Sylvan's Effigy", "slot": "Offhand", "cat": "Arma", "lvl": 78, "p": "ea", "use": 100, "rf": "≈ 0,95 div (4 mil à venda)",
  "why": "Companions ilimitados (tipos diferentes), Azmerian Wolf e Discipline de graça, +50–68% Spirit. Nesta liga custa ~1 div: não é luxo, é o primeiro grande objetivo do Atlas.",
  "how": "Coloque Primate Idol (+40% dano de aliados) e Rabbit Idol (+15% Spirit) nos sockets.",
  "alt": "Rare sceptre com Spirit + Minion Skills até juntar 1 div."},
 {"n": "Forgotten Warden", "slot": "Body Armour", "cat": "Armadura", "lvl": 78, "p": "t15", "use": 80, "rf": "Base ≈ 0,21 div · Runemastered ≈ 5 div",
  "why": "80% dos zoos usam. Companions +30–50% vida, Deflection, 10–15% do dano deflectido vai para os companions, e concede Spirit Vessel nível 16 (um companion a mais sem gastar gem).",
  "how": "Soquete Fox Idol (ativa bonded) e uma skill de Bear/Werewolf no Spirit Vessel.",
  "alt": "Rare Evasion/ES com '% da Evasion como Deflection'."},
 {"n": "Morior Invictus", "slot": "Body Armour", "cat": "Armadura", "lvl": 65, "p": "mm", "use": 11, "rf": "≈ 6 div",
  "why": "Por socket preenchido: +8–10% todas as resists, +45–60 vida, +10 Spirit, menos dano crítico recebido. Tanque de verdade para Arbiter.",
  "how": "Encha todos os sockets com Idols.", "alt": "Forgotten Warden."},
 {"n": "Alpha's Howl", "slot": "Capacete", "cat": "Armadura", "lvl": 65, "p": "ea", "use": 1, "rf": "≈ 0,42 div",
  "why": "+100 Spirit e Presence em dobro (auras e bônus de Presence alcançam o zoo espalhado). Resolve o Spirit do modo barato.",
  "how": "Troca o +Minion Skills do capacete por Spirit: vale enquanto faltar reserva.", "alt": "Rare com +Minion Skills + Idol of Ralakesh."},
 {"n": "The Vertex", "slot": "Capacete", "cat": "Armadura", "lvl": 33, "p": "ea", "use": 13, "rf": "≈ 0,41 div",
  "why": "Skill gems sem requisito de atributo (e algumas versões: equipamento também). É o truque para rodar Chober Chaber + Giant's Blood sem empilhar atributos.",
  "how": "Na hora de comprar, confira se o item tem 'Equipment has no Attribute Requirements'.", "alt": "Soul Core of Cholotl + atributos na árvore."},
 {"n": "Starkonja's Head", "slot": "Capacete", "cat": "Armadura", "lvl": 50, "p": "a4", "use": 4, "rf": "≈ 0,01 div",
  "why": "15% do dano de hits vai para o companion antes de você. Defesa barata na campanha e no início dos maps.", "how": "", "alt": ""},
 {"n": "Treefingers", "slot": "Luvas", "cat": "Armadura", "lvl": 11, "p": "ea", "use": 3, "rf": "≈ 0,014 div",
  "why": "Dá Giant's Blood sem gastar pontos na árvore: maça de 2 mãos + sceptre.", "how": "Use enquanto não tiver luvas melhores; depois pegue o keystone na árvore.", "alt": "Keystone Giant's Blood."},
 {"n": "Horror's Flight", "slot": "Luvas", "cat": "Armadura", "lvl": 84, "p": "mm", "use": 3, "rf": "≈ 0,10 div",
  "why": "200–300% Evasion e attack speed. Com Cadigan's Epiphany vira jewel socket.", "how": "", "alt": ""},
 {"n": "Darkness Enthroned", "slot": "Cinto", "cat": "Acessório", "lvl": 62, "p": "t15", "use": 2, "rf": "≈ 0,014 div",
  "why": "Até 3 Charm Slots, flasks ganham carga sozinhas e 2 sockets escondidos com 50–100% mais efeito para runas de vida e resist.", "how": "Socket 1: Greater Body Rune (vida). Socket 2: Greater Desert, Glacial ou Storm Rune (a resist que faltar). Idols não entram: Idol of Ralakesh e Primate Idol são só de Capacete ou Sceptre, então o Ralakesh fica no capacete. Qualquer variante serve; prefira efeito perto de 100%.", "alt": "Rare vida/resist."},
 {"n": "Mageblood", "slot": "Cinto", "cat": "Acessório", "lvl": 55, "p": "mm", "use": 8, "rf": "≈ 570 div",
  "why": "Luxo absoluto: legados de flask permanentes. 13 dos 24 zoos 98+ usam, mas não muda o funcionamento da build.", "how": "", "alt": "Rare vida/resist ou Darkness Enthroned."},
 {"n": "Meginord's Girdle", "slot": "Cinto", "cat": "Acessório", "lvl": 0, "p": "a2", "use": None, "rf": "≈ 0,009 div",
  "why": "+40–50 Strength e resist a frio: resolve requisitos de supports na campanha.", "how": "", "alt": ""},
 {"n": "Ventor's Gamble", "slot": "Anel", "cat": "Acessório", "lvl": 64, "p": "int", "use": 7, "rf": "≈ 0,03 div",
  "why": "Até +80 vida e +20 Spirit (e resists aleatórias). Um bom roll custa quase nada.", "how": "Compre um com resists positivas.", "alt": "Rare vida/resist."},
 {"n": "Kalandra's Touch", "slot": "Anel", "cat": "Acessório", "lvl": 0, "p": "mm", "use": 6, "rf": "≈ 33 div",
  "why": "Copia o outro anel (use com um anel rare perfeito).", "how": "", "alt": ""},
 {"n": "Eshtera's Path", "slot": "Anel", "cat": "Acessório", "lvl": 40, "p": "mm", "use": 3, "rf": "≈ 34 div",
  "why": "Aceita Sapphire jewel (minion crit/dano) e dá atributos + resists.", "how": "", "alt": ""},
 {"n": "Grip of Kulemak", "slot": "Anel", "cat": "Acessório", "lvl": 0, "p": "mm", "use": None, "rf": "≈ 0,006 div",
  "why": "Citado pelo guia base (Spirit efficiency / vida ao matar / chaos res em aliados, dependendo do roll).", "how": "", "alt": ""},
 {"n": "From Nothing", "slot": "Jewel", "cat": "Jewel", "lvl": 0, "p": "t15", "use": 21, "rf": "≈ 0,21 div",
  "why": "Aloca nós sem conexão: Vile Mending, Grip of Evil, Entropic Incarnation e o cluster de minion perto de Blackflame Covenant. É por isso que esses notables aparecem em 54–67% dos zoos top.",
  "how": "Confira o keystone do raio no anúncio (precisa ser o que alcança os nós de minion).", "alt": ""},
 {"n": "Prism of Belief", "slot": "Jewel", "cat": "Jewel", "lvl": 0, "p": "mm", "use": 8, "rf": "+1 barato · +2/+3 Tamed Companion caro",
  "why": "+1 a +3 níveis em todos os Tamed Companions (Zekoa, beasts).", "how": "Procure no trade o mod exato 'Tamed Companion Skills'.", "alt": ""},
 {"n": "Heart of the Well", "slot": "Jewel", "cat": "Jewel", "lvl": 0, "p": "mm", "use": 7, "rf": "≈ 0,73 div",
  "why": "Mods aleatórios; os bons dão resistência física e regeneração para minions.", "how": "", "alt": ""},
 {"n": "Megalomaniac", "slot": "Jewel", "cat": "Jewel", "lvl": 0, "p": "mm", "use": 7, "rf": "≈ 0,32 div",
  "why": "Aloca notables aleatórios; compre só com notables de minion/defesa.", "how": "", "alt": ""},
 {"n": "Flesh Crucible", "slot": "Jewel", "cat": "Jewel", "lvl": 0, "p": "t15", "use": None, "rf": "≈ 0,32 div",
  "why": "Pode rolar Giant's Blood (entre outros keystones) com uma penalidade: alternativa ao Treefingers sem gastar slot de luva.", "how": "Só compre a versão com Giant's Blood e penalidade leve (ex.: less mana).", "alt": "Treefingers."},
 {"n": "Nascent Hope", "slot": "Charm", "cat": "Charm", "lvl": 12, "p": "t15", "use": 33, "rf": "≈ 0,11 div",
  "why": "Thawing Charm que ganha cargas ao matar e inicia recarga de ES ao usar.", "how": "", "alt": "Thawing Charm mágico."},
 {"n": "Beira's Anguish", "slot": "Charm", "cat": "Charm", "lvl": 32, "p": "a4", "use": 43, "rf": "≈ 0,01 div",
  "why": "Contra ignite: cria chão em chamas que queima com 500% da sua vida máxima.", "how": "", "alt": "Ruby/Dousing Charm."},
 {"n": "Sanguis Heroum", "slot": "Charm", "cat": "Charm", "lvl": 18, "p": "a4", "use": 26, "rf": "≈ 0,006 div",
  "why": "Contra bleed: ganha cargas sozinho e cria Consecrated Ground.", "how": "", "alt": "Staunching Charm."},
 {"n": "Arakaali's Gift", "slot": "Charm", "cat": "Charm", "lvl": 24, "p": "a4", "use": 22, "rf": "≈ 0,003 div",
  "why": "Contra poison: recupera vida e mana ao usar.", "how": "", "alt": "Antidote Charm."},
 {"n": "The Fall of the Axe", "slot": "Charm", "cat": "Charm", "lvl": 10, "p": "t15", "use": 12, "rf": "≈ 0,64 div",
  "why": "Onslaught quando você é desacelerado: mais velocidade para acompanhar o zoo.", "how": "", "alt": ""},
 {"n": "Rite of Passage", "slot": "Charm", "cat": "Charm", "lvl": 50, "p": "mm", "use": 10, "rf": "≈ 15 div",
  "why": "Possessão por Azmeri Spirits ao matar raros/únicos. Luxo.", "how": "", "alt": ""},
 {"n": "Lavianga's Spirits", "slot": "Flask", "cat": "Flask", "lvl": 49, "p": "t15", "use": 25, "rf": "≈ 0,11 div",
  "why": "Flask de mana com efeito constante: sustenta os Commands do Azmerian Wolf e marks, e combina com Mind Over Matter.", "how": "", "alt": "Mana flask normal."},
]
IDOLS = [
 {"n": "Primate Idol", "where": "Sceptre / Capacete", "price": 0.011, "eff": "Sceptre: aliados na Presence +40% dano · Capacete: minions +15% vida"},
 {"n": "Rabbit Idol", "where": "Sceptre / Body", "price": 0.094, "eff": "Sceptre: +15% Spirit · Bonded: +30% recarga de Command"},
 {"n": "Idol of Ralakesh", "where": "Capacete / Sceptre", "price": 0.056, "eff": "Capacete: +8% reservation efficiency de minions · Sceptre bonded: companions +25% vida"},
 {"n": "Fox Idol", "where": "Body / Sceptre", "price": 0.196, "eff": "Body: ativa os Bonded dos Idols do item · Sceptre: +50% Presence"},
 {"n": "Carved Majesty", "where": "Body / Luvas / Botas", "price": 85.47, "eff": "Body: +3 Spirit por Idol equipado · Luvas: Onslaught nos alvos marcados · bonded: companions +30% dano"},
 {"n": "Soul Core of Cholotl", "where": "Arma / Armadura", "price": None, "eff": "Converte 40% dos requisitos em Dexterity (ajuda Chober Chaber)"},
 {"n": "Greater Rune of Leadership", "where": "Arma / Armadura", "price": None, "eff": "Arma: minions 10% phys como lightning · bonded: +20% dano de minion"},
]

# ------------------------------------------------------------------ OTIMIZAÇÕES (o que muda vs guia base)
OPTIMIZATIONS = [
 {"t": "Mantenha Trusted Kinship mesmo com Sylvan's Effigy", "ev": "99% dos 5.649 zoos com Effigy mantêm o keystone.",
  "why": "O Effigy libera o limite de companions, mas os 30% more de reservation efficiency continuam valendo. Tirar o keystone derruba o Spirit.", "was": "Guia base: remover Trusted Kinship com o Effigy."},
 {"t": "Sylvan's Effigy no início do Atlas, não no fim", "ev": "≈ 0,95 div com mais de 4 mil à venda.",
  "why": "É o maior salto de poder depois da Catha e está barato nesta liga. Junte 1 div nos primeiros maps e compre.", "was": "Guia base: tratado como item raro e opcional para T15+."},
 {"t": "Forgotten Warden como body padrão", "ev": "80% dos zoos com Effigy; ≈ 0,21 div.",
  "why": "Mais vida no zoo, dano redirecionado para companions e um Spirit Vessel grátis.", "was": "Guia base: body rare de Evasion."},
 {"t": "Silverfist → Zekoa, the Headcrusher", "ev": "Zekoa em 72% dos zoos, contra 23% do Silverfist.",
  "why": "Zekoa é a versão de Atlas do macaco e pode ter mais mods. Cace em Riverside/Rupture com tablets de mod extra.", "was": "Guia base: manter o Silverfist da campanha."},
 {"t": "Supports de endgame pelo meta", "ev": "No Zekoa: Muster 93%, Feeding Frenzy II 86%, Rapid Attacks II 86%, Rage III 75%.",
  "why": "Armour Break e Armour Demolisher ajudam na campanha, mas no endgame o meta usa Feeding Frenzy II + Rapid Attacks II. Loyalty entra em quase todos os companions.", "was": "Guia base: Armour Break III no macaco até o fim."},
 {"t": "Caminho da arma: Trenchtimbre → Tyranny's Grip → Chober Chaber", "ev": "Main-hand: Tyranny 39%, Trenchtimbre 26%, Chober 24% (32% usam maça 2 mãos + sceptre).",
  "why": "Trenchtimbre dá +1 Minion Skill logo após o respec. A Tyranny é a Catha barata. A Chober Chaber com Giant's Blood soma +4 levels, +47 Spirit e o maior dano por golpe.", "was": "Guia base: spear rare até a Catha."},
 {"t": "Giant's Blood sem gastar pontos", "ev": "Giant's Blood em 34% dos zoos com Effigy.",
  "why": "Treefingers (0,014 div) ou Flesh Crucible dão o keystone; The Vertex ou Soul Core of Cholotl resolvem os requisitos triplicados.", "was": "Não existia no guia base."},
 {"t": "Idols certos no Sceptre", "ev": "Primate Idol ≈ 0,01 div, Rabbit Idol ≈ 0,09 div.",
  "why": "Primate = +40% dano de aliados; Rabbit = +15% Spirit. É muito poder por quase nada.", "was": "Guia base: só Primate Idol."},
 {"t": "Mind Over Matter no endgame", "ev": "27% dos zoos com Effigy.",
  "why": "Chober Chaber (+100 mana) e Lavianga's Spirits (flask constante) tornam o MoM uma camada de defesa forte.", "was": "Não existia no guia base."},
 {"t": "Anoint Warlord Leader ou The Soul Meridian", "ev": "Warlord Leader 20%, Gigantic Following 13%, The Soul Meridian 11%.",
  "why": "Warlord Leader = +40% dano de aliados e Presence maior. Soul Meridian = Deflection + reservation efficiency.", "was": "Guia base: só Warlord Leader."},
]

EXTRA_TRICKS = [
 {"cat": "Captura", "lvl": "Fácil", "title": "Como o Tame Beast funciona",
  "body": "Use o Tame Beast num raro: ele fica envolto em wisps (Hinder) por ~8–12s. Mate enquanto os wisps estão nele para capturar. O beast guarda até 4 mods de monstro, então capture o que tem os mods que você quer."},
 {"cat": "Silverfist", "lvl": "Médio", "title": "Zekoa com 3+ mods",
  "body": "Riverside ou Rupture + 1 Cruel Hegemony + 2 tablets raros com 'Unique Monsters have 1 additional Rare Modifier'. Ordem de mods: Extra Crits > Hasted > Extra Damage as Chaos/Physical > Soul Eater."},
 {"cat": "Silverfist", "lvl": "Avançado", "title": "Reroll de mods morrendo (softcore)",
  "body": "Com Doryani como Atlas Master e o nó Stitch the Flesh (revive extra), dá para morrer de propósito na luta e o boss volta com mods novos. Rituals perto de City biomes geram vários Zekoas no mesmo map."},
 {"cat": "Dano", "lvl": "Médio", "title": "Giant's Blood + The Vertex",
  "body": "Treefingers dá Giant's Blood (maça 2 mãos + sceptre), mas triplica requisitos. The Vertex remove requisitos de gems (e, em algumas versões, do equipamento). Soul Core of Cholotl converte 40% para Dex."},
 {"cat": "Spirit", "lvl": "Fácil", "title": "Idols no Sylvan's Effigy",
  "body": "Primate Idol (+40% dano de aliados) e Rabbit Idol (+15% Spirit) custam centavos. No capacete, Idol of Ralakesh dá +8% reservation efficiency de minions."},
 {"cat": "Spirit", "lvl": "Fácil", "title": "Alpha's Howl quando faltar Spirit",
  "body": "+100 Spirit e Presence em dobro por ~0,4 div. Troque de volta por capacete com +Minion Skills quando o Spirit sobrar."},
 {"cat": "Dano", "lvl": "Fácil", "title": "Spirit Vessel do Forgotten Warden",
  "body": "O body já concede Spirit Vessel nível 16. Soquete skills de Bear/Werewolf/Wyvern nele (ex.: Furious Slam): ganha 20% more dano por skill diferente."},
 {"cat": "Economia", "lvl": "Fácil", "title": "Compre uniques já runeforged",
  "body": "Tyranny's Grip Runeforged sai ≈ 0,003 div e Chober Chaber Runeforged ≈ 0,04 div: mais barato do que juntar Verisium para fazer você mesmo."},
 {"cat": "Defesa", "lvl": "Médio", "title": "Mind Over Matter + Lavianga's Spirits",
  "body": "O flask de mana com efeito constante e a mana da Chober Chaber sustentam o MoM e os Commands do Azmerian Wolf."},
]

# ------------------------------------------------------------------ ajustes nas fases
def _ph(pid): return next(p for p in PHASES if p["id"] == pid)

a3 = _ph("a3")
# Ato 3 = dois momentos: spear até capturar o Silverfist (nv 31–34) e zoo puro depois do respec (nv 35+)
for g in a3["gems"]:
    if g["skill"] in ("Whirling Slash", "Twister", "Cull The Weak", "Barrage"):
        g["until"] = 35; g["role"] = "Só até capturar o Silverfist e fazer o respec"
a3["rotation"] = ["Nv 31–34 (antes da captura): rotação de spear — Entangle → Whirling Slash → Twister", "Nv 35+ (depois do respec): tire Twister, Whirling, Cull e Barrage da barra", "Entangle para agrupar os packs no macaco e no urso, e fique na Presence deles"]
a3["avoid"] = ["Matar o Silverfist antes de ter The Natural Order", "Manter Twister/Whirling depois do respec: a árvore não escala mais spear, só ocupa a barra", "Manter skills não-companion caras em Spirit (Trusted Kinship dá 20% less eficiência a elas)"]
a3["carry"] = "Spear até o nv 34 → Mighty Silverfist"
a3["cheap"] = ["Sceptre raro com Spirit no offhand", "Trenchtimbre na main-hand depois do respec (+1 Minion Skills, ~0,02 div)", "Meginord's Girdle se faltar Strength", "Gold guardado para o respec"]
a3["full"] = ["Trenchtimbre Runeforged (+2 Minion Skills)", "Amuleto +2 Minion Skills", "Sceptre com Spirit + % dano de minions + Primate Idol"]

a4 = _ph("a4")
a4["cheap"] = ["Botas 25–30% MS", "Starkonja's Head (15% do dano vai para o companion, ~0,01 div)", "Charms únicos baratos: Beira's Anguish, Sanguis Heroum, Arakaali's Gift", "+1 Minion Skills em amuleto/capacete"]
a4["full"] = ["+2 Minion Skills em amuleto e capacete", "Compre Tyranny's Grip Runeforged (~0,003 div) e guarde para a Catha", "Comece a juntar 1 div para o Sylvan's Effigy"]

it = _ph("int")
it["cheap"] = ["Ventor's Gamble com resists positivas (+vida +Spirit, ~0,03 div)", "Ajuste resists com anéis/luvas/cinto", "Jewels: Minions +% Elemental Res, Companion vida"]
it["full"] = ["+2/+3 Minion Skills em slots-chave", "Deflection em body/capacete/botas", "Separe 1 div para o Effigy no nível 65+"]

ea = _ph("ea")
ea["goal"] = "The Catha's Balance + Tyranny's Grip, Sylvan's Effigy assim que tiver 1 div, e começar a caçar Zekoa. É a fase de maior salto de dano."
ea["gems"] = [
 {"skill": "Entangle", "set": "—", "sup": ["Upheaval I", "Slow Potency", "Magnified Area II", "Blind II"], "role": "Controle"},
 {"skill": "Wild Protector", "set": "Asc.", "sup": ["Muster", "Rapid Attacks II", "Feeding Frenzy II", "Rage III"], "role": "Tank + DPS"},
 {"skill": "Tame Beast (Mighty Silverfist → Zekoa)", "set": "—", "sup": ["Muster", "Feeding Frenzy II", "Rapid Attacks II", "Rage III", "Minion Mastery"], "role": "CARRY"},
 {"skill": "Tame Beast (Quadrilla / aura)", "set": "—", "sup": ["Loyalty", "Meat Shield II", "Rage III", "Minion Mastery"], "role": "Aura/Tank"},
 {"skill": "Azmerian Wolf", "set": "Effigy", "sup": ["Muster", "Loyalty", "Rapid Attacks II", "Feeding Frenzy II", "Minion Splash II"], "role": "Com o Effigy"},
 {"skill": "Skeletal Cleric", "set": "—", "sup": ["Meat Shield II", "Rapid Casting II", "Last Gasp", "Minion Mastery"], "role": "Sustain (sem Effigy)"},
 {"skill": "Wind Dancer", "set": "—", "sup": ["Blind II", "Pin III", "Maim", "Magnified Area II"], "role": "Defesa"},
 {"skill": "Malice", "set": "—", "sup": ["Upwelling I", "Healing Runes", "Vitality I"], "role": "Defesa (Discipline vem no Effigy)"},
 {"skill": "Lightning Warp", "set": "—", "sup": ["Magnified Area II", "Prolonged Duration II", "Persistent Ground III"], "role": "Shock/cull"},
 {"skill": "Sniper's Mark", "set": "—", "sup": ["Eternal Mark", "Cooldown Recovery II", "Second Wind III", "Charged Mark"], "role": "Marca (Effigy: +dano em marcados)"},
]
ea["cheap"] = ["Tyranny's Grip Runeforged (~0,003 div) na main-hand ao pegar a Catha", "Sylvan's Effigy (~1 div) com Primate + Rabbit Idol", "Alpha's Howl (+100 Spirit) se a reserva apertar", "Charms: Beira's Anguish / Sanguis Heroum / Arakaali's Gift"]
ea["full"] = ["Chober Chaber Runeforged + Treefingers (Giant's Blood) + The Vertex", "Sylvan's Effigy com Primate + Rabbit Idol", "Capacete +2 Minion Skills com Idol of Ralakesh", "Anoint Warlord Leader no amuleto"]
ea["tree"] = "Clusters de minion/companion, jewel sockets e Giant's Blood (se não usar Treefingers). Mantenha Trusted Kinship e Easy Going para sempre."
ea["avoid"] = ["Olhar pDPS da arma: com Catha vale dano por golpe", "Tirar Trusted Kinship (99% do meta mantém)", "Pagar caro para runeforjar: compre pronto"]

t15 = _ph("t15")
t15["goal"] = "Zoo completo: Zekoa com mods, Azmerian Wolf, Wolf Pack, Spirit Vessel (Forgotten Warden) e beasts de aura. Idolatry na 4ª Asc. Mantenha Trusted Kinship."
t15["gems"] = [
 {"skill": "Discipline", "set": "Effigy", "sup": ["Vitality I"], "role": "Vem no Effigy"},
 {"skill": "Tame Beast (Zekoa, the Headcrusher)", "set": "—", "sup": ["Muster", "Feeding Frenzy II", "Rapid Attacks II", "Rage III", "Minion Mastery"], "role": "Maior DPS (776k no top 1)"},
 {"skill": "Azmerian Wolf", "set": "Effigy", "sup": ["Muster", "Loyalty", "Rapid Attacks II", "Feeding Frenzy II", "Minion Splash II"], "role": "DPS + Eternal Hunt"},
 {"skill": "Wild Protector", "set": "Asc.", "sup": ["Muster", "Rapid Attacks II", "Feeding Frenzy II", "Rage III", "Loyalty"], "role": "Tank + DPS"},
 {"skill": "Wolf Pack", "set": "—", "sup": ["Loyalty", "Rapid Attacks II", "Muster", "Feeding Frenzy II", "Rage III"], "role": "Vários corpos"},
 {"skill": "Spirit Vessel", "set": "Forgotten Warden", "sup": ["Furious Slam (socketada)", "Rapid Attacks II", "Minion Mastery", "Loyalty", "Feeding Frenzy II"], "role": "Companion grátis do body"},
 {"skill": "Tame Beast (Diretusk Boar / Plague Harvester)", "set": "—", "sup": ["Loyalty", "Muster", "Rapid Attacks II", "Minion Mastery", "Minion Splash II"], "role": "DPS / aura"},
 {"skill": "Tame Beast (aura: Haste / Physical)", "set": "—", "sup": ["Loyalty", "Meat Shield II", "Rage III", "Minion Mastery", "Romira's Requital"], "role": "Aura"},
 {"skill": "Freezing Mark / Sniper's Mark", "set": "—", "sup": ["Prolonged Duration II", "Efficiency II", "Charged Mark"], "role": "+dano em marcados (Effigy)"},
]
t15["cheap"] = ["Forgotten Warden base (~0,21 div) com Fox Idol", "Tyranny's Grip Runeforged continua ótima", "Lavianga's Spirits (~0,11 div) + Nascent Hope (~0,11 div)", "Darkness Enthroned (~0,014 div) com Greater Body Rune + rune de resist"]
t15["full"] = ["Chober Chaber Runeforged + Giant's Blood", "From Nothing (Vile Mending, Grip of Evil, Entropic Incarnation)", "Prism of Belief +1/+2 Tamed Companion", "Mind Over Matter com mana alta"]
t15["tree"] = "Mantenha Trusted Kinship. Keystones do meta: Giant's Blood (34%) e Mind Over Matter (27%). Notables mais comuns: Bond of the Wolf, Bond of the Mamba, Lord of Horrors, The Soul Meridian, Gigantic Following."
t15["avoid"] = ["Remover Trusted Kinship", "Pegar Idolatry enquanto depende de runas de resist (-4% por Augment que não é Idol)", "Corromper o Effigy antes de colocar os sockets"]
t15["exit"] = ["Effigy + Forgotten Warden", "Zekoa com Extra Crits ou Hasted", "Idolatry com 4+ Idols", "300+ Spirit (mediana dos top: ~330)"]

mm = _ph("mm")
mm["cheap"] = ["Mesma árvore do T15; troque Wind Dancer por Mana Remnants quando Evasion/Deflection já estiverem no cap", "Megalomaniac/Heart of the Well bem rolados (< 1 div)"]
mm["full"] = ["Morior Invictus (~6 div) com todos os sockets de Idol", "Prism of Belief +3 Tamed Companion", "Kalandra's Touch / Eshtera's Path", "Rite of Passage · Carved Majesty · Mageblood (luxo)"]

# milestones e diagnóstico
MILESTONES[35] = "RESPEC: Trusted Kinship + Easy Going. Sceptre com Spirit no offhand e Trenchtimbre na main-hand."
MILESTONES[65] = "The Catha's Balance + Tyranny's Grip Runeforged. Comece a juntar 1 div para o Sylvan's Effigy."
MILESTONES[67] = "Sylvan's Effigy (~1 div) com Primate Idol + Rabbit Idol. Azmerian Wolf entra."
MILESTONES[72] = "Caça ao Zekoa: Riverside/Rupture com Cruel Hegemony + tablets de mod extra."
MILESTONES[78] = "Forgotten Warden (~0,21 div): companions +vida e Spirit Vessel grátis."
MILESTONES[80] = "Wolf Pack + beast de aura. MANTENHA Trusted Kinship."
MILESTONES[84] = "Chober Chaber Runeforged + Giant's Blood (Treefingers/Vertex) no modo completo."
MILESTONES[86] = "From Nothing para Vile Mending / Grip of Evil / Entropic Incarnation."
_base.TROUBLESHOOT[:] = [x for x in TROUBLESHOOT if not x[0].startswith("Removi")] + [
 ("Tirei Trusted Kinship com o Effigy e o Spirit estourou", "Recoloque o keystone: os 30% more de reservation efficiency continuam valendo mesmo com companions ilimitados."),
 ("Não consigo equipar a Chober Chaber com Giant's Blood", "Os requisitos triplicam. Use The Vertex, Soul Core of Cholotl (40% vira Dex) ou atributos na árvore."),
 ("Zekoa com poucos mods", "Use tablets com 'Unique Monsters have 1 additional Rare Modifier' + Cruel Hegemony em Riverside/Rupture."),
]
BUY_ORDER[:] = [
 {"p": 1, "item": "Botas 25–30% Movement Speed", "phase": "Sempre", "cost": "Barato", "impact": "Qualidade de vida enorme"},
 {"p": 2, "item": "Resistências no cap + vida (anéis/cinto)", "phase": "Sempre", "cost": "Barato", "impact": "Sobrevivência"},
 {"p": 3, "item": "Trenchtimbre (+1 Minion Skills) + sceptre com Spirit", "phase": "Ato 3", "cost": "Barato (~0,02 div)", "impact": "Zoo mais forte logo no respec"},
 {"p": 4, "item": "Charms únicos: Beira's Anguish, Sanguis Heroum, Arakaali's Gift", "phase": "Ato 4", "cost": "Barato (< 0,02 div)", "impact": "Cobre ignite, bleed e poison"},
 {"p": 5, "item": "Tyranny's Grip Runeforged", "phase": "Nv 65 (Catha)", "cost": "Barato (~0,003 div)", "impact": "Maior salto de dano"},
 {"p": 6, "item": "Sylvan's Effigy + Primate Idol + Rabbit Idol", "phase": "Nv 67+", "cost": "Valor (~1,1 div)", "impact": "Zoo ilimitado + Azmerian Wolf"},
 {"p": 7, "item": "Forgotten Warden + Fox Idol", "phase": "Nv 78", "cost": "Valor (~0,4 div)", "impact": "Vida do zoo + Spirit Vessel"},
 {"p": 8, "item": "Lavianga's Spirits + Nascent Hope", "phase": "T15", "cost": "Valor (~0,2 div)", "impact": "Mana constante + ES"},
 {"p": 9, "item": "Chober Chaber Runeforged + Treefingers + The Vertex", "phase": "T15", "cost": "Valor (~0,5 div)", "impact": "+4 levels, +47 Spirit, dano por golpe"},
 {"p": 10, "item": "From Nothing + Prism of Belief (+2)", "phase": "T15+", "cost": "Valor → Luxo", "impact": "Notables de minion + levels no Zekoa"},
 {"p": 11, "item": "Morior Invictus / Kalandra's Touch / Mageblood", "phase": "Arbiter", "cost": "Luxo (6 → 570 div)", "impact": "Teto da build"},
]
# ------------------------------------------------------------------ SETS PRÓPRIOS (Ato 3+): uniques no set principal
def R(slot, name, mods, r=None): return {"slot": slot, "n": name, "u": 0, "mods": mods, "r": r or []}
def U(slot, name, r=None, note=""): return {"slot": slot, "n": name, "u": 1, "mods": [], "r": r or [], "note": note}
HELM = lambda lv, idol: R("Capacete", "Capacete rare de Evasion", [f"+{lv} to Level of all Minion Skills", "+70–100 to maximum Life", "+Resistências (fechar cap)", "% increased Evasion Rating"], [idol])
BODY = R("Body Armour", "Body rare de Evasion", ["+80–120 to maximum Life", "% increased Evasion Rating", "Gain Deflection Rating equal to X% of Evasion Rating", "+Resistências"], ["Runa de resistência"])
GLOV = R("Luvas", "Luvas rare", ["+60–90 to maximum Life", "+Resistências", "+Dexterity/Intelligence (requisitos)", "% increased Evasion Rating"])
BOOT = lambda ms: R("Botas", "Botas rare", [f"{ms}% increased Movement Speed", "+70–90 to maximum Life", "+Resistências", "Evasion / Deflection"], ["Runa de resistência"])
AMU = lambda lv, extra: R("Amuleto", "Amuleto rare", [f"+{lv} to Level of all Minion Skills", "+Spirit", "+Life", "+Resistências"] + extra)
RING = lambda k: R(k, "Anel rare", ["+Life", "+Resistências (o maior lugar para capar)", "+Atributos"])
BELT = R("Cinto", "Cinto rare", ["+Life", "+Resistências", "+Strength"])
SCEP = R("Offhand (Set 1)", "Sceptre rare", ["+30–60 to Spirit", "+1 to Level of all Minion Skills", "Allies in your Presence deal % increased Damage"], ["Primate Idol"])
CH_CHEAP = [U("Charm", "Beira's Anguish"), U("Charm", "Sanguis Heroum"), U("Charm", "Arakaali's Gift")]
SETS = {
 "a3": {"cheap": [U("Arma (Set 1)", "Trenchtimbre", note="+1 Minion Skills; dano da arma não importa até a Catha"), SCEP, HELM(1, "Runa de resistência"), BODY, GLOV, BOOT(20), AMU(1, []), RING("Anel E"), RING("Anel D"), U("Cinto", "Meginord's Girdle")],
        "full": [U("Arma (Set 1)", "Trenchtimbre", ["Runeforged"], "+2 Minion Skills na versão Runeforged"), SCEP, HELM(2, "Primate Idol"), BODY, GLOV, BOOT(25), AMU(2, []), RING("Anel E"), RING("Anel D"), BELT]},
 "a4": {"cheap": [U("Arma (Set 1)", "Trenchtimbre"), SCEP, U("Capacete", "Starkonja's Head", note="15% do dano vai para o companion"), BODY, GLOV, BOOT(25), AMU(1, []), RING("Anel E"), RING("Anel D"), U("Cinto", "Meginord's Girdle")] + CH_CHEAP,
        "full": [U("Arma (Set 1)", "Trenchtimbre", ["Runeforged"]), SCEP, HELM(2, "Primate Idol"), BODY, GLOV, BOOT(30), AMU(2, []), RING("Anel E"), RING("Anel D"), BELT] + CH_CHEAP},
 "int": {"cheap": [U("Arma (Set 1)", "Trenchtimbre"), SCEP, HELM(1, "Primate Idol"), BODY, GLOV, BOOT(30), AMU(1, []), U("Anel E", "Ventor's Gamble", note="role com resists positivas"), RING("Anel D"), BELT] + CH_CHEAP,
         "full": [U("Arma (Set 1)", "Trenchtimbre", ["Runeforged"]), SCEP, HELM(2, "Primate Idol"), BODY, GLOV, BOOT(30), AMU(2, []), U("Anel E", "Ventor's Gamble"), RING("Anel D"), BELT] + CH_CHEAP},
 "ea": {"cheap": [U("Arma (Set 1)", "Tyranny's Grip", ["Runeforged"], "Catha's Balance: 60% do dano por golpe vai para os companions"), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), U("Capacete", "Alpha's Howl", note="+100 Spirit enquanto a reserva apertar"), BODY, GLOV, BOOT(30), AMU(2, ["Anoint: Warlord Leader"]), U("Anel E", "Ventor's Gamble"), RING("Anel D"), BELT] + CH_CHEAP,
        "full": [U("Arma (Set 1)", "Chober Chaber", ["Runeforged", "Greater Rune of Leadership"], "+4 Minion Skills, +47 Spirit; precisa Giant's Blood"), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), U("Capacete", "The Vertex", note="tira requisitos de atributo"), BODY, U("Luvas", "Treefingers", note="Giant's Blood"), BOOT(30), AMU(3, ["Anoint: Warlord Leader"]), RING("Anel E"), RING("Anel D"), BELT] + CH_CHEAP},
 "t15": {"cheap": [U("Arma (Set 1)", "Tyranny's Grip", ["Runeforged"]), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), HELM(2, "Primate Idol"), U("Body Armour", "Forgotten Warden", ["Fox Idol", "Spirit Vessel: Furious Slam"]), GLOV, BOOT(30), AMU(2, ["Anoint: Warlord Leader"]), U("Anel E", "Ventor's Gamble"), RING("Anel D"), U("Cinto", "Darkness Enthroned", ["Socket 1: Greater Body Rune (vida)", "Socket 2: Greater Desert, Glacial ou Storm Rune (a resist que faltar)"], "Idols não entram: Idol of Ralakesh e Primate Idol são só de Capacete ou Sceptre"), U("Flask mana", "Lavianga's Spirits"), U("Charm", "Nascent Hope"), U("Charm", "Beira's Anguish"), U("Charm", "Sanguis Heroum")],
         "full": [U("Arma (Set 1)", "Chober Chaber", ["Runeforged", "Greater Rune of Leadership"]), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), U("Capacete", "The Vertex"), U("Body Armour", "Forgotten Warden", ["Fox Idol", "Spirit Vessel: Furious Slam"]), U("Luvas", "Treefingers"), BOOT(30), AMU(3, ["Anoint: The Soul Meridian"]), RING("Anel E"), RING("Anel D"), U("Cinto", "Darkness Enthroned", ["Socket 1: Greater Body Rune (vida)", "Socket 2: Greater Desert, Glacial ou Storm Rune (a resist que faltar)"], "Idols não entram: Idol of Ralakesh e Primate Idol são só de Capacete ou Sceptre"), U("Flask mana", "Lavianga's Spirits"), U("Charm", "Nascent Hope"), U("Charm", "The Fall of the Axe"), U("Charm", "Sanguis Heroum")]},
 "mm": {"cheap": [U("Arma (Set 1)", "Tyranny's Grip", ["Runemastered"]), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), HELM(2, "Primate Idol"), U("Body Armour", "Forgotten Warden", ["Fox Idol", "Spirit Vessel: Furious Slam"]), GLOV, BOOT(30), AMU(3, ["Anoint: Warlord Leader"]), U("Anel E", "Ventor's Gamble"), RING("Anel D"), U("Cinto", "Darkness Enthroned", ["Socket 1: Greater Body Rune (vida)", "Socket 2: Greater Desert, Glacial ou Storm Rune (a resist que faltar)"], "Idols não entram: Idol of Ralakesh e Primate Idol são só de Capacete ou Sceptre"), U("Flask mana", "Lavianga's Spirits"), U("Charm", "Nascent Hope"), U("Charm", "Beira's Anguish"), U("Charm", "Sanguis Heroum")],
        "full": [U("Arma (Set 1)", "Chober Chaber", ["Runeforged", "Greater Rune of Leadership"]), U("Offhand (Set 1)", "Sylvan's Effigy", ["Primate Idol", "Rabbit Idol"]), U("Capacete", "The Vertex"), U("Body Armour", "Morior Invictus", ["Idols em todos os sockets"]), U("Luvas", "Treefingers"), BOOT(30), AMU(4, ["Anoint: The Soul Meridian"]), U("Anel E", "Kalandra's Touch"), RING("Anel D"), U("Cinto", "Mageblood"), U("Flask mana", "Lavianga's Spirits"), U("Charm", "Rite of Passage"), U("Charm", "The Fall of the Axe"), U("Charm", "Nascent Hope")]},
}
JEWEL_SETS = {"ea": ["Sapphire rare: Minions Critical Damage Bonus + Minion Damage + Companion Life"], "t15": ["From Nothing (Vile Mending / Grip of Evil)", "Prism of Belief +1/+2 Tamed Companion", "Sapphires de minion crit"], "mm": ["From Nothing", "Prism of Belief +3", "Megalomaniac / Heart of the Well bem rolados"]}

# textos que ainda falavam de dano do jogador depois do respec
a3["tree"] = "Respec no nível ~35: árvore 100% de companion. Caminho: Trusted Kinship → Easy Going → Bonds (Cat, Mamba, Ape, Viper, Wolf) → Long Distance Relationship → Blur. Inspiring Ally é só nó de passagem para o Easy Going (no zoo não dá dano). Pontos de Weapon Set: deixe para depois ou use em nós de companion — nunca em ataque."
a3["stats"] = ["Movement Speed", "+Minion Skills", "Spirit", "Vida", "Resistências", "Evasion"]
_ph("a4")["stats"] = ["Movement Speed", "+Minion Skills", "Spirit", "Vida", "Resistências", "Evasion", "Deflection"]
_ph("int")["stats"] = ["Movement Speed", "+Minion Skills", "Spirit", "Vida", "Resistências (cap 75%)", "Evasion", "Deflection"]
_ph("a4")["tree"] = "Continue a árvore de companion: Bond of the Wolf, Sturdy Ally, Captivating Companionship e jewel sockets (vida/dano de companion)."
_ph("int")["tree"] = "Lord of Horrors (+12% eficiência de reserva de minion) e mais jewel sockets. Atributos só o necessário para gems e itens."
ea["tree"] = "Vile Mending, Grip of Evil, Entropic Incarnation e Unstable Bond (cluster de minion). Giant's Blood só no modo completo (ou via Treefingers). Mantenha Trusted Kinship e Easy Going para sempre."
for kp in KEY_PASSIVES:
    if kp["node"] == "Inspiring Ally":
        kp.update(text="Aumentos de dano de Companion também valem para você.", when="Ato 2 (e passagem no Ato 3)", why="Útil só no Ato 2, enquanto você ainda bate de spear. No zoo é apenas o nó de passagem até o Easy Going.")
GEAR[:] = [g for g in GEAR]

_G = {g["slot"]: g for g in GEAR}
_G["Main-hand"].update(cheap="Campanha: spear rare. Ato 3: Trenchtimbre. Nv 65: Tyranny's Grip Runeforged (~0,003 div)",
    value="Tyranny's Grip Runemastered (~0,41 div) ou Trenchtimbre Runeforged", full="Chober Chaber Runeforged + Giant's Blood (Treefingers/keystone) + The Vertex",
    note="Catha's Balance: companions ganham 60% do dano da main-hand. 32% dos zoos com Effigy usam maça de 2 mãos + sceptre.")
_G["Offhand"].update(cheap="Campanha: escudo. Ato 3+: sceptre rare com Spirit", value="Sylvan's Effigy (~0,95 div) com Primate Idol + Rabbit Idol",
    full="Sylvan's Effigy com Primate + Rabbit Idol", note="Com ~1 div o Effigy entra logo no início do Atlas.")
_G["Capacete"].update(value="+1/+2 Minion Skills com Idol of Ralakesh, ou Alpha's Howl (+100 Spirit) se faltar reserva",
    full="+2 Minion Skills com Idol of Ralakesh, ou The Vertex para a Chober Chaber", note="Starkonja's Head é defesa barata na campanha.")
_G["Body Armour"].update(value="Forgotten Warden (~0,21 div) com Fox Idol", full="Forgotten Warden Runemastered ou Morior Invictus (~6 div)",
    note="Forgotten Warden em 80% dos zoos: vida do zoo + Spirit Vessel grátis.")
_G["Luvas"].update(value="Treefingers (Giant's Blood) se usar maça de 2 mãos", full="Rare de Evasion/Deflection, Horror's Flight, ou Carved Majesty nas luvas")
_G["Anéis"].update(value="Ventor's Gamble com resists positivas (+vida +Spirit)", full="Kalandra's Touch copiando um rare perfeito")
_G["Cinto"].update(value="Rare vida/resist ou Darkness Enthroned (Greater Body Rune + rune de resist)", full="Darkness Enthroned (Greater Body Rune + rune de resist) · Mageblood (luxo)")
_G["Jewels"].update(value="From Nothing (~0,21 div) + Sapphires de minion crit", full="From Nothing + Prism of Belief +2/+3 + Megalomaniac/Heart of the Well")
_G["Charms"].update(cheap="Beira's Anguish · Sanguis Heroum · Arakaali's Gift (todos < 0,02 div)", value="Nascent Hope · The Fall of the Axe", full="Rite of Passage (luxo)")
_G["Flasks"].update(value="Lavianga's Spirits (mana constante)", full="Lavianga's Spirits + life flask de recuperação instantânea")
TRICKS[:0] = EXTRA_TRICKS
FIXES += ["Guia base mandava tirar Trusted Kinship com o Effigy: o meta (99%) mantém.", "Effigy tratado como luxo: custa ~1 div na Forbidden Rites.", "Uniques do meta adicionados: Forgotten Warden, Chober Chaber, The Vertex, Treefingers, Alpha's Howl etc."]
SOURCES += [("poe.ninja — Spirit Walker Forbidden Rites (builds + economia)", "Uso real de uniques, keystones, companions e preços", "https://poe.ninja/poe2/builds/forbiddenrites?class=Spirit%20Walker"),
            ("poe-vault — Spiritwalker Boss Companion Endgame", "Zekoa, mods desejados, reroll com Doryani", "https://www.poe-vault.com/poe2/huntress/spirit-walker/tamed-boss-beast-build-guide")]

# preços / ícones da economia
def _eco():
    out = {}
    for f in glob.glob("dl/eco_*.json"):
        for l in json.load(open(f, encoding="utf-8")).get("lines", []):
            k = l["name"]; bt = l["baseType"]
            cur = out.get(k)
            if not cur or not bt.startswith(("Runemastered", "Runeforged")):
                out[k] = {"price": l["primaryValue"], "icon": l["icon"], "base": bt.replace("Runemastered ", "").replace("Runeforged ", ""), "lvl": l.get("levelRequired"),
                          "mods": [re.sub(r"\[([^|\]]+\|)?([^\]]+)\]", r"\2", m["text"]) for m in l.get("explicitModifiers", [])]}
    ex = json.load(open("dl/ex_Idols.json", encoding="utf-8"))
    names = {i["id"]: i for i in ex["items"]}
    for l in ex["lines"]:
        i = names[l["id"]]; out[i["name"]] = {"price": l["primaryValue"], "icon": ("https://web.poecdn.com" + i["image"]) if i.get("image") else None, "base": "Idol", "lvl": None, "mods": []}
    return out
ECO = _eco()
for u in UNIQUES:
    e = ECO.get(u["n"], {})
    u["price"] = round(e["price"], 3) if e.get("price") is not None else None
    u["base"] = e.get("base", ""); u["mods"] = [m for m in e.get("mods", []) if "\n" not in m][:7]; u["iconUrl"] = e.get("icon")
    if u["n"] == "Prism of Belief": u["mods"] = ["+(1-3) to Level of all Tamed Companion Skills (versão para a build)"]
    if u["n"] == "From Nothing": u["mods"] = ["Passives in Radius of (keystone) can be Allocated without being connected to your tree"]
    if u["n"] == "Flesh Crucible": u["mods"] = ["Concede 1 keystone aleatório (procure Giant's Blood)", "(10-20)% less de um atributo defensivo/ofensivo"]
    if u["n"] == "Megalomaniac": u["mods"] = ["Aloca notables aleatórios (enchant)"]
    u["tier"] = "Barato" if (u["price"] or 0) < 0.1 else "Valor" if (u["price"] or 0) < 3 else "Luxo"
    if u["n"] == "Prism of Belief": u["tier"] = "Valor"
for i in IDOLS:
    e = ECO.get(i["n"], {}); i["iconUrl"] = e.get("icon")
    if e.get("price") is not None: i["price"] = round(e["price"], 3)

DATA = dict(league=LEAGUE, patch=PATCH, updated=UPDATED, phases=PHASES, milestones=MILESTONES, gear=GEAR, beasts=BEASTS,
            auraPriority=AURA_PRIORITY, ascendancy=ASCENDANCY, keyPassives=KEY_PASSIVES, treeStages=TREE_STAGES,
            quests=[dict(act=a, area=b, boss=c, reward=d, prio=e) for a, b, c, d, e in QUESTS],
            tricks=TRICKS, troubleshoot=[dict(q=a, a=b) for a, b in _base.TROUBLESHOOT], atlas=ATLAS,
            atlasCheck=[dict(stage=a, goal=b, gear=c) for a, b, c in ATLAS_CHECK], buyOrder=BUY_ORDER,
            current=CURRENT_SETUP, sources=[dict(name=a, use=b, url=c) for a, b, c in SOURCES], fixes=FIXES,
            meta=META, sets=SETS, jewelSets=JEWEL_SETS, uniques=UNIQUES, idols=IDOLS, optimizations=OPTIMIZATIONS, snap=SNAP)
TROUBLESHOOT = _base.TROUBLESHOOT

if __name__ == "__main__":
    print(len(UNIQUES), [(u["n"], u["price"], u["tier"], bool(u["iconUrl"])) for u in UNIQUES])
    print([(i["n"], i["price"], bool(i["iconUrl"])) for i in IDOLS])
