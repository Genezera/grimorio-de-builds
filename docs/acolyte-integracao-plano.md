# Plano de integração e simplificação — Acolyte Poison/Archon

## Objetivo

Transformar a página do Acolyte em um companheiro de progressão único e coerente. O nível, o ato, os itens, as skills, os supports, a ascendência e o objetivo atual (limpar mapa ou matar boss) precisam alimentar a mesma recomendação.

O trabalho é exclusivo do **Monk Acolyte of Chayula**. Não haverá Gemling.

## Diagnóstico

Hoje há conteúdo útil, mas cada aba responde a uma pergunta isolada:

- **Agora** cita Splinterheart, The Lethal Draw e Ghostmarch, porém não sabe se o jogador já os conseguiu.
- **Meu personagem** registra poucos buffs e itens de endgame; não representa a barra real de skills de cada ato.
- **Skills** mostra um setup prescrito, mas não deixa evidente o que já está disponível, o que falta e o que deve sair.
- **Itens** explica progressão e alternativas, mas não fecha o ciclo com as recomendações do painel “Seu build, agora”.
- **Chamas & Archon**, **Árvore**, **Ascendência** e **Atlas** têm informações necessárias, porém algumas prioridades aparecem em mais de um lugar sem uma ação principal clara.
- O mesmo jogador pode receber uma recomendação já concluída ou ver uma peça de leveling muito depois de ela ter perdido valor.

A causa é o modelo de dados: itens, skills e marcos não compartilham uma identidade e um estado comuns.

## Modelo de estado

Cada escolha terá uma chave estável e pertencerá a uma categoria:

1. **Skills ativas** — Poisonburst Arrow, Toxic Growth, Vine Arrow, Contagion, Plague Bearer, Into the Breach, Despair, Pounce e Archon of Chayula.
2. **Skills persistentes** — Herald of Blood, Herald of Plague, Wind Dancer, Ghost Dance e Blasphemy.
3. **Supports decisivos** — Concentrated Area, Bursting Plague, Bleed, Escalating Poison, Deadly Poison, Fork e os supports do Archon.
4. **Equipamento** — incluindo Splinterheart, The Lethal Draw, Ghostmarch e suas substituições.
5. **Ascendência, árvore e conteúdo** — Waking Dream, Choice of Power, snapshot do Weapon Set 2, Tul/Esh e Archon.

O estado salvo no navegador continuará compatível com as marcações existentes. Novas marcações serão adicionadas sem apagar o progresso atual.

## Regra de adaptação

O sistema cruza quatro dimensões:

- **nível/fase**: define o que já pode ser usado e o que ficou obsoleto;
- **posse**: indica o que o jogador efetivamente tem;
- **perfil**: leveling, clear ou boss;
- **dependências**: skill, support, Spirit, item, ascendência e conteúdo que desbloqueia outra peça.

Uma recomendação deve dizer:

- qual é a ação;
- por que ela importa agora;
- onde resolver;
- qual alternativa usar enquanto faltar;
- quando a peça deixa de ser prioridade.

Exemplo: no Ato 2, Splinterheart melhora muito a cobertura; The Lethal Draw melhora dano/velocidade do arco; Ghostmarch melhora mobilidade. Depois, cada um deve ganhar uma instrução clara de comparação ou substituição, sem permanecer como pendência eterna.

## Perfis de combate

### Leveling

Prioriza desbloqueio simples, mana sustentável, movimento e poucos botões. O sistema mostra apenas as skills relevantes ao nível atual e sinaliza Contagion como temporária.

### Clear

Prioriza cobertura e cadeia de mortes:

- Poisonburst Arrow como ataque principal;
- Fork quando a fase e os sockets permitirem;
- Herald of Blood e Herald of Plague para propagar mortes;
- Plague Bearer para acelerar packs densos;
- Vine Arrow/Toxic Growth apenas em raros e packs resistentes;
- mobilidade e alcance antes de dano de alvo único quando essa troca melhora o ritmo do mapa.

### Boss

Prioriza sobreposição e multiplicadores:

- Concentrated Area em Toxic Growth;
- boss posicionado sobre as pústulas;
- Poisonburst Arrow alimentando veneno na área;
- Vine Arrow, Despair e Plague Bearer conforme a fase;
- chamas roxas e Choice of Power;
- Archon e seus tornados no endgame;
- crítico e Garukhan's Resolve somente quando o limiar necessário for atingido.

Os dois perfis mostrarão o que muda na barra, nos supports e na rotação. O jogador não precisará deduzir quais peças pertencem a clear ou boss.

## Estrutura das abas

### Agora

Será a fila curta de ações. No máximo três prioridades, ordenadas por bloqueio, dano e qualidade de vida. Cada cartão abre diretamente a aba que resolve a pendência.

### Meu personagem

Será o único lugar para registrar estado:

- números (Spirit, crítico e resistência a caos);
- skills ativas;
- buffs e reservas;
- supports decisivos;
- itens por etapa;
- ascendência, árvore e desbloqueios.

As listas serão agrupadas por função, com descrições curtas. A página indicará que marcar significa “tenho e posso usar”, não “está obrigatoriamente equipado agora”.

### Skills

Será o montador da barra atual:

- alternância **Clear / Boss**;
- status **tenho**, **falta** ou **futuro**;
- skills principais antes das utilidades;
- supports dentro da skill correta;
- rotação curta e específica do perfil;
- aviso de dependência ausente e alternativa imediata.

### Itens

Será a progressão por slot. Cada item mostrará a janela em que vale a pena, a troca seguinte e o efeito prático. Splinterheart, The Lethal Draw e Ghostmarch serão conectados às marcações de posse e às recomendações.

### Árvore, Ascendência, Chamas & Archon e Atlas

Cada aba manterá apenas a decisão que lhe pertence:

- **Árvore**: próxima rota e snapshot do Set 2;
- **Ascendência**: ordem dos pontos e efeito de cada marco;
- **Chamas & Archon**: mecânica, execução e rotações;
- **Atlas**: desbloqueio de Tul/Esh e conteúdo de endgame.

O painel “Agora” será o índice de pendências; essas abas serão a explicação e a execução.

### Demais abas

Quests, crafting, diagnósticos e fontes serão auditados para remover instruções duplicadas, corrigir destinos de links e garantir que cada uma responda a uma pergunta clara. Nenhuma aba deverá exigir que o jogador procure a continuação da mesma instrução em outra parte sem um link direto.

## Navegação e simplificação

- Agrupar a navegação visualmente em **Jogar agora**, **Montar a build** e **Referência**.
- Preservar acesso direto por teclado e leitura por leitor de tela.
- Em telas estreitas, usar rolagem horizontal previsível e manter a aba ativa visível.
- Evitar blocos longos antes da ação principal.
- Usar os mesmos nomes e ícones para a mesma skill/item em toda a página.
- Mostrar uma legenda curta para “tenho”, “falta” e “futuro”.

## Responsividade

Validar pelo menos 360×800, 390×844, 768×1024, 1024×768, 1366×768 e 1440×900:

- nenhuma rolagem horizontal no documento;
- abas e filtros acessíveis;
- cartões sem texto ou imagens cortados;
- painel “Seu build, agora” utilizável como drawer no celular e lateral no desktop;
- alvos de toque adequados;
- foco visível, Escape e navegação por teclado funcionando;
- `prefers-reduced-motion` respeitado.

## Validação funcional

Serão testados estes percursos:

1. personagem novo sem marcações;
2. Ato 2 com Splinterheart, The Lethal Draw e Ghostmarch;
3. campanha sem Concentrated Area;
4. mapas sem snapshot;
5. Archon bloqueado por Tul/Esh;
6. Archon não crítico;
7. min-max crítico abaixo e acima do limiar;
8. troca entre Clear e Boss;
9. persistência após recarregar;
10. português e inglês.

Também serão executados os testes do projeto, auditoria de links internos, inspeção de console e capturas nas larguras principais.

## Critério de conclusão

O Acolyte estará concluído quando uma única atualização em **Meu personagem** mudar de forma coerente:

- as prioridades de **Agora**;
- os status e alternativas de **Skills**;
- o equipamento relevante;
- o painel lateral;
- e os avisos de mecânica, árvore, ascendência ou atlas relacionados.

O jogador deverá conseguir responder sem procurar em várias abas: **o que uso agora, o que me falta, o que troco para clear, o que troco para boss e qual é minha próxima melhoria real**.
