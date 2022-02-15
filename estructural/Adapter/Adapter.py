#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Adapter.Adaptee import Adaptee
from estructural.Adapter.Target import Target


"""
A classe Adapter torna a classe Adaptee compatível com o a interface Target.
"""


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"adapter: (TRANSLATED) {self.specific_request()[::-1]}"
