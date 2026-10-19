# Etapa 6 Leitura e fichamento

## Solicitação

Preencha uma cópia deste template para cada artigo selecionado.

## Identificação do artigo

- Referência completa: `[Zhang, W.; Holtmann, J.; Strüber, D.; Hebig, R.; Steghöfer, J.-P. Supporting meta-model-based language evolution and rapid prototyping with automated grammar transformation. Journal of Systems and Software, v. 214, 112069, 2024]`
- DOI ou URL: `[https://doi.org/10.1016/j.jss.2024.112069]`
- Base de origem: `[Google Scholar / ScienceDirect]`
- Leitor responsável: `[Igor Nonaka Oliveira]`
- Data da leitura: `[20/08/2026]`

## Fichamento

### Problema investigado

`[O artigo investiga o problema de manter e modificar gramáticas de linguagens específicas de domínio (DSLs) durante a evolução da linguagem e durante processos de prototipação rápida. Os autores destacam que alterações manuais em gramáticas geradas automaticamente podem ser trabalhosas e sujeitas a erros.]`

### Objetivo do estudo

`[Os autores analisaram linguagens existentes para identificar padrões de transformação de gramáticas. A partir dessa análise, desenvolveram regras de transformação automatizadas e avaliaram o GrammarTransformer em situações relacionadas à evolução de linguagens e à prototipação rápida.]`

### Método utilizado

`[Os autores analisaram linguagens existentes para identificar padrões de transformação de gramáticas. A partir dessa análise, desenvolveram regras de transformação automatizadas e avaliaram o GrammarTransformer em situações relacionadas à evolução de linguagens e à prototipação rápida.]`

### Contexto, amostra ou dados

`[O estudo está inserido no contexto de engenharia dirigida por modelos (MDE) e desenvolvimento de DSLs textuais. Foram analisadas sete linguagens para estabelecer as regras de transformação utilizadas pelo GrammarTransformer. A avaliação considerou o esforço necessário para realizar as alterações nas gramáticas.]`

### Principais resultados

`[Os resultados indicam que o GrammarTransformer consegue automatizar parte das alterações necessárias nas gramáticas e reduzir significativamente o esforço manual durante a evolução das linguagens. A abordagem procura tornar a manutenção das gramáticas mais eficiente e menos sujeita a erros.]`

### Limitações apresentadas

`[Uma limitação é que a abordagem depende das regras de transformação definidas para os diferentes tipos de alterações nas gramáticas. Além disso, a avaliação foi realizada com um conjunto específico de linguagens, portanto os resultados podem não representar todos os tipos de DSL existentes]`

### Contribuição para o nosso artigo

`[Este estudo contribui diretamente para o projeto GameLang, pois apresenta uma abordagem relacionada à criação e evolução de DSLs e suas gramáticas. A GameLang também utiliza uma gramática para definir a estrutura da linguagem. O artigo ajuda a justificar a importância de manter a gramática organizada e de considerar mecanismos que facilitem sua evolução conforme novos comandos e recursos sejam adicionados à linguagem.

Também contribui para a discussão sobre eficiência do processamento e desenvolvimento de linguagens, embora seu foco principal seja a transformação e manutenção das gramáticas, e não a análise assintótica do parser.]`

### Comentário crítico

`[Uma das principais forças do artigo é apresentar uma solução prática para um problema comum no desenvolvimento de DSLs: a dificuldade de manter gramáticas durante a evolução da linguagem. A utilização de regras automatizadas pode diminuir o trabalho manual e a possibilidade de erros.

Como diferença em relação ao GameLang, o estudo está mais relacionado à evolução automatizada de gramáticas dentro de um contexto de engenharia dirigida por modelos, enquanto nosso projeto concentra-se na construção de uma DSL para representar a lógica de combates de RPG e no processamento dessa linguagem por um compilador.]`

### Citação literal opcional

> `[Manually changing automatically created grammars is tedious and error prone.]`

Página: `[1]`

## Identificação do artigo

- Referência completa: `[Zhang, W.; Strüber, D.; Hebig, R. Development and evolution of Xtext-based DSLs on GitHub: an empirical investigation. Empirical Software Engineering, v. 31, artigo 48, 2026.]`
- DOI ou URL: `[https://doi.org/10.1007/s10664-025-10775-2]`
- Base de origem: `[Google Scholar / Springer]`
- Leitor responsável: `[Igor Nonaka Oliveira]`
- Data da leitura: `[26/08/2026]`

## Fichamento

### Problema investigado

`[O artigo investiga a falta de conhecimento sistemático sobre como as linguagens específicas de domínio (DSLs) são desenvolvidas e evoluem ao longo do tempo. Os autores destacam que estudos anteriores geralmente analisavam poucos casos, dificultando a identificação de padrões gerais]`

### Objetivo do estudo

`[O objetivo é realizar uma investigação em larga escala sobre o desenvolvimento e a evolução de DSLs textuais criadas com o framework Xtext e hospedadas no GitHub. O estudo procura identificar características dos projetos, artefatos utilizados, formas de desenvolvimento e padrões de evolução das linguagens.]`

### Método utilizado

`[Os autores utilizaram uma metodologia de mineração de repositórios de software. Foram identificados e analisados 1.002 repositórios do GitHub relacionados ao Xtext. Depois de uma classificação manual, 226 repositórios foram identificados como contendo linguagens completamente desenvolvidas. Os autores analisaram gramáticas, metamodelos, instâncias de linguagens, cenários de desenvolvimento e alterações realizadas ao longo do tempo]`

### Contexto, amostra ou dados

`[O estudo está inserido no contexto de DSLs, engenharia dirigida por modelos (MDE) e desenvolvimento de software de código aberto.

A amostra inicial foi composta por 1.002 repositórios do GitHub. Desses, 226 foram classificados como projetos com linguagens completamente desenvolvidas. Além disso, foram encontradas definições de gramáticas em 722 repositórios. O estudo analisou projetos de diferentes domínios de aplicação.]`

### Principais resultados

`[Os autores observaram que:

o desenvolvimento orientado por gramáticas é a abordagem predominante entre os projetos analisados;

muitos projetos de DSL continuam evoluindo e recebendo alterações ao longo do tempo;

foram encontradas gramáticas em 722 dos repositórios analisados;

as DSLs de determinados domínios, como gerenciamento de dados e bancos de dados, apresentaram evolução mais rápida e maior tempo de manutenção;

alterações nas definições das gramáticas e nas instâncias de exemplo ocorreram com frequência;

também foi identificada a prática de adaptar linguagens existentes para o Xtext.]`

### Limitações apresentadas

`[Uma limitação importante é que o estudo está concentrado em DSLs desenvolvidas com Xtext e hospedadas no GitHub. Portanto, os resultados não necessariamente representam todas as DSLs existentes ou outras ferramentas de desenvolvimento de linguagens.

Além disso, o estudo analisa principalmente os artefatos relacionados ao desenvolvimento e evolução das linguagens, não sendo uma avaliação direta da velocidade de execução dos compiladores ou parsers.]`

### Contribuição para o nosso artigo

`[O estudo contribui para o projeto GameLang porque fornece evidências de como DSLs são desenvolvidas e mantidas na prática. Ele reforça a importância da gramática como parte central da definição de uma DSL e mostra que as linguagens podem evoluir com o acréscimo e alteração de regras.

Isso se relaciona diretamente à GameLang, pois nossa linguagem possui uma gramática que define comandos como criação de personagens, ataques, defesa, habilidades, turnos e movimentação. Conforme novos recursos forem adicionados, a gramática também poderá evoluir.

O artigo também ajuda a fundamentar a decisão de utilizar uma abordagem baseada em gramática para estruturar a GameLang.]`

### Comentário crítico

`[Uma das principais forças do artigo é o tamanho da investigação, pois foram analisados 1.002 repositórios, permitindo observar padrões que seriam difíceis de identificar em estudos pequenos.

Outra vantagem é a relação direta com DSLs e gramáticas. Como diferença em relação ao nosso projeto, o artigo analisa projetos existentes desenvolvidos com Xtext, enquanto a GameLang está sendo desenvolvida especificamente para representar a lógica de combates de RPG utilizando Python e uma gramática própria.

O artigo também não deve ser utilizado como referência específica para afirmar uma determinada complexidade assintótica ou velocidade do parser, pois esse não é o foco da pesquisa.]`

### Citação literal opcional

> `[grammar-driven development remains the dominant workflow]`

Página: `[seção 7 — Conclusion]`

## Identificação do artigo

- Referência completa: `[Lano, K.; Xue, Q.; Haughton, H. A Concrete Syntax Transformation Approach for Software Language Processing. SN Computer Science, v. 5, artigo 645, 2024.]`
- DOI ou URL: `[https://doi.org/10.1007/s42979-024-02979-y]`
- Base de origem: `[Google Scholar / Springer]`
- Leitor responsável: `[Igor Nonaka Oliveira]`
- Data da leitura: `[26/08/2026]`

## Fichamento

### Problema investigado

`[O artigo investiga dificuldades relacionadas ao processamento de linguagens de software, especialmente em tarefas como geração de código, engenharia reversa, refatoração e transformação de modelos. Os autores apontam que abordagens tradicionais baseadas em transformações modelo-para-modelo (M2M) ou modelo-para-texto (M2T) podem ser mais complexas para determinadas tarefas.]`

### Objetivo do estudo

`[O objetivo é apresentar uma abordagem baseada em transformações texto-para-texto (T2T) utilizando a sintaxe concreta das linguagens de origem e destino. A proposta busca tornar a especificação de transformações de linguagens mais simples e utilizável, inclusive em tarefas relacionadas ao desenvolvimento e suporte de DSLs.]`

### Método utilizado

`[Os autores desenvolveram uma abordagem chamada Concrete Grammar Transformation Language (CGTL), baseada em transformações definidas utilizando a sintaxe concreta das linguagens.

Para construir as gramáticas e os parsers, foi utilizado o ANTLR. A abordagem foi aplicada em diferentes tarefas de processamento de linguagens, incluindo definição e suporte de DSLs, abstração de software, transformação de modelos, engenharia reversa e tradução de programas.

A avaliação considerou a efetividade das soluções, o esforço necessário para desenvolvê-las e a eficiência computacional das transformações.]`

### Contexto, amostra ou dados

`[O trabalho está inserido no contexto de Engenharia Dirigida por Modelos (MDE), engenharia de linguagens e DSLs.

Foram utilizados diferentes casos de estudo para avaliar a abordagem. Entre eles estão a definição de três DSLs e suas ferramentas de suporte, transformações relacionadas à linguagem MathOCL, refatoração de código e tradução de programas.

Os experimentos de desempenho foram executados em um notebook com Windows 10, processador Intel i5-7440HQ de 2,80 GHz, 8 GB de RAM e alocação de 25% do processador. Os tempos foram calculados como a média de três execuções independentes.]`

### Principais resultados

`[Os autores observaram que:

a abordagem baseada em CGTL pode ser utilizada para diferentes tarefas de processamento de linguagens;

o uso da sintaxe concreta permite especificar transformações de forma mais direta;

a abordagem pode reutilizar gramáticas e parsers existentes, como os produzidos pelo ANTLR;

a técnica foi aplicada a tarefas envolvendo DSLs, refatoração, tradução de programas e transformação de modelos;

os experimentos indicaram que a abordagem pode ser eficiente computacionalmente;

os autores também relatam redução do esforço necessário para desenvolver e estender ferramentas de processamento de linguagens.]`

### Limitações apresentadas

`[Uma limitação importante é que a abordagem possui atualmente uma forte relação com o ANTLR, embora os autores indiquem que outras tecnologias de parsing, como JavaCC, poderiam ser utilizadas.

Além disso, no caso de transformações de modelos, os autores apontam que a abordagem pode gerar custos adicionais relacionados ao parsing e à montagem do modelo de destino.

Portanto, os resultados de desempenho apresentados não devem ser interpretados como uma medida geral da complexidade de qualquer parser ou linguagem, pois dependem da abordagem, das ferramentas e dos casos avaliados.]`

### Contribuição para o nosso artigo

`[O artigo contribui diretamente para o projeto GameLang porque apresenta uma abordagem baseada em gramáticas, parsing e processamento de linguagens, conceitos que fazem parte da construção do nosso compilador.

A utilização do ANTLR também é relevante porque demonstra na prática como uma gramática pode ser utilizada para construir parsers e realizar processamento de linguagens.

Para a GameLang, o artigo ajuda a fundamentar a relação entre a definição da linguagem por meio de uma gramática e as etapas posteriores de processamento. Além disso, a discussão sobre eficiência computacional é útil para o nosso trabalho quando formos analisar o custo do processamento da linguagem.

Entretanto, o artigo não define a complexidade assintótica do parser da GameLang. Essa complexidade deverá ser analisada de acordo com o parser e as técnicas efetivamente utilizadas no nosso projeto.]`

### Comentário crítico

`[Uma das principais vantagens do artigo é sua relação direta com engenharia de linguagens, DSLs, gramáticas e parsing. Além disso, diferente de alguns dos outros trabalhos selecionados, este artigo apresenta também uma avaliação envolvendo desempenho e esforço de desenvolvimento, o que é interessante para a discussão sobre eficiência no nosso projeto.

Como diferença, o artigo trabalha com transformações de linguagens utilizando CGTL e ANTLR, enquanto a GameLang está sendo desenvolvida como uma DSL própria para representar a lógica de combates de RPG.

Mesmo assim, os conceitos apresentados podem ser aproveitados para fundamentar a construção e o processamento da GameLang.]`

### Citação literal opcional

> `[To build grammars and parsers for software languages we use ANTLR.”]`

Página: `[Página: 2]`

## Identificação do artigo

- Referência completa: `[Frölich, D.; van Binsbergen, L. T. iCoLa+: An extensible meta-language with support for exploratory language development. Journal of Systems and Software, v. 211, artigo 111979, 2024.]`
- DOI ou URL: `[https://doi.org/10.1016/j.jss.2024.111979]`
- Base de origem: `[Google Scholar / ScienceDirect]`
- Leitor responsável: `[Igor Nonaka Oliveira]`
- Data da leitura: `[ 26/08/2026]`

## Fichamento

### Problema investigado

`[O artigo aborda a dificuldade e o esforço envolvidos no desenvolvimento de linguagens de programação e DSLs. Os autores destacam que criar uma linguagem envolve decisões de projeto, implementação da sintaxe e semântica, além da construção de ferramentas para seus usuários.

No caso das DSLs, o processo também é iterativo, pois a linguagem pode precisar ser modificada conforme as necessidades e experiências dos usuários.]`

### Objetivo do estudo

`[O objetivo é apresentar o iCoLa+, uma meta-linguagem extensível voltada ao desenvolvimento exploratório de linguagens.

A proposta busca facilitar o desenvolvimento de linguagens por meio da reutilização e composição de componentes de linguagem, permitindo criar, modificar e experimentar linguagens de maneira incremental.]`

### Método utilizado

`[Os autores desenvolveram o iCoLa+ utilizando Haskell e demonstraram seu funcionamento por meio da construção de diferentes linguagens.

Entre os exemplos utilizados estão as linguagens Imp, SIMPLE e MiniJava, construídas por meio da composição e restrição de fragmentos de linguagem.

Também foram desenvolvidas outras linguagens utilizando um conjunto fixo de operadores, permitindo avaliar diferentes formas de extensão e composição dentro do iCoLa+]`

### Contexto, amostra ou dados

`[O trabalho está inserido no contexto de engenharia de linguagens, DSLs, meta-linguagens, sintaxe e semântica.

A avaliação é realizada por meio de exemplos e construções de linguagens utilizando o iCoLa+. Os autores demonstram a construção de Imp, SIMPLE e MiniJava, além de outras linguagens criadas pela combinação e extensão de componentes.

O artigo também apresenta suporte a definições de domínio específicas de DSL e a diferentes domínios semânticos.]`

### Principais resultados

`[Os autores demonstraram que o iCoLa+ permite:

construir linguagens de maneira incremental e exploratória;

reutilizar componentes de linguagens existentes;

combinar e restringir fragmentos para formar novas linguagens;

estender linguagens existentes;

definir domínios específicos utilizando DSLs;

trabalhar com sintaxe e semântica dentro de uma mesma abordagem;

facilitar a prototipação e experimentação durante o desenvolvimento de linguagens.]`

### Limitações apresentadas

`[Uma limitação é que o trabalho está concentrado na abordagem e implementação do iCoLa+, utilizando Haskell e seus mecanismos de composição e programação incremental.

Além disso, os exemplos apresentados são voltados principalmente à demonstração da construção e extensão de linguagens. Portanto, o artigo não deve ser utilizado como uma referência específica para determinar a complexidade assintótica ou a velocidade do parser da GameLang.]`

### Contribuição para o nosso artigo

`[O artigo contribui para o projeto GameLang porque apresenta uma abordagem para facilitar o desenvolvimento e a evolução de linguagens específicas de domínio.

A ideia de construir linguagens de forma incremental é relacionada ao desenvolvimento da GameLang, pois nossa DSL também pode ser ampliada progressivamente, começando com comandos básicos e posteriormente incorporando recursos como habilidades, condições e turnos.

Além disso, o artigo reforça a importância de separar e organizar os elementos de uma linguagem, especialmente sua sintaxe e semântica, conceitos que também estão presentes no desenvolvimento do compilador da GameLang.

O trabalho também mostra que a reutilização e composição de componentes podem reduzir o esforço necessário para desenvolver novas linguagens.]`

### Comentário crítico

`[Uma das principais vantagens do artigo é sua relação direta com DSLs e desenvolvimento de linguagens, além de apresentar uma solução prática para facilitar a criação e evolução dessas linguagens.

Outro ponto interessante é o foco no desenvolvimento incremental, que possui relação com a forma como a GameLang está sendo construída em etapas.

Como diferença, o iCoLa+ utiliza uma abordagem própria baseada em uma meta-linguagem implementada em Haskell, enquanto a GameLang está sendo desenvolvida em Python e possui uma gramática específica para representar combates de RPG.

O artigo é, portanto, mais útil para fundamentar o desenvolvimento e a evolução da DSL do que para analisar diretamente o desempenho ou a complexidade do parsing.]`

### Citação literal opcional

> `[language development involves complex design and engineering processes]`

Página: `[Página: 1.]`

## Identificação do artigo

- Referência completa: `[Ballantyne, M.; Gamburg, M.; Hemann, J. Compiled, Extensible, Multi-language DSLs (Functional Pearl). Proceedings of the ACM on Programming Languages, v. 8, ICFP, 64–87, 2024.]`
- DOI ou URL: `[https://doi.org/10.1145/3674627]`
- Base de origem: `[Google Scholar / ACM]`
- Leitor responsável: `[Igor Nonaka Oliveira]`
- Data da leitura: `[26/08/2026]`

## Fichamento

### Problema investigado

`[O artigo investiga como implementar linguagens específicas de domínio (DSLs) de forma que elas possam oferecer, ao mesmo tempo, extensibilidade, integração com uma linguagem hospedeira e otimizações de compilação.

Os autores destacam que diferentes estratégias de implementação de DSLs apresentam vantagens distintas. Enquanto algumas facilitam a extensão da linguagem e sua interação com a linguagem hospedeira, outras permitem o uso de um compilador capaz de realizar otimizações.]`

### Objetivo do estudo

`[O objetivo é apresentar uma arquitetura para implementação de DSLs que combine três características:

possibilidade de extensão pelos usuários da DSL;

interação facilitada entre a DSL e a linguagem hospedeira;

utilização de um compilador capaz de realizar otimizações.

Para demonstrar a proposta, os autores apresentam uma nova implementação da DSL miniKanren, utilizando recursos da linguagem Racket.]`

### Método utilizado

`[Os autores desenvolveram uma implementação de miniKanren utilizando a syntax-spec metalanguage do Racket.

A arquitetura utiliza um macro expander, que transforma programas escritos na linguagem de superfície da DSL em uma linguagem central mais adequada para compilação. Essa linguagem central é integrada à linguagem hospedeira por meio de uma abordagem multilíngue.

A implementação foi utilizada para combinar extensibilidade com um compilador otimizador, permitindo comparar os benefícios dessa abordagem com estratégias anteriores de implementação de DSLs.]`

### Contexto, amostra ou dados

`[O trabalho está inserido no contexto de:

linguagens específicas de domínio;

compiladores;

metaprogramação;

linguagens funcionais;

programação lógica e por restrições.

A principal aplicação utilizada como estudo de caso é a miniKanren, uma DSL voltada à programação relacional. O trabalho demonstra como diferentes extensões e otimizações podem ser reunidas em uma única implementação.]`

### Principais resultados

`[Os autores demonstraram que a arquitetura proposta permite:

criar uma implementação de DSL extensível;

integrar a DSL com a linguagem hospedeira;

utilizar um compilador com otimizações;

combinar extensões da linguagem com técnicas de compilação;

manter uma interação mais natural entre a DSL e a linguagem hospedeira;

reunir em uma única implementação características que anteriormente apareciam separadas em diferentes abordagens.

Um resultado importante para nosso projeto é que o trabalho demonstra que DSLs compiladas podem ser projetadas considerando tanto extensibilidade quanto desempenho.]`

### Limitações apresentadas

`[O trabalho utiliza principalmente Racket, syntax-spec e miniKanren para demonstrar sua proposta. Dessa forma, os resultados estão relacionados a esse ambiente específico e não representam necessariamente o comportamento de qualquer DSL ou compilador.

Além disso, o artigo não tem como objetivo determinar a complexidade assintótica de parsers. Portanto, ele não deve ser utilizado para afirmar uma complexidade específica para o parser da GameLang.]`

### Contribuição para o nosso artigo

`[O artigo possui uma relação importante com o projeto GameLang, principalmente porque trata diretamente da implementação de DSLs compiladas.

A pesquisa ajuda a fundamentar a ideia de que uma DSL pode ser projetada para possuir uma linguagem própria e, posteriormente, ser processada por um compilador.

Também é relevante para a discussão sobre desempenho, pois os autores consideram explicitamente otimizações de compilação como uma das características desejáveis para implementações de DSLs.

No caso da GameLang, isso ajuda a justificar a preocupação com o processamento eficiente dos comandos da linguagem, embora a complexidade específica do nosso parser ainda precise ser determinada de acordo com a implementação utilizada.]`

### Comentário crítico

`[Uma das principais vantagens do artigo é sua relação direta com DSLs e compiladores, além de abordar explicitamente a questão do desempenho e das otimizações.

O trabalho também apresenta uma arquitetura concreta, em vez de apenas discutir conceitos teóricos.

Como diferença em relação à GameLang, o artigo trabalha com uma DSL de programação lógica chamada miniKanren, implementada no ecossistema Racket, enquanto a GameLang está sendo desenvolvida em Python para representar a lógica de combates de RPG.

Mesmo assim, os conceitos de DSL compilada, extensibilidade e otimização são relevantes para fundamentar nosso projeto.]`

### Citação literal opcional

> `[Implementations of domain-specific languages should offer both extensibility and performance optimizations.]`

Página: `[Página: 1.]`


## Identificação do artigo

- Referência completa: `[Faria, D.; Baptista, T. J.; Henriques, P. R. Upgrade of Lark Compiler Generator to Support Attribute Grammars. In: 13th Symposium on Languages, Applications and Technologies (SLATE 2024). Open Access Series in Informatics (OASIcs), v. 120, p. 7:1–7:16, 2024.]`
- DOI ou URL: `[https://doi.org/10.4230/OASIcs.SLATE.2024.7]`
- Base de origem: `[Google Scholar / OASIcs]`
- Leitor responsável: `[Igor Nonaka Oliveira]`
- Data da leitura: `[26/08/2026]`

## Fichamento

### Problema investigado

`[O artigo aborda a necessidade de ampliar ferramentas de análise sintática e processamento de linguagens para que elas também possam representar e processar informações semânticas.

Os autores observam que o Lark Compiler Generator possui recursos para análise sintática, mas não oferecia originalmente suporte completo para Gramáticas de Atributos (Attribute Grammars), utilizadas para especificar aspectos semânticos de linguagens.]`

### Objetivo do estudo

`[O objetivo é desenvolver o LarkAG, uma extensão do Lark Compiler Generator que adiciona suporte a Gramáticas de Atributos.

A proposta permite especificar de maneira formal aspectos da semântica estática e dinâmica de linguagens, complementando os recursos de análise sintática já existentes no Lark.]`

### Método utilizado

`[Os autores estudaram o funcionamento das Gramáticas de Atributos e analisaram exemplos de especificações baseadas nesse formalismo.

Em seguida, desenvolveram a arquitetura do LarkAG, composta por cinco componentes principais:

AG Parser;

Lark Parser Generator;

Interpreter Class Generator;

Lark Parser;

Custom Interpreter Class.

O AG Parser utiliza o Lark Parser Generator configurado com uma gramática específica da DSL do LarkAG. Depois do parsing, é produzido um Parse Tree, que é processado por um Transformer para extrair a GLC e as informações semânticas. Essas informações são utilizadas posteriormente para gerar dinamicamente uma classe responsável pela execução das regras semânticas.]`

### Contexto, amostra ou dados

`[O trabalho está inserido no contexto de:

gramáticas livres de contexto;

gramáticas de atributos;

análise sintática;

processamento de linguagens;

DSLs;

geração de compiladores.

A proposta foi implementada sobre o Lark Compiler Generator. O artigo apresenta a arquitetura, o desenvolvimento e exemplos de utilização do LarkAG, incluindo a DSL criada para representar ocorrências de atributos, regras semânticas e condições de contexto.]`

### Principais resultados

`[Os autores desenvolveram o LarkAG, permitindo que o Lark trabalhe também com Gramáticas de Atributos.

Entre os principais resultados estão:

extensão do Lark para suporte a Gramáticas de Atributos;

criação de uma DSL específica para representar regras semânticas;

geração de uma árvore de parsing a partir da entrada;

extração da GLC e das informações semânticas;

geração dinâmica de uma classe responsável pela execução das regras;

integração entre análise sintática e processamento semântico.

Segundo os autores, essa extensão permite utilizar o Lark na construção de compiladores e processadores de linguagens mais confiáveis.]`

### Limitações apresentadas

`[O próprio artigo destaca que a proposta não representa uma nova técnica fundamental de Gramáticas de Atributos. Os autores caracterizam o trabalho principalmente como uma extensão de uma ferramenta moderna, incorporando um formalismo já conhecido ao Lark.

Além disso, a solução está diretamente relacionada ao ecossistema do Lark e à arquitetura desenvolvida pelos autores. Portanto, seus resultados não devem ser utilizados para afirmar uma determinada complexidade ou desempenho para qualquer parser.]`

### Contribuição para o nosso artigo

`[O artigo possui uma contribuição muito direta para o projeto GameLang, principalmente por relacionar GLC, parsing, árvore sintática, DSL e processamento semântico.

Um ponto especialmente importante é que o artigo mostra uma sequência semelhante à que estamos utilizando no projeto: uma gramática define a estrutura da linguagem, o parser analisa a entrada e uma representação em árvore é produzida para que informações posteriores possam ser processadas.

Isso se relaciona com a GameLang, que utiliza uma gramática para definir comandos como criação de personagens, ataques, defesa, habilidades, turnos e movimentação, passando posteriormente para as etapas de parser e AST.

O artigo também pode ajudar futuramente na parte de análise semântica, caso a GameLang passe a verificar regras como existência de personagens, valores válidos de atributos ou condições de combate.]`

### Comentário crítico

`[Uma das principais vantagens do artigo é a proximidade com as etapas técnicas do projeto GameLang. Ele apresenta de forma prática a relação entre gramática, parser, árvore sintática e semântica.

Outro ponto positivo é a utilização do Lark, que é uma ferramenta moderna de processamento de linguagens e possui relação com Python, linguagem utilizada na implementação da GameLang.

Como diferença, o LarkAG utiliza Gramáticas de Atributos e gera componentes para processamento semântico, enquanto o projeto GameLang está inicialmente concentrado na construção do lexer, parser e AST.

Portanto, o artigo é especialmente útil para fundamentar a evolução futura do projeto, mas não deve ser utilizado para afirmar que a GameLang possui as mesmas características do LarkAG.]`

### Citação literal opcional

> `[The CFG is obtained in string format, representing the structural elements of the grammar.]`

Página: `[Página: 7:7]`

## Checklist

- [x] O artigo foi lido além do resumo.
- [x] O método e os resultados foram identificados.
- [x] As limitações foram registradas.
- [x] A conexão com o tema foi explicada.
- [x] Toda citação literal contém página.
