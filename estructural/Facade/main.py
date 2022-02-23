#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
    ## Facade
           - O Facade é um padrão de projeto estrutural que fornece uma interface simplificada para uma biblioteca, um framework, ou qualquer conjunto complexo de classes.
           - Uma fachada é uma classe que fornece uma interface simples para um subsistema complexo que contém muitas partes que se movem. Uma fachada pode fornecer funcionalidades limitadas em comparação com trabalhar com os subsistemas diretamente. Contudo, ela inclui apenas aquelas funcionalidades que o cliente se importa.

            ### Quando usar?
                - Utilize o padrão Facade quando você precisa ter uma interface limitada mas simples para um subsistema complexo.
                - Utilize o Facade quando você quer estruturar um subsistema em camadas.

            ### Vantagens:
                - Uma fachada pode se tornar um objeto deus acoplado a todas as classes de uma aplicação.
"""
from estructural.Facade.Facade import Facade
from estructural.Facade.Subsystem1 import Subsystem1
from estructural.Facade.Subsystem2 import Subsystem2


def client_code(facade: Facade) -> None:
    print(facade.operation(), end="")


def start() -> None:

    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()

    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
