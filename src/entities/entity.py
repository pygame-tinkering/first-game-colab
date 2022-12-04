
from ..animation import Animation
from ..control import MouseKeyboard
from assets import CHARACTER_PATH, CHARACTER_DATA_PATH
from ..animation import PlayerState

class Entity:
    def __init__(self,
                 position: list[int, int] | tuple[int, int],
                 control: MouseKeyboard | None = None,
                 frame_rate: int = 60,
                 ):
        self.animations = Animation.create('character', CHARACTER_DATA_PATH, CHARACTER_PATH, PlayerState.DOWN)
        self.rect = self.animations.get_rect(center=position)
        self.control = control
        self.frame_rate = frame_rate
        self.speed = 5

    def check_state(self):
        if self.control.direction['left']:
            self.animations.state = PlayerState.LEFT
        if self.control.direction['right']:
            self.animations.state = PlayerState.RIGHT

        if self.control.direction['up'] and self.control.direction['left']:
            self.animations.state = PlayerState.UPLEFT
        elif self.control.direction['up'] and self.control.direction['right']:
            self.animations.state = PlayerState.UPRIGHT
        elif self.control.direction['up']:
            self.animations.state = PlayerState.UP

        if self.control.direction['down'] and self.control.direction['left']:
            self.animations.state = PlayerState.DOWNLEFT
        elif self.control.direction['down'] and self.control.direction['right']:
            self.animations.state = PlayerState.DOWNRIGHT
        elif self.control.direction['down']:
            self.animations.state = PlayerState.DOWN

    def movement(self):
        if self.control.direction['up']:
            self.rect.y -= self.speed
        if self.control.direction['down']:
            self.animations.state = PlayerState.DOWN
            self.rect.y += self.speed
        if self.control.direction['left']:
            self.animations.state = PlayerState.LEFT
            self.rect.x -= self.speed
        if self.control.direction['right']:
            self.animations.state = PlayerState.RIGHT
            self.rect.x += self.speed

    def update(self) -> None:
        self.animations.update(self.frame_rate)
        self.movement()
        self.check_state()

    def render(self, surface) -> None:
        surface.blit(self.animations.current_surface(), self.rect)

































