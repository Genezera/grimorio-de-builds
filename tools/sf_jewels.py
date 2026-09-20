# -*- coding: utf-8 -*-
"""Joias do Silverfist: em qual jewel socket cada joia vai (o guia do Mattjestic lista `jw` = ["jewel-<tipo>@node-<id>"] em cada variante).

O Silverfist não usa o kit, então este módulo faz o mesmo que kit/jewels.py + kit/jewels_patch.py:
  · convert(slugs)   → lista normalizada {node, n, u, base, mods, ...} que o jewels.collect() entende (soquete, vizinhança, primeira fase em que o socket está alocado)
  · PATCH_JS(t)      → painel "Joias e jewel sockets" na aba Árvore, anel dourado no mapa e joia no tooltip do socket (aplicado ao template em memória por build_site.py)
Os textos das joias raras vêm do que o próprio guia diz (linha "Jewels" da aba Itens: 'Minion crit/dano > attack speed > resist de minion'); nada aqui é inventado."""
import re

KIND = {"jewelint": "Sapphire", "jewelstr": "Ruby", "jeweldex": "Emerald", "jeweldiamond": "Diamond"}
RARE_TXT = {
    "Sapphire": ("Prioridade do guia: crítico e dano de Minions > attack speed > resistência de Minions (barato: Minion +% Elemental Res).",
                 "The guide's priority: Minion crit and damage > attack speed > Minion resistance (cheap: Minion +% Elemental Res)."),
    "Ruby": ("Redução de dano físico para Minions.", "Physical damage reduction for Minions."),
    "Emerald": ("Companion: dano e vida.", "Companion damage and life."),
    "Diamond": ("O guia usa um Diamond neste socket mas não detalha os afixos.", "The guide uses a Diamond in this socket but doesn't detail the affixes."),
}
NOTE_NO_TEXT = ("O guia não detalha esta joia.", "The guide doesn't detail this jewel.")
EN_PAIRS = {pt: en for pt, en in RARE_TXT.values()}                  # PT -> EN das descrições das joias raras (build_site.py aplica na versão EN)
EN_PAIRS[NOTE_NO_TEXT[0]] = NOTE_NO_TEXT[1]
SMALL = {"of", "the", "and", "a"}


def _title(s):
    w = s.replace("-", " ").split()
    return " ".join(x if (i and x in SMALL) else x.capitalize() for i, x in enumerate(w))


def convert(slugs, uniques):
    """slugs: ["jewel-jewelint@node-60735", "jewel-fouruniquejewel8-prism-of-belief@node-46882", ...]; uniques: D.UNIQUES (chober) para o texto de cada unique."""
    out = []
    for raw in slugs or []:
        m = re.match(r"^(jewel-[^@]+)@node-(\d+)$", raw)
        if not m:
            continue
        slug, node = m.group(1), int(m.group(2))
        kind = KIND.get(slug.replace("jewel-", ""))
        if kind:
            name, unique, mods = f"Rare {kind} Jewel", False, [RARE_TXT[kind][0]]
        else:
            name = _title(re.sub(r"^jewel-(?:[a-z]*unique[a-z]*\d*-+)?", "", slug))
            unique = True
            u = next((x for x in uniques if x["n"] == name), None)
            mods = [u["why"]] if u and u.get("why") else [NOTE_NO_TEXT[0]]
        out.append({"node": node, "n": name, "u": unique, "base": "", "mods": mods, "radius": None, "corrupted": False, "note": ""})
    return out


CSS = """
.nrow.ahead{opacity:.72} .nrow small{display:block;color:var(--mute);line-height:1.4;margin-top:2px}
.jw-note{margin:2px 0 8px;padding:0 6px;color:var(--mute);font-size:.86rem;line-height:1.4}
"""

HELPER = '''function jewelsPanel(pid) {
  const list = (A.jewelsBy && A.jewelsBy[pid]) || [];
  if (!list.length) return `<div class="plate">${JT("Joias e jewel sockets", "Jewels and jewel sockets")}</div><p class="jw-note">${JT("O guia do Mattjestic não coloca joia em nenhum socket nesta fase: use a joia que der vida, resistência ou o dano que você usa.", "Mattjestic's guide puts no jewel in any socket in this phase: use whatever gives life, resistances or the damage you use.")}</p>`;
  return `<div class="plate">${JT("Joias e jewel sockets", "Jewels and jewel sockets")}</div>
  <p class="jw-note">${JT("Cada joia vai no socket indicado — anel dourado no mapa da árvore. Clique para centralizar. É o plano desta fase no guia do Mattjestic.", "Each jewel goes in the socket shown — gold ring on the tree map. Click to centre it. This is this phase's plan in Mattjestic's guide.")}</p>
  <div class="nlist">${list.map((j, i) => { const im = j.u ? uniqImg(j.n) : "";
    return `<div class="nrow k3" data-gotree="${j.node}">${im ? `<img src="${im}" alt="">` : `<img alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==">`}<div><b>${i + 1}. ${esc(j.n)} <span class="chip ${j.u ? "unique" : "gold"}" style="font-size:.7rem">${j.u ? "Unique" : "Rare"}</span></b>
      <small>${JT("Socket perto de", "Socket near")} <span style="color:var(--text)">${esc(j.near || "?")}</span>${j.first ? "" : ` · ${JT("fora do caminho do guia (Sinister Jewel Socket): só aparece se a sua árvore tiver outra fonte desse socket", "off the guide's path (Sinister Jewel Socket): only shows up if your tree has another source of that socket")}`}${j.where === "s1" ? ` · Weapon Set I` : j.where === "s2" ? ` · Weapon Set II` : ""}</small>
      ${j.mods && j.mods.length ? `<small>${j.mods.map(esc).join(" · ")}</small>` : ""}</div></div>`; }).join("")}</div>`;
}
'''

RING = """    if (typeof A !== "undefined" && A.jewels) {
      for (const j of (this.jw || A.jewels || [])) { const i = this.idx.get(j.node); if (i == null) continue; const n = this.nodes[i]; const rad = Math.max(58, 6 / s) * 1.7;
        ctx.beginPath(); ctx.arc(n[1], n[2], rad, 0, Math.PI * 2); ctx.strokeStyle = "#E8C66A"; ctx.lineWidth = Math.max(3 / s, 20); ctx.shadowColor = "#E8C66A"; ctx.shadowBlur = 12 * r; ctx.stroke(); ctx.shadowBlur = 0; }
    }
"""

TIP_OLD = 'el.innerHTML = `<div class="th">${esc(m[0])}</div><div class="st">${(m[1] || []).map(s => `<span>${esc(s)}</span>`).join("") || "<span>—</span>"}</div>`;'
TIP_NEW = ('const jw = (typeof A !== "undefined" && (A.jewelsBy && A.jewelsBy[pid] || A.jewels) || []).find(j => j.node === n[0]); const lines = jw ? [`${jw.n} · ${jw.u ? "Unique" : "Rare"}`, ...(jw.mods || [])] : (m[1] || []);\n'
           '    el.innerHTML = `<div class="th">${esc(m[0])}${jw ? " ◆" : ""}</div><div class="st">${lines.map(s => `<span>${esc(s)}</span>`).join("") || "<span>—</span>"}</div>`;')


_JT = re.compile(r'\$\{JT\("((?:[^"\\]|\\.)*)", "((?:[^"\\]|\\.)*)"\)\}')
UI_PAIRS = []                                                          # (PT, EN) dos textos do painel: build_site.py junta a ui_en.UI para gerar en.html


def _plain(js):
    """O helper é escrito com JT("pt", "en"); no template fica só o PT e o par entra em UI_PAIRS (mesmo mecanismo do resto do Silverfist)."""
    def one(m):
        if (m.group(1), m.group(2)) not in UI_PAIRS:
            UI_PAIRS.append((m.group(1), m.group(2)))
        return m.group(1)
    return _JT.sub(one, js)


def patch(t):
    """Aplica o painel, o anel dourado e o tooltip ao template do Silverfist (string). Falha alto se algum ponto de ancoragem sumir."""
    i = t.index("</style>")
    t = t[:i] + CSS.strip("\n") + "\n" + t[i:]
    a = "function vArvore() {"
    assert t.count(a) == 1, "vArvore anchor"
    t = t.replace(a, _plain(HELPER) + a, 1)
    old = "      <div class=\"divider\"></div><p class=\"label\" style=\"padding:0 6px\">Notables do meta"
    assert t.count(old) == 1, "meta anchor"
    t = t.replace(old, "      ${jewelsPanel(pid)}\n" + old, 1)
    old = "    if (this.metaSet) {\n      for (const n of this.nodes) { if (!this.metaSet.has(n[0])) continue;"
    assert t.count(old) == 1, "canvas anchor"
    t = t.replace(old, RING + old, 1)
    assert t.count(TIP_OLD) == 1, "tooltip anchor"
    t = t.replace(TIP_OLD, TIP_NEW, 1)
    old = "  if (S.treeMeta) TV.metaSet = new Set(A.metaNotables.map(m => m.id));"
    assert t.count(old) == 1, "mountTree anchor"
    t = t.replace(old, "  TV.jw = (A.jewelsBy && A.jewelsBy[pid]) || A.jewels;\n" + old, 1)
    return t


def compute(alloc, uniques):
    """(jewels, jewelsBy) a partir de dl/matt.json, tree.json e da alocação por fase (alloc) do assets.json. build_site.py chama isto a cada build:
    o assets.json do Silverfist passa por vários scripts (build_assets → tree_order → ...), então as joias não são gravadas nele."""
    import json, os, sys
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(here, "kit"))
    import jewels as JW
    N = json.load(open(os.path.join(here, "tree.json"), encoding="utf-8"))["nodes"]
    matt = json.load(open(os.path.join(here, "dl", "matt.json"), encoding="utf-8"))
    adj = {}
    for k, n in N.items():
        for c in n.get("connections", []):
            adj.setdefault(int(k), set()).add(c["id"]); adj.setdefault(c["id"], set()).add(int(k))
    order = ["a1", "a2", "a3", "a4", "int", "ea", "t15", "mm", "uber"]
    vmap = {"a1": 5, "a2": 7, "a3": 8, "a4": 9, "int": 10, "ea": 11, "t15": 13, "mm": 17, "uber": 18}      # a mesma escolha de variantes do build_assets.py
    class _D:
        VMAP = {p: p for p in order}
    var = {p: {"tree": {"jewels": convert(matt["vs"][vmap[p]].get("jw"), uniques)}} for p in order}
    final = JW.collect(var, _D, alloc, order, N, adj)
    by = {}
    for p in order:
        lst = JW.collect({p: var[p]}, _D, alloc, [p], N, adj)
        by[p] = [j for j in lst if j["first"] == p or (p == "uber" and j["first"] is None)]
    return final, by
