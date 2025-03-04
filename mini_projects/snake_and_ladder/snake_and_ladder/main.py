from .game import Game
from .enums import InputType

def main() -> None:
    command = int(input("Enter type of board input: \n 1=COMMANDLINE \n 2=FILE \n").strip())
    if command!=2 and command!=1: print("Invalid Input")

    new_game = Game(InputType(command-1))
    new_game.play_game()
