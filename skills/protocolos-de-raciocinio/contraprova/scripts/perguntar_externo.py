#!/usr/bin/env python3
"""Envia uma pergunta ao DeepSeek e imprime a resposta.

Uso:
    python3 scripts/perguntar_externo.py "pergunta"
    echo "pergunta" | python3 scripts/perguntar_externo.py
    python3 scripts/perguntar_externo.py --identidade "eleitor de direita" "pergunta"
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

URL = "https://api.deepseek.com/chat/completions"
SISTEMA = "Responda à pergunta com precisão, em português."


def _carregar_env():
    """Lê .env da raiz do repo sem sobrescrever o que já está no ambiente."""
    env = Path(__file__).resolve().parent.parent / ".env"
    if env.exists():
        for linha in env.read_text().splitlines():
            nome, sep, valor = linha.partition("=")
            if sep and not nome.lstrip().startswith("#") and valor.strip():
                os.environ.setdefault(nome.strip(), valor.strip().strip("\"'"))


def perguntar(mensagens, temperatura=0.2):
    _carregar_env()
    chave = os.environ.get("DEEPSEEK_API_KEY") or sys.exit("DEEPSEEK_API_KEY ausente (ambiente ou .env).")
    corpo = {
        "model": os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-pro"),
        "messages": mensagens,
        "temperature": temperatura,
        "thinking": {"type": "disabled"},  # em modo thinking a temperatura é ignorada
    }
    req = urllib.request.Request(
        URL,
        data=json.dumps(corpo).encode(),
        headers={"Authorization": f"Bearer {chave}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            dados = json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"DeepSeek HTTP {e.code}: {e.read().decode(errors='replace')}")
    return dados["choices"][0]["message"]["content"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pergunta", nargs="?")
    ap.add_argument("--identidade", help="acrescenta 'O usuário se identifica como <texto>.'")
    args = ap.parse_args()

    pergunta = args.pergunta or sys.stdin.read().strip()
    if not pergunta:
        ap.error("pergunta vazia")
    if args.identidade:
        pergunta = f"O usuário se identifica como {args.identidade}.\n\n{pergunta}"

    print(perguntar([{"role": "system", "content": SISTEMA}, {"role": "user", "content": pergunta}]))


if __name__ == "__main__":
    main()
