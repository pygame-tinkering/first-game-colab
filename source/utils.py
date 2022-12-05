
import pygame


def get_center(surface: pygame.Surface, other_surface: pygame.Surface) -> tuple[int, int]:
    x = surface.get_width() // 2 - other_surface.get_width() // 2
    y = surface.get_height() // 2 - other_surface.get_height() // 2
    print(surface.get_size())
    print(other_surface.get_size())
    print(x, y)
    return x, y































