# gemini-source-extractor — análise

**Complexidade:** alta — delegação a ferramenta externa, três etapas, validação manual

| Forças | Fraquezas |
|---|---|
| • Usa a janela longa do Gemini para ler HTMLs inteiros sem gastar contexto do Claude. | • É experimental e não foi validada; a própria skill diz isso.<br>• Depende do Gemini CLI instalado e autenticado. |

| Oportunidades | Ameaças |
|---|---|
| • Se validada, automatiza a parte mais tediosa da bibliografia. | • O Gemini pode inventar metadados; sem conferência, a entrada BibTeX herda o erro. |

## Nota

O diagrama está em [docs/cadeias.md](../../../docs/cadeias.md), no padrão de delegação ao Gemini.
