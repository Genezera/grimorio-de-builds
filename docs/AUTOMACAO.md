# Automação do Grimório

O que roda sozinho, o que decide por número e o que ainda precisa de uma pessoa (ou de uma sessão do Claude) — sem prometer o que não existe.

## O ciclo (toda segunda, ou sob demanda)

`.github/workflows/update.yml` → `tools/update_all.py`:

| Etapa | Script | O que faz | Automático? |
|---|---|---|---|
| Coleta | `ninja_meta.py` | Lê a API de builds do poe.ninja (liga atual detectada sozinha): quantos personagens usam cada ascendência e cada skill, e DPS/EHP dos personagens do topo de cada combinação | Sim |
| Classificação | `registry.py` | Classe, ascendência, estilo e **rankings**: mais fácil, mais difícil, dano, clear, boss, clear + boss, mais resistente, fora do meta | Sim |
| Descoberta | `discover.py` | Lista combinações ascendência + skill **fora do meta**, fortes e **sem guia** aqui → `docs/candidates.md` | Sim |
| Reconstrução | `build_all.py` | Regera todas as páginas | Sim |
| Auditoria | `audit.py` | Procura o que está perdido, quebrado ou impossível de seguir → `docs/audit.md` | Sim |
| Testes | `unittest` | Suíte do repositório | Sim |
| Publicação | workflow | Faz commit **só se auditoria e testes passarem**; se não, abre/atualiza uma issue com o relatório | Sim |

Rodar à mão: `python tools/update_all.py` (`--no-fetch` usa o snapshot salvo; `--no-build` só dados e auditoria).

## Como cada ranking é calculado

- **Fácil / difícil** — do próprio guia: skills ativas, passos de rotação, reservas de Spirit, supports, truques e uniques exigidos, relativos às builds do site. Silverfist e Oracle (que não usam o kit) têm nota editorial.
- **Dano** — percentil do DPS mediano dos personagens do topo daquela ascendência + skill, entre todas as combinações do poe.ninja. Número deles (PoB do poe.ninja), não meu.
- **Mais resistente** — mesmo método com o EHP.
- **Fora do meta** — parcela da skill dentro da ascendência: ≥ 25% meta, 5–25% alternativa, < 5% fora do meta.
- **Clear e boss** — hoje **notas editoriais** (1–5) em `IDENT` de `registry.py`; o boss mistura com o percentil de dano. O poe.ninja não expõe medida de clear, então isso não é automático ainda e a landing avisa.

## O que a auditoria verifica

Faixas de nível sem lacuna nem sobreposição, gems que entram depois do fim da fase, supports sem explicação, uniques definidos e nunca usados (ou usados sem definição), níveis inválidos, slots sem opção barata, Spirit acima do plausível, árvore desconectada do início da classe, fontes sem URL, páginas ausentes, `undefined`/`NaN` no texto visível, arquivos de `shared/` referenciados e inexistentes, pastas com `index.html` fora do registro, snapshot velho e builds em `revisar` (ninguém mais usa a skill principal).

- **Erro** reprova o ciclo. **Aviso** vai para o relatório. **Info** mostra o estado.
- Build com status `revisar` é a candidata a sair: o ciclo **avisa**, não apaga. Para aposentar, mude `status` para `aposentada` no registro — ela some da landing e das listas, e o histórico do Git guarda tudo.

## O que ainda NÃO é automático

1. **Escrever um guia novo.** O ciclo *acha* a candidata e mostra os números; montar as fases nível a nível, itens, árvore e rotação com sentido é trabalho de curadoria (fica na issue "Automação"). Publicar guia gerado sem revisão vai contra o objetivo "dá para seguir sem problema".
2. **"Divertida" e "fácil de seguir".** Não há número para isso; a facilidade calculada é uma proxy (menos botões e reservas). A escolha final é humana.
3. **Preços de uniques.** O poe.ninja deixou de responder o endpoint de uniques usado antes; o ciclo atualiza o que a API expõe. Os preços dos uniques nos guias continuam do último snapshot.
4. **Verificar no jogo.** A auditoria confere coerência interna e dados; nenhum robô joga a build. Alguém precisa jogar o Ato 1 de vez em quando.
