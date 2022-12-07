from functools import reduce

from connector import puzzle_connector


def tokenize(puzzle_input):
    return puzzle_input.split('\n')


def go_to(wd: str, fs: dict) -> dict:
    current_dir = fs

    for d in wd.split('/'):
        if d != '':
            current_dir = current_dir[d]

    return current_dir


def go_up(wd: str) -> str:
    wd = '/' + reduce(lambda a, b: a + '/' + b, wd.split('/')[:-1])
    return wd


def go_down(wd: str, dir: str) -> str:
    wd = wd + '/' + dir
    return wd


def size_below(dir: dict, size: int) -> bool:
    return get_size(dir) < size


def get_size(dir: dict):
    if not dir:
        return 0
    else:
        return sum([item[1] if type(item[1]) == int else get_size(item[1]) for item in dir.items()])


def find_all_below(fs: dict) -> int:
    if size_below(fs, 100000):
        return get_size(fs) + sum([find_all_below(item[1]) if type(item[1]) == dict else 0 for item in fs.items()])
    else:
        s = 0
        for item in fs.items():
            if type(item[1]) == dict:
                s += find_all_below(item[1])
        return s


def get_all_sizes(fs: dict) -> list:
    l = [get_size(fs)]

    for item in fs.items():
        if type(item[1]) == dict:
            l.extend(get_all_sizes(item[1]))

    return l


def solve_part_1(puzzle_input: str):
    fs = parse_input(puzzle_input)

    return find_all_below(fs)


def parse_input(puzzle_input):
    fs = dict()
    current_wd = ''
    current_dir_dict = fs
    for c in puzzle_input:
        match c.split(' '):
            case ['dir', name]:
                current_dir_dict[name] = dict()
            case ['$', 'cd', name]:
                if name == '..':
                    current_wd = go_up(current_wd)
                    current_dir_dict = go_to(current_wd, fs)
                else:
                    current_wd = go_down(current_wd, name)
                    current_dir_dict = go_to(current_wd, fs)
            case ['$', 'ls']:
                pass
            case [size, name]:
                current_dir_dict[name] = int(size)
            case [*rest]:
                pass
    return fs


def solve_part_2(puzzle_input: str):
    fs = parse_input(puzzle_input)

    total_size = get_size(fs)
    current_free = 70000000 - total_size
    min_free_required = 30000000 - current_free
    all_sizes = get_all_sizes(fs)

    return min([x for x in all_sizes if x > min_free_required])


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 7)
    tokenized = tokenize(raw_input)

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    puzzle_connector.submit_puzzle_solution(2022, 7, str(solution_1), 1)

    solution_2 = solve_part_2(tokenized)
    print("Solution 2: " + str(solution_2))
    puzzle_connector.submit_puzzle_solution(2022, 7, str(solution_2), 2)
