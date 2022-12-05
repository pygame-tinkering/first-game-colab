
from typing import Iterable, Any
from ..settings import settings
from ..singleton import Singleton
import pygame

class UpdateManager(Singleton):
    def __init__(self):
        self.settings = settings.Settings()
        self.clock = pygame.time.Clock()

    def _update(self, objects: Iterable | Any):
        if isinstance(objects, Iterable):
            for obj in objects:
                self._update(obj)
        else:
            objects.update()

    def update(self, objects: Iterable | Any):
        #pygame.display.set_caption(f'FPS:{self.clock.get_fps():.2f}')
        self.clock.tick(self.settings.frame_rate)
        self._update(objects)
































