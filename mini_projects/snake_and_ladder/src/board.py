from .snake_or_ladder import SnakeOrLadder
from .snake_or_ladder_factory import SnakeOrLadderFactory
from .enums import BoardEntityType

class Board:
    __maxPosition: int=None
    __snakesAndLadders: dict[int, SnakeOrLadder]={}

    def __init__(self, maxPosition: int, snakeAndLadders: list[tuple[int,int,BoardEntityType]]) -> None:
        self.__maxPosition=maxPosition
        self.__addSnakeOrLadder(snakeAndLadders)

    def __addSnakeOrLadder(self, snakeAndLadders: list[tuple[int,int,BoardEntityType]]) -> None:
        snakeOrLadderCreator = SnakeOrLadderFactory()

        for entity in snakeAndLadders:
            snakeOrLadder = snakeOrLadderCreator.createSnakeOrLadder(entity[0],entity[1],entity[2])
            if snakeOrLadder:
                self.__snakesAndLadders[snakeOrLadder.getStart()] = snakeOrLadder
            else:
                print("Error: Cannot initialise the following: ", entity)
        return
    
    def getNewPosition(self, position: int, roll: int) -> int:
        if position+roll>self.__maxPosition: 
           return position
        newPosition = position+roll
        while(newPosition in self.__snakesAndLadders.keys()):
            if self.__snakesAndLadders[newPosition].getType()==BoardEntityType.SNAKE:
                print("Hissssssss")
            elif self.__snakesAndLadders[newPosition].getType()==BoardEntityType.LADDER:
                print("tuk tuk tuk tuk")
            newPosition=self.__snakesAndLadders[newPosition].getEnd()
        return newPosition