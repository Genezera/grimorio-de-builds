# Grimório de Builds · Build Grimoire — Path of Exile 2

Guias interativos de build para Path of Exile 2 — patch 0.5.5, liga Forbidden Rites. Cada guia vai do nível 1 ao 100, explica cada gem, support, item, unique e passiva, e se adapta ao que você marca em **Meu personagem** (nível, Spirit, itens que já tem).

Interactive build guides for Path of Exile 2 — patch 0.5.5, Forbidden Rites league. Each guide goes from level 1 to 100, explains every gem, support, item, unique and passive, and adapts to what you tick in **My character** (level, Spirit, items you already own).

Site: https://genezera.github.io/trilha-silverfist/

| Página / Page | Conteúdo / Content |
|---|---|
| `index.html` · `en.html` | Página inicial para escolher a build · Build picker (PT · EN) |
| `silverfist/index.html` · `silverfist/en.html` | Huntress · Spirit Walker — Mighty Silverfist zoo (guia do Mattjestic) |
| `oracle/index.html` · `oracle/en.html` | Druid · Oracle — Spell Totem (guia do Lowepe) |

O botão **PT / EN** troca de idioma; o progresso de cada build é compartilhado entre as duas versões (localStorage `silverfist2:` e `oracle1:`).
The **PT / EN** switch changes language; each build's progress is shared between both versions.

O site é 100% estático (HTML + JS) e também funciona abrindo os arquivos direto no navegador.
The site is fully static (HTML + JS) and also works by opening the files directly in a browser.

## Estrutura / Structure

```
index.html, en.html           página inicial · landing page
silverfist/                   app Spirit Walker (index.html, en.html, assets/assets.js)
oracle/                       app Oracle (index.html, en.html, assets/assets.js)
planilha/                     planilha Excel do Silverfist · Silverfist Excel workbook (PT)
tools/                        scripts do Silverfist + página inicial · Silverfist + landing scripts
tools/oracle/                 scripts do Oracle · Oracle scripts
```

## Regenerar / Rebuild (opcional)

Requer Python 3 com `openpyxl` e `Pillow`.

```bash
cd tools
python build_assets.py        # assets.json do Silverfist (árvore, ícones, sets)
python build_site.py          # ../silverfist/index.html, en.html, assets/assets.js
python build_xlsx.py          # out.xlsx
python build_landing.py       # ../index.html e ../en.html (usa assets.json e oracle/assets.json)

cd oracle
python extract.py             # dl/oracle_variants.json (variantes do Mobalytics)
python oassets.py             # assets.json do Oracle
python opatch.py              # app_template.html do Oracle (a partir do template do Silverfist)
python obuild.py              # ../../oracle/index.html, en.html, assets/assets.js
```

- Dados Silverfist: `tools/chober.py`; tradução `tools/i18n/en_*.json` e `tools/ui_en.py`.
- Dados Oracle: `tools/oracle/odata.py` (textos bilíngues), lógica `ochar.js`, `oadapt.js`, `ototem.js`.
- Dados de jogo: Path of Building PoE2 (`tools/dl/pob/`), preços poe.ninja.

## Fontes / Sources

Mattjestic e Lowepe (Mobalytics), imortilize (Mobalytics), Zizaran (Maxroll), poe.ninja, PoE2DB e dados do Path of Building (PoE2). Preços da liga são um retrato do momento da pesquisa · League prices are a snapshot from research time.

Projeto de fã, sem vínculo com a Grinding Gear Games. Path of Exile é marca da Grinding Gear Games.
Fan project, not affiliated with Grinding Gear Games.
