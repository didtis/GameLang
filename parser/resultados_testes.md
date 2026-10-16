Resultados dos Testes do Parser — Sprint 3

Teste 1 — Criação de herói válida
Entrada:
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 2 — Criação de inimigo válida
Entrada:
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 3 — Ataque válido
Entrada:
ATACAR Arthur Goblin
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 4 — Defesa válida
Entrada:
DEFENDER Arthur
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 5 — Habilidade válida
Entrada:
HABILIDADE Arthur GOLPE_FORTE
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 6 — Turno válido
Entrada:
TURNO Arthur
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 7 — Movimento para direita
Entrada:
MOVER Arthur DIREITA
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 8 — Movimento para cima
Entrada:
MOVER Arthur CIMA
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 9 — Movimento para baixo
Entrada:
MOVER Arthur BAIXO
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 10 — Movimento para esquerda
Entrada:
MOVER Arthur ESQUERDA
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 11 — Condicional simples
Entrada:
SE VIDA Goblin <= 20
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 12 — Condicional com ataque
Entrada:
SE VIDA Goblin <= 20
ATACAR Arthur Goblin
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 13 — Condicional com SENAO
Entrada:
SE VIDA Goblin <= 20
ATACAR Arthur Goblin
SENAO
DEFENDER Arthur
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 14 — Repetição válida
Entrada:
REPETIR 3
MOVER Arthur DIREITA
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 15 — Vários comandos
Entrada:
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
MOVER Arthur DIREITA
ATACAR Arthur Goblin
DEFENDER Arthur
HABILIDADE Arthur GOLPE_FORTE
TURNO Arthur
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 16 — ATACAR sem alvo
Entrada:
ATACAR Arthur
Resultado:
Erro sintático: esperado IDENTIFICADOR, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 17 — SE sem FIM
Entrada:
SE VIDA Goblin <= 20
ATACAR Arthur Goblin
Resultado:
Erro sintático: esperado FIM, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 18 — REPETIR sem FIM
Entrada:
REPETIR 3
MOVER Arthur DIREITA
Resultado:
Erro sintático: esperado FIM, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 19 — MOVER com direção inválida
Entrada:
MOVER Arthur CENTRO
Resultado:
Erro sintático: direção esperada
Status: PASSOU — erro sintático detectado corretamente.

Teste 20 — CRIAR sem DEFESA
Entrada:
CRIAR HEROI Arthur VIDA 100 ATAQUE 20
Resultado:
Erro sintático: esperado DEFESA, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 21 — ATACAR com apenas um personagem
Entrada:
ATACAR Arthur
Resultado:
Erro sintático: esperado IDENTIFICADOR, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 22 — DEFENDER sem personagem
Entrada:
DEFENDER
Resultado:
Erro sintático: esperado IDENTIFICADOR, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 23 — HABILIDADE sem nome
Entrada:
HABILIDADE Arthur
Resultado:
Erro sintático: esperado IDENTIFICADOR, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 24 — TURNO sem personagem
Entrada:
TURNO
Resultado:
Erro sintático: esperado IDENTIFICADOR, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 25 — MOVER sem personagem
Entrada:
MOVER
Resultado:
Erro sintático: esperado IDENTIFICADOR, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 26 — CRIAR sem tipo de personagem
Entrada:
CRIAR Arthur VIDA 100 ATAQUE 20 DEFESA 10
Resultado:
Erro sintático: esperado HEROI ou INIMIGO
Status: PASSOU — erro sintático detectado corretamente.

Teste 27 — CRIAR com atributo inválido
Entrada:
CRIAR HEROI Arthur VITIMA 100 ATAQUE 20 DEFESA 10
Resultado:
Erro sintático: esperado VIDA, mas encontrado IDENTIFICADOR ('VITIMA')
Status: PASSOU — erro sintático detectado corretamente.

Teste 28 — VIDA com valor inválido
Entrada:
CRIAR HEROI Arthur VIDA cem ATAQUE 20 DEFESA 10
Resultado:
Erro sintático: esperado NUMERO, mas encontrado IDENTIFICADOR ('cem')
Status: PASSOU — erro sintático detectado corretamente.

Teste 29 — ATAQUE com valor inválido
Entrada:
CRIAR HEROI Arthur VIDA 100 ATAQUE forte DEFESA 10
Resultado:
Erro sintático: esperado NUMERO, mas encontrado IDENTIFICADOR ('forte')
Status: PASSOU — erro sintático detectado corretamente.

Teste 30 — DEFESA com valor inválido
Entrada:
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA resistente
Resultado:
Erro sintático: esperado NUMERO, mas encontrado IDENTIFICADOR ('resistente')
Status: PASSOU — erro sintático detectado corretamente.

Teste 31 — Operador relacional inválido
Entrada:
SE VIDA Goblin != 20
FIM
Resultado:
Erro sintático: esperado OPERADOR_RELACIONAL, mas encontrado ERRO_LEXICO ('!')
Status: PASSOU — erro sintático detectado corretamente.

Teste 32 — SE sem condição
Entrada:
SE
FIM
Resultado:
Erro sintático: esperado VIDA, mas encontrado FIM ('FIM')
Status: PASSOU — erro sintático detectado corretamente.

Teste 33 — REPETIR sem quantidade
Entrada:
REPETIR
MOVER Arthur DIREITA
FIM
Resultado:
Erro sintático: esperado NUMERO, mas encontrado MOVER ('MOVER')
Status: PASSOU — erro sintático detectado corretamente.

Teste 34 — HABILIDADE sem personagem
Entrada:
HABILIDADE GOLPE_FORTE
Resultado:
Erro sintático: esperado IDENTIFICADOR, mas o código terminou
Status: PASSOU — erro sintático detectado corretamente.

Teste 35 — Operador relacional >=
Entrada:
SE VIDA Goblin >= 20
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 36 — Operador relacional <
Entrada:
SE VIDA Goblin < 20
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 37 — Operador relacional >
Entrada:
SE VIDA Goblin > 20
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 38 — Operador relacional ==
Entrada:
SE VIDA Goblin == 20
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 39 — SE com SENAO
Entrada:
SE VIDA Goblin <= 20
ATACAR Arthur Goblin
SENAO
DEFENDER Arthur
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 40 — REPETIR válido
Entrada:
REPETIR 3
MOVER Arthur DIREITA
ATACAR Arthur Goblin
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 41 — CRIAR INIMIGO válido
Entrada:
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 42 — MOVER BAIXO
Entrada:
MOVER Arthur BAIXO
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 43 — MOVER ESQUERDA
Entrada:
MOVER Arthur ESQUERDA
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 44 — MOVER CIMA
Entrada:
MOVER Arthur CIMA
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — código válido aceito corretamente.

Teste 45 — Programa completo
Entrada:
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
HABILIDADE Arthur GOLPE_FORTE
TURNO Arthur
MOVER Arthur DIREITA
SE VIDA Goblin <= 20
ATACAR Arthur Goblin
SENAO
DEFENDER Arthur
FIM
REPETIR 2
MOVER Arthur CIMA
FIM
Resultado:
Parser: código aceito com sucesso!
Status: PASSOU — programa completo aceito corretamente.
