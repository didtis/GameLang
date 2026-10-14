<programa> ::= { <comando> }

<comando> ::= <criacao>
            | <ataque>
            | <defesa>
            | <habilidade>
            | <turno>
            | <movimentacao>
            | <condicional>
            | <repeticao>

<criacao> ::= CRIAR <tipo_personagem> <identificador>
              VIDA <numero>
              ATAQUE <numero>
              DEFESA <numero>

<tipo_personagem> ::= HEROI
                    | INIMIGO

<ataque> ::= ATACAR <identificador> <identificador>

<defesa> ::= DEFENDER <identificador>

<habilidade> ::= HABILIDADE <identificador> <identificador>

<turno> ::= TURNO <identificador>

<movimentacao> ::= MOVER <identificador> <direcao>

<direcao> ::= CIMA
            | BAIXO
            | ESQUERDA
            | DIREITA

<condicional> ::= SE <condicao>
                    { <comando> }
                  [ SENAO { <comando> } ]
                  FIM

<repeticao> ::= REPETIR <numero>
                  { <comando> }
                FIM

<condicao> ::= VIDA <identificador> <operador> <numero>

<operador> ::= <=
             | >=
             | <
             | >
             | ==

<identificador> ::= [A-Za-z_][A-Za-z0-9_]*

<numero> ::= [0-9]+
