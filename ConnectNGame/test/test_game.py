import unittest
from ConnectNGame.src.game import Game
from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player


class TestGame(unittest.TestCase):

    def test_check_tie_true(self):

        test_board_1 = [
            ["x", "o", "x", "x"],
            ["x", "o", "o", "o"],
            ["x", "x", "x", "x"]
        ]
        self.assertTrue(Game.check_tie(test_board_1, "1"))

        test_board_2 = [
            ["x", "1", "x", "1", "1"],
            ["1", "x", "1", "1", "x"],
            ["1", "1", "x", "x", "1"],
            ["1", "1", "1", "1", "1"],
            ["x", "x", "x", "x", "1"],
            ["x", "x", "1", "x", "x"]]

        self.assertTrue(Game.check_tie(test_board_2, "0"))

    def test_check_tie_false(self):

        test_board_1 = [
            ["x", "1", "x", "x"],
            ["x", "o", "o", "o"],
            ["x", "x", "x", "x"]
        ]
        self.assertFalse(Game.check_tie(test_board_1, "1"))

        test_board_2 = [
            ["x", "1", "x", "0", "1"],
            ["1", "x", "1", "1", "x"],
            ["1", "1", "x", "x", "1"],
            ["1", "1", "1", "1", "1"],
            ["x", "x", "x", "x", "1"],
            ["x", "x", "1", "x", "x"]]

        self.assertFalse(Game.check_tie(test_board_2, "0"))

    def test_check_horizontal_true(self):

        test_board_1 = [
            ["x", "x", "x", "x"],
            ["x", "o", "o", "o"],
            ["x", "x", "x", "x"]
        ]

        self.assertTrue(Game.check_horizontal(3, 4, "o", 3, test_board_1))

        test_board_2 = [
            ["1", "1", "1", "1", "1"],
            ["1", "x", "1", "1", "1"],
            ["1", "1", "x", "x", "1"],
            ["1", "1", "1", "1", "1"],
            ["x", "x", "x", "x", "1"],
            ["x", "x", "1", "x", "1"]
        ]

        self.assertTrue(Game.check_horizontal(6, 5, "x", 4, test_board_2))

    def test_check_horizontal_false(self):

        test_board_a = [
            ["2", "1", "&"],
            ["2", "1", "2"],
            ["1", "2", "1"]
        ]

        self.assertFalse(Game.check_horizontal(3, 3, "2", 3, test_board_a))  # PASSES

        test_board_1 = [
            ["x", "x", "x", "x"],
            ["x", "o", "o", "x"],
            ["x", "x", "x", "x"]
        ]

        self.assertFalse(Game.check_horizontal(3, 4, "o", 3, test_board_1))

        test_board_2 = [
            ["1", "1", "1", "1", "1"],
            ["1", "x", "1", "1", "1"],
            ["1", "1", "x", "x", "1"],
            ["1", "1", "1", "1", "1"],
            ["x", "x", "x", "1", "1"],
            ["x", "x", "1", "x", "1"]
        ]

        self.assertFalse(Game.check_horizontal(6, 5, "x", 4, test_board_2))

    def test_check_vertical_true(self):
        test_board_1 = [
            ["x", "x", "o", "x"],
            ["x", "x", "o", "x"],
            ["x", "x", "o", "x"]
        ]

        self.assertTrue(Game.check_vertical(3, 4, "o", 3, test_board_1))

        test_board_2 = [
            ["1", "1", "1", "1", "1"],
            ["1", "x", "x", "1", "1"],
            ["1", "x", "x", "1", "1"],
            ["1", "x", "x", "1", "1"],
            ["x", "1", "x", "1", "1"],
            ["x", "1", "1", "1", "1"]
        ]

        self.assertTrue(Game.check_vertical(6, 5, "x", 4, test_board_2))

    def test_check_vertical_false(self):

        test_board_a = [
            ["2", "1", "&"],
            ["2", "1", "2"],
            ["1", "2", "1"]
        ]

        self.assertFalse(Game.check_vertical(3, 3, "2", 3, test_board_a))  # PASSES

        test_board_1 = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["x", "o", "x"]
        ]

        self.assertFalse(Game.check_vertical(3, 3, "o", 3, test_board_1))

        test_board_2 = [
            ["1", "1", "1", "1", "x"],
            ["1", "x", "1", "1", "x"],
            ["1", "1", "x", "x", "1"],
            ["1", "1", "1", "1", "1"],
            ["x", "x", "x", "1", "1"],
            ["x", "x", "1", "x", "1"]
        ]

        self.assertFalse(Game.check_vertical(6, 5, "x", 4, test_board_2))

    def test_check_neg_diagonal_true(self):


        test_board_1 = [
            ["x", "o", "x", "x"],
            ["x", "x", "o", "x"],
            ["x", "x", "x", "o"]
        ]

        self.assertTrue(Game.check_neg_diagonal(3, 4, "o", 3, test_board_1))

        test_board_2 = [
            ["1", "1", "x", "1", "1"],
            ["1", "x", "1", "x", "1"],
            ["x", "1", "x", "1", "1"],
            ["1", "x", "1", "1", "1"],
            ["x", "x", "x", "1", "x"],
            ["1", "x", "1", "x", "1"]
        ]

        self.assertTrue(Game.check_neg_diagonal(6, 5, "x", 4, test_board_2))

    def test_check_neg_diagonal_false(self):

        test_board_a = [
            ["2", "1", "&"],
            ["2", "1", "2"],
            ["1", "2", "1"]
        ]

        self.assertFalse(Game.check_neg_diagonal(3, 3, "2", 3, test_board_a))  # PASSES

        test_board_1 = [
            ["x", "x", "o", "x"],
            ["x", "o", "o", "x"],
            ["x", "o", "x", "x"]
        ]

        self.assertFalse(Game.check_neg_diagonal(3, 4, "o", 3, test_board_1))

        test_board_2 = [
            ["1", "1", "1", "1", "x"],
            ["1", "1", "1", "1", "x"],
            ["1", "1", "x", "x", "1"],
            ["1", "x", "x", "1", "1"],
            ["1", "x", "x", "1", "1"],
            ["x", "x", "1", "x", "1"]
        ]

        self.assertFalse(Game.check_neg_diagonal(6, 5, "x", 4, test_board_2))

    def test_check_pos_diagonal_true(self):
        test_board_1 = [
            ["x", "x", "x", "o"],
            ["x", "x", "o", "x"],
            ["x", "o", "x", "x"]
        ]

        self.assertTrue(Game.check_pos_diagonal(3, 4, "o", 3, test_board_1))

        test_board_2 = [
            ["1", "1", "x", "1", "1"],
            ["1", "1", "1", "x", "1"],
            ["x", "1", "1", "1", "x"],
            ["1", "1", "1", "x", "1"],
            ["x", "1", "x", "1", "x"],
            ["1", "x", "1", "1", "1"]
        ]

        self.assertTrue(Game.check_pos_diagonal(6, 5, "x", 4, test_board_2))

    def test_check_pos_diagonal_false(self):

        test_board_a = [
            ["2", "1", "&"],
            ["2", "1", "2"],
            ["1", "2", "1"]
        ]

        self.assertFalse(Game.check_pos_diagonal(3, 3, "2", 3, test_board_a))  # this was the problem but fixed

        test_board_1 = [
            ["x", "o", "x", "o"],
            ["o", "x", "x", "x"],
            ["x", "o", "x", "x"]
        ]

        self.assertFalse(Game.check_pos_diagonal(3, 4, "o", 3, test_board_1))

        test_board_2 = [
            ["1", "1", "x", "1", "1"],
            ["1", "1", "1", "x", "1"],
            ["x", "1", "1", "1", "x"],
            ["1", "1", "1", "x", "1"],
            ["x", "1", "x", "1", "x"],
            ["1", "1", "1", "1", "1"]
        ]

        self.assertFalse(Game.check_pos_diagonal(6, 5, "x", 4, test_board_2))

if __name__ == '__main__':
    unittest.main()
