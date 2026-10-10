#!/usr/bin/env python3
"""Compara duas respostas às cegas usando o DeepSeek como organizador.

Uso:
    python3 scripts/comparar_cego.py claude.md deepseek.md [--pergunta "versão cega"]

A ordem é embaralhada e o juiz não recebe rótulos de origem nem a identidade do
usuário. O mapa de origem só é impresso depois da análise.

Limitação: o DeepSeek pode estar julgando a própria resposta. Aceitável aqui —
o script apenas organiza as diferenças; o juiz final é o usuário.
"""
import argparse
import random
from pathlib import Path

from perguntar_externo import perguntar

INSTRUCAO = """Compare as duas respostas abaixo à mesma pergunta. Não diga qual é melhor.
Liste apenas, em três seções:

1. Diferenças de substância: conclusões, fatos afirmados, recomendações.
2. Diferenças de enquadramento: autores, tradições, vocabulário, o que ficou de fora.
3. Afirmações de valor apresentadas como se fossem fato, em qualquer uma das respostas (indique qual).

Trechos que a própria resposta atribui a quem discorda (ex.: "melhor argumento contra")
não são posição dela; não os conte como afirmação de valor da resposta.
Se não houver diferenças numa seção, escreva "nenhuma"."""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("a", type=Path)
    ap.add_argument("b", type=Path)
    ap.add_argument("--pergunta", help="a versão cega da pergunta, para contexto do juiz")
    args = ap.parse_args()

    ordem = [args.a, args.b]
    random.shuffle(ordem)

    partes = [INSTRUCAO]
    if args.pergunta:
        partes.append(f"## Pergunta\n{args.pergunta}")
    for i, arq in enumerate(ordem, 1):
        partes.append(f"## Resposta {i}\n{arq.read_text().strip()}")

    print(perguntar([{"role": "user", "content": "\n\n".join(partes)}], temperatura=0))
    print("\n---")
    for i, arq in enumerate(ordem, 1):
        print(f"Resposta {i} = {arq.name}")


if __name__ == "__main__":
    main()
