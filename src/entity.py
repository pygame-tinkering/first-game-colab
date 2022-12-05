import pygame
import math

# Will expand upon this class when I get the time


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, image, group) -> None:
        super().__init__(group)
        self.image = image
        self.rect = image.get_rect(center=pos)
        
        self.health = 100
        self.maxHealth = 100
        self.regenPerSecond = 10
        self.regenDelayAfterHit = 3 # How many seconds after you've been damaged can you start regenerating health

    def handleDamage(self, dmg) -> None:
        self.health -= dmg
        if self.health <= 0:
            self.handleDeath()

    def handleDeath(self) -> None:
        raise NotImplementedError('handleDeath must be overridden')
    
    def handleRegen(self) -> None:
        pass # @TODO: Implement regen behaviour

    def update(self) -> None:
        self.handleRegen()