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

    def desenhar(self, tela, tamanho_tile):
        x = self.coluna * tamanho_tile
        y = self.linha * tamanho_tile

        centro_x = x + tamanho_tile // 2
        centro_y = y + tamanho_tile // 2

        raio = tamanho_tile // 3

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
            center=(centro_x, y + 15)
        )

        tela.blit(texto, texto_rect)

        self.desenhar_barra_vida(
            tela,
            x,
            y,
            tamanho_tile
        )

    def desenhar_barra_vida(
        self,
        tela,
        x,
        y,
        tamanho_tile
    ):
        largura = tamanho_tile - 10
        altura = 8

        barra_x = x + 5
        barra_y = y + tamanho_tile - 12

        pygame.draw.rect(
            tela,
            (80, 80, 80),
            (barra_x, barra_y, largura, altura)
        )

        porcentagem = self.vida / self.vida_maxima

        largura_vida = int(
            largura * porcentagem
        )

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
