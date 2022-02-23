#!/usr/bin/python
# -*- coding: UTF-8 -*-


class SelfReferencingEntity:
    def __init__(self):
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

