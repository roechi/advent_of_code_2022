from functools import cmp_to_key
from math import prod

from connector import puzzle_connector


def tokenize(puzzle_input) -> list[str]:
    return puzzle_input.split('\n')


def solve_part_1(puzzle_input: list):
    results = []

    while len(puzzle_input):
        first = eval(puzzle_input.pop(0))
        second = eval(puzzle_input.pop(0))
        puzzle_input.pop(0)
        results.append(ordered(first, second))

    return sum([i + 1 if v == -1 else 0 for i, v in enumerate(results)])


def ordered(a, b):
    result = 0

    for i in range(min(len(a), len(b))):
        match isinstance(a[i], list), isinstance(b[i], list):
            case True, True:
                result = ordered(a[i], b[i])
            case True, False:
                result = ordered(a[i], [b[i]])
            case False, True:
                result = ordered([a[i]], b[i])
            case _:
                result = (a[i] > b[i]) - (a[i] < b[i])

        if result:
            return result
    return (len(a) > len(b)) - (len(a) < len(b))

def solve_part_2(puzzle_input: list):
    parsed = [eval(l) for l in puzzle_input if l != '']

    parsed.sort(key=cmp_to_key(ordered))

    decoder_key = prod(i + 1 for i, v in enumerate(parsed) if ordered(v, [[2]]) == 0 or ordered(v, [[6]]) == 0)
    return decoder_key


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 13)
    #raw_input = '[1, 1, 3, 1, 1]\n[1, 1, 5, 1, 1]\n\n[[1], [2, 3, 4]]\n[[1], 4]\n\n[9]\n[[8, 7, 6]]\n\n[[4, 4], 4, 4]\n[[4, 4], 4, 4, 4]\n\n[7, 7, 7, 7]\n[7, 7, 7]\n\n[]\n[3]\n\n[[[]]]\n[[]]\n\n[1, [2, [3, [4, [5, 6, 7]]]], 8, 9]\n[1, [2, [3, [4, [5, 6, 0]]]], 8, 9]\n'

    tokenized = tokenize(raw_input)

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    #puzzle_connector.submit_puzzle_solution(2022, 13, str(solution_1), 1)

    inpt2 = tokenize(raw_input)
    inpt2.extend(['[[2]]', '[[6]]', ''])
    solution_2 = solve_part_2(inpt2)
    print("Solution 2: " + str(solution_2))
    #puzzle_connector.submit_puzzle_solution(2022, 13, str(solution_2), 2)
