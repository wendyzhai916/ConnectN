from typing import List
from .player import Player
from .board import Board


class Game(object):

    def __init__(self):
        self.num_player = 2
        self.players: List[Player] = []
        self.board: Board = None

    def play_game(self):
        self.create_players()
        while True:
            self.round_game()

    def round_game(self):
        for player in self.players:
            pass

    def create_players(self):
        """
        get num_player amount of players appended into the players list
        """
        for num in self.num_player:
            self.players.append(self.create_one_player(num))

    @staticmethod
    def create_one_player(num):
        """
        get user input got name and piece
        return a player object
        """
        name = input("Player {} enter your name: ".format(str(num)))
        piece = input("Player {} enter your piece: ".format(str(num)))
        return Player(name, piece)
