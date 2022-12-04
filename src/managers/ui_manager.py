


from ..ui import UI
from .manager import Manager

class UIManager(Manager):
    def __init__(self):
        self.elements = []

    def add(self, element: UI):
        self.elements.append(element)






























