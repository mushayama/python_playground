import unittest
from snake_and_ladder.board import Board
from ..enums import BoardEntityType

'''
Run command:
python3 -m unittest mini_projects/snake_and_ladder/tests/test_snake_and_ladder.py
from appropriate directory ofc
'''

class TestSnakeAndLadder(unittest.TestCase):
    def test_board(self):
        snakes_and_ladders = [
            (81, 100, BoardEntityType.LADDER),
            (11, 20, BoardEntityType.LADDER),
            (99, 6, BoardEntityType.SNAKE),
            (50, 12, BoardEntityType.SNAKE)
        ]
        board = Board(100, snakes_and_ladders)

        self.assertEqual(board.get_max_position(), 100)
        self.maxDiff=None
        snakes_and_ladders_on_board = board.get_snakes_and_ladders()
        self.assertEqual(len(snakes_and_ladders),4)
        for i in range(4):
            self.assertTrue(snakes_and_ladders[i][0] in snakes_and_ladders_on_board.keys())
            self.assertEqual(snakes_and_ladders_on_board[snakes_and_ladders[i][0]].get_end(), snakes_and_ladders[i][1])
            self.assertEqual(snakes_and_ladders_on_board[snakes_and_ladders[i][0]].get_type(), snakes_and_ladders[i][2])

        self.assertEqual(board.get_new_position(10, 3), 13)
        self.assertEqual(board.get_new_position(98, 3), 98)
        self.assertEqual(board.get_new_position(97, 3), 100)
        self.assertEqual(board.get_new_position(10, 1), 20)
        self.assertEqual(board.get_new_position(98, 1), 6)
