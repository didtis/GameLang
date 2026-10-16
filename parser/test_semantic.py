from semantic import TabelaSimbolos


tabela = TabelaSimbolos()


print("Teste 1: adicionar personagem")

try:
    tabela.adicionar(
        "Arthur",
        "HEROI",
        "100",
        "20",
        "10"
    )

    print("Personagem Arthur adicionado com sucesso!")

except ValueError as erro:
    print(erro)


print("\nTeste 2: verificar personagem")

if tabela.existe("Arthur"):
    print("Arthur existe na tabela de símbolos.")
else:
    print("Arthur não existe na tabela de símbolos.")


print("\nTeste 3: obter atributos")

try:
    dados = tabela.obter("Arthur")

    print("Dados de Arthur:")
    print("Tipo:", dados["tipo"])
    print("Vida:", dados["vida"])
    print("Ataque:", dados["ataque"])
    print("Defesa:", dados["defesa"])

except ValueError as erro:
    print(erro)


print("\nTeste 4: personagem inexistente")

try:
    tabela.obter("Goblin")

except ValueError as erro:
    print(erro)


print("\nTeste 5: personagem duplicado")

try:
    tabela.adicionar(
        "Arthur",
        "HEROI",
        "100",
        "20",
        "10"
    )

except ValueError as erro:
    print(erro)
