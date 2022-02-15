#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod


class Implementation(ABC):
    """
    A implementação define a interface para todas as classes de implementação.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass
