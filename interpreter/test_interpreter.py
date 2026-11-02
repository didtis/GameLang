# Teste do Interpretador da GameLang - Sprint 4

from interpreter.interpreter import Interpretador
from parser.ast import (
    Programa,
    CriarPersonagem,
    Atacar,
    Defender,
    Habilidade,
    Turno,
    Mover,
    Condicional,
    CondicaoVida
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
        15,
        10,
        5
    ),

    Habilidade(
        "Arthur",
        "GOLPE_FORTE"
    ),

    Turno("Arthur"),

    Mover(
        "Arthur",
        "DIREITA"
    ),

    Condicional(
        CondicaoVida(
            "Goblin",
            "<=",
            20
        ),

        [
            Atacar(
                "Arthur",
                "Goblin"
            )
        ],

        [
            Defender("Arthur")
        ]
    )
])


interpretador = Interpretador()
interpretador.executar(ast)
