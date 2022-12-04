
from typing import Iterable
from src.singleton import Singleton

class ObjectSingleton(Singleton):
    def __init__(self):
        self.objects = {}

    def _add(self, objects: Iterable | object):
        if isinstance(objects, Iterable):
            for obj in objects:
                self._add(obj)
        else:
            self._add(objects)

    def add(self, objects: Iterable | object):
        self._add(objects)

    def create(self, name: str):
        pass



































