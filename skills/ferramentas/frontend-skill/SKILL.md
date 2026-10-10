---
name: frontend-skill
description: Constrói páginas HTML de página única (SPA) para apresentar informação — sínteses de pesquisa, páginas de referência consultável e pequenas ferramentas utilitárias. Use sempre que o pedido envolver resumir ou apresentar material pesquisado numa página, criar uma referência rápida (cheatsheet, tabela, glossário, índice navegável) ou automatizar uma tarefa repetitiva de pesquisa numa interface de página única — mesmo que as palavras "página" ou "site" não apareçam. Acione também para "monta uma página com isso", "faz um resumo visual disso", "transforma essa pesquisa em algo navegável", "preciso de uma ferramentinha para X". NÃO é para dashboards de produto nem sites institucionais; o objeto é sempre apresentar ou operar sobre conhecimento, não vender.
---

# Páginas para apresentar conhecimento

Esta skill constrói páginas de página única, em arquivo único, para um propósito específico: **apresentar ou operar sobre informação**. Não é uma skill de "frontend bonito" genérico. O gênero governa tudo — clareza, hierarquia e velocidade de acesso valem mais que espetáculo visual.

## Os três gêneros

Identifique qual está sendo pedido antes de qualquer outra decisão. Eles têm objetivos diferentes e, às vezes, incompatíveis.

1. **Síntese de pesquisa.** Material extenso foi reunido; a página destila o que importa. O leitor precisa pegar a tese central em segundos e poder descer ao detalhe quando quiser. A página é um *argumento*, não uma vitrine. Modelo mental: ensaio visual, página de jornalismo de dados, verbete denso.
2. **Referência consultável.** A página existe para ser acessada rápido e de novo: cheatsheet, tabela, glossário, índice. Aqui a velocidade de consulta *é* a estética. Modelo mental: cartão de cola, manual técnico, tabela periódica.
3. **Ferramenta utilitária.** Uma SPA que automatiza ou agiliza uma tarefa repetitiva. A interface deve desaparecer atrás da função. Modelo mental: utilitário Unix, bookmarklet, calculadora de página única.

## O princípio central: slop é a média

O visual genérico de IA não é feio — é **médio**. É o centro da distribuição: o previsível, o sem-referente. Por isso listas de proibição não resolvem. "Nunca use Inter" só empurra todo mundo para a próxima fonte da moda; a skill anterior teve que banir nominalmente Space Grotesk porque a regra "use fontes características" colapsou numa única fonte característica. Trocar um item da lista de banidos por ano é correr atrás da própria sombra.

O antídoto não é uma lista melhor de escolhas de bom gosto. É **especificidade ancorada num referente concreto e externo**. O *tell* do slop é a ausência de referente — a página não vem de lugar nenhum, então aterrissa na média. Uma página que parte de um objeto específico (um sistema de sinalização, um manual, uma publicação, um movimento tipográfico) diverge naturalmente, porque o ponto de partida não é o centro.

Isto é o coração da skill. Tudo abaixo serve a este princípio.

## Procedimento: ancore antes de estilizar

Antes de escolher fonte, cor ou layout, execute este passo — e torne-o visível para o usuário em uma linha.

1. **Nomeie um referente.** Escolha um ponto de partida concreto e nomeável — não um adjetivo ("editorial", "refinado", "moderno", que convergem), mas um objeto: ver `references/repertorio.md`. A escolha deve ser **motivada pelo assunto da página**, não pelo seu gosto. Uma síntese sobre infraestrutura urbana puxa para sistemas de sinalização; um glossário técnico puxa para manuais; um ensaio sobre um tema sombrio puxa para outro lugar.
2. **Derive dele.** Tire da referência decisões concretas: a paleta, a relação tipográfica, a grade, a densidade, o tratamento de hierarquia. Não decore com ela — *derive*.
3. **Deforme pelo conteúdo.** A referência é ponto de partida, não fôrma. Deixe o material específico desta página puxar a derivação para fora do óbvio. Duas páginas que partem do mesmo referente, com conteúdos diferentes, devem chegar a lugares diferentes.

Esse passo é o que produz divergência real entre páginas — em vez de orbitarem todas o mesmo "editorial de IA".

## O viés desta skill: clareza acima de espetáculo

Para apresentar conhecimento, redução vence acúmulo. Isto **não** é timidez de design — é onde mora a sofisticação do gênero.

- A "coisa memorável" de uma página vem de uma **decisão** e de uma **hierarquia limpa**, não de uma profusão de efeitos. Uma única escolha forte (uma grade incomum mas justificada, um tratamento tipográfico decidido, uma cor) supera dez micro-animações.
- A coragem é **editorial**: cortar o que não é essencial, comprometer-se com uma ordem de leitura, deixar respirar. Espaço em branco é estrutura, não desperdício.
- Animação serve à compreensão (revelar relação, orientar o olhar, dar feedback) — nunca à decoração. Se uma animação atrasa o acesso à informação, ela está trabalhando contra o gênero. Numa página de referência, anime quase nada.
- Desconfie de qualquer efeito que você adicionaria "porque fica bonito". Se não serve à leitura, à consulta ou à função, corte.

## Princípios por gênero

### Síntese de pesquisa
- O leitor pega a tese em ~10 segundos no topo, e *então* pode descer. Estruture do geral ao específico.
- Hierarquia tipográfica clara faz o trabalho pesado: tamanho, peso e espaço marcam os níveis do argumento. Tipografia confortável para leitura longa (medida de ~60–75 caracteres por linha, entrelinha generosa).
- Princípios de Tufte quando houver dados: maximize a razão dado-tinta, prefira *small multiples* a um gráfico ornamentado, integre número e texto. Sem "chartjunk".
- A página é um argumento. Cada seção deve avançar uma ideia, não só preencher.

### Referência consultável
- A estética é a velocidade de consulta. O usuário escaneia, encontra, sai. Otimize para isso.
- Densidade legível é virtude, não defeito: tabelas compactas, listas escaneáveis, âncoras e índice. Funcione com Ctrl-F.
- Zero fricção: nada que atrase o acesso. Animações de entrada são um estorvo aqui.
- Considere busca/filtro client-side quando a referência for grande.

### Ferramenta utilitária
- A interface some atrás da função. O caminho principal deve ser óbvio sem instrução.
- Estado claro e feedback imediato: o usuário sempre sabe o que aconteceu e o que fazer.
- Robustez antes de adorno: trate entrada vazia, erro, caso-limite. Uma ferramenta que quebra silenciosamente é pior que feia.

## Execução

- **Arquivo único, portátil, autossuficiente.** Tudo (HTML/CSS/JS) num só arquivo, sem etapa de build, funcionando ao abrir localmente. Estas páginas são colecionáveis e vão para um portfólio — portabilidade é requisito, não conveniência. Use CDNs só quando indispensável; prefira nada.
- **Acessibilidade é parte da clareza**, não um extra: HTML semântico, contraste real, foco visível, navegação por teclado, `prefers-reduced-motion` respeitado. Uma página de informação inacessível falhou no próprio objetivo.
- **Tipografia primeiro.** É 80% do resultado neste gênero. Escala tipográfica deliberada, fluida com `clamp()` quando fizer sentido, mas sob controle. Uma boa relação display/corpo derivada do referente vale mais que qualquer efeito.
- **Cor com economia.** Uma cor dominante, um acento, derivados do referente. Use `prefers-color-scheme` quando servir à leitura. Variáveis CSS para coerência.
- **Performance** porque a página deve abrir instantânea: sem peso desnecessário, sem dependências gordas para um efeito.

## O repertório

`references/repertorio.md` é um catálogo curado de pontos de partida concretos, com viés deliberado para a tradição da clareza. **Leia-o no passo de ancoragem**, ao escolher o referente. Use-o como semente: a melhor referência para uma página específica pode estar fora dele — o repertório ensina o *tipo* de objeto a procurar, não fecha a lista. O usuário deve fazê-lo crescer com o tempo.
