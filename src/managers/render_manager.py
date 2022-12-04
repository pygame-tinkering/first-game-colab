
from typing import Iterable
from ..settings import Settings
from ..singleton import Singleton
import pygame

class RenderSingleton(Singleton):
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

































