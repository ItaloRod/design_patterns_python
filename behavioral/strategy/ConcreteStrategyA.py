#!/usr/bin/python
# -*- coding: UTF-8 -*-
from behavioral.strategy.strategy import Strategy


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: list) -> list:
        return sorted(data)
