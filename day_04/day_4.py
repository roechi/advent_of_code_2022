from typing import List
from connector import puzzle_connector
import re


def tokenize(puzzle_input):
    return [s.strip(' ') for s in puzzle_input.split('\n')]


def get_pattern():
    pattern = re.compile('([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)')
    return pattern


def get_ranges(pattern, t):
    groups = pattern.match(t).groups()
    elf_one_range = [*range(int(groups[0]), int(groups[1]) + 1)]
    elf_two_range = [*range(int(groups[2]), int(groups[3]) + 1)]
    return elf_one_range, elf_two_range


def ranges_contain_each_other(range_one, range_two):
    return set(range_one).issubset(range_two) or set(range_two).issubset(range_one)


def ranges_overlap(range_one, range_two):
    return set(range_one) & set(range_two)


def solve_part_1(puzzle_input: List[str]):
    pattern = re.compile('([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)')

    count_included = 0

    for t in puzzle_input[:-1]:
        elf_one_range, elf_two_range = get_ranges(pattern, t)

        if ranges_contain_each_other(elf_one_range, elf_two_range):
            count_included += 1

    return count_included


def solve_part_2(puzzle_input: List[str]):
    pattern = get_pattern()

    count_overlap = 0

    for t in puzzle_input[:-1]:
        elf_one_range, elf_two_range = get_ranges(pattern, t)

        if ranges_overlap(elf_one_range, elf_two_range):
            count_overlap += 1

    return count_overlap


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 4)
    tokenized = tokenize(raw_input)

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    puzzle_connector.submit_puzzle_solution(2022, 4, str(solution_1), 1)

    solution_2 = solve_part_2(tokenized)
    print("Solution 2: " + str(solution_2))
    puzzle_connector.submit_puzzle_solution(2022, 4, str(solution_2), 2)
