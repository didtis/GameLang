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

    def limpar_destaques(self):
        for linha in self.tiles:
            for tile in linha:
                tile.destacado = False

    def posicao_valida(self, linha, coluna):
        return (
            0 <= linha < self.linhas
            and 0 <= coluna < self.colunas
        )
      
