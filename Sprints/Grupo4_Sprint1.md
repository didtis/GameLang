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
| Quais elementos do domínio a v1 cobre (personagens, atributos, ataques, defesa, habilidades, condições, turnos)? | Personagens, aliados, atributos, ataques, defesa, habilidades, condições, turnos, inimigos, movimentação |
| Qual é a unidade de compilação (um script = um combate? um personagem? uma habilidade)? | Um combate |
| Qual é a saída do compilador nesta fase (AST validada; execução é bônus)? | Execução do combate |
| Justificativa do recorte escolhido para a v1 (o que fica de fora e por quê) | Imagens dos personagens, estágios e itens ficam fora do escopo da v1, pois o foco da GameLang nesta etapa é representar a lógica do combate. Esses elementos poderão ser representados posteriormente por símbolos ou referências.|

- [X] Elementos do domínio da v1 listados e fechados
- [X] Unidade de compilação definida sem ambiguidade
- [X] Recorte da v1 justificado (o que fica de fora explicitamente)

## 2. Glossário do domínio

- [X] Cada termo do domínio (personagem, atributo, ação, habilidade, condição, turno) definido em uma frase
- [X] Relações entre os termos esclarecidas (ex.: uma habilidade pode alterar um atributo ou aplicar uma condição)

**Glossário:**

| Termo | Definição | Relação com outros termos |
| Personagens | Representação das entidades do jogo, sendo os elementos necessarios para que uma batalha possa acontecer | Aliados e inimigos são os personagens |
| Aliados | Representação do jogador | Os atributos, ataque, defesa, habilidades, condições, e movimentação, são as definições das capacidades dos personagens / Turnos, afeta as escolhas do aliado em seu turno / Inimigos, interagem com o aliado, servindo como obstaculos, para atrapalhar o seu progresso |
| Atributos | São os status dos personagens (Características e condições que definem a capacidade dos personagems) | São informações para atribuir os Status dos personagens, afetando também, ataque, defesa, e habilidades |
| Ataque | A capacidade de causar ou receber dano | Com o ataque, o personagem pode causar e receber dano, diminuindo os pontos de vida (HP), o mesmo caso acontece com os inimigos|
| Defesa | A capacidade de resistir, ou diminuir o dano recebido pelo inimigo | No momento de defesa, o aliado consegue fazer a tentativa de se defender contra um inimigo, fazendo com que perca menos HP |
| Habilidade | A capacidade de poder fazer um movimento mais complexo com uma certa condição (Um ataque mais forte, um movimento de suporte para aumentar ou diminuir os Status do determinado alvo, etc) | Afeta aliados e inimigos de uma forma mais dinâmica comparado ao ataque e defesa, é fortemente baseado nos atributos e condições |
| Condições | Define demandas para o personagem em questão poder fazer uma certa ação | Afeta mais as habilidades dos personagens dando uma condição para poder utiliza-la (Por exemplo, utilizar parte do HP, utilizar ponots de magia [MP], etc) |
| Turnos | Periodo de combate em que os personagens podem fazer as suas ações | Determina quando aliados ou inimigos podem realizar a sua ação na batalha |
| Inimigos | Personagens que atuam como adversarios durante o combate | Integarem contra aliados por meio de ataques e habilidades |
| Movimentação | Permite que os aliados se desloquem pelo mundo, avançando uma casa por vez | Afeta os aliados e inimigos, permitindo que se movimentem pelo mapa, porém ao interagir com os inimigos, eles impedirão que você se movimente antes que a batalha acabe |

## 3. Especificação léxica

- [X] Tabela de tokens (palavras-chave, identificadores, literais, símbolos) com expressão regular de cada um
- [X] Palavras-chave escolhidas alinhadas ao glossário da seção 2
- [X] Casos de ambiguidade léxica verificados

**Tabela de tokens:**

| Token | Expressão regular | Exemplo |
|CRIAR|CRIAR|CRIAR|
|HEROI|HEROI|HEROI|
|INIMIGO|INIMIGO|INIMIGO|
|VIDA|VIDA|VIDA|
|ATAQUE|ATAQUE|ATAQUE|
|DEFESA|DEFESA|DEFESA|
|HABILIDADE|HABILIDADE|HABILIDADE|
|TURNO|TURNO|TURNO|
|SE|SE|SE|
|SENAO|SENAO|SENAO|
|FIM|FIM|FIM|
|REPETIR|REPETIR|REPETIR|
|MOVER|MOVER|MOVER|
| CIMA | CIMA | CIMA |
| BAIXO | BAIXO | BAIXO |
| ESQUERDA | ESQUERDA | ESQUERDA |
| DIREITA | DIREITA | DIREITA |
|IDENTIFICADOR|[A-Za-z_][A-Za-z0-9_]*|Arthur|
|NUMERO|[0-9]+|100|
|OPERADOR_RELACIONAL |<=|>=|==|<|>| <= |

## 4. Rascunho da gramática e exemplos-alvo

- [X] Gramática em BNF/EBNF cobrindo todas as construções da lista fechada (seção 1)
- [X] Pelo menos 3 scripts de exemplo (ex.: um personagem, uma habilidade, um turno de combate simples)
- [X] Derivação manual de pelo menos 1 exemplo, para checar se a gramática gera o script esperado

**Gramática (BNF/EBNF):**
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
                  [ SENAO 
                    { <comando> } ]
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

<identificador> ::= ...
<numero> ::= ...
**Scripts de exemplo:**
### 1. Criação de personagens

text
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5


### 2. Turno, movimentação, ataque e defesa

text
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5

TURNO Arthur
MOVER Arthur DIREITA
ATACAR Arthur Goblin
DEFENDER Arthur


### 3. Condição e habilidade

text
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10
CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5

SE VIDA Goblin <= 20
    HABILIDADE Arthur GOLPE_FORTE
SENAO
    ATACAR Arthur Goblin
FIM

Derivação manual
<comando>
↓
<ataque>
↓
ATACAR <identificador> <identificador>
↓
ATACAR Arthur Goblin

## 5. Scrum

- [X] Papéis definidos (Product Owner = docente; Scrum Master do sprint; Development Team)
- [x] Board criado (GitHub Projects ou Trello) com To do / Doing / Done
- [x] Backlog inicial com pelo menos 3 user stories

**User stories do backlog inicial:**
1.Como integrante do grupo, quero definir os elementos do domínio da GameLang para estabelecer quais conceitos farão parte da linguagem.
2.Como desenvolvedor da GameLang, quero definir os tokens e suas expressões regulares para estabelecer a especificação léxica da linguagem.
3.Como desenvolvedor da GameLang, quero definir a gramática da linguagem para estabelecer quais estruturas são válidas nos scripts.

**Link do board:**

## 6. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|José Gonçalves Braz Junior|Participei da definição dos elementos do domínio, do glossário, da especificação léxica e da gramática da GameLang. Também organizei o quadro Scrum e dei continuidade à documentação do Sprint 1.|Tive dificuldade em transformar os conceitos da GameLang em regras formais e em organizar a gramática de forma que representasse corretamente os comandos definidos|Pretendo manter a organização das etapas e a revisão da gramática antes da implementação. Também pretendo melhorar a divisão das tarefas e o acompanhamento do Sprint.|
| | | | |
| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|Igor Nonaka Oliveira|Participei da definição dos elementos do domínio, do glossário, da especificação léxica e da gramática da GameLang junto ao grupo durante a aula|Tive dificuldade em transformar as ideias do domínio do RPG em uma estrutura de linguagem e em definir algumas regras da gramática.|Pretendo manter a organização das etapas e continuar participando da definição e revisão da linguagem nas próximas etapas.|
| | | | |
| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|Marcus Gabriel Oliveira da Silva|Participei junto ao grupo da definição dos elementos do domínio, do glossário, dos tokens, das expressões regulares e da gramática da GameLang até o final da aula.|Tive dificuldade em organizar os conceitos do combate de RPG de forma que pudessem ser representados pela linguagem.|Pretendo continuar colaborando com o grupo e revisar as definições antes de iniciar a implementação.|
| | | | |

## 7. Evidências gerais

- Link do canvas:https://docs.google.com/document/d/1RNtUeo0gL_-ifj41nFv4RKTm4IcYX2WxFDOIIQL_Fx8/edit?usp=sharing
- Link do glossário:https://docs.google.com/document/d/1_vEDmbeeLQKD4-9uirkbxWLAbXCzmaLF_YB7WdtpfBs/edit?usp=sharing
- Link do rascunho da gramática: https://docs.google.com/document/d/1UQ62_zqI0mNml6Ioge9Mqil4ke3zuhQ4sxF-twgoFsE/edit?usp=sharing
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
