
import pygame
from src import Settings

def main():
    pygame.init()
    settings = Settings()

    pygame.display.set_caption(settings.caption)
    pygame.display.set_mode(
        size=settings.resolution,
        flags=settings.flags,
        depth=0,
        display=0,
        vsync=0,
    )

    from src import Game
    game = Game(settings)
    game.run()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()

