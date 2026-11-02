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

- [X] Confirmei que os testes cobrem todas as construções da lista fechada da Sprint 1

---

## 1. Bateria de testes automatizados

- [X] Testes cobrindo cada construção da v1 (personagem, atributo, ação, habilidade, condição, turno), com pelo menos 1 caso válido e 1 inválido cada
- [X] Testes de erro léxico, sintático e semântico, verificando a mensagem retornada
- [X] Todos os testes passando; falhas corrigidas ou documentadas como limitação conhecida

**Cobertura de testes (resumo) e link do repositório:https://github.com/didtis/GameLang/tree/main**

#### Testes realizados

Na etapa de validação final, foram considerados os testes realizados nas etapas anteriores do projeto e os novos testes do interpretador.

Foram validados:

- **Lexer:** reconhecimento das palavras-chave, identificadores, números e operadores relacionais;
- **Lexer:** identificação de erros léxicos, como caracteres inválidos e identificadores iniciados por números;
- **Parser:** reconhecimento das construções válidas da gramática;
- **Parser:** identificação de estruturas que não seguem a gramática definida;
- **Análise semântica:** verificação de referências a personagens existentes e identificação de personagens duplicados;
- **Interpretador:** 8 testes realizados, sendo situações válidas e inválidas, todos aprovados.

Os erros encontrados durante o desenvolvimento foram corrigidos e os testes foram executados novamente após as correções.

## 2. Interpretador simples (opcional)

> Só se houver tempo depois da seção 1. Não é obrigatório para o sucesso do projeto.

- [X] Decisão registrada: o grupo vai ou não implementar o interpretador nesta sprint, e por quê
- [X] Se sim: interpretador percorre a AST e simula ao menos um combate simples (ex.: ataque reduzindo HP, condição sendo aplicada)
- [X] Se sim: pelo menos 1 exemplo de execução documentado (entrada → estado final do combate)

**Decisão e, se aplicável, descrição do interpretador:**

O interpretador foi implementado em Python utilizando a AST produzida pelo parser. Sua função é percorrer os comandos da árvore sintática e simular a execução da lógica de combate.

A implementação contempla:

- criação de heróis e inimigos;
- ataques com cálculo de dano baseado em ataque e defesa;
- estado de defesa;
- habilidades;
- turnos;
- movimentação;
- condições `SE` e `SENAO`;
- repetição com `REPETIR`;
- identificação de personagens inexistentes;
- identificação de personagens duplicados.

O interpretador foi testado com diferentes situações válidas e inválidas. Foram realizados **8 testes**, todos aprovados.

#### Exemplo de execução

Foi utilizado um script simples para demonstrar a execução da lógica de combate:


CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 5
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5

HABILIDADE Arthur GOLPE_FORTE
TURNO Arthur
MOVER Arthur DIREITA
ATACAR Arthur Goblin
DEFENDER Arthur


O interpretador processou a AST e produziu a seguinte saída:


=== EXECUÇÃO DO COMBATE ===
Arthur entrou no combate (Vida: 100)
Goblin entrou no combate (Vida: 50)
Arthur usou GOLPE_FORTE!
Turno de Arthur
Arthur moveu-se para DIREITA
Arthur atacou Goblin!
Goblin perdeu 15 de vida.
Vida do Goblin: 35
Arthur está se defendendo!

=== FIM DO COMBATE ===


Nesse exemplo, o ataque de Arthur causa 15 pontos de dano ao Goblin, calculados pela diferença entre o ataque de Arthur e a defesa do Goblin:

**20 − 5 = 15**

O resultado demonstra que a AST foi percorrida pelo interpretador e que os comandos da GameLang foram transformados em ações de combate.

## 3. Documentação final da linguagem

- [X] Gramática comentada (BNF/EBNF com explicação de cada regra)
- [X] Exemplos de scripts comentados, cobrindo os principais casos de uso
- [X] Escopo da v1 (o que a linguagem cobre e não cobre) explícito

**Link da documentação: (https://github.com/didtis/GameLang/tree/main/Sprints)**

## 4. Apresentação/demo final

- [x] Roteiro definido (motivação → domínio/glossário → gramática → compilador → demo ao vivo → limitações)
- [x] Demo preparada com pelo menos 1 script válido e 1 inválido, mostrando o erro semântico reportado

## 5. Scrum

- [X] Atualizações assíncronas semanais registradas
- [X] Board refletindo o backlog, em andamento e concluído

## 6. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
|Igor Nonaka Oliveira|Participação na organização e revisão dos materiais relacionados ao projeto e ao artigo.|Organização das atividades e conciliação das tarefas da sprint.|Manter a divisão das atividades e melhorar o acompanhamento das tarefas.|
|José Gonçalves Braz Junior|Desenvolvimento e testes do interpretador, integração com a AST, execução dos testes e organização da documentação e apresentação final|Integração entre a AST e a execução dos comandos e correção de erros encontrados durante os testes.|Manter a realização de testes antes da entrega e melhorar a organização das etapas de desenvolvimento.|
|Marcus Gabriel Oliveira da Silva|Participação na organização e revisão dos materiais relacionados ao projeto e ao artigo.|Organização das atividades e conciliação das tarefas da sprint.|Manter a divisão das atividades e melhorar o acompanhamento das tarefas|

---

## Rubrica de avaliação — Sprint 4 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Bateria de testes automatizados | 1,5 | Cobertura completa da v1; testes de erro em todas as camadas | | |
| Documentação final | 1,0 | Gramática comentada, exemplos e escopo explícitos | | |
| Interpretador opcional ou refinamento extra | 0,5 | Decisão justificada; se implementado, funciona no exemplo mostrado | | |
| Apresentação final / Scrum + diário | 1,0 | Demo funcional; board e diário atualizados | | |
| **Nota final da Sprint 4** | **4,0** | | **___ / 4,0** | |
