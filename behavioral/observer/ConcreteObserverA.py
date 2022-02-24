#!/usr/bin/python
# -*- coding: UTF-8 -*-
from behavioral.observer.Observer import Observer
from behavioral.observer.Subject import Subject


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state() < 3:
            print("ConcreteObserverA: Reagindo ao evento")
