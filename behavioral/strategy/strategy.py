#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod


class Strategy(ABC):
    """
        Interface do strategy que declara as operações comum para todas as versões suportadas do algoritmo.
    """
    @abstractmethod
    def do_algorithm(self, data: list) -> list:
        pass
