# Etapa (a) — Escolha do Tema

> **Como preencher:** este documento deve ser preenchido **em conjunto pelo grupo**, mas com registro individualizado da contribuição de cada integrante. Substitua os campos entre `[ ]` pelas informações do seu grupo. Não apague as instruções em itálico — elas ajudam na avaliação do orientador.

---

## 1. Identificação do Grupo

| Campo | Informação |
|---|---|
| Curso / Disciplina | `[Ciências da Computação — Linguagens Formais e Autômatos]` |
| Projeto de Pesquisa / IC | `[Desenvolvimento de um compilador para uma linguagem especifica de domínio voltada a lógica de combates de rpg]` |
| Orientador(a) | `[Andrea Ono Sakai]` |
| Data de entrega desta etapa | `[18/08/2026]` |
| Integrantes do grupo | `[Igor Nonaka Oliveira, José Gonçalves Braz Junior, Luis Carlos de Oliveira Dias Maia, Marcus Gabriel Oliveira da Silva]` |

---

## 2. Tema Escolhido

### 2.1 Área geral de interesse
*Qual grande área do conhecimento/disciplina motivou a escolha (ex.: complexidade dos algoritmos, classes de problemas P, NP, Algoritmos Gulosos, Programação Dinâmica, Divisão e conquista)?*

`[Linguagens Formais, Compiladores e Linguagens Específicas de Domínio (DSLs), com foco na utilização de Gramáticas Livres de Contexto (GLCs) para definição da sintaxe de uma linguagem própria.]`

### 2.2 Tema delimitado (versão final)
*Escreva o tema já delimitado, de forma específica — não o tema amplo. Lembre-se: o tema deve ser enunciado em 1 a 2 frases, como um assunto (ainda não é uma pergunta de pesquisa, isso vem na etapa "c").*

> **Tema:** `[Desenvolvimento de uma linguagem específica de domínio (DSL), denominada provisoriamente GameLang, e de um compilador capaz de analisar programas voltados à representação da lógica de combates de jogos do gênero RPG, utilizando uma Gramática Livre de Contexto para especificar sua sintaxe.]`

### 2.3 Do amplo ao específico
*Mostre o raciocínio de delimitação — como vocês chegaram do tema amplo ao tema específico.*

| Tema amplo (ponto de partida) | Tema delimitado (ponto de chegada) |
|---|---|
| `[Linguagens Formais]` | `[Aplicação de formalismos de linguagens na construção de uma linguagem própria]` |
| `[Gramáticas Livres de Contexto]` | `[Utilização de uma GLC para definir formalmente a sintaxe da GameLang]` |
| `[Compiladores]` | `[ Desenvolvimento das etapas de um compilador para analisar programas GameLang]` |
| `[Linguagens Específicas de Domínio (DSLs)]` | `[Criação de uma DSL voltada à representação de lógica de combates de RPG]` |
| `[Jogos e programação]` | `[Representação de personagens, atributos, ataques, defesa, habilidades, condições e turnos por meio de uma linguagem própria]` |

---

## 3. Justificativa da Escolha

### 3.1 Relevância
*Por que esse tema é importante ou atual? Para quem ele importa (academia, mercado, sociedade)?*

`[O tema é relevante por integrar conceitos teóricos de Linguagens Formais e Compiladores a uma aplicação prática relacionada ao desenvolvimento de jogos. A criação da GameLang permite utilizar uma Gramática Livre de Contexto para especificar formalmente a sintaxe da linguagem e relacionar esse conhecimento à construção de um analisador sintático. Além disso, o projeto permite trabalhar diferentes etapas de um compilador, incluindo análise léxica, análise sintática, construção de uma Árvore Sintática Abstrata (AST), análise semântica e geração de saída. Dessa forma, o projeto possibilita transformar conceitos estudados na disciplina em uma implementação prática e testável. O trabalho também possui potencial para continuidade acadêmica, pois o desenvolvimento, os testes, as decisões de projeto e os resultados obtidos poderão posteriormente servir como base para um Trabalho de Conclusão de Curso (TCC).]`

### 3.2 Viabilidade
*O grupo avaliou se tem tempo, recursos, acesso a dados/fontes e domínio mínimo do assunto para desenvolver esse tema até o fim do projeto?*

| Critério | Avaliação (Sim/Parcial/Não) | Observação |
|---|---|---|
| Tempo disponível é suficiente | `[Parcial]` | `[Dois dos integrantes trabalham e os outros dois tem tempo limitado]` |
| Há acesso a fontes/dados necessários | `[Sim]` | `[O grupo possui acesso a bibliotecas digitais, mecanismos de busca acadêmica e artigos científicos necessários ao levantamento bibliográfico.]` |
| O grupo já tem domínio mínimo do tema | `[Parcial]` | `[Alguns tem, outros não]` |
| Recursos técnicos necessários estão disponíveis | `[Sim]` | `[Presumimos que os nossos dispositivos não terão problemas]` |

### 3.3 Originalidade / Não-redundância
*O grupo verificou rapidamente (via um levantamento preliminar) se o tema já é excessivamente explorado ou se existe um ângulo próprio a ser explorado?*

`[Foi realizado um levantamento preliminar para identificar trabalhos relacionados a DSLs, compiladores, gramáticas e aplicações de linguagens em jogos. Até o momento, o diferencial proposto pelo grupo é a aplicação desses conceitos na criação de uma DSL voltada à representação genérica da lógica de combates de RPG. O levantamento de trabalhos semelhantes continuará durante o desenvolvimento e a seleção das referências acadêmicas.]`

---

## 4. Validação com o Orientador

| Campo | Informação |
|---|---|
| Data da conversa/validação | `[28/08/2026]` |
| Tema aprovado pelo orientador? | `[Sim com ajustes]` |
| Observações ou ajustes solicitados pelo orientador | `[Detalhar como a complexidade de cada fase do compilador será medida/analisada; os integrantes devem mostrar evidências e descrições de contribuição mais específicas.]` |

---

## 5. Contribuição Individual dos Integrantes

> **Importante:** cada integrante deve descrever, com suas próprias palavras, o que efetivamente fez nesta etapa. Contribuições genéricas como "ajudei em tudo" não serão aceitas. Use verbos de ação e seja específico (ex.: "pesquisei 5 temas candidatos e apresentei prós/contras ao grupo").

### Integrante 1 — `[Igor Nonaka Oliveira]`
- **O que fez nesta etapa:** `[Pesquisou o tema]`
- **Tempo dedicado (aprox.):** `[6h]`
- **Evidência da contribuição** *(print de conversa, rascunho, e-mail, documento compartilhado etc.)*: `[Igor: Qual linguagem formal se encaixa em compilador de jogos? ChatGPT: Se você está falando de linguagens formais usadas na construção de compiladores para jogos, a mais adequada depende da parte do compilador: Gramáticas livres de contexto (GLC) → descrevem a sintaxe da linguagem usada para programar o jogo. Expressões regulares / linguagens regulares → usadas principalmente no analisador léxico, para reconhecer tokens como números, identificadores e operadores. Gramáticas de atributos → podem representar informações semânticas, como tipos e escopos. Máquinas de estados finitos → muito comuns na implementação do lexer. Por exemplo, se você está criando uma linguagem de programação própria para um game engine, uma combinação típica seria: Linguagem regular → análise léxica → GLC → análise sintática → análise semântica → código intermediário → código de máquina /bytecode...]`

### Integrante 2 — `[José Gonçalves Braz Junior]`
- **O que fez nesta etapa:** `[Pesquisou o tema, deu início no tema, pesquisou os artigos]`
- **Tempo dedicado (aprox.):** `[20h]`
- **Evidência da contribuição:** `[José: Estrutura planejada do compilador A estrutura geral que estamos planejando é: 
Código GameLang
       ↓ 
Analisador Léxico (Lexer)
       ↓
Tokens
       ↓
Analisador Sintático (Parser)
       ↓
GLC       
       ↓
AST
       ↓
Análise Semântica
       ↓
Geração de código / saída

O Lexer, Parser, AST, análise semântica e geração de código ainda serão desenvolvidos]`

### Integrante 3 — `[Luis Carlos de Oliveira Dias Maia]`
- **O que fez nesta etapa:** `[Nos auxiliou com o seu conhecimento]`
- **Tempo dedicado (aprox.):** `[1h]`
- **Evidência da contribuição:** `[Luis: Analise da pesquisa realizada em aula juntamente pelo grupo]`

### Integrante 4 — `[Marcus Gabriel Oliveira da Silva]`
- **O que fez nesta etapa:** `[Pesquisou os artigos]`
- **Tempo dedicado (aprox.):** `[6h]`
- **Evidência da contribuição:** `[Nome dos artigos ciêntificos: Supporting meta-model-based language evolution and rapid prototyping with automated grammar transformation — 2024, Development and evolution of Xtext-based DSLs on GitHub: an empirical investigation — 2025/2026, A Concrete Syntax Transformation Approach for Software Language Processing — 2024, iCoLa+: An extensible meta-language with support for exploratory language development — 2024]`

*(Copie o bloco acima para cada integrante adicional do grupo.)*

### 5.1 Quadro-resumo de participação

| Integrante | Contribuição principal | % estimado de participação nesta etapa |
|---|---|---|
| `[Igor]` | `[Pesquisa sobre o tema]` | `[20%]` |
| `[José]` | `[Desenvolvedor]` | `[40%]` |
| `[Luis]` | `[Consultor]` | `[10%]` |
| `[Marcus]` | `[Pesquisa sobre os artigos do tema]` | `[30%]` |

*A soma das porcentagens deve ser igual a 100%. Divergências de percepção sobre a participação devem ser discutidas em grupo antes do envio — o orientador pode solicitar esclarecimentos individuais em caso de disparidade relevante.*

---

## 6. Checklist Final da Etapa

- [✓] Tema delimitado e redigido em 1-2 frases
- [✓] Justificativa de relevância escrita
- [✓] Viabilidade avaliada pelo grupo
- [✓] Verificação preliminar de originalidade realizada
- [✓] Tema validado com o orientador
- [✓] Contribuição individual de cada integrante registrada
- [✓] Quadro-resumo de participação preenchido (soma = 100%)

---


