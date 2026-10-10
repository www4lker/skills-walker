---
name: auditoria-causal-sistemica
description: "Protocolo de auditoria causal-sistêmica de consequências. Não é um estilo: reestrutura a investigação, não a formatação. Apply only when the user explicitly requests this skill by its exact name 'auditoria-causal-sistemica'."
---

# Auditoria causal-sistêmica

## O que isto é — e o que não pode ser

Isto é uma **auditoria de cadeias causais**, não um gerador de consequências. A distinção é o motivo de a skill existir.

Nenhum protocolo em prosa faz um modelo de linguagem realizar inferência causal válida. Contrafactual, mecanismo e evidência são trabalho empírico; nenhum prompt os substitui. Não prometa rigor que você não pode entregar — prometer isso reproduz, uma camada acima, a fraude que esta skill existe para evitar: profundidade aparente.

O que a skill entrega é modesto e real: força um pequeno conjunto de movimentos que **suprimem quatro patologias** da falsa análise sistêmica e **deixam todo elo fraco visivelmente marcado como fraco**. As quatro patologias:

1. **Efeito-enciclopédia** — cobrir todas as esferas para parecer abrangente.
2. **Paradoxo fabricado** — inversões retoricamente atraentes sem condição declarada.
3. **Ancoragem-na-tese** — declarar o mecanismo dominante antes de investigar e depois organizar tudo para sustentá-lo.
4. **Setas vazias** — cadeias causalmente gramaticais e epistemicamente ocas.

Critério de sucesso: ao terminar, o leitor consegue apontar exatamente onde a análise sustenta peso e onde é ar. Uma auditoria honesta que conclui "o elo central é conjectural" cumpriu seu trabalho. Uma que produz certeza fluida falhou, por mais elegante que seja.

Nenhuma seta transforma hipótese em mecanismo. Cada movimento abaixo produz um **artefato discreto e inspecionável** — algo que o leitor confere e que o modelo não consegue esvaziar sem que a lacuna apareça.

## Ordem de construção ≠ ordem de apresentação

A patologia 3 nasce da ordem. **Construa nesta sequência; não abra pelo mecanismo dominante:**

1. Caso-base e fronteira.
2. Mecanismos candidatos (vários).
3. Cadeias + rival.
4. Loops + falsificador + indicador.
5. **Só então** nomeie o mecanismo dominante — como conclusão conquistada por (1)–(4), nunca como premissa.

Na saída para o leitor você pode apresentar a tese primeiro (é mais legível). Mas você deve tê-la **escrito por último**. Se o mecanismo dominante saiu antes de (1)–(4) existirem, você ancorou — recomece.

Uma nota de projeto: esta skill **abandona** o eixo "primeira/segunda/terceira ordem". Aquela taxonomia funde três coisas distintas — distância causal, distância temporal e profundidade institucional — e obriga o modelo a improvisar a classificação depois de já ter imaginado os efeitos. Aqui a análise se organiza por **mecanismo**, e quando os dois eixos importam eles aparecem separados: *passos causais* (quantos atores entre intervenção e efeito) e *tempo de manifestação* (rápido / lento). Um efeito institucional pode ser imediato; uma consequência direta pode levar anos. Não force um ordinal a carregar os dois.

## As oito operações

Cada operação é um movimento com um artefato obrigatório. Se você não consegue produzir o artefato, isso **é** o achado — declare-o, não o contorne.

**1. Fronteira — nomeie o lado de fora.**
Declare pelo menos dois fatores adjacentes que você está escolhendo *não* rastrear, e por quê. Uma fronteira da qual você não sabe dizer o lado de fora não é fronteira.

**2. Caso-base — o contrafactual, antes de tudo.**
Antes de rastrear qualquer efeito, escreva o que já estava acontecendo: a tendência anterior, o que ocorreria *sem* a intervenção. Toda afirmação seguinte é um **delta contra esse caso-base**, não um valor absoluto. Sem caso-base, você descreve uma sequência imaginada, não o efeito atribuível.
> Exemplo do seu terreno: se uma universidade adota detectores de IA e as acusações a estudantes sobem, o caso-base pergunta — as acusações já subiam por conta do uso crescente de IA, independentemente do detector? O delta é o que o detector adiciona a essa tendência, não o total.

**3. Cadeias — ator, adaptação e tag de apoio por elo.**
Para cada efeito, nomeie o **ator** cuja conduta o produz e a **adaptação** disponível a ele (estudantes migram para outro dispositivo; docentes mudam a prova). Um efeito sem ator e sem contra-movimento é uma suposição mecânica — marque-a como tal.
Etiquete cada elo que sustenta peso com o **tipo de apoio**, não com uma probabilidade vaga:
- **demonstrado** — visto num caso comparável que você consegue nomear;
- **mecanístico** — decorre de um incentivo/restrição conhecido, não observado neste caso;
- **conjectural** — teoricamente possível, sem apoio específico.

Nunca fabrique um "demonstrado". "Mecanístico" e "conjectural" honestos são superiores a um "demonstrado" inventado. Não cite fonte que você não consegue apontar. (Isto substitui a palavra "provável", que é indefinível — pode significar >50%, ou mais que a alternativa, ou apenas dito com mais firmeza linguística.)

**4. Orçamento — no máximo 3–4 cadeias.**
Gaste-as nos mecanismos que dominam o resultado, não em preencher esferas. Nomear uma esfera que você não vai rastrear é pior que omiti-la: se o efeito econômico é marginal aqui, escreva "econômico: desprezível, não rastreado" em vez de fabricar uma cadeia. Abrangência não é mérito; identificar os mecanismos dominantes é.

**5. Rival — um mecanismo concorrente para o dominante.**
Para o mecanismo que você vai nomear como dominante, produza ao menos **um mecanismo rival** que geraria um resultado observado semelhante por um caminho diferente. Se não conseguir, explique por que o resultado é diagnóstico do *seu* mecanismo especificamente. (No caso dos detectores: a alta de acusações pode vir do detector, da norma institucional nova, da maior disposição docente a denunciar, ou da mudança no perfil das provas. Um rival examinado impede que o primeiro encadeamento plausível vire a narrativa principal por inércia.)

**6. Loops — feche no papel ou corte a palavra.**
Se você afirma retroalimentação, **feche o loop por escrito**: nomeie a variável, ligue-a de volta a uma variável anterior da sua própria cadeia, e declare o sinal (reforçador / compensatório). Um loop que você não fecha na página é decoração — apague "feedback" e "dependência de trajetória".

**7. Paradoxo — condição declarada ou silêncio.**
"Paradoxalmente, a política destinada a X produz o contrário de X" é proibido sem a **condição específica** sob a qual a inversão se sustenta e a mesma tag de apoio de qualquer outro elo. Inversões são retoricamente atraentes e fáceis de fabricar. Sem condição, não afirme o paradoxo.

**8. Falsificador e indicador — um de cada, concretos, antes de qualquer recomendação.**
- **Falsificador:** a observação única mais barata que derrubaria sua afirmação central.
- **Indicador:** o sinal único que você observaria para saber, cedo, se a cadeia se realiza como previsto — com a direção que confirmaria e a que desmentiria.

## Alavancagem (só quando pedida)

Ponto de alavancagem sem modelo de intervenção vira recomendação genérica — "ampliar transparência", "monitorar impactos", "envolver os atores", "implementar gradualmente". Essas são intercambiáveis entre quase todos os assuntos; sua presença é o sinal de uma alavanca falsa. Cada ponto de alavancagem real carrega: **variável controlável / quem a controla / custo aproximado / atraso / adaptação esperada dos agentes / como se mede sucesso ou fracasso.** Sem esses seis campos, não é alavanca — corte.

## Autoverificação antes de emitir

Confira contra a própria saída. Cada "não" é um defeito a corrigir, não a ocultar:

- Há caso-base explícito, e cada efeito é delta contra ele?
- A fronteira nomeia o que ficou de fora?
- Cada elo que sustenta peso carrega tag de apoio? Nenhum "demonstrado" sem caso nomeável?
- O mecanismo dominante tem ao menos um rival examinado?
- Todo loop está fechado no papel, com sinal? Nenhum uso decorativo de "retroalimentação"?
- Todo paradoxo tem condição declarada?
- Existe exatamente um falsificador e um indicador, concretos, antes das recomendações?
- O mecanismo dominante foi escrito por último, mesmo que apresentado primeiro?
- Cada alavanca tem os seis campos? Nenhuma recomendação genérica intercambiável?
- Nenhum fato desconhecido foi inventado; toda lacuna está marcada como lacuna?

## Formato de saída para o leitor

Nesta ordem (lembrando: a tese é lida primeiro, mas foi escrita por último):

1. **Tese** (1–2 frases): qual mecanismo domina.
2. **Caso-base e fronteira**: o que já ocorria; o que ficou de fora.
3. **Cadeias auditadas**, organizadas por mecanismo. Cada elo com sua tag; marque *passos causais* e *tempo de manifestação* quando divergirem.
4. **Rival examinado.**
5. **Loops fechados**, se houver.
6. **Um falsificador, um indicador.**
7. **Alavancagem**, se pedida — só variáveis controláveis, com os seis campos.
8. **Lacunas honestas.**

Densidade acompanha o objeto. Uma intervenção pequena não merece as oito operações infladas; execute-as com o peso que o caso comporta.

## Quando usar — e quando recusar o enquadramento

**Use** quando uma decisão ou intervenção real precisa ser auditada quanto a consequências e você quer ver onde a análise é sólida e onde é ar, antes de agir ou escrever.

**Não use**, e diga por que, quando: o pedido é só uma explicação direta de como algo funciona (não é auditoria de consequências); não há intervenção nem contrafactual possível (fenômeno sem agente, sem decisão); ou o custo do enquadramento excede o valor. Nem toda pergunta comporta as oito operações. Recusar o enquadramento é preferível a aplicá-lo a um objeto que não o comporta — a aplicação forçada é, ela mesma, a patologia 1.

Recomendação final: Adicione um parágrafo em texto simples e objetivo, seguindo os princípios de clareza textual de Zinsser onde é explicado o que foi auditado, quais os cenários e as consequências possíveis das escolhas envolvidas. 
