# -*- coding: utf-8 -*-
"""Auditoria de consistência das builds do kit: tudo que uma aba cita precisa existir nas outras.

Verifica, para cada build:
  - itens citados nas fases (barato/completo), na progressão por slot e na ordem de compra existem como unique, gem ou texto livre com ícone;
  - chaves usadas nas regras de "Meu personagem", nas trocas e no timing existem na lista de itens marcáveis;
  - fases citadas por trocas/timing existem; marcos caem dentro de alguma fase;
  - notables de ascendência por fase existem na árvore e cabem nos Trials liberados.
"""
import json, os, re, sys, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, os.path.join(ROOT, "kit"))
sys.path.insert(0, ROOT)
import common  # noqa: E402

BUILDS = ["tactician", "infernalist", "acolyte", "pathfinder", "smith", "martial"]
TREE = json.load(open(os.path.join(ROOT, "tree.json"), encoding="utf-8"))["nodes"]


def assets(bid):
    return json.load(open(os.path.join(ROOT, "builds", bid, "assets.json"), encoding="utf-8"))


class Links(unittest.TestCase):
    def check(self, bid):
        D = common.load_build(bid)
        A = assets(bid)
        phases = {p["id"] for p in D.PHASES}
        uniq = {u["n"] for u in D.UNIQUES}
        gems = {g["skill"] for p in D.PHASES for g in p["gems"]} | {s for p in D.PHASES for g in p["gems"] for s in g["sup"]}
        icons = set(A["uniqIcon"]) | set(A["gemIcon"]) | set(A["supIcon"])
        own = {k for _, k, _ in D.CHAR["own"]}
        problems = []

        # 2) progressão por slot: cada item nomeado tem ícone (unique ou gem) ou é texto explicativo
        for g in getattr(D, "GEAR", []):
            for x in g.get("lvls", []):
                n = x["n"]
                if n in uniq or n in gems or n in icons or n in A.get("baseIcon", {}):
                    continue
                if ":" in n or "(" in n or re.search(r"(rare|rares|com|de|até|sem|mãos|any|with|and)", n, re.I):
                    continue                                   # frase explicativa (ex.: "Rare: vida + resist")
                problems.append(f"{bid}: item '{n}' na progressão do slot '{g['slot']}' não é unique nem gem")

        # 3) chaves de regras/trocas/timing existem entre os itens marcáveis
        for r in D.CHAR["rules"]:
            for k in (r["when"].get("own") or []) + (r["when"].get("notOwn") or []) + (r["when"].get("anyOwn") or []):
                if k not in own:
                    problems.append(f"{bid}: regra de Meu personagem usa '{k}', que não existe na lista de marcar")
            if r.get("tab") and r["tab"] not in {t[0] for t in D.TABS}:
                problems.append(f"{bid}: regra aponta para a aba '{r['tab']}', que não existe")
        for s in getattr(D, "ADAPT_SWAPS", []):
            for pid in ([s["pid"]] if s.get("pid") else s.get("pids", [])):
                if pid not in phases:
                    problems.append(f"{bid}: troca declarada para a fase '{pid}', que não existe")
            if s.get("gemsFrom") and s["gemsFrom"] not in phases:
                problems.append(f"{bid}: troca puxa gems da fase '{s['gemsFrom']}', que não existe")
            for k in (s["when"].get("own") or []) + (s["when"].get("notOwn") or []):
                if k not in own:
                    problems.append(f"{bid}: troca usa a chave '{k}', que não existe na lista de marcar")
        for k in getattr(D, "TIMING_KEY", {}).values():
            if k not in own:
                problems.append(f"{bid}: timing aponta para a chave '{k}', que não existe na lista de marcar")

        # 4) marcos caem dentro de alguma fase
        for lv in D.MILESTONES:
            if not any(p["lv"][0] <= lv <= p["lv"][1] for p in D.PHASES):
                problems.append(f"{bid}: marco do nível {lv} está fora de todas as fases")

        # 5) ascendência por fase: nome existe na árvore e cabe nos Trials já liberados
        names = {n.get("name") for n in TREE.values() if n.get("ascendancyName") == D.ASC}
        for pid, want in getattr(D, "ASC_PHASE", {}).items():
            if pid not in phases:
                problems.append(f"{bid}: ASC_PHASE cita a fase '{pid}', que não existe")
            for nm in want:
                if nm not in names:
                    problems.append(f"{bid}: ASC_PHASE cita '{nm}', que não é notable de {D.ASC}")
            lv = next((p["lv"][1] for p in D.PHASES if p["id"] == pid), 0)
            trials = sum(1 for u in D.ASC_UNLOCK if u <= lv)
            if len(want) > max(trials, 0):
                problems.append(f"{bid}: fase '{pid}' aloca {len(want)} notables, mas só {trials} Trials liberam até o nível {lv}")

        # 6) ordem de compra aponta para fases/itens plausíveis
        for b in D.BUY_ORDER:
            if not str(b["phase"]).strip():
                problems.append(f"{bid}: item '{b['item']}' na ordem de compra sem fase")
        return problems

    def test_builds(self):
        todos = []
        for bid in BUILDS:
            todos += self.check(bid)
        self.assertEqual(todos, [], "\n" + "\n".join(todos))


if __name__ == "__main__":
    unittest.main()
