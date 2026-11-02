# Teste de erro do Interpretador da GameLang - Sprint 4

from interpreter.interpreter import Interpretador
from parser.ast import (
    Programa,
    CriarPersonagem,
    Atacar
)


ast = Programa([
    CriarPersonagem(
        "HEROI",
        "Arthur",
        100,
        20,
        5
    ),

    Atacar(
        "Arthur",
        "Goblin"
    )
])


interpretador = Interpretador()
interpretador.executar(ast)
