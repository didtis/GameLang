from lexer import tokenizar

codigo = "ATACAR Arthur # Goblin"

tokens = tokenizar(codigo)

for token in tokens:
    print(token)
