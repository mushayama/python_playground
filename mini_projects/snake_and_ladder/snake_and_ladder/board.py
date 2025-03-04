from .snake_or_ladder import SnakeOrLadder
from .snake_or_ladder_factory import SnakeOrLadderFactory
from .enums import BoardEntityType

class Board:
    __max_position: int=None
    __snakes_and_ladders: dict[int, SnakeOrLadder]={}

    def __init__(self, max_position: int, snake_and_ladders: list[tuple[int,int,BoardEntityType]]) -> None:
        self.__max_position=max_position
        self.__add_snake_or_ladder(snake_and_ladders)

    def __add_snake_or_ladder(self, snake_and_ladders: list[tuple[int,int,BoardEntityType]]) -> None:
        snake_or_ladder_creator = SnakeOrLadderFactory()

        for entity in snake_and_ladders:
            snake_or_ladder = snake_or_ladder_creator.create_snake_or_ladder(entity[0],entity[1],entity[2])
            if snake_or_ladder:
                self.__snakes_and_ladders[snake_or_ladder.get_start()] = snake_or_ladder
            else:
                print("Error: Cannot initialise the following: ", entity)
        return

    def get_max_position(self) -> int:
        return self.__max_position

    def get_snakes_and_ladders(self) -> dict[int, SnakeOrLadder]:
        return self.__snakes_and_ladders

    def get_new_position(self, position: int, roll: int) -> int:
        if position+roll>self.__max_position:
           return position
        new_position = position+roll
        while(new_position in self.__snakes_and_ladders.keys()):
            if self.__snakes_and_ladders[new_position].get_type()==BoardEntityType.SNAKE:
                print("Hissssssss")
            elif self.__snakes_and_ladders[new_position].get_type()==BoardEntityType.LADDER:
                print("tuk tuk tuk tuk")
            new_position=self.__snakes_and_ladders[new_position].get_end()
        return new_position