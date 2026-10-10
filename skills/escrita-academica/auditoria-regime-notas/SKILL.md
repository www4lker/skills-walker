---
name: "auditoria-regime-notas"
description: "Audita as notas de rodapé de um capítulo de tese ou dissertação contra o regime corpo/nota declarado e aponta só as que o violam. Use para revisar ou auditar notas, ou quando alguém perguntar se há notas demais."
---

# Auditoria do regime de notas

## Propósito

O capítulo usa muitas notas por escolha metodológica: elas tornam visível a pressão epistêmica numa escrita autoetnográfica. O regime corpo/nota está declarado no corpo do texto. Esta skill **não reduz notas**. Ela encontra as notas que contrariam o regime declarado ou que vão diretamente contra as recomendações mais úteis das fontes. A banca pode aceitar uma nota abundante, mas não perdoa uma regra declarada e descumprida.

**Saída:** um relatório que lista **apenas** as notas sinalizadas. Notas conformes aparecem só na contagem.

## O regime (fonte de verdade)

Se existir `declaracao-regime-notas.md` ou se a declaração já estiver no `.tex`, leia essa versão primeiro. Onde ela divergir do texto abaixo, **vale a declaração**, e a divergência deve ser registrada no relatório.

**CORPO:** tese, inferência do pesquisador e toda qualificação que altera a força da tese.

**NOTA:** quatro funções:

1. **Infraestrutura conceitual:** define um conceito que o argumento usa sem discutir. Exemplo: a definição de um termo técnico que o capítulo usa mas não discute.
2. **Melhor argumento localizado de uma fonte:** resume o argumento mais forte de um autor para o movimento que o corpo faz. Por isso um autor pode estrear em nota.
3. **Objeção antecipada:** registra a crítica no ponto em que ela incide (Eco: corrigir ou qualificar quando se sabe que alguém discordaria).
4. **Caminho não tomado:** uma via que o pesquisador conhece e escolheu não transformar em eixo.

## As seis violações

Estas são as únicas categorias sinalizáveis. Não invente outras.

| Código | Violação | Teste | Base |
|---|---|---|---|
| **V1** | A nota carrega uma premissa necessária ao corpo | *Teste de apagamento.* Releia o parágrafo sem a nota. Se a afirmação do corpo vira uma asserção sem lastro **e** o capítulo se apoia nela adiante, é V1. Se o corpo apenas fica menos erudito, não é. | Critério de dispensabilidade (convergente em APA, Chicago e Eco) |
| **V2** | A nota qualifica a força da tese | A nota restringe, relativiza ou limita o alcance do que o corpo afirma ("isso vale apenas quando…", "a rigor, não se pode dizer que…"). O leitor que pula a nota fica com uma tese mais forte do que a que o pesquisador sustenta. | Regime (CORPO). Por isso, ressalvas que limitam a tese ficam no corpo. |
| **V3** | Resumo de fonte sem paginação quando a passagem é localizável | Ver "Regra de paginação" abaixo. | Grafton (a nota como prova verificável); regime, função 2 |
| **V4** | Autor que estreia em nota e vira interlocutor estrutural sem ser promovido ao corpo | O autor entra pela primeira vez numa nota e, em qualquer capítulo, passa a ser discutido no corpo (argumento dele retomado ou contestado, e não só citado de passagem) **sem** jamais ter sido apresentado no corpo. | Regime (função 2) |
| **V5** | Nota que é só uma lista de "cf." | Remete a obras sem resumir o argumento de nenhuma. Não exerce nenhuma das quatro funções. | Regime (a função 2 exige resumo) |
| **V6** | A nota abre uma tese nova | Introduz uma afirmação própria do pesquisador, sem ancoragem no movimento do corpo onde a nota está, e que não se reduz a objeção (3) nem a caminho não tomado (4). | Regime; recomendação "uma ideia por nota" (APA) |

### Regra de paginação (V3)

V3 **não** significa "toda nota sem página". Aplica-se só quando a nota:

- atribui a uma fonte uma **afirmação, um achado, um dado ou um argumento específico** (algo que o leitor precisaria localizar na obra para conferir); ou
- faz paráfrase próxima de uma passagem.

Não é V3 quando a nota remete à tese geral de uma obra, à proveniência de um termo (exemplo: "capitalismo de vigilância", Zuboff) ou paga uma dívida intelectual difusa. A NBR 10520 torna a página opcional na citação indireta.

Se a declaração do regime disser "**sempre** com paginação" e a prática for majoritariamente sem página, **não** sinalize nota por nota. Registre uma única vez, em "Achados sistêmicos", a divergência entre a declaração e a prática, e apresente as duas saídas:

- paginar as notas localizáveis; ou
- reformular a declaração, por exemplo: "com paginação sempre que o argumento resumido for localizável na obra".

## O que NÃO sinalizar

- Densidade ou quantidade de notas, inclusive várias notas no mesmo parágrafo. Isso só entra se houver redundância entre elas, e mesmo assim como observação, não como violação.
- Definições de termos técnicos de conhecimento comum sem fonte (exemplo: "commit"). A função 1 não exige autor.
- Ausência das funções 3 e 4 na prática. A declaração pode prever funções não exercidas.
- Estilo, extensão ou redação da nota, exceto quando a redação produz V2.
- Formatação ABNT de referências. Não é o objeto desta skill.

## Procedimento

### 0. Localizar insumos

Localize o `.tex` do capítulo, a declaração do regime e o inventário de calibragem, se existir (`inventario-notas-calibragem.md`).

Se houver inventário, reutilize a classificação de função, mas **reverifique** as notas cuja linha ou texto mudou desde a data dele.

### 1. Extrair as notas

Use o script abaixo. Ele faz casamento de chaves, ignora comentários `%` e preserva a numeração de linhas.

```python
# extrair_notas.py  —  uso: python extrair_notas.py cap.tex [--body-only]
import re, sys, json, pathlib

def strip_comments(s):
    return '\n'.join(re.sub(r'(?<!\\)%.*$', '', l) for l in s.split('\n'))

def close_brace(s, i):
    depth = 1
    while i < len(s):
        c = s[i]
        if c == '\\': i += 2; continue
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0: return i
        i += 1
    raise ValueError('chave não fechada')

src = strip_comments(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
spans, notes = [], []
for m in re.finditer(r'\\footnote(?:\[[^\]]*\])?\{', src):
    end = close_brace(src, m.end())
    spans.append((m.start(), end + 1))
    notes.append({'n': len(notes) + 1,
                  'linha': src.count('\n', 0, m.start()) + 1,
                  'texto': src[m.end():end].strip()})

def sem_notas(a, b):
    out, k = [], a
    for s, e in spans:
        if e <= a or s >= b: continue
        out.append(src[k:s]); k = e
    out.append(src[k:b]); return ''.join(out)

if '--body-only' in sys.argv:
    print(sem_notas(0, len(src))); sys.exit()

for note, (s, e) in zip(notes, spans):
    a = max(src.rfind('\n\n', 0, s), 0)
    b = src.find('\n\n', e); b = len(src) if b == -1 else b
    note['ancora'] = sem_notas(a, s)[-300:].strip()
    note['paragrafo_sem_notas'] = ' '.join(sem_notas(a, b).split())
print(json.dumps(notes, ensure_ascii=False, indent=1))
```

Antes de julgar a paginação, abra o preâmbulo e leia as definições das macros de citação do projeto (por exemplo, `\cite` com opções de página ou macros próprias) para saber qual argumento carrega a página. Se não conseguir determinar, trate a paginação como "indeterminada" e **não** sinalize V3.

A numeração do script segue a ordem no arquivo. Se a do PDF for diferente, informe sempre a linha do `.tex`.

### 2. Aplicar os testes

Para cada nota:

1. Classifique a função (1–4 ou "outra").
2. Aplique V1 → V6 nessa ordem.
3. Para V1, execute de fato o teste de apagamento usando `paragrafo_sem_notas`, e verifique se o capítulo retoma a afirmação adiante.
4. Para V4, rode `--body-only` em **todos** os capítulos e procure o sobrenome e a chave bibliográfica do autor.
   - É V4 se o autor é discutido no corpo e nunca foi apresentado nele.
   - Citação de passagem no corpo não conta como apresentação estrutural nem como discussão.

Cada nota recebe um de três graus:

- **violação:** o teste falha claramente e você consegue citar o trecho que prova isso;
- **limítrofe:** o teste é ambíguo. Explique por quê, em uma frase;
- **conforme:** não aparece no relatório.

Na dúvida entre violação e limítrofe, escolha **limítrofe**. Um falso positivo custa mais do que um limítrofe honesto, porque empurra o pesquisador a mexer em nota defensável.

### 3. Freio de calibragem

Se mais de ~30% das notas saírem como violação, **pare antes de listar**. Reexamine se o problema está nas notas ou no regime/declaração (uma regra formulada de modo estrito demais para a prática que ela descreve). Se for isso, reporte-o como achado sistêmico e liste só os casos mais claros.

## Formato do relatório

Salve como `auditoria-notas-<capitulo>-<AAAA-MM-DD>.md`. Datas no texto em DD/MM/AA.

```
# Auditoria do regime de notas — <capítulo> — <DD/MM/AA>
Fonte: <arquivo .tex>, <n> notas · Regime: <declaração usada + divergências, se houver>

## Resumo
<n> conformes · <n> violações · <n> limítrofes

## Notas sinalizadas
### Nota <n> (linha <l>) — <V#> · <violação|limítrofe>
- Trecho: "<até 2 linhas da nota>" / âncora no corpo: "<até 1 linha>"
- Por que: <1–3 frases, teste aplicado + base>
- Opções: <2–3 saídas concretas, p. ex. promover a frase X ao corpo;
  reescrever a nota como função 3; paginar; manter e defender assim: "...">

## Achados sistêmicos
<padrões que atravessam várias notas, registrados uma única vez;
divergência declaração × prática>

## Registro de processo
<modelo/agente que executou; o que foi classificado automaticamente;
o que depende do julgamento do pesquisador>
```

Em "Opções", inclua sempre **"manter e defender"** quando for defensável, com a frase de defesa pronta. Cortar a nota é uma opção entre outras, nunca a recomendação padrão.

## Restrições duras

- Não edite o `.tex` nem nenhum arquivo do capítulo. A saída é só o relatório.
- Não invente paginação, edição ou passagem. Se precisar de uma página que não tem, escreva `[VERIFICAR]`.
- Não use como fonte relatórios do NotebookLM sem conferir o original. Esses relatórios podem confabular uma tradição inteira a partir de uma descrição de catálogo.
- Não sinalize nada fora das seis categorias.
- Sem hedging ornamental. Cada sinalização cita o trecho que a sustenta.