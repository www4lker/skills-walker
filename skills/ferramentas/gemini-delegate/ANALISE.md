# gemini-delegate — análise

**Complexidade:** média — dois scripts (prompt único e batch sobre CSV)

| Forças | Fraquezas |
|---|---|
| • Economiza tokens: só o resultado compacto volta ao contexto do Claude.<br>• O batch sobre CSV é retomável. | • Só texto: o CLI não tem visão.<br>• No batch, as linhas que falham não são tentadas de novo automaticamente.<br>• Os scripts não foram executados na preparação deste repositório. |

| Oportunidades | Ameaças |
|---|---|
| • Pode servir de base para delegar a outros modelos de contexto longo. | • Mudanças no Gemini CLI quebram os scripts. |

## Nota

Requer Gemini CLI e chave em `.env`. Veja o padrão de delegação em [docs/cadeias.md](../../../docs/cadeias.md).
