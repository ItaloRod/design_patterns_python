#!/usr/bin/python
# -*- coding: UTF-8 -*-
import copy

class SomeComponent:
    def __init__(self, some_int: int, some_list_ofobjects: list, some_circular_ref ):
        self.some_int = some_int
        self.some_list_of_objects = some_list_ofobjects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):

        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)

        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memodict=None):

        if memodict is None:
            memo = {}

        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memodict)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memodict)

        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memodict)

        return new
