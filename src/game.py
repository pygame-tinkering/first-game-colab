
import pygame
from .settings import Settings

class Game:
    def __init__(self, settings: Settings):
        self.screen = pygame.display.get_surface()
        self.settings = settings
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self) -> None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.clock.tick(self.settings.frame_rate)

            pygame.display.flip()
































