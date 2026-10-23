import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from lexer.lexer import tokenizar
from parser.parser import Parser
from parser.semantic_analyzer import AnalisadorSemantico


def testar(codigo, nome_teste):
    print(f"\n{'=' * 50}")
    print(nome_teste)
    print("=" * 50)

    try:
        tokens = tokenizar(codigo)
        parser = Parser(tokens)
        arvore = parser.programa()

        analisador = AnalisadorSemantico()
        analisador.analisar(arvore)

        print("Resultado: código aceito!")

    except SyntaxError as erro:
        print(erro)

    except ValueError as erro:
        print(erro)



