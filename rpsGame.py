import itertools
import random
import sys
from time import sleep

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins, losses, ties = 0, 0, 0

# Establish which options beat others. Options beat next option in sequence, final option beats first option.
ACCEPTABLE_MOVES = {'p': 'PAPER', 'r': 'ROCK', 's': 'SCISSORS'}

win_cycle = itertools.cycle(ACCEPTABLE_MOVES.values())


def player_input():
    formatted_options = [
        '(' + move[0].lower() + ')' + move[1:].lower()
        for move in ACCEPTABLE_MOVES.values()
    ]
    prompt = f"\nEnter your move: {', '.join(formatted_options)} or (q)uit\n"

    while True:
        player_move = input(prompt)
        if is_valid_move(player_move):
            break
        print('Sorry, that is not a valid move.')
    return ACCEPTABLE_MOVES[player_move]


def is_valid_move(move):
    if move == 'q':
        sys.exit()
    return move in ACCEPTABLE_MOVES


def update_score(player_move, cpu_move):

    global ties, wins, losses
    if player_move == cpu_move:
        print("It's a tie!")
        ties += 1
        return

    for selection in win_cycle:
        losing_move = next(win_cycle)
        if player_move == selection and cpu_move == losing_move:
            print("You win!")
            wins += 1
            break
        if cpu_move == selection and player_move == losing_move:
            print("You lose!")
            losses += 1
            break


def main():
    while True:
        print(f'\nCurrent score: {wins} Wins, {losses} Losses, {ties} Ties')

        player_move = player_input()
        print(player_move, 'versus...')
        sleep(0.75)

        cpu_move = random.choice(list(ACCEPTABLE_MOVES.values()))
        print(cpu_move)
        sleep(0.75)

        update_score(player_move, cpu_move)

if __name__ == '__main__':
    main()
