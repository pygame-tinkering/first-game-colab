
import pygame

class Bullet:
    def __init__(self, position):
        self.image = pygame.Surface((10, 10))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=position)

    def update(self):
        pass

    def render(self, surface):
        surface.blit(self.image, self.rect)
































