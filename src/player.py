import pygame
import math 
from .entity import Entity
from .bullet import Bullet


class Player(Entity):
	def __init__(self, pos, group, level):
		super().__init__(
			pos, 
			pygame.image.load(r".\assets\images\planes\ship_001.png").convert_alpha(),
		 	group
		)

		self.level = level

		# general setup
		self.image = pygame.transform.scale(self.image, (64,64))
		self.o_image = self.image

		# movement attributes
		self.inertia = 0 # 0.0 to 1.0
		self.drag = 0.02
		self.acceleration = 0.1
		self.speed = 7 

		self.angleDirection = 45
		self.angleChangeSpeed = 3

		# shooting attributes
		self.shotCooldown = 250 
		self.delayCounter = 0

	def input(self):
		keys = pygame.key.get_pressed()

		appliedAcceleration = False # False if the player didn't "move"

		if keys[pygame.K_w]:
			self.inertia += self.acceleration
			appliedAcceleration = True

		if self.inertia > 1:
			self.inertia = 1

		# Change the angle at which you're moving
		if keys[pygame.K_a]:
			self.angleDirection -= self.angleChangeSpeed
		if keys[pygame.K_d]:
			self.angleDirection += self.angleChangeSpeed

		# Apply drag if the player didn't move.
		if not appliedAcceleration:   
			self.inertia -= self.drag
			self.inertia = max(self.inertia, 0)
		
		if keys[pygame.K_SPACE]:
			self.shoot()

	def move(self):
		moveDirection = math.radians(self.angleDirection)

		self.pos.x += self.speed*math.cos(moveDirection) * self.inertia
		self.rect.centerx = self.pos.x
		
		self.pos.y += self.speed*math.sin(moveDirection) * self.inertia
		self.rect.centery = self.pos.y
		
		# Rotate visually
		self.rot_center(-self.angleDirection-90)

	def update(self):
		self.input()
		self.move()
		# self.shoot()

		super().update()

	def rot_center(self, angle):
		"""rotate an image while keeping its center"""
		self.image = pygame.transform.rotate(self.o_image, angle)
		self.rect = self.image.get_rect(center=self.rect.center)

	def shoot(self):
		self.delayCounter += self.level.gameObject.clock.get_time()
		if self.delayCounter > self.shotCooldown:
			b = Bullet(self.rect.center, self.level.all_sprites, self.angleDirection)
			self.delayCounter = 0 
					
