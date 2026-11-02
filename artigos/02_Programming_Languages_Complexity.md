# Determining Programming Languages Complexity and Its Impact on Processing

## 1. Referência bibliográfica

PINTO, Gonçalo Rodrigues; HENRIQUES, Pedro Rangel; DA CRUZ, Daniela; CRUZ, João. **Determining Programming Languages Complexity and Its Impact on Processing**. In: *11th Symposium on Languages, Applications and Technologies (SLATE 2022)*. Open Access Series in Informatics (OASIcs), v. 104, p. 16:1–16:15, 2022. DOI: 10.4230/OASIcs.SLATE.2022.16.

## 2. Área de estudo

* Linguagens de programação
* Complexidade de linguagens
* Processamento de linguagens
* Gramáticas
* DSLs
* Análise de propriedades de linguagens

## 3. Resumo

O artigo investiga a complexidade de linguagens de programação e o impacto dessa complexidade no processamento realizado por ferramentas de análise.

Os autores destacam que ferramentas de processamento de linguagens, como analisadores estáticos, precisam ser adaptadas quando passam a trabalhar com uma nova linguagem de programação.

Para auxiliar nesse processo, o trabalho apresenta uma abordagem para descrever propriedades das linguagens e utilizar essas informações para estimar a complexidade da nova linguagem em comparação com linguagens que já são suportadas.

O artigo também apresenta uma DSL chamada **Properties Language**, utilizada para descrever propriedades de linguagens de programação.

## 4. Objetivo do artigo

O objetivo é estudar como determinar a complexidade de uma linguagem de programação e como essa complexidade pode afetar o esforço necessário para desenvolver ou adaptar ferramentas de processamento.

A ideia é permitir que características de uma linguagem sejam analisadas antes de implementar completamente uma ferramenta para processá-la.

## 5. Problema abordado

Uma ferramenta desenvolvida para uma determinada linguagem pode não funcionar diretamente para outra linguagem.

Quando uma nova linguagem é adicionada, pode ser necessário modificar analisadores, ferramentas de análise estática ou outros componentes.

O trabalho busca fornecer informações que permitam estimar o esforço necessário para lidar com uma nova linguagem.

## 6. Metodologia

O trabalho utiliza uma abordagem baseada na descrição das propriedades das linguagens.

Entre os elementos apresentados está uma DSL denominada **Properties Language**, utilizada para representar propriedades de uma linguagem de programação.

A partir dessas propriedades, torna-se possível analisar características da linguagem e relacioná-las à complexidade do seu processamento.

## 7. Relação entre linguagem e processamento

Uma das ideias centrais do trabalho é que linguagens diferentes podem apresentar diferentes níveis de complexidade.

Consequentemente, ferramentas que processam essas linguagens podem apresentar diferentes níveis de dificuldade de implementação e manutenção.

Essa ideia é importante para a GameLang porque o projeto também pretende analisar a complexidade da linguagem criada.

## 8. Relação com GLC e AST

A GameLang será definida por uma gramática que especificará quais comandos são válidos.

Depois que o parser reconhecer esses comandos, eles poderão ser representados em uma estrutura como uma Árvore Sintática Abstrata (AST).

De forma simplificada:

```text
Código GameLang
      ↓
Tokens
      ↓
Parser
      ↓
Regras da gramática
      ↓
AST
```

A complexidade da gramática e do parser pode influenciar o esforço necessário para realizar essas etapas.

## 9. Relação com a GameLang

Este é um dos artigos mais diretamente relacionados à parte de complexidade do projeto.

A GameLang possui como objetivo representar uma linguagem específica para lógica de combates de RPG.

Assim, além de definir os comandos, o projeto pode analisar características da linguagem e discutir como elas influenciam o processamento.

Por exemplo, a quantidade e a organização das regras gramaticais podem ser consideradas durante a análise da linguagem.

## 10. Contribuição para o projeto

O artigo contribui para:

* Fundamentar a análise de complexidade;
* Relacionar propriedades da linguagem ao processamento;
* Justificar a análise das características da GameLang;
* Apoiar a discussão sobre DSLs;
* Relacionar características gramaticais ao processamento.

## 11. Limitações

O trabalho não apresenta uma análise específica de uma DSL voltada para combates de RPG.

Seu objetivo é mais amplo e está relacionado à avaliação da complexidade de linguagens de programação e ao impacto dessa complexidade nas ferramentas de processamento.

Por isso, seus conceitos serão utilizados como fundamentação teórica para a análise da GameLang.

## 12. Conclusão

O artigo é uma referência importante para a GameLang porque trata diretamente da relação entre a complexidade de uma linguagem e o esforço necessário para processá-la.

A abordagem apresentada ajuda a justificar a inclusão de uma análise de complexidade no projeto, principalmente nas etapas relacionadas à gramática e ao parsing.

## 13. Palavras-chave

Complexidade; Linguagens de programação; DSL; Gramáticas; Processamento de linguagens; Análise estática.

https://doi.org/10.4230/OASIcs.SLATE.2022.16?utm_source=chatgpt.com