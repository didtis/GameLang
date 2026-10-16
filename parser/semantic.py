# Análise semântica da GameLang - Sprint 3


class TabelaSimbolos:
    def __init__(self):
        self.simbolos = {}

    def adicionar(self, nome, tipo, vida, ataque, defesa):
        if nome in self.simbolos:
            raise ValueError(
                f"Erro semântico: personagem '{nome}' já foi criado"
            )

        self.simbolos[nome] = {
            "tipo": tipo,
            "vida": vida,
            "ataque": ataque,
            "defesa": defesa
        }

    def existe(self, nome):
        return nome in self.simbolos

    def obter(self, nome):
        if not self.existe(nome):
            raise ValueError(
                f"Erro semântico: personagem '{nome}' não foi criado"
            )

        return self.simbolos[nome]
