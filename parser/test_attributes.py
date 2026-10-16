import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from lexer.lexer import tokenizar
from parser.parser import Parser
from parser.semantic_analyzer import AnalisadorSemantico


def testar(codigo, nome_teste):
    print(f"\n{'=' * 50}")
    print(nome_teste)
    print("=" * 50)

    try:
        tokens = tokenizar(codigo)
        parser = Parser(tokens)
        arvore = parser.programa()

        analisador = AnalisadorSemantico()
        analisador.analisar(arvore)

        print("Resultado: código aceito!")

    except SyntaxError as erro:
        print(erro)

    except ValueError as erro:
        print(erro)


# Teste 1 - atributos válidos
testar(
    """
    CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
    """,
    "Teste 1 - Atributos válidos"
)


# Teste 2 - vida como texto
testar(
    """
    CRIAR HEROI Arthur VIDA cem ATAQUE 20 DEFESA 10
    """,
    "Teste 2 - Vida inválida"
)


# Teste 3 - ataque como texto
testar(
    """
    CRIAR HEROI Arthur VIDA 100 ATAQUE forte DEFESA 10
    """,
    "Teste 3 - Ataque inválido"
)


# Teste 4 - defesa como texto
testar(
    """
    CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA resistente
    """,
    "Teste 4 - Defesa inválida"
)


# Teste 5 - tipo de personagem inválido
testar(
    """
    CRIAR PERSONAGEM Arthur VIDA 100 ATAQUE 20 DEFESA 10
    """,
    "Teste 5 - Tipo inválido"
)
