
from abc import ABC
from types import SimpleNamespace

class Controller(ABC):
    def __init__(self):
        self.direction = SimpleNamespace(**{direction: False for direction in ['up', 'down', 'left', 'right']})
        self.roll = False































