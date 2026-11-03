
from parser.ast import (
    Programa,
    CriarPersonagem,
    Mover,
    Atacar
)

from interpreter.interpreter import Interpretador
from interface.game import Game


ast = Programa([

    # Criação dos personagens
    CriarPersonagem(
        "HEROI",
        "Arthur",
        30,
        5,
        0
    ),

    CriarPersonagem(
        "INIMIGO",
        "Goblin",
        50,
        20,
        0
    ),

    # Aproximação dos personagens
    Mover("Arthur", "DIREITA"),
    Mover("Arthur", "DIREITA"),
    Mover("Arthur", "DIREITA"),

    # O Goblin ataca Arthur até derrotá-lo
    Atacar("Goblin", "Arthur"),
    Atacar("Goblin", "Arthur"),
    Atacar("Goblin", "Arthur"),
])

interpretador = Interpretador()

jogo = Game(
    interpretador,
    ast.comandos
)

jogo.executar()
