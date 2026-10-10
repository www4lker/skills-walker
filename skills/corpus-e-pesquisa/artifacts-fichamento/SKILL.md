---
name: artifacts-fichamento
description: "Processa Artifacts do NotebookLM (.md) de um corpus de pesquisa e gera fichamentos críticos prontos para integração na pasta de fichamentos do projeto. Use quando o usuário fornecer um Artifact específico ou pedir para processar material de um notebook temático."
---

Esta skill converte Artifacts do NotebookLM em fichamentos críticos
integrados à pesquisa descrita em <PESQUISA: título, programa, eixos>.

REGRA DE LEITURA:
Ler apenas arquivos .md dentro de pastas /Artifacts/.
Nunca abrir /Sources/ — são HTMLs massivos.
Ignorar .wav, .mp4, .json não-Markdown.

LOCALIZAÇÃO DO CORPUS (preencher):
Primário:   <CAMINHO_DO_CORPUS>/
Adicional:  <CAMINHO_DO_EXPORT_ADICIONAL>/   (opcional)

NOTEBOOKS COM .md UTILIZÁVEIS (prioridade alta — preencher):
- <notebook>/Artifacts/

NOTEBOOKS SEM .md (não processar via esta skill — preencher):
- <notebook> — <apenas .wav | sem Artifacts>

AO PROCESSAR UM ARTIFACT:

1. IDENTIFICAÇÃO
- Notebook de origem e título do Artifact
- Tipo: [síntese teórica | análise empírica | guia de estudos |
  mapeamento de pressupostos | briefing | relatório técnico]

2. VERIFICAR REFERÊNCIAS ABNT
Se o Artifact já contém seção de referências: extrair e preservar.
Se não contém: registrar "sem referências — verificar Source original".

3. FICHAMENTO
Salvar em:
<PASTA_DE_FICHAMENTOS>/notebooklm/[notebook-abrev]_[titulo-curto].md

Esquema:
---
tipo: fichamento-artifact
notebook_origem:
artifact_titulo:
tipo_artifact:
data_processamento:
eixo_pesquisa: [<eixos do projeto>]
hipoteses_afetadas: [<H1…Hn> | nenhuma]
referencias_abnt_presentes: [sim | não | parcial]
---

## Argumento central
[Tese principal do Artifact em uma frase]

## Utilizável para a pesquisa
[Máximo 3 contribuições concretas. Para cada uma:
indicar se requer verificação na Source primária]

## Referências ABNT (se presentes no Artifact)
[Copiar integralmente da seção de referências do Artifact]

## Alerta crítico
[Onde o Artifact harmoniza tensões que deveriam permanecer abertas.
Paradoxos resolvidos artificialmente. Afirmações sem fonte citada.]

## Conexão com as hipóteses
[Qual hipótese este material sustenta, fragiliza ou ignora]

## Lacuna
[O que o Artifact não responde. Requer consulta à Source original?]

4. GIT (se o projeto versionar fichamentos)
git add <PASTA_DE_FICHAMENTOS>/notebooklm/[arquivo]
git commit -m "fichamento-artifact: [notebook-abrev] - [titulo-curto]"

5. LOG
Registrar com tipo [referência] e aguardar [aceito|editado|rejeitado].

RESTRIÇÃO: Artifacts são sínteses geradas pelo NotebookLM, não pelo
pesquisador. Nunca tratar como citação direta. Sempre rastrear até a
Source primária antes de usar no texto.
