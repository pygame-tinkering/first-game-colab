
from assets import CHARACTER_SPRITE_PATH, CHARACTER_DATA_PATH
from .animation_state import AnimationState
from .player_state import PlayerState
from os import path

class AnimationLoader:
    animations = {
        'character': [CHARACTER_SPRITE_PATH, CHARACTER_DATA_PATH, PlayerState.DOWN],
    }

    @classmethod
    def load(cls, sheet_name: str) -> list[path, path, AnimationState]:
        return cls.animations[sheet_name]

































