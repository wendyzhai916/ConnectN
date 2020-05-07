from . import game
from typing import List

class Player(object):

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece


    @staticmethod
    def create_one_player(num: int, players: List["Player"], empty_char) -> "Player":
        """
        get user input got name and piece
        return a player object
        """
        player_names = [player.name for player in players]
        pieces_list = [player.piece for player in players]

        while True:

            try:
                name = Player.get_name(num, player_names, players)

                piece = Player.get_valid_piece(num, empty_char, players)

                new_player = Player(name, piece)

                return new_player

            except ValueError as error:
                print(error)


    @staticmethod
    def get_valid_piece(num, empty_char, players: List["Player"]):

        piece = input(f"Player {num} enter your piece: ")
        piece = piece.strip()

        if not piece:
            raise ValueError("Your piece cannot be the empty string or whitespace")

        elif len(piece) > 1:
            raise ValueError(f"{piece} is not a single character. Your piece can only be a single character.")

        elif piece == empty_char:
            raise ValueError("Your piece cannot be the same as the blank character")

        for player in players:
            if piece == player.piece:
                raise ValueError(f"You cannot use {piece} for your piece as {player.name} is already using it")

        else:
            return piece



    @staticmethod
    def get_name(num, player_names, players):

        name = input(f"Player {num} enter your name: ")

        name = name.strip()

        if not name:  # if empty
            raise ValueError(f"Your name cannot be the empty string or whitespace.")

        for player in players:
            if name == player.name.lower():
                raise ValueError(f"You cannot use {name} for your name as someone else is already using it.")

        else:
            return name




