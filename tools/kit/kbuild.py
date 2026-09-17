# -*- coding: utf-8 -*-
"""Gera <bid>/index.html (PT), <bid>/en.html (EN) e <bid>/assets/assets.js na raiz do repositório.  Uso: python kbuild.py <bid>"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
os.chdir(ROOT); sys.path.insert(0, ROOT); sys.path.insert(0, HERE)
import chober as SF          # só para reaproveitar quests e traduções comuns
from enhance import enhance
import timing, hunting
from ui_en import UI
import common
BID = sys.argv[1]
D = common.load_build(BID)
BDIR = os.path.join(ROOT, "builds", BID)

OUT = os.path.join(ROOT, "..", D.CONFIG["dir"])
os.makedirs(OUT + "/assets", exist_ok=True)
safe = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

DATA_PT = D.build(SF.DATA["quests"])
src = json.load(open("i18n_src.json", encoding="utf-8")); en = {}
for f in ["i18n/en_1.json", "i18n/en_2.json", "i18n/en_3.json"]:
    en.update(json.load(open(f, encoding="utf-8")))
MAP = {src[k]: v for k, v in en.items()}
MAP.update(json.load(open("i18n/en_extra.json", encoding="utf-8")))
MAP.update(timing.EN_PAIRS); MAP.update(hunting.EN_PAIRS); MAP.update(D.EN_PAIRS)
SUBS = [(r"(\d),(\d)", r"\1.\2")]
SKIP = {"ic", "iconUrl", "url", "img", "id", "p", "skill", "sup"}
def tr(s):
    if s in MAP: return MAP[s]
    if " ; " in s: return " ; ".join(tr(x) for x in s.split(" ; "))
    for a, b in SUBS: s = re.sub(a, b, s)
    return s
def walk(o, key=None):
    if isinstance(o, dict): return {k: (v if k in SKIP else walk(v, k)) for k, v in o.items()}
    if isinstance(o, list): return [walk(v, key) for v in o]
    if isinstance(o, str): return tr(o)
    return o
DATA_EN = walk(DATA_PT)
DATA_EN["supWhy"] = {k: tr(v) for k, v in DATA_PT["supWhy"].items()}
DATA_EN["milestones"] = {k: tr(v) for k, v in DATA_PT["milestones"].items()}

A = json.load(open(os.path.join(BDIR, "assets.json"), encoding="utf-8"))
A_EN_TXT = {"sets": walk(A["sets"]), "guide": walk(A["guide"])}
open(OUT + "/assets/assets.js", "w", encoding="utf-8").write("window.__A=" + safe(A) + ";\nwindow.__IMG={};\n")

tpl = open(os.path.join(BDIR, "app_template.html"), encoding="utf-8").read()
HEAD = '<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>__EMOJI__</text></svg>">\n'
TXT = D.TXT
def page(lang):
    t = tpl
    if lang == "en":
        for a, b in sorted(UI, key=lambda p: -len(p[0])):
            t = t.replace(a, b)
    tabs = D.TABS
    t = t.replace("__TABS__", json.dumps([[a, pt if lang == "pt" else en] for a, pt, en in tabs], ensure_ascii=False))
    for k, v in TXT[lang].items():
        t = t.replace(f"__{k}__", v)
    data = DATA_PT if lang == "pt" else DATA_EN
    assets_expr = "window.__A" if lang == "pt" else "Object.assign(window.__A," + safe(A_EN_TXT) + ")"
    t = (t.replace("__LANG__", lang).replace("__DATA__", safe(data)).replace("__ASSETS__", assets_expr).replace("__IMG__", "window.__IMG")
          .replace("__PT_HREF__", "index.html").replace("__EN_HREF__", "en.html")
          .replace("__PT_ON__", "on" if lang == "pt" else "").replace("__EN_ON__", "on" if lang == "en" else ""))
    t = t.replace("<script>\nconst LANG =", '<script src="assets/assets.js"></script>\n<script>\nconst LANG =', 1)
    assert 'src="assets/assets.js"' in t
    t = t.replace("__PILL__", D.CONFIG["pill"])
    t = enhance(t, lang, D.CONFIG["build"])
    i = t.index("</style>") + len("</style>")
    home = '<a class="homebtn" href="../%s">%s</a>' % ("index.html" if lang == "pt" else "en.html", "← Builds")
    body = t[i:].replace('<div class="eyebrow">', '<div class="eyebrow">' + home, 1)
    return HEAD.replace("__EMOJI__", D.CONFIG["emoji"]).format(lang="pt-BR" if lang == "pt" else "en") + t[:i] + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n"

open(OUT + "/index.html", "w", encoding="utf-8").write(page("pt"))
open(OUT + "/en.html", "w", encoding="utf-8").write(page("en"))
# sobras de PT no EN (strings de dados)
PT = re.compile(r"[ãõçÇ]|\b(não|você|para|com|mais|sem|dano|vida|nível|fase|seu|sua|agora|árvore|itens|preço|barato|completo|quando|depois|antes|também|então|está|são)\b", re.I)
left = set()
def scan(o):
    if isinstance(o, dict): [scan(v) for k, v in o.items() if k not in SKIP]
    elif isinstance(o, list): [scan(v) for v in o]
    elif isinstance(o, str) and PT.search(o): left.add(o[:120])
scan(DATA_EN); scan(A_EN_TXT)
print("EN data leftovers:", len(left)); [print("  -", x) for x in sorted(left)[:40]]
print("sizes:", {f: os.path.getsize(OUT + "/" + f) for f in ["index.html", "en.html", "assets/assets.js"]})
