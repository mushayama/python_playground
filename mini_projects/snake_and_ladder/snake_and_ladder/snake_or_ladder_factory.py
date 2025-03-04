from .enums import BoardEntityType
from .snake_or_ladder import SnakeOrLadder
from .snake import Snake
from .ladder import Ladder
from typing import Optional

class SnakeOrLadderFactory:
    def __init__(self) -> None:
        pass

    def create_snake_or_ladder(self, start:int, end:int, type: BoardEntityType) -> Optional[SnakeOrLadder]:
        if type==BoardEntityType.LADDER:
            return Ladder(start,end)
        elif type==BoardEntityType.SNAKE:
            return Snake(start,end)
        return None