
from typing import Iterable, Any
from src.settings import Settings
from .manager import Manager
import pygame

class UpdateManager(Manager):
    def __init__(self):
        self.settings = Settings()
        self.clock = pygame.time.Clock()

    def _update(self, objects: Iterable | Any):
        if isinstance(objects, Iterable):
            for obj in objects:
                self._update(obj)
        else:
            objects.update()

    def update(self, objects: Iterable | Any):
        self.clock.tick(self.settings.frame_rate)
        self._update(objects)
































