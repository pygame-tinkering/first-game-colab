
import pygame
from assets.paths import FONTS

class Font(pygame.font.Font):
    def __init__(self,
                 name: str = None,
                 size: int = None,
                 text: str = '',
                 ):
        super().__init__(FONTS[name], size)
        self.name = name
        self.size = size
        self.text = text

    def render(self,
               text: str | bytes = None,
               antialias: bool = True,
               bg_color: tuple[int, int, int] | list[int, int, int] | str = None,
               fg_color: tuple[int, int, int] | list[int, int, int] | str = 'white',
               ) -> pygame.Surface:
        return super().render('Hello', antialias, fg_color)































