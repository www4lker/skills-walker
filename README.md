# Skills de pesquisa em humanidades para Claude

Coleção de 27 skills escritas para trabalho de pesquisa acadêmica com o Claude: protocolos de raciocínio, estilos de resposta, revisão de escrita acadêmica, navegação de corpus e algumas ferramentas.

Elas nasceram dentro de um projeto de dissertação real. As que dependiam desse projeto foram **generalizadas**: nomes, caminhos e dados do projeto viraram placeholders (`<...>`, `$CORPUS`, `$VAULT`), e algumas trazem um bloco "preencher" que precisa ser adaptado antes do primeiro uso.

Cada pasta tem dois arquivos:

- `SKILL.md`: a skill propriamente dita.
- `ANALISE.md`: uma análise SWOT curta e, nas skills mais complexas, um fluxograma em Mermaid.

As ligações entre skills estão em [docs/cadeias.md](docs/cadeias.md).

## Índice

### Protocolos de raciocínio

| Skill | O que faz | Complexidade |
|---|---|---|
| [auditoria-causal-sistemica](skills/protocolos-de-raciocinio/auditoria-causal-sistemica/) | Audita cadeias causais de uma decisão e marca os elos fracos | alta |
| [reductio-ad-absurdum](skills/protocolos-de-raciocinio/reductio-ad-absurdum/) | Extremiza premissas e separa contradição de desconforto | alta |
| [contraprova](skills/protocolos-de-raciocinio/contraprova/) | Compara às cegas a resposta do Claude com a de um modelo externo (API paga) | alta |
| [invariancia-politica](skills/protocolos-de-raciocinio/invariancia-politica/) | Responde de forma invariante à ideologia declarada, sem modelo externo | baixa |

### Estilos de resposta

| Skill | O que faz | Complexidade |
|---|---|---|
| [auditor-argumentativo-style](skills/estilos-de-resposta/auditor-argumentativo-style/) | Laudo adversarial sobre texto de terceiro e sobre a leitura do usuário | alta |
| [diletante-empatico](skills/estilos-de-resposta/diletante-empatico/) | Preparação personalizada para a defesa a partir de um perfil de personalidade | alta |
| [auditor-pesquisa-style](skills/estilos-de-resposta/auditor-pesquisa-style/) | Assistente de pesquisa com modos de resposta e disciplina de evidência (molde) | média |
| [analista-rigoroso-style](skills/estilos-de-resposta/analista-rigoroso-style/) | Equilíbrio entre perguntar e responder, por domínio | baixa |
| [analista-sistemico-style](skills/estilos-de-resposta/analista-sistemico-style/) | Efeitos de 1ª, 2ª e 3ª ordem (versão anterior da auditoria causal) | baixa |
| [blind-spot-detective-style](skills/estilos-de-resposta/blind-spot-detective-style/) | Busca pontos cegos com lentes interdisciplinares | baixa |
| [diletante-style](skills/estilos-de-resposta/diletante-style/) | Perfil de interlocutor e padrões epistêmicos | baixa |
| [eu-sabo-style](skills/estilos-de-resposta/eu-sabo-style/) | Aconselhamento com TCC e filosofia (template em inglês) | baixa |
| [parceiro-de-aula-ao-vivo](skills/estilos-de-resposta/parceiro-de-aula-ao-vivo/) | Acompanha aula ao vivo a partir de fragmentos, sem interpretar demais | baixa |

### Escrita acadêmica

| Skill | O que faz | Complexidade |
|---|---|---|
| [revisar-clareza](skills/escrita-academica/revisar-clareza/) | Revisão de clareza com arbitragem de tensões entre autores | alta |
| [auditar-citacoes](skills/escrita-academica/auditar-citacoes/) | Confere se a fonte diz o que o texto diz que ela diz | alta |
| [auditoria-regime-notas](skills/escrita-academica/auditoria-regime-notas/) | Aponta só as notas de rodapé que violam o regime declarado | alta |
| [simular-banca](skills/escrita-academica/simular-banca/) | Encena os examinadores de uma banca | alta |
| [simular-pesquisador](skills/escrita-academica/simular-pesquisador/) | Treinador socrático: aponta o texto, não responde | média |
| [testar-arbitragem-clareza](skills/escrita-academica/testar-arbitragem-clareza/) | Testa adversarialmente as arbitragens de revisar-clareza | média |
| [titular](skills/escrita-academica/titular/) | Cinco opções de título para qualquer nível do trabalho | média |
| [quem-fala](skills/escrita-academica/quem-fala/) | Separa, em texto feito com IA, a voz da fonte, a do pesquisador e a do modelo | média |

### Corpus e pesquisa

| Skill | O que faz | Complexidade |
|---|---|---|
| [corpus-search](skills/corpus-e-pesquisa/corpus-search/) | Busca em corpus exportado do NotebookLM, com grep em 4 camadas | alta |
| [gemini-source-extractor](skills/corpus-e-pesquisa/gemini-source-extractor/) | Extração bibliográfica delegada ao Gemini (experimental) | alta |
| [artifacts-fichamento](skills/corpus-e-pesquisa/artifacts-fichamento/) | Fichamento crítico de Artifacts do NotebookLM | média |
| [navegacao-corpus](skills/corpus-e-pesquisa/navegacao-corpus/) | Índice estático do corpus, sem abrir arquivos | baixa |

### Ferramentas

| Skill | O que faz | Complexidade |
|---|---|---|
| [gemini-delegate](skills/ferramentas/gemini-delegate/) | Delega ao Gemini CLI tarefas de texto com muita entrada e pouca saída | média |
| [frontend-skill](skills/ferramentas/frontend-skill/) | Páginas de arquivo único para apresentar conhecimento | média |

## Como a complexidade foi definida

Três critérios, e basta um deles em grau alto para a skill ser classificada como alta:

1. **Estrutura:** número de fases, condicionais e ordens obrigatórias.
2. **Dependências:** scripts, ferramentas externas, APIs e outras skills.
3. **Estado:** arquivos que a skill cria ou lê entre sessões (registros, perfis, notas).

Toda skill de complexidade alta tem um fluxograma: no próprio `ANALISE.md` ou, quando funciona em conjunto com outras, nos diagramas de [docs/cadeias.md](docs/cadeias.md).

## Marcas epistêmicas

Várias skills usam estas marcas:

| Marca | Significado |
|---|---|
| `[V]` | Verificado diretamente: arquivo, comando, teste, Git ou fonte externa |
| `[I]` | Inferência, com evidência incompleta |
| `[H]` | Hipótese ainda não testada |
| `[D]` | Decisão humana registrada |

## Como instalar

Copie a pasta da skill (a pasta inteira, não só o `SKILL.md`) para um destes lugares:

- `.claude/skills/` dentro de um projeto, para usar só nele;
- `~/.claude/skills/`, para usar em todos os projetos.

```bash
cp -r skills/protocolos-de-raciocinio/auditoria-causal-sistemica ~/.claude/skills/
```

Antes de usar, procure por `<` e por `preencher` no `SKILL.md`. Os blocos marcados precisam ser adaptados ao seu projeto.

Algumas skills precisam de mais coisas:

- **contraprova:** Python 3 e uma chave da API do DeepSeek em `DEEPSEEK_API_KEY` ou num `.env` dentro da pasta da skill. Cada uso faz chamadas pagas.
- **gemini-delegate** e **gemini-source-extractor:** Gemini CLI instalado e autenticado.

Nunca versione arquivos `.env`. O `.gitignore` deste repositório já os exclui.

## O que ficou de fora e por quê

- **Skills de terceiros** que estavam instaladas junto com estas, como as de Obsidian, as de Hugo, as oficiais da Anthropic e outras skills de design. Elas pertencem aos seus autores.
- **Skills presas ao projeto de origem:** dependem de scripts, pastas ou dados que só existem nele e perderiam o sentido se fossem generalizadas.

## Licença

[CC BY 4.0](LICENSE). Você pode copiar, adaptar e redistribuir, inclusive para uso comercial, desde que dê o crédito.

Crédito sugerido: "Skills de pesquisa em humanidades para Claude, por W. ([www4lker](https://github.com/www4lker)), CC BY 4.0".
