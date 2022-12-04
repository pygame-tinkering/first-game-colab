
from typing import Self

class Manager:
    def __new__(cls) -> Self:
        if not hasattr(cls, 'instance'):
            cls.instance = super(type(cls), cls).__new__(cls)
        return cls.instance

































