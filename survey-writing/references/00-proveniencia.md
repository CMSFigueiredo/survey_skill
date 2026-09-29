# Proveniência desta skill

## Histórico de escopo

A v1 desta skill foi redigida usando o artigo de Niyato et al. como referência direta, o que deixou vocabulário e exemplos (venues, bases de dados, critérios de citação) enviesados para comunicações/redes, já que é a comunidade de origem do artigo. Na revisão seguinte, o escopo foi generalizado para Computação e Engenharia como um todo — os 7 pilares metodológicos do artigo (crítica de tema, taxonomia, síntese crítica, ilustrações, desafios futuros) são domain-agnostic dentro dessas áreas; apenas os exemplos e as bases de dados precisaram ser ampliados (ver `references/02-coleta-literatura.md` e `references/01-selecao-tema.md`).

Esta skill foi montada a partir de um levantamento de skills públicas de terceiros (não instaladas por padrão), analisadas contra os 7 pilares de Niyato et al. (2026, "From Literature to Insights: Methodological Guidelines for Survey Writing in Communications Research", arXiv:2509.25828). Nenhuma dessas skills foi copiada literalmente — os conceitos e estruturas foram adaptados e reescritos para este fluxo.

## Skills do levantamento inicial (cobriam parte dos pilares)

| Skill de origem | Pilar(es) de Niyato cobertos | O que foi incorporado aqui | O que foi deixado de fora / adaptado |
|---|---|---|---|
| `literature-scout` (repo `luwill/research-skills`) | Coleta de literatura | Ideia de matriz de literatura com deduplicação e filtro por citação/cobertura | Fontes específicas (arXiv, Semantic Scholar, PapersWithCode) generalizadas para "bases configuráveis pelo usuário", já que aqui o alvo é Computação e Engenharia como um todo (IA/ML é uma das subáreas possíveis, não a única) |
| `systematic-review` (repo `beita6969/scienceclaw`, PRISMA 2020) | Coleta de literatura (parcial) | Rigor de protocolo de busca e triagem documentada | Deliberadamente **não** foi trazido o aparato de meta-análise quantitativa (GRADE, forest plots, risco de viés estatístico) — não se aplica a uma survey narrativa de engenharia; ver Fase 2 |
| `survey-writer` (repo `luwill/research-skills`) | Estrutura, síntese crítica | Ideia de templates de seção com tabelas comparativas e linguagem de "hedging" acadêmico | Generalizado para os 4 padrões de taxonomia de Niyato em vez de um template fixo único |
| `paper-writing-skill` (repo `SNL-UCSB`) | Estrutura, síntese crítica, integração final | O pipeline em 5 estágios (Brainstorming → Architecture → Section Drafts → Integration → Compression) inspirou a divisão em Fases 3/4/8; o "mandatory style audit gate" virou a Fase 8 | Regras editoriais específicas do laboratório de origem não foram trazidas (são de outro domínio) |
| `figure-generation` / `data-visualization` (repo `lingzhi227/agent-research-skills`) | Ilustrações | Ideia de gerar figuras a partir de script versionado, com verificação de qualidade antes de aceitar | Especificidades de "VLM feedback loop" não foram detalhadas aqui; a skill apenas exige script rastreável + fonte de dados confirmada |
| `citation-management` (repo `lingzhi227/agent-research-skills`) | Coleta de literatura (gestão) | BibTeX como formato de referência, deduplicação de citações | — |

## Gap identificado e busca adicional realizada

No levantamento inicial, **nenhuma skill cobria adequadamente a escrita de seções de tutorial** (pilar 5 de Niyato — pedagogia, objetivos de aprendizagem, progressão do básico ao avançado, estudos de caso). Foi feita uma busca adicional e localizada a família de skills `learning-pedagogy` / `curriculum-design` / `curriculum-develop-content` (repo `pauljbernard/content`), voltada a design instrucional. Desse material foram incorporados, na Fase 5:
- A prática de declarar objetivos de aprendizagem explícitos antes de escrever o conteúdo.
- A ideia de progressão pedagógica controlada (evitar sobrecarga cognitiva, construir subseções que se apoiam umas nas outras).

O restante do aparato de design curricular (nivelamento de idioma, coaching, metacognição) não é relevante para um artigo científico e foi deixado de fora.

## O que não veio de nenhuma skill (decisão original desta skill)

- A exigência de **crítica obrigatória do tema antes de qualquer coleta** (Fase 1) — nenhuma skill do levantamento tratava disso como etapa formal com critério quantitativo (limiar de 50-120 referências de Niyato); foi formalizado aqui.
- O **protocolo de log em `research.md`** e a separação rígida de subdiretórios (`artigo/`, `scripts/`, `literature/`) — requisito explícito do usuário desta skill, sem equivalente direto no levantamento.
- Os **pontos de interação obrigatórios** (checkpoints) em cada fase — nenhuma das skills levantadas era interativa por design; a maioria assume execução autônoma de ponta a ponta, o que o próprio artigo de Niyato implicitamente desaconselha ao enfatizar julgamento editorial em quase toda etapa.
- A **auditoria local de PDFs** (`literature/pdfs/`) e o **Índice de Referências** mantido em `research.md` (com status explícito de disponibilidade local por item, gerado por `scripts/sync_reference_index.py`) — nenhuma skill do levantamento (nem `literature-scout`, nem `citation-management`) ia além de gerenciar metadados/BibTeX; a materialização de uma cópia auditável de cada referência, com registro de por que ela não está disponível quando não foi possível baixar, foi acrescentada por pedido explícito do usuário desta skill.
