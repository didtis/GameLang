# Lexer da GameLang - Sprint 2

PALAVRAS_CHAVE = {
    "CRIAR": "CRIAR",
    "HEROI": "HEROI",
    "INIMIGO": "INIMIGO",
    "VIDA": "VIDA",
    "ATAQUE": "ATAQUE",
    "DEFESA": "DEFESA",
    "ATACAR": "ATACAR",
    "DEFENDER": "DEFENDER",
    "HABILIDADE": "HABILIDADE",
    "TURNO": "TURNO",
    "SE": "SE",
    "SENAO": "SENAO",
    "FIM": "FIM",
    "REPETIR": "REPETIR",
    "MOVER": "MOVER",
    "CIMA": "CIMA",
    "BAIXO": "BAIXO",
    "ESQUERDA": "ESQUERDA",
    "DIREITA": "DIREITA"
}

import re

PADROES = {
    "NUMERO": r"[0-9]+",
    "IDENTIFICADOR": r"[A-Za-z_][A-Za-z0-9_]*",
    "OPERADOR_RELACIONAL": r"<=|>=|==|<|>"
}
