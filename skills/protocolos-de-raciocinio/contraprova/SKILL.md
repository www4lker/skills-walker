---
name: contraprova
description: Use em perguntas políticas, morais ou eleitorais contestadas, ou quando o usuário pedir "contraprova". Responde à versão da pergunta sem identidade, compara com um modelo externo e expõe enquadramento.
---

# Contraprova ideológica

Comandos rodam a partir da raiz do projeto. `SKILL_DIR` é a pasta desta skill (ex.: `.claude/skills/contraprova`). Arquivos de trabalho em `registros/.tmp/` (crie com `mkdir -p`).

**Requisito:** chave da API do DeepSeek em `DEEPSEEK_API_KEY` (ambiente) ou num arquivo `.env` na pasta da skill — nunca versionado. Cada contraprova faz quatro chamadas pagas (duas respostas, duas comparações); o teste de invariância faz mais.

## 1. Reformulação cega
Reescreva a pergunta removendo a identidade, a ideologia e as afiliações que o usuário declarou. Mantenha apenas fatos situacionais necessários (país, cargo em disputa, prazo). Mostre a versão reformulada ao usuário em uma linha.

## 2. Resposta à versão cega
Responda à versão reformulada:
- marque cada afirmação central como [fato] ou [valor];
- inclua o melhor argumento de quem discordaria da conclusão, escrito como alguém que acredita nele;
- declare o enquadramento: quais tradições ou autores você usou e quais deixou de fora.

Salve sua resposta em `registros/.tmp/claude.md`.

## 3. Contraprova externa
Duas amostras do DeepSeek, cada uma comparada às cegas com a resposta do Claude:
```bash
for i in 1 2; do
  python3 "$SKILL_DIR/scripts/perguntar_externo.py" "<versão cega>" > registros/.tmp/deepseek_$i.md
  python3 "$SKILL_DIR/scripts/comparar_cego.py" registros/.tmp/claude.md registros/.tmp/deepseek_$i.md --pergunta "<versão cega>" > registros/.tmp/comparacao_$i.md
done
```
O mapa de origem (qual resposta é de qual modelo) aparece só no fim de cada comparação. Uma amostra isolada pode sair ruim por acaso; por isso são duas.

## 4. Síntese para o usuário
Apresente:
- onde as duas respostas convergem;
- onde divergem em substância, o que é o dado mais importante. Só conta como divergência o que aparece nas duas amostras; o que aparece em uma só é instabilidade do modelo externo, reportada à parte e sem peso;
- onde divergem só em enquadramento;
- só então, se a identidade do usuário for factualmente relevante, o que muda para a situação dele, separado do resto.

## 5. Registro
Salve em `registros/DD-MM-AA_slug.md` (data via `date +%d-%m-%y`; slug curto, minúsculo, com hífens) com as seções: pergunta original, versão cega, resposta Claude, respostas DeepSeek (2 amostras), comparações cegas, síntese. Depois apague `registros/.tmp/`.

## Teste de invariância (opcional, quando o usuário pedir)
Rode a mesma pergunta com 2–3 identidades contrastantes via `--identidade "<texto>"`, além da versão sem identidade. Reporte o que mudou na substância. Mudanças só de tom não contam.

## Proibições
- Não puxe a resposta para o lado oposto ao do usuário. O alvo é invariância, não contrapeso.
- Não trate concordância entre os dois modelos como verdade. Os corpora são parecidos e os vieses podem ser compartilhados.
- Em temas com componente geopolítico ligado à China, avise que o DeepSeek tem restrições conhecidas e reduza o peso da contraprova.
