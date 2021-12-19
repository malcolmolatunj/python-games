from random import shuffle
from collections import deque


class Card:
    def __init__(self, value, faceup=False):
        self.value = value
        self.faceup = faceup

    def __repr__(self):
        return f'Card {self.value}, faceup={self.faceup}'


def has_won(stacks):
    return all(
        card.faceup
        for stack in stacks
        for card in stack
    )


def distribute_cards():
    deck = [Card(n % 13) for n in range(52)]
    shuffle(deck)

    stacks = []
    for i in range(13):
        stacks.append(deque())
        for _ in range(4):
            stacks[i].append(deck.pop())
    return stacks


def main():
    stacks = distribute_cards()
    stacks[-1][-1].faceup = True
    ejected_card = stacks[-1].pop()

    while True:
        current_stack = stacks[ejected_card.value]
        current_stack.appendleft(ejected_card)
        if current_stack[-1].faceup:
            break
        current_stack[-1].faceup = True
        ejected_card = current_stack.pop()

    return has_won(stacks)


if __name__ == '__main__':
    games = 10000
    for test in range(1, 5):
        wins = sum(main() for _ in range(games))
        win_chance = wins / games
        print(f'Test {test}: {round(win_chance * 100, 2)}% chance of winning')
