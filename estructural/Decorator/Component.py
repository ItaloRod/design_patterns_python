#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
interface base do componente que tem uma operação alterada pelos decorators
"""
from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass
