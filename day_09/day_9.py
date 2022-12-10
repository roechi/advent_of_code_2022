import numpy as np

from connector import puzzle_connector


def tokenize(puzzle_input) -> list[str]:
    return puzzle_input.split('\n')


def follow_head(head: np.array, tail: np.array) -> np.array:
    x, y = head[0] - tail[0], head[1] - tail[1]

    abs_x = abs(x)
    abs_y = abs(y)

    if abs_x > 1 or abs_y > 1:
        return (
            tail + np.array([0 if x == 0 else x // abs_x, 0 if y == 0 else y // abs_y])
        )
    return tail


def run(puzzle_input: list[str], knots=2) -> int:
    dir_vecs = {
        'R': np.array([1, 0]),
        'L': np.array([-1, 0]),
        'U': np.array([0, 1]),
        'D': np.array([0, -1]),
    }

    moves = [row.split() for row in puzzle_input]
    moves = [(dir_vecs[c], int(mag)) for c, mag in moves]
    rope = [np.array([0, 0]) for _ in range(knots)]
    tail_visited = [rope[-1]]
    for dir_vec, magnitude in moves:
        for _ in range(magnitude):
            a = rope[0]
            rope[0] = a + dir_vec
            for x in range(1, knots):
                rope[x] = follow_head(rope[x - 1], rope[x])
            tail_visited.append(rope[-1])

    return len(set((v[0], v[1]) for v in tail_visited))


def solve_part_1(inp):
    return run(inp, 2)


def solve_part_2(inp):
    return run(inp, 10)


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 9)
    tokenized = tokenize(raw_input)[:-1]

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))

    solution_2 = solve_part_2(tokenized)
    print("Solution 2: " + str(solution_2))
