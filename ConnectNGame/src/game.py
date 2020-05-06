from typing import List
from .player import Player
from .board import Board


class Game(object):

    def __init__(self, file_name):
        self.num_player = 2
        self.players: List[Player] = []
        self.board: Board = None
        self.configFile = file_name

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

        self.board.drop(col,"-")

        # FIXME: create drop method
        # TODO: modify the board to drop the object
        # maybe create drop_col in the board class? <- probably this depends on how the board class turns out


    def print_cur_board(self):
        print(repr(self.board))  # TODO: the create (or just use the one from hw2) method in board class


    def create_board(self):
        # TODO: take information from the config file to create board

        #print("Config file: " + self.configFile);

        with open(self.configFile) as fp:
            line = fp.readline()
            count = 1
            while line:
                #print("Line {}: {}".format(count, line.strip()))
                line = fp.readline()
                count += 1

        self.board = Board(5 ,5 ,"*")


    def create_players(self):
        """
        get num_player amount of players appended into the players list
        """
        for num in range(1,self.num_player+1):
            self.players.append(self.create_one_player(num))



    @staticmethod
    def create_one_player(num: int) -> Player:
        """
        get user input got name and piece
        return a player object
        """
        player_names = [] # empty list of player names
        pieces_list = []

        while True:
            try:
                name = input("Player {} enter your name: ".format(str(num)))

                name = name.lower()
                player_names.append(name) # append lower case name to list

                if " " in name or name.isspace(): # what about empty string
                    print("Your name cannot be the empty string or whitespace.")

                elif name in player_names:
                    print("You cannot use {name} for your name as someone else is already using it.")

            except:
                break

        while True:
            try:
                piece = input("Player {} enter your piece: ".format(str(num)))

                if " " in piece or piece.isspace():
                    print("Your piece cannot be the empty string or whitespace")

                if len(piece) == 1:
                    print("{piece} is not a single character. Your piece can only be a single character.")

                #if piece == board.empty_char
                    print("Your piece cannot be the same as the blank character")

                if piece in pieces_list: # save name and piece together to get name
                    print("You cannot use {piece} for your piece as {name} is already using it")

            except:
                break




        #name = input("Player {} enter your name: ".format(str(num)))
        #piece = input("Player {} enter your piece: ".format(str(num)))
        #return Player(name, piece)




