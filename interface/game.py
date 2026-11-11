
import os
import pygame

from .board import Board
from .characters import Character

from parser.ast import (
    CriarPersonagem,
    Atacar,
    Defender,
    Habilidade,
    Turno,
    Mover,
    Condicional,
    Repeticao
)


LARGURA = 700
ALTURA_TABULEIRO = 560
ALTURA_PAINEL = 90
ALTURA = ALTURA_TABULEIRO + ALTURA_PAINEL
FPS = 60


class Game:

    def __init__(self, interpretador, comandos):

        pygame.init()

        self.tela = pygame.display.set_mode(
            (LARGURA, ALTURA)
        )

        pygame.display.set_caption(
            "GameLang - Combate"
        )

        self.relogio = pygame.time.Clock()

        self.board = Board(
            linhas=7,
            colunas=12
        )

        caminho_fundo = os.path.join(
            os.path.dirname(__file__),
            "assets",
            "masmorra.png"
        )

        self.fundo = pygame.image.load(
            caminho_fundo
        ).convert()

        self.fundo = pygame.transform.scale(
            self.fundo,
            (LARGURA, ALTURA_TABULEIRO)
        )

        self.interpretador = interpretador
        self.comandos = comandos
        self.indice_comando = 0

        # Controle visual da repetição
        self.repeticao_ativa = None

        self.personagens = []

        self.executando = True
        self.finalizado = False
        self.resultado_exibido = False

        self.fonte = pygame.font.Font(None, 25)
        self.fonte_pequena = pygame.font.Font(None, 21)
        self.fonte_resultado = pygame.font.Font(None, 76)

        self.mensagem = "Pressione ESPACO para iniciar."

        self.carregar_personagens_iniciais()

    def carregar_personagens_iniciais(self):

        for comando in self.comandos:

            if isinstance(comando, CriarPersonagem):

                if comando.tipo == "HEROI":
                    linha = 3
                    coluna = 2
                else:
                    linha = 3
                    coluna = 6

                personagem = Character(
                    comando.nome,
                    linha,
                    coluna,
                    int(comando.vida),
                    int(comando.ataque),
                    int(comando.defesa)
                )

                self.personagens.append(personagem)

    def executar(self):

        while self.executando:

            self.processar_eventos()
            self.desenhar()

            self.relogio.tick(FPS)

        pygame.quit()

    def processar_eventos(self):

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                self.executando = False

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
                    self.executando = False

                elif evento.key == pygame.K_SPACE:
                    self.proximo_comando()

    def proximo_comando(self):

        if self.finalizado:
            return

        # Se existe uma repetição em andamento,
        # executa somente o próximo comando interno.
        if self.repeticao_ativa is not None:
            self.executar_proximo_comando_repeticao()
            return

        if self.indice_comando >= len(self.comandos):

            self.finalizado = True
            self.board.limpar_destaques()
            self.mensagem = "Combate finalizado!"
            return

        comando = self.comandos[self.indice_comando]

        try:

            # A repetição será controlada pelo Pygame,
            # em vez de ser executada inteira de uma vez.
            if isinstance(comando, Repeticao):

                quantidade = int(comando.quantidade)

                # Mantém o comportamento original para
                # repetições vazias ou com quantidade zero.
                if quantidade <= 0 or not comando.comandos:

                    self.interpretador.executar_comando(comando)
                    self.atualizar_personagens()
                    self.indice_comando += 1

                    self.finalizar_ou_continuar()

                    return

                self.repeticao_ativa = {
                    "comando": comando,
                    "quantidade": quantidade,
                    "iteracao": 0,
                    "indice_interno": 0
                }

                self.mensagem = (
                    f"REPETIR {quantidade} iniciado. "
                    "Pressione ESPACO para executar."
                )

                self.atualizar_destaques_proximo_comando()
                return

            # Execução normal dos demais comandos
            self.interpretador.executar_comando(comando)

            self.atualizar_personagens()

            self.mensagem = (
                f"Executado: {self.formatar_comando(comando)}"
            )

            self.indice_comando += 1

            self.finalizar_ou_continuar()

        except ValueError as erro:

            self.mensagem = str(erro)
            self.finalizado = True
            self.repeticao_ativa = None
            self.board.limpar_destaques()

    def executar_proximo_comando_repeticao(self):

        estado = self.repeticao_ativa

        comando_repeticao = estado["comando"]
        comandos_internos = comando_repeticao.comandos

        iteracao = estado["iteracao"]
        indice_interno = estado["indice_interno"]
        quantidade = estado["quantidade"]

        if indice_interno >= len(comandos_internos):
            return

        comando = comandos_internos[indice_interno]

        try:

            # Executa apenas um comando interno por ESPACO.
            self.interpretador.executar_comando(comando)

            self.atualizar_personagens()

            estado["indice_interno"] += 1

            # Verifica se o combate terminou durante a repetição.
            if self.verificar_resultado_combate():
                return

            # Verifica se todos os comandos desta iteração
            # foram executados.
            if estado["indice_interno"] >= len(comandos_internos):

                estado["iteracao"] += 1

                # Todas as iterações foram concluídas.
                if estado["iteracao"] >= quantidade:

                    self.repeticao_ativa = None
                    self.indice_comando += 1

                    self.mensagem = (
                        f"REPETIR {quantidade} concluído!"
                    )

                    self.finalizar_ou_continuar()

                    return

                # Prepara a próxima iteração.
                estado["indice_interno"] = 0

                self.mensagem = (
                    f"REPETIR: iteração "
                    f"{estado['iteracao']} de {quantidade} concluída."
                )

            else:

                self.mensagem = (
                    f"REPETIR: {self.formatar_comando(comando)} "
                    f"(iteração {iteracao + 1}/{quantidade})"
                )

            self.atualizar_destaques_proximo_comando()

        except ValueError as erro:

            self.mensagem = str(erro)
            self.finalizado = True
            self.repeticao_ativa = None
            self.board.limpar_destaques()

    def finalizar_ou_continuar(self):

        if self.verificar_resultado_combate():
            return

        if self.indice_comando >= len(self.comandos):

            self.finalizado = True
            self.board.limpar_destaques()

            if self.repeticao_ativa is None:
                self.mensagem = "Todos os comandos foram executados!"

        else:

            self.atualizar_destaques_proximo_comando()

    def verificar_resultado_combate(self):

        if not self.interpretador.combate_encerrado:
            return False

        self.finalizado = True
        self.resultado_exibido = True
        self.repeticao_ativa = None

        self.board.limpar_destaques()

        if self.interpretador.resultado == "VITORIA":

            self.mensagem = (
                "VITÓRIA! Todos os inimigos foram derrotados!"
            )

        elif self.interpretador.resultado == "DERROTA":

            self.mensagem = (
                "DERROTA! Todos os heróis foram derrotados!"
            )

        return True

    def atualizar_destaques_proximo_comando(self):

        self.board.limpar_destaques()

        # Se estiver dentro de REPETIR, destaca
        # a movimentação do próximo comando interno.
        if self.repeticao_ativa is not None:

            estado = self.repeticao_ativa

            comandos = estado["comando"].comandos
            indice = estado["indice_interno"]

            if indice >= len(comandos):
                return

            proximo_comando = comandos[indice]

        else:

            if self.indice_comando >= len(self.comandos):
                return

            proximo_comando = self.comandos[self.indice_comando]

        if not isinstance(proximo_comando, Mover):
            return

        nome = proximo_comando.personagem

        if nome not in self.interpretador.posicoes:
            return

        posicao = self.interpretador.posicoes[nome]

        linha = posicao["linha"]
        coluna = posicao["coluna"]

        ocupadas = []

        for outro_nome, outra_posicao in self.interpretador.posicoes.items():

            if outro_nome != nome:

                ocupadas.append((
                    outra_posicao["linha"],
                    outra_posicao["coluna"]
                ))

        self.board.destacar_movimentos_possiveis(
            linha,
            coluna,
            ocupadas
        )

    def atualizar_personagens(self):

        for personagem in self.personagens:

            nome = personagem.nome

            if nome not in self.interpretador.personagens:
                continue

            if nome not in self.interpretador.posicoes:
                continue

            dados = self.interpretador.personagens[nome]
            posicao = self.interpretador.posicoes[nome]

            personagem.vida = int(dados["vida"])

            personagem.mover(
                posicao["linha"],
                posicao["coluna"]
            )

    def formatar_comando(self, comando):

        if isinstance(comando, CriarPersonagem):
            return f"CRIAR {comando.tipo} {comando.nome}"

        elif isinstance(comando, Atacar):
            return f"ATACAR {comando.atacante} {comando.alvo}"

        elif isinstance(comando, Defender):
            return f"DEFENDER {comando.personagem}"

        elif isinstance(comando, Habilidade):
            return f"HABILIDADE {comando.personagem} {comando.nome}"

        elif isinstance(comando, Turno):
            return f"TURNO {comando.personagem}"

        elif isinstance(comando, Mover):
            return f"MOVER {comando.personagem} {comando.direcao}"

        elif isinstance(comando, Condicional):
            return "SE (condição)"

        elif isinstance(comando, Repeticao):
            return f"REPETIR {comando.quantidade}"

        return "Comando"

    def desenhar(self):

        self.tela.blit(
            self.fundo,
            (0, 0)
        )

        self.board.desenhar_destaques(self.tela)

        for personagem in self.personagens:

            centro_x, centro_y = self.board.obter_centro(
                personagem.linha,
                personagem.coluna
            )

            if personagem.nome.lower() == "goblin":
                centro_x -= 5

            personagem.desenhar(
                self.tela,
                centro_x,
                centro_y,
                self.board.largura_tile,
                self.board.altura_tile
            )

        if self.resultado_exibido:
            self.desenhar_resultado()

        self.desenhar_painel()

        pygame.display.flip()

    def desenhar_resultado(self):

        resultado = self.interpretador.resultado

        if resultado == "VITORIA":
            texto = "VITORIA!"
            cor = (80, 230, 100)

        else:
            texto = "DERROTA!"
            cor = (230, 70, 70)

        superficie = self.fonte_resultado.render(
            texto,
            True,
            cor
        )

        retangulo = superficie.get_rect(
            center=(LARGURA // 2, ALTURA_TABULEIRO // 2)
        )

        fundo = pygame.Surface(
            (retangulo.width + 40, retangulo.height + 30),
            pygame.SRCALPHA
        )

        fundo.fill((15, 15, 25, 210))

        fundo_rect = fundo.get_rect(
            center=retangulo.center
        )

        self.tela.blit(
            fundo,
            fundo_rect
        )

        self.tela.blit(
            superficie,
            retangulo
        )

    def desenhar_painel(self):

        pygame.draw.rect(
            self.tela,
            (25, 25, 35),
            (0, ALTURA_TABULEIRO, LARGURA, ALTURA_PAINEL)
        )

        texto_comando = self.fonte.render(
            self.mensagem,
            True,
            (255, 255, 255)
        )

        self.tela.blit(
            texto_comando,
            (10, ALTURA_TABULEIRO + 10)
        )

        if not self.finalizado:

            texto_ajuda = self.fonte_pequena.render(
                "ESPACO: proximo comando    ESC: sair",
                True,
                (180, 180, 180)
            )

        else:

            texto_ajuda = self.fonte_pequena.render(
                "Combate encerrado    ESC: sair",
                True,
                (180, 180, 180)
            )

        self.tela.blit(
            texto_ajuda,
            (10, ALTURA_TABULEIRO + 48)
        )
