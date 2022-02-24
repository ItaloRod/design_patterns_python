#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABC, abstractmethod

from behavioral.observer.Observer import Observer


class Subject(ABC):

    _state: int = None
    _observers: list[Observer] = []

    @property
    def state(self):
        return self._state
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass
