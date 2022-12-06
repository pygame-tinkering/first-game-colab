
import pygame

class Bullet:
    def __init__(self, position):
        self.image = pygame.Surface((10, 10))
        self.image.fill('white')
        self.position = pygame.Vector2(position)
        self.rect = self.image.get_rect(center=position)
        self.speed = 10
        self.velocity = pygame.Vector2(0, 0)

    def apply_force(self, force: tuple[float, float] | list[float, float] | pygame.Vector2):
        self.velocity += force

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position

    def render(self, surface):
        surface.blit(self.image, self.rect)
































