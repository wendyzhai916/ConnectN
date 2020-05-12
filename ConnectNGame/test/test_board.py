import unittest
from unittest.mock import patch
from .print_capturer import PrintCapturer
from ConnectNGame.src.board import Board


class TestBoard(unittest.TestCase):

    def test_repr_board(self): # test the repr function
        temp_board = Board( 3, 3, "*")
        ans_board = """  0 1 2\n0 * * *\n1 * * *\n2 * * *"""
        self.assertEqual(repr(temp_board), ans_board)

    def test_repr_board_multi(self):  # test with different row/col nums
        temp_board = Board(3, 2, "?")
        ans_board = """  0 1\n0 ? ?\n1 ? ?\n2 ? ?"""
        self.assertEqual(repr(temp_board), ans_board)

    def test_drop(self):
        test_board = Board(2, 2, "#")
        test_board.drop(0, "!")
        self.assertEqual(test_board.board_array[1][0], "!")
        test_board.drop(0, "!")
        self.assertEqual(test_board.board_array[0][0], "!")


if __name__ == '__main__':
    unittest.main()
