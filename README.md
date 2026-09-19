# Grimório de Builds · Build Grimoire — Path of Exile 2

Guias interativos de build para Path of Exile 2 — patch 0.5.5, liga Forbidden Rites. Cada guia vai do nível 1 ao 100, explica cada gem, support, item, unique e passiva, e se adapta ao que você marca em **Meu personagem** (nível, Spirit, itens que já tem).

Interactive build guides for Path of Exile 2 — patch 0.5.5, Forbidden Rites league. Each guide goes from level 1 to 100, explains every gem, support, item, unique and passive, and adapts to what you tick in **My character** (level, Spirit, items you already own).

Site: https://genezera.github.io/grimorio-de-builds/

| Página / Page | Conteúdo / Content |
|---|---|
| `index.html` · `en.html` | Página inicial para escolher a build · Build picker (PT · EN) |
| `silverfist/index.html` · `silverfist/en.html` | Huntress · Spirit Walker — Mighty Silverfist zoo (guia do Mattjestic) |
| `oracle/index.html` · `oracle/en.html` | Druid · Oracle — Spell Totem (guia do Lowepe) |
| `tactician/index.html` · `tactician/en.html` | Mercenary · Tactician — Pin2Win Grenades (guia do BlazeworksTV) |
| `infernalist/index.html` · `infernalist/en.html` | Witch · Infernalist — Spark → Cast on Critical Comet, recoup e CoA de luxo (guias do Ignatius e do kingkongor) |
| `acolyte/index.html` · `acolyte/en.html` | Monk · Acolyte of Chayula — Poisonburst Arrow + Archon of Chayula (planner do Goratha, Maxroll) |
| `pathfinder/index.html` · `pathfinder/en.html` | Ranger · Pathfinder — poison bow → Corpsewade Decompose (guias do Skadoosh) |
| `smith/index.html` · `smith/en.html` | Warrior · Smith of Kitava — Shield Wall + Avatar of Fire (guia do Lexd) |
| `martial/index.html` · `martial/en.html` | Monk · Martial Artist — Oil Barrage + Cast on Critical + Lightning Warp (planner do havoc616, Maxroll + ladder do poe.ninja) |
| `shaman/index.html` · `shaman/en.html` | Druid · Shaman — Archmage Spark + Comet automatizado por Cast on Critical (os 10 Shamans de maior DPS do poe.ninja) |
| `legionnaire/index.html` · `legionnaire/en.html` | Mercenary · Gemling Legionnaire — Falling Thunder com cajado e Power Charges (PoB nível 96 do poe.ninja) |
| `whirling/index.html` · `whirling/en.html` | Mercenary · Gemling Legionnaire — Whirling Slash + Glacial Bolt (besta de gelo; skills do endgame já no leveling: Whirling Slash desde o nível 1 e Glacial Bolt do ~24; árvore de dano na campanha e respec no 79) — guia do Phylaris POE (Mobalytics) |
| `whirling/whirling-glacial-bolt.filter` | Loot filter da build (camada para colar no topo do seu filtro); `python tools/build_filter.py --install` monta por cima do NeverSink e grava em Documents/My Games/Path of Exile 2 |
| `rites/index.html` · `rites/en.html` | Liga Forbidden Rites — guia das 8 challenges (checklists, planejador de Omens, progresso salvo) |

O botão **PT / EN** troca de idioma; o progresso de cada build é compartilhado entre as duas versões (localStorage `silverfist2:`, `oracle1:`, `tactician1:`, `infernalist1:`, `acolyte1:`, `pathfinder1:`, `smith1:`, `martial1:`, `shaman1:`, `legionnaire1:`, `whirling1:`).
The **PT / EN** switch changes language; each build's progress is shared between both versions.

O site é 100% estático (HTML + JS) e também funciona abrindo os arquivos direto no navegador.
The site is fully static (HTML + JS) and also works by opening the files directly in a browser.

## Oficina e navegação / Workshop and navigation

- Todas as páginas usam a mesma camada visual **skin v3** (`shared/skin.css`, `shared/skin.js`, `shared/fx.css`, `shared/fx.js`): cabeçalho compacto, navegação em uma linha (Agora · Power/mecânica · Rota · Skills · Itens · Árvore · Ascendência + menu **Mais** com Meu personagem, Uniques, Crafting, Quests, Truques, Diagnóstico e Fontes), painéis planos, seções secundárias da aba Agora dobradas e uma animação de assinatura por classe (raio, fogo, forja, inferno, vazio, veneno, espíritos, estrelas) no medalhão de cada build e nos cartões da página inicial. Tudo respeita `prefers-reduced-motion`.
- Navegação por assunto, busca local por itens/skills/conceitos (`Ctrl/Cmd+K`), links diretos às seções e impressão da seção aberta.
- Crafting nas duas builds: 12 categorias de equipamentos, três rotas de investimento (comprar · craft progressivo · avançado) com receitas concretas por build em `shared/craft-detail.js` — alvos com ilvl, essence/omen/osso/alloy pelo nome, custos de Verisium, materiais com preço do poe.ninja e o que fazer se falhar.
- Glossário de mecânicas, consulta de pesos com hipótese explícita e simulador de custo/risco, incluindo compra pronta e orçamento de 90%.
- Visual Path of Exile 2 (`shared/poe2.css`, `shared/poe2.js`, `shared/art/`): paleta, fontes e arte de ascendência próprias de cada build (Spirit Walker: ouro, teal espectral e carmesim; Oracle: prata, violeta do destino e ciano), cenário de fundo que muda a cada aba, trilha de níveis com gemas, partículas, animações de entrada e layout para celular, tablet, paisagem e ultrawide. Respeita `prefers-reduced-motion`.
- Tela de carregamento e transições (`shared/loader.css`, `shared/loader.js`): medalhão com a arte da ascendência da build (ou do grimório), anéis e faíscas animados, barra de progresso real e abertura em íris ao revelar a página; ao clicar num link do site, a cortina se fecha já com a build de destino. Não bloqueia cliques, some em até 5 s mesmo em rede lenta, respeita `prefers-reduced-motion` e fica desligada em testes automatizados (`?loader=1` força).
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
tactician/ infernalist/ acolyte/ pathfinder/ smith/ martial/ shaman/ legionnaire/ whirling/   apps gerados pelo kit · kit-generated apps
tools/kit/                    kit genérico de builds (extract/maxroll → kassets → kpatch → kbuild, js/, craftkit)
tools/builds/<build>/         dados de cada build do kit (bdata.py, bcraft.py) · per-build kit data
```

## Adicionar uma build a partir de um Path of Building / Adding a build from a PoB

1. Baixe o código do PoB (ex.: `https://poe.ninja/poe2/pob/raw/<id>`) para `tools/dl/<build>_pob.txt`.
2. Crie `tools/builds/<build>/mkvariants.py` (veja o do Legionnaire): `kit/pobxml.py` decodifica o PoB, corta a árvore por pontos em fases e monta os itens de cada fase. `pobxml.walk_order` gera a ordem de alocação que a classe realmente consegue seguir (útil quando o PoB parte de outro ponto inicial, como com a joia Split Personality).
3. Escreva `bdata.py` (fases, gems por nível, uniques, textos PT/EN) e, se quiser crafting, `bcraft.py`.
4. `python tools/kit/mkart.py <prefixo> <ilustração>` gera a arte da build em `shared/art/`; registre a build em `shared/poe2.js`, `shared/poe2.css`, `shared/loader.js`, `shared/fx.js`, `tools/enhance.py`, `tools/build_all.py`, `tools/build_landing.py`, `tools/landing_v2.py` e nas listas de `tools/tests`.

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
- Builds do kit: `python tools/kit/extract.py <build> <fonte>` (Mobalytics) ou `python tools/kit/maxroll.py <build> <fonte> "Perfil[@passo]|pontos|nome|Ascendências..."` (Maxroll; perfis com várias variantes viram uma variante cada), depois `kassets.py`, `kpatch.py` e `kbuild.py <build>` (o `build_all.py` já roda os três).
- Dados de jogo: Path of Building PoE2 (`tools/dl/pob/`), bases do RePoE2 (`tools/dl/repoe_*.json`), preços poe.ninja.

## Verificação / Verification

```bash
python -m unittest discover -s tools/tests -v
# Com Playwright disponível no Node (e o navegador instalado):
node tools/tests/browser.cjs
node tools/tests/recipes.cjs  # ordem de finalização das receitas PT/EN
node tools/tests/build-now.cjs # painel adaptável, teclado, rolagem e movimento reduzido
# Auditoria de sobreposição (todas as abas, 10 tamanhos de tela, PT/EN):
node tools/tests/overlap.cjs
# Celular e tablet (texto cortado, fora da tela, toque pequeno, fonte minúscula, imagem distorcida, vãos vazios):
node tools/tests/mobile.cjs
```

O teste de navegador usa um servidor temporário local, testa as 14 páginas das 7 builds e as duas da entrada em 1366px, 1024px, 768px e 390px, além das duas páginas de challenges. Percorre todas as abas e rotas de crafting, verifica overflow, busca, teclado, persistência PT/EN, deep links, limites das calculadoras e preços ausentes no planejador de Omens. Também verifica as builds no nível 95 em 320px e 1920px. `BROWSER_CHANNEL=msedge` permite usar o Edge instalado; `SCREENSHOT_DIR` habilita capturas fora do repositório.

## Fontes / Sources

Mattjestic, Lowepe, BlazeworksTV, Ignatius, kingkongor, Skadoosh e Lexd (Mobalytics), Goratha e havoc616 (Maxroll), imortilize (Mobalytics), Zizaran (Maxroll), poe.ninja, PoE2DB e dados do Path of Building (PoE2). Preços da liga são um retrato do momento da pesquisa · League prices are a snapshot from research time.

Projeto de fã, sem vínculo com a Grinding Gear Games. Path of Exile é marca da Grinding Gear Games.
Fan project, not affiliated with Grinding Gear Games.
