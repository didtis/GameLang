# Parser da GameLang - Sprint 3

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
        while self.token_atual() is not None:
            self.comando()

        return True

    def comando(self):
        token = self.token_atual()

        if token is None:
            return

        tipo = token[0]

        if tipo == "CRIAR":
            self.criacao()

        elif tipo == "ATACAR":
            self.ataque()

        elif tipo == "DEFENDER":
            self.defesa()

        elif tipo == "HABILIDADE":
            self.habilidade()

        elif tipo == "TURNO":
            self.turno()

        elif tipo == "MOVER":
            self.movimentacao()

        elif tipo == "SE":
            self.condicional()

        elif tipo == "REPETIR":
            self.repeticao()

        else:
            self.erro(
                f"comando esperado, mas encontrado '{token[1]}'"
            )

   

    def ataque(self):
        self.esperar("ATACAR")
        self.esperar("IDENTIFICADOR")
        self.esperar("IDENTIFICADOR")

    def defesa(self):
        self.esperar("DEFENDER")
        self.esperar("IDENTIFICADOR")

    def habilidade(self):
        self.esperar("HABILIDADE")
        self.esperar("IDENTIFICADOR")
        self.esperar("IDENTIFICADOR")

    def turno(self):
        self.esperar("TURNO")
        self.esperar("IDENTIFICADOR")

    def movimentacao(self):
        self.esperar("MOVER")
        self.esperar("IDENTIFICADOR")

        direcoes = {
            "CIMA",
            "BAIXO",
            "ESQUERDA",
            "DIREITA"
        }

        token = self.token_atual()

        if token is None or token[0] not in direcoes:
            self.erro("direção esperada")

        self.avancar()

    def condicional(self):
        self.esperar("SE")

        self.esperar("VIDA")
        self.esperar("IDENTIFICADOR")
        self.esperar("OPERADOR_RELACIONAL")
        self.esperar("NUMERO")

        while self.token_atual() is not None:
            if self.token_atual()[0] == "SENAO":
                self.avancar()

                while (
                    self.token_atual() is not None
                    and self.token_atual()[0] != "FIM"
                ):
                    self.comando()

                break

            if self.token_atual()[0] == "FIM":
                break

            self.comando()

        self.esperar("FIM")

    def repeticao(self):
        self.esperar("REPETIR")
        self.esperar("NUMERO")

        while (
            self.token_atual() is not None
            and self.token_atual()[0] != "FIM"
        ):
            self.comando()

        self.esperar("FIM")
