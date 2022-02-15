#!/usr/bin/python
# -*- coding: UTF-8 -*-
from behavioral.strategy.strategy import Strategy


class Context:
    """
    Contém a interface de interesse para os clientes
    """

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:

        self._strategy = strategy

    def do_some_business_logic(self) -> None:

        print("Context: Ordenando dados usando o Strategy")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))
