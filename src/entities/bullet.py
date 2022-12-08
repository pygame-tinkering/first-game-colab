
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,
                 position: tuple[int, int] | list[int, int],
                 max_distance: int,
                 *groups: list
                 ) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((10, 10))
        self.image.fill('white')
        self.position = pygame.Vector2(position)
        self.rect = self.image.get_rect(center=position)
        self.speed = 10
        self.max_distance = max_distance
        self.velocity = pygame.Vector2(0, 0)
        self.start_position = pygame.Vector2(position)
        self.travel_distance = 0

    def apply_force(self, force: tuple[float, float] | list[float, float] | pygame.Vector2):
        self.velocity += force

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position
        self.check_distance_traveled()

    def check_distance_traveled(self):
        distance = self.start_position.distance_to(self.rect.center)
        if distance >= self.max_distance:
            self.kill()

    def render(self, surface):
        surface.blit(self.image, self.rect)

































