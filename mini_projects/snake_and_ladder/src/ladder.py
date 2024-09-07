from .enums import BoardEntityType
from .snake_or_ladder import SnakeOrLadder

class Ladder(SnakeOrLadder):
    def __init__(self, start: int, end: int) -> None:
        super().__init__(start, end, BoardEntityType.LADDER)

    def getEnd(self) -> int:
        return self._end;

    def getType(self) -> BoardEntityType:
        return self._type
    
    def getStart(self) -> int:
        return self._start