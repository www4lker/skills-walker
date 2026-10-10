---
name: revisar-clareza
description: "Revisa a clareza sintática e estilística de um capítulo ou trecho já rascunhado de um texto acadêmico em português, arbitrando tensões documentadas entre Zinsser, Pinker, Salvador, Moura, Bechara, Marconi, Viscardi e Tufte para cortar ruído sem apagar a voz autoral. Nunca edita o arquivo original — produz um relatório de intervenções em <pasta-de-processo>/revisoes-clareza/. Use quando o autor pedir para revisar, polir, dar clareza a, ou verificar a prosa de um capítulo já escrito. Não use durante a geração de um rascunho novo."
---

# Revisar Clareza

## Por que esta skill existe

O autor já tem a própria voz. O que esta skill faz é reduzir ruído — excesso,
jargão institucional, sintaxe que esconde o agente — sem confundir isso com
apagar cadência, ritmo ou escolha estilística deliberada.

Os critérios vêm de um corpus de escrita lido pelo autor da skill fora do
repositório (Zinsser, Pinker, Salvador, Moura, Bechara, Marconi, Viscardi,
Tufte, *Paralelismo for Dummies*). **Nenhuma dessas fontes está no repo**:
as citações abaixo não são auditáveis a partir daqui e reproduzem uma
leitura pessoal `[I]`. Não são regras genéricas importadas sem
adaptação, mas também não são verificáveis por um agente sem acesso ao
corpus externo. Ao invocar uma delas contra um trecho, dizer de quem é a
posição — nunca apresentá-la como fato linguístico neutro.

Esta skill nunca decide sozinha o que fica no texto. Ela diagnostica, arbitra
declaradamente e sinaliza dúvida. A decisão final é sempre do autor.

## Antes de agir

1. Ler os arquivos de contrato e de estado do projeto, se existirem (ex.:
   `AGENTS.md`, `CLAUDE.md`, arquivo de estado datado).
2. Ler o arquivo de guardrails do projeto inteiro antes de tocar qualquer
   trecho. Não há lista de
   vocabulário protegido embutida aqui de propósito — guardrails do
   repositório mudam mais rápido do que este arquivo seria atualizado.
   Regra geral na ausência de guardrail nomeado: nunca substituir, simplificar
   ou parafrasear um termo que apareça formalmente definido ou atribuído a
   uma linhagem teórica em outra parte do texto-fonte, mesmo que pareça
   hermético ou incomum.
3. Confirmar com o autor qual arquivo revisar. Um arquivo por invocação —
   arquivos disjuntos permitem paralelismo seguro.
4. **Identificar o eixo do trecho** antes de julgar registro — ver Tensão 3.

## Princípio-guia (não negociável)

Antes de qualquer camada abaixo, para cada trecho: **isso é ruído ou é voz?**

- **Ruído**: excesso de palavras supérfluas (*clutter*), jargão institucional,
  substantivo abstrato sem função informativa. Corte mecânico, sem hesitação.
- **Voz**: cadência, ritmo, ênfase expressiva deliberada — inclusive
  assimetrias e "irregularidades" intencionais. Protegida de qualquer
  intervenção.

Na dúvida entre as duas, a resposta padrão é **voz — não mexa**, e a dúvida
vai para o log, não para uma decisão automática.

## Como as tensões funcionam

O corpus de clareza **não é unânime**. Em três pontos as fontes se contradizem
frontalmente, e tratar qualquer um dos lados como regra produz revisão cega:
ou se passa a régua sobre a voz (lado prescritivo), ou não se corta nada
(lado permissivo). Cada tensão abaixo tem quatro partes — **tese**,
**antítese**, **arbitragem** e **quando não resolve**.

A arbitragem é o único trabalho real desta skill. Ela é situada: deriva do
que *este* texto assume (no exemplo abaixo, a Teoria Ator-Rede; troque pelos pressupostos do seu), não de uma preferência
estilística geral. Ao aplicar uma arbitragem, **nomeá-la no relatório** —
"Tensão 1, favorece Pinker porque o agente é actante técnico" é auditável;
"passiva mantida" não é.

Quando a arbitragem não alcança o caso, a cláusula *quando não resolve*
manda apresentar as duas leituras e não decidir. Isso não é hesitação: é o
resultado correto.

---

### Tensão 1 — Voz passiva: Zinsser × Pinker (Camada 3)

**Tese (Zinsser)** `[I]` — voz passiva em excesso é impessoal, esconde
responsabilidade, deve ser cortada por padrão.

**Antítese (Pinker)** `[I]` — classificar a passiva como erro em si ignora sua
função cognitiva: direciona foco, ordena informação dada antes de nova,
estabiliza o protagonista da cena.

**Arbitragem** `[H]` — o texto de origem adota a Teoria Ator-Rede (TAR). Logo o critério não é "sempre
ativa" nem "sempre passiva", e sim: **a passiva oculta um actante que a
própria teoria exige tornar visível?**

- Favorece **Pinker** (preservar) quando o agente oculto é actante técnico
  já estabelecido na cena — o detector, o modelo, o *threshold* — e nomeá-lo
  de novo seria redundância, não revelação.
- Favorece **Zinsser** (converter) quando o agente oculto é o próprio
  pesquisador sendo apagado por covardia burocrática, não por escolha
  metodológica declarada.

A distinção é entre impessoalidade **convencional** (legítima, é a norma do
gênero) e impessoalidade **evasiva** (ruído: esconde quem decidiu o quê).

**Quando não resolve:** apresentar as duas leituras no relatório, não decidir.

---

### Tensão 2 — Paralelismo: Salvador × Bechara (Camada 2)

**Tese (Salvador)** `[I]` — termos coordenados devem compartilhar estritamente
a mesma classe gramatical.

**Antítese (Bechara)** `[I]` — coordenação mista (sintagma nominal + oração
subordinada, via hipotaxe) é gramaticalmente legítima, documentada com
exemplo de Alexandre Herculano.

**Arbitragem** `[H]` — a assimetria é **falha** quando mistura categorias
conceitualmente incompatíveis de um jeito que confunde ("alhos com bugalhos",
*Paralelismo for Dummies*); é **voz** quando cria ênfase ou ritmo perceptível
e parece deliberada.

O teste operacional: a assimetria atrapalha a leitura da lista, ou marca o
último item como diferente de propósito?

**Quando não resolve:** sinalizar, não decidir.

---

### Tensão 3 — Impessoalidade: Marconi × Viscardi (Camada 3)

**Tese (Marconi)** `[I]` — redação científica exige caráter estritamente
impessoal.

**Antítese (Viscardi)** `[I]` — a escrita é espaço legítimo de afirmação de
identidade: geográfica, de classe, de gênero.

**Nenhuma fonte do corpus reconcilia as duas** `[I]`. Nem Marconi é absoluta:
ela mesma admite que "é inútil falar em impessoalidade verbal… o enunciador
deixa marcas de sua subjetividade… na escolha do vocabulário, no uso de
adjetivos e advérbios."

**Arbitragem** `[H] — hipótese do autor em teste, sem fonte que a
sustente` — **o eixo do trecho decide o registro**:

- eixo **empírico/metodológico** → pende para Marconi (já é o registro dos
  capítulos substantivos);
- eixo **autoetnográfico** (registro de processo, prosa reflexiva) → pende para Viscardi, por
  definição de gênero.

Não aplicar padrão único ao documento inteiro. Antes de tratar primeira
pessoa ou marcador subjetivo como ruído ou como voz, **perguntar em que eixo
o trecho está**.

**Status desta arbitragem:** é a mais frágil das três — a única sem fonte
dando o critério. Está em teste. **Toda vez que ela for aplicada, registrar
no relatório com a marca `[H]` e o eixo identificado**, para que o autor
possa julgar se o critério se sustenta na prática antes de virar política. Se
o autor discordar de "eixo determina registro", esta tensão inteira muda.

**Quando não resolve:** se o eixo do trecho for ambíguo ou misto, não arbitrar
— sinalizar e perguntar.

---

## Camada 1 — Macroestrutura e ordenação

- Cada parágrafo sustenta uma única tese secundária subordinada ao problema
  do capítulo.
- Informação já estabelecida antes de informação nova (*given-before-new*) —
  como estratégia retórica, não como regra sintática rígida.

## Camada 2 — Sintaxe e paralelismo (Bechara; Tufte; *Paralelismo for Dummies*)

- Enumerações e comparações coordenadas passam pela **Tensão 2**.
- Segmentar períodos com mais de duas subordinadas encaixadas — mas sem
  fragmentar em telegrama. A subordinação é mais tolerada em português culto
  do que em inglês; não aplicar o padrão de frase curta anglófono sem
  necessidade. Um parágrafo longo mas coeso, de tese única, não é candidato
  a corte só por comprimento.

## Camada 3 — Léxico, diátese e voz (Zinsser; Pinker; Salvador; Moura; Marconi; Viscardi)

- Toda voz passiva passa pela **Tensão 1**.
- Toda marca de subjetividade (primeira pessoa, adjetivo avaliativo, advérbio
  modal) passa pela **Tensão 3**.
- Nominalização **convertida** quando é a primeira escolha para relatar um
  evento novo ("substantivo zumbi" — esvazia o agente, impede visualizar a
  ação).
- Nominalização **preservada** quando retoma anaforicamente algo já dito,
  atenua uma afirmação crítica (*face-work*), **ou é terminologia técnica do
  campo**. Este último caso é o mais comum no texto de origem e não é sintoma:
  *detecção*, *atribuição*, *evasão* são o vocabulário do objeto, não
  substantivos zumbis. Contagem bruta de nominalizações é um sinal falso —
  não usar como métrica.
- *Clutter* — palavra que pode sair sem perda ("diversas vezes" depois de
  "reformula", "plenamente" antes de "explicado") — é ruído puro. Corte sem
  consultar tensão.

## Camada 4 — Gramática normativa (Bechara)

- Concordância, regência, pontuação — norma culta padrão.
- Subordinada às Camadas 2 e 3: uma correção normativa que apagaria voz ou
  quebraria um guardrail do projeto não é aplicada automaticamente — é
  sinalizada para decisão do autor.
- **Travessão é escopo de um revisor de pontuação dedicado**, se o projeto
  tiver um, não desta skill. Não reescrever travessões nem trocar sinais de pontuação por eles.
- Inconsistência tipográfica (aspas Unicode `“ ”` onde o arquivo usa
  `` `` '' ``, travessão Unicode onde usa `---`) é achado legítimo de Camada 4,
  mas **corrigi-la altera linhas de prosa** — logo é sempre sinalização,
  nunca intervenção.

## Execução

1. Ler o arquivo indicado.
2. Identificar o eixo do trecho (Tensão 3, passo 4 do *Antes de agir*).
3. Aplicar as camadas em ordem, sempre filtradas pelo princípio-guia
   (ruído ou voz?) e pelas tensões quando o caso as convocar.
4. Escrever um **relatório de intervenções** em
   `<pasta-de-processo>/revisoes-clareza/<nome-do-arquivo>.md` — **nunca editar o
   arquivo original, e não gravar espelho do arquivo inteiro.**

   O espelho foi abandonado `[D]`: um arquivo de 191 linhas
   para comunicar 4 edições esconde o sinal em vez de exibi-lo, e o diff
   textual confunde mudança de palavra com mudança de quebra de linha.

   Formato de cada item do relatório:

   ```
   ### <arquivo>:<linha> — <ação>

   **Antes:** <trecho original, só a extensão necessária>
   **Depois:** <trecho proposto — omitir se ação = sinalizar>
   **Tensão:** <número e lado favorecido, ou "—" se clutter/Camada 1>
   **Motivo:** <uma frase>
   ```

   Ações possíveis: `reescrever` · `sinalizar` · `manter` (só registrar
   `manter` quando o trecho pareceria candidato óbvio e foi deliberadamente
   preservado — não listar prosa intocada).

5. Fechar o relatório com um sumário: total avaliado, reescritos por tipo,
   sinalizados, e **quantas vezes cada tensão foi convocada e para que lado**.
   Se a Tensão 3 foi aplicada, listar cada aplicação com o eixo identificado.
6. Recompilar e aplicar as mudanças são atos do autor. Esta skill não aplica
   merge nem decide sozinha o que entra no texto.

## O que esta skill não faz

- Não edita os arquivos do texto em nenhuma circunstância.
- Não grava espelho de arquivo inteiro — grava relatório de intervenções.
- Não decide sozinha quando a arbitragem de uma tensão não alcança o caso —
  apresenta as duas leituras e devolve ao autor.
- Não apresenta uma posição do corpus como fato linguístico neutro: sempre
  nomeia de quem é.
- Não trata contagem bruta (nominalizações, passivas, comprimento de linha)
  como diagnóstico.
- Não mexe em travessões — escopo do revisor de pontuação.
- Não é chamada durante a geração de um rascunho novo — só depois que um
  rascunho completo já existe (Becker; Bolker).
- Não mantém lista própria de vocabulário protegido — lê o arquivo de
  guardrails do projeto a cada invocação, porque o estado do repositório muda mais rápido do que
  este arquivo seria atualizado.
- Não inventa rótulos de severidade — usa o esquema `[V]/[I]/[H]/[D]` já
  vigente no repositório.

## Crítica argumentativa não é escopo desta skill

Esta skill lê **como o texto está escrito**, não **se o que ele afirma se
sustenta**. Um capítulo pode sair daqui cristalino e continuar
argumentativamente frágil: conclusão que excede a evidência, petição de
princípio, transposição analógica rompida, objeção óbvia
não antecipada.

Se o autor pedir isso, dizer que é outro trabalho e não tentar fazer os dois
na mesma passada.
