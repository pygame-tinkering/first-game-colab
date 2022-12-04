
from ..animation import Animation, AnimationState
from ..control import Controller
from ..animation import PlayerState
from os import path
import pygame

class Entity:
    def __init__(self,
                 position: list[int, int] | tuple[int, int],
                 control: Controller | None = None,
                 frame_rate: int = 60,
                 ):
        self.animations = {}
        self.rect = pygame.Rect(position, (0, 0))
        self.control = control
        self.frame_rate = frame_rate
        self.speed = 5

    def load_animations(self, sheet_name: str):
        self.animations = Animation.create(sheet_name)
        self.rect = self.animations.get_rect(center=self.rect.center)

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

    def shoot(self):
        pass

    def update(self) -> None:
        self.animations.update(self.frame_rate)
        self.movement()
        self.check_state()

    def render(self, surface) -> None:
        surface.blit(self.animations.current_surface(), self.rect)

































