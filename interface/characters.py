
import pygame


class Character:

    def __init__(self, nome, linha, coluna, vida, ataque, defesa):

        self.nome = nome
        self.linha = linha
        self.coluna = coluna

        self.vida = vida
        self.vida_maxima = vida
        self.ataque = ataque
        self.defesa = defesa

    def mover(self, linha, coluna):

        self.linha = linha
        self.coluna = coluna

    def desenhar(
        self,
        tela,
        centro_x,
        centro_y,
        largura_tile,
        altura_tile
    ):

        raio = int(min(largura_tile, altura_tile) / 3)

        if self.nome.lower() == "arthur":
            cor = (50, 100, 220)
        else:
            cor = (180, 60, 60)

        pygame.draw.circle(
            tela,
            cor,
            (centro_x, centro_y),
            raio
        )

        fonte = pygame.font.Font(None, 24)

        texto = fonte.render(
            self.nome,
            True,
            (255, 255, 255)
        )

        texto_rect = texto.get_rect(
            center=(centro_x, centro_y - raio - 12)
        )

        tela.blit(texto, texto_rect)

        self.desenhar_barra_vida(
            tela,
            centro_x,
            centro_y,
            largura_tile,
            altura_tile
        )

    def desenhar_barra_vida(
        self,
        tela,
        centro_x,
        centro_y,
        largura_tile,
        altura_tile
    ):

        largura = int(largura_tile - 10)
        altura = 7

        barra_x = int(centro_x - largura / 2)
        barra_y = int(
            centro_y + altura_tile / 2 - altura - 5
        )

        pygame.draw.rect(
            tela,
            (80, 80, 80),
            (barra_x, barra_y, largura, altura)
        )

        porcentagem = max(
            0,
            min(1, self.vida / self.vida_maxima)
        )

        largura_vida = int(largura * porcentagem)

        pygame.draw.rect(
            tela,
            (60, 200, 80),
            (
                barra_x,
                barra_y,
                largura_vida,
                altura
            )
        )
