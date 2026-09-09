# Etapa (b) — Levantamento Bibliográfico

> **Como preencher:** este documento deve ser preenchido **em conjunto pelo grupo**, mas com registro individualizado da contribuição de cada integrante em cada passo. Substitua os campos entre `[ ]` pelas informações do seu grupo. Não apague as instruções em itálico — elas ajudam na avaliação do orientador.

---

## 1. Identificação do Grupo

| Campo | Informação |
|---|---|
| Curso / Disciplina | `[Ciências da Computação — Linguagens Formais e Autômatos]` |
| Projeto de Pesquisa / IC | `[Desenvolvimento de um compilador para uma linguagem específica de domínio voltada à lógica de combates de RPG]` |
| Orientador(a) | `[Andrea Ono Sakai]` |
| Data de entrega desta etapa | `[dd/mm/aaaa]` |
| Integrantes do grupo | `[Igor Nonaka Oliveira; José Gonçalves Braz Junior; Luis Carlos de Oliveira Dias Maia; Marcus Gabriel Oliveira da Silva]` |
| Tema (da etapa "a") | `[Desenvolvimento de uma DSL, denominada provisoriamente GameLang, e de um compilador capaz de analisar programas que representam a lógica de combates de RPG, utilizando uma Gramática Livre de Contexto (GLC) para especificação da sintaxe]` |

---

## FASE 1 — Planejamento da Busca

### Passo 1 — Pergunta de pesquisa e palavras-chave

**1.1 Problema/pergunta de pesquisa (versão de trabalho)**
*Ainda não precisa ser a versão final (isso vem na etapa "c"), mas deve orientar a busca desta fase.*

> `[Como uma linguagem específica de domínio (DSL) baseada em uma Gramática Livre de Contexto (GLC) pode representar a lógica de combates de RPG e ser processada por um compilador, considerando as etapas de análise sintática, construção da AST e complexidade do parsing?]`

**1.2 Conceitos-chave e sinônimos**
*Liste os conceitos centrais da pergunta e seus sinônimos, em português e inglês.*

| Conceito-chave | Sinônimos / termos relacionados (PT) | Sinônimos / termos relacionados (EN) |
|---|---|---|
| `[ex.: Segurança]` | `[proteção, vulnerabilidade]` | `[security, vulnerability]` |
| `[ex.: IoT]` | `[Internet das Coisas]` | `[Internet of Things, smart devices]` |
| `[DSL]` | `[Linguagem específica de domínio; linguagem de domínio específico]` | `[Domain-Specific Language; DSL]` |
| `[Compilador]` | `[Compilação; processo de compilação]` | `[Compiler; compilation]` |
| `[GLC]` | `[Gramática Livre de Contexto; gramática formal]` | `[Context-Free Grammar; CFG]` |
| `[Análise sintática]` | `[Parsing; analisador sintático]` | `[Syntax analysis; parsing; parser]` |
| `[AST]` | `[Árvore sintática abstrata; árvore de sintaxe]` | `[Abstract Syntax Tree; AST]` |
| `[Complexidade]` | `[Complexidade computacional; desempenho]` | `[Computational complexity; performance]` |
| `[Jogos/RPG]` | `[Jogos digitais; combate de RPG]` | `[Games; RPG; role-playing games; game combat]` |

*Responsável por este passo: `[José Gonçalves Braz Junior]`*

---

### Passo 2 — Strings de busca

*Combine os termos do passo 1 com operadores booleanos (`AND`, `OR`, `NOT`). Use aspas para termos compostos e truncamento (`*`) quando a base permitir.*

| Nº | String de busca | Base(s) em que será usada | Elaborada por |
|---|---|---|---|
| 1 | `[("Domain-Specific Language" OR DSL) AND ("Context-Free Grammar" OR CFG) AND (parser OR parsing)]` | `[IEEE Xplore; Google Scholar; Portal CAPES]` | `[José Gonçalves Braz Junior]` |
| 2 | `[("Domain-Specific Language" OR DSL) AND (compiler OR compilation) AND (parsing OR parser)]` | `[IEEE Xplore; Google Scholar; Portal CAPES]` | `[José Gonçalves Braz Junior]` |
| 3 | `[("Domain-Specific Language" OR DSL) AND (games OR "role-playing game" OR RPG) AND (grammar OR parsing)]` | `[IEEE Xplore; Google Scholar; Portal CAPES]` | `[José Gonçalves Braz Junior]` |

---

### Passo 3 — Bases de dados escolhidas

*Selecione de 2 a 4 bases relevantes ao tema. Registre a justificativa — isso vai para a seção de metodologia do artigo/relatório de IC.*

| Base de dados | Por que foi escolhida | Responsável pela busca nesta base |
|---|---|---|
| `[IEEE Xplore]` | `[Base relevante para pesquisas na área de computação, compiladores, linguagens de programação e desenvolvimento de software.]` | `[José Gonçalves Braz Junior]` |
| `[Portal CAPES]` | `[Permite acesso a periódicos e trabalhos científicos de diferentes áreas, incluindo computação e engenharia de software.]` | `[José Gonçalves Braz Junior]` |
| `[Google Scholar]` | `[Utilizado para ampliar a busca e localizar artigos científicos, trabalhos acadêmicos e publicações relacionadas ao tema.]` | `[José Gonçalves Braz Junior]` |

---

### Passo 4 — Critérios de inclusão e exclusão

**Critérios de inclusão:**
- `[Artigos publicados preferencialmente entre 2018 e 2026]`
- `[trabalhos relacionados a DSLs (Domain-Specific Languages)]`
- `[Trabalhos relacionados a compiladores, parsing ou análise sintática]`
- `[Trabalhos que abordem Gramáticas Livres de Contexto (GLC/CFG) ou técnicas relacionadas à definição e análise de linguagens]`
- `[Artigos em português ou inglês]`
- `[Trabalhos com conteúdo suficiente para análise e utilização como referência no projeto]`

**Critérios de exclusão:**
- `[Resumos sem conteúdo suficiente para análise]`
- `[Artigos duplicados entre as bases pesquisadas]`
- `[Trabalhos fora do escopo de DSL, compiladores, parsing, gramáticas ou áreas relacionadas ao projeto]`
- `[Trabalhos que não apresentem relação relevante com a proposta do GameLang]`
- `[Trabalhos sem informações suficientes para identificação e análise da publicação]`

*Definidos em conjunto por: `[José Gonçalves Braz Junior e demais integrantes do grupo]`*

---

## FASE 2 — Execução da Busca e Triagem

### Passo 5 — Execução das buscas e registro dos resultados

*Anote quantos resultados cada string trouxe em cada base (útil para o fluxograma tipo PRISMA, se o projeto exigir). Exporte as referências (BibTeX, RIS, CSV) para um gerenciador de referências.*

| Base | String usada (nº) | Data da busca | Nº de resultados | Executada por |
|---|---|---|---|---|
| `[IEEE Xplore]` | `[1]` | `[20/08/2026]` | `[1]` | `[Igor Nonaka Oliveira]` |
| `[IEEE Xplore]` | `[2]` | `[20/08/2026]` | `[2]` | `[Igor Nonaka Oliveira]` |
| `[IEEE Xplore]` | `[3]` | `[22/08/2026]` | `[0]` | `[Igor Nonaka Oliveira]` |
| `[Portal CAPES]` | `[1]` | `[22/08/2026]` | `[13]` | `[Igor Nonaka Oliveira]` |
| `[Portal CAPES]` | `[2]` | `[22/08/2026]` | `[18]` | `[Igor Nonaka Oliveira]` |
| `[Portal CAPES]` | `[3]` | `[23/08/2026]` | `[1]` | `[Igor Nonaka Oliveira]` |
| `[Google Scholar]` | `[1]` | `[26/08/2026]` | `[aproximadamente 3.500]` | `[Igor Nonaka Oliveira]` |
| `[Google Scholar]` | `[2]` | `[26/08/2026]` | `[aproximadamente 15.600]` | `[Igor Nonaka Oliveira]` |
| `[Google Scholar]` | `[3]` | `[26/08/2026]` | `[aproximadamente 5.040]` | `[Igor Nonaka Oliveira]` |

**Total de resultados brutos (soma de todas as buscas):** `[24.175 resultados]`

**Gerenciador de referências utilizado:** `[Gerenciador de referências utilizado: Não utilizado.]`
**Formato de exportação:** `[Formato de exportação: Não utilizado.]`

---

### Passo 6 — Triagem por título e resumo (1ª filtragem)

*Leia apenas título e resumo de cada resultado. Classifique: incluir / excluir / dúvida. Remova duplicatas entre bases.*

| Item de controle | Quantidade |
|---|---|
| Total de resultados antes da triagem | `[24]` |
| Duplicatas removidas | `[1]` |
| Classificados como "Incluir" | `[5]` |
| Classificados como "Excluir" | `[11]` |
| Classificados como "Dúvida" | `[7]` |

*A triagem detalhada, artigo por artigo, deve ser registrada na planilha de controle do projeto (aba "Triagem de Artigos"). Aqui, registre apenas o resumo quantitativo.*

**Como as dúvidas foram resolvidas?** *(ex.: discussão em grupo, consulta ao orientador)*
`[As dúvidas foram resolvidas por meio de discussão entre os integrantes do grupo, considerando a relação dos artigos com o tema da GameLang, os critérios de inclusão e exclusão definidos e a relevância dos trabalhos para DSLs, compiladores, parsing e gramáticas. Nos casos em que permaneceu alguma incerteza, os artigos foram encaminhados para análise mais detalhada na etapa de leitura do texto completo.]`

*Responsável(is) por esta triagem: `[José Gonçalves Braz Junior, Igor Nonaka Oliveira, Luis Carlos de Oliveira Dias Maia e Marcus Gabriel Oliveira da Silva]`*

---

### Passo 7 — Triagem por leitura completa (2ª filtragem)

*Para os artigos que passaram na primeira filtragem, leia introdução e conclusão. Aplique os critérios de inclusão/exclusão (passo 4) de forma mais rigorosa.*

| Item de controle | Quantidade |
|---|---|
| Total de artigos que entraram nesta filtragem | `[5]` |
| Aprovados (conjunto definitivo para fichamento) | `[5]` |
| Excluídos nesta etapa | `[0]` |

**Principais motivos de exclusão nesta filtragem:**
- `[Não houve exclusões nesta etapa]`
- `[Os cinco artigos analisados atenderam aos critérios definidos e foram mantidos para o fichamento.]`

*Responsável(is) por esta triagem: `[José Gonçalves Braz Junior, Igor Nonaka Oliveira, Luis Carlos de Oliveira Dias Maia e Marcus Gabriel Oliveira da Silva]`*

---

## 3. Lista Final de Artigos Selecionados (Conjunto Definitivo)

*Liste aqui os artigos que passaram por todas as filtragens e seguirão para o fichamento (etapa "j"). Referência completa no formato ABNT/APA definido pelo projeto.*

1. `[Context-sensitive Parsing for Programming Languages (2022)]`
2. `[Determining Programming Languages Complexity and Its Impact on Processing (2022)]`
3. `[A Concrete Syntax Transformation Approach for Software Language Processing (2024)]`
4. `[Supporting Meta-model-based Language Evolution and Rapid Prototyping with Automated Grammar Transformation (2024)]`
5. `[GIGL: A Domain Specific Language for Procedural Content Generation with Grammatical Representations (2018)]`

*(Adicione quantas linhas forem necessárias.)*

---

## 4. Contribuição Individual dos Integrantes

> **Importante:** cada integrante deve descrever, com suas próprias palavras, o que efetivamente fez em cada passo desta etapa. Contribuições genéricas como "ajudei em tudo" não serão aceitas. Use verbos de ação e seja específico (ex.: "executei a busca no IEEE Xplore com a string 2 e obtive 84 resultados; fiz a triagem por título/resumo de 40 desses").

### Integrante 1 — `[Igor Nonaka Oliveira]`
- **Passo(s) em que atuou:** `[Passos 1, 5 e 6.]`
- **O que fez em cada passo:** `[Participou da definição do tema e dos conceitos relacionados ao projeto GameLang. Auxiliou na pesquisa bibliográfica e na identificação de trabalhos relacionados ao tema. Também participou da triagem dos artigos encontrados, avaliando títulos e resumos de acordo com os critérios definidos pelo grupo]`
- **Tempo dedicado (aprox.):** `[6h]`
- **Evidência da contribuição** *(print de busca, planilha de triagem, exportação BibTeX, etc.)*: `[link ou descrição]`

### Integrante 2 — `[José Gonçalves Braz Junior]`
- **Passo(s) em que atuou:** `[Passos 1, 2, 3, 4, 5, 6 e 7]`
- **O que fez em cada passo:** `[Participou da definição da pergunta de pesquisa, conceitos-chave e palavras-chave. Elaborou e executou as strings de busca nas bases IEEE Xplore, Portal CAPES e Google Scholar. Auxiliou na definição dos critérios de inclusão e exclusão, organizou os resultados encontrados e participou da triagem por título e resumo. Também participou da análise dos artigos selecionados para a segunda filtragem]`
- **Tempo dedicado (aprox.):** `[20h]`
- **Evidência da contribuição:** `[link ou descrição]`

### Integrante 3 — `[Luis Carlos de Oliveira Dias Maia]`
- **Passo(s) em que atuou:** `[Passos 4, 6 e 7]`
- **O que fez em cada passo:** `[Contribuiu para a discussão dos critérios utilizados para selecionar os artigos. Participou da análise dos títulos e resumos dos trabalhos encontrados e auxiliou na avaliação dos artigos que passaram para a segunda filtragem]`
- **Tempo dedicado (aprox.):** `[1h]`
- **Evidência da contribuição:** `[link ou descrição]`

### Integrante 4 — `[Marcus Gabriel Oliveira da Silva]`
- **Passo(s) em que atuou:** `[Passos 5, 6 e 7]`
- **O que fez em cada passo:** `[Realizou pesquisas por artigos relacionados a DSLs, compiladores, parsing e gramáticas. Auxiliou na seleção dos trabalhos relevantes e participou da triagem por título e resumo. Também contribuiu para a análise dos artigos selecionados para a leitura completa]`
- **Tempo dedicado (aprox.):** `[6h]`
- **Evidência da contribuição:** `[link ou descrição]`
*(Copie o bloco acima para cada integrante adicional do grupo.)*

### 4.1 Quadro-resumo de participação por passo

| Passo | Responsável(is) | % estimado de participação de cada um |
|---|---|---|
| 1. Pergunta e palavras-chave | `[José, Igor, Luis, Marcus]` | `[José 40% / Igor 20% / Luis 10% / Marcus 30%]` |
| 2. Strings de busca | `[José]` | `[José 100%]` |
| 3. Bases de dados | `[José]` | `[José 100%]` |
| 4. Critérios de inclusão/exclusão | `[José, Igor, Luis, Marcus]` | `[José 40% / Igor 20% / Luis 10% / Marcus 30%]` |
| 5. Execução das buscas | `[José, Igor, Marcus]` | `[José 40% / Igor 30% / Marcus 30%]` |
| 6. Triagem título/resumo | `[José, Igor, Luis, Marcus]` | `[José 40% / Igor 20% / Luis 10% / Marcus 30%]` |
| 7. Triagem texto completo | `[José, Luis, Marcus]` | `[José 40% / Luis 20% / Marcus 40%]` |

### 4.2 Quadro-resumo geral de participação na etapa

| Integrante | % estimado de participação total nesta etapa |
|---|---|
| `[José Gonçalves Braz Junior]` | `[40%]` |
| `[Igor Nonaka Oliveira]` | `[20%]` |
| `[Luis Carlos de Oliveira Dias Maia]` | `[10%]` |
| `[Marcus Gabriel Oliveira da Silva]` | `[30%]` |

*A soma das porcentagens deve ser igual a 100%. Divergências de percepção sobre a participação devem ser discutidas em grupo antes do envio — o orientador pode solicitar esclarecimentos individuais em caso de disparidade relevante.*

---

## 5. Checklist Final da Etapa

**Fase 1 — Planejamento**
- [x] Pergunta de pesquisa de trabalho definida
- [x] Conceitos-chave e sinônimos (PT/EN) listados
- [x] Strings de busca elaboradas com operadores booleanos
- [x] Bases de dados escolhidas e justificadas
- [x] Critérios de inclusão e exclusão definidos

**Fase 2 — Execução e triagem**
- [x] Buscas executadas e resultados registrados por base/string
- [ ] Referências exportadas para o gerenciador de referências
- [x] Triagem por título/resumo concluída (com duplicatas removidas)
- [x] Triagem por texto completo (introdução/conclusão) concluída
- [x] Conjunto definitivo de artigos para fichamento compilado

**Documentação**
- [x] Contribuição individual de cada integrante registrada por passo
- [x] Quadro-resumo de participação preenchido (soma = 100%)

---


