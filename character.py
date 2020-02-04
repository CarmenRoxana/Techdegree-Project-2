class Character:
    def __init__(self, original):
        # store the original
        self.original = original
    # store a bool of whether or not this letter has had a guess attempted against it
        if self.original == ' ':
            self.was_guessed = True
        else:
            self.was_guessed = False

    def verify_guess(self, guess):
        self.guess = guess
        if self.guess.lower() == self.original.lower():
            self.was_guessed = True

    def __str__(self):
        return "{self.original}".format(self=self)

    @property
    def show_guess(self):
        if self.was_guessed:
            return self.original
        else:
            return "_"
