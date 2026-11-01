# Interpretador da GameLang - Sprint 4

from parser.ast import (
    CriarPersonagem,
    Atacar,
    Defender,
    Habilidade,
    Turno,
    Mover
)


class Interpretador:
    def __init__(self):
        self.personagens = {}

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

    def criar_personagem(self, comando):
        self.personagens[comando.nome] = {
            "tipo": comando.tipo,
            "vida": comando.vida,
            "ataque": comando.ataque,
            "defesa": comando.defesa
        }

        print(
            f"{comando.nome} entrou no combate "
            f"(Vida: {comando.vida})"
        )

    def atacar(self, comando):
        print(
            f"{comando.atacante} atacou "
            f"{comando.alvo}!"
        )

    def defender(self, comando):
        print(
            f"{comando.personagem} está se defendendo!"
        )

    def habilidade(self, comando):
        print(
            f"{comando.personagem} usou "
            f"{comando.habilidade}!"
        )

    def turno(self, comando):
        print(
            f"Turno de {comando.personagem}"
        )

    def mover(self, comando):
        print(
            f"{comando.personagem} moveu-se para "
            f"{comando.direcao}"
        )
