# reductio-ad-absurdum — análise

**Complexidade:** alta — sete operações, tags de consequência, teste obrigatório da bala mordida

| Forças | Fraquezas |
|---|---|
| • Distingue contradição de desconforto, a confusão mais comum em reductio.<br>• Trata a "bala mordida" como resultado legítimo (custo revelado), não como fracasso.<br>• Exige a qualificação mínima que salvaria a premissa, o que torna a crítica construtiva. | • Depende de uma reconstrução caridosa feita pelo próprio modelo, que pode errar sem que o protocolo perceba.<br>• Não serve para desacordos empíricos, e a própria skill avisa isso. |

| Oportunidades | Ameaças |
|---|---|
| • É útil para ensinar argumentação: o formato de saída funciona como exercício didático.<br>• Pode alimentar a seção de "objeções antecipadas" de um texto acadêmico. | • A tag "prova-demais" pode virar atalho retórico se a premissa extremizada não for a que o proponente sustenta (patologia 1). |

## Fluxo

```mermaid
flowchart TD
    A["Argumento"] --> B["1. Reconstrução caridosa<br>P1, P2 ... -> C"]
    B --> C["2. Escolher 2-4 premissas-alvo<br>+ declarar uma poupada"]
    C --> D["3. Extremizar cada premissa<br>(nomear o que foi removido)"]
    D --> E{"4. Tag da consequência"}
    E -- "contradição interna<br>prova-demais<br>colapso conceitual" --> F{"5. O proponente pode<br>morder a bala?"}
    E -- "desconforto" --> G["Não conta como refutação"]
    F -- "sim" --> H["Custo revelado"]
    F -- "não" --> I["Premissa cai"]
    I --> J["7. Qualificação mínima<br>ou declaração de que nenhuma salva"]
    H --> K["6. Veredito por premissa"]
    J --> K
    G --> K
```
