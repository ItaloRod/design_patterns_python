#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Bridge.Implementation import Implementation


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "Implementação Concreta A: Aqui está o resultado na plataforma A"
