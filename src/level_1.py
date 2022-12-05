import pygame 
from .player import Player

class Level:
	def __init__(self, game):
		self.gameObject = game
		# get the display surface
		self.display_surface = pygame.display.get_surface()
		self.background = pygame.image.load("./assets/images/background/bg.png").convert_alpha()
		# print(self.gameObject.settings)
		self.background= pygame.transform.scale(self.background, (self.gameObject.screen.get_width(), self.gameObject.screen.get_height()))
		# sprite groups
		self.all_sprites = pygame.sprite.Group()

		self.setup()

	def setup(self):
		self.player = Player((340,360), self.all_sprites, self)

	def run(self):
		self.display_surface.fill('black')
		self.display_surface.blit(self.background, (0, 0))
		self.all_sprites.update()
		self.all_sprites.draw(self.display_surface)
