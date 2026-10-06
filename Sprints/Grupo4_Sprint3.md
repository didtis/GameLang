# Diário de Sprint 3 — Parser, AST e análise semântica
**Período:** Semanas 3–4
**Grupo / tema:** Grupo 4 — GameLang, DSL para lógica de combate de RPG

**Equipe:**
**Scrum Master do Sprint:**
**Repositório GitHub:** (link)

> Lexer funcional e gramática validada na Sprint 2. Esta sprint constrói o **parser**, a **AST** e a **análise semântica** (tabela de símbolos, checagem de referências e tipos/atributos). **Não** reabre a gramática sem justificar e **não** implementa o interpretador de execução ainda (isso é opcional e só na Sprint 4, se houver tempo).

### Contrato desta sprint

| | Artefato | Origem / destino |
|---|---|---|
| **Entra** | Lexer funcional + gramática congelada | Sprint 2 — **mesma gramática, salvo ajuste justificado** |
| **Entra** | Scripts de exemplo (válidos/inválidos) | Sprint 2 |
| **Sai** | Parser gerando AST | Sprint 4 (testes finais) |
| **Sai** | Tabela de símbolos + checagem semântica (referências, tipos, atributos) | Sprint 4 |
| **Sai** | Mensagens de erro específicas | Sprint 4 (refinamento) |

**Não sai daqui:** bateria de testes automatizados completa, documentação final, interpretador de execução.

- [ ] Confirmei que o parser usa a gramática congelada da Sprint 2

---

## 1. Implementação do parser

- [ ] Estratégia de parsing definida (recursivo descendente ou tabela) e justificada
- [ ] Parser cobre todas as regras da gramática congelada
- [ ] Erros sintáticos tratados com mensagem indicando onde e o que era esperado

**Estratégia escolhida e justificativa:**
**Evidências (link do repositório/commit):**

## 2. Construção da AST

- [ ] Estrutura de nós da AST definida para cada construção do domínio (personagem, atributo, ação, habilidade, condição, turno)
- [ ] Parser gera a AST corretamente para os scripts de exemplo válidos da Sprint 2
- [ ] AST impressa/visualizada para pelo menos 2 exemplos, para conferência manual

**Estrutura da AST (resumo) e exemplos gerados:**

## 3. Análise semântica

- [ ] Tabela de símbolos implementada (personagens, atributos, habilidades declarados)
- [ ] Checagem de referências válidas (ex.: uma habilidade não pode referenciar um atributo inexistente)
- [ ] Checagem de tipos/atributos conforme o glossário da Sprint 1
- [ ] Cada regra semântica testada com pelo menos 1 caso que a viola

**Regras semânticas implementadas e como foram testadas:**

## 4. Mensagens de erro específicas

- [ ] Mensagens de erro léxico, sintático e semântico revisadas para indicar claramente o problema (ex.: "habilidade X referencia atributo Y, que não existe")

**Exemplos de mensagens de erro:**

## 5. Sprint Review — checkpoint intermediário

**Incremento demonstrado ao PO (docente):**
**Feedback recebido:**

## 6. Scrum

- [ ] Atualizações assíncronas semanais registradas
- [ ] Board refletindo o estado real da Sprint

## 7. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
| | | | |

---

## Rubrica de avaliação — Sprint 3 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Parser e AST | 1,5 | Parser cobre a gramática congelada; AST correta nos exemplos válidos | | |
| Análise semântica | 1,0 | Tabela de símbolos, referências e tipos checados e testados | | |
| Mensagens de erro específicas | 1,0 | Mensagens claras indicando o problema exato | | |
| Sprint Review / Scrum + diário | 0,5 | Incremento demonstrado; board e diário atualizados | | |
| **Nota final da Sprint 3** | **4,0** | | **___ / 4,0** | |
