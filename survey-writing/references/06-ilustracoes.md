# Fase 6 — Ilustrações

Base: Niyato et al., Seção II-F ("Illustration").

## Regra de posicionamento: nada na Introdução

Nenhum dos tipos abaixo — figura, tabela, gráfico ou qualquer `\includegraphics`/`\begin{table}` — aparece na Introdução (seção 1 do artigo). A primeira ilustração do artigo surge a partir da seção 2 (Background, quando existir, ou a subseção de taxonomia do corpo principal, quando não existir Background). Ver `references/03-estrutura-taxonomias.md`, seção "Regras de conteúdo da Introdução".

## Os tipos (avalie cada um para o seu artigo — o item 2b é obrigatório, os demais nem sempre)

1. **Figura de estrutura da survey**: mapa visual da organização do artigo (taxonomia adotada). Fica na primeira subseção do corpo principal ("Taxonomia adotada" — ver `references/03-estrutura-taxonomias.md`), **nunca na Introdução**: a Introdução não leva ilustrações, só um resumo em prosa do framework.
2. **Tabelas de resumo/comparação**: comprimem literatura extensa em formato comparável lado a lado. Um caso especial importante: a tabela comparando a survey atual com surveys relacionadas — é a peça central para demonstrar diferenciação (ligação direta com a Fase 1). Fica no Background, quando essa seção existir; na ausência de Background, fica na primeira subseção do corpo principal (taxonomia adotada) — **nunca na Introdução**, que trata surveys relacionadas apenas de forma superficial, sem tabela.
2b. **Tabela de classificação da taxonomia (obrigatória)**: mapeia **todas** as referências incluídas na Fase 2 para a subseção do corpo principal (eixo principal ou transversal) a que cada uma foi atribuída, seguindo exatamente a mesma hierarquia confirmada na Fase 3. Fica sempre na primeira subseção do corpo principal ("Taxonomia adotada"), logo após a apresentação/justificativa do critério de organização — é o que torna a taxonomia verificável, não apenas descrita em prosa. Ver seção "Tabela de classificação da taxonomia" abaixo para o formato e o script que a gera.
3. **Figuras técnicas**: diagramas de modelo de sistema, pilha de protocolo, framework arquitetural — ancoram seções individuais.
4. **Resultados experimentais**: curvas de desempenho, medições, comparações de latência — só use dados reais extraídos/citados da literatura ou de análise própria feita via script; nunca invente números "ilustrativos".
5. **Lista de abreviações**: se o artigo usa muitas siglas, uma tabela dedicada melhora a legibilidade.

## Tabela de classificação da taxonomia

Esta tabela é o elo de auditoria entre a matriz de literatura e a taxonomia do artigo: qualquer leitor (ou o próprio usuário) deve conseguir conferir, olhando só essa tabela, onde cada uma das referências coletadas na Fase 2 foi alocada.

- **Cobertura completa**: toda referência que passou pela triagem da Fase 2 (`status_triagem` = incluída) aparece exatamente uma vez na tabela — nenhuma pode ficar de fora, mesmo que só receba citação agrupada (nunca tratamento individual) no corpo do texto.
- **Estrutura**: uma linha (ou bloco) por subseção do corpo principal, na mesma ordem confirmada na Fase 3 (taxonomia → eixos principais → transversais). Cada linha lista as chaves de citação daquele grupo, tipicamente como `\cite{a,b,c,...}` compactado (não uma linha por referência) — para grupos grandes, considere uma coluna adicional só com a contagem de trabalhos, para não sobrecarregar a célula de citações.
- **Fonte de dados**: a coluna `subtema_provisorio` de `literature/literature_matrix.csv`, **atualizada na Fase 3** para conter o nome final da subseção (eixo/transversal) confirmada com o usuário — não o rótulo provisório da Fase 2. Nunca monte essa tabela "de cabeça": gere-a por script.
- **Script**: `scripts/gen_taxonomia_table.py`, que lê `literature/literature_matrix.csv`, agrupa por `subtema_provisorio` na ordem da taxonomia confirmada, e escreve a tabela LaTeX em `artigo/figures/tabela_taxonomia.tex`, incluída via `\input{figures/tabela_taxonomia.tex}` dentro da subseção "Taxonomia adotada". Regere o script (e a tabela) sempre que a atribuição de alguma referência a uma subseção mudar — a tabela nunca é editada manualmente no `.tex`.
- Isso não substitui a tabela comparativa de surveys relacionadas (item 2) nem as tabelas comparativas por grupo (item 2, quando >5 trabalhos com dimensões comparáveis) — são objetos distintos: a de classificação mapeia *todas* as referências à taxonomia; as demais comparam *dimensões técnicas* de subconjuntos específicos.
- **Gatilhos de regeneração (vale para o projeto inteiro, não só a Fase 3)**: regenere `scripts/gen_taxonomia_table.py` sempre que qualquer um destes eventos ocorrer, em qualquer fase: (a) uma referência é incluída ou excluída em `literature/literature_matrix.csv` (Fase 2, inclusive complementos pedidos depois, ex. na Fase 4 ou 7); (b) a taxonomia, a lista de eixos/transversais, ou o título/ordem de alguma subseção do corpo principal muda (revisão da Fase 3, ou qualquer ajuste estrutural posterior); (c) a atribuição de uma referência a uma subseção (`subtema_provisorio`) muda. A tabela é sempre a **última coisa a rodar antes de compilar**, nunca uma foto antiga da matriz — e a Fase 8 confirma isso como parte da auditoria final (ver `SKILL.md`, Fase 8).

## Regra de consistência texto-figura

Toda figura/tabela deve ser (a) referenciada explicitamente no texto próximo de onde aparece e (b) discutida, não apenas citada de passagem ("ver Figura X" sem comentário nenhum é insuficiente). Verifique isso na auditoria da Fase 8.

## Scripts de geração

- Qualquer ilustração que dependa de processamento de dados (contagem de publicações, agregação de métricas da matriz de literatura, comparações quantitativas) deve ter um script correspondente em `scripts/` do projeto — nunca gere o número "de cabeça".
- Nomeie os scripts de forma rastreável à figura que geram (ex.: `scripts/fig_publication_trend.py` → `artigo/figures/publication_trend.pdf`).
- Se o script consome a matriz de literatura (`literature/literature_matrix.csv`), documente isso no cabeçalho do próprio script.
- Depois de gerar a figura, verifique visualmente (via `view` da imagem) se ela está legível e coerente com o que o texto vai afirmar, antes de inserir no LaTeX.

## Checkpoint com o usuário

Antes de gerar qualquer figura de "resultados experimentais" ou que dependa de um levantamento que você mesmo precisaria estimar (ex.: número de publicações por ano em uma base específica), confirme com o usuário a fonte exata dos dados — não estime silenciosamente.

## O que registrar em research.md

- Lista de figuras/tabelas criadas, tipo (dos itens acima), e localização no artigo.
- Para figuras geradas por script: qual script, qual fonte de dados, data de geração.
- Para a tabela de classificação da taxonomia (item 2b): confirmação de que o total de referências tabuladas bate com o total de referências `incluídas` na Fase 2.
