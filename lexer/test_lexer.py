from lexer import tokenizar

codigo = """
SENAO
REPETIR 3
MOVER Arthur CIMA
MOVER Arthur BAIXO
MOVER Arthur ESQUERDA
MOVER Arthur DIREITA
FIM
"""

tokens = tokenizar(codigo)

for token in tokens:
    print(token)
