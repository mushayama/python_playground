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
    def getType(self) -> BoardEntityType:
        pass
    
    @abstractmethod
    def getStart(self) -> int:
        pass
    
    @abstractmethod
    def getEnd(self) -> int:
        pass