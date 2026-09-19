# -*- coding: utf-8 -*-
"""Gera o loot filter do Whirling Glacial Bolt (Mercenary · Gemling Legionnaire) para o PoE 2.

Saída:
  whirling/whirling-glacial-bolt.filter   — só a camada da build (funciona sozinha e pode ser colada no topo de qualquer filtro)
  --install [ARQUIVO_BASE]                — copia a camada da build por cima de um filtro base (padrão: o NeverSink online já baixado pelo jogo)
                                            e grava em Documents/My Games/Path of Exile 2/WhirlingGlacialBolt.filter

A camada fica NO TOPO: o primeiro bloco que casa decide, então os itens da build ganham destaque antes do filtro base e as armas que a
build nunca usa (normal/mágico) somem. Nomes de base/gema/runa seguem o que o próprio filtro NeverSink usa."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "..")
OUT = os.path.join(REPO, "whirling", "whirling-glacial-bolt.filter")
DOCS = os.path.join(os.path.expanduser("~"), "Documents", "My Games", "Path of Exile 2")

ICE = "111 214 255 255"
DEEP = "8 34 62 255"

# uniques da build por base (o filtro só enxerga a base; confira o nome do unique ao pegar)
UNIQ_BASES = {"Tense Crossbow": "Rampart Raptor", "Winged Spear": "Skysliver", "Garment": "Tabula Rasa", "Iron Ring": "Blackheart", "Rawhide Belt": "Meginord's Girdle",
              "Wrapped Sandals": "Wanderlust", "Spired Greathelm": "Thrillsteel", "Grand Regalia": "Morior Invictus"}
LINEAGE = ["Ahn's Citadel", "Kaom's Madness", "Vorana's Siege", "Rakiata's Flow", "Rigwald's Ferocity", "Uhtred's Augury", "Dialla's Desire"]
RUNES = ["Lesser Glacial Rune", "Glacial Rune", "Greater Glacial Rune", "Perfect Glacial Rune"]
# (classe do gem, nível, o que é) — Uncut Skill/Spirit Gem: o nível do gem é o tier da skill
GEMS = [("Uncut Skill Gem", 7, "Glacial Bolt: a skill principal do nível 24 ao 100"), ("Uncut Skill Gem", 11, "Emergency Reload / Seismic Cry"), ("Uncut Skill Gem", 3, "Pounce (endgame)"),
        ("Uncut Spirit Gem", 4, "Herald of Ice · War Banner · Scavenged Plating · Arctic Armour (30 Spirit cada)"), ("Uncut Spirit Gem", 14, "Berserk (endgame)")]
CRAFT_BASES = [("Crossbows", "Desolate Crossbow", 82, "Glacial Bolt no endgame"), ("Helmets", "Imperial Greathelm", 82, "Capacete de Armour"), ("Gloves", "Massive Mitts", 78, "Luvas de Armour"),
               ("Boots", "Vaal Greaves", 82, "Botas de Armour (35% de movimento)"), ("Amulets", "Absent Amulet", 75, "Spirit para as reservas")]


def show(title, conds, size=42, text=ICE, border=ICE, bg=None, sound="2 300", effect="Cyan", icon="1 Cyan Triangle"):
    lines = [f"Show # {title}"] + [f"\t{c}" for c in conds] + [f"\tSetFontSize {size}", f"\tSetTextColor {text}", f"\tSetBorderColor {border}"]
    if bg:
        lines.append(f"\tSetBackgroundColor {bg}")
    if sound:
        lines.append(f"\tPlayAlertSound {sound}")
    if effect:
        lines.append(f"\tPlayEffect {effect}")
    if icon:
        lines.append(f"\tMinimapIcon {icon}")
    return "\n".join(lines) + "\n"


def layer():
    o = ["#===============================================================================================================",
         "# WHIRLING GLACIAL BOLT — Mercenary · Gemling Legionnaire (guia: grimorio-de-builds / whirling)",
         "# Camada da build: destaca o que a build usa e esconde armas normais/mágicas que ela nunca usa.",
         "# Cores: azul-gelo = peça da build. Para desligar o esconde-armas, apague o bloco 'Hide' no fim desta camada.",
         "#===============================================================================================================", ""]
    o.append("# --- Uniques da build (o filtro enxerga só a base; confira o nome: " + ", ".join(f"{b} = {u}" for b, u in UNIQ_BASES.items()) + ")")
    o.append(show("build: uniques", ["Rarity Unique", 'BaseType == ' + " ".join(f'"{b}"' for b in UNIQ_BASES)], 45, bg=DEEP, sound="2 300", effect="Cyan", icon="0 Cyan Star"))
    o.append("# --- Spear branca: a Whirling Slash precisa de uma spear no Weapon Set 1 desde o nível 1")
    o.append(show("build: spear branca do começo", ["AreaLevel <= 20", 'Class == "Spears"', "Rarity Normal"], 40, bg=None, sound="2 200", effect="Cyan Temp", icon="1 Cyan Diamond"))
    o.append("# --- Gems que viram peça da build (o nível do Uncut é o tier da skill)")
    for cls, lv, why in GEMS:
        o.append(show(f"build: {cls} nível {lv} — {why}", [f"GemLevel {lv}", f'BaseType "{cls}"'], 44, bg=DEEP, sound="2 300", effect="Cyan", icon="0 Cyan Triangle"))
    o.append(show("build: suportes Uncut de tier baixo (I–V)", ["GemLevel >= 1", "GemLevel <= 5", 'BaseType "Uncut Support Gem"'], 40, sound="2 200", effect="Cyan Temp", icon="1 Cyan Circle"))
    o.append("# --- Suportes de Lineage do endgame")
    o.append(show("build: Lineage", ['Class == "Skill Gems" "Support Gems"', "BaseType == " + " ".join(f'"{n}"' for n in LINEAGE)], 45, bg=DEEP, sound="2 300", effect="Cyan", icon="0 Cyan Star"))
    o.append("# --- Runas de gelo (arma) ")
    o.append(show("build: runas de gelo", ['Class == "Augment"', "BaseType == " + " ".join(f'"{n}"' for n in RUNES)], 40, sound="2 200", effect="Cyan Temp", icon="1 Cyan Square"))
    o.append("# --- Bases de craft do endgame (ilvl alto, só de mapas em diante)")
    for cls, base, ilvl, why in CRAFT_BASES:
        o.append(show(f"build: {base} — {why}", ["AreaLevel >= 65", f"ItemLevel >= {ilvl}", f'Class == "{cls}"', f'BaseType == "{base}"', "Rarity Normal Magic Rare"], 40, sound="2 200", effect="Cyan Temp", icon="2 Cyan Diamond"))
    o.append("# --- Anéis rare do leveling (~30 e ~50): dano adicionado, vida e resistências")
    o.append(show("build: anéis rare do leveling", ["AreaLevel <= 65", 'Class == "Rings"', "Rarity Rare"], 40, sound="2 200", effect=None, icon="2 Cyan Diamond"))
    o.append("# --- Esconde armas normais/mágicas que a build não usa (spear e besta ficam; Talisman fica para o Pounce)")
    o.append('Hide # build: armas e off hands que a build nunca usa\n\tRarity Normal Magic\n\tClass == "Bows" "Wands" "Staves" "Quarterstaves" "Sceptres" "Foci" "Quivers" "One Hand Maces" "Two Hand Maces" "Bucklers" "Shields"\n')
    o.append("#===============================================================================================================\n# FIM DA CAMADA DA BUILD\n#===============================================================================================================\n")
    return "\n".join(o)


def newest_online():
    d = os.path.join(DOCS, "OnlineFilters")
    files = [os.path.join(d, f) for f in os.listdir(d)] if os.path.isdir(d) else []
    return max(files, key=os.path.getmtime) if files else None


def main():
    text = layer()
    open(OUT, "w", encoding="utf-8", newline="\n").write(text)
    print("camada:", os.path.relpath(OUT, REPO), len(text.splitlines()), "linhas")
    if "--install" in sys.argv:
        args = [a for a in sys.argv[1:] if a != "--install"]
        base = args[0] if args else newest_online()
        if not base or not os.path.isfile(base):
            sys.exit("filtro base não encontrado")
        b = open(base, encoding="utf-8").read()
        b = re.sub(r"\A(?:#(?:Online Item Filter|name|version|realm|errors|hash|filterVersion|filterType|lastUpdate|monthTimeStamp)[^\n]*\n)+", "", b)   # metadados do filtro online
        dest = os.path.join(DOCS, "WhirlingGlacialBolt.filter")
        open(dest, "w", encoding="utf-8", newline="\n").write(text + "\n# ===== FILTRO BASE (" + os.path.basename(base) + ") =====\n" + b)
        print("instalado:", dest, os.path.getsize(dest), "bytes")


if __name__ == "__main__":
    main()
