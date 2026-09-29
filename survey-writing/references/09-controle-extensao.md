# Controle de extensão e estilo de síntese

Este arquivo existe porque um teste real desta skill produziu um artigo de mais de 50 páginas — muito acima do padrão de qualquer veículo revisado por pares em Computação/Engenharia. As causas identificadas foram duas, e ambas têm correção específica abaixo: (1) nenhuma fase definia um orçamento de extensão, então o artigo crescia sem limite natural; (2) a instrução de "citar os trabalhos de apoio a cada afirmação" (Fase 4) empurrava para tratamento individual de cada referência (um parágrafo ou frase por trabalho), quando o correto em uma survey é agrupar trabalhos que compartilham uma mesma ideia sob uma única afirmação sintetizada. É lido nas Fases 0, 3, 4 e 8 — ver os apontamentos específicos em cada uma.

## 1. Definir um orçamento de extensão (Fase 0, e não depois)

Todo projeto de survey precisa de um alvo de extensão definido **antes** de começar a escrever, não descoberto no final:

- **Primeiro, verifique o limite real do venue-alvo** (confirmado na Fase 0): a maioria dos periódicos/conferências revisados por pares declara um limite explícito nas "author guidelines" — em número de páginas (formato de 1 ou 2 colunas) ou de palavras. Exemplos de referência (não regras fixas — confirme sempre a norma vigente do venue real):
  - Artigo de survey em periódico do tipo IEEE Transactions/Journal, 2 colunas: tipicamente 12-16 páginas.
  - IEEE Communications Surveys & Tutorials (o próprio venue de origem de Niyato et al.): a faixa mencionada no artigo é 20-40 páginas, mas isso é para o tipo de survey mais abrangente daquele periódico específico — não é um padrão geral a copiar para outros venues.
  - Periódicos/conferências da SBC (ex. JBCS): costumam ter limites próprios, geralmente bem mais enxutos (verifique o template/chamada específica).
  - ACM Computing Surveys: também tem diretrizes próprias de extensão, tipicamente por contagem de palavras.
  - TCC, dissertação, tese: o limite normalmente vem do regimento do programa, não de um periódico — confirme com o usuário.
- **Se o venue-alvo ainda não está definido ou o limite não é conhecido**, não assuma a faixa mais ampla (20-40 páginas) como padrão — pergunte ao usuário qual extensão ele tem em mente, ou pesquise ativamente o limite antes de seguir. Um alvo razoável e seguro na ausência de outra informação, para uma survey de revisão de literatura (não a modalidade mais extensa de tutorial-survey), é a faixa de **10.000-15.000 palavras de corpo de texto** (excluindo referências) — ajuste para baixo se o número de referências incluídas na Fase 2 for mais próximo de 50 do que de 120.
- **Registre o orçamento confirmado em `research.md`** como uma `DECISÃO` da Fase 0, e trate-o como um requisito rígido do projeto, não uma sugestão.

## 2. Distribuir o orçamento pelas subseções (Fase 3)

Depois de confirmada a taxonomia (Fase 3) e o total de referências incluídas (Fase 2), aloque o orçamento de palavras entre as partes do artigo antes de escrever qualquer prosa:

- Introdução: curta por definição nesta skill (ver `references/03-estrutura-taxonomias.md`) — tipicamente 400-700 palavras, sem exceção relevante.
- Background (quando existir): proporcional à complexidade do tema, mas não deve competir em tamanho com o corpo principal.
- Corpo principal (a `\section{}` única com todas as subseções): normalmente 55-70% do orçamento total. Divida esse valor entre as subseções (taxonomia + eixos + transversais) proporcionalmente ao número de referências que cada uma cobre — não igualmente. Uma subseção com 30 referências não deveria ter o mesmo tamanho que uma com 8.
- Desafios e direções futuras: compacta — 3-5 desafios bem articulados cabem tipicamente em 600-1000 palavras, não precisam de um parágrafo longo cada.
- Conclusão: curta, 300-500 palavras.

Apresente essa distribuição ao usuário junto com a taxonomia confirmada (mesmo checkpoint da Fase 3) para que a expectativa de extensão de cada subseção já esteja combinada antes de começar a escrever — isso evita a surpresa de um artigo estourado só na Fase 8.

## 3. Agrupar citações por ideia, não tratar cada referência individualmente (Fase 4)

Esta é a correção mais importante. Uma survey **não** é uma sequência de "o trabalho X fez Y; o trabalho Z fez W; ...". O objetivo da síntese crítica (Fase 4) é identificar o que vários trabalhos têm em comum ou como divergem, e escrever **uma frase que cubra vários deles com citações agrupadas**, reservando tratamento individual só para os poucos trabalhos que realmente merecem destaque isolado.

Regras práticas:

- **Cite em grupo sempre que a afirmação for compartilhada.** Em vez de "O trabalho A propõe X \cite{a}. O trabalho B também propõe X \cite{b}. O trabalho C estende X \cite{c}.", escreva algo como "Diversos trabalhos convergem para a abordagem X \cite{a,b,c}, com variações principalmente em [dimensão que realmente diferencia]." Uma única frase com 3-8 chaves de citação agrupadas é o padrão esperado, não a exceção.
- **Reserve tratamento individual (frase ou parágrafo dedicado) para um número pequeno de trabalhos por subseção** — tipicamente os 2-4 mais seminais, mais citados, ou mais representativos de uma virada de abordagem. Todos os demais entram em citações agrupadas dentro de frases de síntese, ou na tabela comparativa (ver `references/06-ilustracoes.md`) quando o grupo for grande (>5 trabalhos com dimensões comparáveis).
- **Regra de bolso para o número de frases por subseção**: o número de frases que tratam de literatura numa subseção não deveria crescer linearmente com o número de referências daquele grupo. Um grupo com 25 referências não deve virar 25 frases — deve virar uma síntese de poucos parágrafos (a extensão orçada no passo 2), com a maioria das referências entrando em citações agrupadas e/ou na tabela comparativa, não em prosa individual.
- **Teste de bloat**: se ao reler uma subseção você percebe muitas frases estruturalmente idênticas ("O trabalho N faz M \cite{n}."), isso é sinal de tratamento individual excessivo — pare, reagrupe por ideia compartilhada e reescreva como síntese.
- Isso não contradiz o "erro central a evitar" já descrito no restante deste arquivo (compilação vs. síntese) — é a mesma correção vista pelo ângulo da extensão: tratamento individual de cada referência é, ao mesmo tempo, o que produz um artigo raso (compilação) E um artigo inchado (extensão descontrolada). Corrigir um lado corrige o outro.

## 4. Auditoria de extensão (Fase 8)

Além da auditoria de estilo já descrita, a Fase 8 deve checar extensão explicitamente:

- Rode a compilação (já exigida na Fase 8) e verifique o número de páginas do `main.pdf` contra o orçamento confirmado na Fase 0.
- Se o artigo estourar o orçamento em mais de ~15-20%, não aceite como "quase lá" — identifique quais subseções estão acima do que foi alocado no passo 2 e aplique a correção do passo 3 (reagrupar citações, mover trabalhos individuais para citação agrupada ou para a tabela comparativa) antes de considerar a fase concluída.
- Contagem rápida de sinal de alerta: se o número de citações (`\cite{}`) no artigo for próximo ao número de frases do corpo principal, é sinal de tratamento individual excessivo — meta razoável é várias citações por frase de síntese em boa parte do texto, não uma frase por citação.
- Registre em `research.md` o número de páginas final, o orçamento confirmado, e qualquer correção de extensão aplicada.
