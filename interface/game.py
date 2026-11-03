
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
            linhas=8,
            colunas=10,
            tamanho_tile=70
        )

        # Carrega a imagem da masmorra
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

        self.personagens = []

        self.executando = True
        self.finalizado = False

        self.fonte = pygame.font.Font(None, 25)
        self.fonte_pequena = pygame.font.Font(None, 21)

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
                    comando.vida,
                    comando.ataque,
                    comando.defesa
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

        if self.indice_comando >= len(self.comandos):

            self.finalizado = True
            self.board.limpar_destaques()
            self.mensagem = "Combate finalizado!"
            return

        comando = self.comandos[self.indice_comando]

        try:

            self.interpretador.executar_comando(comando)

            self.atualizar_personagens()

            self.mensagem = (
                f"Executado: {self.formatar_comando(comando)}"
            )

            self.indice_comando += 1

            if self.indice_comando >= len(self.comandos):

                self.finalizado = True
                self.board.limpar_destaques()
                self.mensagem = "Todos os comandos foram executados!"

            else:

                self.atualizar_destaques_proximo_comando()

        except ValueError as erro:

            self.mensagem = str(erro)
            self.finalizado = True
            self.board.limpar_destaques()

    def atualizar_destaques_proximo_comando(self):

        self.board.limpar_destaques()

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

            personagem.vida = dados["vida"]

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

        # Desenha a masmorra como fundo
        self.tela.blit(
            self.fundo,
            (0, 0)
        )

        # Desenha somente os destaques verdes
        self.board.desenhar_destaques(self.tela)

        # Desenha os personagens
        for personagem in self.personagens:

            personagem.desenhar(
                self.tela,
                self.board.tamanho_tile
            )

        self.desenhar_painel()

        pygame.display.flip()

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
                "Execucao encerrada    ESC: sair",
                True,
                (180, 180, 180)
            )

        self.tela.blit(
            texto_ajuda,
            (10, ALTURA_TABULEIRO + 48)
        )
