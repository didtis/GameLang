import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from lexer.lexer import tokenizar
from parser import parser as parser_module


def imprimir_ast(no, nivel=0):
    espacos = "    " * nivel

    if no.__class__.__name__ == "Programa":
        print(f"{espacos}Programa")

        for comando in no.comandos:
            imprimir_ast(comando, nivel + 1)

    elif no.__class__.__name__ == "CriarPersonagem":
        print(f"{espacos}CriarPersonagem")
        print(f"{espacos}    tipo: {no.tipo}")
        print(f"{espacos}    nome: {no.nome}")
        print(f"{espacos}    vida: {no.vida}")
        print(f"{espacos}    ataque: {no.ataque}")
        print(f"{espacos}    defesa: {no.defesa}")

    elif no.__class__.__name__ == "Atacar":
        print(f"{espacos}Atacar")
        print(f"{espacos}    atacante: {no.atacante}")
        print(f"{espacos}    alvo: {no.alvo}")

    elif no.__class__.__name__ == "Defender":
        print(f"{espacos}Defender")
        print(f"{espacos}    personagem: {no.personagem}")

    elif no.__class__.__name__ == "Habilidade":
        print(f"{espacos}Habilidade")
        print(f"{espacos}    personagem: {no.personagem}")
        print(f"{espacos}    nome: {no.nome}")

    elif no.__class__.__name__ == "Turno":
        print(f"{espacos}Turno")
        print(f"{espacos}    personagem: {no.personagem}")

    elif no.__class__.__name__ == "Mover":
        print(f"{espacos}Mover")
        print(f"{espacos}    personagem: {no.personagem}")
        print(f"{espacos}    direcao: {no.direcao}")

    elif no.__class__.__name__ == "Condicional":
        print(f"{espacos}Condicional")

        print(f"{espacos}    Condicao:")
        imprimir_ast(no.condicao, nivel + 2)

        print(f"{espacos}    Comandos:")
        for comando in no.comandos:
            imprimir_ast(comando, nivel + 2)

        if no.senao is not None:
            print(f"{espacos}    SENAO:")
            for comando in no.senao:
                imprimir_ast(comando, nivel + 2)

    elif no.__class__.__name__ == "Repeticao":
        print(f"{espacos}Repeticao")
        print(f"{espacos}    quantidade: {no.quantidade}")

        print(f"{espacos}    Comandos:")
        for comando in no.comandos:
            imprimir_ast(comando, nivel + 2)

    elif no.__class__.__name__ == "CondicaoVida":
        print(f"{espacos}CondicaoVida")
        print(f"{espacos}    personagem: {no.personagem}")
        print(f"{espacos}    operador: {no.operador}")
        print(f"{espacos}    valor: {no.valor}")


codigo = """
SE VIDA Goblin <= 20
ATACAR Arthur Goblin
SENAO
DEFENDER Arthur
FIM
REPETIR 2
MOVER Arthur CIMA
FIM
"""


tokens = tokenizar(codigo)

print("Tokens:")
for token in tokens:
    print(token)


print("\nTeste do parser:")

try:
    parser = parser_module.Parser(tokens)
    arvore = parser.programa()

    print("Parser: código aceito com sucesso!")

    print("\nAST:")
    imprimir_ast(arvore)

except SyntaxError as erro:
    print(erro)
