
import sys
from pathlib import Path

from lexer.lexer import tokenizar
from parser.parser import Parser
from parser.semantic_analyzer import AnalisadorSemantico
from interpreter.interpreter import Interpretador


BANNER = """
====================================================
             GAMELANG - COMPILADOR DE RPG
====================================================
Uma linguagem para descrever combates de RPG.
Escreva comandos, acompanhe o compilador e veja
o resultado acontecer na interface grafica.
"""


def compilar_codigo(codigo, modo="visual"):
    """Executa as etapas do compilador e, se aprovado, inicia o combate."""
    print("\n" + "=" * 52)
    print("                 COMPILADOR GAMELANG")
    print("=" * 52)

    if not codigo.strip():
        print("\nNenhum codigo foi informado.")
        return False

    # 1. Analise lexica
    print("\n[1/5] ANALISE LEXICA")
    print("O lexer identifica palavras-chave, nomes, numeros e operadores.")
    tokens = tokenizar(codigo)

    for tipo, valor in tokens:
        print(f"  Token: {tipo:<22} Valor: {valor}")

    erros_lexicos = [token for token in tokens if token[0] == "ERRO_LEXICO"]
    if erros_lexicos:
        print("\n[ERRO LEXICO] Existem simbolos que nao pertencem a linguagem:")
        for erro in erros_lexicos:
            print(f"  - {erro[1]!r}")
        print("Corrija o codigo e tente novamente.")
        return False

    print(f"\n[OK] Analise lexica concluida: {len(tokens)} tokens identificados.")

    # 2. Analise sintatica e AST
    print("\n[2/5] ANALISE SINTATICA")
    print("O parser verifica se os comandos seguem a gramatica da GameLang.")
    try:
        parser = Parser(tokens)
        arvore = parser.programa()
    except SyntaxError as erro:
        print(f"\n[ERRO SINTATICO] {erro}")
        print("Confira a ordem das palavras e os argumentos de cada comando.")
        return False

    print("[OK] Estrutura reconhecida pela gramatica.")
    print(f"Comandos de nivel principal: {len(arvore.comandos)}")

    print("\n[3/5] CONSTRUCAO DA AST")
    print("A AST organiza os comandos em estruturas que o programa consegue processar.")
    for indice, comando in enumerate(arvore.comandos, start=1):
        print(f"  {indice}. {type(comando).__name__}")
    print("[OK] Arvore sintatica abstrata criada.")

    # 4. Analise semantica
    print("\n[4/5] ANALISE SEMANTICA")
    print("O analisador verifica personagens, atributos e referencias.")
    try:
        analisador = AnalisadorSemantico()
        analisador.analisar(arvore)
    except ValueError as erro:
        print(f"\n[ERRO SEMANTICO] {erro}")
        print("Verifique se os personagens foram criados antes de serem utilizados.")
        return False

    print("[OK] Analise semantica concluida.")
    print("\nTabela de simbolos:")
    if analisador.tabela.simbolos:
        for nome, dados in analisador.tabela.simbolos.items():
            print(
                f"  - {nome}: tipo={dados['tipo']}, vida={dados['vida']}, "
                f"ataque={dados['ataque']}, defesa={dados['defesa']}"
            )
    else:
        print("  (nenhum personagem declarado)")

    # 5. Interpretacao / representacao
    print("\n[5/5] EXECUCAO")
    print("[OK] Codigo aprovado pelas etapas do compilador.")
    interpretador = Interpretador()

    if modo == "terminal":
        print("Executando o combate no terminal:\n")
        try:
            interpretador.executar(arvore)
        except ValueError as erro:
            print(f"[ERRO DURANTE A EXECUCAO] {erro}")
        return True

    print("Abrindo o Pygame para representar o combate.")
    print("Na janela do jogo: ESPACO = proximo comando | ESC = sair")
    try:
        from interface.game import Game
        jogo = Game(interpretador, arvore.comandos)
        jogo.executar()
    except ImportError as erro:
        print("\nNao foi possivel carregar o Pygame.")
        print(f"Detalhes: {erro}")
        print("Instale as dependencias com: pip install -r requirements.txt")
        print("Como alternativa, execute novamente com --terminal.")
    except (FileNotFoundError, OSError) as erro:
        print(f"\nNao foi possivel iniciar a interface grafica: {erro}")
        print("Confira os arquivos da pasta interface/assets.")
    return True


def mostrar_ajuda():
    print("""
COMO ESCREVER NA GAMELANG
-------------------------
1) Criar um heroi:
   CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10

2) Criar um inimigo:
   CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5

3) Escolher o turno:
   TURNO Arthur

4) Atacar ou defender:
   ATACAR Arthur Goblin
   DEFENDER Arthur

5) Usar habilidade:
   HABILIDADE Arthur GOLPE_FORTE

6) Mover uma casa:
   MOVER Arthur DIREITA
   Direcoes aceitas: CIMA, BAIXO, ESQUERDA, DIREITA

7) Repetir comandos:
   REPETIR 2
       MOVER Arthur DIREITA
   FIM

8) Criar uma condicao:
   SE VIDA Goblin <= 20
       ATACAR Arthur Goblin
   SENAO
       DEFENDER Arthur
   FIM

Observacoes:
- Os nomes dos personagens sao identificadores.
- Crie os personagens antes de referencia-los.
- Os numeros de VIDA, ATAQUE e DEFESA devem ser inteiros.
- FIM encerra blocos de REPETIR e SE/SENAO.
""")


def mostrar_comandos():
    print("""
COMANDOS DISPONIVEIS
--------------------
CRIAR HEROI / CRIAR INIMIGO  - cria personagens e define atributos
ATACAR personagem alvo      - realiza um ataque
DEFENDER personagem         - prepara a defesa
HABILIDADE personagem nome  - utiliza uma habilidade
TURNO personagem            - indica o turno
MOVER personagem DIRECAO    - movimenta uma casa no tabuleiro
SE VIDA nome operador valor - executa comandos se a condicao for verdadeira
SENAO                       - alternativa de uma condicao
REPETIR quantidade          - repete um bloco de comandos
FIM                         - encerra um bloco

Operadores de condicao: <, >, <=, >=, ==
""")


def exemplo_curto():
    return """CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
TURNO Arthur
MOVER Arthur DIREITA
ATACAR Arthur Goblin
DEFENDER Arthur
"""


def ler_codigo_interativo():
    print("\nEDITOR SIMPLES DA GAMELANG")
    print("Digite ou cole seu codigo, uma linha por vez.")
    print("Quando terminar, digite EXECUTAR em uma linha separada.")
    print("Digite CANCELAR para voltar ao menu.\n")
    linhas = []
    while True:
        try:
            linha = input("GL> ")
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada cancelada.")
            return None
        comando = linha.strip().upper()
        if comando == "CANCELAR":
            return None
        if comando == "EXECUTAR":
            return "\n".join(linhas)
        linhas.append(linha)


def executar_interativo():
    while True:
        print(BANNER)
        print("O que voce deseja fazer?")
        print("  [1] Aprender a escrever na GameLang")
        print("  [2] Consultar os comandos")
        print("  [3] Ver um exemplo de codigo")
        print("  [4] Escrever meu proprio combate")
        print("  [5] Executar o exemplo completo do projeto")
        print("  [0] Sair")

        try:
            opcao = input("\nEscolha uma opcao: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAte mais!")
            return

        if opcao == "1":
            mostrar_ajuda()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "2":
            mostrar_comandos()
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "3":
            print("\nEXEMPLO DE CODIGO\n-----------------")
            print(exemplo_curto())
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "4":
            codigo = ler_codigo_interativo()
            if codigo is not None:
                compilar_codigo(codigo, modo="visual")
                input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "5":
            caminho = Path(__file__).parent / "exemplos" / "combate.gl"
            try:
                codigo = caminho.read_text(encoding="utf-8")
            except OSError as erro:
                print(f"Nao foi possivel abrir o exemplo: {erro}")
            else:
                print(f"\nExecutando: {caminho.name}")
                compilar_codigo(codigo, modo="visual")
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == "0":
            print("\nObrigado por conhecer a GameLang!")
            return
        else:
            print("\nOpcao invalida. Escolha uma opcao do menu.")
            input("Pressione ENTER para continuar...")


def executar_arquivo(caminho, modo="visual"):
    try:
        codigo = Path(caminho).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho}' nao encontrado.")
        return
    compilar_codigo(codigo, modo=modo)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Uso:")
        print("  Interativo: python main.py --interativo")
        print("  Visual:     python main.py exemplos/combate.gl")
        print("  Terminal:   python main.py exemplos/combate.gl --terminal")
    elif sys.argv[1] in {"--interativo", "-i"}:
        executar_interativo()
    else:
        caminho = sys.argv[1]
        modo = "terminal" if len(sys.argv) >= 3 and sys.argv[2] == "--terminal" else "visual"
        executar_arquivo(caminho, modo)
