#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod

'''
Esta é a interface de produto que será a base dos concreteProducts 1 e 2. Como no python não tem interface, esta tem que ser feita usando abstractMethod. 
'''


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass