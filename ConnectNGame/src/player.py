from .game import Game
from .player import Player
from typing import List

class Player(object):

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece


    def create_players(self, players, empty_char):
        """
        get num_player amount of players appended into the players list
        """
        for num in range(1,self.num_player+1):
            self.players.append(self.create_one_player(num, players, empty_char))



    @staticmethod
    def create_one_player(num: int, players: List[Player], empty_char) -> Player:
        """
        get user input got name and piece
        return a player object
        """
        player_names = [player.name for player in players]
        pieces_list = [player.piece for player in players]

        while True:

            try:
                name = Game.get_name(num, player_names)

                piece = Game.get_valid_piece(num, pieces_list, empty_char)

                new_player = Player(name, piece)

                return new_player

            except ValueError as error:
                print(error)


    @staticmethod
    def get_valid_piece(num, pieces_list, empty_char):

        piece = input("Player {} enter your piece: ".format(str(num)))
        piece = piece.strip()

        if not piece:
            raise ValueError("Your piece cannot be the empty string or whitespace")

        elif len(piece) > 1:
            raise ValueError("{piece} is not a single character. Your piece can only be a single character.")

        elif piece == empty_char:
            raise ValueError("Your piece cannot be the same as the blank character")

        elif piece in pieces_list:  # save name and piece together to get name
            raise ValueError("You cannot use {piece} for your piece as {name} is already using it")

        else:
            return piece



    @staticmethod
    def get_name(num, player_names):

        name = input("Player {} enter your name: ".format(str(num)))

        name = name.lower()
        name = name.strip()

        if not name:  # if empty
            raise ValueError("Your name cannot be the empty string or whitespace.")


        elif name in player_names:
            raise ValueError("You cannot use {name} for your name as someone else is already using it.")

        else:
            return name








