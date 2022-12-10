from functools import reduce
from itertools import accumulate
from typing import List, Callable
from connector import puzzle_connector
import re


def tokenize(puzzle_input) -> list[str]:
    return puzzle_input.split('\n')


class State:
    x: int
    cycles_left: int
    instruction: Callable[[int], int]

    def run_cycle(self):
        self.cycles_left -= 1
        if self.cycles_left == 0:
            self.x = self.instruction(self.x)

    def __init__(self, X, cycles, instruction):
            self.x = X
            self.cycles_left = cycles
            self.instruction = instruction

    def get_x(self):
        return self.x

    def has_finished(self):
        return self.cycles_left == 0

    def add_op(self, val):
        self.x += val

    def noop(self):
        pass


def get_signal_strength(cycle: int, vals: list[int]):
    return cycle * vals[cycle -1]


def solve_part_1(puzzle_input: list):
    x_vals = run(puzzle_input)

    vals_ = [get_signal_strength(20, x_vals),
             get_signal_strength(60, x_vals),
             get_signal_strength(100, x_vals),
             get_signal_strength(140, x_vals),
             get_signal_strength(180, x_vals),
             get_signal_strength(220, x_vals)
             ]
    return sum(vals_)


def run(puzzle_input):
    x_vals = [1]
    for l in puzzle_input:
        state: State
        match l.split(' '):
            case ['addx', val]:
                state = State(x_vals[-1], 2, lambda x: x + int(val))
            case ['noop', *rest]:
                state = State(x_vals[-1], 1, lambda x: x)

        while not state.has_finished():
            state.run_cycle()
            x_vals.append(state.get_x())
    return x_vals


def solve_part_2(puzzle_input: list):
    screen = render(puzzle_input)

    line = ''
    for v in screen:
        line += str(v)
        if len(line) == 40:
            print(line)
            line = ''


def render(puzzle_input):
    x_vals = [1]
    screen = ['_' for i in range(40 * 6)]
    current_pixel = 0
    for l in puzzle_input:
        state: State
        match l.split(' '):
            case ['addx', val]:
                state = State(x_vals[-1], 2, lambda x: x + int(val))
            case ['noop', *rest]:
                state = State(x_vals[-1], 1, lambda x: x)

        while not state.has_finished():
            if x_vals[-1] in [(current_pixel - 1) % 40, current_pixel % 40, (current_pixel + 1) % 40]:
                screen[current_pixel] = '#'
            current_pixel += 1
            state.run_cycle()
            x_vals.append(state.get_x())
    return screen


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 10)
    tokenized = tokenize(raw_input)[:-1]

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    puzzle_connector.submit_puzzle_solution(2022, 10, str(solution_1), 1)

    print("Solution 2: \n")
    solution_2 = solve_part_2(tokenized)
