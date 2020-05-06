import sys
from ConnectNGame.src.game import Game

def main() -> None:

    game = Game(sys.argv[1])
    game.play_game()

if __name__ == '__main__':
    main()

