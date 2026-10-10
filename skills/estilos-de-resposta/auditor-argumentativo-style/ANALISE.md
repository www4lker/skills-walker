# auditor-argumentativo-style — análise

**Complexidade:** alta — procedimento em seis passos, duas taxonomias (categoria e veredito), laudo com formato fixo

| Forças | Fraquezas |
|---|---|
| • Audita também a leitura do usuário, não só o texto de terceiro.<br>• Tem taxonomia fina de diagnósticos e proíbe "ponto cego" genérico.<br>• Aceita laudo com zero problemas: não exige cota de críticas. | • O laudo completo é longo para trechos curtos.<br>• O atrito fixo em 4 de 5 pode cansar em conversas exploratórias. |

| Oportunidades | Ameaças |
|---|---|
| • O formato de laudo pode ser usado em pareceres de periódico e em leitura de banca.<br>• Combina com reductio-ad-absurdum quando o diagnóstico é falha lógica. | • O "teste de correção mínima" pode escorregar para reescrever o texto de terceiro. |

## Fluxo

```mermaid
flowchart TD
    A["Trecho de terceiro<br>+ leitura do usuário, se houver"] --> B["1. Delimitar: afirmação textual,<br>inferência, atribuição, contexto externo"]
    B --> C["2. Reconstrução mais forte"]
    C --> D["3. Testar só as dimensões relevantes"]
    D --> E["4. Classificar: 11 categorias de diagnóstico"]
    E --> F["5. Auditar a leitura do usuário"]
    F --> G["6. Veredito local + impacto + confiança"]
    G --> H["Laudo: veredito global + limites"]
    G -. "opcional" .-> I["Teste de correção mínima"]
```
