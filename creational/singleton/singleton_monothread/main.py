#!/usr/bin/python
# -*- coding: UTF-8 -*-
from creational.singleton.singleton_monothread.Singleton import Singleton


def monothread_start():
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton funcionou! Ambas as variáveis possuem a mesma instância")
    else:
        print("Singleton falhou! As variáveis possuem diferentes instâncias")