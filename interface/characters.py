
import os
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

        # Localização das imagens
        pasta_assets = os.path.join(
            os.path.dirname(__file__),
            "assets"
        )

        # Seleciona a imagem conforme o personagem
        if self.nome.lower() == "arthur":
            caminho_imagem = os.path.join(
                pasta_assets,
                "arthur.png"
            )
            self.cor = (50, 100, 220)

        else:
            caminho_imagem = os.path.join(
                pasta_assets,
                "goblin.png"
            )
            self.cor = (180, 60, 60)

        # Carrega a imagem do personagem
        self.imagem = None

        try:
            self.imagem = pygame.image.load(
                caminho_imagem
            ).convert_alpha()

        except (pygame.error, FileNotFoundError):
            print(
                f"Aviso: imagem não encontrada para {self.nome}."
            )

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

        # Define o tamanho máximo do personagem
        largura_maxima = int(largura_tile * 0.85)
        altura_maxima = int(altura_tile * 0.75)

        if self.imagem:

            # Mantém a proporção original da imagem
            imagem_largura, imagem_altura = self.imagem.get_size()

            escala = min(
                largura_maxima / imagem_largura,
                altura_maxima / imagem_altura
            )

            nova_largura = max(
                1,
                int(imagem_largura * escala)
            )

            nova_altura = max(
                1,
                int(imagem_altura * escala)
            )

            # Usa scale para preservar o estilo pixel art
            imagem_redimensionada = pygame.transform.scale(
                self.imagem,
                (nova_largura, nova_altura)
            )

            imagem_rect = imagem_redimensionada.get_rect(
                center=(centro_x, centro_y - 3)
            )

            tela.blit(
                imagem_redimensionada,
                imagem_rect
            )

        else:

            # Desenho antigo como alternativa
            raio = int(min(largura_tile, altura_tile) / 3)

            pygame.draw.circle(
                tela,
                self.cor,
                (centro_x, centro_y),
                raio
            )

        # Nome do personagem
        fonte = pygame.font.Font(None, 24)

        texto = fonte.render(
            self.nome,
            True,
            (255, 255, 255)
        )

        texto_rect = texto.get_rect(
            center=(
                centro_x,
                centro_y - altura_maxima / 2 - 8
            )
        )

        tela.blit(texto, texto_rect)

        # Barra de vida
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
