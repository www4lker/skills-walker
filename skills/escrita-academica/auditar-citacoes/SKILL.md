---
name: auditar-citacoes
description: "Audita se cada citação (\\cite e afins) de um capítulo sustenta a afirmação que a acompanha — não se a chave existe no .bib, mas se a fonte diz o que o texto diz que ela diz, no ponto exato em que é citada. Camadas da checagem barata (a chave existe, o tipo de entrada é válido, os campos ABNT estão lá) à cara (a fonte real sustenta a afirmação? o escopo da afirmação excede a fonte?). Nunca edita o texto nem a bibliografia — produz um relatório em <pasta-de-processo>/revisoes-citacoes/. Um arquivo por invocação. Rende mais em capítulos empíricos, onde as fontes têm DOI verificável; em capítulos teóricos boa parte das citações fica em \"fora do alcance\". Use quando o autor pedir para conferir, auditar, checar o lastro ou a adequação das citações de um capítulo. Não use para resolver placeholders de citação nem para revisar prosa (é a skill revisar-clareza)."
---

# Auditar Citações

## Por que esta skill existe

Uma citação pode ser bibliograficamente impecável — a chave existe, os metadados
batem, a entrada compila — e ainda assim estar **errada no ponto de uso**: a
fonte não sustenta a afirmação que ela ancora, ou sustenta uma afirmação mais
estreita do que a que o texto faz.

Um exemplo do tipo de erro: um capítulo citava Liang et al. (2023, *Patterns*,
DOI `10.1016/j.patter.2023.100779`) para "textos de não nativos classificados
como IA em taxas superiores a 60%". O dado é correto **para os detectores que
Liang testou** (GPTZero e o classificador da OpenAI, entre outros). Mas o
capítulo usava a citação a um passo de *outro* detector, que o estudo não
testou e para o qual o viés não estava demonstrado. A citação estava
certa; o escopo em que era invocada, não.

Ferramentas de bibliografia respondem *"a chave existe? o placeholder está
resolvido?"*. Revisão de clareza lê *como* o texto está escrito. Nenhuma das
duas pergunta se a fonte sustenta a frase — é o buraco que esta skill preenche.

Esta skill não decide se a citação sai ou fica. Diagnostica, marca o estatuto
epistêmico de cada achado e devolve a decisão ao autor.

## Antes de agir

1. Ler os arquivos de contrato e de estado do projeto, se existirem (ex.:
   `AGENTS.md`, `CLAUDE.md`, arquivo de estado datado), em especial a fronteira
   de escrita e os guardrails conceituais. Uma citação teórica pode estar
   esticada além do que a fonte permite, e isso é achado de L4.
2. Rodar `git status --short`. Alterações preexistentes são do autor.
3. **Confirmar com o autor qual arquivo auditar.** Um por invocação. Um recorte
   menor ("só as citações da Seção X", "só a chave `fulano_2023`") é aceito para
   iterar rápido sobre um caso.
4. Ler os casos já sabidos (seção **Casos conhecidos**, abaixo) para não
   relevá-los como novos.
5. **Confirmar a contagem e o estado do `.bib` na branch atual** (ex.:
   `grep -c "^@" <arquivo>.bib`). Não assumir número herdado desta skill ou de
   memória.

## Fontes

Preencha os caminhos do seu projeto.

| Fonte | Para quê | Estatuto |
|---|---|---|
| `<bibliografia>.bib` (todos os arquivos ativos) | chave, tipo de entrada, metadados, `doi`/`url`/`eprint`/`howpublished`, os `abstract` que existirem | `[V]` — leitura direta |
| A frase que precede/segue cada citação, nos arquivos do texto | a afirmação que a citação precisa sustentar | `[V]` |
| Fonte on-line via `doi`/`url`/`eprint` (busca na web) | o que a fonte real diz | `[V]` se o texto for acessível; `[I]` se só abstract / resumo de editora / paywall |
| Catálogo de metadados do acervo, se houver | "a obra está no acervo?" — **não serve para conteúdo** | `[V]` para presença; `[I]` para ausência (o catálogo pode estar defasado) |
| Corpus local de fontes (ex.: export do NotebookLM, PDFs) | matéria-prima textual dos livros sem `doi` | `[I]` — índice de recuperação |
| Registros do projeto sobre casos conhecidos (pendências, handoffs, caixa de entrada) | contra-dados e decisões já tomadas | `[V]`/`[D]` conforme a marca no arquivo |

## Regra-mestra sobre fontes

- **Só se cita uma fonte verbatim com localizador** (página, seção, parágrafo,
  timestamp). Sem localizador, não se afirma "a fonte diz X" — afirma-se "não
  verifiquei o texto da fonte".
- **Busca semântica, NotebookLM e índices vetoriais são índice de recuperação,
  nunca fonte de frase.** Dizem *onde procurar*; a frase só entra no relatório
  depois de lida na fonte. Síntese de IA sobre a fonte não é evidência primária.
  Atenção: corpora exportados costumam misturar fontes primárias convertidas
  com sínteses geradas — uma síntese não é a fonte.
- **Catálogo de metadados responde "a obra existe no acervo?" e nada mais.**
- Quando a verificação de conteúdo não é possível daqui, o achado é
  `verificação de conteúdo fora do alcance desta skill` — não um `[V]` nem um
  silêncio.

## As camadas

Cada citação passa por L1 → L4 na ordem. L1 e L2 são mecânicas; L3 e L4 são o
trabalho real. Falha em L1 ⇒ L2–L4 não rodam para aquela chave.

### L1 — Existência e forma (determinística, `[V]`)

- **A chave existe** num dos `.bib` ativos? Se não: achado `chave ausente`.
  Reportar e encaminhar a quem cuida da bibliografia — esta skill não cria
  entradas.
- **Tipo de entrada válido para o sistema de citação em uso?** Exemplo real:
  com BibTeX puro + `abntex2cite`, `@online` é inválido e a entrada some em
  silêncio, sem erro de compilação — achado `tipo inválido`.
- **Campos mínimos da norma (ex.: ABNT autor-data):** `author` — ou
  `organization`/`title` para obra institucional — mais `year` e `title`.
  Faltando `year` numa entrada citada: `campo ABNT ausente`.
- **Placeholder** de citação (o marcador que o projeto usar) perto de afirmação
  sem citação: reportar `citação pendente` e encaminhar.

### L2 — Plausibilidade dos metadados (semi-determinística, `[V]`/`[I]`, sem rede)

Confronta o que o texto **implica** sobre a fonte com o que o `.bib` **diz**:

- Ano citado na prosa ("estudos de 2023") bate com `year`?
- Autor nomeado na prosa ("como argumenta Latour") aparece em `author`?
- Título/veículo plausível para a afirmação? (Citação de "relatório técnico da
  empresa X" apontando para um `@article` de outro autor é sinal.)
- Mesma obra sob duas chaves com anos/edições diferentes é achado de L2 — salvo
  se estiver em **Casos conhecidos** como decisão consciente.

Saída: `metadados plausíveis` / `divergência de metadados` + o quê.

### L3 — A fonte real sustenta a afirmação? (cara, `[V]` ou `[I]` conforme acesso)

1. **Isolar a afirmação ancorada.** Ler o período (ou lista de períodos) que a
   citação sustenta. Escrever numa frase no relatório: "Afirmação ancorada: …".
2. **Escolher a via conforme o caso:**

   | Caso | Via | Estatuto |
   |---|---|---|
   | Entrada tem `abstract` no `.bib` | leitura direta do abstract | `[V]` se cobre a afirmação; `[I]` se insuficiente |
   | Entrada tem `doi`/`url`/`eprint` | leitura da fonte (página do artigo, arXiv, PDF aberto, documentação do fabricante) | `[V]` se o texto acessado sustenta ou contradiz; `[I]` se paywall / só metadados |
   | Livro teórico sem `abstract`/`doi`/`url` | ver seção **Livros teóricos** | `[I]` ou `fora do alcance` |
   | Chave ausente | — | reportado em L1 |

3. **Veredito de L3:** `sustenta` · `sustenta parcialmente` (a fonte diz menos,
   ou com ressalva que o texto omite → segue para L4) · `não sustenta` ·
   `não verificável daqui` (nomear por quê).

**Nunca** `sustenta` sem localizador da passagem (Regra-mestra).

### L4 — O escopo da afirmação excede a fonte? (sempre julgamento, sempre `[I]`, sempre devolve ao autor)

O caso Liang. Roda quando L3 deu `sustenta` ou `sustenta parcialmente`.

**A L4 é conservadora.** Só levanta achado quando:

- (a) a afirmação **generaliza além da população / objeto / instrumento** que a
  fonte estudou, de forma claramente distinta; ou
- (b) há **contra-dado no próprio projeto** que deveria estar no mesmo parágrafo
  e não está; ou
- (c) a citação é usada como **apoio** quando é, na verdade, **contra-dado**.

Transposição analógica não marcada (ex.: passar de "arquitetura técnica" a
"hiper-real" via Baudrillard) é **registrada como observação no relatório, não
como achado**. O autor calibra depois se quer uma L4 mais ampla.

Todo achado de L4:
- nomeia a inferência (`[I]`, "não verifiquei a intenção do autor aqui");
- cita **onde** o contra-dado ou a ressalva vive (arquivo:linha ou o registro do
  projeto);
- termina em **"decisão do autor"**.

A skill conclui que *o escopo merece exame* e mostra o material — **não** que a
citação está errada.

## Livros teóricos sem matéria-prima textual

Citações teóricas — Foucault, Latour, Ihde, Baudrillard, Bourdieu e afins — em
geral não têm `abstract`, `doi` nem `url`. A verificação de conteúdo delas tem
três níveis:

1. **Metadado (sempre).** Confirmar no catálogo do acervo que a obra está lá.
   Resultado `[V]`: "obra presente no acervo" — elimina a hipótese de citação
   fantasma.
2. **Recuperação contra o corpus (`[I]`, se o projeto tiver a via).** Localizar
   o texto da fonte e recuperar 3–5 passagens próximas da afirmação (ex.: por
   delegação a outro modelo — ver `gemini-delegate` — ou por índice vetorial
   local). Serve para o autor abrir a fonte no ponto certo — **nunca** vira
   veredito `sustenta`.
3. **Fora do alcance (o caso mais comum, e o honesto).** Para afirmações que
   dependem de leitura fina de argumento filosófico ("Foucault define parrésia
   como X"), o veredito é `verificação de conteúdo requer a edição (física ou PDF
   completo) — fora do alcance desta skill`, com a marca `[I]`, sem fingir `[V]`.

Racional: fingir auditar Foucault a partir de uma síntese gerada violaria a
Regra-mestra. O valor da skill aqui é **estreitar onde o autor precisa olhar**,
não substituir a leitura dele.

## Interação com outras ferramentas

A skill é independente por design; delega quando — e só quando — a dependência
estiver viva. Ferramentas caras (reindexação, embeddings, modelos locais pesados)
**não são invocadas por padrão**; se o autor gerar a saída delas, a skill pode
consumi-la como insumo de L3, e o veredito continua sendo da skill.

## Marcas epistemológicas

| Marca | Uso nesta skill |
|---|---|
| `[V]` | li a fonte (abstract no `.bib`, texto acessado por `doi`/`url`, ou edição) e comparei com a afirmação. **Localizador obrigatório.** |
| `[I]` | inferência: divergência de L2, `sustenta parcialmente` de L3 sem acesso pleno, **todo achado de L4**, metadado do corpus |
| `[H]` | hipótese sobre a intenção do texto que nem o texto nem a fonte confirmam |
| `[D]` | decisão do autor já registrada |

**Proibido** inventar rótulos de severidade ("crítico", "grave") ou novos
rótulos epistemológicos. **Quando não verificou, escrever "não verifiquei"** — um
`[H]` honesto vale mais que um `[V]` inventado.

## Casos conhecidos — não relevar como novos

Mantenha aqui uma tabela dos casos já registrados no projeto. Ao encontrá-los,
**citar o registro e seguir** — no máximo confirmar que o estado não mudou.

| Caso | Registro | Como tratar |
|---|---|---|
| `<ex.: fonte X é contra-dado, não apoio, para o objeto Y>` | `<arquivo de registro>` | Levantar se o contra-dado ainda não estiver no parágrafo, enquadrado como "risco já conhecido", `[I]`, decisão do autor. **Não** apresentar como descoberta. |
| `<ex.: mesma obra em duas edições, decisão consciente>` | `<registro>` | Registrar "duas chaves, decisão pendente/tomada" e **não** abrir achado de L2. |
| `<ex.: maioria das entradas é @misc>` | `<registro>` | **Não é erro por si** quando o objeto é recente e a documentação primária só existe como página, relatório ou reportagem. Só reportar se uma entrada específica falhar L3/L4. |

Ao buscar nesses registros, prefira uma ferramenta de busca confiável e confira
um termo que você sabe que existe: uma busca que volta vazia por defeito da
ferramenta produz um "caso conhecido não encontrado" falso.

## Protocolo de saída

1. Ler o arquivo indicado. Listar toda citação com `arquivo:linha`.
2. Rodar L1 para todas. L2 para as que passaram em L1. L3 para cada uma que
   passou. L4 para as que L3 deu `sustenta` ou `sustenta parcialmente`.
3. Escrever **um relatório** em
   `<pasta-de-processo>/revisoes-citacoes/<nome-do-arquivo>.md` — **nunca editar o
   texto nem o `.bib`, e não gravar espelho do arquivo.**

   Formato de cada item (espelha `revisar-clareza`):

   ```
   ### <arquivo>:<linha> — <chave> — <veredito>

   **Afirmação ancorada:** <a frase que a citação sustenta, uma frase>
   **A fonte:** <o que a fonte diz, com localizador — ou "não verificável daqui: <motivo>">
   **Camada:** <L1 | L2 | L3 | L4>
   **Estatuto:** <[V] | [I] | [H] | [D]>
   **Motivo:** <uma a três frases>
   **Para o autor:** <ação sugerida — só em L4 e em "não sustenta"; senão "—">
   ```

   Vereditos possíveis: `sustenta` · `sustenta parcialmente` · `não sustenta` ·
   `escopo excede a fonte` (L4) · `chave ausente` · `tipo inválido` ·
   `campo ABNT ausente` · `divergência de metadados` · `citação pendente` ·
   `não verificável daqui` · `caso conhecido — sem mudança`.

   Listar `sustenta` limpo só quando a citação passou por L3 real com localizador
   — não inflar a lista com prosa intocada.

4. Fechar com um **sumário**: total de citações · quantas passaram em L1 ·
   vereditos de L3 por tipo · nº de achados de L4 · nº de "não verificável daqui"
   e por quê · lista dos casos conhecidos tocados (com "sem mudança" ou o que
   mudou).

5. Se houver achado que peça marcação no texto para decidir depois, **propor** a
   linha de comentário no formato que o projeto usar — e só anotar com
   autorização do autor na sessão. Nunca escrever nem comentar prosa.

6. Aplicar mudanças, editar o `.bib`, commitar e decidir o destino de cada
   citação são atos do autor. Esta skill não aplica nada.

## Limites — o que esta skill não faz

- Não edita os arquivos do texto nem a bibliografia. Não inventa entradas,
  chaves, DOIs, páginas nem passagens.
- Não resolve placeholders de citação — detecta e encaminha.
- Não roda ferramentas caras (reindexação, embeddings, modelos locais) sem o
  autor pedir.
- Não chama serviços externos de terceiros que o projeto usa como objeto de
  pesquisa (ex.: detectores) sem autorização explícita — por limite de uso e pelos
  termos de acesso.
- Não decide se uma citação sai ou fica.
- Não faz crítica de prosa (é `revisar-clareza`) nem crítica de argumento em
  geral — só da relação citação ↔ fonte no ponto de uso.
- Não converte memória de conversa ou de sessão anterior em `[V]`. Não apresenta
  síntese de IA sobre uma fonte como evidência primária.
- Não commita, não faz push, não mescla.
- **Não detecta afirmações que deveriam ter citação e não têm.** A skill audita
  as citações presentes; uma afirmação forte sem citação e sem placeholder passa
  despercebida. Isso pede outra ferramenta, que parta do lado oposto: achar o
  parágrafo sem citação e dizer se o lastro já existe no projeto.
