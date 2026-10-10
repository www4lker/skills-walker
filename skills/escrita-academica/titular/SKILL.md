---
name: titular
description: "Propõe cinco opções de título para qualquer nível de um trabalho acadêmico (tese, dissertação, artigo) — do título da pesquisa ao de uma subsubseção — em dois movimentos: (1) colhe os dados que sustentam a escolha, com escopo proporcional à importância do título; (2) oferece cinco opções avaliadas contra um checklist de clareza, concisão, especificidade e fidelidade. Nunca grava título no arquivo-fonte: propõe, o autor escolhe e promove. Use quando o autor pedir título, subtítulo, nome de seção/capítulo, ou perguntar se um título existente funciona. Não use para revisar prosa (revisar-clareza) nem para formular frases do corpo do texto."
---

# Titular

## Base

As regras vêm de um relatório de orientação sobre titulação (manuais de
redação científica, normas editoriais, recomendações de periódicos). O relatório **não traz referências**; os números de extensão
abaixo são faixas de bom senso, não norma verificada. Em particular, a
afirmação "ABNT: até 7 palavras" **não foi conferida** contra a NBR 14724 ou
a NBR 6022 — `[H]` até alguém abrir a norma. Não a apresente como regra.

Princípios centrais:

- **Título não é tema.** Tema é amplo; título é a síntese do objetivo e do
  recorte do que foi efetivamente feito naquele trecho.
- **Quatro critérios:** clareza (entende-se sem ler mais nada), concisão (toda
  palavra carrega informação), especificidade (delimita objeto/recorte),
  fidelidade (descreve o que o texto faz, sem prometer mais).
- **Título secreto → título público.** Primeiro a pergunta em uma frase ("o
  que exatamente este trecho investiga/mostra?"); depois a versão editada.
- **Evitar:** generalismo, enchimento ("Um estudo sobre…", "Reflexões
  acerca de…"), siglas e jargão, ambiguidade, metáfora/ironia/trocadilho,
  título que não bate com o desenho do trabalho.
- **Título: subtítulo** — a primeira parte nomeia a ideia central; o
  subtítulo delimita recorte, população ou desenho do estudo.

## Regras da casa que valem aqui

Adapte esta lista ao seu projeto. As que seguem são as do projeto de origem,
reescritas em forma genérica:

- Esta skill **não edita o arquivo-fonte** (`.tex`, `.md`, `.docx`) — nem o
  comando de seção, nem comentário. A entrega é no chat; se o autor quiser
  registro, grava-se em `<pasta-de-processo>/titulos/AAAA-MM-DD-<slug>.md`.
- Sem terminologia não aprovada pelo autor: as opções usam o vocabulário que
  **já está no texto**. Termo novo só entra marcado como tal.
- Sem a estrutura "não é X, é Y".
- Se o projeto tem escalas ou códigos próprios (hipóteses H1–Hn, níveis N1–Nn),
  não os misture num título.
- Conceito que o autor rebaixou ou abandonou não vai para título de nível alto
  sem confirmação dele.
- "Capítulo N" é o número do documento compilado, não o do arquivo — confira
  no sumário gerado antes de localizar o trecho.
- Leia a versão vigente do texto (o ramo principal), não uma cópia defasada.

## Nível do título → escopo da coleta

Antes de tudo, classifique o título pedido. Se o autor não disser, deduza pelo
comando LaTeX (`\chapter`, `\section`, …) e declare a dedução.

| Nível | Exemplo | Extensão-alvo | O que ler no Movimento 1 |
|---|---|---|---|
| **T0** — subsubseção, parágrafo nomeado | `\subsubsection`, `\paragraph` | 2–7 palavras | o próprio trecho; o título da seção-mãe; os títulos irmãos |
| **T1** — seção / subseção | `\section`, `\subsection` | 3–10 palavras | o trecho inteiro; título do capítulo; todos os títulos irmãos; primeira e última frase de cada parágrafo |
| **T2** — capítulo | `\chapter` | 4–12 palavras | o capítulo inteiro (ou seus inícios/fins de seção, se longo); o sumário completo (`.toc`); o Resumo; o capítulo anterior e o seguinte (títulos e parágrafo de abertura) |
| **T3** — título do trabalho ou de artigo derivado | capa, submissão | 8–15 palavras (ou a norma do alvo) | Resumo e Abstract; palavras-chave; pergunta de pesquisa e objetivos (introdução); conclusões; sumário; norma do programa/periódico-alvo; títulos de trabalhos próximos (recuperabilidade) |

Nos níveis T0–T1, os critérios de indexação (palavras-chave, busca) **quase
não pesam**: quem lê um título de subseção já está dentro do documento. Ali
pesam fidelidade ao trecho e **paralelismo com os irmãos** (mesma forma
gramatical, mesmo grau de abstração). Em T2–T3 a recuperabilidade passa a
pesar, e em T3 ela é central.

## Movimento 1 — colher

Leia o que a tabela manda para o nível, e só isso. Produza, no chat, uma
ficha curta:

1. **Nível e localização** — `T_ · cap. N / arquivo.tex:linha` (título atual,
   se houver).
2. **Título secreto** — o que o trecho faz, numa frase direta, com verbo.
   Ex.: "mostra que os dois grupos não diferem na média".
3. **Recorte** — objeto, corpus/população, método ou desenho, se o trecho os
   tiver. Diga "sem recorte empírico" quando for trecho teórico.
4. **Termos âncora** — 3 a 5 termos que o **próprio texto** usa para nomear
   seu objeto (com contagem de ocorrências, via `grep -c`, quando ajudar).
   Em T3, cruze com as palavras-chave declaradas.
5. **Vizinhança** — títulos irmãos (T0–T1) ou títulos dos capítulos (T2–T3),
   para checar paralelismo e evitar repetição.
6. **Restrições** — norma do alvo (T3), limite de caracteres, termos vetados.
   Se a norma não foi verificada, diga "não verifiquei".

Em T3 — e só em T3 — vale uma busca externa por títulos de trabalhos
próximos, para calibrar vocabulário e evitar título quase idêntico a outro.
Busca paga ou que exija conta: pergunte antes.

Não gaste leitura de T3 num título de T0. A proporção é o ponto.

## Movimento 2 — cinco opções

Ofereça **exatamente cinco** títulos, ordenados do mais descritivo ao mais
interpretativo (da constatação do que o trecho faz à tese que ele sustenta).
Isso dá ao autor um eixo de escolha em vez de uma lista solta.

Para cada opção, uma linha de tabela:

| # | Título | Palavras / caracteres | Âncoras presentes | Nota |
|---|---|---|---|---|

- **Nota** = o que a opção ganha e o que perde, numa frase. Aponte qual
  critério ela sacrifica, se algum.
- Pelo menos uma opção sem subtítulo e, em T1–T3, pelo menos uma no formato
  **Título: subtítulo**.
- Nenhuma opção com metáfora, a menos que o texto já a use como conceito; se
  usar, marque o risco na nota.
- Nenhuma opção que prometa mais do que o trecho entrega. Se o título atual
  faz isso, diga.

Depois da tabela:

1. **Checklist** aplicado às cinco (✓ / ✗ por opção), com os itens do nível:
   - todos: reflete o que o trecho faz · funciona sozinho · sem sigla/jargão
     desnecessário · sem metáfora/trocadilho · sem enchimento · dentro da
     extensão-alvo;
   - T0–T1: paralelo aos irmãos · não repete o título da seção-mãe;
   - T2–T3: contém 2–3 termos âncora · subtítulo (se houver) acrescenta
     recorte, método ou população;
   - T3: dentro da norma do alvo · reconhecível numa lista bibliográfica.
2. **Recomendação** — uma opção, com a razão em uma ou duas frases ligadas ao
   checklist. É recomendação; a escolha é do autor.
3. **Título atual** (se existir) — passa ou não passa no checklist, em uma
   linha. Se passa, diga que pode ficar como está.

## Registro

Se o autor pedir para guardar, grave em
`<pasta-de-processo>/titulos/AAAA-MM-DD-<slug>.md`: a ficha do Movimento 1, a
tabela, o checklist, a recomendação e, depois, a escolha do autor marcada
`[D]`. Nunca commite; nunca altere o arquivo-fonte.
