---
name: navegacao-corpus
description: "Localiza Artifacts relevantes num corpus exportado do NotebookLM para um conceito ou lacuna da pesquisa. Use antes de processar material — evita leitura desnecessária de arquivos e mapeia o que realmente existe em .md. Exige um mapa do corpus preenchido pelo pesquisador."
---

Esta skill funciona como índice do corpus NotebookLM antes de qualquer
leitura de Artifact. Evita consumo desnecessário de tokens.

FUNÇÃO:
Dado um conceito, hipótese ou lacuna da pesquisa, localizar os
Artifacts .md mais relevantes — sem abrir os arquivos.

PESQUISA EM ANDAMENTO (preencher):
Título: "<título do trabalho>"
Eixos: <ex.: (1) empírico, (2) autoetnográfico, (3) normativo>
Hipóteses: <H1–Hn, uma linha cada>
Conceitos centrais: <4–8 termos>

MAPA DO CORPUS (preencher — notebooks com .md utilizáveis, por eixo):

EIXO 1 — <NOME>:
- <nome do notebook> → <o que cobre, numa linha>

EIXO 2 — <NOME>:
- <nome do notebook> → <o que cobre>

EIXO 3 — <NOME>:
- <nome do notebook> → <o que cobre; nº de Artifacts, se souber>

PERIFÉRICO (usar com cautela):
- <notebook> → <por que é periférico>

SEM .md DISPONÍVEL (não enviar para artifacts-fichamento):
- <notebooks só com áudio ou sem Artifacts>

PROCEDIMENTO:
1. Receber conceito ou lacuna do usuário
2. Mapear 2–4 Artifacts mais relevantes por nome e notebook
3. Indicar tipo de arquivo e o que cada um provavelmente contém
4. Perguntar: "Quer que eu processe algum destes com artifacts-fichamento?"
5. Não abrir os arquivos — apenas indicar o caminho

RESTRIÇÃO: Esta skill não lê conteúdo. Apenas navega e indica.
A leitura é feita pela skill artifacts-fichamento.

MANUTENÇÃO: o mapa acima é estático. Quando notebooks forem criados,
renomeados ou descontinuados, atualize-o — um mapa defasado faz a skill
indicar com confiança o que já não existe.
