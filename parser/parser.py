# Parser da GameLang - Sprint 3

from .ast import (
    Programa,
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


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicao = 0

    def token_atual(self):
        if self.posicao < len(self.tokens):
            return self.tokens[self.posicao]
        return None

    def avancar(self):
        self.posicao += 1

    def erro(self, mensagem):
        raise SyntaxError(f"Erro sintático: {mensagem}")

    def esperar(self, tipo):
        token = self.token_atual()

        if token is None:
            self.erro(f"esperado {tipo}, mas o código terminou")

        if token[0] != tipo:
            self.erro(
                f"esperado {tipo}, mas encontrado {token[0]} ('{token[1]}')"
            )

        self.avancar()
        return token

    def programa(self):
        comandos = []

        while self.token_atual() is not None:
            comandos.append(self.comando())

        return Programa(comandos)

    def comando(self):
        token = self.token_atual()

        if token is None:
            return None

        tipo = token[0]

        if tipo == "CRIAR":
            return self.criacao()

        elif tipo == "ATACAR":
            return self.ataque()

        elif tipo == "DEFENDER":
            return self.defesa()

        elif tipo == "HABILIDADE":
            return self.habilidade()

        elif tipo == "TURNO":
            return self.turno()

        elif tipo == "MOVER":
            return self.movimentacao()

        elif tipo == "SE":
            return self.condicional()

        elif tipo == "REPETIR":
            return self.repeticao()

        else:
            self.erro(
                f"comando esperado, mas encontrado '{token[1]}'"
            )

    def criacao(self):
        self.esperar("CRIAR")

        token = self.token_atual()

        if token is None or token[0] not in {"HEROI", "INIMIGO"}:
            self.erro("esperado HEROI ou INIMIGO")

        tipo = token[1]
        self.avancar()

        nome = self.esperar("IDENTIFICADOR")[1]
        self.esperar("VIDA")
        vida = self.esperar("NUMERO")[1]
        self.esperar("ATAQUE")
        ataque = self.esperar("NUMERO")[1]
        self.esperar("DEFESA")
        defesa = self.esperar("NUMERO")[1]

        return CriarPersonagem(
            tipo,
            nome,
            vida,
            ataque,
            defesa
        )

    def ataque(self):
        self.esperar("ATACAR")

        atacante = self.esperar("IDENTIFICADOR")[1]
        alvo = self.esperar("IDENTIFICADOR")[1]

        return Atacar(atacante, alvo)

    def defesa(self):
        self.esperar("DEFENDER")

        personagem = self.esperar("IDENTIFICADOR")[1]

        return Defender(personagem)

    def habilidade(self):
        self.esperar("HABILIDADE")

        personagem = self.esperar("IDENTIFICADOR")[1]
        nome = self.esperar("IDENTIFICADOR")[1]

        return Habilidade(personagem, nome)

    def turno(self):
        self.esperar("TURNO")

        personagem = self.esperar("IDENTIFICADOR")[1]

        return Turno(personagem)

    def movimentacao(self):
        self.esperar("MOVER")

        personagem = self.esperar("IDENTIFICADOR")[1]

        direcoes = {
            "CIMA",
            "BAIXO",
            "ESQUERDA",
            "DIREITA"
        }

        token = self.token_atual()

        if token is None or token[0] not in direcoes:
            self.erro("direção esperada")

        direcao = token[1]
        self.avancar()

        return Mover(personagem, direcao)

    def condicional(self):
        self.esperar("SE")

        self.esperar("VIDA")
        personagem = self.esperar("IDENTIFICADOR")[1]
        operador = self.esperar("OPERADOR_RELACIONAL")[1]
        valor = self.esperar("NUMERO")[1]

        condicao = CondicaoVida(
            personagem,
            operador,
            valor
        )

        comandos = []
        comandos_senao = None

        while self.token_atual() is not None:

            if self.token_atual()[0] == "SENAO":
                self.avancar()

                comandos_senao = []

                while (
                    self.token_atual() is not None
                    and self.token_atual()[0] != "FIM"
                ):
                    comandos_senao.append(self.comando())

                break

            if self.token_atual()[0] == "FIM":
                break

            comandos.append(self.comando())

        self.esperar("FIM")

        return Condicional(
            condicao,
            comandos,
            comandos_senao
        )

    def repeticao(self):
        self.esperar("REPETIR")

        quantidade = self.esperar("NUMERO")[1]

        comandos = []

        while (
            self.token_atual() is not None
            and self.token_atual()[0] != "FIM"
        ):
            comandos.append(self.comando())

        self.esperar("FIM")

        return Repeticao(
            quantidade,
            comandos
        )
