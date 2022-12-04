
from ..animation import Animation
from ..control import MouseKeyboard
from assets.paths import CHARACTER_PATH, CHARACTER_DATA_PATH

class Entity:
    def __init__(self,
                 position: list[int, int] | tuple[int, int],
                 control: MouseKeyboard | None = None,
                 frame_rate: int = 60,
                 ):
        self.animations = Animation.create('character', CHARACTER_DATA_PATH, CHARACTER_PATH)
        self.rect = self.animations.get_rect(center=position)
        self.control = control
        self.frame_rate = frame_rate
        self.speed = 5

    def movement(self):
        if self.control.direction['up']:
            self.rect.y -= self.speed
        if self.control.direction['down']:
            self.rect.y += self.speed
        if self.control.direction['left']:
            self.rect.x -= self.speed
        if self.control.direction['right']:
            self.rect.x += self.speed

    def update(self) -> None:
        self.animations.update(self.frame_rate)
        self.movement()

    def render(self, surface) -> None:
        surface.blit(self.animations.current_surface(), self.rect)

































