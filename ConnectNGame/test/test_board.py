import unittest
from unittest.mock import patch
from .print_capturer import PrintCapturer
from ConnectNGame.src.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        test_board = Board(2, 2, "#")

    def test_repr(self):
        capture = PrintCapturer()
        with patch('ConnectNGame.src.board.print', side_effect=capture):  # TODO: in general how does test print work in general
            print(repr(test_board))  # FIXME: how does setUp work????
            self.assertEqual([''], capture.output)

    def test_drop(self):
        test_board.drop(0, "!")
        self.assertEqual(test_board.board_array[1][0], "!")




if __name__ == '__main__':
    unittest.main()
