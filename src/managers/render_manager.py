
from typing import Iterable
from src.settings import Settings
from .manager import Manager
import pygame

class RenderManager(Manager):
    def __init__(self):
        self.settings = Settings()

    def _render(self, surface: pygame.Surface, objects: Iterable | object):
        if isinstance(objects, Iterable):
            for obj in objects:
                self._render(surface, obj)
        else:
            objects.render(surface)

    def render(self, surface: pygame.Surface, objects: Iterable | object):
        surface.fill(self.settings.bg_color)
        self._render(surface, objects)
        pygame.display.flip()

































