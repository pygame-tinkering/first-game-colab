


from ..ui import UI
from src.singleton import Singleton

class UIManager(Singleton):
    def __init__(self):
        self.elements = []

    def add(self, element: UI):
        self.elements.append(element)

    def get_elements(self) -> list:
        return self.elements





























