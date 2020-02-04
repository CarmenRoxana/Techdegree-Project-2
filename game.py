import random
from phrase import Phrase

PHRASES = [
    ("We are what we think"),
    ("Powerful dreams inspire powerful action"),
    ("All limitations are self imposed"),
    ("Be gentle first with yourself"),
    ("Failure cannot cope with persistence"),
]


class Game:

    def __init__(self, phrases):
        self.lives = 5
        self.guesses = []
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.current_phrase = random.choice(self.phrases)

    # def test(self):
    #     print(self.phrases)

    def player_input(self):
        guess = ""
        while not guess:
            try:
                user_guess = input("Make a guess: ")
                if not user_guess.isalpha():
                    print(
                        "That is not a  valid guess. The guess needs to be only one letter and never a number or special character.")
                    continue
                elif len(user_guess) > 1:
                    print("You've entered too many characters.Enter only one letter at a time.")
                    continue
                elif user_guess.lower() in self.guesses:
                    print("Please try again, you have already guessed that letter!")
                    continue
            except Exception:
                print("Something went wrong. Please retry!")
            else:
                guess = user_guess
                self.guesses.append(guess.lower())
                return guess.lower()

    def play_game(self):
        game_won = False
        print("Welcome to a new phrase guessing game!")
        while not game_won:
            print(f"Lives You Have: {self.lives}")
            print(f"Letters you've guessed: {self.guesses}\n")
            self.current_phrase.display_phrase()
            new_guess = self.player_input()
            if new_guess not in [letter.original.lower() for letter in self.current_phrase]:
                self.lives -= 1
            for character in self.current_phrase:
                character.verify_guess(new_guess)
            if self.lives == 0:
                print(f"You have {self.lives} lives left.")
                answer = input(
                    "Sorry, you ran out of lives. Would you like to play again? [y/n] ")
                if answer.lower() == 'y':
                    Game(PHRASES).play_game()
                    break
                else:
                    print("Thanks for playing. See you next time.")
                    break
            if self.current_phrase.letters_all_guessed():
                game_won = True
                self.current_phrase.display_phrase()
                print("Congratulations, you've won the game!")
                break
