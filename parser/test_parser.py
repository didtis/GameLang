from lexer.lexer import tokenizar
from parser.parser import Parser


codigo = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
"""

tokens = tokenizar(codigo)

print("Tokens:")
for token in tokens:
    print(token)

print("\nTeste do parser:")

try:
    parser = Parser(tokens)
    parser.programa()
    print("Parser: código aceito com sucesso!")

except SyntaxError as erro:
    print(erro)
