import pygame.mouse

from .ui import UI
from ..utils import get_center

class Button(UI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hovered = False
        self._refresh()

    def _render_hover(self):
        if self.hovered:
            rect = self.image.get_rect()
            pygame.draw.rect(self.image, self.fg_color, rect, 5)
        else:
            self.image.fill(self.bg_color)

    def _render_text(self):
        if self.font:
            rendered_text = self.font.render()
            rect = rendered_text.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
            self.image.blit(rendered_text, rect)

    def _refresh(self) -> None:
        self._render_hover()
        self._render_text()

    @property
    def hovered(self) -> bool:
        return self._hovered

    @hovered.setter
    def hovered(self, value) -> None:
        self._hovered = value
        self._refresh()

    def hover(self) -> None:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

    def update(self) -> None:
        self.hover()

































