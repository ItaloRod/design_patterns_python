#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, subject):
        pass
