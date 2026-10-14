# Diário de Sprint 2 — Lexer e gramática validada
**Período:** Semana 2
**Grupo / tema:** Grupo 4 — GameLang, DSL para lógica de combate de RPG

**Equipe:**
**Scrum Master do Sprint:**
**Repositório GitHub:** (link)

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
- [ ] Gramática final documentada em BNF/EBNF, versionada

**Ajustes feitos na gramática e por quê:**
Foram realizadas derivações manuais dos três exemplos definidos no Sprint 1. Os três exemplos foram aceitos pela gramática. Não foram identificadas ambiguidades relevantes, pois os comandos possuem palavras-chave iniciais diferentes
**Gramática final (BNF/EBNF):**

## 4. Scripts de exemplo

- [ ] Pelo menos 5 scripts válidos, cobrindo personagens, habilidades, condições e turnos da v1
- [ ] Pelo menos 3 scripts inválidos, cada um violando uma regra diferente (léxica, sintática)
- [ ] Cada exemplo inválido com a explicação do que deveria ser rejeitado e por quê

**Lista de scripts de exemplo (válidos e inválidos) e link do arquivo:**

## 5. Scrum

- [ ] Atualizações semanais no board
- [ ] Board refletindo o estado real

**Link do board:**

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
