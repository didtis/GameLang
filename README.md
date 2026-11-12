
# GameLang

## Projeto

Desenvolvimento de um compilador para uma linguagem específica de domínio (DSL) voltada à representação da lógica de combates de RPG.

## Objetivo

O objetivo do projeto é desenvolver a GameLang, uma DSL capaz de representar elementos da lógica de combates de RPG, como personagens, atributos, ataques, defesa, habilidades, condições e turnos.

A linguagem é analisada por um compilador, utilizando uma Gramática Livre de Contexto (GLC) para definir sua estrutura sintática, passando por etapas como análise léxica, análise sintática, construção da AST e análise semântica.

## Integrantes

- Igor Nonaka Oliveira
- José Gonçalves Braz Junior
- Luis Carlos de Oliveira Dias Maia
- Marcus Gabriel Oliveira da Silva

## Turma

Ciências da Computação — 4D1_20261

## Disciplina

Linguagens Formais e Autômatos

## Orientadora

Andrea Ono Sakai

## Tecnologias utilizadas

- Python
- Pygame

## Estrutura do projeto

```text
GameLang/
├── README.md
├── requirements.txt
├── lexer/
├── parser/
├── interpreter/
├── interface/
├── exemplos/
├── assets/
├── etapas/
└── artigos/
```

## Instalação

É necessário ter o Python instalado.

Clone o repositório:

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

## Execução

Para executar um exemplo pelo terminal:

```bash
python main.py exemplos/combate.gl --terminal
```

Para executar o exemplo com a interface gráfica:

```bash
python main.py exemplos/combate.gl
```

## Etapas do compilador

O projeto possui as seguintes etapas:

1. Análise léxica: identificação dos tokens da linguagem.
2. Análise sintática: verificação da estrutura dos comandos conforme a gramática.
3. Construção da AST: organização da estrutura sintática em uma árvore.
4. Análise semântica: verificação de regras e referências dos personagens.
5. Interpretação: execução dos comandos da GameLang.
6. Interface gráfica: representação visual do combate.

## Exemplo de código

```text
CRIAR HEROI Arthur VIDA 100 ATAQUE 20 DEFESA 10

CRIAR INIMIGO Goblin VIDA 30 ATAQUE 10 DEFESA 5

ATACAR Arthur Goblin

FIM
```

## Repositório

https://github.com/didtis/GameLang
