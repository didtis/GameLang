from lexer import tokenizar

codigo = "CRIAR HEROI 123Arthur VIDA 100"

tokens = tokenizar(codigo)

for token in tokens:
    print(token)
