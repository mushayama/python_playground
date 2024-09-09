from src.game import Game
from src.enums import InputType

def __main__():
    command = int(input("Enter type of board input: \n 1=COMMANDLINE \n 2=FILE \n").strip())
    if command!=2 and command!=1: print("Invalid Input")
    
    newGame = Game(InputType(command-1))
    newGame.playGame()

__main__()