# Fase 3 — Organização estrutural (taxonomia)

Base: Niyato et al., Seção II-C ("Structure Organization").

## Esqueleto geral de uma survey (independente da taxonomia escolhida)

1. Introdução (motivação, escopo, posicionamento **superficial** frente a surveys existentes, contribuições explícitas em bullets) — ver regras de conteúdo específicas abaixo, que restringem bastante o que pode entrar aqui.
2. Background/Preliminares (teoria básica, definições, terminologia necessária antes do corpo principal; também onde entra o aprofundamento do estado da arte e, se usada, a tabela comparativa com surveys relacionadas). Nem toda survey precisa disso — decida com base na maturidade/complexidade do tema. Quando não houver Background, esse conteúdo mais aprofundado migra para a primeira subseção do corpo principal (taxonomia adotada), nunca para a Introdução.
3. **Corpo principal — uma única `\section{}`**, cuja primeira `\subsection{}` apresenta a taxonomia adotada e cujas demais `\subsection{}` são, em sequência, os eixos principais da taxonomia e, na sequência, as seções transversais pertinentes (segurança/privacidade, datasets/benchmarks, padronização/indústria). Ver "Estrutura de subseções" abaixo — isso é diferente de versões anteriores desta skill, que tratavam eixos e transversais como `\section{}` separadas.
4. Desafios e direções futuras (seção dedicada — ver Fase 7, nunca espalhado pelo texto; permanece uma `\section{}` própria, fora do corpo principal, conforme Niyato).
5. Conclusão.

## Regras de conteúdo da Introdução

A Introdução tem um papel deliberadamente limitado nesta skill — ela situa o leitor e posiciona a contribuição, mas não faz o trabalho analítico do artigo. Use `assets/template-introducao.tex` (não o `assets/template-section.tex` genérico) para gerar `artigo/sections/01_introducao.tex`. Regras específicas:

- **Sem subseções**: a Introdução é um único bloco de prosa corrido, nunca dividida com `\subsection{}` — mesmo que o conteúdo pareça longo o suficiente para justificar divisões. Se parecer longa demais, o problema geralmente é que algo que deveria estar no Background ou no corpo principal foi deixado na Introdução — corte, não divida.
- **Sem ilustrações**: nenhuma figura, tabela, gráfico ou `\includegraphics`/`\begin{table}` aparece na Introdução. A primeira ilustração do artigo só surge a partir da segunda seção (Background, quando existir, ou a subseção de taxonomia do corpo principal, quando não existir Background).
- **Framework/taxonomia apenas resumido**: a Introdução dá, no máximo, 1-2 frases de visão geral do framework/taxonomia adotada — o suficiente para o leitor saber que existe uma organização, não como ela funciona em detalhe. O detalhamento completo (incluindo a figura de estrutura da survey) é exclusivo da primeira subseção do corpo principal.
- **Sem aprofundamento de estado da arte**: discussão mais profunda do estado da arte — o que já foi feito, comparações entre abordagens, tendências — não pertence à Introdução. Isso é papel do Background (quando existir) ou dos próprios eixos do corpo principal.
- **Trabalhos relacionados apenas para posicionar, não para comparar em profundidade**: cite as 1-3 surveys mais próximas com `\cite{}` e diga em uma frase o que esta survey acrescenta — sem tabela comparativa, sem análise crítica detalhada de cada uma. Essa comparação aprofundada (inclusive a eventual tabela comparativa com surveys relacionadas — ver `references/06-ilustracoes.md`, tipo 2) vai para o Background ou, na ausência dele, para a subseção de taxonomia do corpo principal.

Isso não é apenas estilo: mantém a Introdução curta e ágil de ler (como um leitor de periódico espera) e evita duplicar, logo no início do artigo, o conteúdo que a síntese crítica da Fase 4 vai desenvolver com profundidade mais adiante.

## Estrutura de subseções do corpo principal

O corpo principal é **uma única seção**, tipicamente chamada algo como "Panorama da Área", "Revisão da Literatura" ou um nome mais específico ao tema (defina com o usuário) — nunca "Corpo Principal" literalmente no artigo final. Dentro dela, a ordem das subseções é:

1. **Subseção 1 — Taxonomia adotada**: apresenta e justifica o critério de organização escolhido (um dos 4 padrões abaixo, ou combinação) com o detalhamento completo que a Introdução deliberadamente não tem, tipicamente acompanhada da figura de estrutura da survey (ver `references/06-ilustracoes.md`, tipo 1) — a primeira ilustração do artigo, portanto, é normal que apareça aqui. Contém também, **sempre**, a tabela de classificação da taxonomia (ver `references/06-ilustracoes.md`, item 2b): mapeia todas as referências incluídas na Fase 2 para a subseção (eixo/transversal) a que cada uma foi atribuída, seguindo a mesma hierarquia da taxonomia — gerada por `scripts/gen_taxonomia_table.py`, nunca escrita à mão. Se não houver seção de Background, é também aqui que entra a tabela comparativa com surveys relacionadas (tipo 2), já que ela não pode ficar na Introdução.
2. **Subseções seguintes — eixos principais**: uma `\subsection{}` por eixo/categoria da taxonomia escolhida, cada uma contendo a síntese crítica daquele grupo (Fase 4).
3. **Últimas subseções — transversais**: uma `\subsection{}` por seção transversal pertinente (segurança/privacidade, datasets/benchmarks, padronização/indústria), na mesma seção, no mesmo nível que os eixos principais — não como um bloco à parte.

Todo esse conteúdo (subseção da taxonomia + todos os eixos + todas as transversais) vive em **um único arquivo `.tex`** (ex.: `artigo/sections/03_corpo_principal.tex`), não um arquivo por subseção.

## Os 4 padrões de taxonomia (escolha com base nos clusters observados na matriz de literatura, não a priori)

- **Por função**: agrupa por tarefa funcional que os trabalhos desempenham (ex.: geração, classificação, otimização, predição). Boa opção quando a literatura se organiza naturalmente por "o que o método faz".
- **Por camada de sistema**: organização em camadas técnicas (ex.: física, rede, aplicação). Boa opção quando o tema atravessa uma pilha de sistema clara.
- **Por aplicação/vertical**: seções dedicadas a domínios de aplicação (ex.: 5G, mobile-edge computing, indústria). Boa opção em domínios ricos em aplicações onde o interesse do leitor é por vertical.
- **Por framework arquitetural**: propõe um framework/arquitetura conceitual logo no início e organiza a revisão de casos representativos através dessa lente. Boa opção para temas emergentes com componentes complexos que se beneficiam de uma estrutura conceitual unificadora.

## Como decidir com o usuário

1. Rode uma clusterização informal sobre `literature/literature_matrix.csv` (coluna `subtema_provisorio`) e veja qual padrão os clusters sugerem naturalmente.
2. Apresente 1-2 candidatos concretos com a lista de subseções resultante (não abstrato — mostre os nomes reais das subseções/eixos que sairiam da taxonomia aplicada aos dados coletados, já incluindo as transversais propostas na mesma lista).
3. Pergunte explicitamente qual o usuário prefere, ou se quer combinar elementos de dois padrões, e confirme o título da seção principal (o nome que sairá como `\section{}` no artigo).
4. Depois de confirmado, gere o esqueleto LaTeX (Fase 3, ação): `artigo/sections/03_corpo_principal.tex` contendo `\section{<título confirmado>}` e, dentro dele, um `\subsection{}` por item da lista (taxonomia + eixos + transversais), cada um com um comentário `% TODO: [descrição do que entra aqui]` — sem prosa ainda. Isso é um único arquivo, não um arquivo por subseção.
5. Atualize `subtema_provisorio` em `literature/literature_matrix.csv` para o nome final de cada subseção e rode `scripts/gen_taxonomia_table.py` para gerar `artigo/figures/tabela_taxonomia.tex`, incluída na subseção de taxonomia adotada — toda referência incluída deve aparecer nessa tabela.

## O que registrar em research.md

- Os padrões candidatos apresentados e por quê.
- A taxonomia escolhida e a lista final de subseções (eixos + transversais, na ordem confirmada).
- O título confirmado da seção principal.
- Seções transversais incluídas e sua justificativa.
- Confirmação de que a tabela de classificação da taxonomia foi gerada e cobre todas as referências incluídas.
