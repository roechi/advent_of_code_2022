from typing import List

from connector import puzzle_connector
import re


def tokenize(puzzle_input):
    return [s.strip(' ') for s in puzzle_input.split('\n')]


def solve_part_1(puzzle_input: List[str]):
    pattern = re.compile('([A-Z]) ([X-Z])')

    all_scores = []
    for t in puzzle_input:
        matched = pattern.match(t)
        if matched:
            opponent = ord(matched.groups()[0]) - 65
            me = ord(matched.groups()[1]) - 88
            score = me + 1

            win = determine_rock_paper_scissors(me, opponent)

            score = score + 3 * (win + 1)

            all_scores.append(score)

    return sum(all_scores)


def solve_part_2(puzzle_input: List[str]):
    pattern = re.compile('([A-Z]) ([X-Z])')

    all_scores = []
    for t in puzzle_input:
        matched = pattern.match(t)
        if matched:
            opponent = ord(matched.groups()[0]) - 65
            adv = ord(matched.groups()[1]) - 89
            me = get_fitting_option(opponent, adv)
            score = me + 1

            win = determine_rock_paper_scissors(me, opponent)
            score = score + 3 * (win + 1)

            all_scores.append(score)
    return sum(all_scores)


def determine_rock_paper_scissors(a: int, b: int) -> int:
    """ Calculate the result of a Rock-Paper-Scissors Match in a overcomplicated
        arithmetic way by trying to make everything hard for yourself
        while avoiding control structures and dictionary lookups (and fail on the last line).

        Input parameters are encoded as:
            0 -> rock
            1 -> paper
            2 -> scissors
        :param a: input of player a as a number between 0 and 2
        :param b: input of player b as a number between 0 and 2
        :returns result of match: 1 if a won, -1 if b won, 0 if it was a draw
    """

    res = (a - b + 3) % 3
    return -1 if res == 2 else res


def get_fitting_option(opponent: int, advice: int) -> int:
    return (opponent + advice) % 3


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 2)
    tokenized = tokenize(raw_input)

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    puzzle_connector.submit_puzzle_solution(2022, 2, str(solution_1), 1)

    solution_2 = solve_part_2(tokenized)
    print("Solution 2: " + str(solution_2))
    puzzle_connector.submit_puzzle_solution(2022, 2, str(solution_2), 2)
