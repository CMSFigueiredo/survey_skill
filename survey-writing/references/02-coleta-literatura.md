# Fase 2 — Coleta e triagem da literatura

Base: Niyato et al., Seção II-B ("Literature Collection").

## Bases a considerar

**Preferência explícita por bases de relevância reconhecida.** A espinha dorsal da survey vem de periódicos/conferências revisados por pares em bases de relevância consolidada; arXiv não é base primária de busca (detalhes de como isso se aplica na prática, na seção "Prioridade de fontes e papel do arXiv" abaixo).

Escolha as bases primárias conforme a subárea do tema (nem toda survey de Computação/Engenharia precisa das mesmas fontes que uma survey de redes) — proponha um subconjunto ao usuário na Fase 2, não use todas por padrão:

**Bases primárias (buscar aqui primeiro, sempre):**
- **IEEE Xplore** — cobre não só comunicações/redes, mas também computação, engenharia elétrica, engenharia biomédica, etc. Base forte por padrão para qualquer subárea de Engenharia/Computação. Acesse via web_search/web_fetch (resultados que apontem para ieeexplore.ieee.org) ou, se houver um conector MCP acadêmico disponível (verifique com `search_mcp_registry` por termos como "IEEE", "academic", "scholar", "zotero" antes de assumir que não há nada), prefira o conector.
- **ACM Digital Library** — base primária para Ciência da Computação em sentido amplo (IA/ML, IHC, engenharia de software, sistemas, segurança, banco de dados), especialmente relevante quando o tema não é de comunicações/redes.
- **DBLP** — bom para mapear rapidamente o histórico de publicações de uma subárea de Computação (conferências e periódicos indexados), útil na Fase 1 para estimar volume/maturidade do tema.
- **Google Scholar** — cobertura ampla (IEEE, ACM, Springer, Elsevier, dissertações, relatórios técnicos), útil para não perder trabalhos relevantes fora das bases específicas de editora. Ao usá-lo, priorize os resultados que apontam para o registro do periódico/conferência de origem, não para cópias soltas em preprint.
- **Semantic Scholar** — bom para contagem de citações e grafos de citação quando precisar avaliar impacto, com boa cobertura de IA/ML; use o registro de venue que ele associa ao trabalho (não o link de preprint, quando houver os dois).
- **Scopus / Web of Science** — quando disponíveis (o usuário pode ter acesso institucional), são referência para indicadores de citação e para checar o extrato Qualis/CAPES de periódicos, relevante em contexto de pós-graduação brasileira.
- **Biblioteca Digital da SBC** — quando o tema/venue-alvo for brasileiro (ex.: conferências e periódicos como os organizados pela SBC, incluindo o JBCS), é a fonte mais direta para mapear a produção nacional na subárea.

**Fonte secundária/complementar (não usar como busca principal):**
- **arXiv** (seções cs.\*, eess.\*, stat.ML etc.) — use apenas para: (a) complementar um subtema muito recente onde a busca nas bases primárias voltou vazia ou claramente insuficiente, ou (b) localizar uma versão de acesso aberto de um trabalho que já foi encontrado em base primária e está atrás de paywall (ver seção de download de PDFs). Nunca use arXiv como ponto de partida da busca de um grupo temático. Todo item cuja única fonte seja arXiv precisa de justificativa explícita registrada em `research.md` (ver "Prioridade de fontes" abaixo), e sempre sinalize no texto final que se trata de preprint não revisado por pares.

**Fontes complementares por subárea** (apoio, não espinha dorsal): repositórios de código e datasets (ex.: Papers with Code, para IA/ML), documentos de padronização (3GPP, IETF, ITU — quando o tema for redes/telecom), white papers de indústria e notícias técnicas — úteis para seções transversais (padronização/indústria).

## Prioridade de fontes e papel do arXiv

Uma busca genérica (`web_search`/`web_search_fast` com um termo solto) tende a devolver desproporcionalmente resultados do arXiv para temas de IA/Computação — é a base mais indexada, com PDFs abertos e metadados limpos, então motores de busca a privilegiam. Sem uma regra explícita, o "corpo principal" da survey acaba majoritariamente composto por preprints não revisados por pares, o que contraria o próprio critério de qualidade de veículo de Niyato (Seção II-B) e enfraquece a survey perante revisores. Por isso a regra aqui é mais forte do que apenas "evitar excesso": **arXiv é fonte secundária por padrão**, não uma entre outras.

Como conduzir a busca na prática:

1. **Busque primeiro e principalmente nas bases primárias**, com consultas **dirigidas** a cada uma (não uma busca livre que por acaso as retorne). Exemplos de como direcionar via `web_search`/`web_search_fast`/`web_fetch`:
   - IEEE Xplore: inclua `site:ieeexplore.ieee.org` na query, ou busque diretamente a partir do portal de busca do IEEE Xplore.
   - ACM Digital Library: `site:dl.acm.org`.
   - DBLP: busque diretamente em `dblp.org` (ótimo para levantar rapidamente veículos/anos de uma subárea).
   - Google Scholar / Semantic Scholar: usar os termos do tema diretamente nesses serviços, priorizando o registro de venue revisado quando o mesmo trabalho aparecer também como preprint.
   - Se houver conector MCP acadêmico disponível, prefira-o à busca livre — ele tende a consultar a base certa diretamente, sem o viés de indexação do buscador geral.
2. **Só recorra ao arXiv depois de esgotar as bases primárias para aquele subtema/grupo**, e apenas para: (a) preencher uma lacuna real (subtema recente sem cobertura revisada ainda) ou (b) obter a versão de acesso aberto de um item já localizado em base primária e bloqueado por paywall — nesse segundo caso o `venue`/`base_busca` do item continua sendo a base primária onde foi encontrado, o arXiv entra só como `pdf_fonte_url` (ver "Download de PDFs" abaixo).
3. **Registre a `base_busca` de cada item na matriz** — não deixe essa coluna em branco. É o que permite auditar a composição final por fonte.
4. **Todo item cuja única fonte seja arXiv** (não existe versão revisada localizável) precisa de uma justificativa de 1 linha registrada em `research.md` — normalmente "subtema emergente, ainda sem publicação em veículo revisado". Sem essa justificativa, o item não deveria entrar como `incluído`.
5. **Antes de fechar a Fase 2, confira a composição final**: itens com `base_busca = arxiv` devem ser claramente minoritários e cada um deve ter a justificativa do item 4. Se isso não se sustentar, volte e busque mais nas bases primárias antes de seguir para a Fase 3. Registre essa checagem em `research.md` mesmo quando o resultado já estiver adequado.

## Critérios de qualidade (aplicar a cada item antes de incluir na matriz)

- **Veículo**: priorize periódicos/transações de editoras reconhecidas (IEEE, ACM, Elsevier, Springer) e conferências de primeira linha da subárea — o que conta como "primeira linha" varia por subárea (ex.: ranking CORE para conferências, extrato Qualis/CAPES para o contexto brasileiro, quando aplicável). Trabalhos em veículos de qualidade duvidosa entram só se houver justificativa clara (ex.: única fonte disponível sobre um subtema emergente).
- **Impacto de citação**: >100 citações é um sinal forte de relevância estabelecida, mas isso penaliza automaticamente trabalhos recentes — não descarte um artigo de 1-2 anos só por baixa contagem de citações; combine com veículo e relevância temática. Normas de citação variam bastante entre subáreas de Computação (IA/ML tende a citar muito mais rápido que, por exemplo, engenharia de software formal) — calibre a expectativa numérica à subárea real, não aplique 100 citações como regra rígida universal.
- **Atualidade**: o núcleo da survey (a maioria das referências) deve vir dos últimos 5 anos — em subáreas de ritmo muito acelerado (ex.: LLMs/IA generativa) pode fazer sentido restringir ainda mais o núcleo aos últimos 2-3 anos, a combinar com o usuário. Trabalhos seminais mais antigos que estabeleceram conceitos fundamentais devem ser incluídos seletivamente, não por padrão.

## Estrutura sugerida de `literature/literature_matrix.csv`

| Coluna | Descrição |
|---|---|
| `id` | chave BibTeX correspondente em `artigo/refs.bib` e nome do arquivo em `literature/pdfs/<id>.pdf` |
| `titulo` | título do trabalho |
| `autores` | autores (formato "Sobrenome, N.; Sobrenome2, N2.") |
| `ano` | ano de publicação |
| `venue` | periódico/conferência/preprint |
| `citacoes` | contagem de citações no momento da coleta (registre a data da consulta em `research.md`, pois esse número muda) |
| `subtema_provisorio` | cluster temático inicial (será refinado na Fase 3) |
| `status_triagem` | incluído / excluído / dúvida |
| `motivo_exclusao` | preenchido só se `status_triagem = excluído` |
| `pdf_status` | `baixado` / `indisponivel_pago` / `indisponivel_nao_encontrado` / `nao_aplicavel` (itens excluídos não precisam de PDF) / `pendente` |
| `pdf_fonte_url` | URL de onde o PDF foi obtido (ou de onde a tentativa foi feita) |
| `pdf_data` | data em que o download foi tentado/realizado |
| `base_busca` | base primária onde o item foi originalmente localizado (ex.: `ieee_xplore`, `acm_dl`, `dblp`, `google_scholar`, `semantic_scholar`, `scopus`, `wos`, `sbc`); só use `arxiv` quando não houver versão revisada localizável, com justificativa registrada (ver "Prioridade de fontes e papel do arXiv" abaixo) |

## Download de PDFs (auditoria)

Objetivo: para toda referência marcada `incluído`, deixar uma cópia local em `literature/pdfs/<id>.pdf`, para que o usuário possa auditar depois exatamente o que foi lido/citado.

### Como baixar (restrição técnica do ambiente)

O `bash_tool` (execução de código) só tem rede liberada para um conjunto fixo de domínios de pacotes (pypi, npm, github etc.) — **não** inclui arxiv.org, ieeexplore.ieee.org, dl.acm.org e afins. Portanto, `curl`/`wget` dentro do container **não funcionam** para isso. Use este processo:

1. Chame `web_fetch` na URL do PDF (ex.: a versão `/pdf/` de um preprint arXiv, um link de PDF de acesso aberto, a página do DOI se ela redirecionar para um PDF acessível), com `web_fetch_pdf_extract_text: false` para receber os bytes brutos em vez de texto extraído.
2. Se o retorno for conteúdo binário de PDF, decodifique e grave em `literature/pdfs/<id>.pdf` (via `bash_tool`/`create_file`, decodificando base64 conforme o formato retornado pela ferramenta).
3. Se o `web_fetch` retornar uma página HTML (não o PDF em si — comum em páginas de editoras com paywall), **não** tente contornar login/paywall. Marque o item como `indisponivel_pago` e registre a URL consultada.
4. Se a URL não existir/quebrar ou nenhuma versão de acesso aberto for localizada após uma busca razoável, marque como `indisponivel_nao_encontrado`.

### Onde procurar a versão de acesso aberto, antes de desistir

Isto é justamente um dos dois usos legítimos do arXiv nesta skill (o outro é complementar subtemas sem cobertura revisada — ver "Prioridade de fontes" acima): quando um item já está na matriz com origem em base primária (`base_busca` = IEEE Xplore, ACM DL etc.) mas o PDF está atrás de paywall, procure a versão aberta antes de marcar `indisponivel_pago`:

- Preprint correspondente em arXiv (link `/abs/` → troque por `/pdf/`) — aqui o `venue`/`base_busca` do item continua sendo a base primária original; o arXiv entra só em `pdf_fonte_url`.
- Página pessoal do autor / página do grupo de pesquisa (muitas vezes hospedam o PDF final ou uma pre-print equivalente).
- Repositórios institucionais (ex.: repositório da universidade do autor).
- Versão "open access" indicada pela própria editora (IEEE Open Access, ACM Open, artigos com licença CC).

### Limite ético/legal — não contornar

**Nunca** tente baixar de forma automatizada conteúdo claramente pago/protegido por login institucional (ex.: PDF completo direto de ieeexplore.ieee.org ou dl.acm.org sem acesso aberto explícito) — isso não é uma limitação técnica, é uma linha que a skill não deve cruzar. Quando isso acontecer, apenas registre o item como `indisponivel_pago` com a URL da página do artigo, para que o próprio usuário baixe manualmente pelo seu acesso institucional (biblioteca da sua universidade, portal de periódicos ao qual tenha assinatura, etc.) e coloque o arquivo em `literature/pdfs/<id>.pdf` se quiser completar a pasta de auditoria — a skill não deve prometer isso por ele.

## Deduplicação e gestão de referências

- Antes de adicionar um item novo à matriz, verifique duplicatas por título normalizado + primeiro autor + ano (não confie só no DOI, pois nem toda fonte fornece um).
- Mantenha `artigo/refs.bib` sincronizado com a matriz — toda linha "incluído" na matriz deve ter uma entrada BibTeX correspondente, com a mesma chave (`id`).

## Pontos de parada obrigatórios

- Volume de itens "incluído" < ~50 após uma rodada razoável de busca → pare e volte à Fase 1 com essa evidência concreta (pode indicar que a crítica inicial de maturidade estava otimista demais).
- Volume muito acima de 120-150 → pare e proponha ao usuário um recorte adicional de escopo (por subtema, por período, por camada) antes de continuar a triagem.
- Item limítrofe (dentro ou fora do escopo?) → não decida sozinho; liste as dúvidas acumuladas e resolva em bloco com o usuário, não uma pergunta por item (isso quebraria o fluxo).
- **Qualquer item com `base_busca = arxiv` sem a justificativa de 1 linha exigida** (subtema emergente sem versão revisada) → não inclua ainda; primeiro tente localizar a versão revisada em base primária, e só marque `incluído` com essa origem se a busca adicional confirmar que não existe.
- **Itens com `base_busca = arxiv` formando uma parcela relevante do total `incluído`** (não apenas casos pontuais e justificados) → pare, rode buscas adicionais dirigidas às bases primárias ainda não exploradas a fundo, e só prossiga depois de rebalancear ou de confirmar com o usuário que a composição é aceitável para aquele tema específico.

## O que registrar em research.md

No **Log de Atividades**:
- Termos de busca usados por base, e data da busca.
- Total de itens encontrados vs. incluídos após triagem, por rodada.
- Qualquer decisão de recorte de escopo motivada pelo volume de literatura.
- Itens limítrofes e a decisão tomada sobre cada um (em bloco).
- Sempre que uma parcela relevante de itens ficar `indisponivel_pago`, uma nota avisando o usuário.
- A checagem de composição por fonte (quantos itens têm `base_busca = arxiv`, e a justificativa de cada um), mesmo quando o resultado for "sem problema".

Na seção **Índice de Referências** (gerada por `scripts/sync_reference_index.py`, nunca editada à mão): todo item `incluído`, com seu `pdf_status` e, quando baixado, o caminho em `literature/pdfs/`.
