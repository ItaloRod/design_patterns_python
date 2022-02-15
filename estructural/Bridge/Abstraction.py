#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Bridge.Implementation import Implementation


class Abstraction:

    """
    Dfine a interface que vai controlar parte das duas classes herdadas.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (
            f"Abstração: Operaçào base com: \n"
            f"{self.implementation.operation_implementation()}"
        )
