import unittest
from ConnectNGame.src.game import Game
from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player


class TestGame(unittest.TestCase):
    """def test_something(self):
        self.assertEqual(True, False)"""

    def test_check_horizontal_true(self):
        test_board_1 = [
            ["x", "x", "x", "x"],
            ["x", "o", "o", "o"],
            ["x", "x", "x", "x"]
        ]
        self.assertTrue(Game.check_horizontal(3, 4, "o", 3, test_board_1))

    def test_check_horizontal_false(self):
        test_board_2 = [
            ["1", "1", "1", "1", "1"],
            ["1", "x", "1", "1", "1"],
            ["1", "1", "x", "x", "1"],
            ["1", "1", "1", "1", "1"],
            ["x", "x", "x", "1", "1"],
            ["x", "x", "1", "x", "1"]
        ]

        self.assertFalse(Game.check_horizontal(6, 5, "x", 4, test_board_2))


if __name__ == '__main__':
    unittest.main()
