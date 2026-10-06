# Diário de Sprint 1 — Definição do domínio e da gramática
**Período:** Semana 1
**Grupo / tema:** Grupo 4 — GameLang, DSL para lógica de combate de RPG

**Equipe:** Equipe 4
**Integrantes:** Igor Nonaka Oliveira, José Gonçalves Braz Junior, Marcus Gabriel Oliveira da Silva
**Scrum Master do Sprint:**
**Repositório GitHub:** (link)

> Esta sprint **só define a linguagem no papel**: glossário do domínio, lista fechada de construções da v1, especificação léxica e rascunho da gramática. **Não há** implementação de lexer/parser nem código — isso começa na Sprint 2.

### Contrato desta sprint

| | Artefato | Quem usa depois |
|---|---|---|
| **Entra** | Enunciado do projeto (nada de sprint anterior) | — |
| **Sai** | Canvas de kickoff (elementos do domínio, unidade de compilação, saída do compilador) | Sprints seguintes |
| **Sai** | Glossário do domínio (personagem, atributo, ação, habilidade, condição, turno) | Sprint 2 e 3 |
| **Sai** | Especificação léxica (tokens/expressões regulares) | Sprint 2 **é obrigada a usar esta especificação** |
| **Sai** | Rascunho da gramática (BNF/EBNF) + exemplos de scripts-alvo | Sprint 2 (revisão e implementação) |

**Não sai daqui:** lexer implementado, parser, AST, análise semântica.

---

## 1. Canvas de kickoff

| Pergunta | Resposta |
|---|---|
| Quais elementos do domínio a v1 cobre (personagens, atributos, ataques, defesa, habilidades, condições, turnos)? | |
| Qual é a unidade de compilação (um script = um combate? um personagem? uma habilidade)? | |
| Qual é a saída do compilador nesta fase (AST validada; execução é bônus)? | |
| Justificativa do recorte escolhido para a v1 (o que fica de fora e por quê) | |

- [ ] Elementos do domínio da v1 listados e fechados
- [ ] Unidade de compilação definida sem ambiguidade
- [ ] Recorte da v1 justificado (o que fica de fora explicitamente)

## 2. Glossário do domínio

- [ ] Cada termo do domínio (personagem, atributo, ação, habilidade, condição, turno) definido em uma frase
- [ ] Relações entre os termos esclarecidas (ex.: uma habilidade pode alterar um atributo ou aplicar uma condição)

**Glossário:**

| Termo | Definição | Relação com outros termos |
|---|---|---|

## 3. Especificação léxica

- [ ] Tabela de tokens (palavras-chave, identificadores, literais, símbolos) com expressão regular de cada um
- [ ] Palavras-chave escolhidas alinhadas ao glossário da seção 2
- [ ] Casos de ambiguidade léxica verificados

**Tabela de tokens:**

| Token | Expressão regular | Exemplo |
|---|---|---|

## 4. Rascunho da gramática e exemplos-alvo

- [ ] Gramática em BNF/EBNF cobrindo todas as construções da lista fechada (seção 1)
- [ ] Pelo menos 3 scripts de exemplo (ex.: um personagem, uma habilidade, um turno de combate simples)
- [ ] Derivação manual de pelo menos 1 exemplo, para checar se a gramática gera o script esperado

**Gramática (BNF/EBNF):**

**Scripts de exemplo:**
1.
2.
3.

## 5. Scrum

- [ ] Papéis definidos (Product Owner = docente; Scrum Master do sprint; Development Team)
- [ ] Board criado (GitHub Projects ou Trello) com To do / Doing / Done
- [ ] Backlog inicial com pelo menos 3 user stories

**User stories do backlog inicial:**
1.
2.
3.

**Link do board:**

## 6. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
| | | | |

## 7. Evidências gerais

- Link do canvas:
- Link do glossário:
- Link do rascunho da gramática:
- Link do board:

---

## Rubrica de avaliação — Sprint 1 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Canvas e recorte da v1 | 0,5 | Elementos do domínio e unidade de compilação claros; recorte justificado | | |
| Glossário do domínio | 0,5 | Termos definidos e relacionados corretamente | | |
| Especificação léxica | 1,0 | Tokens completos, expressões regulares corretas, sem ambiguidade óbvia | | |
| Rascunho da gramática e exemplos | 1,5 | Gramática cobre a lista de construções; exemplos derivados corretamente | | |
| Scrum + diário de bordo | 0,5 | Papéis, board, backlog e diário reflexivo de todos | | |
| **Nota final da Sprint 1** | **4,0** | | **___ / 4,0** | |
