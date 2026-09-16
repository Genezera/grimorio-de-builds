# Grimório de Builds · Build Grimoire — Path of Exile 2

Guias interativos de build para Path of Exile 2 — patch 0.5.5, liga Forbidden Rites. Cada guia vai do nível 1 ao 100, explica cada gem, support, item, unique e passiva, e se adapta ao que você marca em **Meu personagem** (nível, Spirit, itens que já tem).

Interactive build guides for Path of Exile 2 — patch 0.5.5, Forbidden Rites league. Each guide goes from level 1 to 100, explains every gem, support, item, unique and passive, and adapts to what you tick in **My character** (level, Spirit, items you already own).

Site: https://genezera.github.io/trilha-silverfist/

| Página / Page | Conteúdo / Content |
|---|---|
| `index.html` · `en.html` | Página inicial para escolher a build · Build picker (PT · EN) |
| `silverfist/index.html` · `silverfist/en.html` | Huntress · Spirit Walker — Mighty Silverfist zoo (guia do Mattjestic) |
| `oracle/index.html` · `oracle/en.html` | Druid · Oracle — Spell Totem (guia do Lowepe) |
| `rites/index.html` · `rites/en.html` | Liga Forbidden Rites — guia das 8 challenges (checklists, planejador de Omens, progresso salvo) |

O botão **PT / EN** troca de idioma; o progresso de cada build é compartilhado entre as duas versões (localStorage `silverfist2:` e `oracle1:`).
The **PT / EN** switch changes language; each build's progress is shared between both versions.

O site é 100% estático (HTML + JS) e também funciona abrindo os arquivos direto no navegador.
The site is fully static (HTML + JS) and also works by opening the files directly in a browser.

## Oficina e navegação / Workshop and navigation

- Todas as seis páginas foram redesenhadas, com versões PT/EN, layout responsivo e contraste de leitura maior.
- Navegação por assunto, busca local por itens/skills/conceitos (`Ctrl/Cmd+K`), links diretos às seções e impressão da seção aberta.
- Crafting nas duas builds: 12 categorias de equipamentos, três rotas de investimento (comprar · craft progressivo · avançado) com receitas concretas por build em `shared/craft-detail.js` — alvos com ilvl, essence/omen/osso/alloy pelo nome, custos de Verisium, materiais com preço do poe.ninja e o que fazer se falhar.
- Glossário de mecânicas, consulta de pesos com hipótese explícita e simulador de custo/risco, incluindo compra pronta e orçamento de 90%.
- Visual Path of Exile 2 (`shared/poe2.css`, `shared/poe2.js`, `shared/art/`): paleta, fontes e arte de ascendência próprias de cada build (Spirit Walker: ouro, teal espectral e carmesim; Oracle: prata, violeta do destino e ciano), cenário de fundo que muda a cada aba, trilha de níveis com gemas, partículas, animações de entrada e layout para celular, tablet, paisagem e ultrawide. Respeita `prefers-reduced-motion`.
- Dados de crafting e limites do modelo: [documentação de fontes](tools/craft/README.md).

All six pages share a redesigned responsive interface. Both builds include searchable navigation, section links, printing, persistent crafting plans for 12 equipment categories, a mechanics glossary, an opt-in published-weight explorer and a cost/risk simulator. Unverified weights and undated prices are explicitly labelled.

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

Para reconstruir apenas o site usando os snapshots locais, basta Python 3 (biblioteca padrão):

```bash
python tools/build_all.py
python -m http.server 8000
```

Abra `http://localhost:8000`. O servidor local oferece uma origem consistente para compartilhar progresso PT/EN; o comportamento de localStorage em `file://` varia por navegador. `openpyxl` e `Pillow` são necessários apenas para os fluxos de planilha/regeneração de imagens abaixo.

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

## Verificação / Verification

```bash
python -m unittest discover -s tools/tests -v
# Com Playwright disponível no Node (e o navegador instalado):
node tools/tests/browser.cjs
```

O teste de navegador usa um servidor temporário local, testa as seis páginas em 1366px, 1024px e 768px (tablet) e 390px (celular), percorre todas as abas e as rotas de crafting, verifica overflow, busca, teclado, persistência PT/EN, deep links e limites das calculadoras. `BROWSER_CHANNEL=msedge` permite usar o Edge instalado; `SCREENSHOT_DIR` habilita capturas fora do repositório.

## Fontes / Sources

Mattjestic e Lowepe (Mobalytics), imortilize (Mobalytics), Zizaran (Maxroll), poe.ninja, PoE2DB e dados do Path of Building (PoE2). Preços da liga são um retrato do momento da pesquisa · League prices are a snapshot from research time.

Projeto de fã, sem vínculo com a Grinding Gear Games. Path of Exile é marca da Grinding Gear Games.
Fan project, not affiliated with Grinding Gear Games.
