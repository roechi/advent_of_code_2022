from functools import reduce
from typing import List
from connector import puzzle_connector
import re


def tokenize(puzzle_input):
    return puzzle_input.strip()


def end_of_first_slice_no_duplicates(ipt: str, slice_len: int) -> int:
    for i in range(len(ipt) - slice_len):
        slice = ipt[i:i + slice_len]
        if len(set(slice)) == len(slice):
            return i + slice_len


def solve_part_1(puzzle_input: str):
    return end_of_first_slice_no_duplicates(puzzle_input, 4)


def solve_part_2(puzzle_input: str):
    return end_of_first_slice_no_duplicates(puzzle_input, 14)


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 6)
    tokenized = tokenize(raw_input)

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    puzzle_connector.submit_puzzle_solution(2022, 6, str(solution_1), 1)

    solution_2 = solve_part_2(tokenized)
    print("Solution 2: " + str(solution_2))
    puzzle_connector.submit_puzzle_solution(2022, 6, str(solution_2), 2)
