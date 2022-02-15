#!/usr/bin/python
# -*- coding: UTF-8 -*-
from estructural.Decorator.Component import Component


class Decorator(Component):
    """
        É o decorator base que tem a mesma interface que outros componentes. Ele vai servir de base para decoradores concretos que irão envolver esse código.
    """
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()
