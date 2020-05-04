from typing import List
from .player import Player
from .board import Board


class Game(object):

    def __init__(self):
        self.num_player = 2
        self.players: List[Player] = []
        self.board: Board = None

    def play_game(self):
        """
        the main method basically
        """
        self.create_board()
        self.create_players()
        while True:
            self.round_game()  # TODO: when does the game stops?

    def round_game(self):  # FIXME
        """
        one round of game
        """
        for player in self.players:
            self.drop_piece(player.name)
            self.print_cur_board()

    def drop_piece(self, name: str):
        """
        1) ask for player input for col
        2) if the input is not int, raise TypeError
        3) if the input is not a valid col, raise ValueError
        4) use the input in the drop method (in board class) to modify the board
        """
        col = None
        while True:
            try:
                col = int(input("{}, please enter the column you want to play in: ".format(name)))
                if col >= self.board.col or col < 0:  # FIXME: col in the board class
                    raise ValueError("That is not a valid column.")
            except TypeError:
                print("{}, column needs to be an integer. {} is not an integer. ".format(name, col))
                continue
            except ValueError:
                continue
            else:
                break
        self.board.drop(col)  # FIXME: create drop method
        # TODO: modify the board to drop the object
        # maybe create drop_col in the board class? <- probably this depends on how the board class turns out

    def print_cur_board(self):
        print(repr(self.board))  # TODO: the create (or just use the one from hw2) method in board class

    def create_board(self):
        pass  # TODO: take information from the config file to create board

    def create_players(self):
        """
        get num_player amount of players appended into the players list
        """
        for num in range(self.num_player):
            self.players.append(self.create_one_player(num))

    @staticmethod
    def create_one_player(num: int) -> Player:
        """
        get user input got name and piece
        return a player object
        """
        name = input("Player {} enter your name: ".format(str(num)))
        piece = input("Player {} enter your piece: ".format(str(num)))
        return Player(name, piece)
