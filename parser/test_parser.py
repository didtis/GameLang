import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from lexer.lexer import tokenizar
from parser import parser as parser_module


codigo = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
ATACAR Arthur Goblin
DEFENDER Arthur
"""


tokens = tokenizar(codigo)

print("Tokens:")
for token in tokens:
    print(token)


print("\nTeste do parser:")

try:
    parser = parser_module.Parser(tokens)
    arvore = parser.programa()

    print("Parser: código aceito com sucesso!")

    print("\nAST:")
    print(arvore)

    print("\nComandos da AST:")

    for comando in arvore.comandos:
        print(" -", type(comando).__name__)

except SyntaxError as erro:
    print(erro)
