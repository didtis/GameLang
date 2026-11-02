# Supporting Meta-model-based Language Evolution and Rapid Prototyping with Automated Grammar Transformation

## 1. Referência bibliográfica

ZHANG, Weixing; HOLTMANN, Jörg; STRÜBER, Daniel; HEBIG, Regina; STEGHÖFER, Jan-Philipp. **Supporting meta-model-based language evolution and rapid prototyping with automated grammar transformation**. *Journal of Systems and Software*, v. 214, article 112069, 2024. DOI: 10.1016/j.jss.2024.112069.

## 2. Área de estudo

* Domain-Specific Languages
* Gramáticas
* Evolução de linguagens
* Prototipagem
* Metamodelos
* Xtext
* Engenharia de software

## 3. Resumo

O artigo aborda o desenvolvimento e a evolução de linguagens específicas de domínio textuais.

Em um processo baseado em metamodelos, o metamodelo define a estrutura abstrata da linguagem enquanto a gramática define sua sintaxe concreta.

Os autores observam que a evolução de uma linguagem pode exigir alterações na gramática. Quando essas alterações são realizadas manualmente, o processo pode ser trabalhoso e sujeito a erros.

Para solucionar esse problema, os autores apresentam o **GrammarTransformer**, uma abordagem que utiliza regras configuráveis para automatizar transformações em gramáticas.

## 4. Objetivo

O objetivo é reduzir o esforço manual necessário para modificar gramáticas durante a evolução e a prototipagem rápida de DSLs.

A abordagem permite configurar regras de transformação que podem ser aplicadas novamente quando a linguagem evolui.

## 5. Problema abordado

Durante a evolução de uma DSL, alterações realizadas no metamodelo podem exigir alterações correspondentes na gramática.

Realizar essas alterações manualmente pode gerar:

* Maior esforço;
* Repetição de tarefas;
* Possibilidade de erros;
* Dificuldade de manutenção;
* Maior tempo de desenvolvimento.

O GrammarTransformer procura reduzir esses problemas.

## 6. Metodologia

Os autores desenvolveram um conjunto de regras de transformação para gramáticas.

Essas regras foram obtidas a partir da comparação entre gramáticas geradas automaticamente e gramáticas desenvolvidas por especialistas.

A análise foi realizada utilizando sete linguagens específicas de domínio.

Posteriormente, os autores avaliaram se o GrammarTransformer conseguia realizar transformações semelhantes às alterações feitas manualmente pelos especialistas.

## 7. Resultados

A avaliação realizada com sete DSLs mostrou que o GrammarTransformer conseguiu modificar gramáticas geradas pelo Xtext de maneira compatível com as alterações realizadas manualmente por especialistas.

Os autores também relatam uma redução significativa do esforço manual.

A abordagem permite que determinadas transformações sejam aplicadas novamente após futuras alterações na linguagem, reduzindo a necessidade de repetir manualmente as mesmas modificações.

## 8. Relação com a GameLang

A GameLang também terá uma gramática que poderá evoluir durante o desenvolvimento.

Inicialmente, a linguagem pode possuir comandos básicos como:

```text
ATAQUE
DEFESA
MOVIMENTO
```

Posteriormente, podem ser adicionados elementos como:

```text
HABILIDADE
CONDICAO
TURNO
EFEITO
```

Cada novo recurso pode exigir alterações na gramática.

Nesse contexto, o artigo ajuda a compreender os problemas relacionados à evolução de uma DSL e à manutenção de sua gramática.

## 9. Relação com GLC

A GameLang pretende utilizar uma Gramática Livre de Contexto para especificar sua sintaxe.

Uma alteração na linguagem pode exigir a criação ou modificação de regras gramaticais.

Por exemplo:

```text
<ataque> ::= ATAQUE <personagem> ALVO <inimigo>
```

Se futuramente a linguagem permitir um tipo adicional de ataque, a gramática poderá precisar ser modificada.

O artigo fornece uma perspectiva sobre como alterações desse tipo podem ser organizadas e automatizadas em determinados ambientes.

## 10. Contribuição para o projeto

O artigo contribui para:

* Definição de DSLs;
* Evolução da gramática;
* Manutenção de linguagens;
* Prototipagem rápida;
* Automação de transformações;
* Organização das regras gramaticais.

## 11. Limitações

O artigo não é específico para linguagens de jogos ou sistemas de combate.

Além disso, a abordagem está relacionada ao desenvolvimento de DSLs baseado em metamodelos e ferramentas como Xtext.

A GameLang possui um escopo menor e será desenvolvida como projeto acadêmico.

## 12. Conclusão

O artigo demonstra que a evolução de uma DSL pode gerar trabalho adicional quando as alterações precisam ser realizadas manualmente na gramática.

A abordagem GrammarTransformer mostra uma forma de automatizar parte desse processo.

Para a GameLang, o artigo é importante porque ajuda a compreender como a gramática poderá ser mantida e modificada conforme novos comandos e funcionalidades forem adicionados à linguagem.

## 13. Palavras-chave

DSL; Gramática; Xtext; Evolução de linguagens; Prototipagem; Transformação de gramáticas.

https://doi.org/10.1016/j.jss.2024.112069?utm_source=chatgpt.com