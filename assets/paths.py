

import os



def font_path(file_name):
    return os.path.join(FONTS_DIR, file_name)

def image_path(file_name):
    return os.path.join(IMAGE_DIR, file_name)

def musics_path(file_name):
    return os.path.join(MUSICS_DIR, file_name)

def sounds_path(file_name):
    return os.path.join(SOUNDS_DIR, file_name)

def get_fonts() -> dict:
    fonts = {}
    files = os.listdir(FONTS_DIR)

    for file in files:
        name, extension = file.rsplit('.')
        if extension.lower() in ['otf', 'ttf']:
            fonts.update({name.lower(): font_path(file)})
    return fonts

ASSETS_DIR = os.path.abspath(os.path.dirname(__file__))
FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')
IMAGE_DIR = os.path.join(ASSETS_DIR, 'images')
MUSICS_DIR = os.path.join(ASSETS_DIR, 'musics')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')

# FONTS
FONTS = get_fonts()

# SPRITE and SPRITE_DATA
CHARACTER_SPRITE_PATH = image_path('character.png')
CHARACTER_DATA_PATH = image_path('character.txt')


# MUSICS
TEST_MUSIC = musics_path('Retro Music - ABMU - ChipWave 01.wav')

# SOUNDS
TEST_SHOOT_SFX = sounds_path('Retro Gun SingleShot 04.wav')
























