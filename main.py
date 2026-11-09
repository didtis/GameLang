
import sys

from lexer.lexer import tokenizar
from parser.parser import Parser
from parser.semantic_analyzer import AnalisadorSemantico
from interpreter.interpreter import Interpretador


def executar_arquivo(caminho, modo="visual"):

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

    for tipo, valor in tokens:
        print(f"Token: {tipo:<22} Valor: {valor}")

    erros_lexicos = [
        token for token in tokens
        if token[0] == "ERRO_LEXICO"
    ]

    if erros_lexicos:
        print("\nForam encontrados erros léxicos:")

        for erro in erros_lexicos:
            print(f"Símbolo inválido: {erro[1]}")

        return

    print(f"\nAnálise léxica concluída: {len(tokens)} tokens encontrados.")

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

    print("\nPersonagens registrados na tabela de símbolos:")

    for nome, dados in analisador.tabela.simbolos.items():
        print(
            f"- {nome}: tipo={dados['tipo']}, "
            f"vida={dados['vida']}, "
            f"ataque={dados['ataque']}, "
            f"defesa={dados['defesa']}"
        )

    # 5. Execução
    interpretador = Interpretador()

    if modo == "terminal":

        print("\n[4] EXECUÇÃO PELO TERMINAL")
        print("O combate será executado sem interface gráfica.")

        try:
            interpretador.executar(arvore)

        except ValueError as erro:
            print(f"Erro durante a execução: {erro}")

        return

    print("\n[4] EXECUÇÃO VISUAL")
    print("Abrindo a interface do combate...")
    print("Pressione ESPAÇO para executar o próximo comando.")
    print("Pressione ESC para sair.")

    try:
        from interface.game import Game

        jogo = Game(interpretador, arvore.comandos)
        jogo.executar()

    except ImportError as erro:
        print("\nNão foi possível carregar o Pygame.")
        print(f"Detalhes: {erro}")
        print("Execute novamente utilizando --terminal.")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Uso:")
        print("  Visual:   python main.py exemplos/combate.gl")
        print("  Terminal: python main.py exemplos/combate.gl --terminal")

    else:
        caminho = sys.argv[1]
        modo = "visual"

        if len(sys.argv) >= 3 and sys.argv[2] == "--terminal":
            modo = "terminal"

        executar_arquivo(caminho, modo)
