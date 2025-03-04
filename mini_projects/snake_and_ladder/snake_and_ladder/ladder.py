from .enums import BoardEntityType
from .snake_or_ladder import SnakeOrLadder

class Ladder(SnakeOrLadder):
    def __init__(self, start: int, end: int) -> None:
        super().__init__(start, end, BoardEntityType.LADDER)

    def get_end(self) -> int:
        return self._end;

    def get_type(self) -> BoardEntityType:
        return self._type

    def get_start(self) -> int:
        return self._start