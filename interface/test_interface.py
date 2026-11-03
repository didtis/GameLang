
from parser.ast import (
    Programa,
    CriarPersonagem,
    Mover,
    Atacar,
    Defender
)

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
    ),

    Atacar(
        "Arthur",
        "Goblin"
    ),

    Defender(
        "Arthur"
    ),

    Atacar(
        "Goblin",
        "Arthur"
    )

])


interpretador = Interpretador()

jogo = Game(
    interpretador,
    ast.comandos
)

jogo.executar()
