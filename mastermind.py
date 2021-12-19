import string
import random
import sys
import itertools

NUMBER_OF_NUMS = 6


class Mastermind:
    _NONE = "Bagels"
    _ONE = "Pico"
    _CORRECT = "Fermi"
    NUM_DIGITS = 4
    NUM_GUESSES = 10
    CLUES = {
        _NONE: "None of the digits is correct.",
        _ONE: "One digit is correct, but in the wrong position.",
        _CORRECT: "One digit is correct and in the right position."
    }
    possible_nums = string.digits[:NUMBER_OF_NUMS]

    def __init__(self, answer=None):
        self.secret_number = answer or \
                             ''.join(random.sample(self.possible_nums * self.NUM_DIGITS, self.NUM_DIGITS))

    @staticmethod
    def display_title():
        for _ in range(3):
            print()

        print('*' * 75)
        print()
        print(''' #     #    #     #####  ####### ####### ######  #     # ### #     # ######  
 ##   ##   # #   #     #    #    #       #     # ##   ##  #  ##    # #     # 
 # # # #  #   #  #          #    #       #     # # # # #  #  # #   # #     # 
 #  #  # #     #  #####     #    #####   ######  #  #  #  #  #  #  # #     # 
 #     # #######       #    #    #       #   #   #     #  #  #   # # #     # 
 #     # #     # #     #    #    #       #    #  #     #  #  #    ## #     # 
 #     # #     #  #####     #    ####### #     # #     # ### #     # ######  
                                                                             ''')
        print('*' * 75)
        print()

    ##    @property
    ##    def secret_number(self):
    ##        if self._secret is None:
    ##            self._secret = ''.join(random.sample(self.possible_nums*4, self.NUM_DIGITS))
    ##        return self._secret

    @classmethod
    def display_rules(cls):
        print(f"I'm thinking of a {cls.NUM_DIGITS}-digit number.", end=' ')
        print("Digits may appear in the number more than once.")
        print(f"All digits are less than or equal to {NUMBER_OF_NUMS - 1}.")
        print("Try to guess what number I'm thinking of.")
        print("The clues I give are:")
        for clue, definition in cls.CLUES.items():
            print(f'\t{clue}: {definition}')
        print()

    def give_clues(self, guess):

        guess_tally, answer_tally = '', ''

        for g_char, s_char in zip(guess, self.secret_number):
            if g_char == s_char:
                guess_tally += '_'
                answer_tally += '?'
            else:
                guess_tally += g_char
                answer_tally += s_char

        clues = [
            self._CORRECT
            for guessed_digit, secret_digit in zip(guess, self.secret_number)
            if guessed_digit == secret_digit
        ]
        for guessed_digit in guess_tally:
            if guessed_digit in answer_tally:
                clues.append(self._ONE)
        if not clues:
            clues.append(self._NONE)

        clues.sort()
        return ', '.join(clues)

    def is_won(self, guess):
        return all(
            guessed_digit == secret_digit
            for guessed_digit, secret_digit in zip(guess, self.secret_number)
        )


def guess_is_valid(guess):
    if guess == 'help':
        Mastermind.display_rules()
        return False
    elif len(guess) != Mastermind.NUM_DIGITS:
        print(f"Your guess must be exactly {Mastermind.NUM_DIGITS} digits!")
        return False
    elif not guess.isnumeric():
        print(f"Your guess must be a number!")
        return False
    elif any(digit not in string.digits[:NUMBER_OF_NUMS] for digit in guess):
        print(f"All digits must be less than or equal to {NUMBER_OF_NUMS - 1}!")
        return False
    else:
        return True


def main():
    game = Mastermind()
    game.display_title()
    game.display_rules()
    print(f"I've thought up a number. You have {Mastermind.NUM_GUESSES} guesses to get it.")

    for guess_num in range(1, Mastermind.NUM_GUESSES + 1):
        while True:
            try:
                guess = input(f"Guess #{guess_num}: ")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                sys.exit()
            else:
                if guess_is_valid(guess):
                    break
        print(game.give_clues(guess))
        if game.is_won(guess):
            print("Yay! You won!")
            break
    else:
        print(f"Sorry, my number was {game.secret_number}.")

    response = input("Would you like to play again?\n> ")
    if response.lower().startswith('y'):
        main()
    else:
        print("Alright, thanks for playing! Let's play again soon!")
        print("Goodbye!")
        sys.exit()


if __name__ == '__main__':
    main()
