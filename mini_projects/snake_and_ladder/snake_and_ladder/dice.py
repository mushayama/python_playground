from random import randint

class Dice:
    __sides: int = None

    def __init__(self, sides: int) -> None:
        self.__sides = sides

    def get_roll(self) -> int:
        return randint(1, self.__sides)

    def get_sides(self) ->int:
        return self.__sides