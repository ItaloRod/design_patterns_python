#!/usr/bin/python
# -*- coding: UTF-8 -*-
from behavioral.observer.Observer import Observer
from behavioral.observer.Subject import Subject


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state() == 0 or subject.state() >= 2:
            print("ConcreteObserverB: Reagindo ao evento")
