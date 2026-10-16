import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lexer.lexer import tokenizar
from parser import parser as parser_module

codigo = """
SE
FIM
"""
tokens = tokenizar(codigo)

print("Tokens:")
for token in tokens:
    print(token)

print("\nTeste do parser:")

try:
    parser = parser_module.Parser(tokens)
    parser.programa()
    print("Parser: código aceito com sucesso!")

except SyntaxError as erro:
    print(erro)
