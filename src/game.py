
import pygame


from .settings import Settings
from .entities import Entity
from .control import MouseKeyboard
from .managers import EventManager
from .managers import RenderManager
from .managers import UpdateManager
from .managers import UIManager
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
        self.player = Entity(
            position=(self.settings.width // 2, self.settings.height // 2),
            control=MouseKeyboard(),
            frame_rate=1,
        )
        self._create_ui()
        self._register_events()

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
        self.event_manager.subscribe([pygame.KEYDOWN,
                                      pygame.KEYUP],
                                     self.player,
                                     lambda event: self.player.control.keyboard(event))
        self.event_manager.subscribe([pygame.MOUSEBUTTONDOWN,
                                      pygame.MOUSEBUTTONUP,
                                      pygame.MOUSEMOTION,
                                      pygame.MOUSEWHEEL],
                                     self.player,
                                     lambda event: self.player.control.mouse(event))

    def _quit(self, event: int = None) -> None:
        self.running = False

    def run(self) -> None:
        while self.running:
            self.event_manager.notify(pygame.event.get())
            self.update_manager.update([self.player, self.ui_manager.elements])
            self.render_manager.render(self.screen, [self.player, self.ui_manager.elements])

































