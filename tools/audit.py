# -*- coding: utf-8 -*-
"""Auditoria de coerência de todas as builds: acha o que ficou perdido, quebrado, incoerente ou impossível de seguir.

Erros (E) reprovam a execução; avisos (W) entram no relatório; informações (I) mostram o estado. Cada verificação é uma função pequena em CHECKS.
Saída: docs/audit.md e tools/dl/audit.json. Uso: python audit.py [--strict]   (--strict: avisos também reprovam)"""
import json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "..")
sys.path.insert(0, os.path.join(HERE, "kit"))
import common, ninja  # noqa: E402

REG = os.path.join(HERE, "dl", "registry.json")
issues = []


def add(lvl, bid, code, msg):
    issues.append(dict(level=lvl, build=bid, code=code, msg=msg))


def load(bid):
    try:
        return common.load_build(bid)
    except Exception as e:                                                        # noqa: BLE001
        add("E", bid, "load", f"bdata não carrega: {e}")
        return None


SPIRIT_QUESTS = [(62, 100), (38, 60), (10, 30), (1, 0)]        # (nível, Spirit de quest acumulado): King in the Mists, Ignagduk, Lythara


def spirit_budget(lv):
    return next(v for l, v in SPIRIT_QUESTS if lv >= l)


def check_phases(bid, B):
    ph = B.PHASES
    prev_end = 0
    for p in ph:
        a, b = p["lv"]
        if a > b: add("E", bid, "phase-range", f"{p['id']}: faixa {a}–{b} invertida")
        if a != prev_end + 1 and prev_end and a <= prev_end: add("E", bid, "phase-overlap", f"{p['id']}: começa em {a} mas a anterior termina em {prev_end}")
        if prev_end and a > prev_end + 1: add("W", bid, "phase-gap", f"{p['id']}: lacuna de níveis {prev_end + 1}–{a - 1} sem fase")
        prev_end = max(prev_end, b)
        if not p.get("gems"): add("E", bid, "phase-empty", f"{p['id']}: sem gems")
        if not p.get("rotation"): add("W", bid, "phase-rotation", f"{p['id']}: sem rotação")
        for g in p["gems"]:
            if g.get("since") and g["since"] > b: add("W", bid, "gem-since", f"{p['id']}: {g['skill']} só entra no nível {g['since']}, depois do fim da fase ({b}): não aparece nela")
            if g.get("until") and g["until"] < a: add("W", bid, "gem-until", f"{p['id']}: {g['skill']} já saiu no nível {g['until']} (antes da fase)")
    if ph and ph[0]["lv"][0] != 1: add("E", bid, "phase-start", f"a primeira fase começa no nível {ph[0]['lv'][0]}, não no 1")
    if ph and ph[-1]["lv"][1] < 100: add("W", bid, "phase-end", f"a última fase termina no nível {ph[-1]['lv'][1]}")
    for lv in getattr(B, "MILESTONES", {}):
        if not 1 <= lv <= 100: add("E", bid, "milestone", f"marco no nível {lv}")


def check_spirit(bid, B):
    for p in B.PHASES:
        cost = 0
        for g in p["gems"]:
            if g.get("sp") == "core":
                m = re.search(r"\d+", str(g.get("cost", "")))
                if m and not (g.get("until") and g["until"] < p["lv"][0]) and not (g.get("since") and g["since"] > p["lv"][1]): cost += int(m.group())
        if "Set 2" in str(p.get("spiritNote", "")): continue                        # a build alterna dois conjuntos de Spirit por Weapon Set: a soma não vale
        lv = p["lv"][1] if p["lv"][1] <= 100 else 100
        if cost > spirit_budget(lv) + 200: add("W", bid, "spirit", f"{p['id']}: {cost} de Spirit em reservas no nível {lv}, com {spirit_budget(lv)} de quests (+ 200 de itens, ascendência e atlas é o teto plausível)")


def base_names():
    global _BASES
    if "_BASES" not in globals():
        d = json.load(open(os.path.join(HERE, "dl", "repoe_base_items.json"), encoding="utf-8"))
        _BASES = {v["name"] for v in d.values() if v.get("name")}
    return _BASES


def check_uniques(bid, B):
    uniq = {u["n"] for u in getattr(B, "UNIQUES", [])}
    used = set()
    for p in B.PHASES:
        for k in ("cheap", "full"):
            used.update(x for x in p.get(k, []) if isinstance(x, str))
    for g in getattr(B, "GEAR", []):
        for k in ("cheap", "value", "full", "slot"):
            v = g.get(k)
            if isinstance(v, str): used.add(v)
        for o in g.get("opts") or []: used.add(o["n"])
    for b in getattr(B, "BUY_ORDER", []): used.add(b["item"])
    blob = " ".join(used)
    src = open(os.path.join(HERE, "builds", bid, "bdata.py"), encoding="utf-8").read()
    for n in sorted(uniq):
        # órfão = nenhum slot/fase/compra usa E o nome não é citado em nenhum outro texto do guia (só na própria definição)
        if n not in blob and src.count(n) <= 1: add("W", bid, "unique-orphan", f"{n}: está em UNIQUES mas nada no guia usa ou cita")
    for p in B.PHASES:
        for k in ("cheap", "full"):
            for x in p.get(k, []):
                if isinstance(x, str) and re.match(r"^[A-Z][A-Za-z']*(?: (?:of|the|and)| [A-Z][A-Za-z']*)*$", x) and x not in uniq and len(x) < 30 and re.sub(r"^(Runeforged|Runemastered) ", "", x) not in base_names() and not any(x in str(g.get("slot", "")) for g in getattr(B, "GEAR", [])):
                    add("W", bid, "unique-missing", f"{p['id']}.{k}: '{x}' não tem entrada em UNIQUES")
    for u in getattr(B, "UNIQUES", []):
        if u.get("p") not in {p["id"] for p in B.PHASES}: add("E", bid, "unique-phase", f"{u['n']}: fase '{u.get('p')}' não existe")
    for g in getattr(B, "GEAR", []):
        for o in g.get("opts") or []:
            if o["lv"] < 1 or o["lv"] > 100: add("E", bid, "opt-level", f"{g['slot']}: {o['n']} com nível {o['lv']}")
        if g.get("opts") and not g.get("no_cheap"):                                       # no_cheap: slot que por desenho só tem opção de valor/luxo
            for lv in ((10, 25, 40, 60, 80, 95) if str(g["slot"]).startswith("Charms") else (1, 10, 25, 40, 60, 80, 95)):     # charms só existem depois da quest do Medallion
                if lv < g.get("from_lv", 0): continue                                            # slot que só existe a partir de um nível (ex.: Set 2)
                if not [o for o in g["opts"] if o["lv"] <= lv and o["c"] in ("free", "cheap")]: add("W", bid, "opt-empty", f"{g['slot']}: nenhuma opção barata no nível {lv}")


def check_supports(bid, B):
    why = getattr(B, "SUPWHY", {})
    used = {s for p in B.PHASES for g in p["gems"] for s in g["sup"]}
    for s in sorted(used - set(why)): add("E", bid, "support-why", f"{s}: support usado sem explicação (SUPWHY)")
    for s in sorted(set(why) - used): add("I", bid, "support-orphan", f"{s}: explicado em SUPWHY mas nunca usado")


def check_tree(bid, B):
    """Usa a ordem de alocação que a página realmente mostra (assets.json > order): cada fase = os N primeiros nós dessa ordem.
    Um nó que não liga ao início da classe pelos nós já alocados é um passo que o jogador não consegue dar."""
    p = os.path.join(HERE, "builds", bid, "assets.json")
    if not os.path.exists(p):
        add("W", bid, "tree-missing", "sem assets.json (rode kassets)"); return
    A = json.load(open(p, encoding="utf-8"))
    start = getattr(B, "START", None) or ninja.CLASS_START.get(getattr(B, "CLASS", ""))
    order = A.get("order", {})
    prev_n = 0
    for pid in getattr(B, "ORDER", [p_["id"] for p_ in B.PHASES]):
        o = order.get(pid)
        if not o: add("W", bid, "tree-phase", f"{pid}: sem ordem de árvore"); continue
        nodes, n = o["o"], o["n"]
        if n < prev_n: add("I", bid, "tree-respec", f"{pid}: a árvore tem {prev_n - n} nós a menos que a fase anterior (respec)")
        prev_n = n
        cut = set(nodes[:n])
        st0 = getattr(B, "PHASE_START", {}).get(pid, start)                       # a build pode partir de outro ponto (joia Split Personality)
        if st0 and cut:
            seen, stack = {st0}, [st0]
            while stack:
                u = stack.pop()
                for w in ninja.ADJ.get(u, ()):
                    if w in cut and w not in seen: seen.add(w); stack.append(w)
            lost = len(cut - seen)
            if lost: add("W", bid, "tree-connect", f"{pid}: {lost} de {n} nós da árvore não ligam ao início da classe pelos nós anteriores (caminho que o jogador não consegue seguir)")


_NOTABLES = {}


def _notable_names():
    if not _NOTABLES:
        for k, n in ninja.NODES.items():
            if (n.get("isNotable") or n.get("isKeystone")) and not n.get("ascendancyName") and len(n.get("name") or "") >= 8:
                _NOTABLES.setdefault(n["name"], set()).add(int(k))
    return _NOTABLES


def _cited(text):
    """Nomes de notável/keystone citados no texto (os mais longos primeiro; um nome dentro de outro, ou parte de um nome próprio maior, não conta)."""
    names, out = _notable_names(), []
    txt = text
    for nm in sorted(names, key=len, reverse=True):
        for m in re.finditer(r"(?<![A-Za-z])" + re.escape(nm) + r"(?![A-Za-z])", txt):
            before, after = txt[:m.start()], txt[m.end():]
            if re.search(r"[A-Z][a-z']+ $", before) or re.match(r" [A-Z]", after): continue        # parte de um nome próprio maior (item, gem, ascendência)
            out.append(nm)
            txt = txt[:m.start()] + " " * len(nm) + txt[m.end():]
            break
    return out


_FWD = re.compile(r"pr[óo]xim|next|at[ée] |towards?|road|pathing|caminho|s[óo] entra|only come|nos cortes|a partir d", re.I)


def _forward(text, nm):
    """A frase que cita o nó fala de caminho ou de um corte futuro (\"caminho até X\", \"X vem no próximo corte\"): não é promessa desta fase."""
    for sent in re.split(r"(?<=[.;])\s", text):
        if nm in sent and _FWD.search(sent): return True
    return False


def check_tree_text(bid, B):
    """O texto 'Árvore' de cada fase só pode citar notables que o corte dessa fase (ou seus Weapon Sets) realmente tem.
    Foi assim que o guia do Shaman prometia Brain Storm e Chakra of Elements numa árvore que nunca os alocava."""
    p = os.path.join(HERE, "builds", bid, "assets.json")
    if not os.path.exists(p): return
    A = json.load(open(p, encoding="utf-8"))
    names = _notable_names()
    for ph in B.PHASES:
        o, al = A.get("order", {}).get(ph["id"]), A.get("alloc", {}).get(ph["id"])
        tx = ph.get("tree")
        if not o or not al or not tx: continue
        text = tx if isinstance(tx, str) else (tx.get("pt") if isinstance(tx, dict) else str(tx))
        have = set(o["o"][:o["n"]]) | set(al.get("s1", [])) | set(al.get("s2", []))
        miss = [nm for nm in _cited(text or "") if not (names[nm] & have) and not _forward(text, nm)]
        if miss: add("W", bid, "tree-text", f"{ph['id']}: o texto da Árvore cita {', '.join(miss)}, que o corte dessa fase não tem")


def check_tree_damage(bid, B):
    """Meça o dano da árvore por fase (kit/deepcheck.py). Uma fase de campanha com 17+ nós e nenhum dano nem velocidade repete o bug da Whirling e do Legionnaire."""
    import deepcheck
    for pid, lv, n, t in deepcheck.tree_rows(bid, B):
        if lv and lv[0] >= 5 and lv[1] <= 64 and n >= 10 and t["dmg"] + t["spd"] + t["flat"] < 30:
            add("W", bid, "tree-damage", f"{pid} (níveis {lv[0]}–{lv[1]}): a árvore tem {n} nós e só {t['dmg']}% de dano e {t['spd']}% de velocidade somados")


def check_jewels(bid, B):
    """Joias: o jogador precisa saber em qual jewel socket cada uma vai. Sem dados = aviso honesto; socket que nenhuma fase aloca = incoerência."""
    p = os.path.join(HERE, "builds", bid, "assets.json")
    if not os.path.exists(p): return
    J = json.load(open(p, encoding="utf-8")).get("jewels") or []
    if not J:
        add("I", bid, "jewels-none", "o guia de origem não define joias: a aba Árvore mostra o aviso"); return
    for j in J:
        if j.get("first") is None and not j.get("via"): add("W", bid, "jewel-socket", f"{j['n']}: o socket {j['node']} não é alocado em nenhuma fase da árvore")
        if not j.get("mods") and not j.get("u"): add("I", bid, "jewel-mods", f"{j['n']} (socket {j['node']}): sem lista de afixos")


def check_sources(bid, B):
    if not getattr(B, "SOURCES", None): add("E", bid, "sources", "sem fontes")
    for s in getattr(B, "SOURCES", []):
        if not str(s.get("url", "")).startswith("http"): add("E", bid, "source-url", f"fonte sem URL: {s.get('name')}")
    if not getattr(B, "GUIDE_URL", ""): add("I", bid, "guide-url", "sem GUIDE_URL de um guia de referência único (a build vem de várias fontes?)")


REQUIRED = ["PHASES", "MILESTONES", "SUPWHY", "ASCENDANCY", "ASC_UNLOCK", "KEY_PASSIVES", "TREE_STAGES", "UNIQUES", "GEAR", "BUY_ORDER", "TRICKS", "TROUBLESHOOT", "ATLAS_CHECK", "CRAFT", "CASES",
            "SOURCES", "FIXES", "UI", "CHAR", "TREE_RULES", "MECH", "CRAFT_KIT", "TXT", "TABS", "ORDER", "VMAP", "CONFIG"]


def check_contract(bid, B):
    """O contrato de uma build (docs/COMO-ADICIONAR-BUILD.md): tudo o que precisa existir para o jogador conseguir seguir do nível 1 ao 100."""
    for k in REQUIRED:
        v = getattr(B, k, None)
        if v in (None, "", [], {}): add("E", bid, "contract-missing", f"falta {k}")
    ids = [p["id"] for p in B.PHASES]
    if len(ids) < 5: add("W", bid, "contract-phases", f"só {len(ids)} fases: o contrato pede campanha (Atos), mapas e endgame")
    for p in B.PHASES:
        for k in ("goal", "rotation", "gems", "stats", "tree", "avoid", "exit", "cheap", "full"):
            if k not in p: add("E", bid, "contract-phase-field", f"{p['id']}: falta '{k}'")
    if not any(g.get("opts") for g in getattr(B, "GEAR", [])): add("I", bid, "contract-gear-opts", "sem ranking de opções por slot (GEAR opts): a aba Itens usa as linhas fixas travadas por nível")
    if not getattr(B, "FIXES", None): add("E", bid, "contract-honesty", "sem FIXES: diga o que é adaptação, estimativa ou aproximação")
    if not (getattr(B, "MECH", {}) or {}).get("sections"): add("E", bid, "contract-mech", "MECH sem seções")
    tabs = {t[0] for t in getattr(B, "TABS", [])}
    for t in ("agora", "meu", "rota", "skills", "gear", "arvore", "asc", "quests", "fontes"):
        if t not in tabs: add("E", bid, "contract-tab", f"aba obrigatória ausente: {t}")
    ck = getattr(B, "CRAFT_KIT", {}) or {}
    if "amulet" not in {i.get("id") for i in ck.get("items", [])}: add("E", bid, "contract-craft", "o kit de crafting precisa do item 'amulet' (o teste de navegador usa)")


def check_registration(entry):
    """Uma build só existe de verdade quando está registrada em todos os lugares compartilhados."""
    folder, key = entry["folder"], entry["key"]
    def has(rel, needle):
        p = os.path.join(REPO, rel)
        return os.path.exists(p) and needle in open(p, encoding="utf-8").read()
    where = [("shared/fx.js", folder), ("shared/loader.js", folder), ("shared/poe2.js", folder), ("shared/poe2.css", f'data-build="{folder}"'),
             ("tools/enhance.py", f"'{folder}'"), ("tools/landing_v2.py", f"'{folder}'"), ("tools/registry.py", f'folder="{folder}"'),
             ("tools/tests/mobile.cjs", f"'{folder}'"), ("tools/tests/browser.cjs", f"'{folder}'")]
    if key != "sf": where.append(("shared/landing.css", f".build.{key}"))              # Silverfist é o estilo base do card
    if entry.get("kit"): where += [("tools/build_all.py", f"'{folder}'"), ("tools/tests/test_links.py", f'"{folder}"'), ("tools/build_landing.py", f'"{folder}"')]
    for rel, needle in where:
        if not has(rel, needle): add("E", key, "register-missing", f"{folder} não está registrada em {rel}")
    for f in (f"shared/art/{key}-asc.webp", f"shared/art/{key}-class.webp"):
        if not os.path.exists(os.path.join(REPO, f)): add("E", key, "art-missing", f"falta {f}")


def check_pages(entry):
    folder, bid = entry["folder"], entry["key"]
    for f in ("index.html", "en.html"):
        p = os.path.join(REPO, folder, f)
        if not os.path.exists(p): add("E", bid, "page-missing", f"{folder}/{f} não existe"); continue
        t = open(p, encoding="utf-8").read()
        for bad in ("undefined", "NaN", "[object Object]", "None</"):
            n = len(re.findall(r"(?<![A-Za-z\"'_.])" + re.escape(bad) + r"(?![A-Za-z\"'_:])", re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)))
            if n: add("W", bid, "page-text", f"{folder}/{f}: '{bad}' aparece {n}x no texto visível")
        for m in set(re.findall(r'(?:src|href)="((?:\.\./)?(?:shared|assets)/[^"?#]+)', t)):
            if not os.path.exists(os.path.normpath(os.path.join(REPO, folder, m))): add("E", bid, "asset-missing", f"{folder}/{f}: {m} não existe")


def check_registry(reg):
    snap = reg.get("snapshot")
    if not snap: add("W", "-", "snapshot", "sem snapshot do poe.ninja (rode ninja_meta.py)")
    else:
        age = (time.time() - time.mktime(time.strptime(snap["fetched"], "%Y-%m-%d"))) / 86400
        if age > 14: add("W", "-", "snapshot-old", f"snapshot do poe.ninja tem {int(age)} dias")
    for e in reg["builds"]:
        if e["status"] != "ativa": add("W", e["key"], "status", f"status '{e['status']}': ninguém usa mais {e['ninja']['skill'] or e['ninja']['ascN']}? revisar ou aposentar")
        if e["meta"] == "sem dados": add("I", e["key"], "meta", "sem dados do poe.ninja para a skill principal")
    folders = {e["folder"] for e in reg["builds"]}
    for d in sorted(os.listdir(REPO)):
        if os.path.exists(os.path.join(REPO, d, "index.html")) and d not in folders and d not in ("rites", "docs", "planilha", "shared", "tools"):
            add("W", d, "orphan-folder", f"pasta '{d}' tem index.html mas não está no registro")


def main():
    reg = json.load(open(REG, encoding="utf-8"))
    check_registry(reg)
    for e in reg["builds"]:
        bid = e["folder"]
        if e.get("kit"):
            B = load(bid)
            if B:
                for fn in (check_contract, check_phases, check_spirit, check_uniques, check_supports, check_tree, check_tree_text, check_tree_damage, check_jewels, check_sources): fn(bid, B)
        check_registration(e)
        check_pages(dict(e, key=e["key"]))
    E = [i for i in issues if i["level"] == "E"]; W = [i for i in issues if i["level"] == "W"]; I = [i for i in issues if i["level"] == "I"]
    json.dump(dict(date=time.strftime("%Y-%m-%d"), errors=len(E), warnings=len(W), info=len(I), issues=issues), open(os.path.join(HERE, "dl", "audit.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    lines = [f"# Auditoria das builds — {time.strftime('%Y-%m-%d')}", "", f"**{len(E)} erros · {len(W)} avisos · {len(I)} informações**", ""]
    for title, arr in (("Erros", E), ("Avisos", W), ("Informações", I)):
        if arr:
            lines += [f"## {title}", ""] + [f"- `{i['build']}` **{i['code']}** — {i['msg']}" for i in arr] + [""]
    open(os.path.join(REPO, "docs", "audit.md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"{len(E)} erros · {len(W)} avisos · {len(I)} informações  →  docs/audit.md")
    for i in E + W[:25]: print(f"  {i['level']} {i['build']:12} {i['code']:14} {i['msg']}")
    sys.exit(1 if E or (W and "--strict" in sys.argv) else 0)


if __name__ == "__main__":
    main()
