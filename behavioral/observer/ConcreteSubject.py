#!/usr/bin/python
# -*- coding: UTF-8 -*-
from random import randrange

from behavioral.observer.Observer import Observer
from behavioral.observer.Subject import Subject


class ConcreteSubject(Subject):

    def attach(self, observer: Observer) -> None:
        print("Subject: Anexando Observer")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("Subject: Desanexando Observer")
        self._observers.remove(observer)

    def notify(self) -> None:
        print("subject: Notificando Observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: Estou fazendo algo importante.")
        self._state = randrange(0, 10)
        print(f"Subject: Meu estado foi alterado para: {self._state}")
