
from typing import Iterable
import pygame
from .bullet import Bullet
from ..animation import Animation
from ..animation import ImageLoader

class Weapon(pygame.sprite.Sprite):
    def __init__(self,
                 position: tuple[int, int] | list[int, int],
                 frame_rate: int = 30,
                 *groups: list
                 ) -> None:
        super().__init__(*groups)
        #self.animations = {}
        self.image = ImageLoader.load_image('itemspack')
        self.rect = pygame.Rect(position, (0, 0))
        self.frame_rate = frame_rate
        self._has_shot: bool = False
        self.fire_rate = 10
        self.can_shoot = True
        self._cooldown = 0
        self.max_range = 200

        # Refactor weapon stats into dictionary for easier loading

    def load_animations(self, sheet_name: str):
        #self.animations = Animation.create(sheet_name)
        self.rect = self.image.get_rect(center=self.rect.center)

    @property
    def has_shot(self) -> bool:
        return self._has_shot

    @has_shot.setter
    def has_shot(self, value: bool) -> None:
        self._has_shot = value

    @property
    def cooldown(self) -> int:
        return self._cooldown

    @cooldown.setter
    def cooldown(self, value: int) -> None:
        self._cooldown = max(value, 0)
        if self._cooldown <= 0:
            self.can_shoot = True

    def shoot(self) -> Bullet:
        bullet = Bullet(self.rect.center, self.max_range)
        direction = self.get_direction_towards_mouse()
        bullet.apply_force(direction * bullet.speed)
        self.has_shot = False
        self.can_shoot = False
        self.cooldown = self.fire_rate
        return bullet

    def update(self):

        self.cooldown -= 1

    def render(self, surface):
        surface.blit(self.image, self.rect)

    def get_direction_towards_mouse(self) -> pygame.Vector2:
        target_position = pygame.Vector2(pygame.mouse.get_pos())
        direction = (target_position - self.rect.center).normalize()
        return direction





























