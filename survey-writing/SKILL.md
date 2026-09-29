---
name: survey-writing
description: >-
  Conduz, do inicio ao fim e de forma interativa, a escrita de um artigo de
  survey ou survey-tutorial academico em Computacao e Engenharia (IA/ML,
  redes, engenharia de software, sistemas, visao computacional, PLN, etc.),
  priorizando bases de relevancia reconhecida (IEEE Xplore, ACM Digital
  Library, DBLP, SBC/JBCS; arXiv so como fonte secundaria/complementar),
  conforme as diretrizes de Niyato et al. (2026,
  From Literature to Insights). Use sempre que o usuario pedir para
  escrever, planejar, estruturar ou conduzir uma survey, revisao de
  literatura ampla, artigo de revisao, tutorial academico, state-of-the-art,
  ou o capitulo de trabalhos relacionados de uma dissertacao/TCC em
  computacao ou engenharia - mesmo sem usar a palavra "survey". NAO use
  para revisoes sistematicas PRISMA/meta-analise clinico-estatistica (GRADE,
  forest plots) nem para artigos de pesquisa original (resultados
  proprios); nesses casos, avise que a skill e voltada a surveys narrativas
  e confirme com o usuario.
---

# Survey Writing (survey/tutorial acadêmico em Computação e Engenharia)

Esta skill opera como um **orquestrador de projeto**, não como um gerador de texto de uma vez só. Ela cobre os 7 pilares de Niyato, Dobre, Duong, Karagiannidis & Schober (2026) — artigo originalmente escrito para a comunidade de comunicações/redes, mas cujos princípios metodológicos (crítica de tema, taxonomia, síntese crítica, ilustrações, desafios futuros) são domain-agnostic dentro de Computação e Engenharia. Esta versão da skill generaliza esses princípios para as fontes, veículos e convenções típicas dessas áreas mais amplas (IA/ML, sistemas, redes, engenharia de software, visão computacional, PLN, engenharia elétrica/de computação), sem se prender ao vocabulário ou aos exemplos específicos de telecomunicações do artigo original. A skill cobre uma fase de configuração e uma de integração final além dos 7 pilares. Em cada fase há **pontos de decisão obrigatórios com o usuário** — a skill nunca avança sozinha em decisões que mudam o escopo, a estrutura ou o conteúdo do artigo.

## Estrutura de diretórios do projeto

Ao iniciar, confirme com o usuário o diretório-raiz do projeto (padrão: diretório de trabalho atual). Dentro dele, a skill mantém:

```
<raiz-do-projeto>/
├── research.md              # diário de pesquisa + índice de referências (ver references/08-research-log.md)
├── artigo/                  # o artigo em LaTeX
│   ├── main.tex
│   ├── sections/*.tex
│   ├── figures/
│   └── refs.bib
├── scripts/                 # scripts de análise de dados/visualização (se houver)
│   └── ...
└── literature/              # matriz de literatura + PDFs baixados para auditoria
    ├── literature_matrix.csv
    └── pdfs/                # um PDF por referência incluída, quando disponível (ver Fase 2)
        └── <id-bibtex>.pdf
```

Use `scripts/init_project.py` (nesta skill) para criar o esqueleto na primeira execução — não recrie manualmente arquivo por arquivo se o script resolver.

## Protocolo de log (research.md)

**Isto é inegociável**: toda ação importante, toda decisão (do usuário ou proposta por você), toda dúvida levantada e sua resolução devem virar uma entrada em `research.md`, na raiz do projeto — nunca dentro de `artigo/`. O formato exato está em `references/08-research-log.md`. `research.md` tem duas partes com regras diferentes:

1. **Índice de Referências** (seção fixa no topo, entre marcadores `<!-- INDICE-REFERENCIAS:START -->` / `:END`): tabela com todas as referências usadas no survey, indicando se o PDF está disponível localmente em `literature/pdfs/` ou não (e por quê). Esta seção **é atualizada em lugar**, não é append-only — ela reflete o estado atual da coleção, não um histórico. Nunca edite essa tabela manualmente linha por linha: regenere-a com `scripts/sync_reference_index.py` a partir de `literature/literature_matrix.csv`, que é a fonte de verdade.
2. **Log de Atividades** (o restante do arquivo, abaixo da seção de índice): este sim é **append-only** — nunca reescreva ou apague entradas antigas, só adicione novas.
   - Cada entrada tem data, fase, tipo (`AÇÃO` / `DECISÃO` / `DÚVIDA` / `INTERAÇÃO`) e um resumo de 1 a 4 linhas.
   - Decisões do usuário são registradas com a opção escolhida e, quando relevante, as alternativas descartadas.
   - Registre mesmo decisões pequenas (ex.: "usuário confirmou taxonomia por camada de sistema") — o valor do arquivo é reconstituir o raciocínio do projeto meses depois.

Se o arquivo `research.md` ainda não existir no início da sessão, crie-o a partir de `assets/research-md-template.md`.

## Visão geral das fases

0. Configuração inicial
1. Seleção e crítica do tema
2. Coleta e triagem da literatura
3. Organização estrutural (taxonomia)
4. Síntese crítica / redação da revisão
5. Seção de tutorial (condicional)
6. Ilustrações
7. Desafios e direções futuras
8. Integração final e auditoria de estilo

Cada fase abaixo indica: objetivo, o que fazer, e **o que obrigatoriamente perguntar ao usuário antes de prosseguir**. Leia o arquivo de referência indicado antes de executar a fase pela primeira vez em uma sessão.

---

### Fase 0 — Configuração inicial

Objetivo: alinhar parâmetros que afetam tudo depois.

Pergunte (pode agrupar em um único bloco de perguntas):
- Diretório-raiz do projeto (ou confirme o atual).
- Tema/área de partida (mesmo que ainda vago — será criticado na Fase 1).
- Venue-alvo, se já houver (ex.: ACM Computing Surveys, uma transaction/survey IEEE de qualquer subárea de computação/engenharia, periódico ou conferência brasileira como os da SBC — incluindo veículos como o JBCS —, TCC, dissertação ou tese) — isso muda idioma, classe LaTeX (IEEEtran, acmart, sbc, article genérico) e extensão esperada. Se o venue já usa um extrato Qualis/CAPES ou ranking CORE conhecido, registre isso também — ele entra como critério de qualidade na Fase 2.
- Idioma do artigo em si (frequentemente inglês para veículos IEEE, mesmo que a interação com você seja em português). Documente a decisão.
- Se o survey terá componente de tutorial (se o usuário não souber ainda, adie para a Fase 1, onde isso fica mais claro junto com o escopo).
- **Orçamento de extensão do artigo** (páginas ou palavras): confirme o limite declarado pelo venue-alvo (guidelines de autor), ou pesquise ativamente se não for conhecido. Sem essa informação, artigos tendem a crescer sem controle. Ver `references/09-controle-extensao.md` para faixas de referência e como proceder quando o venue/limite ainda não está definido.

Ação: crie a estrutura de diretórios (via `scripts/init_project.py`) e a primeira entrada em `research.md`.

Registre em `research.md` todas as respostas acima como `DECISÃO`.

---

### Fase 1 — Seleção e crítica do tema

**Esta fase é obrigatória e não pode ser pulada, mesmo que o usuário já chegue com um tema definido.** Ler `references/01-selecao-tema.md`.

Objetivo: validar que o tema é maduro o suficiente e diferenciado de surveys existentes, ANTES de qualquer coleta de literatura.

O que fazer:
1. Busque na web (ou peça ao usuário) quantas surveys recentes (últimos 2-3 anos) já existem sobre o tema proposto ou temas muito próximos.
2. Avalie e apresente ao usuário, de forma crítica (não apenas "parece bom"):
   - Maturidade do tema: há indício de que existam pelo menos ~50-120 trabalhos relevantes (limiar de Niyato)? Se claramente insuficiente, isso é um problema a discutir, não a ignorar.
   - Diferenciação: o que este survey ofereceria que os existentes não oferecem (escopo mais amplo, ângulo diferente, subtema emergente não coberto, atualização temporal)?
   - Adequação ao venue-alvo (se definido na Fase 0).
3. Apresente um veredito estruturado: **maduro e diferenciado** / **precisa de ajuste de escopo** (sugira 1-2 ajustes concretos) / **tema arriscado** (poucos trabalhos ou já coberto exaustivamente).
4. **Pare e pergunte ao usuário** qual caminho seguir. Não prossiga para a Fase 2 sem confirmação explícita do tema final (que pode ser diferente do tema inicial).

Registre em `research.md`: o tema inicial, a crítica levantada, as opções discutidas e a decisão final do usuário (tipo `DECISÃO`, com a crítica como `DÚVIDA` resolvida).

---

### Fase 2 — Coleta e triagem da literatura

Ler `references/02-coleta-literatura.md`.

Objetivo: montar uma base de referências de qualidade, sem depender de gestão manual.

O que fazer:
- Defina com o usuário (ou proponha e confirme) as **bases primárias** a usar, conforme a subárea do tema: web_search/web_fetch para IEEE Xplore, ACM Digital Library, DBLP, Google Scholar, Semantic Scholar, Scopus/Web of Science e, para temas/venues brasileiros, a Biblioteca Digital da SBC; conectores MCP acadêmicos se disponíveis (busque com `search_mcp_registry` por termos como "IEEE", "ACM", "Semantic Scholar", "Zotero" antes de assumir que não há nada conectado). Detalhes em `references/02-coleta-literatura.md`.
- **Rode consultas dirigidas a cada base primária confirmada** (ex.: `site:dl.acm.org`, `site:ieeexplore.ieee.org`, busca direta em dblp.org) — não confie numa busca genérica só, que tende a concentrar demais em arXiv.
- **arXiv é fonte secundária, não primária**: só recorra a ele depois de esgotar as bases primárias para aquele grupo temático, e apenas para (a) complementar um subtema recente sem cobertura revisada ainda, ou (b) obter a versão de acesso aberto de um item já localizado em base primária e bloqueado por paywall. Todo item com `base_busca = arxiv` como única fonte precisa de justificativa de 1 linha em `research.md`. Ver `references/02-coleta-literatura.md`, seção "Prioridade de fontes e papel do arXiv".
- Aplique os critérios de qualidade de Niyato: veículo, citações (>100 é sinal forte, mas não descarte trabalhos recentes só por baixa citação), atualidade (grosso nos últimos 5 anos + clássicos seminais mais antigos).
- Construa a matriz de literatura incrementalmente em `literature/literature_matrix.csv` (colunas sugeridas em `references/02-coleta-literatura.md`): título, autores, ano, venue, citações, subtema/cluster provisório, status de triagem, status do PDF, **base de busca de origem**.
- Gerencie citações em `artigo/refs.bib` (BibTeX), evitando duplicatas.
- **Para toda referência marcada "incluído"**, tente obter o PDF e salvá-lo em `literature/pdfs/<id-bibtex>.pdf`, para fins de auditoria local. Siga exatamente o processo (incluindo os limites de acesso a conteúdo pago) descrito em `references/02-coleta-literatura.md`, seção "Download de PDFs (auditoria)". Nunca deixe isso implícito — todo item entra na matriz com um `pdf_status` explícito (baixado / indisponível-pago / indisponível-não-encontrado / pendente).
- Ao final de cada rodada de coleta/triagem, rode `scripts/sync_reference_index.py` para regenerar a seção "Índice de Referências" de `research.md` a partir da matriz atualizada.

**Pare e pergunte ao usuário quando:**
- O volume de literatura de qualidade ficar abaixo de ~50 itens (sinal de tema imaturo — volte à Fase 1 com essa evidência) ou for excessivo a ponto de exigir recorte adicional de escopo.
- Houver ambiguidade sobre incluir ou não uma subárea limítrofe.
- Uma parcela relevante das referências ficar marcada como "indisponível-pago" — informe ao usuário quais itens ele talvez precise baixar manualmente via acesso institucional próprio, para completar a pasta de auditoria.
- **Um item com `base_busca = arxiv` sem justificativa** de 1 linha registrada — não inclua antes de tentar localizar a versão revisada em base primária.
- **Itens com `base_busca = arxiv` formarem uma parcela relevante do total `incluído`** (não apenas casos pontuais e justificados) — pare, rode buscas adicionais dirigidas às bases primárias, e só prossiga após rebalancear ou confirmar com o usuário que a composição é aceitável para aquele tema.

Registre em `research.md` (Log de Atividades) as buscas feitas (termos, bases), o total de itens coletados/triados, qualquer decisão de recorte de escopo, e a checagem de diversidade de fonte. A disponibilidade de PDF de cada item fica na seção "Índice de Referências" (regenerada pelo script, não digitada à mão).

---

### Fase 3 — Organização estrutural (taxonomia)

Ler `references/03-estrutura-taxonomias.md`.

Objetivo: escolher como a literatura será organizada — decisão estrutural que molda todo o artigo.

O que fazer:
1. Com base na matriz de literatura, proponha ao usuário 1-2 taxonomias candidatas entre os 4 padrões de Niyato (funcional, por camada de sistema, por aplicação, por framework arquitetural), com uma justificativa concreta baseada nos clusters observados nos dados coletados — não uma escolha genérica.
2. Proponha também: seções transversais pertinentes (segurança/privacidade, datasets/benchmarks, padronização/indústria), se cabe uma seção de background/preliminares, e um título para a seção principal (o corpo inteiro vira uma única `\section{}` — ver `references/03-estrutura-taxonomias.md`).
3. **Distribua o orçamento de extensão confirmado na Fase 0 entre as subseções**, proporcionalmente ao número de referências que cada eixo/transversal cobre (ver `references/09-controle-extensao.md`, seção 2) — apresente essa distribuição junto com a taxonomia, não depois.
4. **Pare e peça a confirmação do usuário sobre a taxonomia, a lista de subseções, o título da seção principal e a distribuição de extensão** antes de gerar o esqueleto do artigo — essa é a decisão estrutural mais cara de reverter depois.
5. **Depois de confirmada, atualize a coluna `subtema_provisorio` de `literature/literature_matrix.csv`** para cada referência incluída, substituindo o rótulo provisório da Fase 2 pelo nome final da subseção (eixo/transversal) confirmada — toda referência incluída precisa de um valor aqui, sem exceção.

Ação após confirmação: gere o esqueleto do LaTeX (`artigo/main.tex` a partir de `assets/template-article.tex`). O **corpo principal é um único arquivo**, `artigo/sections/03_corpo_principal.tex`, copiado de `assets/template-corpo-principal.tex`: contém uma `\section{<título confirmado>}` e, dentro dela, uma `\subsection{}` para a taxonomia adotada (com o detalhamento completo do framework, a **tabela de classificação da taxonomia** — obrigatória, mapeando todas as referências para suas subseções, ver abaixo — e, se não houver seção de Background, também a tabela comparativa com surveys relacionadas) seguida de uma `\subsection{}` por eixo principal e uma `\subsection{}` por transversal confirmada — tudo no mesmo arquivo, nunca um arquivo por subseção. Gere a tabela de classificação rodando `python3 scripts/gen_taxonomia_table.py --matrix literature/literature_matrix.csv --out artigo/figures/tabela_taxonomia.tex --ordem "<subseção 1>" "<subseção 2>" ...` (na ordem confirmada no passo 2/4) — nunca escreva essa tabela à mão (ver `references/06-ilustracoes.md`, item 2b). A **Introdução** usa um template próprio e mais restrito, `assets/template-introducao.tex` (não o genérico): sem `\subsection{}`, sem figuras/tabelas, sem aprofundar framework ou estado da arte, trabalhos relacionados só de forma superficial (ver `references/03-estrutura-taxonomias.md`, seção "Regras de conteúdo da Introdução"). As demais seções de nível superior (background, tutorial, desafios futuros, conclusão) usam o template genérico `assets/template-section.tex`. Não escreva conteúdo de revisão ainda — só a estrutura com placeholders/comentários indicando o que vai em cada subseção. Ajuste os `\input{...}` de `main.tex` conforme necessário. **Rode `pdflatex` (ou `latexmk`) sobre `artigo/main.tex` mesmo com o conteúdo ainda vazio (exceto a tabela de classificação, que já pode ser real)**, só para confirmar que o esqueleto compila antes de começar a preencher — pegar um erro de estrutura aqui é muito mais barato do que depois de todo o texto escrito.

Registre em `research.md`: taxonomia escolhida, título da seção principal, lista de subseções (eixos + transversais, na ordem), o motivo, e a confirmação de que a tabela de classificação foi gerada cobrindo todas as referências incluídas.

**A tabela de classificação nunca é gerada uma única vez.** Regenere `scripts/gen_taxonomia_table.py` sempre que, em qualquer fase posterior, ocorrer: inclusão ou exclusão de referência em `literature/literature_matrix.csv` (ex.: complementos pedidos na Fase 4 ou 7, ou um item removido na revisão), mudança na taxonomia/lista de subseções, ou mudança na atribuição (`subtema_provisorio`) de alguma referência. Trate isso como parte rotineira de qualquer uma dessas edições, não como uma tarefa à parte a lembrar depois.

---

### Fase 4 — Síntese crítica / redação da revisão

Ler `references/04-sintese-critica.md`. **Esta é a fase mais fácil de fazer mal** — o próprio artigo de Niyato aponta que o erro mais comum de pesquisadores juniores é tratar a survey como compilação em vez de síntese.

O que fazer, por grupo/subseção da taxonomia (cada eixo principal e cada transversal é um grupo, todos dentro do único arquivo `artigo/sections/03_corpo_principal.tex`):
1. Releia os itens do grupo na matriz de literatura.
2. Antes de escrever texto corrido, produza uma lista curta de **insights coletivos** do grupo (trade-offs comuns, limitações compartilhadas, progressão técnica, contradições entre autores) — não resumos artigo por artigo.
3. Depois de validados (checkpoint abaixo), **escreva a prosa final diretamente na `\subsection{}` correspondente dentro de `artigo/sections/03_corpo_principal.tex`**, substituindo o placeholder/comentário `% TODO` gerado na Fase 3 — não deixe a prosa só na conversa e não crie um arquivo novo por subseção. Respeite o orçamento de palavras alocado a essa subseção na Fase 3 (ver `references/09-controle-extensao.md`, seção 2).
4. **Agrupe citações por ideia compartilhada, não uma frase por referência**: quando vários trabalhos convergem para a mesma abordagem/achado, escreva uma única frase de síntese cobrindo-os com `\cite{a,b,c}` (3-8 chaves é o padrão esperado), em vez de uma frase dedicada a cada um. Reserve tratamento individual (frase ou parágrafo próprio) a ~2-4 trabalhos mais seminais/representativos por subseção — os demais entram em citações agrupadas e/ou na tabela comparativa (passo 6). Use `\cite{chave}`, com as mesmas chaves da coluna `id` de `literature/literature_matrix.csv` / `artigo/refs.bib`. Use linguagem de "hedging" acadêmico apropriada (evitar afirmações categóricas sem base). Ver a regra completa e o "teste de bloat" em `references/09-controle-extensao.md`, seção 3 — essa é a mesma correção que evita tanto a compilação rasa quanto o artigo inchado.
5. Antes de seguir para a próxima subseção, aplique o teste de bloat: se muitas frases têm a mesma estrutura "trabalho X faz Y \cite{x}", pare e reagrupe por ideia em vez de continuar.
6. Insira uma tabela comparativa (em LaTeX, na mesma `\subsection{}` ou em `artigo/figures/tabela_*.tex` incluído via `\input`) quando o grupo tiver >5 trabalhos com dimensões comparáveis (ver Fase 6/ilustrações) — é o destino natural para trabalhos que não recebem tratamento individual nem entram numa frase agrupada.

**Pare e mostre ao usuário os insights levantados (passo 2) antes de escrever a prosa final de cada subseção** — é mais barato corrigir a direção da síntese nesse ponto do que depois de um texto inteiro escrito.

Registre em `research.md`: por subseção, os insights validados pelo usuário, a contagem de palavras resultante frente ao orçamento alocado, e quaisquer correções de rumo pedidas.

---

### Fase 5 — Seção de tutorial (condicional)

Só execute se a Fase 0/1 confirmou que o artigo terá componente de tutorial (survey-tutorial híbrido). Ler `references/05-secao-tutorial.md`.

O que fazer:
- Para cada bloco tutorial, defina objetivos de aprendizagem explícitos antes de escrever o conteúdo.
- Estruture em progressão do básico ao avançado, com formulações matemáticas derivadas passo a passo (não só o resultado final) quando aplicável — use ambientes `equation`/`align` do LaTeX, não texto corrido para fórmulas.
- Proponha 1-2 estudos de caso por bloco, equilibrando realismo e acessibilidade.
- Depois de confirmado com o usuário (checkpoint abaixo), **escreva o conteúdo final diretamente em `artigo/sections/09_tutorial.tex`** (ou um arquivo por bloco, se forem vários), com `\cite{}` para os trabalhos de apoio, seguindo o mesmo esquema de chaves de `artigo/refs.bib`.

**Pergunte ao usuário** quais tópicos merecem tratamento tutorial completo vs. menção breve — nem todo subtema do survey precisa virar tutorial.

Registre em `research.md` os blocos de tutorial definidos e os objetivos de aprendizagem confirmados.

---

### Fase 6 — Ilustrações

Ler `references/06-ilustracoes.md`.

O que fazer:
- Para cada um dos 5 tipos de ilustração de Niyato (estrutura do survey, tabelas comparativas, figuras técnicas, resultados experimentais, lista de abreviações), avalie se cabe no seu artigo e onde.
- Se alguma ilustração exigir processamento de dados (ex.: gráfico de tendência de publicações, comparação quantitativa extraída da matriz de literatura), crie o script correspondente em `scripts/` (nunca solto em `artigo/`) e gere a figura a partir dele — não invente números.
- Salve o arquivo de imagem gerado em `artigo/figures/` e **insira de fato `\includegraphics{...}`/`\begin{table}...\end{table}` no ponto certo do `.tex`** — quando a ilustração pertence a um eixo/transversal do corpo principal, isso é dentro da `\subsection{}` correspondente em `artigo/sections/03_corpo_principal.tex` (nunca em arquivo separado); para as demais seções, no arquivo daquela seção. Sempre com `\caption`, `\label` e a chamada `Figura~\ref{...}`/`Tabela~\ref{...}` no texto próximo — não deixe a figura só gerada em disco sem estar referenciada no artigo.
- Garanta que cada figura/tabela seja referenciada e discutida no texto próximo (evite "figura solta").

**Pergunte ao usuário** antes de gerar qualquer figura que dependa de dados/levantamento que você mesmo terá que estimar (ex.: contagem de publicações por ano) — confirme a fonte dos dados.

Registre em `research.md` cada figura/tabela criada, sua fonte de dados e o script usado (se houver).

---

### Fase 7 — Desafios e direções futuras

Ler `references/07-desafios-futuros.md`.

O que fazer:
- Proponha 3-5 desafios, cobrindo (o quanto fizer sentido para o tema) as 5 categorias de Niyato: técnicos, implementação/sistema, aplicação, segurança/privacidade, padronização/indústria.
- Alinhe cada desafio a uma seção/taxonomia já existente no artigo (não introduza categorias novas do nada nesta fase).
- Depois de validado (checkpoint abaixo), **escreva o texto final em `artigo/sections/10_desafios_futuros.tex`**, com `\cite{}` para as limitações/trade-offs já discutidos na Fase 4 que motivam cada desafio.

**Pare e valide com o usuário a lista final de desafios antes de redigir o texto completo da seção.**

Registre em `research.md` a lista de desafios validada.

---

### Fase 8 — Integração final e auditoria de estilo

Ler `references/04-sintese-critica.md` (seção de auditoria) e revise o artigo completo:
- Compressão: corte redundância entre seções.
- Consistência: verifique se toda figura/tabela é citada no texto, se a taxonomia é seguida à risca, se abreviações estão na lista, e se o corpo principal continua como uma única `\section{}` com todas as subseções (taxonomia + eixos + transversais) dentro de `artigo/sections/03_corpo_principal.tex` — nenhum eixo ou transversal deve ter virado uma `\section{}`/arquivo separado ao longo da escrita.
- **Tabela de classificação da taxonomia (checagem final)**: regenere `artigo/figures/tabela_taxonomia.tex` com `scripts/gen_taxonomia_table.py` a partir da matriz atualizada — mesmo que já tenha sido regenerada durante as fases anteriores — e confirme que o total de referências na tabela bate exatamente com o total `incluído` em `literature/literature_matrix.csv`. Esta é a última chance de pegar uma referência incluída/excluída ou uma reatribuição de subseção que não tenha propagado para a tabela.
- **Introdução**: confirme que ela não ganhou `\subsection{}` nem figura/tabela/gráfico ao longo da escrita, que o framework/taxonomia aparece só como resumo de 1-2 frases (não o detalhamento, que é da subseção de taxonomia do corpo principal), que não há aprofundamento de estado da arte, e que surveys relacionadas são tratadas apenas de forma superficial (posicionamento da contribuição, sem tabela comparativa nem crítica detalhada). Corrija movendo o excesso para o Background ou para a subseção de taxonomia do corpo principal, não apagando o conteúdo.
- "Style audit gate": releia a Fase 4 — há algum trecho que ainda é resumo artigo-por-artigo em vez de síntese? Corrija antes de considerar concluído.
- **Compilação**: rode `pdflatex`/`latexmk` (duas passadas, para resolver referências cruzadas e a bibliografia via `bibtex`/`biber`) sobre `artigo/main.tex` e confirme que gera `main.pdf` sem erros — trate warnings de `\cite`/`\ref` não resolvidos como pendência a corrigir, não como algo a ignorar.
- **Auditoria de extensão** (ver `references/09-controle-extensao.md`, seção 4): confirme o número de páginas de `main.pdf` contra o orçamento definido na Fase 0. Se estourar em mais de ~15-20%, não aceite como "quase lá" — identifique as subseções acima do alocado na Fase 3 e aplique o reagrupamento de citações do passo 4 da Fase 4 antes de fechar esta fase. Sinal de alerta rápido: contagem de `\cite{}` próxima da contagem de frases do corpo principal indica tratamento individual excessivo.
- Confirme com o usuário se o artigo está pronto para submissão ou se falta mais uma rodada.

Registre em `research.md` o resultado da auditoria, se a compilação passou ou quais erros restaram, o número de páginas final frente ao orçamento, qualquer correção de extensão aplicada, e o status final da versão.

---

## Notas gerais de operação

- Nunca gere uma versão "final" de uma fase sem o checkpoint de interação indicado — isso é o que diferencia esta skill de simplesmente pedir para o modelo escrever uma survey de uma vez.
- Se o usuário pedir para pular etapas ("só me dá o artigo pronto"), avise objetivamente o risco (survey vira compilação, não síntese) e pergunte se ainda assim deseja pular — respeite a decisão final dele, mas registre o aviso e a escolha em `research.md`.
- Todo arquivo de código (scripts de coleta, dedup, geração de figura, análise, sincronização de índice) vai em `scripts/`; todo conteúdo do artigo em si vai em `artigo/`; todo PDF de referência baixado vai em `literature/pdfs/`; nada de código ou PDF solto na raiz do projeto além de `research.md`.
- Nunca tente contornar paywall/login para baixar um PDF — ver o limite ético/legal em `references/02-coleta-literatura.md`. Quando não for possível baixar, registre isso explicitamente no índice em vez de deixar a lacuna implícita.
- O orçamento de extensão confirmado na Fase 0, distribuído na Fase 3, escrito com citações agrupadas na Fase 4 e auditado na Fase 8, é um requisito rígido do projeto, não uma sugestão — ver `references/09-controle-extensao.md`. Um artigo que estoura o padrão de qualquer veículo revisado por pares geralmente indica tratamento individual de referências em vez de síntese; corrija a causa, não apenas corte texto às cegas.
- A tabela de classificação da taxonomia (`artigo/figures/tabela_taxonomia.tex`, gerada por `scripts/gen_taxonomia_table.py`) é um artefato vivo, não uma foto tirada uma vez na Fase 3: regenere-a a cada inclusão/exclusão de referência, cada revisão da taxonomia/subseções, ou cada reatribuição de referência a subseção, e confirme-a de novo na auditoria final da Fase 8 — ver `references/06-ilustracoes.md`, "Gatilhos de regeneração".
