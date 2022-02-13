#!/usr/bin/python
# -*- coding: UTF-8 -*-
from creational.factory_method.Product import Product


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado do ConcreteProduct2}"
