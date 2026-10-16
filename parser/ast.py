# Estruturas da AST da GameLang - Sprint 3


class Programa:
    def __init__(self, comandos):
        self.comandos = comandos


class CriarPersonagem:
    def __init__(self, tipo, nome, vida, ataque, defesa):
        self.tipo = tipo
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa


class Atacar:
    def __init__(self, atacante, alvo):
        self.atacante = atacante
        self.alvo = alvo


class Defender:
    def __init__(self, personagem):
        self.personagem = personagem


class Habilidade:
    def __init__(self, personagem, nome):
        self.personagem = personagem
        self.nome = nome


class Turno:
    def __init__(self, personagem):
        self.personagem = personagem


class Mover:
    def __init__(self, personagem, direcao):
        self.personagem = personagem
        self.direcao = direcao


class Condicional:
    def __init__(self, condicao, comandos, senao=None):
        self.condicao = condicao
        self.comandos = comandos
        self.senao = senao


class Repeticao:
    def __init__(self, quantidade, comandos):
        self.quantidade = quantidade
        self.comandos = comandos


class CondicaoVida:
    def __init__(self, personagem, operador, valor):
        self.personagem = personagem
        self.operador = operador
        self.valor = valor
