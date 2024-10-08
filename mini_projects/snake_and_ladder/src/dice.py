from random import randint

class Dice:
    __sides: int = None

    def __init__(self, sides: int) -> None:
        self.__sides = sides

    def getRoll(self) -> int:
        return randint(1, self.__sides)
    
    def getSides(self) ->int:
        return self.__sides