
import pygame
from typing import Iterable
from ..singleton import Singleton
from ..entities import Entity, Bullet
from ..control import Controller
from ..managers.event_manager import EventManager
from ..managers.audio_manager import AudioManager
#from ..managers import EventManager, AudioManager

# Move function to appropriate file
def get_direction_to_mouse(source_position: tuple[float, float] | list[int, int] | pygame.Vector2):
    target_position = pygame.Vector2(pygame.mouse.get_pos())
    direction = (target_position - source_position).normalize()
    return direction

class ObjectManager(Singleton):
    def __init__(self):
        self.objects = {}  # Should be a class? DefaultDict?
        self.event_manager = EventManager()
        self.audio_manager = AudioManager()

    def _add(self, obj: object):
        object_type = type(obj).__name__
        objects = self.objects.get(object_type)
        if objects:
            objects.append(obj)
        else:
            self.objects.update({object_type: [obj]})

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
        self.add(entity)

    def update(self) -> None:
        for entity in self.objects.get('Entity'):
            if entity.shoot:
                position = entity.rect.center
                bullet = Bullet(position)  # Weapon position later
                direction = get_direction_to_mouse(position)
                bullet.apply_force(direction * bullet.speed)
                self.audio_manager.play_sound('test')
                entity.shoot = False
                self.add(bullet)

    def get_objects(self) -> list:
        return list(self.objects.values())

































