# Lexer da GameLang - Sprint 2

import re

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

PADROES = {
    "NUMERO": r"[0-9]+",
    "IDENTIFICADOR": r"[A-Za-z_][A-Za-z0-9_]*",
    "OPERADOR_RELACIONAL": r"<=|>=|==|<|>"
}


def tokenizar(codigo):
    tokens = []

    partes = re.findall(
        r"<=|>=|==|<|>|[A-Za-z_][A-Za-z0-9_]*|[0-9]+|\S",
        codigo
    )

    for parte in partes:
        if parte in PALAVRAS_CHAVE:
            tokens.append((PALAVRAS_CHAVE[parte], parte))

        elif re.fullmatch(PADROES["NUMERO"], parte):
            tokens.append(("NUMERO", parte))

        elif re.fullmatch(PADROES["OPERADOR_RELACIONAL"], parte):
            tokens.append(("OPERADOR_RELACIONAL", parte))

        elif re.fullmatch(PADROES["IDENTIFICADOR"], parte):
            tokens.append(("IDENTIFICADOR", parte))

        else:
            tokens.append(("ERRO_LEXICO", parte))

    return tokens
