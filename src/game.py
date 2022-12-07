
import pygame

from .settings import Settings
from .managers import EventManager, \
    RenderManager, \
    UpdateManager, \
    UIManager, \
    ObjectManager, \
    AudioManager
from .control import MouseKeyboard
from .ui import Button
from .ui import Font

class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.get_surface()
        self.running = True
        self.event_manager = EventManager()
        self.render_manager = RenderManager()
        self.update_manager = UpdateManager()
        self.ui_manager = UIManager()
        self.audio_manager = AudioManager()
        self.object_manager = ObjectManager()

        self.audio_manager.play_music('None')

        self._create_entities()
        self._create_ui()
        self._register_events()

    def _create_entities(self):
        self.object_manager.create(
            sheet_name='character',
            position=(self.settings.width // 2, self.settings.height // 2),
            control=self.settings.controller.value,
            frame_rate=1,
        )
        self.object_manager.create(
            sheet_name='character',
            position=(120, self.settings.height // 2),
            control=None,
            frame_rate=1,
        )
        self.object_manager.create(
            sheet_name='character',
            position=(500, 100),
            control=None,
            frame_rate=1,
        )

    def _create_ui(self):
        self.ui_manager.add(
            Button(
                size=(150,50),
                position=(100, 50),
                bg_color='red',
                fg_color='white',
                font=Font(
                    name=self.settings.font_name,
                    size=24,
                    text='Button'
                )
            )
        )

    def _register_events(self):
        self.event_manager.subscribe(pygame.QUIT,
                                     self, lambda event: self._quit(event)
                                     )
        controlled_entities = (
            entity
            for group in self.object_manager.get_objects()
            for entity in group
            if entity.control
        )
        for entity in controlled_entities:
            if isinstance(entity.control, MouseKeyboard):
                self.event_manager.subscribe([pygame.KEYDOWN,
                                              pygame.KEYUP],
                                             entity,
                                             lambda event: entity.control.keyboard(event))
                self.event_manager.subscribe([pygame.MOUSEBUTTONDOWN,
                                              pygame.MOUSEBUTTONUP,
                                              pygame.MOUSEMOTION,
                                              pygame.MOUSEWHEEL],
                                             entity,
                                             lambda event: entity.control.mouse(event))

    def _quit(self, event: int = None) -> None:
        self.running = False

    def run(self) -> None:
        while self.running:
            self.event_manager.notify(pygame.event.get())
            self.object_manager.update()
            self.update_manager.update(self.object_manager.get_objects() + self.ui_manager.get_elements())
            self.render_manager.render(self.screen, self.object_manager.get_objects() + self.ui_manager.get_elements())

































