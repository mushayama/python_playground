class Player:
    __name: str=None
    __position: int=None

    def __init__(self, name: str) -> None:
        self.__name=name
        self.__position=0

    def get_name(self) -> str:
        return self.__name

    def get_position(self) -> int:
        return self.__position

    def set_position(self, position: int) -> None:
        self.__position = position
        return None