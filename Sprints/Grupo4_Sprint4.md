# Diário de Sprint 4 — Testes, interpretador opcional e entrega
**Período:** Semana 5
**Grupo / tema:** Grupo 4 — GameLang, DSL para lógica de combate de RPG

**Equipe:**
**Scrum Master do Sprint:**
**Repositório GitHub:** (link)

> Parser, AST e análise semântica prontos na Sprint 3. Esta sprint **fecha o projeto**: bateria de testes automatizados, documentação final e, **só se houver tempo**, um interpretador simples que simula o combate a partir da AST. **Não há** sprint seguinte — esta é a entrega.

### Contrato desta sprint

| | Artefato | Origem / destino |
|---|---|---|
| **Entra** | Parser + AST + análise semântica | Sprint 3 — **não redesenhar do zero** |
| **Sai** | Bateria de testes automatizados | Entrega final |
| **Sai** | Documentação final da linguagem | Entrega final |
| **Sai** | Interpretador simples (opcional) + apresentação final | Entrega final / mostra |

**Não há sprint seguinte.**

- [ ] Confirmei que os testes cobrem todas as construções da lista fechada da Sprint 1

---

## 1. Bateria de testes automatizados

- [ ] Testes cobrindo cada construção da v1 (personagem, atributo, ação, habilidade, condição, turno), com pelo menos 1 caso válido e 1 inválido cada
- [ ] Testes de erro léxico, sintático e semântico, verificando a mensagem retornada
- [ ] Todos os testes passando; falhas corrigidas ou documentadas como limitação conhecida

**Cobertura de testes (resumo) e link do repositório:**

## 2. Interpretador simples (opcional)

> Só se houver tempo depois da seção 1. Não é obrigatório para o sucesso do projeto.

- [ ] Decisão registrada: o grupo vai ou não implementar o interpretador nesta sprint, e por quê
- [ ] Se sim: interpretador percorre a AST e simula ao menos um combate simples (ex.: ataque reduzindo HP, condição sendo aplicada)
- [ ] Se sim: pelo menos 1 exemplo de execução documentado (entrada → estado final do combate)

**Decisão e, se aplicável, descrição do interpretador:**

## 3. Documentação final da linguagem

- [ ] Gramática comentada (BNF/EBNF com explicação de cada regra)
- [ ] Exemplos de scripts comentados, cobrindo os principais casos de uso
- [ ] Escopo da v1 (o que a linguagem cobre e não cobre) explícito

**Link da documentação:**

## 4. Apresentação/demo final

- [ ] Roteiro definido (motivação → domínio/glossário → gramática → compilador → demo ao vivo → limitações)
- [ ] Demo preparada com pelo menos 1 script válido e 1 inválido, mostrando o erro semântico reportado

## 5. Scrum

- [ ] Atualizações assíncronas semanais registradas
- [ ] Board refletindo o backlog, em andamento e concluído

## 6. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
| | | | |

---

## Rubrica de avaliação — Sprint 4 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Bateria de testes automatizados | 1,5 | Cobertura completa da v1; testes de erro em todas as camadas | | |
| Documentação final | 1,0 | Gramática comentada, exemplos e escopo explícitos | | |
| Interpretador opcional ou refinamento extra | 0,5 | Decisão justificada; se implementado, funciona no exemplo mostrado | | |
| Apresentação final / Scrum + diário | 1,0 | Demo funcional; board e diário atualizados | | |
| **Nota final da Sprint 4** | **4,0** | | **___ / 4,0** | |
