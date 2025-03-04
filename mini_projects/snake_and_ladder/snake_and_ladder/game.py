from .board import Board
from .dice import Dice
from .player import Player
from .enums import InputType, BoardEntityType
from queue import Queue
from pathlib import Path

class Game:
    __board: Board= None
    __dices: list[Dice]=[]
    __players: Queue[Player]=Queue()
    __MAX_POSITION = 100
    __DICE_FACES = 6

    def __init__(self, input_type: InputType, filepath: str= "") -> None:
        self.__dices.append(Dice(self.__DICE_FACES))
        self.__create_game(input_type, filepath)

    def __create_game(self, input_type: InputType, filepath: str=""):
        if input_type==InputType.COMMANDLINE:
            self.__create_game_from_command_line()
        elif input_type==InputType.FILE:
            self.__create_game_from_file(filepath)

    def __create_game_from_command_line(self) -> None:
        number_of_snakes=int(input("Enter number of snakes: ").strip())
        snakes_and_ladders=[]
        for i in range(1,number_of_snakes+1):
            command = input("Enter "+str(i)+" snake: ").strip().split()
            snakes_and_ladders.append((int(command[0]), int(command[1]), BoardEntityType.SNAKE))

        number_of_ladders=int(input("Enter number of ladders: ").strip())
        for i in range(1,number_of_ladders+1):
            command = input("Enter "+str(i)+" ladder: ").strip().split()
            snakes_and_ladders.append((int(command[0]), int(command[1]), BoardEntityType.LADDER))

        self.__board = Board(self.__MAX_POSITION, snakes_and_ladders)

        number_of_players=int(input("Enter number of players: ").strip())
        for i in range(1,number_of_players+1):
            command = input("Enter "+str(i)+" player name: ").strip()
            self.__players.put(Player(command))

    def __create_game_from_file(self, filepath: str="") -> None:
        if filepath=="":
            path = Path(__file__).parent / "../assets/board.txt"
        else: path = Path(filepath)
        with path.open("r") as file:
            lines = file.readlines()
            i=0;
            snakes_and_ladders=[]

            number_of_snakes=int(lines[i].strip())
            i+=1
            for _ in range(number_of_snakes):
                command = lines[i].strip().split()
                i+=1
                snakes_and_ladders.append((int(command[0]), int(command[1]), BoardEntityType.SNAKE))

            number_of_ladders=int(lines[i].strip())
            i+=1
            for _ in range(number_of_ladders):
                command = lines[i].strip().split()
                i+=1
                snakes_and_ladders.append((int(command[0]), int(command[1]), BoardEntityType.LADDER))

            self.__board = Board(self.__MAX_POSITION, snakes_and_ladders)

            number_of_players = int(lines[i].strip())
            i+=1
            for _ in range(number_of_players):
                self.__players.put(Player(lines[i].strip()))
                i+=1

    def play_game(self) -> None:
        ranking = 1
        while(self.__players.qsize()>1):
            player = self.__players.get()
            roll = self.__get_roll()

            new_position = self.__board.get_new_position(player.get_position(), roll)

            if new_position==self.__MAX_POSITION:
                print(player.get_name()+" has reached the end with roll "+str(roll)+" and gets "+str(ranking)+" rank")
                ranking+=1
            else:
                print(player.get_name()+" has rolled "+str(roll)+" and reached "+str(new_position)+" from "+str(player.get_position()))
                player.set_position(new_position)
                self.__players.put(player)
        print("Game ends")
        return None

    def __get_roll(self) -> int:
        roll=0
        max_roll = 0
        for dice in self.__dices:
            max_roll+=dice.get_sides()
            roll+=dice.get_roll()

        roll_count=1
        while roll%max_roll==0 and roll_count<3:
            for dice in self.__dices:
                roll+=dice.get_roll()
                roll_count+=1

        if roll==3*max_roll:
            roll=0

        return roll
