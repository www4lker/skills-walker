---
name: testar-arbitragem-clareza
description: "Verifica adversarialmente as arbitragens [H] produzidas por revisar-clareza. Lê um relatório de revisão e o arquivo-fonte correspondente, filtra os pontos arbitrados sob hipótese (Tensões 1, 2, 3 com marca [H]) ou deixados em 'quando não resolve', e produz um dossiê dialético — dois lados nomeados, o que está em jogo, concordância com a skill — em <pasta-de-processo>/revisoes-clareza/<arquivo>.adversarial.md. Nunca edita o arquivo-fonte, nunca substitui revisar-clareza, nunca arbitra. Use quando o autor quiser ver o debate por trás de uma arbitragem, ou — enquanto a Tensão 3 estiver em teste — sempre que uma revisão de clareza tiver aplicado [H]. Não use para revisar clareza (revisar-clareza) nem para auditar \\cite existente (auditar-citacoes)."
---

# Testar Arbitragem Clareza

## Por que esta skill existe

`revisar-clareza` comprime cada tensão em uma linha: "Tensão 1, favorece Pinker
porque o agente é actante técnico". A decisão é auditável; a **contestação** não
é visível. Isso está correto para arbitragens sustentadas por fonte clara.

Mas três arbitragens daquela skill são marcadas `[H]` — hipóteses do autor em
teste, sem fonte que as sustente. A Tensão 3 está explicitamente "em teste", e a
própria skill diz: *"registrar no relatório com a marca `[H]` e o eixo
identificado, para que o autor possa julgar se o critério se sustenta na prática
antes de virar política."*

O relatório de `revisar-clareza` **não permite esse julgamento**. Uma linha
"Tensão 3, favorece Viscardi porque eixo autoetnográfico" não mostra a força do
lado Marconi nem o que muda no texto se o lado oposto vencer.

Esta skill produz esse debate. Só ele.

## Antes de agir

1. Ler os arquivos de contrato e de estado do projeto, se existirem (ex.:
   `AGENTS.md`, `CLAUDE.md`, arquivo de estado datado).
2. Ler o arquivo de guardrails do projeto inteiro — os guardrails valem aqui
   como valem em `revisar-clareza`. Em especial: **número de capítulo é o
   número do documento compilado, não o número contido no nome do arquivo**.
3. Identificar o alvo. O autor invoca em linguagem natural — "testa o capítulo 4",
   "testa essa seção", "testa o que a revisar-clareza marcou ontem". A skill não
   exige granularidade: trabalha sobre os itens que o relatório de origem
   efetivamente contém. Se houver mais de um relatório candidato no diretório
   `<pasta-de-processo>/revisoes-clareza/`, perguntar qual antes de agir — não
   escolher pelo mais recente.
4. Falar sempre pelo número do documento compilado, nomeando o arquivo entre
   parênteses: "capítulo 7 (`cap4-<tema>.tex`)". Confundir os dois é erro
   fácil quando a numeração dos arquivos não acompanha a do documento.
5. Se houver registro de sessão recente tratando do mesmo capítulo, ler antes.
   Pode conter decisão do autor sobre uma das `[H]` que muda o dossiê.

## O que é um ponto contestável

Um item do relatório de `revisar-clareza` entra no dossiê adversarial **se, e só
se**, satisfaz um destes critérios:

- aplica uma arbitragem de tensão com a marca `[H]` (Tensão 1, 2 ou 3);
- caiu em `quando não resolve` — a skill apresentou as duas leituras e não
  decidiu.

Um item **não** entra:

- clutter (Camada 3, corte mecânico);
- gramática normativa (Camada 4);
- macroestrutura (Camada 1) — diagnóstico, não debate;
- ações `sinalizar` ou `manter` sem arbitragem de tensão;
- itens `[V]`, `[I]` ou `[D]` onde a arbitragem é clara e não marcada `[H]`.

Regra de bolso: se `revisar-clareza` **decidiu com base em fonte clara** e não
marcou `[H]`, não há o que testar. Só arbitragens sob hipótese são contestáveis.

Se o relatório não tiver nenhum item contestável, dizer isso em uma linha e
encerrar — **não** inventar pontos para justificar a invocação. Dossiê vazio é
resultado correto, não falha.

## Como argumentar cada lado

Para cada ponto contestável, o dossiê apresenta dois lados. Regras:

- **Cada lado é escrito a partir da posição da fonte**, não de uma posição
  genérica. Lado A fala *como* Zinsser, Pinker, Salvador, Bechara, Marconi ou
  Viscardi — conforme a tensão convocada.
- **Se um lado não se sustenta sem invenção**, dizer isso explicitamente. Um
  lado fraco é informação: significa que a arbitragem provavelmente se sustenta.
- **Nenhum lado é resolvido.** Esta skill não arbitra — `revisar-clareza`
  arbitrou; aqui se testa. Fechar com "concordância com a skill" é o máximo de
  síntese permitido.
- **O "o que está em jogo"** é o item mais importante do dossiê: descrever o
  que muda concretamente no texto se o lado A vencer vs se o lado B vencer. Sem
  isso, o dossiê é conversa.
- **Se um lado depende de guardrail do projeto** que `revisar-clareza` já respeitou,
  registrar — não reabrir a decisão de guardrail.
- **Crédito é afirmação factual.** Se um argumento foi construído pelo agente,
  dizer que foi. Não distribuir elogio. Nada de "boa pergunta" ou "ótima
  observação" — quando o próprio processo de escrita é dado de pesquisa (como
  numa autoetnografia), crédito impreciso contamina a fonte.
- **Se o runtime permitir**, cada lado pode ser argumentado por um subagente
  dedicado — a separação reduz o risco de raciocínio motivado. Se não, o mesmo
  agente argumenta os dois lados com separação explícita, e deve resistir à
  tentação de convergir para a arbitragem que já leu no relatório.

## Formato do dossiê

Arquivo: `<pasta-de-processo>/revisoes-clareza/<nome-do-arquivo>.adversarial.md`.

Cada item, pronto para o autor decidir sem nova invocação:

```
### <arquivo>:<linha> — Tensão <N>

**Arbitragem aplicada:** <o que revisar-clareza propôs, com a marca [H] e o eixo/actante/assimetria identificados>
**Lado A (<fonte>):** <argumento, uma ou duas frases>
**Lado B (<fonte>):** <argumento, uma ou duas frases>
**O que está em jogo:** <o que muda no texto se A vence vs se B vence>
**Concordância com a skill:** <sim | não | parcial | indeterminado — uma frase>
```

Se `revisar-clareza` caiu em `quando não resolve`, o campo "Arbitragem
aplicada" registra isso, e "Concordância com a skill" avalia se a recusa em
arbitrar se sustenta (ou se o caso era decidível e a skill hesitou).

`indeterminado` é resultado legítimo: os dois lados são igualmente fortes e
esta skill não decide. Devolve ao autor.

Quando a única informação útil for o dossiê, mostrá-lo no chat em bloco pronto
para colar. Escrever no arquivo só se o autor pedir, ou se ele já tiver
autorizado a escrita no diretório `<pasta-de-processo>/revisoes-clareza/` na sessão.

## Execução

1. Ler o relatório de `revisar-clareza` e o arquivo-fonte correspondente.
2. Filtrar os itens contestáveis (§O que é um ponto contestável).
3. Para cada ponto, construir os dois lados (§Como argumentar cada lado).
4. Escrever o dossiê em `<pasta-de-processo>/revisoes-clareza/<nome>.adversarial.md`.
   **Nunca** editar o arquivo-fonte. **Nunca** gravar espelho do relatório de
   `revisar-clareza` — só os pontos contestados.
5. Fechar com sumário: total de pontos testados; quantos `sim`, quantos `não`,
   quantos `parcial`, quantos `indeterminado`; **se a Tensão 3 foi testada,
   listar cada aplicação com o eixo identificado**. Esse sumário é o artefato
   que permite ao autor decidir se "eixo determina registro" se sustenta antes
   de virar política.

## Como falar com o autor

Em ordem de importância:

- **Instrução é "cole aqui", não "rode este script".** Cada item do dossiê é um
  bloco pronto, com âncora `arquivo:linha` e o que conferir depois.
- **Um ponto por vez quando ele estiver lendo no chat.** O dossiê pode ter
  vários; a conversa, um.
- **Sem poder de veto.** A skill aponta e mostra o custo dos dois lados; quem
  decide é o autor. Se ele mantiver a arbitragem de `revisar-clareza` contra o
  dossiê, registrar `[D]` e seguir.
- **Crédito é afirmação factual** — já dito acima, e vale para o fechamento: se
  a decisão foi do agente, dizer; se foi dele, nomear o que ele fez, com verbo
  factual e sem adjetivo de mérito.
- **Se houver prazo**, entre testar tudo e testar o que muda o que ele faz hoje, testar o segundo.

## Quando chamar outra coisa

| situação | quem resolve |
|---|---|
| revisar a prosa em si (tensões, camadas) | skill `revisar-clareza` |
| a citação existe e talvez esteja errada | skill `auditar-citacoes` |
| pontuação, travessão, voz | revisor de pontuação dedicado, se o projeto tiver |

## Limites — o que esta skill não faz

- Não edita os arquivos do texto em nenhuma circunstância. Nem linha de
  comentário. Se o projeto puder montar a pasta do texto como somente leitura,
  melhor: a fronteira vira garantia técnica, não só promessa.
- Não substitui `revisar-clareza` — só opera sobre o relatório que ela produziu.
- Não arbitra. Apresenta os dois lados e devolve ao autor.
- Não testa clutter, gramática normativa ou macroestrutura — essas camadas não
  são contestáveis.
- Não roda sobre o texto inteiro. Só sobre os pontos contestáveis do relatório.
- Não inventa pontos para justificar a invocação. Relatório sem `[H]` e sem
  `quando não resolve` produz dossiê vazio, e isso é o resultado correto.
- Não apresenta uma posição do corpus como fato linguístico neutro — nomeia de
  quem é.
- Não mantém lista própria de vocabulário protegido — lê o arquivo de
  guardrails do projeto a cada invocação.
- Não inventa rótulos de severidade — usa o esquema `[V]/[I]/[H]/[D]` já vigente.
- Não decide pelo autor sobre a arbitragem — produz material para a decisão.
- Não é chamada durante a geração de um rascunho novo — só depois que um
  rascunho completo já existe e foi revisado por `revisar-clareza`.
- Não prova que a arbitragem está certa nem errada. Ela mostra os dois lados; a
  decisão continua sendo leitura do autor.

