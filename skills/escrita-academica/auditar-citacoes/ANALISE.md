# auditar-citacoes — análise

**Complexidade:** alta — quatro camadas de custo crescente, regra-mestra sobre fontes, vereditos padronizados

| Forças | Fraquezas |
|---|---|
| • Verifica se a fonte diz o que o texto diz que ela diz, não só se a chave existe no .bib.<br>• Organiza as camadas por custo, das baratas e determinísticas às caras e interpretativas.<br>• Nunca dá "sustenta" sem localizador da passagem. | • A L4 (escopo) é conservadora de propósito e deixa passar exageros sutis.<br>• Não detecta citação ausente, só citação presente mal usada.<br>• Livros sem texto disponível ficam em [I] por limitação de acesso. |

| Oportunidades | Ameaças |
|---|---|
| • Pode virar etapa obrigatória antes de qualquer submissão a periódico. | • Busca semântica e NotebookLM podem ser confundidos com fonte; a skill proíbe isso, mas a tentação continua. |

## Fluxo

```mermaid
flowchart TD
    A["Citação no capítulo"] --> L1["L1: existência e forma<br>(determinística, V)"]
    L1 -- "falha" --> X["Achado L1"]
    L1 -- "ok" --> L2["L2: plausibilidade dos metadados<br>(sem rede, V/I)"]
    L2 -- "suspeita" --> Y["Achado L2"]
    L2 -- "ok" --> L3{"L3: a fonte real<br>sustenta a afirmação?"}
    L3 -- "acesso ao texto" --> V3["Veredito com localizador (V)"]
    L3 -- "sem acesso" --> I3["Inferência (I), sem 'sustenta'"]
    V3 --> L4["L4: o escopo excede a fonte?<br>(sempre I, devolve ao autor)"]
    I3 --> L4
```
