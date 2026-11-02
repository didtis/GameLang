# Teste de erro do Interpretador da GameLang - Sprint 4

from interpreter.interpreter import Interpretador
from parser.ast import (
    Programa,
    CriarPersonagem,
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

    Condicional(
        CondicaoVida(
            "Goblin",
            "<=",
            20
        ),
        [
        ],
        None
    )
])


interpretador = Interpretador()
interpretador.executar(ast)
