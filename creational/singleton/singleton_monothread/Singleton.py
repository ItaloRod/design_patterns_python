#!/usr/bin/python
# -*- coding: UTF-8 -*-
from creational.singleton.singleton_monothread.SingletonMeta import SingletonMeta


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass
