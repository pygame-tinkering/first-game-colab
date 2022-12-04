
from typing import Iterable, Callable
from .manager import Manager

class EventManager(Manager):
    def __init__(self):
        self.subscribers = {}
        self.registered_events = {}

    def reset(self):
        self.subscribers = {}
        self.registered_events = {}

    def notify(self, events):
        for event in events:
            if self.registered_events.get(event.type):
                self.alert(event)

    def alert(self, event):
        subscribers = self.subscribers.get(event.type)
        for func in subscribers.values():
            func(event)

    def _add_event(self, event_type: int, obj: object, func: Callable):
        event = self.subscribers.get(event_type)
        if event:
            event.update({obj: func})
        else:
            self.subscribers.update({event_type: {obj: func}})
        self.registered_events.update({event_type: True})

    def subscribe(self, event_types: Iterable | int, obj: object, func: Callable) -> None:
        if isinstance(event_types, Iterable):
            for event_type in event_types:
                self._add_event(event_type, obj, func)
        else:
            self._add_event(event_types, obj, func)

    def unsubscribe(self, event_type: int, obj: object) -> None:
        subscribers = self.subscribers.get(event_type)
        if subscribers:
            subscribers.pop(obj, None)
            subscribers = self.subscribers.get(event_type)
            if not subscribers:
                self.registered_events.pop(event_type, None)






























