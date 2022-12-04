import pygame
import math 


class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)

		# general setup
		self.image = pygame.image.load(r".\assets\images\planes\ship_001.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, (64,64))
		self.o_image = self.image
		self.rect = self.image.get_rect(center=pos)
		# self.image = rot_center(self.image, 45, self.rect.center[0], self.rect.center[1])
		# movement attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 5 
		self.facing_direct = 0
		##junk
		self.counter =0 

	def input(self):
		keys = pygame.key.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		# handle movement direction y axis
		if keys[pygame.K_w]:
			self.direction.y = -1
		elif keys[pygame.K_s]:
			self.direction.y = 1
		else:
			self.direction.y = 0
		# handle movement direction x axis
		if keys[pygame.K_d]:
			self.direction.x = 1
		elif keys[pygame.K_a]:
			self.direction.x = -1
		else:
			self.direction.x = 0
		# handle facing direction (should always face mouse pointer)
		self.facing_direct = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(self.rect.center)

	def move(self):
		# normalizing a vector 
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		# horizontal movement
		self.pos.x += self.direction.x * self.speed
		self.rect.centerx = self.pos.x

		# vertical movement
		self.pos.y += self.direction.y * self.speed
		self.rect.centery = self.pos.y

		# rotation
		self.rot_center(-(self.facing_direct.as_polar()[1]+90))

	def update(self):
		self.input()
		self.move()
		
		self.counter += 0.5

	def rot_center(self, angle):
		"""rotate an image while keeping its center"""
		self.image = pygame.transform.rotate(self.o_image, angle)
		self.rect = self.image.get_rect(center=self.rect.center)
		# return rot_image, rot_rect