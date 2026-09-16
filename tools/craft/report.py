# -*- coding: utf-8 -*-
"""Relatório de mods por item alvo (pesos publicados, não validados, do PoE2DB) para escrever as receitas."""
import re, sys
import db

ITEMS = {
 "amulet": ("Amulets", r"spirit|level of all (spell|minion)|maximum mana|maximum life|resist|attributes|cast speed|mana regen|evasion|energy shield"),
 "ring": ("Rings", r"maximum life|maximum mana|resist|cast speed|mana regen|attributes|intelligence|dexterity|strength|minion"),
 "belt": ("Belts", r"maximum life|maximum mana|resist|charm|flask|strength|stun"),
 "helm_int": ("Helmets_int", r"energy shield|maximum life|maximum mana|resist|minion|level"),
 "helm_dexint": ("Helmets_dex_int", r"evasion|energy shield|maximum life|maximum mana|resist|minion|level|deflect"),
 "body_int": ("Body_Armours_int", r"energy shield|maximum life|maximum mana|resist|spirit|intelligence|mana before"),
 "body_dex": ("Body_Armours_dex", r"evasion|maximum life|resist|spirit|deflect|regen"),
 "gloves_int": ("Gloves_int", r"energy shield|maximum life|maximum mana|resist|per enemy|cast"),
 "gloves_dex": ("Gloves_dex", r"evasion|maximum life|resist|deflect|attributes|dexterity|strength|intelligence"),
 "boots_int": ("Boots_int", r"movement|energy shield|maximum life|maximum mana|resist|spirit"),
 "boots_dex": ("Boots_dex", r"movement|evasion|maximum life|resist|deflect|spirit"),
 "wand": ("Wands", r"spell|mana|level|cast|intelligence|minion"),
 "sceptre": ("Sceptres", r"spirit|mana|allies|minion|level|presence|aura"),
 "mace2h": ("Two_Hand_Maces", r"physical|attack speed|attributes|strength|accuracy|augment"),
}

def tiers_at(page, pattern, ilvl=82, kind="normal"):
    ms = [m for m in db.pool(page, [], kind) if m["level"] <= ilvl]
    tot = {g: sum(m["weight"] for m in ms if m["gen"] == g) for g in ("Prefix", "Suffix")}
    rx = re.compile(pattern, re.I)
    fam = {}
    for m in ms:
        if rx.search(m["text"]):
            key = (m["gen"], m["family"], re.sub(r"[\d.]+", "#", re.sub(r"\([\d.]+-[\d.]+\)", "#", m["text"])))
            fam.setdefault(key, []).append(m)
    return tot, fam

def report(key, ilvl=82):
    page, pat = ITEMS[key]
    print("#" * 8, key, page, "ilvl", ilvl)
    tot, fam = tiers_at(page, pat, ilvl)
    print("pool total", tot)
    for (g, f, label), l in sorted(fam.items(), key=lambda kv: (kv[0][0], -sum(m['weight'] for m in kv[1]))):
        l.sort(key=lambda m: -m["level"])
        w = sum(m["weight"] for m in l)
        t1 = l[0]
        print(f" [{g[0]}] {label[:70]:70} fam {100*w/max(1,tot[g]):5.1f}% | T1 {t1['text'][:60]} ilvl{t1['level']} ({100*t1['weight']/max(1,tot[g]):.2f}%)" + (f" | T2 {l[1]['text'][:40]} ilvl{l[1]['level']}" if len(l) > 1 else ""))
    for kind in ("desecrated", "essence", "perfect_essence", "corruption_upgrade", "breach_minion", "breach_caster"):
        ms = db.pool(page, [], kind)
        if not ms:
            continue
        print(" --", kind, len(ms))
        for m in ms:
            if kind == "essence" and m["level"] < 40:
                continue
            print(f"    [{m['gen'][:1]}] L{m['level']:>2} {m['name'][:38]:38} {m['text'][:110]}")

if __name__ == "__main__":
    for k in (sys.argv[1:] or ITEMS):
        report(k)
