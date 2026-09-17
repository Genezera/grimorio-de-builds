# -*- coding: utf-8 -*-
"""Blocos comuns dos dados de build (mesmo formato do odata.py do Oracle): textos PT/EN, gems, uniques, timing."""
import glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")


class Book:
    """Um por build: guarda os pares PT→EN e as tabelas que o template espera."""

    def __init__(self):
        self.EN_PAIRS = {}
        self.TIMING = []

    def L(self, pt, en):
        if pt != en:
            self.EN_PAIRS[pt] = en
        return pt

    def G(self, skill, sup, role, why, sp=None, pr=0, cost=None, until=None, since=None):
        g = {"skill": skill, "set": "—", "sup": list(sup), "role": role, "why": why}
        if sp:
            g.update(sp=sp, pr=pr, cost=cost or self.L("Sem Spirit", "No Spirit"))
        if until:
            g["until"] = until
        if since:
            g["since"] = since
        return g

    def U(self, n, slot, cat, p, why, how, alt, lvl=None):
        e = ECO.get(n, {})
        price = round(e["price"], 3) if e.get("price") is not None else None
        return dict(n=n, slot=slot, cat=cat, lvl=lvl, p=p, use=None, rf="", why=why, how=how, alt=alt, price=price, base=e.get("base", ""),
                    mods=e.get("mods", []), iconUrl=e.get("icon"), tier="Barato" if (price or 0) < 0.1 else "Valor" if (price or 0) < 3 else "Luxo")

    def T(self, kind, n, lvl, req, when, gives, early, late, steps=(), watch=()):
        self.TIMING.append(dict(kind=kind, n=n, lvl=lvl, req=req, when=when, gives=gives, early=early, late=late, steps=list(steps), watch=list(watch)))

    def common_pairs(self):
        L = self.L
        L("Flask vida", "Life flask"); L("Flask mana", "Mana flask"); L("Barato", "Cheap"); L("Valor", "Value"); L("Luxo", "Luxury")
        L("Sem Spirit", "No Spirit")
        L("Runa de resistência que faltar", "Whatever resistance rune you're missing")
        L("Soul Core/runa de resistência que faltar", "Whatever resistance Soul Core/rune you're missing")
        L("Runa de resistência que faltar (Desert = fogo · Glacial = frio · Storm = raio) · resist no cap: Body Rune (vida)",
          "Whatever resistance rune you're missing (Desert = fire · Glacial = cold · Storm = lightning) · resists capped: Body Rune (life)")


def _eco():
    out = {}
    for f in glob.glob(os.path.join(ROOT, "dl", "eco_*.json")):
        for l in json.load(open(f, encoding="utf-8")).get("lines", []):
            bt = l["baseType"]
            if l["name"] in out and bt.startswith(("Runemastered", "Runeforged")):
                continue
            out[l["name"]] = {"price": l.get("primaryValue"), "icon": l.get("icon"), "base": bt.replace("Runemastered ", "").replace("Runeforged ", ""),
                              "mods": [re.sub(r"\[([^|\]]+\|)?([^\]]+)\]", r"\2", m["text"]) for m in l.get("explicitModifiers", []) if "\n" not in m["text"]][:7]}
    return out


ECO = _eco()


def variants(bid):
    V = json.load(open(os.path.join(ROOT, "dl", f"{bid}_variants.json"), encoding="utf-8"))
    return V, {v["name"]: v for v in V["variants"]}


def load_build(bid):
    import importlib.util
    path = os.path.join(ROOT, "builds", bid, "bdata.py")
    spec = importlib.util.spec_from_file_location(f"bdata_{bid}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ensure_own(data):
    """Garante que toda unique do plano tenha caixinha em "Meu personagem" (usado pelo build e pela auditoria)."""
    own = data["char"]["own"]
    have = {k for _, k, _ in own} | {lbl for _, _, lbl in own}
    ordem = {p["id"]: i for i, p in enumerate(data["phases"])}
    novas = [u for u in sorted(data["uniques"], key=lambda u: (ordem.get(u.get("p"), 99), u["n"])) if u["n"] not in have]
    for i, u in enumerate(novas):
        own.insert(i, ["gear", u["n"], u["n"]])
    return len(novas)
