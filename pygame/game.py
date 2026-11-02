import pygame

from .board import Board
from .characters import Character


LARGURA = 700
ALTURA = 560
FPS = 60


class Game:
    def __init__(self):
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

        self.personagens = [
            Character(
                "Arthur",
                2,
                2,
                100,
                20,
                5
            ),
            Character(
                "Goblin",
                5,
                7,
                50,
                10,
                5
            )
        ]

        self.executando = True

    def executar(self):
        while self.executando:
            self.processar_eventos()
            self.atualizar()
            self.desenhar()

            self.relogio.tick(FPS)

        pygame.quit()

    def processar_eventos(self):
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                self.executando = False

    def atualizar(self):
        pass

    def desenhar(self):
        self.tela.fill((30, 30, 30))

        self.board.desenhar(self.tela)

        for personagem in self.personagens:
            personagem.desenhar(
                self.tela,
                self.board.tamanho_tile
            )

        pygame.display.flip()


if __name__ == "__main__":
    jogo = Game()
    jogo.executar()
