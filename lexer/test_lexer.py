from lexer import tokenizar

codigo = """CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10

TURNO Arthur
MOVER Arthur DIREITA
MOVER Arthur CIMA
MOVER Arthur ESQUERDA"""

tokens = tokenizar(codigo)

for token in tokens:
    print(token)
