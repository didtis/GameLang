from lexer import tokenizar

codigo = """CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 20 ATAQUE 10 DEFESA 5

SE VIDA Goblin <= 20
    HABILIDADE Arthur GOLPE_FORTE
SENAO
    ATACAR Arthur Goblin
FIM"""

tokens = tokenizar(codigo)

for token in tokens:
    print(token)
