#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    ## Decorator
            - O Decorator é um padrão de projeto estrutural que permite que você acople novos comportamentos para objetos ao colocá-los dentro de invólucros de objetos que contém os comportamentos.
            - Estender uma classe é a primeira coisa que vem à mente quando você precisa alterar o comportamento de um objeto. Contudo a herança é estática. Você não pode alterar o comportamento de um objeto existente durante o tempo de execução.

            ### Quando usar?
                - Utilize o padrão Decorator quando você precisa ser capaz de projetar comportamentos adicionais para objetos em tempo de execução sem quebrar o código que usa esses objetos.
                - Utilize o padrão quando é complicado ou impossível estender o comportamento de um objeto usando herança.

            ### Vantagens:
                - Você pode estender o comportamento de um objeto sem fazer um nova subclasse.
                - Você pode adicionar ou remover responsabilidades de um objeto no momento da execução.
                - Você pode combinar diversos comportamentos ao envolver o objeto com múltiplos decoradores.
                - Princípio de responsabilidade única. Você pode dividir uma classe monolítica que implementa muitas possíveis variantes de um comportamento em diversas classes menores.
            ### Desvantagens:
                - É difícil remover um invólucro (wrapper) de uma pilha de invólucros (wrappers).
                - É difícil implementar um decorador de tal maneira que seu comportamento não dependa da ordem do pilha de decoradores.
                - A configuração inicial do código de camadas pode ficar bastante feia.
"""
from estructural.Decorator.Component import Component
from estructural.Decorator.ConcreteComponent import ConcreteComponent
from estructural.Decorator.ConcreteDecoratorA import ConcreteDecoratorA
from estructural.Decorator.ConcreteDecoratorB import ConcreteDecoratorB


def client_code(component: Component) -> None:
    print(f"RESULTADO: {component.operation()}", end="")


def start() -> None:
    simple = ConcreteComponent()
    print("Cliente: Peguei um componente simples")
    client_code(simple)
    print("/n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)

    print("Cliente: Agora tenho um componente decorado")

    client_code(decorator2)

