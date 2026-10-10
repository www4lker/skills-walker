---
name: gemini-source-extractor
description: "Skill experimental: delega extração bibliográfica ao Gemini CLI. Use quando o pesquisador confirmar que uma Source específica precisa de dados completos (título, autor, editora, ano, ISBN) + citações relevantes, sem tentar head/tail manualmente no HTML."
---

Claude orquestra, Gemini extrai Sources HTML.

## Objetivo

Teste de uma arquitetura multiagente em que o Claude orquestra e o Gemini lê.
Em vez de usar as subcamadas 4a (JSON) e 4b (tail grep) da skill `corpus-search`, delegar o arquivo HTML inteiro para Gemini extrair dados bibliográficos completos + passagens sobre um conceito.

## Quando usar

Pesquisador: "Quero o BibTeX completo para a Source 'A hermenêutica do sujeito' E quero as passagens que falam sobre cuidado de si."

Claude: em vez de `head -120 | sed ...`, passa o arquivo inteiro para Gemini via CLI.

## Pré-requisitos

- Gemini CLI instalado e testado (`gemini --help` funciona)
- Path da Source confirmada
- Conceito-alvo de busca identificado

## Fluxo

### Etapa 1 — Confirmar Gemini e o corpus

```bash
# Verificar Gemini
gemini --version 2>/dev/null || echo "ERRO: Gemini CLI não encontrado"

# Caminho absoluto do corpus (preencher)
CORPUS_PATH="<CAMINHO_ABSOLUTO_DO_CORPUS>"
[ -d "$CORPUS_PATH" ] || echo "CORPUS NÃO ENCONTRADO — PARAR"
```

### Etapa 2 — Passar Source HTML inteiro para Gemini

```bash
NOTEBOOK="<nome do notebook>"
SOURCE_FILE="<arquivo da source>.html"
CONCEPT="cuidado de si"

gemini -p "
Você receberá um arquivo HTML com conteúdo de um livro ou artigo acadêmico.

Tarefa:
1. Extraia os dados bibliográficos: Título (exato), Autor(es), Editora, Ano de publicação, ISBN (se houver)
2. Localize e retorne 3-5 passagens que mencionem ou explicam o conceito de '$CONCEPT'
3. Para cada passagem: inclua o contexto (parágrafos vizinhos) e aproximadamente a localização no documento

Formato de retorno:
---
## Dados Bibliográficos
Título:
Autor(es):
Editora:
Ano:
ISBN:

## Passagens sobre $CONCEPT
### Passagem 1
[Contexto + citação]

### Passagem 2
[Contexto + citação]
---
" < "$CORPUS_PATH/$NOTEBOOK/Sources/$SOURCE_FILE"
```

### Etapa 3 — Claude sintetiza output + cria BibTeX

Depois que Gemini retorna:

```bash
# (Claude lê o output da Etapa 2)
# Claude então cria entrada BibTeX:

cat > "/tmp/bib_temp.bib" << 'EOF'
@book{Foucault2006,
  author = {[extraído do Gemini]},
  title = {[extraído do Gemini]},
  publisher = {[extraído do Gemini]},
  year = {[extraído do Gemini]},
  isbn = {[extraído do Gemini]}
}
EOF

# Claude move para local permanente se validado
# E cria nota na pasta de notas referenciais com as citações marcadas como [[wikilinks]]
```

## Checklist antes de executar

- ✅ Path para Source confirmado?
- ✅ `gemini --version` retorna versão?
- ✅ Arquivo Source existe em `$CORPUS_PATH/$NOTEBOOK/Sources/$SOURCE_FILE`?
- ✅ Conceito-alvo está bem definido?

## Monitoramento

Log de execução:
```
[TIMESTAMP] Gemini start: $SOURCE_FILE
[TIMESTAMP] Gemini retornou: [bytes]
[TIMESTAMP] BibTeX criado: [caminho]
[TIMESTAMP] Nota vault: [arquivo]
```

## Limitações conhecidas

1. **Encoding HTML:** Gemini pode ter dificuldade com HTML muito complexo ou mal-formatado. Se retornar "não consegui processar", tentar limpar HTML antes:
   ```bash
   sed 's/<[^>]*>//g' "SOURCE.html" | head -5000 | gemini -p "..."
   ```

2. **Tamanho de arquivo:** Se o HTML > 50MB, dividir em chunks antes de passar para Gemini.

3. **Conceitos abstratos:** Se o conceito-alvo é muito abstrato (ex.: um conceito que o próprio autor nunca nomeia), Gemini pode não encontrar. Usar variações: `"cuidado de si", "tecnologias do eu", "ascese"`.

## Próximos passos após teste bem-sucedido

1. Integrar em um fluxo completo onde Claude chama Gemini sistematicamente para todas as Sources marcadas como "precisa de BibTeX completo"
2. Criar uma pasta de fichamentos/extrações brutas do Gemini para armazenar outputs brutos do Gemini antes da síntese final
3. Adicionar comando de log estruturado para rastreabilidade acadêmica
