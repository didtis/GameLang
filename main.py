
import os
import sys
from pathlib import Path

from lexer.lexer import tokenizar
from parser.parser import Parser
from parser.semantic_analyzer import AnalisadorSemantico
from interpreter.interpreter import Interpretador


# Cores ANSI para o terminal
if os.name == "nt":
    os.system("")

RESET = "\033[0m"
AZUL = "\033[94m"
CIANO = "\033[96m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
NEGRITO = "\033[1m"

BANNER = f"""
{AZUL}{'=' * 60}{RESET}
{NEGRITO}{CIANO}{'GAMELANG - COMPILADOR DE RPG'.center(60)}{RESET}
{AZUL}{'=' * 60}{RESET}
Uma linguagem para descrever combates de RPG.
Escreva comandos, acompanhe as etapas do compilador e veja
as acoes acontecerem na interface grafica.
"""


# ==========================================================
# FUNCOES DE APRESENTACAO DO TERMINAL
# ==========================================================

def mostrar_titulo(texto):
    print("\n" + AZUL + "=" * 60 + RESET)
    print(NEGRITO + CIANO + texto.center(60) + RESET)
    print(AZUL + "=" * 60 + RESET)


def mostrar_etapa(numero, total, texto):
    print("\n" + CIANO + "-" * 60 + RESET)
    print(NEGRITO + f"[{numero}/{total}] {texto}" + RESET)
    print(CIANO + "-" * 60 + RESET)


def mostrar_sucesso(texto):
    print(VERDE + "[OK] " + texto + RESET)


def mostrar_aviso(texto):
    print(AMARELO + "[AVISO] " + texto + RESET)


def mostrar_erro(texto):
    print(VERMELHO + "[ERRO] " + texto + RESET)


def pausar(mensagem="Pressione ENTER para voltar ao menu..."):
    try:
        input("\n" + mensagem)
    except (EOFError, KeyboardInterrupt):
        print()


# ==========================================================
# PROCESSO PRINCIPAL DO COMPILADOR
# ==========================================================

def compilar_codigo(codigo, modo="visual"):
    """Executa as etapas do compilador e inicia a representacao do combate."""

    mostrar_titulo("COMPILADOR GAMELANG")

    if not codigo.strip():
        mostrar_aviso("Nenhum codigo foi informado.")
        return False

    # 1. ANALISE LEXICA
    mostrar_etapa(1, 5, "ANALISE LEXICA")

    print("O lexer identifica palavras-chave, nomes, numeros e operadores.")

    tokens = tokenizar(codigo)

    if tokens:
        print("\nTOKENS IDENTIFICADOS")
        print("-" * 60)

        for tipo, valor in tokens:
            print(f"  {tipo:<22} | {valor}")
    else:
        mostrar_aviso("Nenhum token foi identificado.")

    erros_lexicos = [
        token for token in tokens
        if token[0] == "ERRO_LEXICO"
    ]

    if erros_lexicos:
        mostrar_erro("A analise lexica encontrou simbolos desconhecidos:")

        for erro in erros_lexicos:
            print(f"  - {erro[1]!r}")

        mostrar_aviso("Corrija os simbolos indicados e execute novamente.")
        return False

    mostrar_sucesso(
        f"Analise lexica concluida: {len(tokens)} tokens identificados."
    )

    # 2. ANALISE SINTATICA
    mostrar_etapa(2, 5, "ANALISE SINTATICA")

    print("O parser verifica se os comandos seguem a gramatica da GameLang.")

    try:
        parser = Parser(tokens)
        arvore = parser.programa()

    except SyntaxError as erro:
        mostrar_erro(f"Falha na estrutura do codigo: {erro}")

        mostrar_aviso(
            "Confira a ordem das palavras e os argumentos de cada comando."
        )

        return False

    mostrar_sucesso("Estrutura reconhecida pela gramatica.")

    print(f"Comandos de nivel principal: {len(arvore.comandos)}")

    # 3. CONSTRUCAO DA AST
    mostrar_etapa(3, 5, "CONSTRUCAO DA AST")

    print(
        "A AST organiza os comandos em estruturas "
        "que o programa consegue processar."
    )

    for indice, comando in enumerate(arvore.comandos, start=1):
        print(f"  {indice:02d}. {type(comando).__name__}")

    mostrar_sucesso("Arvore sintatica abstrata criada.")

    # 4. ANALISE SEMANTICA
    mostrar_etapa(4, 5, "ANALISE SEMANTICA")

    print("O analisador verifica personagens, atributos e referencias.")

    try:
        analisador = AnalisadorSemantico()
        analisador.analisar(arvore)

    except ValueError as erro:
        mostrar_erro(f"Problema semantico: {erro}")

        mostrar_aviso(
            "Verifique se os personagens foram criados antes de serem utilizados."
        )

        return False

    mostrar_sucesso("Analise semantica concluida.")

    print("\nTABELA DE SIMBOLOS")
    print("-" * 60)

    if analisador.tabela.simbolos:

        print(
            f"{'PERSONAGEM':<18} {'TIPO':<12} "
            f"{'VIDA':>7} {'ATAQUE':>8} {'DEFESA':>8}"
        )

        for nome, dados in analisador.tabela.simbolos.items():

            print(
                f"{nome:<18} {dados['tipo']:<12} "
                f"{dados['vida']:>7} "
                f"{dados['ataque']:>8} "
                f"{dados['defesa']:>8}"
            )

    else:
        print("Nenhum personagem declarado.")

    # 5. EXECUCAO
    mostrar_etapa(5, 5, "EXECUCAO")

    mostrar_sucesso("Codigo aprovado pelas etapas do compilador.")

    interpretador = Interpretador()

    if modo == "terminal":

        print("\nExecutando o combate no terminal...\n")

        try:
            interpretador.executar(arvore)
            mostrar_sucesso("Execucao finalizada.")

        except ValueError as erro:
            mostrar_erro(f"Erro durante a execucao: {erro}")
            return False

        return True

    print("\nAbrindo o Pygame para representar o combate.")
    print("Na janela do jogo: ESPACO = proximo comando | ESC = sair")

    try:
        from interface.game import Game

        jogo = Game(interpretador, arvore.comandos)
        jogo.executar()

        mostrar_sucesso("Janela de execucao encerrada.")

    except ImportError as erro:

        mostrar_erro(f"Nao foi possivel carregar o Pygame: {erro}")

        mostrar_aviso(
            "Instale as dependencias com: pip install -r requirements.txt"
        )

        mostrar_aviso(
            "Como alternativa, execute novamente com --terminal."
        )

        return False

    except (FileNotFoundError, OSError) as erro:

        mostrar_erro(
            f"Nao foi possivel iniciar a interface grafica: {erro}"
        )

        mostrar_aviso(
            "Confira os arquivos da pasta interface/assets."
        )

        return False

    return True


# ==========================================================
# AJUDA E DOCUMENTACAO DA GAMELANG
# ==========================================================

def mostrar_ajuda():

    mostrar_titulo("COMO ESCREVER NA GAMELANG")

    print("""
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
- VIDA, ATAQUE e DEFESA recebem numeros inteiros.
- FIM encerra blocos de REPETIR e SE/SENAO.
""")


def mostrar_comandos():

    mostrar_titulo("COMANDOS DISPONIVEIS")

    print("""
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


# ==========================================================
# EXEMPLOS E EDITOR INTERATIVO
# ==========================================================

def exemplo_curto():

    return """CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
TURNO Arthur
MOVER Arthur DIREITA
ATACAR Arthur Goblin
DEFENDER Arthur
"""


def ler_codigo_interativo():

    mostrar_titulo("EDITOR SIMPLES DA GAMELANG")

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

            mostrar_aviso("Edicao cancelada.")
            return None

        if comando == "EXECUTAR":

            return "\n".join(linhas)

        linhas.append(linha)


# ==========================================================
# MENU PRINCIPAL
# ==========================================================

def executar_interativo():

    while True:

        print(BANNER)

        print(NEGRITO + "MENU PRINCIPAL" + RESET)

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
            pausar()

        elif opcao == "2":

            mostrar_comandos()
            pausar()

        elif opcao == "3":

            mostrar_titulo("EXEMPLO DE CODIGO")
            print(exemplo_curto())
            pausar()

        elif opcao == "4":

            codigo = ler_codigo_interativo()

            if codigo is not None:
                compilar_codigo(codigo, modo="visual")
                pausar()

        elif opcao == "5":

            caminho = (
                Path(__file__).parent
                / "exemplos"
                / "combate.gl"
            )

            try:
                codigo = caminho.read_text(encoding="utf-8")

            except OSError as erro:

                mostrar_erro(
                    f"Nao foi possivel abrir o exemplo: {erro}"
                )

            else:

                mostrar_sucesso(
                    f"Arquivo carregado: {caminho.name}"
                )

                compilar_codigo(codigo, modo="visual")

            pausar()

        elif opcao == "0":

            print("\nObrigado por conhecer a GameLang!")
            return

        else:

            mostrar_erro(
                "Opcao invalida. Escolha uma opcao do menu."
            )

            pausar(
                "Pressione ENTER para tentar novamente..."
            )


# ==========================================================
# EXECUCAO DE ARQUIVOS
# ==========================================================

def executar_arquivo(caminho, modo="visual"):

    try:
        codigo = Path(caminho).read_text(encoding="utf-8")

    except FileNotFoundError:

        mostrar_erro(f"Arquivo '{caminho}' nao encontrado.")
        return

    except OSError as erro:

        mostrar_erro(
            f"Nao foi possivel ler o arquivo: {erro}"
        )

        return

    compilar_codigo(codigo, modo=modo)


# ==========================================================
# INICIALIZACAO DO PROGRAMA
# ==========================================================

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

        modo = (
            "terminal"
            if len(sys.argv) >= 3 and sys.argv[2] == "--terminal"
            else "visual"
        )

        executar_arquivo(caminho, modo)
