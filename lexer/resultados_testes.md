# Resultados dos Testes do Lexer — Sprint 2

## Teste 1 — Criação de personagem

**Entrada:**

```text
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10

Resultado esperado:
Reconhecimento das palavras-chave, identificador e números.
Resultado obtido:

('CRIAR', 'CRIAR')
('HEROI', 'HEROI')
('IDENTIFICADOR', 'Arthur')
('VIDA', 'VIDA')
('NUMERO', '100')
('ATAQUE', 'ATAQUE')
('NUMERO', '20')
('DEFESA', 'DEFESA')
('NUMERO', '10')

passou

Teste 2 — Comandos de combate e movimentação

CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5
ATACAR Arthur Goblin
DEFENDER Arthur
HABILIDADE Arthur GOLPE_FORTE
TURNO Arthur
MOVER Arthur DIREITA

Resultado esperado:
Reconhecimento das palavras-chave, identificadores e comandos da linguagem.
Resultado obtido:
Os comandos foram reconhecidos corretamente como tokens.

passou

Teste 3 — Condição e operador relacional

SE VIDA Goblin <= 20
FIM

Resultado esperado:
O operador <= deve ser reconhecido como OPERADOR_RELACIONAL.
Resultado obtido:

('SE', 'SE')
('VIDA', 'VIDA')
('IDENTIFICADOR', 'Goblin')
('OPERADOR_RELACIONAL', '<=')
('NUMERO', '20')
('FIM', 'FIM')

passou

Teste 4 — Símbolo inválido

CRIAR HEROI @Arthur VIDA 100

Resultado esperado:
O símbolo @ deve gerar um erro léxico.
Resultado obtido:

('ERRO_LEXICO', '@')

passou

Teste 5 — Identificador inválido

CRIAR HEROI 123Arthur VIDA 100

Resultado esperado:
123Arthur não segue a regra de identificadores da GameLang e deveria ser rejeitado.
Resultado obtido:

('NUMERO', '123')
('IDENTIFICADOR', 'Arthur')

Precisa de correção
