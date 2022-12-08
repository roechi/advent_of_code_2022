from functools import reduce
from itertools import accumulate
from typing import List
from connector import puzzle_connector
import re


def tokenize(puzzle_input) -> list[str]:
    return puzzle_input.split('\n')


def build_grid(puzzle_input: list) -> list[list[int]]:
    grid = [[int(char) for char in line] for line in puzzle_input]

    return grid


def get_slices(grid, x, y) -> tuple[list[int], list[int], list[int], list[int]]:
    x_dim = grid[y]
    y_dim = [grid[y_c][x] for y_c in range(len(grid))]

    up_slice = y_dim[:y]
    down_slice = y_dim[y + 1:]
    left_slice = x_dim[:x]
    right_slice = x_dim[x + 1:]

    return up_slice, down_slice, left_slice, right_slice


def is_visible_from(height, dir_slice) -> bool:
    return max(dir_slice) < height


def get_score(home_tree, up_slice) -> int:
    up_score = 0
    for t in up_slice:
        if t < home_tree:
            up_score += 1
        elif t >= home_tree:
            up_score += 1
            break
    return up_score


def solve_part_1(puzzle_input: list):
    grid = build_grid(puzzle_input)

    vis_counter = 0

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            up_slice, down_slice, left_slice, right_slice = get_slices(grid, x, y)

            height = grid[y][x]
            if any([is_visible_from(height, slc) for slc in [up_slice, down_slice, left_slice, right_slice]]):
                vis_counter += 1

    vis_counter += 2 * len(grid) + 2 * (len(grid[0]) - 2)

    return vis_counter


def solve_part_2(puzzle_input: list):
    grid = build_grid(puzzle_input)

    scenic_scores = []

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            home_tree = grid[y][x]

            up_slice, down_slice, left_slice, right_slice = get_slices(grid, x, y)
            up_slice.reverse()
            left_slice.reverse()

            slice_scores = [get_score(home_tree, slc) for slc in [up_slice, down_slice, left_slice, right_slice]]
            scenic_scores.append(reduce(lambda a, b: a * b, slice_scores))

    return max(scenic_scores)


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 8)
    tokenized = tokenize(raw_input)[:-1]

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    puzzle_connector.submit_puzzle_solution(2022, 8, str(solution_1), 1)

    solution_2 = solve_part_2(tokenized)
    print("Solution 2: " + str(solution_2))
    puzzle_connector.submit_puzzle_solution(2022, 8, str(solution_2), 2)
