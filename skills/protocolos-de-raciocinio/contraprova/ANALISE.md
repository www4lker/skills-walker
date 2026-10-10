# contraprova — análise

**Complexidade:** alta — dois scripts, API externa paga, comparação cega com duas amostras, registro em arquivo

| Forças | Fraquezas |
|---|---|
| • Tira o teste de viés do próprio modelo: um segundo modelo responde à pergunta cega.<br>• Faz a comparação às cegas, com o mapa de origem revelado só no fim.<br>• Usa duas amostras para separar divergência estável de ruído do modelo externo. | • Custa dinheiro: quatro chamadas pagas por contraprova, mais no teste de invariância.<br>• Depende de um único fornecedor externo (DeepSeek); se a API mudar, os scripts quebram em silêncio ou com erro pouco claro.<br>• Os scripts não foram executados na preparação deste repositório. |

| Oportunidades | Ameaças |
|---|---|
| • Trocar o modelo externo, ou acrescentar um terceiro, é mudança pequena nos scripts.<br>• Os registros datados formam, com o tempo, um corpus de divergências entre modelos. | • Concordância entre modelos não é verdade, porque os corpora de treino se sobrepõem. A skill avisa isso.<br>• O DeepSeek tem restrições conhecidas em temas ligados à China. |

## Fluxo

```mermaid
flowchart LR
    Q["Pergunta com identidade"] --> R["1. Reformulação cega"]
    R --> C["2. Resposta Claude<br>[fato]/[valor] + melhor contra-argumento"]
    R --> D1["DeepSeek amostra 1"]
    R --> D2["DeepSeek amostra 2"]
    C --> K1["Comparação cega 1"]
    D1 --> K1
    C --> K2["Comparação cega 2"]
    D2 --> K2
    K1 --> S["4. Síntese: só conta divergência<br>presente nas duas amostras"]
    K2 --> S
    S --> G["5. Registro datado"]
```

## Nota

Requer `DEEPSEEK_API_KEY`. Veja o aviso no SKILL.md.
