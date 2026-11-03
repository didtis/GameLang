
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

    # Criação dos personagens
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

    # Aproximação: Arthur vai da coluna 2 até a 5
    Mover("Arthur", "DIREITA"),
    Mover("Arthur", "DIREITA"),
    Mover("Arthur", "DIREITA"),

    # Combate
    Atacar("Arthur", "Goblin"),
    Defender("Goblin"),
    Atacar("Goblin", "Arthur"),
    Atacar("Arthur", "Goblin"),
    Atacar("Arthur", "Goblin"),
    Atacar("Arthur", "Goblin"),
    Atacar("Arthur", "Goblin"),
])

interpretador = Interpretador()

jogo = Game(
    interpretador,
    ast.comandos
)

jogo.executar()
