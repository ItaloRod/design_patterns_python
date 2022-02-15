#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Bridge.Abstraction import Abstraction


class ExtendedAbstraction(Abstraction):

    """
    Você pode extender a abstraçao sem precisar realizar implementação dentro da classe
    """

    def operation(self) -> str:
        return (
            f"Abstração extendida: Operação extendida com: \n"
            f"{self.implementation.operation_implementation()}"
        )