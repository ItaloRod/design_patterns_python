#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Facade.Subsystem2 import Subsystem2
from estructural.Facade.Subsystem1 import Subsystem1


class Facade:

    _subsystem1: Subsystem1
    _subsystem2: Subsystem2

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        results = []
        results.append("Facade Inicilizando os Subsistemas: ")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Ordens do Subsistemas do Facade para performar a execução: ")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())

        return "\n".join(results)


