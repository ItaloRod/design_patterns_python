#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Decorator.Component import Component


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "Componente Concreto"