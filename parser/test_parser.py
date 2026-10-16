import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lexer.lexer import tokenizar
from parser import parser as parser_module

codigo = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
HABILIDADE Arthur GOLPE_FORTE
TURNO Arthur
MOVER Arthur DIREITA
SE VIDA Goblin <= 20
ATACAR Arthur Goblin
SENAO
DEFENDER Arthur
FIM
REPETIR 2
MOVER Arthur CIMA
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
