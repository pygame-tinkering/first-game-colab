
from typing import Iterable
from ..singleton import Singleton
from ..entities import Entity
from ..control import Controller
from ..managers import EventManager

class ObjectManager(Singleton):
    def __init__(self):
        self.objects = {}
        self.event_manager = EventManager()

    def _add_type(self, obj: object):
        object_type = type(obj)
        objects = self.objects.get(object_type)
        if objects:
            objects.append(obj)
        else:
            self.objects.update({object_type: [obj]})

    def _add(self, objects: Iterable | object):
        if isinstance(objects, Iterable):
            for obj in objects:
                self._add(obj)
        else:
            self._add_type(objects)

    def add(self, objects: Iterable | object):
        self._add(objects)

    def create(self, *,
               sheet_name: str,
               position: list[int, int] | tuple[int, int],
               control: Controller | None = None,
               frame_rate: int = 60,) -> None:
        entity = Entity(position, control, frame_rate)
        entity.load_animations(sheet_name)
        self.add(entity)

    def get_objects(self) -> list:
        return list(self.objects.values())

































