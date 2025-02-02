

class Event:
    pass


class FatalEvent(Event):
    pass


class NonFatalEvent(Event):
    pass


class EventGroup:
    def __init__(self, events: list[Event]):
        pass
