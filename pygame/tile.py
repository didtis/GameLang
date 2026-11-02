import pygame


class Tile:
    def __init__(self, x, y, tamanho):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.destacado = False

    def desenhar(self, tela):
        retangulo = pygame.Rect(
            self.x,
            self.y,
            self.tamanho,
            self.tamanho
        )

        pygame.draw.rect(
            tela,
            (70, 70, 70),
            retangulo
        )

        pygame.draw.rect(
            tela,
            (120, 120, 120),
            retangulo,
            1
        )

        if self.destacado:
            pygame.draw.rect(
                tela,
                (100, 180, 100),
                retangulo,
                4
            )
          
