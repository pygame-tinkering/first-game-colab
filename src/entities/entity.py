
from typing import Iterable
from ..animation import Animation, AnimationState
from ..control.controller import Controller
from ..animation import PlayerState
from .weapon import Weapon
import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,
                 position: tuple[int, int] | list[int, int],
                 control: Controller | None = None,
                 frame_rate: int = 30,
                 *groups: list
                 ) -> None:
        super().__init__(*groups)
        self.animations = {}
        self.rect = pygame.Rect(position, (0, 0))
        self.control = control
        self.weapon = Weapon(position=self.rect.center, frame_rate=5)
        self.frame_rate = frame_rate
        self.speed: int = 5
        self._shoot: bool = False

    def load_animations(self, sheet_name: str):
        self.animations = Animation.create(sheet_name)
        self.rect = self.animations.get_rect(center=self.rect.center)
        if self.weapon:
            self.weapon.load_animations('None')

    def check_state(self):
        if self.control.direction.up and self.control.direction.left:
            self.animations.state = PlayerState.UPLEFT
        elif self.control.direction.up and self.control.direction.right:
            self.animations.state = PlayerState.UPRIGHT
        elif self.control.direction.down and self.control.direction.left:
            self.animations.state = PlayerState.DOWNLEFT
        elif self.control.direction.down and self.control.direction.right:
            self.animations.state = PlayerState.DOWNRIGHT
        elif self.control.direction.up:
            self.animations.state = PlayerState.UP
        elif self.control.direction.down:
            self.animations.state = PlayerState.DOWN
        elif self.control.direction.left:
            self.animations.state = PlayerState.LEFT
        elif self.control.direction.right:
            self.animations.state = PlayerState.RIGHT

    def movement(self):
        if self.control.direction.up:
            self.rect.y -= self.speed
        if self.control.direction.down:
            self.animations.state = PlayerState.DOWN
            self.rect.y += self.speed
        if self.control.direction.left:
            self.animations.state = PlayerState.LEFT
            self.rect.x -= self.speed
        if self.control.direction.right:
            self.animations.state = PlayerState.RIGHT
            self.rect.x += self.speed

    def update(self) -> None:
        self.animations.update(self.frame_rate)
        if self.control:
            self.movement()
            self.check_state()
            if self.control.click.left:
                self.weapon.has_shot = True
            else:
                self.weapon.has_shot = False
        if self.weapon:
            self.weapon.rect.center = self.rect.center


    def render(self, surface) -> None:
        surface.blit(self.animations.current_surface(), self.rect)

































