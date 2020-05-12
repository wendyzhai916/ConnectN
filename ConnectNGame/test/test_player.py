import unittest
from ConnectNGame.src.game import Game
from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player
from unittest.mock import patch


class TestPlayer(unittest.TestCase):

    def test_create_one_player(self):
        player_list = [Player("mary", "!")]
        test_player = Player("joe", "w")
        user_input = ["joe", "w"]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            self.assertEqual(Player.create_one_player(2, player_list, "x"), test_player)

    def test_get_name_blank(self):
        player_list = [Player("mary", "!")]
        user_input = [" "]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with self.assertRaises(ValueError):
                Player.get_name(2, player_list)

    def test_get_name_same_name(self):
        player_list = [Player("mary", "!")]
        user_input = ["mary"]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with self.assertRaises(ValueError):
                Player.get_name(2, player_list)

        user_input = ["Mary"]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with self.assertRaises(ValueError):
                Player.get_name(2, player_list)

    def test_get_name_reg(self):
        player_list = [Player("mary", "!")]
        user_input = ["joe"]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            self.assertEqual(Player.get_name(2, player_list), "joe")

    def test_get_valid_piece_blank(self):
        player_list = [Player("mary", "!")]
        user_input = [" "]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with self.assertRaises(ValueError):
                Player.get_valid_piece(2, "x", player_list)

        user_input = ["   "]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with self.assertRaises(ValueError):
                Player.get_valid_piece(2, "x", player_list)

    def test_get_valid_piece_multi_char(self):
        player_list = [Player("mary", "!")]
        user_input = ["hi"]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with self.assertRaises(ValueError):
                Player.get_valid_piece(2, "x", player_list)

    def test_get_valid_piece_repeat(self):
        player_list = [Player("mary", "!")]
        user_input = "!"
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with self.assertRaises(ValueError):
                Player.get_valid_piece(2, "x", player_list)

    def test_get_valid_piece_blank_char(self):
        player_list = [Player("mary", "!")]
        user_input = ["x"]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            with self.assertRaises(ValueError):
                Player.get_valid_piece(2, "x", player_list)

    def test_get_valid_piece_reg(self):
        player_list = [Player("mary", "!")]
        user_input = ["1"]
        with patch('ConnectNGame.src.player.input', side_effect=user_input):
            self.assertEqual(Player.get_valid_piece(2, "x", player_list), "1")

if __name__ == '__main__':
    unittest.main()
