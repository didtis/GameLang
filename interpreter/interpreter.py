
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
        self.resultado = None
        self.combate_encerrado = False

    def executar(self, ast):
        print("=== EXECUÇÃO DO COMBATE ===")

        for comando in ast.comandos:

            if self.combate_encerrado:
                break

            self.executar_comando(comando)

        print("\n=== FIM DO COMBATE ===")

    def executar_comando(self, comando):

        if self.combate_encerrado:
            return

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

        vida = int(comando.vida)
        ataque = int(comando.ataque)
        defesa = int(comando.defesa)

        self.personagens[comando.nome] = {
            "tipo": comando.tipo,
            "vida": vida,
            "ataque": ataque,
            "defesa": defesa
        }

        self.defendendo[comando.nome] = False

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
            f"(Vida: {vida})"
        )

    def personagem_derrotado(self, nome):

        return self.personagens[nome]["vida"] <= 0

    def verificar_fim_combate(self):

        herois = [
            nome for nome, dados in self.personagens.items()
            if dados["tipo"] == "HEROI"
        ]

        inimigos = [
            nome for nome, dados in self.personagens.items()
            if dados["tipo"] == "INIMIGO"
        ]

        if not herois or not inimigos:
            return

        todos_herois_derrotados = all(
            self.personagem_derrotado(nome)
            for nome in herois
        )

        todos_inimigos_derrotados = all(
            self.personagem_derrotado(nome)
            for nome in inimigos
        )

        if todos_herois_derrotados:
            self.resultado = "DERROTA"
            self.combate_encerrado = True
            print("\n=== DERROTA! TODOS OS HERÓIS FORAM DERROTADOS! ===")

        elif todos_inimigos_derrotados:
            self.resultado = "VITORIA"
            self.combate_encerrado = True
            print("\n=== VITÓRIA! TODOS OS INIMIGOS FORAM DERROTADOS! ===")

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

        if self.personagem_derrotado(comando.atacante):
            print(
                f"{comando.atacante} está derrotado "
                f"e não pode atacar!"
            )
            return

        if self.personagem_derrotado(comando.alvo):
            print(
                f"{comando.alvo} já está derrotado!"
            )
            return

        atacante = self.personagens[comando.atacante]
        alvo = self.personagens[comando.alvo]

        pos_atacante = self.posicoes[comando.atacante]
        pos_alvo = self.posicoes[comando.alvo]

        distancia = (
            abs(pos_atacante["linha"] - pos_alvo["linha"])
            + abs(pos_atacante["coluna"] - pos_alvo["coluna"])
        )

        if distancia != 1:
            print(
                f"{comando.atacante} está longe demais "
                f"para atacar {comando.alvo}!"
            )
            return

        dano = atacante["ataque"] - alvo["defesa"]
        dano = max(0, dano)

        if self.defendendo[comando.alvo]:

            dano = dano // 2

            print(
                f"{comando.alvo} estava se defendendo!"
            )

            self.defendendo[comando.alvo] = False

        alvo["vida"] = max(0, alvo["vida"] - dano)

        print(
            f"{comando.atacante} atacou {comando.alvo}!"
        )

        print(
            f"{comando.alvo} perdeu {dano} de vida."
        )

        print(
            f"Vida do {comando.alvo}: {alvo['vida']}"
        )

        if self.personagem_derrotado(comando.alvo):
            print(f"{comando.alvo} foi derrotado!")

        self.verificar_fim_combate()

    def defender(self, comando):

        if comando.personagem not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.personagem}' não foi criado"
            )

        if self.personagem_derrotado(comando.personagem):
            print(
                f"{comando.personagem} está derrotado "
                f"e não pode se defender!"
            )
            return

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

        if self.personagem_derrotado(comando.personagem):
            print(
                f"{comando.personagem} está derrotado "
                f"e não pode usar habilidades!"
            )
            return

        print(
            f"{comando.personagem} usou {comando.nome}!"
        )

    def turno(self, comando):

        if comando.personagem not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.personagem}' não foi criado"
            )

        if self.personagem_derrotado(comando.personagem):
            print(
                f"{comando.personagem} está derrotado. "
                f"Seu turno foi ignorado."
            )
            return

        print(
            f"Turno de {comando.personagem}"
        )

    def mover(self, comando):

        if comando.personagem not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{comando.personagem}' não foi criado"
            )

        if self.personagem_derrotado(comando.personagem):
            print(
                f"{comando.personagem} está derrotado "
                f"e não pode se movimentar!"
            )
            return

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

        # Verifica os limites do tabuleiro
        if linha < 0 or linha >= 7 or coluna < 0 or coluna >= 12:
            print(
                f"{comando.personagem} não pode sair "
                f"dos limites do tabuleiro!"
            )
            return

        # Verifica se outra personagem ocupa a posição
        for outro_nome, outra_posicao in self.posicoes.items():

            if outro_nome == comando.personagem:
                continue

            if (
                outra_posicao["linha"] == linha
                and outra_posicao["coluna"] == coluna
            ):
                print(
                    f"{comando.personagem} não pode se mover: "
                    f"a posição está ocupada por {outro_nome}!"
                )
                return

        # Atualiza a posição somente se o movimento for válido
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

                if self.combate_encerrado:
                    break

                self.executar_comando(subcomando)

        elif comando.senao is not None:
            print("Condição falsa.")

            for subcomando in comando.senao:

                if self.combate_encerrado:
                    break

                self.executar_comando(subcomando)

    def verificar_condicao(self, condicao):

        if condicao.personagem not in self.personagens:
            raise ValueError(
                f"Erro semântico: personagem "
                f"'{condicao.personagem}' não foi criado"
            )

        personagem = self.personagens[condicao.personagem]

        vida = personagem["vida"]
        valor = int(condicao.valor)

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

            if self.combate_encerrado:
                break

            for subcomando in comando.comandos:

                if self.combate_encerrado:
                    break

                self.executar_comando(subcomando)
