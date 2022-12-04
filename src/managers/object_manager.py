
from typing import Iterable
from ..singleton import Singleton
from ..entities import Entity
from ..control import Controller


class ObjectManager(Singleton):
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

    def create(self,
               sheet_name: str,
               position: list[int, int] | tuple[int, int],
               control: Controller | None = None,
               frame_rate: int = 60,) -> Entity:
        entity = Entity(position, control, frame_rate)
        entity.load_animations(sheet_name)
        return entity


































