from .entity import Entity
import pygame
import math


class Bullet(Entity):
    def __init__(self, pos, group, rotation):
        super().__init__(
            pos,
            pygame.image.load('./assets/images/projectiles/tile_0000.png').convert(),
            group
        )
        self.angleDirection = rotation
        self.rot_center(-rotation-90)
        self.image.set_colorkey((255, 255, 255))

        self.lifespan = 180 # frames, just for now
        self.life = 0

        self.speed = 10
        
    
    def update(self):
        self.life += 1
        if self.life >= self.lifespan:
            self.killSelf()
        
        self.move()
    
    def move(self):
        moveDirection = math.radians(self.angleDirection)

        self.pos.x += self.speed*math.cos(moveDirection)
        self.rect.centerx = self.pos.x

        self.pos.y += self.speed*math.sin(moveDirection)
        self.rect.centery = self.pos.y


    
    def killSelf(self):
        self.groups()[0].remove(self)



    def rot_center(self, angle):
        """rotate an image while keeping its center"""
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)