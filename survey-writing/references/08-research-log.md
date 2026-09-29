# research.md — protocolo de log e índice de referências

`research.md`, na raiz do projeto, é a fonte de verdade do projeto inteiro — não só desta skill. Tem **duas partes com regras diferentes**:

1. **Índice de Referências** — seção fixa no topo do arquivo, entre marcadores `<!-- INDICE-REFERENCIAS:START -->` e `<!-- INDICE-REFERENCIAS:END -->`. É uma tabela que reflete o **estado atual** da coleção de referências (incluída na survey, com PDF disponível localmente ou não). Diferente do log abaixo, esta seção **é atualizada em lugar**, não é append-only — não faz sentido manter histórico de "essa referência tinha status X ontem". Nunca edite essa tabela na mão: regenere-a com `scripts/sync_reference_index.py`, que lê `literature/literature_matrix.csv` (fonte de verdade) e substitui só o conteúdo entre os marcadores, sem tocar no resto do arquivo.
2. **Log de Atividades** — todo o restante do arquivo, abaixo do índice. Este sim é o diário de pesquisa clássico: append-only, cobrindo ações, decisões, dúvidas e interações do processo de escrita.

## Formato da seção "Índice de Referências"

```
<!-- INDICE-REFERENCIAS:START -->
## Índice de Referências

_Gerado automaticamente por `scripts/sync_reference_index.py` a partir de `literature/literature_matrix.csv`. Não editar manualmente — rode o script novamente após qualquer mudança na matriz._

| ID | Título | Ano | Venue | PDF local |
|---|---|---|---|---|
| exemplo2025 | Título do trabalho de exemplo | 2025 | IEEE Trans. XYZ | ✅ `literature/pdfs/exemplo2025.pdf` |
| outro2024 | Outro trabalho | 2024 | ACM Conf. ABC | ❌ indisponível (acesso pago) — https://doi.org/... |

<!-- INDICE-REFERENCIAS:END -->
```

Regras do conteúdo da tabela:
- Uma linha por item com `status_triagem = incluído` na matriz (itens excluídos não entram no índice).
- Coluna "PDF local": `✅` + caminho quando `pdf_status = baixado`; `❌ indisponível (acesso pago) — <url>` quando `indisponivel_pago`; `❌ não encontrado` quando `indisponivel_nao_encontrado`; `⏳ pendente` quando `pendente`.

## Regras do Log de Atividades (parte append-only)

- **Append-only**: nunca edite ou apague entradas antigas. Só adicione ao final (ou ao final da fase corrente, se estiver organizando por fase).
- **Uma entrada por evento relevante**, não um resumo geral no fim do dia. Registre no momento em que a coisa acontece, não em lote no final da sessão.
- **Tipos de entrada** (use exatamente estas etiquetas):
  - `AÇÃO` — algo que você (a skill) executou (ex.: rodou uma busca, gerou um esqueleto de arquivo, criou uma figura, baixou um PDF).
  - `DECISÃO` — uma escolha feita, pelo usuário ou proposta por você e confirmada por ele. Sempre inclua a alternativa escolhida e, se houve outras opções na mesa, quais foram descartadas e por quê.
  - `DÚVIDA` — uma incerteza levantada durante o processo (pode ficar em aberto por um tempo). Quando for resolvida, adicione uma nova entrada `DECISÃO` referenciando a dúvida original (não edite a entrada da dúvida).
  - `INTERAÇÃO` — um checkpoint em que você parou o fluxo para perguntar algo ao usuário; registre a pergunta feita e a resposta recebida, mesmo que a resposta já apareça também como uma `DECISÃO` separada (a entrada `INTERAÇÃO` preserva o contexto da pergunta).

## Formato de cada entrada do log

```
### [AAAA-MM-DD] Fase <N> — <título curto>
**Tipo:** DECISÃO
<corpo de 1 a 4 linhas>
```

Várias entradas podem ter a mesma data/fase — não precisa consolidar em uma seção única por dia.

## Exemplo

```
### [2026-09-17] Fase 1 — Crítica do tema inicial
**Tipo:** DÚVIDA
Tema inicial "modelos de linguagem de grande porte (LLMs) para geração automática
de testes de software" — busca exploratória encontrou 2 surveys de 2025 com escopo
muito próximo. Volume estimado de literatura específica (excluindo essas 2
surveys): ~40 trabalhos. Risco: tema pode estar subdimensionado ou já coberto.

### [2026-09-17] Fase 1 — Decisão de escopo
**Tipo:** DECISÃO
Usuário optou por ampliar o escopo para "LLMs para automação de atividades de
teste de software" (não só geração de casos de teste, mas também priorização e
manutenção de testes), elevando o volume estimado para ~85 trabalhos e
diferenciando-se das 2 surveys existentes por incluir manutenção e priorização
além de geração pura. Alternativa descartada: manter escopo original e focar em
uma crítica mais profunda em vez de escopo mais amplo — usuário preferiu a via
de ampliação de escopo.
```

## Onde a skill deve consultar este arquivo

No início de cada sessão em que a skill for retomada, leia `research.md` inteiro (índice + log, ou pelo menos a fase mais recente do log) antes de perguntar de novo algo que já foi decidido — o objetivo do log é justamente evitar retrabalho e perguntas repetidas.
