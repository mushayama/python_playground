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

    def __init__(self, inputType: InputType, filepath: str= "") -> None:
        self.__dices.append(Dice(self.__DICE_FACES))
        self.__createGame(inputType, filepath)

    def __createGame(self, inputType: InputType, filepath: str=""):
        if inputType==InputType.COMMANDLINE:
            self.__createGameFromCommandLine()
        elif inputType==InputType.FILE:
            self.__createGameFromFile(filepath)

    def __createGameFromCommandLine(self) -> None:
        numberOfSnakes=int(input("Enter number of snakes: ").strip())
        snakesAndLadders=[]
        for i in range(1,numberOfSnakes+1):
            command = input("Enter "+str(i)+" snake: ").strip().split()
            snakesAndLadders.append((int(command[0]), int(command[1]), BoardEntityType.SNAKE))

        numberOfLadders=int(input("Enter number of ladders: ").strip())
        for i in range(1,numberOfLadders+1):
            command = input("Enter "+str(i)+" ladder: ").strip().split()
            snakesAndLadders.append((int(command[0]), int(command[1]), BoardEntityType.LADDER))
        
        self.__board = Board(self.__MAX_POSITION, snakesAndLadders)

        numberOfPlayers=int(input("Enter number of players: ").strip())
        for i in range(1,numberOfPlayers+1):
            command = input("Enter "+str(i)+" player name: ").strip()
            self.__players.put(Player(command))
    
    def __createGameFromFile(self, filepath: str="") -> None:
        if filepath=="":
            path = Path(__file__).parent / "../assets/board.txt"
        else: path = Path(filepath)
        with path.open("r") as file:
            lines = file.readlines()
            i=0;
            snakesAndLadders=[]

            numberOfSnakes=int(lines[i].strip())
            i+=1
            for _ in range(numberOfSnakes):
                command = lines[i].strip().split()
                i+=1
                snakesAndLadders.append((int(command[0]), int(command[1]), BoardEntityType.SNAKE))

            numberOfLadders=int(lines[i].strip())
            i+=1
            for _ in range(numberOfLadders):
                command = lines[i].strip().split()
                i+=1
                snakesAndLadders.append((int(command[0]), int(command[1]), BoardEntityType.LADDER))
            
            self.__board = Board(self.__MAX_POSITION, snakesAndLadders)

            numberOfPlayers = int(lines[i].strip())
            i+=1
            for _ in range(numberOfPlayers):
                self.__players.put(Player(lines[i].strip()))
                i+=1
    
    def playGame(self) -> None:
        ranking = 1
        while(self.__players.qsize()>1):
            player = self.__players.get()
            roll = self.__getRoll()
            
            newPosition = self.__board.getNewPosition(player.getPosition(), roll)

            if newPosition==self.__MAX_POSITION:
                print(player.getName()+" has reached the end with roll "+str(roll)+" and gets "+str(ranking)+" rank")
                ranking+=1
            else:
                print(player.getName()+" has rolled "+str(roll)+" and reached "+str(newPosition)+" from "+str(player.getPosition()))
                player.setPosition(newPosition)
                self.__players.put(player)
        print("Game ends")
        return None
    
    def __getRoll(self) -> int:
        roll=0
        maxRoll = 0
        for dice in self.__dices:
            maxRoll+=dice.getSides()
            roll+=dice.getRoll()
        
        rollCount=1
        while roll%maxRoll==0 and rollCount<3:
            for dice in self.__dices:
                roll+=dice.getRoll()
                rollCount+=1
        
        if roll==3*maxRoll:
            roll=0
        
        return roll


            
