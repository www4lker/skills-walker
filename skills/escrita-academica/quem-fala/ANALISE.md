# quem-fala — análise

**Complexidade:** média — dois modos (redigir e auditar), formato de registro fixo, sem dependências

| Forças | Fraquezas |
|---|---|
| • Uma pergunta só organiza tudo: quem fala aqui, e alguém humano assumiu isso?<br>• Troca a dicotomia fato/valor por proveniência e assunção, que dá para conferir linha a linha.<br>• Procura viés nas duas direções: complacência com o pesquisador e interesse da empresa que treinou o modelo.<br>• Audita sem reescrever: só acrescenta comentários, e a prosa fica idêntica. | • É autoauditoria do mesmo modelo que redigiu, e a própria skill declara essa parcialidade.<br>• Depende de voltar às fontes; sem acesso a elas, a omissão não aparece.<br>• A lista de sinais nasceu de quatro arquivos de um único artigo. |

| Oportunidades | Ameaças |
|---|---|
| • Dá conteúdo verificável à declaração de uso de IA exigida por periódicos.<br>• O registro das marcas pode virar dado de pesquisa e sustentar uma nota metodológica. | • As marcas podem dar ao texto uma aparência de controle que a autoauditoria não garante.<br>• Marcar como `[modelo]` não basta: o risco é o pesquisador assumir em bloco, sem ler. |

## Fluxo

```mermaid
flowchart TD
    T["Trecho com participação de IA"] --> Q{"Quem fala aqui?"}
    Q --> F["[fonte]<br>dá para conferir"]
    Q --> M["[modelo]<br>leitura não assumida"]
    Q --> O["[omissão]<br>só aparece nas fontes"]
    M --> DIR["Direção: reforça ou atenua<br>+ camada + quem responde"]
    O --> DIR
    DIR --> P{"Pesquisador decide"}
    P -- "assume" --> A["[artigo]"]
    P -- "descarta" --> X["Sai do texto"]
```
