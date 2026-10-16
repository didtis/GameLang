# Analisador semântico da GameLang - Sprint 3

from .semantic import TabelaSimbolos


class AnalisadorSemantico:
    def __init__(self):
        self.tabela = TabelaSimbolos()

    def analisar(self, arvore):
        for comando in arvore.comandos:
            self.analisar_comando(comando)

        return True

    def analisar_comando(self, comando):

        if comando.__class__.__name__ == "CriarPersonagem":
            self.analisar_criacao(comando)

        elif comando.__class__.__name__ == "Atacar":
            self.verificar_personagem(comando.atacante)
            self.verificar_personagem(comando.alvo)

        elif comando.__class__.__name__ == "Defender":
            self.verificar_personagem(comando.personagem)

        elif comando.__class__.__name__ == "Habilidade":
            self.verificar_personagem(comando.personagem)

        elif comando.__class__.__name__ == "Turno":
            self.verificar_personagem(comando.personagem)

        elif comando.__class__.__name__ == "Mover":
            self.verificar_personagem(comando.personagem)

        elif comando.__class__.__name__ == "Condicional":
            self.analisar_condicional(comando)

        elif comando.__class__.__name__ == "Repeticao":
            self.analisar_repeticao(comando)

    def analisar_criacao(self, comando):
        self.tabela.adicionar(
            comando.nome,
            comando.tipo,
            comando.vida,
            comando.ataque,
            comando.defesa
        )

    def verificar_personagem(self, nome):
        self.tabela.obter(nome)

    def analisar_condicional(self, comando):
        self.verificar_personagem(
            comando.condicao.personagem
        )

        for subcomando in comando.comandos:
            self.analisar_comando(subcomando)

        if comando.senao is not None:
            for subcomando in comando.senao:
                self.analisar_comando(subcomando)

    def analisar_repeticao(self, comando):
        for subcomando in comando.comandos:
            self.analisar_comando(subcomando)
