#!/usr/bin/python
# -*- coding: UTF-8 -*-
from behavioral.strategy.strategy import Strategy


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: list) -> list:
        return list(reversed(sorted(data)))
