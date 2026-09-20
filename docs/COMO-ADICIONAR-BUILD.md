# Como adicionar uma build (e o que ela precisa ter)

Este é o passo a passo e o **contrato** de uma build do Grimório. Uma build só está pronta quando o jogador consegue seguir do nível 1 ao 100 sem adivinhar nada, e quando `python tools/audit.py` diz **0 erros e 0 avisos**. O contrato é conferido pela própria auditoria (`check_contract` e `check_registration`), então o que está aqui não é opinião: é o que o código cobra.

> Regra de ouro: **nunca invente número**. Nível de unique, tier de gem, preço, efeito de skill e pontos de árvore vêm de dados (poe.ninja, Path of Building, RePoE, PoE2DB) ou o texto diz "aproximado" / "adaptação". O que for opinião (ordem do ranking de itens, notas de clear/boss) fica marcado como opinião.

## 1. De onde vem a build

| Fonte | O que traz | O que costuma faltar (você cria) |
|---|---|---|
| **PoB** (poe.ninja `pob/<id>`, Maxroll `pob/<id>`) | Árvore final, gems, itens do endgame, joias, ascendência | **Leveling inteiro**: fases, árvore por nível, itens por nível |
| **Maxroll planner** (`planners.maxroll.gg/profiles/poe2/<id>`) | Perfis (Campaign/Maps/Endgame), árvore por perfil, itens, joias | Ranking de itens por nível, explicações |
| **Mobalytics** (variantes Leveling/Endgame) | Variantes por fase, joias e afixos desejados | Idem; confira que a árvore de leveling tem dano |

Como baixar: PoB do Maxroll → `curl https://maxroll.gg/poe2/api/pob/<id>` (texto do código) e `https://planners.maxroll.gg/profiles/poe2/<id>` (metadados). Salve o código em `tools/dl/<bid>_pob.txt`.

## 2. O contrato: o que TODA build precisa ter

**Identidade**
- `bid` (pasta, sem espaço), `key` de 2 letras (classe CSS do card), classe, ascendência, nome PT/EN, emoji, paleta (`shared/poe2.css`).
- Nomes das skills como o poe.ninja mostra (`ninja=[...]` em `tools/registry.py`) para o ranking automático.

**7 fases** `a1 a2 a3 a4 maps endgame max` (níveis 1–15, 16–31, 32–45, 46–64, 65–78, 79–90, 91–100). Cada fase tem: `goal`, `rotation`, `gems` (com suportes), `stats`, `tree`, `avoid`, `exit`, `cheap`, `full`, `spiritNote`.

**Skills**
- Entram no nível em que o jogo deixa (Uncut Skill/Spirit Gem: nível do gem = `Tier` do `dl/pob/Gems.lua`).
- Todo suporte usado tem uma linha em `SUPWHY` (o teste reprova sem isso).
- Reservas de Spirit fecham o orçamento: quests dão 30 (~10), +30 (~38), +40 (~62); itens e ascendência dão o resto. A fase diz de onde vem cada ponto.
- Descrições de skill e suporte: copie do `skills_*.lua` do PoB, não de memória.

**Árvore**
- Cada fase é um corte (17/34/50/72/95 pontos) numa ordem de alocação **conectada** a partir do início da classe.
- **Meça o dano por fase** com `python tools/deepcheck.py <bid>` (soma `% increased ... Damage`, velocidade, crítico e vida dos nós de cada corte; a auditoria `tree-damage` reprova campanha com 17+ nós e quase nenhum dano). Uma árvore de campanha com 0% de dano é erro: foi exatamente o bug da Whirling. Se a build tem nós de **mecânica** sem número (cargas, minions), eles vão primeiro numa lista manual (`PRIORITY`): a ordem gulosa `pobxml.walk_greedy` pode pular eles.
- Se a campanha usa nós que saem no endgame, diga quantos e **quando** é o respec.
- **A árvore de campanha não precisa ser um corte da árvore final.** Se o caminho da árvore final a partir do início da classe é uma fila de nós de atributo (Legionnaire: 16 nós, Shaman: 25), a campanha fica sem dano por 30 níveis. Nesse caso monte a campanha com `pobxml.staged_greedy` (ordem 'dano primeiro' em estágios que fecham nos cortes 17/34/50/72/95) sobre a árvore final + os nós a até ~14 passos do início, use `kit/treescore.py` para medir o valor de cada nó **para esta build** (um caster não quer nó de melee; um Legionnaire não quer projétil) e diga em `FIXES` que é adaptação e quando é o respec (ver `builds/shaman/retree.py` e `builds/legionnaire/mkvariants.py`).
- **Nós de mecânica no nível certo.** Passe em `must={corte: [nomes]}` os notáveis/keystones que a build precisa (ex.: Elemental Equilibrium no corte do nível 32–45) e em `ban=` os que só fazem sentido depois. Se o caminho até o nó não cabe nos pontos do corte, ele entra no corte seguinte: ajuste o texto e o `when` de `KEY_PASSIVES`.
- **O texto da fase só pode citar o que o corte tem.** A auditoria (`tree-text`) compara os notáveis citados no texto 'Árvore' de cada fase com os nós do corte e dos Weapon Sets. Prometer Brain Storm numa árvore que nunca o aloca foi o problema do Shaman.
- Joias: qual joia em qual socket (`kit/jewels.py` lê PoB, Mobalytics e Maxroll). Sem joias na fonte: a aba avisa e a auditoria registra `jewels-none`.

**Itens**
- `UNIQUES` com nível: deixe o `U()` preencher pelo **`levelRequired` do poe.ninja** (o nível da base engana: Idol of Uldurn é 24, não 1).
- `GEAR` + `gear_opts.py`: por slot, opções (unique ou rare) com nível, custo (Grátis/Barato/Valor/Luxo) e por que. O ranking é opinião declarada; nível e preço são dados.
- Barato mostra só Grátis+Barato; Completo mostra tudo o que já é possível no nível.
- Itens do PoB sem preço nem nível no poe.ninja entram como Luxo com nível estimado e o texto diz "confira no jogo".

**Ascendência**: 4 Trials (`ASC_UNLOCK`, `ASC_PHASE`), com o que cada nó faz e por que serve a esta build.

**Textos honestos**: `FIXES` diz o que é adaptação, estimativa ou aproximação. Se o autor não validou a progressão, escreva isso.

**Crafting**: `bcraft.py` com os itens que valem craft **e o item `amulet`** (o teste usa). A classe da arma precisa de `tools/dl/web/<Classe>.html` (baixe do PoE2DB: `https://poe2db.tw/us/<Classe>`), depois `craft/db.load('<Classe>')` gera o cache.

**Extras obrigatórios**: `TRICKS`, `TROUBLESHOOT`, `ATLAS_CHECK`, `CASES`, `BUY_ORDER`, `MILESTONES`, `TIMING` (`T(...)`), `MECH` (cards, rotação, tabela de weapon sets, Spirit, linha do tempo), `CHAR` (o que marcar em "Meu personagem" e as regras de recomendação), `SOURCES` com URL.

## 3. Passo a passo

1. **Dados**: baixe o PoB/planner; confira classe, ascendência, gems, itens, joias.
2. **Entenda a mecânica** lendo as descrições no PoB (`dl/pob/skills_*.lua`, `Gems.lua`). Anote o que uma skill consome/gera: isso decide a rotação e o que não pode faltar na árvore.
3. **`tools/builds/<bid>/mkvariants.py`**: gera `tools/dl/<bid>_variants.json` (árvore por fase, itens por fase, joias). Copie o da `twister` (PoB) ou da `whirling`.
4. **`gear_opts.py`**: ranking de itens por nível. Copie o da build mais parecida e troque as armas e as peças finais do PoB.
5. **`bdata.py`**: fases, gems, textos. Comece pelo da `twister`.
6. **`bcraft.py`**: kit de crafting.
7. **Registro nos arquivos compartilhados** (a auditoria lista o que faltar): `shared/fx.js`, `shared/loader.js` (2 lugares), `shared/poe2.js`, `shared/poe2.css`, `shared/landing.css`, `tools/enhance.py`, `tools/landing_v2.py`, `tools/build_landing.py`, `tools/registry.py`, `tools/build_all.py`, `tools/tests/{browser,mobile,overlap,build-now}.cjs`, `tools/tests/test_links.py`, README. Arte: `python tools/kit/mkart.py <key> tools/dl/art/<ilustracao>.webp <key-da-classe> [cool|wind]`.
8. **Gerar**:
   ```bash
   python tools/builds/<bid>/mkvariants.py
   python tools/kit/kassets.py <bid> && python tools/kit/kpatch.py <bid> && python tools/kit/kbuild.py <bid>
   python tools/registry.py && python tools/build_landing.py
   ```
9. **Verificar** (todos precisam passar):
   ```bash
   python tools/audit.py                      # 0 erros, 0 avisos
   python -m unittest discover -s tools/tests
   node tools/tests/browser.cjs               # 0 erros de runtime, 0 overflow
   PAGES=<bid>/index.html,<bid>/en.html node tools/tests/mobile.cjs
   ```
10. **Conferência manual** (a auditoria não joga):
    - Nível 1, 20, 45, 70, 90 na aba **Itens**: nada de item de nível alto como recomendação em nível baixo.
    - Aba **Árvore**: as joias aparecem com o anel dourado e a fase certa.
    - Compare o **dano da árvore por fase** com o das outras builds (o script está na conversa de criação: some os `% increased damage` dos nós da ordem exibida).
    - Leia o guia como um jogador do nível 1: existe algo que ele não tem como fazer?
11. **Commit e push**. O ciclo semanal (`.github/workflows/update.yml`) roda tudo de novo e só publica se passar.

## 4. Se a fonte NÃO tiver... (o que criar)

| Falta na fonte | Faça |
|---|---|
| Leveling (só endgame) | Skills do endgame desde o nível 1 pelo `Tier`; árvore por corte com ordem gulosa + reserva de nós de projétil perto do início (peso 40%); itens pelo ranking por nível. Escreva em `FIXES` que é adaptação. |
| Ordem da árvore por nível | `pobxml.walk_greedy` (dano/velocidade/crítico/vida por ponto gasto) e **confira nós de mecânica**. |
| Itens por nível | `gear_opts.py` com `levelRequired` do poe.ninja (unique) e nível da base do RePoE (rare). |
| Joias | Se o PoB/planner tem, `jewels.py` lê. Se a fonte não define, deixe assim: a aba avisa e a auditoria registra. Não invente. |
| Spirit | Some as reservas por fase e confira o orçamento; fontes de Spirit: quests, Enfolding Dawn (+100), amuleto, sceptre, ascendência. |
| Preço | poe.ninja (`tools/dl/eco_*.json`). Sem preço: Luxo + "confira". |
| Descrição de skill | `dl/pob/skills_*.lua`. |
| Kit de crafting da classe da arma | Baixe a página do PoE2DB e gere o cache (item 2 acima). |

## 5. Como o jogador segue o guia

1. **Nível**: o controle "Você está em" (ou o slider) escolhe a fase. Tudo na página se ajusta.
2. **Barato / Completo**: Barato mostra o que é grátis ou custa menos de 1 Divine; Completo mostra tudo o que já é possível no seu nível.
3. **Agora**: o que fazer neste momento, uma prioridade por vez.
4. **Meu personagem**: marque o que você tem e o Spirit; as abas Skills, Itens e Árvore se adaptam.
5. **Skills & Supports**, **Itens** (ranking por slot com "próximo upgrade"), **Árvore** (caminho por nível, joias e sockets) e **Ascendência** (Trials na ordem).
6. Se algo ficar fraco, anote o **ato e contra quê** (pack ou boss): o guia é ajustado a partir disso.

## 6. O que a auditoria cobra (resumo)

Contrato completo, texto de árvore que só cita notáveis que o corte tem, dano de árvore por fase, faixas de nível sem lacuna, suportes sem explicação, uniques definidos e nunca usados, níveis de item, Spirit plausível, árvore conectada pela ordem que a página mostra, sockets de joia alocados, fontes com URL, páginas e arquivos existentes, build registrada em todos os arquivos compartilhados, snapshot do poe.ninja recente. Detalhes em `docs/AUTOMACAO.md`.
