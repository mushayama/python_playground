import unittest
from ..src.board import Board
from ..src.enums import BoardEntityType

'''
Run command:
python3 -m unittest mini_projects/snake_and_ladder/tests/test_snake_and_ladder.py
from appropriate directory ofc
'''

class TestSnakeAndLAdder(unittest.TestCase):
    def test_Board(self):
        snakesAndLadders = [
            (81, 100, BoardEntityType.LADDER),
            (11, 20, BoardEntityType.LADDER),
            (99, 6, BoardEntityType.SNAKE),
            (50, 12, BoardEntityType.SNAKE)
        ]
        board = Board(100, snakesAndLadders)

        self.assertEqual(board.getMaxPosition(), 100)
        self.maxDiff=None
        bSnakesAndLadders = board.getSnakesAndLadders()
        self.assertEqual(len(snakesAndLadders),4)
        for i in range(4):
            self.assertTrue(snakesAndLadders[i][0] in bSnakesAndLadders.keys())
            self.assertEqual(bSnakesAndLadders[snakesAndLadders[i][0]].getEnd(), snakesAndLadders[i][1])
            self.assertEqual(bSnakesAndLadders[snakesAndLadders[i][0]].getType(), snakesAndLadders[i][2])
        
        self.assertEqual(board.getNewPosition(10, 3), 13)
        self.assertEqual(board.getNewPosition(98, 3), 98)
        self.assertEqual(board.getNewPosition(97, 3), 100)
        self.assertEqual(board.getNewPosition(10, 1), 20)
        self.assertEqual(board.getNewPosition(98, 1), 6)

    
