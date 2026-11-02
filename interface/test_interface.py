from parser.ast import Programa, CriarPersonagem, Mover
from interpreter.interpreter import Interpretador
from interface.game import Game


ast = Programa([
    CriarPersonagem(
        "HEROI",
        "Arthur",
        100,
        20,
        5
    ),

    CriarPersonagem(
        "INIMIGO",
        "Goblin",
        50,
        10,
        5
    ),

    Mover(
        "Arthur",
        "DIREITA"
    )
])


interpretador = Interpretador()

interpretador.executar(ast)

print("\nPosições finais:")
print(interpretador.posicoes)

jogo = Game(interpretador.personagens)
jogo.executar()
