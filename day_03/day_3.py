from typing import List

from connector import puzzle_connector
import re


def tokenize(puzzle_input):
    return [s.strip(' ') for s in puzzle_input.split('\n')]


def split_str(a_list: str):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def solve_part_1(puzzle_input: List[str]):

    priorities = []
    for t in puzzle_input:
        if len(t) > 0:
            left, right = split_str(t)

            left_set = set(left)
            right_set = set(right)

            intersection = set.intersection(left_set, right_set)
            assert len(intersection) == 1

            item = intersection.pop()
            priorities.append(get_priority(item))

    return sum(priorities)


def solve_part_2(puzzle_input: List[str]):
    priorities = []
    for gr in zip(*(iter(puzzle_input[:-1]),) * 3):
        sets = [set(e) for e in gr]

        intersection = set.intersection(*sets)
        assert len(intersection) == 1

        item = intersection.pop()
        priorities.append(get_priority(item))

    return sum(priorities)


def get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    else:
        return  ord(item) - 65 + 27


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 3)
    tokenized = tokenize(raw_input)

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    puzzle_connector.submit_puzzle_solution(2022, 3, str(solution_1), 1)

    solution_2 = solve_part_2(tokenized)
    print("Solution 2: " + str(solution_2))
    puzzle_connector.submit_puzzle_solution(2022, 3, str(solution_2), 2)
