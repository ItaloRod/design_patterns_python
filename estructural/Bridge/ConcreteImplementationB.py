#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Bridge.Implementation import Implementation


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "Implementação Concreta B: Aqui está o resultado na plataforma B"
