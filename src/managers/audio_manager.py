
import pygame
from ..singleton import Singleton
from assets import TEST_MUSIC, TEST_SHOOT_SFX


class AudioManager(Singleton):
    def __init__(self):
        pygame.mixer.set_num_channels(999)

    def play_music(self, name: str):
        pygame.mixer.music.load(TEST_MUSIC)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

    def play_sound(self, name: str):
        channel = pygame.mixer.find_channel()
        shoot_sfx = pygame.mixer.Sound(TEST_SHOOT_SFX)
        shoot_sfx.set_volume(0.3)
        channel.play(shoot_sfx)





























