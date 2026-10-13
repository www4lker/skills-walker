---
name: quem-fala
description: Separa, num texto de pesquisa, o que dizem as fontes, o que o pesquisador assumiu e o que a IA propôs ou deixou de fora. Use sempre que for redigir, revisar ou auditar trecho de artigo, dissertação ou relatório acadêmico em que um modelo de linguagem tenha redigido, selecionado, resumido, transcrito ou conferido material, mesmo que o pedido não fale em viés ou autoria (por exemplo "audita a seção 4", "rascunha o parágrafo a partir das fontes", "faz o resumo", "confere se o texto bate com as transcrições"). Use também quando o pesquisador perguntar se está sendo enviesado pela IA. Não use em conversa sem texto de pesquisa, nem em código.
---

# Quem fala

Em cada passagem de um texto de pesquisa feito com IA, pergunte:

> **Quem fala aqui, e alguém humano assumiu isso?**

O motivo: a IA produz efeitos no texto sem responder por eles. Ela seleciona, ordena,
escolhe verbos, generaliza e omite. Se essas escolhas passam sem marca, viram voz do
pesquisador sem que ele as tenha assumido.

Procure as duas direções de viés:

- **Complacência:** o modelo reforça o enquadramento do pesquisador. Foi o viés
  dominante nas auditorias que deram origem a esta skill.
- **Interesse do instrumento:** o modelo é produto de uma empresa com interesses
  próprios e pode atenuar o que contraria esses interesses.

## As quatro marcas

| Marca | O que é | Quem responde |
|---|---|---|
| `[fonte]` | O que a fonte diz (documento, fala, dado). Dá para conferir | A fonte, e o pesquisador por tê-la conferido |
| `[artigo]` | Leitura que o pesquisador assumiu: a voz dele | O pesquisador |
| `[modelo]` | Leitura proposta pela IA e ainda não assumida | Ninguém, até ser assumida ou descartada |
| `[omissão]` | O que estava no material e a IA deixou de fora | O pesquisador, depois que vê |

As marcas ficam em comentário (`%` no LaTeX, `<!-- -->` no Markdown). Elas nunca
aparecem no texto final.

**Só o pesquisador converte `[modelo]` em `[artigo]`.** Autoria é o ato de assumir, e
não o de digitar.

Se o projeto usa marcação epistemológica (`[V]` verificado, `[I]` inferido, `[H]`
hipótese, `[D]` decisão humana), use as duas juntas. Uma diz o estado da evidência, a
outra diz de quem é a voz.

## Ao redigir

1. Antes de escrever, diga o que foi delegado a você e com quais fontes.
2. Marque como `[modelo]` toda leitura sua.
3. Não use fórmulas como "deste artigo", "defendemos" ou "nossa leitura" para uma
   leitura sua. Elas apresentam como do autor algo que ninguém assumiu.
4. Não redija conclusão, resumo nem síntese antes de o pesquisador escrever a dele.
   O rascunho ancora a conclusão. Se ele pedir mesmo assim:
   - avise do efeito de ancoragem;
   - marque o trecho inteiro como `[modelo]`.
5. Siga as regras locais de prosa. Onde um agente não pode escrever prosa, tudo o que
   você produz vai em comentário.

## Ao auditar

1. **Não altere a prosa.** A auditoria só acrescenta comentários, porque decidir
   cabe ao pesquisador. No fim, confira que a prosa ficou idêntica: compare com a
   versão anterior ignorando comentários e linhas em branco.
2. **Volte às fontes,** e não só ao rascunho. A omissão só aparece nas fontes.
3. **Diga a direção** de cada leitura `[modelo]`: ela reforça o enquadramento do
   pesquisador ou o atenua?
4. **Registre também o puxão que veio do pesquisador** (`[D]`). Nem todo viés vem da
   IA.
5. **Diga quem responde** por cada escolha: a fonte, o pesquisador, ou o modelo e a
   empresa que o treinou. Não escreva "a IA enviesou o texto", porque a IA não é
   sujeito responsável. Diga três coisas:
   - qual escolha apareceu;
   - em qual camada: transcrição, curadoria, redação ou checagem;
   - quem responde por ela.

Sinais que já apareceram em rascunhos auditados:

- verbos que endossam a fala de um lado ("lembrou", "advertiu", "revelou") ao lado de
  verbos neutros para o outro ("afirmou", "pediu");
- a condição de uma fala apagada, de modo que um "se" vira afirmação;
- falas de dias ou contextos diferentes montadas como diálogo;
- generalização de escala: um caso vira "outros países";
- uma fala transformada em fato;
- uma frase final sem fonte que fecha o argumento;
- vozes ausentes, como governo, empresas ou órgão licenciador;
- interesse declarado só para um dos lados;
- um fechamento que contradiz o que a própria seção mostra.

### Formato do registro

Ponha um bloco no topo do arquivo auditado:

```
% AUDITORIA DE POSICIONAMENTO (<modelo>, <data>)
% Marcas: [fonte] [artigo] [modelo] [omissão]
% Limite: autoauditoria do mesmo modelo; contraprova pendente.
% Achados gerais:
% 1. [modelo] <escolha> -- direção: reforça|atenua -- responde: <quem>
```

Ponha um bloco curto sob cada parágrafo:

```
% POS [modelo] "<trecho curto>" -> reforça o enquadramento.
%     Fonte: <arquivo:linha>. Responde: o pesquisador, se assumir.
```

## Limite

A auditoria feita pelo mesmo modelo que redigiu é parcial. A contraprova é a mesma
tarefa feita de outro jeito:

- numa conversa limpa, de preferência com o enquadramento invertido;
- ou noutro modelo.

Diga isso uma vez por auditoria, e não em cada achado.
