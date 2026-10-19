# Etapa 8 Redação do artigo

## Solicitação

Escreva a primeira versão completa do artigo seguindo a estrutura abaixo.

# Título

`[Desenvolvimento de uma DSL para representação da lógica de combates de RPG: uma revisão sobre gramáticas, parsing e compilação]`

## Palavras-chave

`[DSL; Gramática Livre de Contexto; ]; [Parsing]; [Compiladores; Linguagens Específicas de Domínio.]`

## Introdução

`[As Linguagens Específicas de Domínio (Domain-Specific Languages — DSLs) são linguagens desenvolvidas para representar conceitos e operações de um determinado domínio de aplicação. Diferentemente das linguagens de propósito geral, uma DSL pode utilizar uma sintaxe e um conjunto de construções mais próximos dos conceitos específicos do domínio para o qual foi projetada. O desenvolvimento de uma DSL envolve, entre outros aspectos, a definição de sua sintaxe, gramática, mecanismos de análise e formas de processamento.

Nesse contexto, as gramáticas possuem papel importante na definição da estrutura de uma linguagem. A utilização de uma Gramática Livre de Contexto (GLC) permite especificar formalmente como os elementos da linguagem podem ser combinados. A partir dessa definição, ferramentas de processamento de linguagens podem realizar a análise sintática da entrada e produzir representações que serão utilizadas nas etapas posteriores do processamento.

Além da definição inicial, uma DSL precisa considerar sua evolução. Novos comandos e recursos podem exigir alterações na gramática e nas ferramentas responsáveis pelo processamento da linguagem. Zhang et al. (2024) apresentam uma abordagem para automatizar transformações de gramáticas durante a evolução de linguagens, enquanto Zhang, Strüber e Hebig (2026) investigam empiricamente como DSLs desenvolvidas com Xtext evoluem em projetos hospedados no GitHub. Frölich e van Binsbergen (2024), por sua vez, apresentam uma abordagem voltada ao desenvolvimento exploratório e incremental de linguagens.

Outros estudos concentram-se no processamento dessas linguagens. Lano, Xue e Haughton (2024) apresentam uma abordagem de transformação de sintaxe concreta utilizando gramáticas e parsers, enquanto Faria, Baptista e Henriques (2024) ampliam o Lark Compiler Generator para oferecer suporte a Gramáticas de Atributos. Ballantyne, Gamburg e Hemann (2024) discutem ainda a implementação de DSLs compiladas considerando extensibilidade e otimizações de desempenho.

Apesar dessas contribuições, os trabalhos analisados não tratam especificamente da construção de uma DSL voltada à representação da lógica de combates de RPG nem apresentam uma análise específica da complexidade do processamento sintático e da construção da AST para esse domínio.

Dessa forma, o objetivo deste trabalho é analisar, por meio de uma revisão da literatura, abordagens relacionadas ao desenvolvimento e evolução de DSLs, ao uso de gramáticas, parsing e processamento de linguagens, e à compilação e eficiência de DSLs, relacionando esses conceitos ao desenvolvimento da GameLang, uma DSL destinada à representação da lógica de combates de RPG.]`

## Metodologia

`[Este trabalho foi desenvolvido como uma revisão da literatura com abordagem de busca, seleção, leitura e síntese comparativa de estudos relacionados ao desenvolvimento de DSLs, gramáticas, parsing e compiladores.

A questão de pesquisa definida foi: Como uma linguagem específica de domínio (DSL) baseada em uma Gramática Livre de Contexto (GLC) pode representar a lógica de combates de RPG e ser processada por um compilador, considerando as etapas de análise sintática, construção da AST e complexidade do parsing?

Foram definidos como principais conceitos de busca: DSL, Compiler, Context-Free Grammar (CFG), Syntax Analysis, AST, Complexity e Games/RPG. As buscas foram realizadas nas bases IEEE Xplore, Portal de Periódicos CAPES e Google Scholar.

Foram utilizadas três estratégias principais de busca:

("Domain-Specific Language" OR DSL) AND ("Context-Free Grammar" OR CFG) AND (parser OR parsing);

("Domain-Specific Language" OR DSL) AND (compiler OR compilation) AND (parsing OR parser);

("Domain-Specific Language" OR DSL) AND (games OR "role-playing game" OR RPG) AND (grammar OR parsing).

As buscas foram realizadas entre agosto de 2026 e tiveram como objetivo identificar trabalhos relacionados ao desenvolvimento de DSLs, gramáticas, parsing, compiladores e processamento de linguagens. Os registros obtidos nas bases resultaram em aproximadamente 24.175 resultados brutos considerando as diferentes buscas. Após a triagem inicial, foram considerados os critérios de pertinência ao tema, relação com DSLs, gramáticas, parsing, compilação ou processamento de linguagens e disponibilidade de informações suficientes para leitura e análise.

Após as etapas de triagem e leitura, foram selecionados seis artigos publicados entre 2024 e 2026. Os trabalhos foram analisados considerando problema investigado, objetivo, método, contexto, resultados, limitações e contribuição para o projeto GameLang.

A análise dos artigos foi organizada por eixos temáticos, buscando identificar convergências, divergências, limitações e lacunas. Dessa forma, a revisão não foi estruturada apenas como uma sequência de resumos individuais, mas como uma comparação entre diferentes abordagens relacionadas ao desenvolvimento e processamento de DSLs.]`

## Revisão da literatura

### `[Eixo 1]`

`[O desenvolvimento de uma DSL não se limita à definição inicial de sua sintaxe. A linguagem pode sofrer alterações conforme novos requisitos são identificados, tornando necessário modificar suas gramáticas e ferramentas de processamento. Nesse sentido, Zhang et al. (2024) investigam a dificuldade de manter e modificar gramáticas durante a evolução de linguagens e apresentam o GrammarTransformer, uma abordagem baseada em regras de transformação automatizadas. Os autores analisaram sete linguagens para identificar padrões de transformação e avaliaram a redução do esforço manual proporcionada pela abordagem.

A preocupação com a evolução das DSLs também aparece no estudo de Zhang, Strüber e Hebig (2026). Diferentemente de Zhang et al. (2024), que apresentam uma solução para transformação de gramáticas, esse trabalho realiza uma investigação empírica em larga escala. Foram analisados 1.002 repositórios relacionados ao Xtext no GitHub, dos quais 226 foram classificados como contendo linguagens completamente desenvolvidas. O estudo identificou definições de gramáticas em 722 repositórios e observou que o desenvolvimento orientado por gramáticas permanece como uma abordagem predominante.

Frölich e van Binsbergen (2024) apresentam uma perspectiva diferente, concentrando-se no desenvolvimento exploratório e incremental de linguagens. O iCoLa+ permite reutilizar, combinar e estender componentes de linguagens, utilizando uma abordagem que facilita experimentações durante o desenvolvimento. Os autores demonstram a abordagem por meio de linguagens como Imp, SIMPLE e MiniJava.

Os três estudos convergem ao considerar que o desenvolvimento de linguagens precisa levar em conta sua evolução e extensão. Entretanto, apresentam estratégias diferentes. Zhang et al. (2024) priorizam a automação das transformações de gramáticas; Zhang, Strüber e Hebig (2026) investigam empiricamente como projetos existentes evoluem; e Frölich e van Binsbergen (2024) concentram-se na composição e no desenvolvimento incremental de linguagens.

Essas contribuições são relevantes para a GameLang porque a linguagem também pode evoluir ao longo de seu desenvolvimento. A versão inicial possui comandos relacionados à criação de personagens, ataques, defesa, habilidades, turnos e movimentação, podendo posteriormente receber novos recursos. Assim, as alterações realizadas na linguagem poderão exigir modificações correspondentes em sua gramática e nas etapas de processamento.

Apesar das contribuições desses trabalhos, seus contextos são diferentes do domínio da GameLang. Nenhum dos estudos analisados trata especificamente de uma DSL voltada à lógica de combates de RPG. Além disso, os trabalhos utilizam ferramentas e ambientes específicos, como GrammarTransformer, Xtext e iCoLa+, o que limita a generalização direta de seus resultados para qualquer DSL.]`

### `[Eixo 2]`

`[A definição formal da estrutura de uma linguagem constitui uma etapa fundamental para seu processamento. Gramáticas podem especificar quais construções são válidas e servir como base para ferramentas responsáveis pela análise sintática.

Lano, Xue e Haughton (2024) apresentam uma abordagem denominada Concrete Grammar Transformation Language (CGTL), voltada à transformação de linguagens utilizando sua sintaxe concreta. Os autores utilizam gramáticas e parsers para desenvolver diferentes tarefas de processamento de linguagens e utilizam o ANTLR na construção dessas ferramentas. A abordagem foi aplicada em tarefas envolvendo DSLs, abstração de software, transformação de modelos, engenharia reversa, refatoração e tradução de programas.

Uma característica relevante desse trabalho é a tentativa de utilizar diretamente a sintaxe concreta das linguagens para especificar transformações. Os autores também apresentam avaliações envolvendo esforço de desenvolvimento e eficiência das transformações. Entretanto, os resultados estão relacionados à abordagem CGTL e às ferramentas utilizadas, não permitindo estabelecer diretamente uma complexidade geral para qualquer parser.

Faria, Baptista e Henriques (2024) apresentam outra abordagem relacionada ao processamento de linguagens por meio do LarkAG. O trabalho amplia o Lark Compiler Generator para oferecer suporte a Gramáticas de Atributos. A arquitetura apresentada relaciona uma gramática com informações semânticas e utiliza uma árvore de parsing como parte do processo de geração dos componentes responsáveis pelo processamento das regras semânticas.

Enquanto Lano, Xue e Haughton (2024) concentram-se principalmente em transformações de linguagens utilizando sintaxe concreta, Faria, Baptista e Henriques (2024) ampliam as capacidades de uma ferramenta de parsing para incorporar informações semânticas. Dessa maneira, os dois estudos apresentam abordagens diferentes, mas convergem ao demonstrar a importância de gramáticas e mecanismos de parsing no desenvolvimento de ferramentas de processamento de linguagens.

A relação com a GameLang ocorre principalmente nas etapas de definição da gramática, análise sintática e construção de uma representação em árvore. A GameLang utiliza uma gramática para definir a estrutura de comandos da linguagem e posteriormente realiza o processamento desses comandos. A construção da AST constitui uma etapa importante para que a estrutura sintática identificada pelo parser possa ser utilizada nas etapas posteriores do compilador.

Entretanto, nenhum dos trabalhos analisados apresenta especificamente o processamento de uma DSL para lógica de combates de RPG. Também não é possível utilizar diretamente os resultados desses estudos para afirmar a complexidade assintótica do parser da GameLang, uma vez que essa característica depende da implementação e da técnica de parsing utilizada.]`

### `[Eixo 3]`

`[Além da definição da sintaxe e do parsing, a implementação de uma DSL pode considerar aspectos relacionados à compilação, extensibilidade e eficiência. Ballantyne, Gamburg e Hemann (2024) discutem justamente a implementação de DSLs compiladas que procuram combinar extensibilidade, integração com uma linguagem hospedeira e otimizações de compilação.

Como estudo de caso, os autores apresentam uma implementação da DSL miniKanren utilizando recursos do Racket. A arquitetura utiliza mecanismos de expansão e uma linguagem central para possibilitar a integração entre a DSL e a linguagem hospedeira, além de permitir otimizações realizadas pelo compilador. Dessa forma, o trabalho demonstra que extensibilidade e desempenho podem ser considerados conjuntamente na implementação de uma DSL.

Lano, Xue e Haughton (2024) também apresentam resultados relacionados à eficiência, porém em um contexto diferente. Seu trabalho avalia o desempenho de transformações de linguagens e o esforço necessário para desenvolvê-las. Já Faria, Baptista e Henriques (2024) concentram-se principalmente na extensão do Lark para Gramáticas de Atributos e na integração entre informações sintáticas e semânticas.

Os três trabalhos, portanto, possuem objetivos diferentes. Ballantyne et al. (2024) enfatizam DSLs compiladas, extensibilidade e otimizações; Lano et al. (2024) investigam transformações de linguagens e aspectos de eficiência; e Faria et al. (2024) concentram-se na ampliação das capacidades de uma ferramenta de processamento de linguagens.

Para a GameLang, esses estudos ajudam a demonstrar que o desenvolvimento de uma DSL não deve considerar somente a criação de comandos e sua gramática. Também é necessário compreender como esses comandos serão processados e como a linguagem poderá ser estendida futuramente. No entanto, os estudos não fornecem diretamente a complexidade assintótica do parser da GameLang, sendo necessária uma análise específica da implementação utilizada no projeto.]`


### Síntese crítica

`[Os seis artigos analisados apresentam uma tendência comum de tratar DSLs como linguagens que precisam ser estruturadas, processadas e, em diferentes situações, evoluídas ao longo do tempo. Os trabalhos de Zhang et al. (2024), Zhang, Strüber e Hebig (2026) e Frölich e van Binsbergen (2024) concentram-se principalmente no desenvolvimento, manutenção e evolução das linguagens e de suas gramáticas. Já Lano, Xue e Haughton (2024) e Faria, Baptista e Henriques (2024) apresentam abordagens mais diretamente relacionadas ao processamento de linguagens, envolvendo gramáticas, parsing, transformações e informações semânticas. Ballantyne, Gamburg e Hemann (2024), por sua vez, destacam a implementação de DSLs compiladas considerando extensibilidade e otimizações.

Existe, portanto, convergência quanto à importância das gramáticas, das ferramentas de processamento e da possibilidade de evolução das linguagens. Entretanto, os trabalhos diferem quanto aos objetivos e às ferramentas utilizadas. Também não foi identificado, entre os artigos selecionados, um estudo que reúna especificamente uma DSL para representar lógica de combates de RPG, sua gramática, seu parser, sua representação em AST e uma análise específica da complexidade do processamento.

Essa lacuna permite relacionar os conhecimentos encontrados na literatura ao desenvolvimento da GameLang. O projeto pode aplicar os conceitos identificados nos estudos a um domínio específico, investigando como uma linguagem própria para lógica de combate pode ser definida por meio de uma GLC e posteriormente processada por um compilador.]`

## Considerações finais

`[A revisão realizada indica que o desenvolvimento de DSLs envolve diferentes etapas e preocupações, desde a definição da gramática até o processamento, compilação, evolução e manutenção da linguagem. Os estudos analisados demonstram diferentes estratégias para lidar com esses aspectos, incluindo transformação automatizada de gramáticas, investigação empírica da evolução de DSLs, desenvolvimento incremental, transformação de linguagens, extensão de ferramentas de parsing e implementação de DSLs compiladas.

Em relação ao problema de pesquisa, os estudos indicam que uma DSL pode utilizar uma gramática formal para definir sua estrutura e posteriormente ser processada por ferramentas de análise sintática e compilação. A utilização de uma GLC fornece uma forma de representar as construções válidas da linguagem, enquanto o parser pode utilizar essa definição para analisar os comandos e produzir uma representação em árvore utilizada nas etapas seguintes.

Para a GameLang, esses resultados fornecem fundamentação para a utilização de uma gramática na representação da lógica de combates de RPG e para a organização das etapas de lexer, parser e AST. Os estudos também reforçam a importância de considerar a evolução da linguagem, uma vez que novos comandos e regras de combate podem exigir alterações na gramática e no processamento.

Como limitação desta revisão, os artigos selecionados apresentam ferramentas, linguagens e contextos diferentes do projeto GameLang. Além disso, os estudos não permitem determinar diretamente a complexidade assintótica do parser utilizado no projeto. Essa análise deverá ser realizada posteriormente considerando a implementação efetivamente utilizada na GameLang, suas estruturas de dados e seu algoritmo de parsing.

Como continuidade, o projeto pode investigar experimentalmente o processamento da GameLang, incluindo a análise sintática, a construção da AST e a complexidade associada ao parsing. Também poderá ser avaliada a evolução da gramática conforme novos recursos, como habilidades, condições e turnos, forem incorporados à linguagem.]`

## Resumo

`[As Linguagens Específicas de Domínio (DSLs) são utilizadas para representar conceitos e operações de domínios específicos por meio de linguagens próprias. Este trabalho tem como objetivo analisar abordagens relacionadas ao desenvolvimento e evolução de DSLs, ao uso de Gramáticas Livres de Contexto (GLCs), parsing, construção de representações em árvore e compilação, relacionando esses conceitos ao desenvolvimento da GameLang, uma DSL voltada à representação da lógica de combates de RPG. Foi realizada uma revisão da literatura utilizando IEEE Xplore, Portal de Periódicos CAPES e Google Scholar, com estratégias de busca relacionadas a DSLs, gramáticas, compiladores, parsing e jogos. Após as etapas de busca, triagem e leitura, foram selecionados seis artigos publicados entre 2024 e 2026. Os estudos foram organizados em três eixos: desenvolvimento e evolução de DSLs e suas gramáticas; gramáticas, parsing e processamento de linguagens; e compilação, extensibilidade e eficiência. Os resultados indicam a importância das gramáticas no desenvolvimento e processamento de DSLs, além da necessidade de considerar sua evolução, extensibilidade e ferramentas de processamento. Entretanto, não foram identificados estudos que tratassem especificamente de uma DSL para lógica de combates de RPG associada à análise de parsing, AST e complexidade. Conclui-se que a GameLang pode aplicar esses conceitos em um domínio específico, sendo necessária uma investigação posterior da complexidade de seu processamento de acordo com a implementação adotada.]`

## Referências

`[BALLANTYNE, M.; GAMBURG, M.; HEMANN, J. Compiled, Extensible, Multi-language DSLs (Functional Pearl). Proceedings of the ACM on Programming Languages, v. 8, ICFP, p. 64–87, 2024. DOI: 10.1145/3674627.

FARIA, D.; BAPTISTA, T. J.; HENRIQUES, P. R. Upgrade of Lark Compiler Generator to Support Attribute Grammars. In: 13th Symposium on Languages, Applications and Technologies (SLATE 2024). Open Access Series in Informatics (OASIcs), v. 120, p. 7:1–7:16, 2024. DOI: 10.4230/OASIcs.SLATE.2024.7.

FRÖLICH, D.; VAN BINSBERGEN, L. T. iCoLa+: An extensible meta-language with support for exploratory language development. Journal of Systems and Software, v. 211, 111979, 2024. DOI: 10.1016/j.jss.2024.111979.

LANO, K.; XUE, Q.; HAUGHTON, H. A Concrete Syntax Transformation Approach for Software Language Processing. SN Computer Science, v. 5, artigo 645, 2024. DOI: 10.1007/s42979-024-02979-y.

ZHANG, W.; HOLTMANN, J.; STRÜBER, D.; HEBIG, R.; STEGHÖFER, J.-P. Supporting meta-model-based language evolution and rapid prototyping with automated grammar transformation. Journal of Systems and Software, v. 214, 112069, 2024. DOI: 10.1016/j.jss.2024.112069.

ZHANG, W.; STRÜBER, D.; HEBIG, R. Development and evolution of Xtext-based DSLs on GitHub: an empirical investigation. Empirical Software Engineering, v. 31, artigo 48, 2026. DOI: 10.1007/s10664-025-10775-2.]`

## Checklist

- [x] A introdução termina com o objetivo.
- [x] A metodologia descreve o processo realmente realizado.
- [x] A revisão compara os artigos.
- [x] A conclusão responde ao problema.
- [x] O resumo representa o texto completo.
