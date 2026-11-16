# GameLang — Uma linguagem para combates de RPG

## Projeto

Desenvolvimento de um compilador para uma linguagem específica de domínio (DSL) voltada à representação da lógica de combates de RPG.

## Objetivo

O objetivo do projeto é desenvolver a GameLang, uma DSL capaz de representar elementos da lógica de combates de RPG, como personagens, atributos, ataques, defesa, habilidades, condições e turnos.

A linguagem é analisada por um compilador utilizando uma Gramática Livre de Contexto (GLC), passando por etapas como análise léxica, análise sintática, construção da AST, análise semântica e execução dos comandos.

## Integrantes

- Igor Nonaka Oliveira
- José Gonçalves Braz Junior
- Marcus Gabriel Oliveira da Silva

## Informações acadêmicas

- **Curso:** Ciências da Computação
- **Turma:** 4D1_20261
- **Disciplina:** Linguagens Formais e Autômatos
- **Orientadora:** Profa. Dra. Andrea Ono Sakai

## Tecnologias utilizadas

- Python
- Pygame

## Estrutura do projeto

```text
GameLang/
├── README.md
├── main.py
├── requirements.txt
├── lexer/
├── parser/
├── interpreter/
├── interface/
│   └── assets/
├── exemplos/
├── etapas/
├── artigos/
└── Sprints/
```

## Instalação

É necessário ter o Python instalado.

Primeiro, clone o repositório:

```bash
git clone https://github.com/didtis/GameLang.git
```

Entre na pasta do projeto:

```bash
cd GameLang
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como executar

### 1. Modo interativo

Para abrir o menu de apresentação da GameLang:

```bash
python main.py --interativo
```

Nesse modo, o usuário pode:

1. Aprender como escrever comandos na GameLang.
2. Consultar os comandos disponíveis.
3. Visualizar um exemplo de código.
4. Escrever seu próprio combate.
5. Executar o exemplo completo do projeto.

### 2. Execução visual

Para executar diretamente o exemplo de combate com a interface gráfica:

```bash
python main.py exemplos/combate.gl
```

Na janela do Pygame:

- **ESPAÇO:** avança para o próximo comando.
- **ESC:** encerra a interface.

### 3. Execução pelo terminal

Para executar o exemplo sem abrir a interface gráfica:

```bash
python main.py exemplos/combate.gl --terminal
```

## Etapas do compilador

A GameLang realiza o processamento dos comandos por meio das seguintes etapas:

1. **Análise léxica:** identifica os elementos da linguagem, como palavras-chave, identificadores, números e operadores, transformando-os em tokens.
2. **Análise sintática:** verifica se os comandos seguem a estrutura definida pela gramática da GameLang.
3. **Construção da AST:** organiza os comandos reconhecidos em uma árvore sintática abstrata.
4. **Análise semântica:** verifica regras de significado, como a existência dos personagens utilizados nos comandos.
5. **Execução:** interpreta os comandos que passaram pelas análises anteriores.
6. **Interface gráfica:** representa visualmente as ações do combate utilizando o Pygame.

## Exemplo de código

```text
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10

CRIAR INIMIGO Goblin VIDA 50 ATAQUE 10 DEFESA 5

TURNO Arthur
MOVER Arthur DIREITA
ATACAR Arthur Goblin

TURNO Goblin
DEFENDER Goblin
```

## Comandos disponíveis

| Comando | Função |
|---|---|
| `CRIAR HEROI` | Cria um personagem do tipo herói. |
| `CRIAR INIMIGO` | Cria um personagem do tipo inimigo. |
| `ATACAR` | Executa um ataque contra outro personagem. |
| `DEFENDER` | Executa uma ação de defesa. |
| `HABILIDADE` | Utiliza uma habilidade. |
| `TURNO` | Define o personagem do turno. |
| `MOVER` | Movimenta um personagem no tabuleiro. |
| `SE` | Verifica uma condição. |
| `SENAO` | Define uma alternativa para a condição. |
| `REPETIR` | Repete um bloco de comandos. |
| `FIM` | Encerra um bloco de comandos. |

## Repositório

[GitHub — GameLang](https://github.com/didtis/GameLang)
