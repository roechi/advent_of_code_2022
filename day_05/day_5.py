from functools import reduce
from typing import List
from connector import puzzle_connector
import re


def tokenize(puzzle_input):
    return [s for s in puzzle_input.split('\n')]


def solve_part_1(puzzle_input: List[str]):
    input_break = find_input_break(puzzle_input)

    stacks = init_stacks(puzzle_input[0:input_break - 1])

    apply_moves(puzzle_input[input_break + 1:], stacks)

    return reduce(lambda x, y: x+ y, [s[-1] for s in list(stacks.values())])


def solve_part_2(puzzle_input: List[str]):
    input_break = find_input_break(puzzle_input)

    stacks = init_stacks(puzzle_input[0:input_break - 1])

    apply_moves_2(puzzle_input[input_break + 1:], stacks)

    return reduce(lambda x, y: x + y, [s[-1] for s in list(stacks.values())])


def init_stacks(puzzle_input):
    stacks = {}
    for i in range(1, 10):
        stacks[i] = []
    for line in puzzle_input:
        if '[' in line:
            if line[1] != ' ':
                stacks[1].append(line[1])
            pos = 1
            for i in range(2, 10):
                pos += 4
                if line[pos] != ' ':
                    stacks[i].append(line[pos])

    for i in range(1, 10):
        stacks[i].reverse()
    return stacks


def find_input_break(puzzle_input):
    break_found = False
    idx = 0
    while not break_found:
        if puzzle_input[idx] == '':
            break_found = True
        else:
            idx += 1

    return idx


def apply_moves(puzzle_input, stacks):
    move_pattern = re.compile('([0-9]+)')
    for m in puzzle_input:
        groups = re.findall(move_pattern, m)
        if groups:
            amount = int(groups[0])
            origin = int(groups[1])
            target = int(groups[2])

            for s in range(amount):
                v = stacks[origin].pop()
                stacks[target].append(v)


def apply_moves_2(puzzle_input, stacks):
    move_pattern = re.compile('([0-9]+)')
    for m in puzzle_input:
        groups = re.findall(move_pattern, m)
        if groups:
            amount = int(groups[0])
            origin = int(groups[1])
            target = int(groups[2])

            v = stacks[origin][-amount:]
            stacks[origin] = stacks[origin][:-amount]
            stacks[target].extend(v)


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 5)
    tokenized = tokenize(raw_input)

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    puzzle_connector.submit_puzzle_solution(2022, 5, str(solution_1), 1)

    solution_2 = solve_part_2(tokenized)
    print("Solution 2: " + str(solution_2))
    puzzle_connector.submit_puzzle_solution(2022, 5, str(solution_2), 2)
