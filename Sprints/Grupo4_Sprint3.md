# Diário de Sprint 3 — Parser, AST e análise semântica
**Período:** Semanas 3–4
**Grupo / tema:** Grupo 4 — GameLang, DSL para lógica de combate de RPG

**Equipe:** Igor Nonaka Oliveira; José Gonçalves Braz Junior; Marcus Gabriel Oliveira da Silva
**Scrum Master do Sprint:** José Gonçalves Braz Junior
**Repositório GitHub:** https://github.com/didtis/GameLang/tree/main

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

- [x] Confirmei que o parser usa a gramática congelada da Sprint 2

---

## 1. Implementação do parser

- [x] Estratégia de parsing definida (recursivo descendente ou tabela) e justificada
- [x] Parser cobre todas as regras da gramática congelada
- [x] Erros sintáticos tratados com mensagem indicando onde e o que era esperado

**Estratégia escolhida e justificativa:**
Foi escolhido o parser recursivo descendente porque a gramática da GameLang possui uma estrutura simples e organizada em regras hierárquicas. Essa estratégia permite implementar cada regra da gramática como uma função, facilitando a compreensão, manutenção e identificação de erros sintáticos.
**Evidências (link do repositório/commit):**
https://github.com/didtis/GameLang/tree/main/parser
## 2. Construção da AST

- [x] Estrutura de nós da AST definida para cada construção do domínio (personagem, atributo, ação, habilidade, condição, turno)
- [x] Parser gera a AST corretamente para os scripts de exemplo válidos da Sprint 2
- [x] AST impressa/visualizada para pelo menos 2 exemplos, para conferência manual

**Estrutura da AST (resumo) e exemplos gerados:**
A AST foi organizada em nós correspondentes às construções da GameLang:

- `Programa`
- `CriarPersonagem`
- `Atacar`
- `Defender`
- `Habilidade`
- `Turno`
- `Mover`
- `Condicional`
- `Repeticao`
- `CondicaoVida`

Exemplo 1

Programa

CriarPersonagem

tipo: HEROI

nome: Arthur

vida: 100

ataque: 20

defesa: 10

Atacar

atacante: Arthur

alvo: Goblin

Defender

personagem: Arthur
        
Exemplo 2

Programa

Condicional

Condicao:

CondicaoVida

personagem: Goblin

operador: <=

valor: 20

Comandos:

Atacar

atacante: Arthur

alvo: Goblin

SENAO:

Defender

personagem: Arthur

Repeticao

quantidade: 2

Comandos:

Mover

personagem: Arthur

direcao: CIMA
                
## 3. Análise semântica

- [x] Tabela de símbolos implementada (personagens, atributos, habilidades declarados)
- [x] Checagem de referências válidas (ex.: uma habilidade não pode referenciar um atributo inexistente)
- [x] Checagem de tipos/atributos conforme o glossário da Sprint 1
- [x] Cada regra semântica testada com pelo menos 1 caso que a viola

**Regras semânticas implementadas e como foram testadas:**
1 Personagem deve ser criado antes de ser utilizado

CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
ATACAR Arthur Goblin

Resultado: rejeitado porque Goblin não foi criado

2 Não é permitido criar dois personagens com o mesmo nome

Foram criados dois personagens chamados Arthur
Resultado:

Erro semântico: personagem 'Arthur' já foi criado

3 Personagens utilizados em ações devem existir na tabela de símbolos.
    Foram testadas ações de ataque, defesa, habilidade, turno e movimentação.
    Os personagens existentes foram aceitos.
    
4 Atributos do personagem devem seguir as regras da linguagem.
    Foram testados valores inválidos para VIDA, ATAQUE e DEFESA.
    O parser rejeitou valores textuais quando era esperado um número.
     
5 Tipo de personagem deve ser HEROI ou INIMIGO.
    Foi testada a criação com um tipo inválido.
    O código foi rejeitado pelo parser.
    
Os testes foram executados nos arquivos test_semantic_analyzer.py e test_attributes.py.

## 4. Mensagens de erro específicas

- [x] Mensagens de erro léxico, sintático e semântico revisadas para indicar claramente o problema (ex.: "habilidade X referencia atributo Y, que não existe")

**Exemplos de mensagens de erro:**

Erro léxico: quando foi encontrado um caractere ou sequência inválida, o lexer retornou o token ERRO_LEXICO

CRIAR HEROI @Arthur VIDA 100

Resultado:
('ERRO_LEXICO', '@')

CRIAR HEROI 123Arthur VIDA 100

Resultado:
('ERRO_LEXICO', '123Arthur')

ATACAR Arthur # Goblin

Resultado:
('ERRO_LEXICO', '#')

Erro sintático:

Erro sintático: esperado IDENTIFICADOR, mas o código terminou

Erro sintático: esperado FIM, mas o código terminou

Erro sintático: direção esperada

Erro sintático

Erro semântico: personagem 'Goblin' não foi criado

Erro semântico: personagem 'Arthur' já foi criado
## 5. Sprint Review — checkpoint intermediário

**Incremento demonstrado ao PO (docente):**
Foi demonstrada a evolução da GameLang por meio dos testes realizados com o lexer da Sprint 2 integrado ao parser da Sprint 3. Foram realizados testes de análise sintática, geração da AST e análise semântica. Também foram demonstrados exemplos válidos e inválidos para verificar o comportamento da linguagem.
**Feedback recebido:**
Durante esta Sprint, foram mantidas as definições da linguagem estabelecidas anteriormente, utilizando a gramática congelada da Sprint 2 como base para a implementação do parser e da análise semântica.
## 6. Scrum

- [x] Atualizações assíncronas semanais registradas
- [x] Board refletindo o estado real da Sprint

## 7. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
|Igor Nonaka Oliveira |Participei da revisão da gramática e dos testes do parser e da AST, acompanhando a implementação das estruturas da linguagem.|Tive dificuldade em verificar se as regras da gramática estavam sendo representadas corretamente no parser e na AST.|Pretendo continuar colaborando na revisão dos testes e das estruturas da linguagem.|
|José Gonçalves Braz Junior|Implementei o parser recursivo descendente, a AST, a tabela de símbolos e o analisador semântico. Também realizei os testes sintáticos e semânticos e organizei os resultados.|Tive dificuldade principalmente na integração entre lexer, parser, AST e análise semântica e na criação de mensagens de erro adequadas.|Pretendo manter a organização dos testes e continuar validando cada etapa antes de avançar para a próxima.|
|Marcus Gabriel Oliveira da Silva|Participei da revisão da gramática, da AST e dos testes de análise sintática e semântica, verificando os exemplos válidos e inválidos.|Tive dificuldade em acompanhar a relação entre as regras da gramática e as estruturas geradas na AST.|Pretendo continuar revisando os exemplos e colaborando na validação das próximas etapas.|

---

## Rubrica de avaliação — Sprint 3 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Parser e AST | 1,5 | Parser cobre a gramática congelada; AST correta nos exemplos válidos | | |
| Análise semântica | 1,0 | Tabela de símbolos, referências e tipos checados e testados | | |
| Mensagens de erro específicas | 1,0 | Mensagens claras indicando o problema exato | | |
| Sprint Review / Scrum + diário | 0,5 | Incremento demonstrado; board e diário atualizados | | |
| **Nota final da Sprint 3** | **4,0** | | **___ / 4,0** | |
