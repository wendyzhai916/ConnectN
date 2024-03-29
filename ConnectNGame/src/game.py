from typing import List
from .player import Player
from .board import Board
from . import player
from . import board


class Game(object):

    def __init__(self, file_name: str) -> None:
        self.num_player: int = 2
        self.players: List[player.Player] = []
        self.board: Board  # = None
        self.configFile: str = file_name
        self.empty_char: str  # = None
        self.num_rows: int  # = None
        self.num_cols: int  # = None
        self.win_pieces: int  # = None

        self.play_game()

    def play_game(self) -> None:
        self.create_board()
        self.create_players()
        self.print_cur_board()

        while True:
            self.round_game()

    def round_game(self) -> None:
        """
        one round of game
        """
        for player in self.players:
            self.drop_piece(player)
            self.print_cur_board()
            self.check_end_game(player)

    @staticmethod
    def check_tie(board_array: List, empty_char: str) -> bool:  # PASSES
        board_array = board_array
        for item in board_array[0]:
            if item == empty_char:
                return False
        return True

    def check_end_game(self, player: Player) -> None:
        """
        1) print the winner's message
        2) exit the program
        """
        if self.check_win(player):
            print(f"{player.name} won the game!")
            exit()

        if self.check_tie(self.board.board_array, self.empty_char):
            print("Tie Game.")
            exit()

    def check_win(self, player: Player) -> bool:  # Passes since all check methods passes
        """
        1) check if the winner had N connected horizontally
        2) check if the winner had N connected vertically
        3) check if the winner had N connected diagonally
        """
        if self.check_horizontal(self.num_rows, self.num_cols, player.piece, self.win_pieces, self.board.board_array):
            return True
        elif self.check_vertical(self.num_rows, self.num_cols, player.piece, self.win_pieces, self.board.board_array):
            return True
        elif self.check_pos_diagonal(self.num_rows, self.num_cols, player.piece, self.win_pieces,
                                     self.board.board_array):
            return True
        elif self.check_neg_diagonal(self.num_rows, self.num_cols, player.piece, self.win_pieces,
                                     self.board.board_array):
            return True
        else:
            return False

    @staticmethod
    def check_pos_diagonal(row_num: int, col_num: int, piece: str, win_pieces: int, board_array: List) -> bool:  #passes
        """
        check if there are a win case of positive sloped diagonal
        """
        for row in range(row_num - win_pieces + 1):
            for col in range(win_pieces - 1, col_num):
                if board_array[row][col] == piece:
                    num_connect = 1
                    for num in range(1, win_pieces):
                        if board_array[row + num][col - num] == piece:
                            num_connect += 1
                            if num_connect == win_pieces:
                                return True
                        else:
                            break
                else:
                    continue
        return False

    @staticmethod
    def check_neg_diagonal(row_num: int, col_num: int, piece: str, win_pieces: int, board_array: List) -> bool:  #passes
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
    def check_vertical(row_num: int, col_num: int, piece: str, win_pieces: int, board_array: List) -> bool:  #passes
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
    def check_horizontal(row_num: int, col_num: int, piece: str, win_pieces: int, board_array: List) -> bool:  #passes

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

    # def check_diagonal(self, player):
    # pass

    def drop_piece(self, player: Player) -> None:  # test for error   # passes if the drop method in board passes

        while True:
            col: int = input(f"{player.name}, please enter the column you want to play in: ")

            try:
                col = int(col)

            except ValueError:
                print(f"{player.name}, column needs to be an integer. {col} is not an integer.")

            else:
                if col >= self.board.col or col < 0:
                    print(f"Your column needs to be between 0 and {self.num_cols - 1} but it is actually {col}.")

                elif self.board.board_array[0][col] != self.empty_char:
                    print(f"You cannot play in {col} because it is full.")

                else:
                    break

        self.board.drop(col, player.piece)

    def print_cur_board(self) -> None:  # works if the repr method in board class passes
        print(repr(self.board))

    def create_board(self) -> None:

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

    def create_players(self) -> None:
        """
        get num_player amount of players appended into the players list
        """
        for num in range(1, self.num_player + 1):
            self.players.append(Player.create_one_player(num, self.players, self.empty_char))
