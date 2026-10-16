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
        print("Análise semântica concluída com sucesso.")

    except SyntaxError as erro:
        print(erro)

    except ValueError as erro:
        print(erro)


# Teste 1 - programa válido
codigo1 = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
ATACAR Arthur Goblin
DEFENDER Arthur
"""

testar(
    codigo1,
    "Teste 1 - Personagens existentes"
)


# Teste 2 - personagem inexistente
codigo2 = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
ATACAR Arthur Goblin
"""

testar(
    codigo2,
    "Teste 2 - Personagem inexistente"
)


# Teste 3 - personagem duplicado
codigo3 = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR HEROI Arthur VIDA 80 ATAQUE 15 DEFESA 8
"""

testar(
    codigo3,
    "Teste 3 - Personagem duplicado"
)


# Teste 4 - habilidade e movimento
codigo4 = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
HABILIDADE Arthur GOLPE_FORTE
TURNO Arthur
MOVER Arthur CIMA
"""

testar(
    codigo4,
    "Teste 4 - Habilidade, turno e movimentação"
)


# Teste 5 - condicional
codigo5 = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 20 ATAQUE 10 DEFESA 5
SE VIDA Goblin <= 20
ATACAR Arthur Goblin
SENAO
DEFENDER Arthur
FIM
"""

testar(
    codigo5,
    "Teste 5 - Condicional"
)


# Teste 6 - repetição
codigo6 = """
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
REPETIR 2
MOVER Arthur CIMA
FIM
"""

testar(
    codigo6,
    "Teste 6 - Repetição"
)
