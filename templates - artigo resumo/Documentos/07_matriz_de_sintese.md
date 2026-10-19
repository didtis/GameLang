# Etapa 7 Matriz de síntese e organização da revisão

## Solicitação

Compare os artigos e organize a revisão por temas ou eixos. Não produza apenas uma sequência de resumos.

## Eixos da revisão

1. `[Desenvolvimento, evolução e manutenção de DSLs e suas gramáticas]`
2. `[Gramáticas, parsing e processamento de linguagens]`
3. `[Compilação, extensibilidade e eficiência no processamento de DSLs]`

## Matriz de síntese

| Eixo | Artigos relacionados | Convergências | Divergências | Limitações | Lacunas |
|---|---|---|---|---|---|
| `[Desenvolvimento, evolução e manutenção de DSLs e suas gramáticas]` | `[Zhang et al. (2024); Zhang, Strüber e Hebig (2026); Frölich e van Binsbergen (2024)]` | `[Os três trabalhos tratam do desenvolvimento ou evolução de linguagens e destacam a importância de facilitar a criação, manutenção e extensão de DSLs.]` | `[Zhang et al. (2024) focam na transformação automatizada de gramáticas; Zhang et al. (2026) analisam empiricamente projetos Xtext no GitHub; Frölich e van Binsbergen (2024) propõem uma meta-linguagem para desenvolvimento exploratório e incremental.]` | `[Os estudos utilizam ferramentas e contextos específicos, como GrammarTransformer, Xtext e iCoLa+, não representando necessariamente todas as formas de desenvolvimento de DSLs.]` | `[Os trabalhos não tratam especificamente da criação de uma DSL voltada à lógica de combates de RPG nem apresentam uma análise conjunta entre evolução da gramática e processamento de uma DSL desse domínio.]` |
| `[Gramáticas, parsing e processamento de linguagens]` | `[Lano, Xue e Haughton (2024); Faria, Baptista e Henriques (2024); Zhang et al. (2024)]` | `[Os estudos mostram a importância das gramáticas no processamento de linguagens e relacionam gramáticas, parsers e ferramentas de desenvolvimento de linguagens.]` | `[Lano et al. (2024) trabalham com transformação de sintaxe concreta e ANTLR; Faria et al. (2024) ampliam o Lark para Gramáticas de Atributos; Zhang et al. (2024) concentram-se na transformação e evolução de gramáticas.]` | `[As ferramentas e abordagens são específicas e possuem características próprias, portanto não permitem afirmar diretamente qual técnica ou parser é melhor para qualquer DSL.]` | `[Falta uma avaliação específica do processamento sintático de uma DSL de combate de RPG, incluindo a relação entre a gramática utilizada, o parser, a AST e a complexidade do processamento.]` |
| `[Compilação, extensibilidade e eficiência no processamento de DSLs]` | `[Ballantyne, Gamburg e Hemann (2024); Lano, Xue e Haughton (2024); Faria, Baptista e Henriques (2024)]` | `[Os trabalhos relacionam DSLs com processamento, compilação, ferramentas de linguagem e, em diferentes níveis, aspectos de eficiência e extensão.]` | `[Ballantyne et al. (2024) enfatizam DSLs compiladas, extensibilidade e otimizações; Lano et al. (2024) avaliam transformações de linguagens e eficiência; Faria et al. (2024) concentram-se na extensão do Lark para Gramáticas de Atributos.]` | `[Os estudos não possuem o mesmo objetivo e utilizam ambientes e ferramentas diferentes. Nenhum deles fornece diretamente a complexidade assintótica do parser utilizado na GameLang.]` | `[Existe uma lacuna na análise da complexidade do processamento de uma DSL própria para lógica de combate, considerando as etapas de análise sintática e construção da AST.]` |

## Roteiro da revisão da literatura

### Eixo 1

- Ideia principal: `[O desenvolvimento de DSLs envolve não apenas a definição inicial da linguagem, mas também sua manutenção, evolução e extensão. Os trabalhos analisados mostram diferentes estratégias para tornar esse processo mais organizado e eficiente.]`
- Evidências que serão usadas: `[Zhang et al. (2024) apresentam o GrammarTransformer para automatizar transformações de gramáticas e reduzir o esforço manual. Zhang, Strüber e Hebig (2026) analisam 1.002 repositórios Xtext no GitHub e identificam o desenvolvimento orientado por gramáticas como uma abordagem predominante. Frölich e van Binsbergen (2024) apresentam o iCoLa+ como uma abordagem para desenvolvimento exploratório e incremental de linguagens.]`
- Comparação entre estudos: `[Os trabalhos convergem ao reconhecer que DSLs precisam ser projetadas de maneira que possam evoluir. Entretanto, utilizam estratégias diferentes: transformação automatizada de gramáticas, investigação empírica de projetos existentes e composição incremental de componentes de linguagem.]`
- Ligação com o problema: `[Esses estudos ajudam a fundamentar a construção da GameLang como uma DSL que pode começar com comandos básicos e posteriormente incorporar novos recursos, como habilidades, condições e turnos, exigindo alterações e evolução da gramática.]`

### Eixo 2

- Ideia principal: `[As gramáticas são utilizadas para definir a estrutura das linguagens e servem de base para ferramentas de análise e processamento. O parsing transforma a entrada da linguagem em uma representação que pode ser posteriormente processada.]`
- Evidências que serão usadas: `[Lano, Xue e Haughton (2024) apresentam uma abordagem de transformação de sintaxe concreta utilizando gramáticas e parsers, com uso do ANTLR. Faria, Baptista e Henriques (2024) apresentam o LarkAG, estendendo o Lark para trabalhar com Gramáticas de Atributos e integrando análise sintática e processamento semântico.]`
- Comparação entre estudos: `[Os dois trabalhos possuem relação direta com o processamento de linguagens, mas possuem objetivos diferentes. Lano et al. concentram-se em transformações de linguagens utilizando sintaxe concreta, enquanto Faria et al. ampliam uma ferramenta de parsing para incorporar informações semânticas.]`
- Ligação com o problema: `[Esses trabalhos fundamentam as etapas técnicas da GameLang, especialmente a utilização de uma gramática para definir a linguagem, a análise sintática realizada pelo parser e a construção de uma representação em árvore que poderá ser utilizada nas etapas posteriores do compilador.]`

### Eixo 3

- Ideia principal: `[A implementação de uma DSL pode considerar não apenas sua definição sintática, mas também sua compilação, extensibilidade e eficiência de processamento.]`
- Evidências que serão usadas: `[Ballantyne, Gamburg e Hemann (2024) discutem DSLs compiladas, extensibilidade e otimizações de desempenho. Lano et al. (2024) apresentam avaliações envolvendo eficiência das transformações. Faria et al. (2024) demonstram a extensão de uma ferramenta de processamento de linguagens para integrar informações sintáticas e semânticas.]`
- Comparação entre estudos: `[Ballantyne et al. concentram-se principalmente na combinação entre extensibilidade e otimizações de compilação. Lano et al. avaliam uma abordagem de transformação de linguagens, incluindo aspectos de eficiência. Faria et al. concentram-se principalmente na extensão das capacidades de processamento do Lark]`
- Ligação com o problema: `[Esses estudos ajudam a justificar que o desenvolvimento da GameLang não deve considerar apenas a criação da sintaxe, mas também as etapas de processamento realizadas pelo compilador e a possibilidade de evolução futura da linguagem.]`

## Síntese crítica provisória

`[Os artigos analisados apresentam uma tendência de tratar DSLs como linguagens que precisam ser estruturadas de forma organizada, extensível e passível de evolução. Os estudos de Zhang et al. (2024), Zhang, Strüber e Hebig (2026) e Frölich e van Binsbergen (2024) concentram-se principalmente no desenvolvimento, manutenção e evolução das linguagens e de suas gramáticas. Já Lano, Xue e Haughton (2024) e Faria, Baptista e Henriques (2024) apresentam abordagens mais diretamente relacionadas ao processamento de linguagens, envolvendo gramáticas, parsing, transformações e informações semânticas. Ballantyne, Gamburg e Hemann (2024), por sua vez, destacam a combinação entre DSLs compiladas, extensibilidade e otimizações. Apesar dessas contribuições, os trabalhos analisados não tratam especificamente da construção de uma DSL para representar lógica de combates de RPG nem apresentam uma análise específica da complexidade do parser e da construção da AST para esse domínio. Dessa forma, a GameLang pode contribuir ao aplicar esses conceitos em um domínio específico e analisar o processamento de sua própria linguagem.]`

## Checklist

- [x] Os artigos foram agrupados por ideias.
- [x] Há comparações entre estudos.
- [x] As divergências foram registradas.
- [x] As lacunas são específicas e sustentadas pelas leituras.
