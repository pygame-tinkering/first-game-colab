import pygame
from ..constants import \
    SCREEN_WIDTH, \
    SCREEN_HEIGHT, \
    FRAME_RATE, \
    BG_COLOR, \
    FG_COLOR, \
    FONT_NAME, \
    CAPTION

class Settings:
    def __init__(self):
        self._resolution = {
            'width': SCREEN_WIDTH,
            'height': SCREEN_HEIGHT
        }
        self.caption = CAPTION
        self.flags = pygame.SHOWN
        self.frame_rate = FRAME_RATE
        self.bg_color = BG_COLOR
        self.fg_color = FG_COLOR
        self.font_name = FONT_NAME

    @property
    def width(self) -> int:
        return self._resolution['width']

    @width.setter
    def width(self, value: int):
        # Need to check if value is within the monitor size before setting
        self._resolution['width'] = value

    @property
    def height(self) -> int:
        return self._resolution['height']

    @height.setter
    def height(self, value: int):
        # Need to check if value is within the monitor size before setting
        self._resolution['height'] = value

    @property
    def resolution(self) -> list[int, str]:
        return list(self._resolution.values())

    # @resolution.setter
    # def resolution(self, values: tuple[int, int] | list[int, int]):
    #     # Need to check if value is within the monitor size before setting
    #     for key, value in zip(self._resolution.keys(), values):
    #         self._resolution[key] = value
































