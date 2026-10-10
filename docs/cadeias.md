# Cadeias entre skills

Algumas skills só fazem sentido quando usadas junto com outras. Os diagramas abaixo mostram essas ligações.

## Cadeia de clareza

`revisar-clareza` arbitra tensões entre autores e marca cada arbitragem com `[I]` ou `[H]`. `testar-arbitragem-clareza` recebe o relatório, ataca só as arbitragens `[H]` e devolve a decisão ao autor.

```mermaid
flowchart LR
    T["Trecho rascunhado"] --> R["revisar-clareza<br>4 camadas"]
    R --> REL["Relatório<br>arbitragens I e H"]
    REL --> TA["testar-arbitragem-clareza<br>só os pontos H"]
    T --> TA
    TA --> DOS["Dossiê: lado A × lado B<br>+ o que está em jogo"]
    DOS --> AUT{"Autor decide"}
    AUT --> T
```

## Cadeia da defesa

`simular-banca` encena os examinadores. Quando o pesquisador trava, ou no modo `--auto`, ela chama `simular-pesquisador`, que só aponta onde a resposta está no texto. A banca pergunta, o treinador ancora e o pesquisador responde.

```mermaid
flowchart TD
    P["Perfis da banca<br>+ parecer + dossiê"] --> B["simular-banca"]
    B --> Q["Pergunta rotulada<br>com origem marcada"]
    Q --> M{"Modo"}
    M -- "interativo" --> PE["Pesquisador responde"]
    PE --> RE["Examinador reage"]
    RE --> Q
    PE -. "chamar treinador" .-> SP
    M -- "--auto N" --> SP["simular-pesquisador"]
    SP --> AN["Localização + núcleo verbatim<br>ou lacuna declarada"]
    AN --> FIM["Mapa de arguição:<br>apoiadas / lacunas / ponteiros"]
```

## Cadeia do corpus

As três skills de corpus dividem o trabalho por custo. `navegacao-corpus` só indica caminhos, `corpus-search` localiza com grep antes de ler e `artifacts-fichamento` lê e ficha.

```mermaid
flowchart LR
    C["Conceito ou lacuna"] --> N["navegacao-corpus<br>mapa estático, não lê"]
    C --> S["corpus-search<br>grep em 4 camadas"]
    N --> A["artifacts-fichamento<br>lê o Artifact .md"]
    S --> A
    S -. "sob demanda" .-> BIB["Extração bibliográfica"]
    A --> F["Fichamento + alerta crítico"]
    F --> SRC["Rastrear até a Source primária"]
```

## Padrão de delegação ao Gemini

`gemini-delegate` é a ferramenta genérica. `gemini-source-extractor`, ainda experimental, aplica o mesmo padrão à extração bibliográfica. O Gemini lê muito e devolve pouco; o Claude confere e decide.

```mermaid
flowchart LR
    G["Texto grande<br>HTML, CSV, transcrição"] --> D["Gemini CLI<br>ask.sh / ask_batch.py"]
    D --> O["Saída compacta"]
    O --> CL["Claude confere"]
    CL -- "ok" --> USO["Resumo, classificação<br>ou entrada BibTeX"]
    CL -- "suspeito" --> V["Verificação manual na fonte"]
```

## Protocolos de raciocínio: qual usar

```mermaid
flowchart TD
    Q["Pergunta"] --> T{"Sobre o quê?"}
    T -- "consequências de uma decisão" --> ACS["auditoria-causal-sistemica"]
    T -- "estrutura lógica de um argumento" --> RAA["reductio-ad-absurdum"]
    T -- "texto de terceiro a avaliar" --> AA["auditor-argumentativo-style"]
    T -- "tema político ou moral contestado" --> I{"Vale pagar API?"}
    I -- "não" --> IP["invariancia-politica"]
    I -- "sim" --> CP["contraprova"]
```
