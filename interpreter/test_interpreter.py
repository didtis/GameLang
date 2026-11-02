# Teste de estruturas de controle - Sprint 4

from interpreter.interpreter import Interpretador
from parser.ast import (
    Programa,
    CriarPersonagem,
    Atacar,
    Defender,
    Condicional,
    CondicaoVida,
    Repeticao,
    Mover
)


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

    Condicional(
        CondicaoVida(
            "Goblin",
            "<=",
            50
        ),
        [
            Atacar(
                "Arthur",
                "Goblin"
            )
        ],
        [
            Defender(
                "Arthur"
            )
        ]
    ),

    Repeticao(
        2,
        [
            Mover(
                "Arthur",
                "CIMA"
            )
        ]
    )
])


interpretador = Interpretador()
interpretador.executar(ast)
