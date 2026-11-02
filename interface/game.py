import pygame

from .board import Board
from .characters import Character


LARGURA = 700
ALTURA = 560
FPS = 60


class Game:
    def __init__(self, personagens=None):
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

        self.personagens = []

        if personagens is not None:
            self.carregar_personagens(personagens)

        self.executando = True

    def carregar_personagens(self, personagens):
        """
        Recebe os personagens do interpretador
        e cria a representação visual deles.
        """

        for nome, dados in personagens.items():

            linha = dados.get("linha", 0)
            coluna = dados.get("coluna", 0)

            personagem = Character(
                nome,
                linha,
                coluna,
                dados["vida"],
                dados["ataque"],
                dados["defesa"]
            )

            self.personagens.append(personagem)

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

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_ESCAPE:
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

    personagens = {
        "Arthur": {
            "tipo": "HEROI",
            "vida": 100,
            "ataque": 20,
            "defesa": 5,
            "linha": 3,
            "coluna": 2
        },

        "Goblin": {
            "tipo": "INIMIGO",
            "vida": 50,
            "ataque": 10,
            "defesa": 5,
            "linha": 3,
            "coluna": 6
        }
    }

    jogo = Game(personagens)
    jogo.executar()
