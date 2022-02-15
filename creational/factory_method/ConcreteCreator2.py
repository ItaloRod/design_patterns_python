#!/usr/bin/python
# -*- coding: UTF-8 -*-
from creational.factory_method.ConcreteProduct2 import ConcreteProduct2
from creational.factory_method.Creator import Creator
from creational.factory_method.Product import Product


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
