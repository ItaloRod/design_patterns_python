#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    ## Bridge
            - O Bridge é um padrão de projeto estrutural que permite que você divida uma classe grande ou um conjunto de classes intimamente ligadas em duas hierarquias separadas—abstração e implementação—que podem ser desenvolvidas independentemente umas das outras.

            ### Quando usar?
                - Utilize o padrão Bridge quando você quer dividir e organizar uma classe monolítica que tem diversas variantes da mesma funcionalidade (por exemplo, se a classe pode trabalhar com diversos servidores de base de dados).
                - Utilize o padrão quando você precisa estender uma classe em diversas dimensões ortogonais (independentes).
                - Utilize o Bridge se você precisar ser capaz de trocar implementações durante o momento de execução.

            ### Vantagens:
                - Você pode criar classes e aplicações independentes de plataforma.
                -  O código cliente trabalha com abstrações em alto nível. Ele não fica exposto a detalhes de plataforma.
                -  Princípio aberto/fechado. Você pode introduzir novas abstrações e implementações independentemente uma das outras.
                - Princípio de responsabilidade única. Você pode focar na lógica de alto nível na abstração e em detalhes de plataforma na implementação.

            ### Desvantagens:
                - Você pode tornar o código mais complicado ao aplicar o padrão em uma classe altamente coesa.
"""
from estructural.Bridge.Abstraction import Abstraction
from estructural.Bridge.ConcreteImplementationA import ConcreteImplementationA
from estructural.Bridge.ConcreteImplementationB import ConcreteImplementationB
from estructural.Bridge.ExtendedAbstraction import ExtendedAbstraction


def client_code(abstraction: Abstraction) -> None:

    print(abstraction.operation(), end="")


def start():

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
