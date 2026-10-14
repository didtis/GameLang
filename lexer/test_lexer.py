from lexer import tokenizar

codigo = """CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESAA 10"""

tokens = tokenizar(codigo)

for token in tokens:
    print(token)
