import random
import string
import sys

HANGMANPICS = ['''

  +---+

  |   |
  
      |

      |

      |

      |

=========''', '''

  +---+

  |   |
  
  O   |

      |

      |

      |

=========''', '''

  +---+

  |   |
  
  O   |

  |   |

      |

      |

=========''', '''

  +---+

  |   |
  
  O   |

 /|   |

      |

      |

=========''', '''

  +---+

  |   |
  
  O   |

 /|\  |

      |

      |

=========''', '''

  +---+

  |   |
  
  O   |

 /|\  |

 /    |

      |

=========''', '''

  +---+

  |   |
  
  O   |

 /|\  |

 / \  |

      |

=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer '
         'dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose '
         'mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon '
         'seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle '
         'weasel whale wolf wombat zebra').split()


class Hangman():
    """Creates a class containing the rules of the game Hangman"""

    def __init__(self):
        self.missed_letters = ''
        self.correct_letters = ''
        try:
            self.secret_word = words.pop()
        except IndexError:
            print('There are no more words in the word bank.')
            print('Please try again later, goodbye.')
            sys.exit()

    def __repr__(self):
        return HANGMANPICS[self.limbs()]

    @staticmethod
    def banner():
        val = ''' #     #    #    #     #  #####  #     #    #    #     # 
 #     #   # #   ##    # #     # ##   ##   # #   ##    # 
 #     #  #   #  # #   # #       # # # #  #   #  # #   # 
 ####### #     # #  #  # #  #### #  #  # #     # #  #  # 
 #     # ####### #   # # #     # #     # ####### #   # # 
 #     # #     # #    ## #     # #     # #     # #    ## 
 #     # #     # #     #  #####  #     # #     # #     # 
                                                         '''
        return '\n\n\n' + '*' * 60 + '\n\n' + val + '\n' + '*' * 60

    def limbs(self):
        """Counts the number of incorrect guesses made thus far"""
        return len(self.missed_letters)

    def display(self):
        """Displays the updated hangman image,
            the secret word with the correct guesses filled in,
            and all incorrect guesses made."""

        print(self)
        print()

        print(self.word)
        print('Missed letters:', ' '.join(self.missed_letters))

    @property
    def word(self):
        """Prints the secret word and shows the secret word's letters
            where they have been correctly guessed and blanks otherwise."""

        word = [
            letter if letter in self.correct_letters else '_'
            for letter in self.secret_word
        ]

        return ''.join(word)

    def is_valid_guess(self, guess):
        """Returns 'True' if an input guess is considered valid, 'False' otherwise"""

        already_guessed = self.missed_letters + self.correct_letters
        guess = guess.lower()

        if len(guess) != 1:
            print('Input must be a single letter!')
            return False
        elif guess in already_guessed:
            print('You have already guessed that letter!')
            return False
        elif guess not in string.ascii_lowercase:
            print('Please enter a LETTER.')
            return False
        else:
            return True

    def update_letters(self, guess):
        """Adds player's guess to the appropriate list of guessed letters"""

        if guess in self.secret_word:
            self.correct_letters += guess
        else:
            self.missed_letters += guess

    def found_all_letters(self):
        """Returns 'True' if all the letters in the secret word have been guessed
            'False' otherwise."""
        return all(letter in self.correct_letters for letter in self.secret_word)

    def game_over_msg(self):
        """Inform the player if they have won or lost the game."""

        if self.found_all_letters():
            print(f'Yes! The word was {self.secret_word}! You won!')
        else:
            print('You have run out of guesses!')
            print(f'After {self.limbs()} missed guesses and {len(self.correct_letters)}'
                  f' correct guesses, the word was {self.secret_word}.')


def play_again():
    """Ask player if they want to play again.
        Return 'True' if their response starts with a 'y,'
        return 'False' otherwise."""

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def main():
    game = Hangman()
    print(game.banner())

    while game.limbs() < len(HANGMANPICS) - 1:
        game.display()

        while True:
            try:
                guess = input('Guess a letter. \n> ').lower()
            except KeyboardInterrupt:
                print("Goodbye!")
                sys.exit()
            if game.is_valid_guess(guess):
                break

        game.update_letters(guess)
        if game.found_all_letters():
            break
    else:
        game.display()
    game.game_over_msg()

    if play_again():
        main()
    else:
        print('Thanks for playing, goodbye!')
        sys.exit()


if __name__ == '__main__':
    random.shuffle(words)
    main()
