
from .tile import Tile


class Board:

    def __init__(self, linhas=8, colunas=10, tamanho_tile=70):

        self.linhas = linhas
        self.colunas = colunas
        self.tamanho_tile = tamanho_tile

        self.tiles = []

        for linha in range(linhas):

            linha_tiles = []

            for coluna in range(colunas):

                x = coluna * tamanho_tile
                y = linha * tamanho_tile

                tile = Tile(x, y, tamanho_tile)

                linha_tiles.append(tile)

            self.tiles.append(linha_tiles)

    def desenhar(self, tela):

        for linha in self.tiles:

            for tile in linha:

                tile.desenhar(tela)

    def destacar_movimento(self, linha, coluna):

        if self.posicao_valida(linha, coluna):

            self.tiles[linha][coluna].destacado = True

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

            if not self.posicao_valida(nova_linha, nova_coluna):
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

                tile.destacado = False

    def posicao_valida(self, linha, coluna):

        return (
            0 <= linha < self.linhas
            and 0 <= coluna < self.colunas
        )
