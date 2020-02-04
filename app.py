from game import Game
from game import PHRASES

if __name__ == '__main__':
    phrase_guess = Game(PHRASES)
    # phrase_guess.test()
    phrase_guess.play_game()
