# RFC: Proposta de Projeto — Grupo 4

| Campo | Valor |
|---|---|
| **Título** | GameLang — compilador para DSL de lógica de combate de RPG |
| **Trilha** | Projeto novo — linguagem específica de domínio (DSL) com Gramática Livre de Contexto |
| **Equipe** | Grupo 4 |
| **Autores** | Igor Nonaka Oliveira, José Gonçalves Braz Junior, Marcus Gabriel Oliveira da Silva |
| **Status** | Rascunho |
| **Data** | 06/10/2026 |
| **Sprint de referência** | 1 |

> Este RFC formaliza a GameLang, DSL para representar personagens, atributos, ataques, defesa, habilidades, condições e turnos de combate de RPG, e seu compilador front-end (análise léxica, sintática via GLC, construção de AST e análise semântica). Engine gráfico, IA de combate e balanceamento de jogo **não** são escopo — o entregável é a linguagem formalizada e validada.

---

## 1. Resumo (TL;DR)

O grupo define uma Gramática Livre de Contexto para a GameLang e implementa seu compilador front-end (lexer, parser, AST e análise semântica), permitindo descrever e validar scripts de combate de RPG de forma declarativa, sem programar em linguagem de propósito geral.

---

## 2. Contexto e motivação

Sistemas de RPG exigem representar lógica de combate (personagens, atributos, ataques, defesa, habilidades, condições, turnos) de forma estruturada. Uma DSL declarativa, com gramática formal, permite validar essa lógica antes de usá-la no jogo — aplicando diretamente os conceitos centrais da disciplina (GLC, análise léxica/sintática/semântica, AST).

---

## 3. Problema formal e escopo da linguagem

| Pergunta | Resposta |
|---|---|
| Elementos do domínio cobertos na v1 | Personagens, atributos (ex.: HP, ataque, defesa), ações de ataque/defesa, habilidades simples, condições (ex.: envenenado, atordoado), estrutura de turnos — **fechar lista exata na Sprint 1** |
| Unidade de compilação | Um script GameLang = descrição de um combate ou de um personagem/habilidade |
| Saída do compilador nesta fase | AST validada semanticamente (execução/interpretação é bônus, não obrigação) |

---

## 4. Escopo

| Pergunta | Resposta |
|---|---|
| Dentro do escopo | Gramática GLC formal (BNF/EBNF) cobrindo os elementos da v1, analisador léxico, analisador sintático (AST), análise semântica (tabela de símbolos, checagem de tipos/atributos, referências válidas), scripts de teste (válidos e inválidos) |
| Fora de escopo | Engine gráfico de jogo, IA de combate, balanceamento de jogo, geração de código executável otimizado, multiplayer/rede |

> Um interpretador simples que simule o combate a partir da AST é **opcional**, só se sobrar tempo na Sprint 4 — não é obrigatório para o sucesso do projeto.

---

## 5. Usuários e decisão apoiada

Um game designer/desenvolvedor usa a GameLang para descrever combates declarativamente e usa o compilador para **validar o script antes de usá-lo no jogo**, decidindo o que corrigir a partir dos erros léxicos/sintáticos/semânticos reportados.

---

## 6. Referências e especificação de domínio

| Fonte | O que fornece | Papel no projeto |
|---|---|---|
| Regras de RPG de referência (ex.: sistemas simplificados de mesa, JRPGs clássicos) | Vocabulário e semântica dos elementos do domínio | Orientam o glossário e o desenho da gramática |

---

## 7. Custo dos erros de compilação

| Tipo de erro | O que significa | Custo/consequência |
|---|---|---|
| Falso negativo (erro semântico real não detectado, ex.: habilidade referenciando atributo inexistente) | Comportamento indefinido no jogo | Alto — é o erro que a análise semântica precisa evitar |
| Falso positivo (script correto rejeitado) | Trava o desenvolvimento do designer | Médio — atrapalha, mas é mais fácil de perceber e corrigir |

O falso negativo é o erro mais grave e orienta o rigor da análise semântica (checagem de referências e tipos deve ser exaustiva dentro do escopo definido).

---

## 8. Abordagem proposta (visão de alto nível)

definição do vocabulário do domínio (glossário: personagem, atributo, ação, habilidade, condição, turno) → especificação léxica (tokens/expressões regulares) → gramática GLC (BNF/EBNF) para a v1 → implementação do lexer → implementação do parser (construção da AST) → implementação da análise semântica (tabela de símbolos, checagem de referências e tipos) → bateria de scripts de teste (válidos/inválidos) → *(opcional)* interpretador simples simulando o combate a partir da AST → documentação da linguagem (gramática comentada + exemplos).

---

## 9. Riscos e limitações conhecidas

- Escopo da linguagem crescer além do viável em 5 semanas
- Ambiguidade na gramática não detectada a tempo
- Tempo insuficiente para o interpretador (tratado como opcional desde já)
- Dificuldade em cobrir a semântica de turnos e condições dinâmicas dentro do prazo

---

## 10. Critérios de sucesso

- Gramática GLC formalizada e sem ambiguidade relevante
- Lexer e parser funcionando corretamente para todos os scripts de teste válidos
- Análise semântica detectando corretamente os erros propostos nos casos de teste inválidos
- Documentação da linguagem entregue (gramática + exemplos comentados)

---

## 11. Alternativas consideradas *(opcional)*

Representar a lógica de combate em formato de dados (ex.: JSON/YAML) sem gramática própria, descartado por não exercitar os conceitos de GLC/compiladores da disciplina.

---

## 12. Perguntas em aberto

- Conjunto exato de condições e habilidades cobertas na v1 (depende do fechamento do glossário na Sprint 1)
- Se o interpretador opcional entra ou não no escopo final (depende do ritmo até a Sprint 3)

---

## 13. Cronograma e contrato entre sprints

| Sprint | Período | Produz (sai) | A próxima sprint é obrigada a usar |
|---|---|---|---|
| 1 | Semana 1 | Glossário do domínio, lista fechada de construções da v1, especificação léxica (tokens/ER), rascunho da gramática BNF/EBNF | Essa gramática, já congelada |
| 2 | Semana 2 | Lexer funcional, gramática revisada (derivações testadas manualmente, ambiguidades resolvidas), scripts de exemplo (válidos/inválidos) | Os tokens e a gramática congelada |
| 3 | Semanas 3–4 | Parser gerando AST, tabela de símbolos, checagem semântica (referências, tipos, atributos), mensagens de erro específicas | A AST já validada semanticamente |
| 4 | Semana 5 | Bateria de testes automatizados, documentação final (gramática + exemplos), interpretador simples opcional, apresentação/demo | — (entrega final) |

---

## 14. Histórico de revisões

| Versão | Data | Autor | O que mudou |
|---|---|---|---|
| v0.1 | | | Primeira versão do RFC (Sprint 1) |
| | | | |
