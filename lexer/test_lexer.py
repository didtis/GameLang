from lexer import tokenizar

codigo = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
ATACAR Arthur Goblin
DEFENDER Arthur
HABILIDADE Arthur GOLPE_FORTE
TURNO Arthur
MOVER Arthur DIREITA
SE VIDA Goblin <= 20
FIM
"""

tokens = tokenizar(codigo)

for token in tokens:
    print(token)
