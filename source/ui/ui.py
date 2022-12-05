
from abc import ABC
import pygame
from .font import Font

class UI:
    def __init__(self, *,
                 size: tuple[int, int] | list[int, int],
                 position: tuple[int, int] | list[int, int],
                 bg_color: tuple[int, int, int] | list[int, int, int] | str,
                 fg_color: tuple[int, int, int] | list[int, int, int] | str,
                 anchor: str = 'center',
                 font: Font = None,
                 ):
        self.image = pygame.Surface(size)
        self.image.fill(bg_color)
        self.rect = self.image.get_rect(**{anchor: position})
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.anchor = anchor
        self.font = font

    def update(self):
        pass

    def render(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)































