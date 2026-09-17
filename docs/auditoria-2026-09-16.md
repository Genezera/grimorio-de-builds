# Revisão de funcionamento, responsividade e conteúdo

Escopo: oito páginas PT/EN — entrada, Silverfist, Oracle e Forbidden Rites — e seus geradores. Patch de referência: 0.5.5.

## Correções

- Receitas avançadas: Divines precedem o Infuser opcional que pode corromper. Qualidade, sockets e augments também vêm antes dessa etapa. A descrição do Divine não sugere santificar no meio da receita.
- As etapas avançadas reordenadas têm novas chaves de conclusão, para não atribuir uma marca antiga à operação errada. O progresso anterior permanece no armazenamento; as outras rotas mantêm suas chaves.
- Transmutation/Augmentation não são apresentadas como rerrolagem ilimitada da mesma base. Annulment também funciona em Magic, com risco de remover o mod útil.
- Charms comuns são descritos como Magic, em acordo com a receita.
- Repetir Desecration inclui os Omens de Lich/lado consumidos, além dos materiais já listados.
- Comparar trade e crafting depende dos preços e dos mods; removida a promessa de que comprar é quase sempre mais barato.
- O cartão da base acompanha a receita selecionada. A rota econômica mantém a opção genérica de compra; as demais mostram a base da receita detalhada.
- O filtro de mods da wand Oracle inclui níveis de Cold Spell Skills, em acordo com os alvos da receita.
- Materiais exibem o valor em Divine do cache, sem taxa Exalted inventada nem arredondamento mínimo para 1 Exalted.
- No planejador de Omens, preço desconhecido do Omen ou da currency de ativação permanece desconhecido. Não entra como custo zero na seleção mais barata. Quando os filtros deixam poucas opções conhecidas, o resultado informa que é um subtotal e um plano incompleto.
- A leitura dos preços de challenges verifica se a unidade primária é Divine. O texto explicita que bases, Catalysts e materiais de preparação não integram esse subtotal.
- Checkboxes de chefes dos Rites e de Omens têm nomes acessíveis específicos.

## Verificações

- Auditoria automática inicial: 920 verificações em dez viewports, de 320×640 a 2560×1440, incluindo paisagem, com zero sobreposições detectadas ou overflow de página.
- Após as correções: outras 270 verificações nas páginas afetadas, em 320×640, 390×844 e 1366×900, novamente sem problemas detectados.
- Navegador Edge/Playwright: 30 visitas principais, 340 visualizações de abas e 576 combinações de receita, sem erros de execução nem overflow. Inclui buscas, teclado, links internos, persistência PT/EN, calculadoras e cenários de preços ausentes.
- Teste de receitas: 144 rotas localizadas verificam que a etapa opcional de corrupção é a última operação.
- Cinco testes Python das regras de probabilidade, famílias e preços passaram.
- 94 referências locais estáticas conferidas nas oito páginas; nenhum arquivo ausente.
- Inspeção visual de capturas desktop e mobile; reconstrução completa pelo gerador.

## Fontes e limites

Conferidos os requisitos principais das challenges (11 Rites, 15 rares, quatro provas, nível 90, 50 uniques, 18 Omens, árvores 36/31/35 e três pinnacles) com [a lista de desafios](https://poe2db.tw/us/Forbidden_Rites_challenges). Mecânicas gerais e recompensas foram comparadas com as notas oficiais [0.5.5](https://www.pathofexile.com/forum/view-thread/4000864) e [0.5.0](https://www.pathofexile.com/forum/view-thread/3932540). A distinção entre operações Magic/Rare foi conferida na [referência de crafting](https://poe2db.tw/us/Crafting).

Essa auditoria não equivale a uma simulação completa do jogo: preços são snapshots, pesos publicados não garantem chances reais e recomendações de build dependem do personagem e do mercado. Não houve validação individual de cada roll de cada item nem teste em todos os navegadores/dispositivos físicos. A auditoria geométrica detecta sobreposições entre elementos de conteúdo; não prova contraste, legibilidade ou ausência de toda obstrução por elementos flutuantes. As capturas visuais complementam esse teste.
