# Fase 4 — Síntese crítica / redação da revisão (e auditoria na Fase 8)

Base: Niyato et al., Seção II-D ("Review Section Writing") e III ("Discussion and Conclusion").

## O erro central a evitar

Os próprios autores apontam isso como a falha editorial mais comum: tratar a survey como um catálogo (um parágrafo = um resumo de um artigo, encadeados) em vez de uma síntese que revela padrões, contradições e insights que só emergem da análise conjunta. Um teste prático: se um parágrafo poderia ser substituído, sem perda, pelo abstract do artigo citado, ele não está agregando valor de survey.

## Processo por grupo/subseção

1. **Releitura orientada**: releia os itens do grupo focando em identificar, não em resumir: progressões técnicas (trabalho B melhora A em quê, ao custo de quê), abordagens paralelas (mesma tarefa, caminhos distintos), limitações compartilhadas, trade-offs recorrentes, contradições entre autores.
2. **Lista de insights antes da prosa**: escreva 3-6 bullets de insight coletivo por grupo. Exemplo do próprio artigo: "melhorias de desempenho em algoritmos de consenso blockchain consistentemente exigem aumento de complexidade de comunicação" — isso é um insight, não um resumo.
3. **Checkpoint com o usuário**: mostre essa lista de insights antes de escrever o texto corrido da seção. É muito mais barato corrigir a leitura crítica aqui do que reescrever prosa depois.
4. **Prosa**: só depois de validados os insights, escreva a seção em prosa, organizando por progressão técnica ou por abordagens paralelas (o que fizer mais sentido para o grupo). **Agrupe citações por afirmação compartilhada** — uma frase de síntese cobrindo vários trabalhos com `\cite{a,b,c}` (3-8 chaves é o padrão esperado), não uma frase dedicada a cada referência; reserve tratamento individual a ~2-4 trabalhos seminais por grupo. Isso não é só estilo: é o que mantém a extensão do artigo dentro do orçamento definido na Fase 0 (ver `references/09-controle-extensao.md`, seção 3) — tratamento individual de cada referência é, ao mesmo tempo, a causa da compilação rasa (este erro) e do artigo inchado.
5. **Linguagem**: hedging acadêmico apropriado ("os resultados sugerem", "evidências indicam", evitar generalizações categóricas não sustentadas pela literatura revisada); comparações explícitas entre abordagens quando relevante.
6. **Tabela comparativa**: se o grupo tiver mais de ~5 trabalhos com dimensões comparáveis (métrica, método, aplicação, limitação), monte uma tabela em vez de tentar comparar tudo em prosa (ver Fase 6) — é também o destino natural para trabalhos que não justificam citação individual nem entram numa frase agrupada.

## Auditoria de estilo (usar também na Fase 8, sobre o artigo inteiro)

Perguntas de verificação, seção por seção:
- Existe algum parágrafo que é essencialmente um resumo de um único artigo, sem comparação ou síntese com os demais do grupo?
- Há muitas frases estruturalmente idênticas do tipo "o trabalho N faz M \cite{n}." (teste de bloat)? Se sim, reagrupe por ideia compartilhada (ver `references/09-controle-extensao.md`, seção 3).
- As transições entre parágrafos seguem uma lógica (técnica, cronológica, temática) ou é só uma lista encadeada?
- Toda tabela/figura é referenciada e discutida no texto próximo, e não apenas mencionada de passagem?
- A introdução de cada seção principal deixa claro o que o leitor vai aprender e por que essa organização foi escolhida?
- Há redundância entre seções que pode ser cortada (fase de "compressão" do pipeline)?

Se alguma resposta indicar problema, corrija antes de considerar a fase/seção concluída — não deixe para "revisar depois" sem registrar isso como pendência em `research.md`.

## O que registrar em research.md

- Por seção: os insights validados pelo usuário no checkpoint.
- Qualquer correção de rumo pedida pelo usuário (ex.: "essa seção ainda está resumindo, não sintetizando").
- Na Fase 8: resultado da auditoria final, seção por seção, e o que foi corrigido.
