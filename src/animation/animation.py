
from __future__ import annotations  # For python <= 3.10
# from typing import Self # For python 3.11
from os import path
import json
import pygame


class Animation:
    def __init__(self, animations: dict):
        self.animations = animations
        self.state = 'up'
        self.index = 0
        self.frame_rate_count = 0

    def current_surface(self) -> pygame.Surface:
        return self.animations[self.state][self.index]

    def get_rect(self, **kwargs) -> pygame.Rect:
        return self.current_surface().get_rect(**kwargs)

    def update(self, frame_rate: int):
        self.frame_rate_count += 1
        if self.frame_rate_count > len(self.animations[self.state]) / frame_rate:
            self.frame_rate_count = 0
            self.index = (self.index + 1) % len(self.animations[self.state])


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
    def create(cls, sheet_name: str, data_path: path, sprite_path: path) -> Animation:
        with open(data_path, 'r') as meta_data:
            data = json.load(meta_data)
            size, names = data.get(sheet_name).values()
            sheet = pygame.image.load(sprite_path).convert_alpha()
            animations = Animation.sprite_sheet(size, names, sheet, 3)

        return cls(animations)

































