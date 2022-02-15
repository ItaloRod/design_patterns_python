#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
    ## Strategy
        -O Strategy é um padrão de projeto comportamental que permite que você defina uma família de algoritmos, coloque-os em classes separadas, e faça os objetos deles intercambiáveis.O padrão Strategy sugere que você pegue uma classe que faz algo específico em diversas maneiras diferentes e extraia todos esses algoritmos para classes separadas chamadas estratégias.

        ### Quando usar?
            -  Utilize o padrão Strategy quando você quer usar diferentes variantes de um algoritmo dentro de um objeto e ser capaz de trocar de um algoritmo para outro durante a execução.
            - Utilize o Strategy quando você tem muitas classes parecidas que somente diferem na forma que elas executam algum comportamento.
            - Utilize o padrão para isolar a lógica do negócio de uma classe dos detalhes de implementação de algoritmos que podem não ser tão importantes no contexto da lógica.
            - Utilize o padrão quando sua classe tem um operador condicional muito grande que troca entre diferentes variantes do mesmo algoritmo.

        ### Vantagens:
            - Você pode trocar algoritmos usados dentro de um objeto durante a execução.
            - Você pode isolar os detalhes de implementação de um algoritmo do código que usa ele.
            - Você pode substituir a herança por composição.
            - Princípio aberto/fechado. Você pode introduzir novas estratégias sem mudar o contexto.

        ### Desvantagens:
            - Se você só tem um par de algoritmos e eles raramente mudam, não há motivo real para deixar o programa mais complicado com novas classes e interfaces que vêm junto com o padrão.
            - Os Clientes devem estar cientes das diferenças entre as estratégias para serem capazes de selecionar a adequada.
            - Muitas linguagens de programação modernas tem suporte do tipo funcional que permite que você implemente diferentes versões de um algoritmo dentro de um conjunto de funções anônimas. Então você poderia usar essas funções exatamente como se estivesse usando objetos estratégia, mas sem inchar seu código com classes e interfaces adicionais.
"""
from behavioral.strategy.ConcreteStrategyA import ConcreteStrategyA
from behavioral.strategy.ConcreteStrategyB import ConcreteStrategyB
from behavioral.strategy.context import Context


def start():

    context = Context(ConcreteStrategyA())
    print("CLient: Strategy A com ordenação normal")
    context.do_some_business_logic()
    print("\n Client: Strategy B com ordenação reversa")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
