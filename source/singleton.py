
from typing import Self

class Singleton:
    def __new__(cls) -> Self:
        if not hasattr(cls, '_instance'):
            cls._instance = super(type(cls), cls).__new__(cls)
        return cls._instance

































