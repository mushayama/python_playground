from src.game import Game
from src.enums import InputType

def __main__():
    newGame = Game(InputType.COMMANDLINE)
    newGame.playGame()

__main__()