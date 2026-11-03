
# Interpretador da GameLang - Sprint 4

from parser.ast import (
    CriarPersonagem,
    Atacar,
    Defender,
    Habilidade,
    Turno,
    Mover,
    Condicional,
    Repeticao,
    CondicaoVida
)


class Interpretador:

    def __init__(self):
        self.personagens = {}
        self.defendendo = {}
        self.posicoes = {}

    def executar(self, ast):
        print("=== EXECUÇÃO DO COMBATE ===")

        for comando in ast.comandos:
            self.executar_comando(comando)

        print("\n=== FIM DO COMBATE ===")

    def executar_comando(self, comando):

        if isinstance(comando, CriarPersonagem):
            self.criar_personagem(comando)

        elif isinstance(comando, Atacar):
            self.atacar(comando)

        elif isinstance(comando, Defender):
            self.defender(comando)

        elif isinstance(comando, Habilidade):
            self.habilidade(comando)

        elif isinstance(comando, Turno):
            self.turno(comando)

        elif isinstance(comando, Mover):
            self.mover(comando)

        elif isinstance(comando, Condicional):
            self.condicional(comando)

        elif isinstance(comando, Repeticao):
            self.repeticao(comando)

        else:
            raise ValueError(
                f"Comando não reconhecido: {type(comando).__name__}"
            )

    def criar_personagem(self, comando):

        if comando.nome in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.nome}' já foi criado"
            )

        self.personagens[comando.nome] = {
            "tipo": comando.tipo,
            "vida": comando.vida,
            "ataque": comando.ataque,
            "defesa": comando.defesa
        }

        self.defendendo[comando.nome] = False

        # Posições iniciais no tabuleiro
        if comando.tipo == "HEROI":
            self.posicoes[comando.nome] = {
                "linha": 3,
                "coluna": 2
            }
        else:
            self.posicoes[comando.nome] = {
                "linha": 3,
                "coluna": 6
            }

        print(
            f"{comando.nome} entrou no combate "
            f"(Vida: {comando.vida})"
        )

    def atacar(self, comando):

        if comando.atacante not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.atacante}' não foi criado"
            )

        if comando.alvo not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.alvo}' não foi criado"
            )

        atacante = self.personagens[comando.atacante]
        alvo = self.personagens[comando.alvo]

        pos_atacante = self.posicoes[comando.atacante]
        pos_alvo = self.posicoes[comando.alvo]

        # Distância entre os personagens no tabuleiro
        distancia = (
            abs(pos_atacante["linha"] - pos_alvo["linha"])
            + abs(pos_atacante["coluna"] - pos_alvo["coluna"])
        )

        # Ataque só funciona em casas vizinhas
        if distancia != 1:
            print(
                f"{comando.atacante} está longe demais "
                f"para atacar {comando.alvo}!"
            )
            return

        # Cálculo do dano
        dano = atacante["ataque"] - alvo["defesa"]

        if dano < 0:
            dano = 0

        # Verifica se o alvo está defendendo
        if self.defendendo[comando.alvo]:

            dano = dano // 2

            print(
                f"{comando.alvo} estava se defendendo!"
            )

            self.defendendo[comando.alvo] = False

        alvo["vida"] -= dano

        if alvo["vida"] < 0:
            alvo["vida"] = 0

        print(
            f"{comando.atacante} atacou {comando.alvo}!"
        )

        print(
            f"{comando.alvo} perdeu {dano} de vida."
        )

        print(
            f"Vida do {comando.alvo}: {alvo['vida']}"
        )

    def defender(self, comando):

        if comando.personagem not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.personagem}' não foi criado"
            )

        self.defendendo[comando.personagem] = True

        print(
            f"{comando.personagem} está se defendendo!"
        )

    def habilidade(self, comando):

        if comando.personagem not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.personagem}' não foi criado"
            )

        print(
            f"{comando.personagem} usou {comando.nome}!"
        )

    def turno(self, comando):

        if comando.personagem not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.personagem}' não foi criado"
            )

        print(
            f"Turno de {comando.personagem}"
        )

    def mover(self, comando):

        if comando.personagem not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.personagem}' não foi criado"
            )

        posicao = self.posicoes[comando.personagem]

        linha = posicao["linha"]
        coluna = posicao["coluna"]

        if comando.direcao == "CIMA":
            linha -= 1

        elif comando.direcao == "BAIXO":
            linha += 1

        elif comando.direcao == "ESQUERDA":
            coluna -= 1

        elif comando.direcao == "DIREITA":
            coluna += 1

        # Limites do tabuleiro: 8 linhas e 10 colunas
        if linha < 0 or linha >= 8 or coluna < 0 or coluna >= 10:
            print(
                f"{comando.personagem} não pode sair "
                f"dos limites do tabuleiro!"
            )
            return

        posicao["linha"] = linha
        posicao["coluna"] = coluna

        print(
            f"{comando.personagem} moveu-se para "
            f"{comando.direcao}"
        )

        print(
            f"Posição de {comando.personagem}: "
            f"linha {linha}, coluna {coluna}"
        )

    def condicional(self, comando):

        resultado = self.verificar_condicao(
            comando.condicao
        )

        if resultado:
            print("Condição verdadeira.")

            for subcomando in comando.comandos:
                self.executar_comando(subcomando)

        elif comando.senao is not None:
            print("Condição falsa.")

            for subcomando in comando.senao:
                self.executar_comando(subcomando)

    def verificar_condicao(self, condicao):

        if condicao.personagem not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{condicao.personagem}' não foi criado"
            )

        personagem = self.personagens[condicao.personagem]

        vida = personagem["vida"]
        valor = condicao.valor

        if condicao.operador == "<=":
            return vida <= valor

        elif condicao.operador == ">=":
            return vida >= valor

        elif condicao.operador == "<":
            return vida < valor

        elif condicao.operador == ">":
            return vida > valor

        elif condicao.operador == "==":
            return vida == valor

        return False

    def repeticao(self, comando):

        print(
            f"Repetindo comandos "
            f"{comando.quantidade} vezes."
        )

        for i in range(comando.quantidade):

            for subcomando in comando.comandos:
                self.executar_comando(subcomando)
