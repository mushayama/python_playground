from enum import Enum

class InputType(Enum):
    FILE = 1
    COMMANDLINE = 0

class BoardEntityType(Enum):
    SNAKE = 0
    LADDER = 1