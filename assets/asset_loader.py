


from paths import CHARACTER_SPRITE_PATH, CHARACTER_DATA_PATH


class AssetLoader:
    def __init__(self):
        #self.fonts = {}  # May not need
        self.images = {}
        self.musics = {}
        self.sounds = {}

    def reset(self):
        #self.fonts = {}
        self.images = {}
        self.musics = {}
        self.sounds = {}

    def load(self, scene: str = 'game'):
        self.images.update({'character': [CHARACTER_SPRITE_PATH, CHARACTER_DATA_PATH]})
































