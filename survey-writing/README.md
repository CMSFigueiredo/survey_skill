# survey-writing

Skill para Claude Code (e outras superfícies que suportam Agent Skills) que conduz, de forma interativa e do início ao fim, a escrita de um **artigo de survey ou survey-tutorial acadêmico em Computação e Engenharia** (IA/ML, redes, engenharia de software, sistemas, visão computacional, PLN, engenharia elétrica/de computação etc.).

## O que é e para que serve

`survey-writing` não é um gerador de texto de uma vez só — é um **orquestrador de projeto de pesquisa**. Ela conduz o processo em 9 fases (configuração, crítica de tema, coleta de literatura, taxonomia, síntese crítica, tutorial opcional, ilustrações, desafios futuros e integração final), seguindo as diretrizes metodológicas de Niyato et al. (2026, *"From Literature to Insights: Methodological Guidelines for Survey Writing in Communications Research"*), generalizadas para Computação e Engenharia como um todo.

Ao longo do processo, a skill:
- **Para e pergunta ao usuário** em toda decisão que muda o escopo, a estrutura ou o conteúdo do artigo (escolha de tema, taxonomia, insights de síntese, desafios futuros) — nunca decide sozinha nesses pontos.
- Mantém um **projeto em disco**, com o artigo em LaTeX (`artigo/`), scripts de análise/visualização (`scripts/`) e a literatura coletada, incluindo PDFs baixados para auditoria (`literature/`).
- Registra **todo o histórico de decisões, dúvidas e ações** em um `research.md` na raiz do projeto, incluindo um índice sempre atualizado de quais referências têm PDF disponível localmente.
- Ao final, entrega um artigo em LaTeX com texto analítico, tabelas, figuras e bibliografia de fato escritos nos arquivos — e testa se ele compila.

## Motivação

Esta skill nasceu de uma constatação simples: existem várias skills soltas na comunidade para pedaços do processo de escrever uma survey (busca de literatura, geração de figuras, templates de seção, gestão de citações), mas nenhuma delas cobria o processo inteiro, e nenhuma seguia de perto um guia metodológico validado editorialmente. O artigo de Niyato et al. (2026) — assinado pelo Editor-Chefe da IEEE Communications Surveys & Tutorials — oferece justamente esse guia: sete pilares concretos (seleção de tema, coleta de literatura, organização estrutural, síntese crítica, tutorial, ilustrações, desafios futuros), cada um com critérios objetivos e não apenas conselhos genéricos.

Faltava, porém, unir três coisas que normalmente aparecem separadas: (1) esses critérios editoriais, (2) as partes reaproveitáveis das skills já existentes na comunidade, e (3) uma execução **interativa e auditável** — em que cada decisão importante é validada com o pesquisador e fica registrada, em vez de a IA produzir uma survey inteira de uma vez e entregar como caixa-preta. Esta skill existe para preencher essa lacuna: um processo estruturado, fiel à literatura sobre como escrever boas surveys, mas que trata o pesquisador como o responsável final por cada julgamento crítico — a skill organiza, pesquisa e escreve o texto, mas não decide por ele.

## Artefatos analisados e usados na criação (resumo)

- **Niyato, D. et al. (2026). "From Literature to Insights"** (arXiv:2509.25828) — fonte primária dos 7 pilares metodológicos que estruturam toda a skill.
- **`literature-scout`** e **`systematic-review`** (PRISMA) — inspiraram a lógica de busca multi-base, deduplicação e filtro de qualidade da Fase 2 (adaptada de meta-análise clínica para síntese narrativa).
- **`survey-writer`** e **`paper-writing-skill`** (SNL-UCSB) — inspiraram os templates de seção, tabelas comparativas e o pipeline de escrita/integração/auditoria de estilo (Fases 3, 4 e 8).
- **`figure-generation`/`data-visualization`** e **`citation-management`** — inspiraram a geração rastreável de figuras via script (Fase 6) e a gestão de referências em BibTeX (Fase 2).
- **`learning-pedagogy`/`curriculum-design`** — buscados à parte para cobrir um gap do levantamento inicial: nenhuma skill tratava da escrita pedagógica de seções de tutorial (Fase 5).

Mapeamento completo, incluindo o que foi deixado de fora de cada fonte, em `references/00-proveniencia.md` dentro da própria skill.

## Como instalar no Claude Code

Uma skill do Claude Code é apenas uma pasta com um `SKILL.md` dentro. Para instalar `survey-writing`:

1. Baixe e extraia `survey-writing.skill` (é um arquivo zip) — isso gera uma pasta `survey-writing/`.
2. Copie essa pasta para o diretório de skills do Claude Code:

   **Instalação pessoal (disponível em todos os projetos):**
   ```bash
   mkdir -p ~/.claude/skills
   cp -r survey-writing ~/.claude/skills/
   ```

   **Instalação apenas neste projeto** (para versionar com o time, por exemplo):
   ```bash
   mkdir -p .claude/skills
   cp -r survey-writing .claude/skills/
   ```
3. Inicie uma nova sessão do Claude Code (ou reinicie a sessão atual) — a skill é carregada automaticamente. Digite `/` para conferir se `survey-writing` aparece na lista de skills disponíveis.

Não é necessário nenhum passo extra de configuração (não há chaves de API nem dependências externas obrigatórias) — os únicos requisitos de ambiente são Python 3 (para os scripts em `scripts/`) e uma distribuição LaTeX com `pdflatex`/`latexmk` (para compilar o artigo gerado).

## Como usar

Basta pedir, na sua própria sessão do Claude Code, para escrever/planejar/conduzir uma survey — não precisa nem citar a skill pelo nome. Alguns exemplos que acionam a skill automaticamente:

- "Quero escrever uma survey sobre [tema]."
- "Me ajuda a revisar a literatura sobre [tema] e produzir um artigo."
- "Preciso escrever o capítulo de trabalhos relacionados da minha dissertação sobre [tema]."

A partir daí, a skill conduz você pelas 9 fases, uma de cada vez, parando para confirmar decisões importantes (diretório do projeto, crítica do tema, taxonomia, insights de cada seção, desafios finais etc.). Você pode interromper e retomar em outra sessão sem perder contexto: a skill lê `research.md` no início de cada retomada antes de perguntar de novo algo que já foi decidido.

Ao final, o projeto fica assim:

```
<seu-projeto>/
├── research.md              # histórico de decisões + índice de referências
├── artigo/                  # o survey em LaTeX (main.tex, sections/, figures/, refs.bib)
├── scripts/                 # scripts de coleta/análise/geração de figuras
└── literature/              # matriz de literatura + literature/pdfs/ (PDFs para auditoria)
```

Se quiser pular alguma etapa ("só me dá o artigo pronto"), a skill avisa o risco antes de aceitar — mas respeita a decisão final.

## Disclaimer

### Sobre a regulamentação brasileira de uso de IA na pesquisa

O Brasil passou a ter, desde março de 2026, uma norma federal específica sobre o uso de IA generativa em atividades científicas: a **Portaria CNPq nº 2.664/2026** (6 de março de 2026), que institui a Política de Integridade na Atividade Científica do CNPq. Ela se aplica a bolsistas, proponentes, servidores e membros de comitês de assessoramento vinculados ao CNPq, e seus pontos mais relevantes para quem usa esta skill são:

- **Declaração obrigatória do uso**: é preciso declarar explicitamente, no próprio texto ou em exposição eletrônica associada, qual ferramenta de IA generativa foi usada, em qual fase da pesquisa (concepção, redação, análise de dados, submissão) e com qual finalidade — em qualquer etapa em que ela tenha sido empregada, não só na redação final.
- **Vedação de autoria à IA**: uma ferramenta de IA não pode figurar como autora ou coautora do trabalho, nem seu conteúdo pode ser submetido como se fosse de autoria humana sem a devida declaração.
- **Responsabilidade integral do pesquisador**: cabe exclusivamente ao pesquisador humano validar, verificar e responder por tudo que é produzido com apoio de IA — hipóteses, escopo, interpretações e conclusões continuam sendo decisões e responsabilidades dele, não da ferramenta.
- **Transparência metodológica**: o uso de IA deve ser rastreável e auditável, não ocultado no processo de pesquisa.
- **Sanções previstas**: o descumprimento pode resultar em advertência, suspensão ou cancelamento de bolsas/auxílios e devolução de recursos, em casos de irregularidade comprovada.

Este resumo é informativo e não substitui a leitura do texto integral da Portaria nº 2.664/2026 (Diário Oficial da União, 6 de março de 2026) nem a política específica do seu programa de pós-graduação, periódico ou agência de fomento — cada veículo/instituição pode ter exigências adicionais ou mais restritivas sobre declaração de uso de IA.

### Sobre o propósito desta skill

Esta skill foi desenhada precisamente com esse pano de fundo regulatório em mente — daí o formato interativo e o registro obrigatório de todo o processo em `research.md`, que existe também para facilitar a declaração de uso exigida pela Portaria. Ainda assim, é importante deixar explícito:

**O objetivo desta skill não é produzir um survey pronto para publicação.** O resultado gerado deve ser entendido como:
- material de **início de estudo** sobre um tema, útil para se situar rapidamente na literatura;
- apoio ao **aprendizado pessoal** do pesquisador sobre uma área ainda não dominada;
- um **esboço estrutural** de uma área de pesquisa (taxonomia, panorama de trabalhos, lacunas aparentes) — um ponto de partida, não um ponto de chegada.

Para avançar desse esboço a um artigo submetível com rigor, é indispensável a **intervenção humana responsável** em pelo menos estas frentes, que nenhuma automação substitui:
- verificação direta de cada afirmação e citação contra a fonte original (a skill localiza e organiza a literatura, mas não garante que toda leitura crítica esteja livre de erro ou viés de interpretação);
- validação metodológica e teórica por quem domina a subárea, incluindo orientador(es) e revisores;
- julgamento editorial sobre completude, relevância e originalidade da contribuição, que é do pesquisador, não da IA;
- a declaração de uso de IA exigida pela Portaria CNPq nº 2.664/2026 (e por políticas equivalentes de outras agências/periódicos), preenchida pelo próprio pesquisador com base no que de fato foi feito nesta sessão.

Em resumo: use esta skill para ganhar velocidade na fase de levantamento e organização — não para pular a etapa em que o pesquisador humano lê, critica e assume a responsabilidade pelo que está escrito.

