
from assets import CHARACTER_SPRITE_PATH, CHARACTER_DATA_PATH, ITEMSPACK_SPRITE_PATH, ITEMSPACK_DATA_PATH
from .animation_state import AnimationState
from .player_state import PlayerState
from os import path
import pygame

class ImageLoader:
    animations = {
        'character': [CHARACTER_SPRITE_PATH, CHARACTER_DATA_PATH, PlayerState.DOWN],
    }
    images = {
        'itemspack': [ITEMSPACK_SPRITE_PATH, ITEMSPACK_DATA_PATH]
    }

    @classmethod
    def load_animation(cls, sheet_name: str) -> list[path, path, AnimationState]:
        return cls.animations[sheet_name]

    @classmethod
    def load_image(cls, sheet_name: str) -> pygame.Surface:
        image = pygame.Surface((50, 50))
        image.fill('blue')
        return image #pygame.image.load(cls.images[sheet_name]).convert_alpha()

































