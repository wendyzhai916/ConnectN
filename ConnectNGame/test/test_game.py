import unittest
from ConnectNGame.src.game import Game
from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player


class TestGame(unittest.TestCase):
    """def test_something(self):
        self.assertEqual(True, False)"""

    def test_check_horizontal(self):
        test_board = [
            ["x", "x", "x", "x"],
            ["x", "o", "o", "o"],
            ["x", "x", "x", "x"]
        ]
        self.assertTrue(Game.check_horizontal(3, 4, "o", 3, test_board))


if __name__ == '__main__':
    unittest.main()
