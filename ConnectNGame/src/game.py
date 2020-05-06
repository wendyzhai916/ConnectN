from typing import List
from .player import Player
from .board import Board
from . import player
from . import board


class Game(object):

    def __init__(self, file_name):
        self.num_player = 2
        self.players: List[Player] = []
        self.board: Board = None
        self.configFile = file_name
        self.empty_char = None
        self.num_rows = None
        self.num_cols = None
        self.win_pieces = None

        self.play_game()

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

        self.board.drop(col,)


    def print_cur_board(self):
        print(repr(self.board))


    def create_board(self):

        with open(self.configFile) as file:
            line = file.readline()

            while line:
                if line.startswith("num_rows"):
                    self.num_rows = int(line[-2])

                elif line.startswith("num_cols"):
                    self.num_cols = int(line[-2])

                elif line.startswith("blank_char"):
                    self.empty_char = line[-2]

                elif line.startswith("num_pieces_to_win"):
                    self.win_pieces = int(line[-2])

                line = file.readline()

        self.board = Board(self.num_rows ,self.num_cols ,self.empty_char)


    def create_players(self):
        """
        get num_player amount of players appended into the players list
        """
        for num in range(1, self.num_player + 1):
            self.players.append(self.create_one_player(num, self.players, self.empty_char))


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








