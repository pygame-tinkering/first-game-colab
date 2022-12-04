


from ..ui import UI
from src.singleton import Singleton

class UISingleton(Singleton):
    def __init__(self):
        self.elements = []

    def add(self, element: UI):
        self.elements.append(element)






























