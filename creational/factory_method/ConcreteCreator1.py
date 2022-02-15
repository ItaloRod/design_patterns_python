#!/usr/bin/python
# -*- coding: UTF-8 -*-
from creational.factory_method.ConcreteProduct1 import ConcreteProduct1
from creational.factory_method.Creator import Creator
from creational.factory_method.Product import Product


class ConcreteCreator1(Creator):
    """
        Criado a partir do Creator, essa classe implementa a função do método fábrica que retorna a instância do produto que fabrica.
    """
    def factory_method(self) -> Product:
        return ConcreteProduct1()
