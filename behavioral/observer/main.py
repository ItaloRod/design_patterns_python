#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    ## Observer
        - O Observer é um padrão de projeto comportamental que permite que você defina um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando.

        ### Quando usar?
            - Utilize o padrão Observer quando mudanças no estado de um objeto podem precisar mudar outros objetos, e o atual conjunto de objetos é desconhecido de antemão ou muda dinamicamente.
            - Utilize o padrão quando alguns objetos em sua aplicação devem observar outros, mas apenas por um tempo limitado ou em casos específicos.

        ### Vantagens:
            - Princípio aberto/fechado. Você pode introduzir novas classes assinantes sem ter que mudar o código da publicadora (e vice versa se existe uma interface publicadora).
            - Você pode estabelecer relações entre objetos durante a execução.

        ### Desvantagens:
            - Assinantes são notificados em ordem aleatória
"""
from behavioral.observer.ConcreteObserverA import ConcreteObserverA
from behavioral.observer.ConcreteObserverB import ConcreteObserverB
from behavioral.observer.ConcreteSubject import ConcreteSubject


def start():
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.attach(observer_a)
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
