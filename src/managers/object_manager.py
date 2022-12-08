
import pygame
from typing import Iterable
from ..singleton import Singleton
from ..entities import Entity, Bullet
from ..control import Controller
from ..managers.event_manager import EventManager
from ..managers.audio_manager import AudioManager
#from ..managers import EventManager, AudioManager
from collections import defaultdict


class ObjectManager(Singleton):
    def __init__(self):
        self.objects = defaultdict(lambda: pygame.sprite.Group())  # Should be a class? DefaultDict?
        self.event_manager = EventManager()
        self.audio_manager = AudioManager()

    def _add(self, obj: object):
        object_type = type(obj).__name__
        """
        group = self.objects.get(object_type)
        if group:
            group.add(obj)
        else:
            #self.objects.update({object_type: [obj]})
        """
        self.objects[object_type].add(obj)


    def add(self, objects: Iterable | object):
        if isinstance(objects, Iterable):
            for obj in objects:
                self.add(obj)
        else:
            self._add(objects)

    def create(self, *,
               sheet_name: str,
               position: list[int, int] | tuple[int, int],
               control: Controller | None = None,
               frame_rate: int = 60,) -> None:
        entity = Entity(position, control, frame_rate)
        entity.load_animations(sheet_name)
        if entity.weapon:
            self.add(entity.weapon)
        self.add(entity)

    def update(self) -> None:
        entity_with_weapons = (entity
                               for entity in self.objects.get('Entity')
                               if hasattr(entity, 'weapon') and entity.weapon
                               )
        for entity in entity_with_weapons:
            if entity.weapon.has_shot and entity.weapon.can_shoot:
                bullet = entity.weapon.shoot()
                self.audio_manager.play_sound('test')  # Add observer patter
                self.add(bullet)



    def get_objects(self) -> list:
        return list(self.objects.values())

































