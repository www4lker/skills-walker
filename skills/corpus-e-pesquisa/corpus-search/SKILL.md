---
name: corpus-search
description: "Busca direta num corpus exportado do NotebookLM usando protocolo grep de 4 camadas. Executa na sessão principal do Claude Code — sem subagente. Use quando o pesquisador precisa localizar Artifacts relevantes para o referencial teórico, as hipóteses ou qualquer conceito da pesquisa. Exige caminhos e mapa do corpus preenchidos."
---

Esta skill executa busca no corpus NotebookLM diretamente na sessão atual do Claude Code.
Sem subagente. Sem overhead. Os comandos bash rodam na sessão principal.

## AMBIENTE (preencher)

Use sempre caminhos absolutos. Em WSL ou máquinas com mais de um usuário, `~`
pode apontar para outro lugar que não os arquivos.

**Verificar antes de qualquer operação:**
```bash
ls "$CORPUS" | head -3
```
Se falhar: parar e reportar ao pesquisador. Não tentar caminhos alternativos.

| Referência | Variável | Caminho |
|---|---|---|
| Corpus | `$CORPUS` | `<CAMINHO_ABSOLUTO_DO_CORPUS>` |
| Vault | `$VAULT` | `<CAMINHO_ABSOLUTO_DO_VAULT>` |
| Destino notas | `$DESTINO` | `$VAULT/<PASTA_DE_NOTAS_REFERENCIAIS>` |

---

## CONTEXTO DA PESQUISA (preencher)

**Título:** "<título>"

**Eixos:** <um por linha, com o que cada um mede ou discute>

**Hipóteses:** <H1 (…) · H2 (…) · …>

**Conceitos centrais:** <lista>

---

## MAPA DE NOTEBOOKS (preencher)

Agrupe os notebooks por eixo, como na skill `navegacao-corpus`:

```
<Eixo 1>/
  <nome do notebook>/
<Eixo 2>/
  <nome do notebook>/
Transversal/
  <nome do notebook>/
```

### NÃO PROCESSAR
- Pastas marcadas como descontinuadas (ex.: prefixo `(deprecado)`)
- Qualquer pasta `Sources/` — HTMLs massivos, nunca abrir especulativamente
- Notebooks só com `.wav`

---

## PROTOCOLO DE BUSCA — 4 CAMADAS

**Regra absoluta:** nunca ler arquivo sem confirmar relevância via grep primeiro.

### Camada 1 — Localização (grep -ril)
Retorna apenas paths. Custo zero de conteúdo.
```bash
LC_ALL=C.UTF-8 grep -ril "TERMO" \
  "$CORPUS/NOTEBOOK/Artifacts/" \
  2>/dev/null | grep "\.md$"
```

**Variações obrigatórias por conceito** (preencha as do seu projeto; exemplo
de origem):
- parrésia → `parr`, `franc-parler`, `coragem da verdade`, `veridicção`, `dizer-a-verdade`
- ANT → `Latour`, `actante`, `translação`, `ator-rede`, `caixa-preta`
- threshold → `limiar`, `binário`, `classificação`, `threshold`

A lista de variações é o que mais pesa na qualidade da Camada 1: grep não
conhece sinônimo, tradução nem flexão.

### Camada 2 — Contexto (grep -n -A 3)
Para cada arquivo confirmado na Camada 1, extrair linhas relevantes:
```bash
LC_ALL=C.UTF-8 grep -n -A 3 -i "TERMO" "PATH_COMPLETO/arquivo.md" 2>/dev/null
```
Processar no máximo 5 arquivos por query. Parar ao ter contexto suficiente.

### Camada 3 — Leitura seletiva (Read)
Somente se Camada 2 confirmar conteúdo suficientemente relevante.
Usar `offset` e `limit` — nunca ler arquivo inteiro se for longo.
Máximo 3 leituras completas por query.

### Camada 4 — Extração bibliográfica (APENAS sob demanda explícita)
Ativar somente quando o pesquisador confirmar que uma Source específica precisa de BibTeX.

**Sub-camada 4a — JSON metadata (custo zero, sempre primeiro):**
```bash
cat "$CORPUS/NOTEBOOK/Sources/NOME_EXATO.json"
```
O campo `title` frequentemente codifica: `[título] -- [autor] -- [ed, cidade, ano] -- [ISBN]`
Se contiver autor + ano + ISBN → parar aqui.

**Sub-camada 4b — Referências de artigos (tail read):**
Artigos têm referências no FINAL do HTML:
```bash
LC_ALL=C.UTF-8 grep -ni "References\|Referências\|doi\.org" "Sources/arquivo.html" | tail -5
tail -n +LINHA "Sources/arquivo.html" | sed 's/<[^>]*>//g' | grep -v "^[[:space:]]*$" | head -60
```

**Sub-camada 4c — Ficha de livros (head read):**
Livros têm dados bibliográficos no INÍCIO:
```bash
head -120 "Sources/arquivo.html" | sed 's/<[^>]*>//g' | grep -v "^[[:space:]]*$" | head -40
```
Se os 120 primeiros não contiverem título + autor + ano → parar, reportar ao pesquisador.

---

## FORMATO DE RETORNO DA BUSCA

Para cada Artifact relevante encontrado:

```
📄 NOME DO ARQUIVO
📁 Notebook: [nome]
🎯 Eixo: [<eixos do projeto> | transversal]
🔗 Path: [path completo]
💡 Trecho: "[linha(s) do grep -n]"
```

Ao final:
- Quantos notebooks buscados / quantos Artifacts encontrados
- Lacuna detectada (se nenhum Artifact cobrir adequadamente o conceito)
- Pergunta: "Criar notas na pasta de notas referenciais para quais destes?"

---

## CRIAÇÃO DE NOTAS NO VAULT (handoff — segundo turno)

Quando o pesquisador confirmar quais Artifacts devem virar notas:

### Convenção de nomenclatura
```
[TEMA]-[NN]-[descricao-curta].md
```
Exemplos: `CONCEITO-04-descricao-curta.md` · `AUTOR-02-tema-da-nota.md`

**Verificar o maior número existente antes de criar:**
```bash
ls "$DESTINO/" | grep "^TEMA-" | sort | tail -3
```

### Frontmatter obrigatório
```yaml
---
projeto: "[<Eixo> — Referencial Teórico | Transversal — Referencial Teórico]"
eixo: "[<Eixo> | Transversal]"
funcao: "[Uma frase: o que este Artifact contribui para o argumento da pesquisa]"
prioridade-fichamento: [1 | 2 | 3]
tipo: artifact-referencial
status: para-fichar
alias: ["[Nome curto para wikilink]"]
tags:
  - referencial-teorico
  - [<eixo>]
  - [conceito-principal]
  - [conceito-secundario]
relacionado: "[[MAPEAMENTO-REFERENCIAL-TEORICO]]"
---
```

### Conteúdo da nota
Após o frontmatter: colar o conteúdo completo do Artifact `.md` de origem.
Não resumir, não parafrasear — o conteúdo completo preserva fidelidade para fichamento posterior.

### Comando de criação
```bash
cat > "$DESTINO/TEMA-NN-descricao.md" << 'EOF'
[frontmatter + conteúdo]
EOF
```

### Git após criação
```bash
cd "<RAIZ_DO_REPOSITORIO>"
git add "$DESTINO/ARQUIVO.md"
git commit -m "feat(referencial): adiciona artifact [TEMA] às notas referenciais"
```

---

## RESTRIÇÃO EPISTEMOLÓGICA

Artifacts são sínteses geradas pelo NotebookLM (Gemini) — não são fontes primárias.
- Nunca tratar como citação direta no texto
- Sempre rastrear até a Source primária antes de usar
- Sinalizar quando Artifact faz afirmação sem citar fonte
- A nota referencial é material de trabalho, não referência final

---

## VERIFICAÇÃO FINAL

Antes de retornar qualquer resultado:
1. ✅ Usei `LC_ALL=C.UTF-8` nos greps?
2. ✅ Usei caminho absoluto (não `~`)?
3. ✅ Não abri nenhum `Sources/` sem confirmação explícita?
4. ✅ Camada 4 ativada só após pedido explícito de BibTeX?
5. ✅ Máximo 3 leituras completas de Artifacts?
6. ✅ Frontmatter da nota segue a convenção da pasta de notas referenciais?
7. ✅ Git commit sugerido ao final da criação de notas?
