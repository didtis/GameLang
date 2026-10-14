from lexer import tokenizar

codigo = """CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5

TURNO Arthur
REPETIR 2
    MOVER Arthur DIREITA
    ATACAR Arthur Goblin
FIM"""

tokens = tokenizar(codigo)

for token in tokens:
    print(token)
