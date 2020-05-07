from typing import List

class Board(object):

    def __init__(self, row: int, col: int, char: str) -> None:
        self.row = row
        self.col = col
        self.empty_char = char

        self.board_array = []
        for j in range(self.row):
            cur_row = []
            for i in range(self.col):
                cur_row.append(self.empty_char)
            self.board_array.append(cur_row)


    def clear_spot(self, char: str, row: int, col: int) -> None:
        self.board_array[row][col] = char


    def fill(self, char: str, row: int, col: int) -> None:
        self.board_array[row][col] = char


    def __eq__(self, other) -> bool:
        pass


    def __str__(self) -> str:
        pass

    def __repr__(self) -> str: # represent Board

        i = "  " # empty space
        col_num = 0
        row_num = 0
        for col in self.board_array[0]: # go through list containing board info
            i = i + str(col_num) + " "
            col_num = col_num + 1

        i = i[:-1] # removes last character
        i = i + "\n"

        for row in self.board_array:
            i = i + str(row_num)
            row_num = row_num + 1

            for item in row:
                i = i + " " + str(item)

            i = i + "\n"

        i = i.rstrip()
        return i


    def drop(self, col, letter): # drop character into board

        top = 0
        row_num = 0
        for row in self.board_array:
            if row[col] == self.empty_char:
                top = row_num
            row_num = row_num + 1
        self.board_array[top][col] = letter
