import pygame
from .settings import Settings
from .level_1 import Level

class Game:
    def __init__(self, settings: Settings):
        self.screen = pygame.display.get_surface()
        self.settings = settings
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = Level(self)
        self.frameEvents = []

    def handle_events(self) -> None:
        # events = pygame.event.get()
        self.frameEvents = pygame.event.get()
        for event in self.frameEvents:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.clock.tick(self.settings.frame_rate)
            self.level.run()
            pygame.display.flip()
































