"""Gera o site (index.html PT + en.html EN + assets/) na pasta OUT."""
import json, base64, re, os, sys, shutil
import chober as D
from enhance import enhance
from ui_en import UI

OUT = sys.argv[1] if len(sys.argv) > 1 else "../silverfist"
os.makedirs(OUT + "/assets", exist_ok=True)
safe = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

# ---------- tradução dos dados
src = json.load(open("i18n_src.json", encoding="utf-8"))
en = {}
for f in ["i18n/en_1.json", "i18n/en_2.json", "i18n/en_3.json"]:
    en.update(json.load(open(f, encoding="utf-8")))
MAP = {src[k]: v for k, v in en.items()}
MAP.update(json.load(open("i18n/en_extra.json", encoding="utf-8")))
import unique_fill, sf_jewels
MAP.update(unique_fill.EN_PAIRS)
import timing
MAP.update(timing.EN_PAIRS)
import hunting
MAP.update(hunting.EN_PAIRS)
SUBS = [
    (r"\(\+(\d+) mods de ataque/utilidade que não importam para o zoo\)", r"(+\1 attack/utility mods that don't matter for the zoo)"),
    (r"\(\+1 mod de ataque/utilidade que não importa para o zoo\)", "(+1 attack/utility mod that doesn't matter for the zoo)"),
    (r"Resistências", "Resistances"),
    (r"Liga Forbidden Rites", "Forbidden Rites league"),
    (r"Spirit Vessel do ", "Spirit Vessel from "),
    (r" com ", " with "),
    (r"(\d),(\d)", r"\1.\2"),
]
SKIP = {"ic", "iconUrl", "url", "img", "id", "p"}

def tr(s):
    if s in MAP:
        return MAP[s]
    if " ; " in s:
        return " ; ".join(tr(x) for x in s.split(" ; "))
    for a, b in SUBS:
        s = re.sub(a, b, s)
    return s

def walk(o):
    if isinstance(o, dict):
        return {k: (v if k in SKIP else walk(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [walk(v) for v in o]
    if isinstance(o, str):
        return tr(o)
    return o

DATA_PT = D.DATA
DATA_EN = walk(D.DATA)
DATA_EN["atlas"] = {tr(k): walk(v) for k, v in D.DATA["atlas"].items()}
DATA_EN["supWhy"] = {k: tr(v) for k, v in D.DATA["supWhy"].items()}
DATA_EN["updated"] = D.DATA.get("updated", "")

A = json.load(open("assets.json", encoding="utf-8"))
A["jewels"], A["jewelsBy"] = sf_jewels.compute(A["alloc"], D.UNIQUES)          # joias por jewel socket (guia do Mattjestic), calculadas a cada build
MAP.update(sf_jewels.EN_PAIRS)
A_EN_TXT = {"sets": walk(A["sets"]), "guide": walk(A["guide"]), "jewels": walk(A.get("jewels", [])), "jewelsBy": walk(A.get("jewelsBy", {}))}

# ---------- assets compartilhados (funciona em file:// e GitHub Pages)
imgs = {k: "data:image/png;base64," + base64.b64encode(open("media/" + k, "rb").read()).decode()
        for k in ["image.png", "image2.png", "image4.png", "image5.png"]}
open(OUT + "/assets/assets.js", "w", encoding="utf-8").write("window.__A=" + safe(A) + ";\nwindow.__IMG=" + safe(imgs) + ";\n")

tpl = sf_jewels.patch(open("app_template.html", encoding="utf-8").read())
HEAD = '<!doctype html>\n<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐒</text></svg>">\n'

UI = list(UI) + sf_jewels.UI_PAIRS

def page(lang):
    t = tpl
    if lang == "en":
        for a, b in sorted(UI, key=lambda p: -len(p[0])):
            if a not in t:
                print("  [warn] UI string not found:", a[:70])
            t = t.replace(a, b)
        t = t.replace('content="Guia interativo Spirit Walker / Mighty Silverfist — PoE 2 Forbidden Rites"',
                      'content="Interactive Spirit Walker / Mighty Silverfist guide — PoE 2 Forbidden Rites"')
    data = DATA_PT if lang == "pt" else DATA_EN
    assets_expr = "window.__A" if lang == "pt" else "Object.assign(window.__A," + safe(A_EN_TXT) + ")"
    t = (t.replace("__LANG__", lang).replace("__DATA__", safe(data)).replace("__ASSETS__", assets_expr).replace("__IMG__", "window.__IMG")
          .replace("__PT_HREF__", "index.html").replace("__EN_HREF__", "en.html")
          .replace("__PT_ON__", "on" if lang == "pt" else "").replace("__EN_ON__", "on" if lang == "en" else ""))
    t = t.replace("<script>\nconst LANG =", '<script src="assets/assets.js"></script>\n<script>\nconst LANG =', 1)
    assert 'src="assets/assets.js"' in t, "assets script tag missing"
    t = enhance(t, lang, "silverfist")
    # head: tudo antes de <style>...</style> fica no head
    i = t.index("</style>") + len("</style>")
    home = '<a class="homebtn" href="../%s">← Builds</a>' % ("index.html" if lang == "pt" else "en.html")
    body = t[i:].replace('<div class="eyebrow">', '<div class="eyebrow">' + home, 1)
    return HEAD.format(lang="pt-BR" if lang == "pt" else "en") + t[:i] + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n"

open(OUT + "/index.html", "w", encoding="utf-8").write(page("pt"))
open(OUT + "/en.html", "w", encoding="utf-8").write(page("en"))

# ---------- sobras de PT na versão EN (texto visível / strings)
PT = re.compile(r"[ãõçÇ]|\b(não|você|para|com|mais|sem|dano|vida|nível|fase|seu|sua|agora|árvore|itens|preço|barato|completo|macaco|urso|quando|depois|antes|também|então|está|são)\b", re.I)
body = open(OUT + "/en.html", encoding="utf-8").read()
body = body[body.index("<body>"):]
body = re.sub(r"window\.__A[^\n]*", "", body)
left = sorted(set(m.group(0) for m in re.finditer(r"[^\"<>`{}]{0,60}(?:" + PT.pattern + r")[^\"<>`{}]{0,60}", body, re.I)))
print("EN leftovers:", len(left))
for x in left[:80]:
    print("  -", x.strip()[:150])
print("sizes:", {f: os.path.getsize(OUT + "/" + f) for f in ["index.html", "en.html", "assets/assets.js"]})
