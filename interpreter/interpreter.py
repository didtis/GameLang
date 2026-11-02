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

    def criar_personagem(self, comando):

        self.personagens[comando.nome] = {
            "tipo": comando.tipo,
            "vida": comando.vida,
            "ataque": comando.ataque,
            "defesa": comando.defesa
        }

        self.defendendo[comando.nome] = False

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

        dano = atacante["ataque"] - alvo["defesa"]

        if dano < 0:
            dano = 0

        if self.defendendo[comando.alvo]:

            dano = dano // 2

            print(
                f"{comando.alvo} estava se defendendo!"
            )

            self.defendendo[comando.alvo] = False

        alvo["vida"] -= dano

        print(
            f"{comando.atacante} atacou "
            f"{comando.alvo}!"
        )

        print(
            f"{comando.alvo} perdeu {dano} de vida."
        )

        print(
            f"Vida do {comando.alvo}: "
            f"{alvo['vida']}"
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
            f"{comando.personagem} usou "
            f"{comando.nome}!"
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

        print(
            f"{comando.personagem} moveu-se para "
            f"{comando.direcao}"
        )

    def condicional(self, comando):

        resultado = self.verificar_condicao(comando.condicao)

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
