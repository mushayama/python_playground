from .enums import BoardEntityType
from abc import ABC, abstractmethod

class SnakeOrLadder(ABC):
    _start: int=None
    _end: int=None
    _type: BoardEntityType=None

    def __init__(self, start: int, end: int, type: BoardEntityType) -> None:
        self._start=start
        self._end=end
        self._type=type

    @abstractmethod
    def get_type(self) -> BoardEntityType:
        pass

    @abstractmethod
    def get_start(self) -> int:
        pass

    @abstractmethod
    def get_end(self) -> int:
        pass