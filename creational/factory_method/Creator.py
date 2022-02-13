#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod
# Este módulo provê a infraestrutura necessária para criar classes abstratas no python. abc é de Abstract Base Classes.


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        """
            implementação padrão do  factory method
        :param self:
        :return:
        """
        pass

    def some_operation(self) -> str:
        """
        Chama o factory_method que devolverá a instância do produto ao ser implementada.
        :param self:
        :return: result
        """
        product = self.factory_method()

        result = f"Creator: O mesmo código do criador que funcionou com {product.operation()}"
        return result
