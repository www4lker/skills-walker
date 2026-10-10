# auditoria-causal-sistemica — análise

**Complexidade:** alta — oito operações com artefato obrigatório, ordem de construção imposta, autoverificação

| Forças | Fraquezas |
|---|---|
| • Nomeia as quatro patologias que combate (efeito-enciclopédia, paradoxo fabricado, ancoragem-na-tese, setas vazias); o leitor sabe o que conferir.<br>• Troca "provável" por tags de apoio (demonstrado / mecanístico / conjectural), que o leitor consegue auditar.<br>• Separa ordem de construção de ordem de apresentação: a tese vem primeiro no texto, mas é escrita por último. | • É pesada: num caso pequeno, as oito operações tendem a inflar, apesar do aviso sobre densidade.<br>• O exemplo do caso-base (detectores de IA na universidade) vem do domínio de origem; em outros domínios, quem usa precisa transpor.<br>• O parágrafo final "à la Zinsser" foi acrescentado depois do resto e não passa pela autoverificação. |

| Oportunidades | Ameaças |
|---|---|
| • Pode servir de gabarito de revisão para relatórios de impacto, pareceres e projetos de política pública.<br>• Combina com reductio-ad-absurdum: uma audita consequências, a outra a estrutura lógica. | • O modelo pode cumprir a forma sem a substância e rotular como "mecanístico" o que é palpite. A skill reduz esse risco, mas não o elimina, e diz isso.<br>• Quem só lê a tese pula as lacunas declaradas no fim. |

## Fluxo

```mermaid
flowchart TD
    A["Intervenção a auditar"] --> B["1. Fronteira: o que fica de fora"]
    B --> C["2. Caso-base: o que já acontecia sem ela"]
    C --> D["3. Cadeias por mecanismo<br>ator + adaptação + tag de apoio"]
    D --> E["4. Orçamento: no máximo 3-4 cadeias"]
    E --> F["5. Rival para o mecanismo candidato"]
    F --> G["6. Loops fechados no papel, com sinal"]
    G --> H["7. Paradoxo só com condição declarada"]
    H --> I["8. Um falsificador + um indicador"]
    I --> J{"Autoverificação:<br>algum 'não'?"}
    J -- "sim" --> D
    J -- "não" --> K["Mecanismo dominante<br>(escrito por último)"]
    K --> L["Saída: tese primeiro, lacunas no fim<br>+ parágrafo em prosa simples"]
    I -. "se pedida" .-> M["Alavancagem com 6 campos"]
    M --> J
```

## Nota

O eixo 1ª/2ª/3ª ordem, usado em analista-sistemico-style, é abandonado aqui de propósito. As duas skills, lidas juntas, mostram a evolução do método.
