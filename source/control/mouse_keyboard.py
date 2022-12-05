
import pygame
from .controller import Controller

class MouseKeyboard(Controller):
    def keyboard(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                self.direction.up = True
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                self.direction.down = True
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                self.direction.left = True
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                self.direction.right = True
            if event.key in [pygame.K_SPACE]:
                self.roll = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_w]:
                self.direction.up = False
            if event.key in [pygame.K_DOWN, pygame.K_s]:
                self.direction.down = False
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                self.direction.left = False
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                self.direction.right = False
            if event.key in [pygame.K_SPACE]:
                self.roll = False

    def mouse(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            left, middle, right = event.buttons
        elif event.type == pygame.MOUSEWHEEL:
            pass
        else:
            button = event.button


































