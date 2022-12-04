
from typing import Self
from os import path
from .animation_state import AnimationState
import json
import pygame

class Animation:
    def __init__(self, animations: dict, animation_states: AnimationState):
        self.animations = animations
        self._state = animation_states
        self.index = 0
        self.frame_count = 0

    def current_surface(self) -> pygame.Surface:
        #print(self.state)
        return self.animations[self.state.value][self.index]

    def get_rect(self, **kwargs) -> pygame.Rect:
        return self.current_surface().get_rect(**kwargs)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: AnimationState):
        if state is not self._state:
            self._state = state
            #self.frame_count = 0

    def update(self, frame_rate: int):
        self.frame_count += 1
        if self.frame_count > len(self.animations[self.state.value]) / frame_rate:
            self.frame_count = 0
            self.index = (self.index + 1) % len(self.animations[self.state.value])

    @staticmethod
    def sprite_sheet(size: dict, names: dict, sheet: pygame.Surface, scale=1):
        animations = {}
        width, height = size.values()

        for row, (name, num_images) in enumerate(names.items()):
            animations.update({name: []})
            for column in range(num_images):
                rect = (column * width, row * height, width, height)
                sub_surface = sheet.subsurface(rect)
                if scale > 1:
                    sub_surface = pygame.transform.smoothscale(sub_surface, (width * scale, height * scale))
                animations[name].append(sub_surface)

        return animations

    @classmethod
    def create(cls, sheet_name: str, data_path: path, sprite_path: path, animation_state: AnimationState) -> Self:
        with open(data_path, 'r') as meta_data:
            data = json.load(meta_data)
            size, names = data.get(sheet_name).values()
            sheet = pygame.image.load(sprite_path).convert_alpha()
            animations = Animation.sprite_sheet(size, names, sheet, 3)

        return cls(animations, animation_state)

































