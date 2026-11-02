# Teste de execução válida do Interpretador da GameLang - Sprint 4

from interpreter.interpreter import Interpretador
from parser.ast import (
    Programa,
    CriarPersonagem,
    Habilidade,
    Turno,
    Mover,
    Atacar,
    Defender
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

    Habilidade(
        "Arthur",
        "GOLPE_FORTE"
    ),

    Turno(
        "Arthur"
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
    )
])


interpretador = Interpretador()
interpretador.executar(ast)
