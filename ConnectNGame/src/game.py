from typing import List
from .player import Player
from .board import Board
from . import player


# from . import board

class Game(object):

    def __init__(self, file_name):
        self.num_player = 2
        self.players: List[player.Player] = []
        self.board: Board = None
        self.configFile = file_name
        self.empty_char = None
        self.num_rows = None
        self.num_cols = None
        self.win_pieces = None

        self.play_game()

    def play_game(self):
        self.create_board()
        self.create_players()
        self.print_cur_board()

        while True:
            self.round_game()

    def round_game(self):  # FIXME
        """
        one round of game
        """
        for player in self.players:
            self.drop_piece(player)
            self.print_cur_board()
            self.check_end_game(player)

    def check_end_game(self, player):
        """
        1) print the winner's message
        2) exit the program
        """
        if self.check_win(player):
            print(f"{player.name} won the game!")
            exit()

    def check_win(self, player: Player) -> bool:
        """
        1) check if the winner had N connected horizontally
        2) check if the winner had N connected vertically
        3) check if the winner had N connected diagonally
        """
        if self.check_horizontal(self.num_rows, self.num_cols, player.piece, self.win_pieces, self.board.board_array):
            return True
        elif self.check_vertical(self.num_rows, self.num_cols, player.piece, self.win_pieces, self.board.board_array):
            return True
        elif self.check_pos_diagonal(self.num_rows, self.num_cols, player.piece, self.win_pieces, self.board.board_array):
            return True
        elif self.check_neg_diagonal(self.num_rows, self.num_cols, player.piece, self.win_pieces, self.board.board_array):
            return True
        else:
            return False

    @staticmethod
    def check_pos_diagonal(row_num, col_num, piece, win_pieces, board_array) -> bool:
        """
        check if there are a win case of positive sloped diagonal
        """
        pass

    @staticmethod
    def check_neg_diagonal(row_num, col_num, piece, win_pieces, board_array) -> bool:  # PASSES
        """
        check if there are a win case of negative sloped diagonal
        """
        for row in range(row_num - win_pieces + 1):
            for col in range(col_num - win_pieces + 1):
                if board_array[row][col] == piece:
                    num_connect = 1
                    for num in range(1, win_pieces):
                        if board_array[row + num][col + num] == piece:
                            num_connect += 1
                            if num_connect == win_pieces:
                                return True
                        else:
                            break
                else:
                    continue
        return False

    @staticmethod
    def check_vertical(row_num, col_num, piece, win_pieces, board_array) -> bool:  # PASSES
        for col in range(col_num):
            for row in range(row_num - win_pieces + 1):
                if board_array[row][col] == piece:
                    num_connect = 1
                    for num in range(1, win_pieces):
                        if board_array[row + num][col] == piece:
                            num_connect += 1
                            if num_connect == win_pieces:
                                return True
                        else:
                            break
                else:
                    continue
        return False

    @staticmethod
    def check_horizontal(row_num, col_num, piece, win_pieces, board_array) -> bool:  # PASSES

        for row in range(row_num):
            for col in range(col_num - win_pieces + 1):
                if board_array[row][col] == piece:
                    num_connect = 1
                    for num in range(1, win_pieces):
                        if board_array[row][col + num] == piece:
                            num_connect += 1
                            if num_connect == win_pieces:
                                return True
                        else:
                            break
                else:
                    continue
        return False

    def check_diagonal(self, player):
        pass

    def drop_piece(self, player: Player):

        col = None

        while True:

            try:
                col = int(input(f"{player.name}, please enter the column you want to play in: "))

                if col >= self.board.col or col < 0:
                    raise ValueError(
                        f"Your column needs to be between 0 and {self.num_cols - 1} but it is actually {col}.")  # not printing

                else:
                    break

                # elif  column not full

            # except TypeError:
            # print("{}, column needs to be an integer. {} is not an integer. ".format(name, col))
            # continue

            except ValueError:
                print(f"{player.name}, column needs to be an integer. {col} is not an integer.")

        self.board.drop(col, player.piece)

    def print_cur_board(self):
        print(repr(self.board))

    def create_board(self):

        with open(self.configFile) as file:
            line = file.readline()

            while line:

                values = line.split(":")
                values[0] = values[0].strip()
                values[1] = values[1].strip()

                if values[0] == "num_rows":
                    self.num_rows = int(values[1])

                elif values[0] == "num_cols":
                    self.num_cols = int(values[1])

                elif values[0] == "blank_char":
                    self.empty_char = values[1]

                elif values[0] == "num_pieces_to_win":
                    self.win_pieces = int(values[1])

                line = file.readline()

        self.board = Board(self.num_rows, self.num_cols, self.empty_char)

    def create_players(self):
        """
        get num_player amount of players appended into the players list
        """
        for num in range(1, self.num_player + 1):
            self.players.append(Player.create_one_player(num, self.players, self.empty_char))

    
