# corpus-search — análise

**Complexidade:** alta — protocolo grep em quatro camadas, variáveis de ambiente, criação de notas no vault

| Forças | Fraquezas |
|---|---|
| • Nunca lê arquivo sem confirmar relevância com grep, o que economiza muitos tokens.<br>• Faz a extração bibliográfica só sob demanda e começa pelo metadado, que não custa nada. | • Exige preencher ambiente, contexto e mapa de notebooks antes do primeiro uso.<br>• Depende da estrutura de pastas do export do NotebookLM, que pode mudar. |

| Oportunidades | Ameaças |
|---|---|
| • O protocolo de quatro camadas vale para qualquer corpus grande em texto. | • As variações de conceito para o grep, mal escolhidas, geram falso negativo silencioso. |

## Nota

O diagrama está em [docs/cadeias.md](../../../docs/cadeias.md), na cadeia do corpus.
