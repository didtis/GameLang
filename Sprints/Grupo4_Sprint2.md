# Diário de Sprint 2 — Lexer e gramática validada
**Período:** Semana 2
**Grupo / tema:** Grupo 4 — GameLang, DSL para lógica de combate de RPG

**Equipe:** Igor Nonaka Oliveira; José Gonçalves Braz Junior; Marcus Gabriel Oliveira da Silva
**Scrum Master do Sprint:** José Gonçalves Braz Junior
**Repositório GitHub:** ([link](https://github.com/didtis/GameLang/tree/main))

> A entrega é sobre a especificação léxica e o rascunho de gramática da Sprint 1. Esta sprint **implementa o lexer** e **revisa a gramática até eliminar ambiguidades** — não avança para parser/AST, isso é Sprint 3.

### Contrato desta sprint

| | Artefato | Origem / destino |
|---|---|---|
| **Entra** | Especificação léxica + rascunho da gramática | Sprint 1 — **não redefinir tokens sem justificar** |
| **Entra** | Glossário do domínio | Sprint 1 |
| **Sai** | Lexer funcional (tokenizador) | Sprint 3 |
| **Sai** | Gramática revisada e sem ambiguidade relevante | Sprint 3 **é obrigada a usar esta gramática** |
| **Sai** | Scripts de exemplo (válidos e inválidos) | Sprint 3 e 4 (testes) |

**Não sai daqui:** parser, AST, análise semântica.

- [x] Confirmei que os tokens implementados são os da especificação da Sprint 1 (ou revisados com justificativa registrada)

---

## 1. Implementação do lexer

- [x] Tokenizador implementado a partir da tabela de tokens da Sprint 1
- [x] Tratamento de espaços em branco, comentários (se houver) e quebras de linha
- [x] Erros léxicos (caractere/símbolo não reconhecido) tratados com mensagem clara

**Descrição da implementação e estrutura do código:**
O lexer foi implementado em Python no arquivo `lexer/lexer.py`. Ele recebe o código da GameLang e identifica palavras-chave, números, identificadores e operadores relacionais, gerando uma lista de tokens. Também identifica caracteres ou sequências que não pertencem à linguagem como `ERRO_LEXICO`.
**Evidências (link do repositório/commit):**
repositório https://github.com/didtis/GameLang/tree/main
## 2. Testes do lexer

- [x] Casos de teste com tokens válidos de cada categoria (palavra-chave, identificador, literal, símbolo)
- [x] Casos de teste com entradas inválidas e mensagem de erro correspondente
- [x] Todos os testes passando

**Tabela de casos de teste do lexer:**

| Entrada | Tokens esperados | Resultado obtido | Passou? |
|---|---|---|---|
| `CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10` | CRIAR, HEROI, IDENTIFICADOR, VIDA, NUMERO, ATAQUE, NUMERO, DEFESA, NUMERO | Tokens reconhecidos corretamente | Sim |
| `ATACAR Arthur Goblin` / `DEFENDER Arthur` / `HABILIDADE Arthur GOLPE_FORTE` / `TURNO Arthur` / `MOVER Arthur DIREITA` | Tokens correspondentes aos comandos | Tokens reconhecidos corretamente | Sim |
| `SE VIDA Goblin <= 20` / `FIM` | SE, VIDA, IDENTIFICADOR, OPERADOR_RELACIONAL, NUMERO, FIM | Tokens reconhecidos corretamente | Sim |
| `CRIAR HEROI @Arthur VIDA 100` | ERRO_LEXICO em `@` | `ERRO_LEXICO` em `@` | Sim |
| `CRIAR HEROI 123Arthur VIDA 100` | ERRO_LEXICO em `123Arthur` | `ERRO_LEXICO` em `123Arthur` | Sim |
| `REPETIR 3` / comandos de movimentação | REPETIR, NUMERO e tokens das direções | Tokens reconhecidos corretamente | Sim |
| `ATACAR Arthur # Goblin` | ERRO_LEXICO em `#` | `ERRO_LEXICO` em `#` | Sim |
## 3. Revisão da gramática

- [x] Derivações manuais de cada script de exemplo da Sprint 1, conferindo se a gramática os gera
- [x] Pontos de ambiguidade identificados e resolvidos (reescrita de regras, se necessário)
- [x] Gramática final documentada em BNF/EBNF, versionada

**Ajustes feitos na gramática e por quê:**
A gramática foi revisada por meio de derivações manuais dos três scripts de exemplo do Sprint 1. Não foram identificadas ambiguidades relevantes. As regras foram mantidas, pois os exemplos foram gerados corretamente pela gramática
**Gramática final (BNF/EBNF):**
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
## 4. Scripts de exemplo

- [x] Pelo menos 5 scripts válidos, cobrindo personagens, habilidades, condições e turnos da v1
- [x] Pelo menos 3 scripts inválidos, cada um violando uma regra diferente (léxica, sintática)
- [x] Cada exemplo inválido com a explicação do que deveria ser rejeitado e por quê

**Lista de scripts de exemplo (válidos e inválidos) e link do arquivo:**
Script válido 1 — Criação de personagens

CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5

Válido porque usa corretamente CRIAR, HEROI, INIMIGO, VIDA, ATAQUE, DEFESA, identificadores e números

Script válido 2 — Turno e combate

CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5

TURNO Arthur
ATACAR Arthur Goblin
DEFENDER Arthur

Válido

Script válido 3 — Movimentação

CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10

TURNO Arthur
MOVER Arthur DIREITA
MOVER Arthur CIMA
MOVER Arthur ESQUERDA

Válido e testa as direções da GameLang

Script válido 4 — Habilidade e condição

CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 20 ATAQUE 10 DEFESA 5

SE VIDA Goblin <= 20
    HABILIDADE Arthur GOLPE_FORTE
SENAO
    ATACAR Arthur Goblin
FIM

Válido

Script válido 5 — Repetição

CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5

TURNO Arthur
REPETIR 2
    MOVER Arthur DIREITA
    ATACAR Arthur Goblin
FIM

Válido

Script inválido 1 — Símbolo não reconhecido

CRIAR HEROI @Arthur VIDA 100 ATAQUE 20 DEFESA 10

Inválido.

O caractere @ não pertence aos símbolos válidos da GameLang. O lexer deve identificá-lo como ERRO_LEXICO.

Resultado obtido:
('ERRO_LEXICO', '@')

Script inválido 2 — Identificador iniciado por número

CRIAR HEROI 123Arthur VIDA 100 ATAQUE 20 DEFESA 10

Inválido.

O identificador não pode começar com um número. O lexer deve identificar 123Arthur como ERRO_LEXICO.

Resultado obtido:
('ERRO_LEXICO', '123Arthur')

Script inválido 3 — Símbolo não reconhecido

ATACAR Arthur # Goblin

Inválido.

O caractere # não pertence aos símbolos válidos da GameLang. O lexer deve identificá-lo como ERRO_LEXICO.

Resultado obtido:
('ERRO_LEXICO', '#')

Script inválido 4 — Comando incompleto

ATACAR Arthur

Inválido.

A regra da gramática:

<ataque> ::= ATACAR <identificador> <identificador>

exige dois identificadores: o atacante e o alvo. Nesse caso, o alvo está ausente.

A rejeição sintática será validada na implementação do parser na Sprint 3.
## 5. Scrum

- [x] Atualizações semanais no board
- [x] Board refletindo o estado real

**Link do board:**
https://trello.com/invite/b/6ac531640c4d97e5ea54928c/ATTI728956cf7fbb759882e066c08f68a85e4F791E7E/gamelang-sprint-1
## 6. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
| | | | |

---

## Rubrica de avaliação — Sprint 2 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Lexer implementado e testado | 1,5 | Tokenizador funcional, erros léxicos tratados, testes cobrindo categorias e casos inválidos | | |
| Gramática revisada e sem ambiguidade | 1,5 | Derivações conferidas, ambiguidades resolvidas e documentadas | | |
| Scripts de exemplo | 0,5 | Conjunto válido/inválido cobrindo a v1, com explicação dos inválidos | | |
| Scrum + diário de bordo | 0,5 | Board com histórico; diário reflexivo de todos | | |
| **Nota final da Sprint 2** | **4,0** | | **___ / 4,0** | |
