
import pygame
from src import Settings

def main():
    pygame.mixer.pre_init(
        frequency=44100,
        size=-16,
        channels=2,
        buffer=512,
        devicename=None,
        allowedchanges=pygame.AUDIO_ALLOW_FREQUENCY_CHANGE | pygame.AUDIO_ALLOW_CHANNELS_CHANGE
    )
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
    game = Game()
    game.run()
    pygame.quit()
    raise SystemExit


if __name__ == '__main__':
    main()

