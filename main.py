
import sys

from lexer.lexer import tokenizar
from parser.parser import Parser
from parser.semantic_analyzer import AnalisadorSemantico
from interpreter.interpreter import Interpretador
from interface.game import Game


def executar_arquivo(caminho):

    print("===================================")
    print("       COMPILADOR GAMELANG")
    print("===================================")

    # 1. Leitura do arquivo
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            codigo = arquivo.read()

    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho}' não encontrado.")
        return

    # 2. Análise léxica
    print("\n[1] ANÁLISE LÉXICA")

    tokens = tokenizar(codigo)

    erros_lexicos = [
        token for token in tokens
        if token[0] == "ERRO_LEXICO"
    ]

    if erros_lexicos:
        print("Foram encontrados erros léxicos:")

        for erro in erros_lexicos:
            print(f"Símbolo inválido: {erro[1]}")

        return

    print(f"Análise léxica concluída: {len(tokens)} tokens encontrados.")

    # 3. Análise sintática
    print("\n[2] ANÁLISE SINTÁTICA")

    try:
        parser = Parser(tokens)
        arvore = parser.programa()

    except SyntaxError as erro:
        print(f"Erro sintático: {erro}")
        return

    print("Análise sintática concluída com sucesso.")
    print(f"Comandos encontrados: {len(arvore.comandos)}")

    # 4. Análise semântica
    print("\n[3] ANÁLISE SEMÂNTICA")

    try:
        analisador = AnalisadorSemantico()
        analisador.analisar(arvore)

    except ValueError as erro:
        print(f"Erro semântico: {erro}")
        return

    print("Análise semântica concluída com sucesso.")

    # 5. Execução do interpretador e Pygame
    print("\n[4] EXECUÇÃO")
    print("Abrindo a interface do combate...")
    print("Pressione ESPAÇO para executar o próximo comando.")
    print("Pressione ESC para sair.")

    interpretador = Interpretador()
    jogo = Game(interpretador, arvore.comandos)
    jogo.executar()


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Uso: python main.py caminho/do/arquivo.gl")
    else:
        executar_arquivo(sys.argv[1])
