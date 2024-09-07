class Player:
    __name: str=None
    __position: int=None

    def __init__(self, name: str) -> None:
        self.__name=name
        self.__position=0
    
    def getName(self) -> str:
        return self.__name

    def getPosition(self) -> int:
        return self.__position
    
    def setPosition(self, position: int) -> None:
        self.__position = position
        return None