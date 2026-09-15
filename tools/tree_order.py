"""Ordem de alocação da árvore por fase, para a árvore acompanhar o nível.

Para cada fase gera uma lista ordenada de nós principais:
  1) primeiro os nós que você já tinha na fase anterior (não precisa refazer),
  2) depois o caminho mais curto até cada notable/keystone da fase,
  3) quando a fase acaba, continua com os nós das PRÓXIMAS fases (conectados).
O app mostra os N primeiros, onde N = pontos disponíveis no nível.
Rode depois do build_assets.py: python tree_order.py
"""
import json
from collections import deque

T = json.load(open("tree.json", encoding="utf-8"))
N = T["nodes"]
A = json.load(open("assets.json", encoding="utf-8"))
START = 50459
ORDER = ["a1", "a2", "a3", "a4", "int", "ea", "t15", "mm", "uber"]

adj = {}
for k, n in N.items():
    for c in n.get("connections", []):
        adj.setdefault(int(k), set()).add(c["id"])
        adj.setdefault(c["id"], set()).add(int(k))

def important(nid):
    n = N[str(nid)]
    return n.get("isNotable") or n.get("isKeystone") or n.get("isJewelSocket")

def grow(have, targets, prefer, out):
    """Aloca todos os `targets` conectados, a partir de `have`, anexando em `out`."""
    remaining = [t for t in targets if t not in have]
    rem = set(remaining)
    # 1) nós preferidos (já alocados antes) — só entram se conectados
    changed = True
    while changed:
        changed = False
        for t in remaining:
            if t in rem and t in prefer and any(v in have for v in adj.get(t, ())):
                have.add(t); rem.discard(t); out.append(t); changed = True
    # 2) caminho mais curto até o próximo notable (na ordem do guia)
    while rem:
        allowed = rem
        # BFS a partir do conjunto alocado, andando só por nós-alvo
        prev = {}; dq = deque()
        for h in have:
            for v in adj.get(h, ()):
                if v in allowed and v not in prev:
                    prev[v] = None; dq.append(v)
        found = None
        order_rank = {t: i for i, t in enumerate(remaining)}
        best = None
        while dq:
            u = dq.popleft()
            if important(u):
                if best is None:
                    best = u; bestd = 0
                    x = u
                    while prev[x] is not None:
                        x = prev[x]; bestd += 1
                # mantém o primeiro achado (mais perto)
                break
            for v in adj.get(u, ()):
                if v in allowed and v not in prev:
                    prev[v] = u; dq.append(v)
        if best is not None:
            path = []; x = best
            while x is not None:
                path.append(x); x = prev[x]
            for x in reversed(path):
                if x in rem:
                    have.add(x); rem.discard(x); out.append(x)
            continue
        # sem notables alcançáveis: pega qualquer nó da fronteira (na ordem do guia)
        front = [t for t in remaining if t in rem and any(v in have for v in adj.get(t, ()))]
        if not front:
            break  # desconectado (não deveria acontecer)
        t = front[0]; have.add(t); rem.discard(t); out.append(t)

orders = {}
prev_set = set()
for i, pid in enumerate(ORDER):
    P = A["alloc"][pid]["m"]
    have = {START}; out = []
    grow(have, P, prev_set, out)
    for nxt in ORDER[i + 1:]:
        grow(have, A["alloc"][nxt]["m"], set(), out)
        if len(out) >= 123:
            break
    orders[pid] = {"o": out, "n": len(P)}
    prev_set = set(P)
    print(pid, "fase", len(P), "ordem total", len(out))

# pontos de quest (campanha 0.5): 24 no total; nível 98 = 97 + 24 = 121 (igual à árvore final do guia)
QUEST = [[8, 1], [12, 2], [18, 3], [22, 4], [26, 5], [30, 6], [34, 8], [40, 10], [45, 12], [50, 14], [54, 16], [58, 18], [62, 20], [66, 22], [70, 24]]
kinds = {n[0]: n[3] for n in A["tree"]["nodes"]}
A["order"] = orders
A["quest"] = QUEST
A["nodeKind"] = {str(k): v for k, v in kinds.items() if v in (1, 2, 3)}
json.dump(A, open("assets.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("ok")
