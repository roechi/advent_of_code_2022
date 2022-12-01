from typing import List

from connector import puzzle_connector
import re


def tokenize(puzzle_input):
    return [s.strip(' ') for s in puzzle_input.split('\n')]


def get_calorie_sums(puzzle_input):
    pattern = re.compile('([0-9]+)')
    current_elf = 0
    all_elfs = []
    for t in puzzle_input:
        matched = pattern.match(t)
        if matched:

            current_elf += int(matched.groups()[0])
        else:
            all_elfs.append(current_elf)
            current_elf = 0
    return all_elfs


def solve_part_1(puzzle_input: List[str]):
    all_elfs = get_calorie_sums(puzzle_input)

    return max(all_elfs)


def solve_part_2(puzzle_input: List[str]):
    all_elfs = get_calorie_sums(puzzle_input)

    all_elfs.sort(reverse=True)
    return sum(all_elfs[:3])


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 1)
    tokenized = tokenize(raw_input)

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    puzzle_connector.submit_puzzle_solution(2022, 1, str(solution_1), 1)

    solution_2 = solve_part_2(tokenized)
    print("Solution 2: " + str(solution_2))
    puzzle_connector.submit_puzzle_solution(2022, 1, str(solution_2), 2)
