#!/usr/bin/python
# -*- coding: UTF-8 -*-

from creational.factory_method.ConcreteCreator1 import ConcreteCreator1
from creational.factory_method.ConcreteCreator2 import ConcreteCreator2

"""
    ## Factory Method
        - O Factory Method é um padrão criacional de projeto que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.

        ### Quando usar?
            -  Use o Factory Method quando não souber de antemão os tipos e dependências exatas dos objetos com os quais seu código deve funcionar.
            - Use o Factory Method quando deseja economizar recursos do sistema reutilizando objetos existentes em vez de recriá-los sempre.
    
        ### Vantagens:
            - Evita acoplamentos firmes entre o criador e os produtos concretos.
            - Utiliza o Princípio de responsabilidade única. Você pode mover o código de criação do produto para um único local do programa, facilitando a manutenção do código.
            - Utiliza o Princípio aberto/fechado. Você pode introduzir novos tipos de produtos no programa sem quebrar o código cliente existente.
            
        ### Desvantagens:
            - O código pode se tornar mais complicado, pois você precisa introduzir muitas subclasses novas para implementar o padrão. O melhor cenário é quando você está introduzindo o padrão em uma hierarquia existente de classes criadoras.
"""


def client_code(creator) -> None:

    print(f"Client: Eu não conheço a classe do criador, mas ainda funciona \n"
          f"{creator.some_operation()}", end="")


def start() -> None:
    print("App:  Chama o cliente com o ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Chama o cliente com o ConcreteCreator2.")
    client_code(ConcreteCreator2())

