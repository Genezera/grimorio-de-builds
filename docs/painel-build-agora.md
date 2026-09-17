# Seu build, agora

O painel foi reconstruído para as duas builds, em PT/EN, em `shared/build-now.js` e `shared/build-now.css`. O gerador remove a implementação antiga antes de carregar a nova.

## Organização

- **Agora:** foco da fase, até três prioridades, checklist de marcos, acesso ao personagem, passivas e planejamento de Spirit/totems.
- **Equipamento:** lista da fase adaptada ao personagem, imagens com proporção preservada, nomes completos e acesso ao guia/crafting. O texto distingue recomendações de inventário real.
- **Skills:** skill, papel no setup e supports identificados por nome e ícone.

A partir de 1440 px, o painel ocupa uma coluna lateral recolhível. Abaixo disso, abre uma gaveta de até 480 px; no celular, usa a largura disponível. Em paisagem baixa, o cabeçalho fica compacto. O conteúdo tem rolagem própria, independente do cabeçalho e dos controles de fechamento.

Inclui animação de entrada, transição de conteúdo, destaque de seleção e efeitos de hover. Movimento reduzido desativa animações e transições. O modal gerencia foco, Escape, Tab/Shift+Tab, bloqueio do fundo e restauração ao fechar ou mudar para desktop. A seção escolhida e os marcos são salvos por build, compartilhados entre idiomas.

## Validação

- 480 estados do painel: quatro páginas, níveis 1/35/70/95, três seções, dez viewports entre 320×568 e 2560×1440, incluindo 844×390 e os dois lados do breakpoint 1439/1440.
- Verificação de limites do painel e dos cards, ausência de overflow horizontal e acesso à última ação por rolagem.
- Abertura, fechamento, foco, teclado, atalhos, recolhimento, mudança de viewport e persistência de seção.
- Rodada adicional de 48 estados em 390×844 e testes de persistência dos marcos e animação com/sem movimento reduzido.
- Regressão geral: 340 visualizações de abas, 576 rotas de crafting, sem erros de JavaScript ou overflow.
- Auditoria de layout das oito páginas: 920 verificações em dez tamanhos, sem sobreposições detectadas ou overflow de página.
- Inspeção visual de capturas no celular, tablet e desktop.

Testado no Edge via Playwright. Nenhuma matriz finita garante todos os dispositivos, navegadores, níveis de zoom e larguras possíveis. Tabelas e navegações horizontais próprias continuam podendo rolar dentro de seus contêineres.
