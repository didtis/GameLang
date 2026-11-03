
import pygame


class Board:

    def __init__(
        self,
        linhas=7,
        colunas=12,
        tamanho_tile=70,
        inicio_x=48,
        inicio_y=66,
        largura_tile=51.5,
        altura_tile=62.4
    ):

        self.linhas = linhas
        self.colunas = colunas

        self.inicio_x = inicio_x
        self.inicio_y = inicio_y

        self.largura_tile = largura_tile
        self.altura_tile = altura_tile

        self.tamanho_tile = tamanho_tile

        self.tiles = []

        for linha in range(linhas):

            linha_tiles = []

            for coluna in range(colunas):

                linha_tiles.append({
                    "destacado": False
                })

            self.tiles.append(linha_tiles)

    def desenhar_destaques(self, tela):

        for linha in range(self.linhas):

            for coluna in range(self.colunas):

                tile = self.tiles[linha][coluna]

                if tile["destacado"]:

                    x = self.inicio_x + (
                        coluna * self.largura_tile
                    )

                    y = self.inicio_y + (
                        linha * self.altura_tile
                    )

                    retangulo = pygame.Rect(
                        round(x),
                        round(y),
                        round(self.largura_tile),
                        round(self.altura_tile)
                    )

                    pygame.draw.rect(
                        tela,
                        (100, 180, 100),
                        retangulo,
                        4
                    )

    def destacar_movimento(self, linha, coluna):

        if self.posicao_valida(linha, coluna):

            self.tiles[linha][coluna]["destacado"] = True

    def destacar_movimentos_possiveis(
        self,
        linha,
        coluna,
        ocupadas=None
    ):

        self.limpar_destaques()

        if ocupadas is None:
            ocupadas = []

        movimentos = [
            (linha - 1, coluna),
            (linha + 1, coluna),
            (linha, coluna - 1),
            (linha, coluna + 1)
        ]

        for nova_linha, nova_coluna in movimentos:

            if not self.posicao_valida(
                nova_linha,
                nova_coluna
            ):
                continue

            if (nova_linha, nova_coluna) in ocupadas:
                continue

            self.destacar_movimento(
                nova_linha,
                nova_coluna
            )

    def limpar_destaques(self):

        for linha in self.tiles:

            for tile in linha:

                tile["destacado"] = False

    def posicao_valida(self, linha, coluna):

        return (
            0 <= linha < self.linhas
            and 0 <= coluna < self.colunas
        )

    def obter_centro(self, linha, coluna):

        x = (
            self.inicio_x
            + coluna * self.largura_tile
            + self.largura_tile / 2
        )

        y = (
            self.inicio_y
            + linha * self.altura_tile
            + self.altura_tile / 2
        )

        return round(x), round(y)
