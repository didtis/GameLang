
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

    # Movimentação do Arthur
    Mover(
        "Arthur",
        "DIREITA"
    ),

    # Movimentação do Goblin
    Mover(
        "Goblin",
        "ESQUERDA"
    ),

    Mover(
        "Goblin",
        "ESQUERDA"
    ),

    Mover(
        "Goblin",
        "DIREITA"
    ),

    Mover(
        "Goblin",
        "DIREITA"
    ),

    # Testes de combate
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
