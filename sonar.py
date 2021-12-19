import string
import sys
import math
from random import randrange, choice


class Sonar:

    def __init__(self):
        self.board = self._new_board()
        self.chests = self.chest_locations()
        self.past_moves = []
        self.sonars_left = 20

    def display(self):
        print(self._tens_digits())
        print(self._ones_digits(), end='\n\n')
        for index, row in enumerate(self.board):
            txt = f"{index} {''.join(row)} {index}"
            print(txt.center(66))
        print()
        print(self._ones_digits())
        print(self._tens_digits())
        print()
        ## print(', '.join(self.chests))

    def score(self):
        return f'You have {self.sonars_left} sonar device(s) left and ' \
               f'{len(self.chests)} treasure chest(s) remaining.'

    def is_valid(self, guess):

        if guess.lower() == 'help':
            print(self.instructions(), end='\n\n')
        elif guess.lower().startswith('q'):
            sys.exit()

        guess = guess.split()

        if len(guess) != 2:
            print('Enter a number from 0-14, a space, then a number 0-59')
            return False

        if (guess[0], guess[1]) in self.past_moves:
            print('You already moved there.')
            return False

        for elem in guess:
            if not elem.isdigit():
                print('Enter a number from 0-14, a space, then a number 0-59')
                return False

        if not (0 <= int(guess[0]) <= 14 and 0 <= int(guess[1]) < 60):
            print('Enter a number from 0-14, a space, then a number 0-59')
            return False

        return True

    def update(self, guess):
        row, col = guess if isinstance(guess, tuple) else guess.split()
        row, col = int(row), int(col)
        dist = self._distance(row, col)

        if dist == 0:
            self.chests.remove((row, col))
            if self.chests:
                for move in self.past_moves:
                    self.update(move)
            return 'You have found the sunken treasure chest!'
        elif dist < 10:
            self.board[row][col] = str(dist)
            return f'Treasure detected {dist} units away!'
        else:
            self.board[row][col] = 'X'
            return 'Sonar did not detect anything.' \
                   'All treasure chests are out of range.'

    def _distance(self, x, y):
        distances = {
            (cx, cy): math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            for cx, cy in self.chests
        }
        c = min(distances, key=lambda k: distances[k])
        return int(distances[c])

    @staticmethod
    def chest_locations():
        locs = set()
        while len(locs) < 3:
            row, col = randrange(15), randrange(60)
            locs.add((row, col))
        return locs

    @staticmethod
    def _new_board():
        board = [[] for _ in range(15)]
        for row in board:
            waves = [choice('~`') for _ in range(60)]
            row.extend(waves)
        return board

    @staticmethod
    def _tens_digits():
        txt = ''
        for i in range(1, 6):
            txt += str(i).ljust(10)
        return txt.rjust(60).center(66)

    @staticmethod
    def _ones_digits():
        txt = string.digits * 6
        return txt.center(66)

    @staticmethod
    def instructions():
        return '''Instructions:

You are the captain of the Simon, a treasure-hunting ship. Your current
mission is to use sonar devices to find three sunken treasure chests at the
bottom of the ocean. But you only have cheap sonar that finds distance, not
direction.

Enter the coordinates to drop a sonar device. The ocean map will be marked
with how far way the nearest chest is, or an X if it is beyond the sonar
device's range.

When you drop a sonar device directly on a chest, you retrieve
it and the other sonar devices update to show how far away the next nearest
chest is.

The treasure chests don't move around. Sonar devices can detect treasure
chests up to 9 spaces away. Try to collect all 3 chests before running out
of sonar devices. Good luck!

Type 'help' during gameplay to repeat these instructions.'''


def main():
    game = Sonar()
    while game.sonars_left:
        game.display()
        print(game.score())
        while True:
            guess = input('Where do you want to drop the next sonar device?\n> ')
            if game.is_valid(guess):
                x, y = guess.split()
                game.past_moves.append((x, y))
                game.sonars_left -= 1
                break
        print(game.update(guess))
        if not game.chests:
            print('You have found all the sunken treasure chests! Congratulations!')
            break
    else:
        print("We've run out of sonar devices!")
        print('Now we have to turn the ship around and head home with no treasure!')

    if input('Would you like to play again?\n> ').lower().startswith('y'):
        main()
    else:
        print('Ok, goodbye!')
        sys.exit()


if __name__ == '__main__':
    main()
