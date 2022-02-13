#!/usr/bin/python
# -*- coding: UTF-8 -*-
from creational.factory_method.Product import Product


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado do ConcreteProduct1}"
