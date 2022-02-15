#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Decorator.Decorator import Decorator


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"
