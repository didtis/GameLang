# GIGL: A Domain Specific Language for Procedural Content Generation with Grammatical Representations

## 1. Referência bibliográfica

CHEN, Tiannan; GUY, Stephen. **GIGL: A Domain Specific Language for Procedural Content Generation with Grammatical Representations**. In: *Proceedings of the 14th AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment (AIIDE 2018)*. v. 14, n. 1, p. 9–16, 2018. DOI: 10.1609/aiide.v14i1.13025.

## 2. Área de estudo

* Desenvolvimento de jogos
* Domain-Specific Languages
* Geração procedural de conteúdo
* Gramáticas
* Inteligência artificial aplicada a jogos
* C++

## 3. Resumo

O artigo apresenta a **Grammatical Item Generation Language (GIGL)**, uma linguagem específica de domínio desenvolvida para geração procedural de conteúdo.

A linguagem utiliza gramáticas estocásticas para representar conteúdos que podem ser gerados proceduralmente.

Um dos objetivos da GIGL é permitir uma representação compacta e expressiva para problemas de geração procedural de conteúdo.

A linguagem também possui integração direta com C++, permitindo sua utilização em jogos e sistemas de produção.

## 4. Objetivo

O objetivo da GIGL é fornecer uma linguagem específica para representar e gerar conteúdo procedural utilizando representações gramaticais.

A proposta busca facilitar a implementação de sistemas de geração procedural, permitindo representar regras de geração de maneira mais compacta.

## 5. Funcionamento geral

A GIGL utiliza gramáticas estocásticas para representar processos de geração.

De maneira simplificada:

```text
Gramática
   ↓
Regras de geração
   ↓
Processo procedural
   ↓
Conteúdo gerado
```

Os objetos produzidos durante a geração mantêm estruturas gramaticais.

## 6. Integração com C++

Uma característica importante da GIGL é sua interface direta com C++.

Essa integração permite que a linguagem seja incorporada a sistemas desenvolvidos em C++ e utilizada em ambientes de produção de jogos.

Essa característica demonstra como uma DSL pode ser criada para um domínio específico e, ao mesmo tempo, integrada a uma linguagem de programação de propósito geral.

## 7. Avaliação

Os autores apresentam exemplos representativos de problemas de geração procedural de conteúdo.

A avaliação demonstra a expressividade e a flexibilidade da linguagem em diferentes situações relacionadas à geração procedural baseada em gramáticas.

Os autores também relatam que implementações baseadas em GIGL apresentam velocidade comparável às implementações correspondentes em C++, utilizando menos código.

## 8. Relação com jogos

Este artigo possui uma relação especialmente forte com o projeto GameLang.

A GIGL foi criada especificamente para aplicações relacionadas à geração procedural de conteúdo em jogos.

A GameLang também possui como domínio os jogos, porém com um objetivo diferente.

Enquanto a GIGL trabalha com geração procedural de conteúdo, a GameLang será utilizada para representar a lógica de combates de RPG.

## 9. Relação com gramáticas

As gramáticas são um elemento fundamental da GIGL.

A linguagem utiliza representações gramaticais para descrever como conteúdos podem ser gerados.

Esse conceito é relevante para a GameLang porque o projeto também utilizará uma gramática para definir a estrutura dos comandos.

Por exemplo, a GameLang poderá possuir uma regra semelhante a:

```text
<ataque> ::= ATAQUE <personagem> ALVO <inimigo>
```

Essa regra determina uma estrutura válida para um comando de ataque.

## 10. Relação com DSLs

A GIGL demonstra uma aplicação prática do conceito de Domain-Specific Language.

Em vez de utilizar uma linguagem de programação geral para representar diretamente todas as regras de geração procedural, os desenvolvedores criaram uma linguagem especializada no domínio.

A GameLang segue uma ideia semelhante.

Seu objetivo é criar uma linguagem especializada para representar comandos relacionados à lógica de combates de RPG.

## 11. Comparação conceitual

| Característica | GIGL                | GameLang           |
| -------------- | ------------------- | ------------------ |
| Tipo           | DSL                 | DSL                |
| Domínio        | Jogos               | Jogos/RPG          |
| Gramáticas     | Sim                 | Sim                |
| Objetivo       | Geração procedural  | Lógica de combate  |
| Integração     | C++                 | Compilador próprio |
| Aplicação      | Conteúdo procedural | Combates de RPG    |

Essa comparação demonstra que, embora as duas linguagens sejam diferentes, ambas utilizam o conceito de uma linguagem específica para solucionar problemas dentro do domínio de jogos.

## 12. Contribuição para o projeto

O artigo contribui para:

* Fundamentação do uso de DSLs em jogos;
* Aplicação de gramáticas em sistemas de jogos;
* Demonstração de uma DSL real;
* Relação entre gramáticas e geração de conteúdo;
* Discussão de desempenho;
* Integração entre uma DSL e uma linguagem de programação.

## 13. Limitações

A GIGL possui um objetivo diferente da GameLang.

O foco da GIGL é a geração procedural de conteúdo, enquanto a GameLang será voltada para a representação da lógica de combates de RPG.

Portanto, o artigo não deve ser utilizado como modelo direto da arquitetura do compilador da GameLang.

Sua principal contribuição é demonstrar que DSLs baseadas em representações gramaticais podem ser aplicadas de maneira prática no desenvolvimento de jogos.

## 14. Conclusão

A GIGL é uma referência importante para o projeto GameLang porque demonstra uma aplicação concreta de uma DSL baseada em representações gramaticais dentro do desenvolvimento de jogos.

O trabalho ajuda a justificar a escolha de uma DSL para um domínio específico e demonstra que uma linguagem especializada pode tornar determinadas representações mais compactas e expressivas.

Embora os objetivos da GIGL e da GameLang sejam diferentes, os dois projetos compartilham a ideia de utilizar linguagens específicas de domínio e conceitos gramaticais para resolver problemas relacionados a jogos.

## 15. Palavras-chave

GIGL; DSL; Jogos; Geração procedural; Gramáticas; C++; Inteligência artificial.

https://doi.org/10.1609/aiide.v14i1.13025?utm_source=chatgpt.com