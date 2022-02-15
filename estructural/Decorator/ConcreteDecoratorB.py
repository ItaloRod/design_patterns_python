#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Decorator.Decorator import Decorator


class ConcreteDecoratorB(Decorator):

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


