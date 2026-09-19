# -*- coding: utf-8 -*-
"""Coleta automática do poe.ninja (builds): popularidade de cada ascendência e de cada skill principal, e DPS/EHP dos personagens do topo.

A API de builds do poe.ninja responde em protobuf sem schema público; este módulo decodifica o que precisa (facetas com contagens, dicionários NDIC de nomes e as colunas
de personagens) só com a biblioteca padrão. Saída: tools/dl/meta_snapshot.json  — usado por registry.py (meta x fora do meta) e discover.py (candidatas a novas builds).
Uso: python ninja_meta.py [--league forbidden-rites] [--top 100]"""
import json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "dl", "meta_snapshot.json")
BASE = "https://poe.ninja/poe2/api"
UA = {"User-Agent": "Mozilla/5.0 (grimorio-de-builds meta collector)"}


def get(url, tries=3):
    for k in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
        except Exception:
            if k == tries - 1: raise
            time.sleep(2 + 3 * k)


# ---------------------------------------------------------------- protobuf genérico (só o que a API usa)
def _varint(b, i):
    x = s = 0
    while True:
        c = b[i]; i += 1
        x |= (c & 0x7f) << s; s += 7
        if not c & 0x80: return x, i


def pb(b, depth=0, maxd=6):
    """Decodifica bytes em [(campo, valor)]; valores length-delimited viram sub-mensagem, texto ou bytes crus."""
    i, out = 0, []
    while i < len(b):
        try:
            k, i = _varint(b, i)
            f, w = k >> 3, k & 7
            if f == 0 or f > 200: return None
            if w == 0:
                v, i = _varint(b, i); out.append((f, v))
            elif w == 2:
                n, i = _varint(b, i)
                if i + n > len(b): return None
                ch = b[i:i + n]; i += n
                sub = pb(ch, depth + 1, maxd) if depth < maxd and n else None
                try:
                    txt = ch.decode("utf-8"); txt = txt if txt.isprintable() else None
                except UnicodeDecodeError:
                    txt = None
                out.append((f, txt if txt is not None else (sub if sub is not None else ch)))
            elif w == 1:
                out.append((f, b[i:i + 8])); i += 8
            elif w == 5:
                out.append((f, b[i:i + 4])); i += 4
            else:
                return None
        except IndexError:
            return None
    return out


def raw_fields(b):
    """Como pb(), mas sem interpretar: length-delimited sempre como bytes (para colunas empacotadas)."""
    i, out = 0, []
    while i < len(b):
        k, i = _varint(b, i)
        f, w = k >> 3, k & 7
        if w == 0:
            v, i = _varint(b, i); out.append((f, v))
        elif w == 2:
            n, i = _varint(b, i); out.append((f, b[i:i + n])); i += n
        elif w == 1:
            out.append((f, b[i:i + 8])); i += 8
        elif w == 5:
            out.append((f, b[i:i + 4])); i += 4
        else:
            raise ValueError("wire")
    return out


def ndic(b):
    """Dicionário NDIC (nomes por índice): cabeçalho, tabela de comprimentos (1 byte por nome, ou varint no formato antigo) e as strings coladas."""
    count = int.from_bytes(b[12:16], "little")

    def cut(i, ls):
        out, p = [], i
        for n in ls:
            out.append(b[p:p + n].decode("utf-8", "replace")); p += n
        return out if all(x.isprintable() for x in out) else None             # descarta cortes coincidentes (com bytes de controle)
    for L0 in range(16, min(len(b), 4096)):
        ls = b[L0:L0 + count]
        if len(ls) == count and L0 + count + sum(ls) == len(b):                       # formato com 1 byte por comprimento
            r = cut(L0 + count, ls)
            if r: return r
        try:
            i, vs = L0, []
            for _ in range(count):
                n, i = _varint(b, i); vs.append(n)
            if i + sum(vs) == len(b):
                r = cut(i, vs)
                if r: return r
        except IndexError:
            pass
    raise ValueError("NDIC não reconhecido")


def packed_bytes(v):
    return list(v) if isinstance(v, (bytes, bytearray)) else [ord(c) for c in v]


def packed_varints(v):
    b = v if isinstance(v, (bytes, bytearray)) else v.encode("latin1")
    i, out = 0, []
    while i < len(b):
        x, i = _varint(b, i); out.append(x)
    return out


# ---------------------------------------------------------------- coleta
def state():
    d = json.loads(get(BASE + "/data/index-state"))
    cur = next(x for x in d["snapshotVersions"] if x["url"] and not x["url"].endswith("hc") and x["name"] == d["economyLeagues"][0]["name"])
    return d, cur


def search(version, overview, extra=""):
    raw = get(f"{BASE}/builds/{version}/search?overview={overview}&type=exp{extra}")
    top = pb(raw)[0][1]
    return raw, top


def facets(top, dicts):
    """{faceta: [(índice, contagem)]} das mensagens campo 2; ids de dicionário no campo 6."""
    out = {}
    for f, v in top:
        if f == 2 and isinstance(v, list):
            name = v[0][1]
            out[name] = [(dict(x).get(1, 0), dict(x).get(2, 0)) for ff, x in v if ff == 3 and isinstance(x, list)]
    return out


def dict_hashes(top):
    res = {}
    for f, v in top:
        if f == 6 and isinstance(v, list):
            res[v[0][1]] = [x[1] for x in v[1:]]
    return res


def dictionary(h, cache):
    if h not in cache:
        cache[h] = ndic(get(f"{BASE}/builds/dictionary/{h}"))
    return cache[h]


def columns(raw):
    """Colunas de personagens (campo 12 da mensagem principal), sem interpretar os bytes: {coluna: {campo: [valores]}}."""
    top = dict((f, v) for f, v in raw_fields(raw))[1]
    cols = {}
    for f, v in raw_fields(top):
        if f == 12:
            d = {}
            for ff, vv in raw_fields(v):
                d.setdefault(ff, []).append(vv)
            cols[d[1][0].decode()] = d
    return cols


def num(s):
    m = re.match(r"([\d.]+)\s*([kmb]?)", s or "", re.I)
    return float(m.group(1)) * {"": 1, "k": 1e3, "m": 1e6, "b": 1e9}[m.group(2).lower()] if m else None


def top_rows(raw):
    """Personagens do topo do filtro: nível, EHP e DPS totais (números do poe.ninja, calculados pelo PoB dele)."""
    cols = columns(raw)
    g = lambda c, k: cols.get(c, {}).get(k, [])
    dk = next((k for k in cols if k.startswith("dps") and k.endswith(".total")), "dps.total")     # com filtro de skill a coluna vira dps-<Skill>.total
    dps, ehp = [x.decode() for x in g(dk, 7)], [x.decode() for x in g("ehp__str", 7)]
    lv = list(g("level", 6)[0]) if g("level", 6) else []
    return [{"lv": lv[j] if j < len(lv) else None, "dps": num(dps[j]), "ehp": num(ehp[j])} for j in range(min(len(dps), len(ehp)))]


def med(rs, k, q=.5):
    v = sorted(r[k] for r in rs if r.get(k))
    return v[min(len(v) - 1, int(len(v) * q))] if v else None


def add_extras(out, version, overview):
    """Skills das builds do site que não estão entre as mais usadas da ascendência: consulta direta com o filtro de skill (o total da resposta é a contagem)."""
    import registry
    for b in registry.IDENT:
        a = out["ascendancies"].get(b["asc"])
        if not a: continue
        have = {x["skill"] for x in a["skills"]}
        for name in b["ninja"]:
            if name in have: continue
            try:
                raw = get(f"{BASE}/builds/{version}/search?overview={overview}&type=exp&class={urllib.parse.quote(b['asc'])}&skills={urllib.parse.quote(name)}")
                n = next(v for f, v in pb(raw)[0][1] if f == 1)
                rs = top_rows(raw)
            except Exception:
                continue
            a["skills"].append({"skill": name, "n": n, "share": round(n / a["n"] * 100, 1), "top": len(rs), "dps": med(rs, "dps"), "dpsP75": med(rs, "dps", .75), "ehp": med(rs, "ehp"), "lv": med(rs, "lv")})
            print(f"  + {b['asc']}: {name} ({n})", flush=True)
            time.sleep(.25)


def main():
    if "--extras-only" in sys.argv:
        out = json.load(open(OUT, encoding="utf-8"))
        add_extras(out, out["snapshot"], out["overview"])
        json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("extras salvos"); return
    league = next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--league"), None)
    per = int(next((sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--skills"), 12))
    st, cur = state()
    overview = league or cur["snapshotName"]; version = cur["version"]
    print("liga", cur["name"], "snapshot", version)
    cache = {}
    raw, top = search(version, overview)
    dh = dict_hashes(top)
    cls = dictionary(dh["class"][0], cache)
    fc = facets(top, cache)
    total = next(v for f, v in top if f == 1)
    cls_counts = {cls[i]: c for i, c in fc["class"] if i < len(cls)}
    out = {"league": cur["name"], "overview": overview, "snapshot": version, "fetched": time.strftime("%Y-%m-%d"), "characters": total, "passiveTree": cur.get("passiveTree"),
           "ascendancies": {}}
    for a in sorted(cls_counts, key=lambda k: -cls_counts[k]):
        if cls_counts[a] < 150: continue                                # ascendências sem amostra
        q = "&class=" + urllib.parse.quote(a)
        try:
            raw2, t2 = search(version, overview, q)
        except Exception as e:
            print("falhou", a, e); continue
        gem = dictionary(dict_hashes(t2)["gem"][0], cache)
        f2 = facets(t2, cache)
        rows_a = top_rows(raw2)
        skills = []
        for i, c in sorted(f2.get("skills", []), key=lambda x: -x[1])[:per]:
            if i >= len(gem) or c < 40: continue
            try:
                r3 = get(f"{BASE}/builds/{version}/search?overview={overview}&type=exp{q}&skills={urllib.parse.quote(gem[i])}")
                rs = top_rows(r3)
            except Exception:
                rs = []
            skills.append({"skill": gem[i], "n": c, "share": round(c / cls_counts[a] * 100, 1), "top": len(rs), "dps": med(rs, "dps"), "dpsP75": med(rs, "dps", .75), "ehp": med(rs, "ehp"), "lv": med(rs, "lv")})
            time.sleep(.25)
        out["ascendancies"][a] = {"n": cls_counts[a], "share": round(cls_counts[a] / (total or 1) * 100, 2), "top": {"n": len(rows_a), "dps": med(rows_a, "dps"), "ehp": med(rows_a, "ehp")}, "skills": skills}
        print(f"{a:24} {cls_counts[a]:6} {out['ascendancies'][a]['share']:5}%  " + ", ".join(f"{s['skill']}({s['share']}%)" for s in skills[:3]), flush=True)
    add_extras(out, version, overview)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("salvo", os.path.relpath(OUT, HERE))


if __name__ == "__main__":
    main()
