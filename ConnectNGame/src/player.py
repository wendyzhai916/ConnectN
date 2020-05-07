from . import game
from . import player
from typing import List


class Player(object):

    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
