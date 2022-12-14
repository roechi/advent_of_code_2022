import copy
from functools import reduce
from itertools import accumulate
from typing import List, Callable
from connector import puzzle_connector
import re


def tokenize(puzzle_input) -> list[str]:
    return puzzle_input.split('\n')


class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], bool]
    if_true_target: int
    if_false_target: int
    worry_decrease: bool
    test_number: int

    def __init__(self, items, operation, test, true_target, false_target, test_num, worry_decrease=True):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true_target = true_target
        self.if_false_target = false_target
        self.worry_decrease = worry_decrease
        self.test_number = test_num

    def inspect(self, item: int) -> int:
        return self.operation(item)

    def perform_test(self, item: int) -> bool:
        return self.test(item)

    def handle_next_item(self) -> [int, int]:
        item = self.items.pop(0)
        inspected = self.inspect(item)
        if self.worry_decrease:
            inspected = inspected // 3

        test_result = self.perform_test(inspected)
        if test_result:
            return inspected, self.if_true_target
        else:
            return inspected, self.if_false_target

    def has_items(self):
        return len(self.items) > 0

    def give_item(self, item: int):
        self.items.append(item)


def parse_monkey_input(inpt: list[str], worry_decrease: bool):
    item_pattern = re.compile('([0-9]+)')
    operation_pattern = re.compile('new = old (.) ([0-9]+|old)')
    test_pattern = re.compile('divisible by ([0-9]+)$')
    true_pattern = re.compile('If true: throw to monkey ([0-9]+)$')
    false_pattern = re.compile('If false: throw to monkey ([0-9]+)$')

    monkeys = []

    while inpt:
        inpt.pop(0)
        items_raw = inpt.pop(0)
        items_matched = item_pattern.findall(items_raw)
        items = [int(i) for i in items_matched]

        operation = None
        operation_raw = inpt.pop(0)
        operation_rules = []
        operation_rules = operation_pattern.findall(operation_raw)
        operator_rules = copy.copy(operation_rules[0])
        operator = operator_rules[0]
        operand = operator_rules[1]
        if operator == '+':
            if operand == 'old':
                operation = lambda x: x + x
            else:
                operation = lambda x, op=operand: x + int(op)
        else:
            if operand == 'old':
                operation = lambda x: x * x
            else:
                operation = lambda x, op=operand: x * int(op)

        test_raw = inpt.pop(0)
        test_rule = test_pattern.findall(test_raw)[0]
        test = lambda x, div=test_rule: x % int(div) == 0
        true_target = int(true_pattern.findall(inpt.pop(0))[0])
        false_target = int(false_pattern.findall(inpt.pop(0))[0])

        monkey = Monkey(
            items,
            operation,
            test,
            true_target,
            false_target,
            test_num=int(test_rule),
            worry_decrease=worry_decrease
        )
        monkeys.append(monkey)

        inpt.pop(0)
    return monkeys

def solve_part_1(puzzle_input: list):
    monkeys = parse_monkey_input(puzzle_input, worry_decrease=True)

    inspections = [0 for monkey in monkeys]
    for round in range(20):
        for id, monkey in enumerate(monkeys):
            while monkey.has_items():
                item, target = monkey.handle_next_item()
                monkeys[target].give_item(item)
                inspections[id] += 1

    inspections.sort()
    return inspections[-1] * inspections[-2]


def solve_part_2(puzzle_input: list):
    monkeys = parse_monkey_input(puzzle_input, worry_decrease=False)

    inspections = [0 for monkey in monkeys]
    for round in range(10000):
        for id, monkey in enumerate(monkeys):
            while monkey.has_items():
                item, target = monkey.handle_next_item()
                item_reduced = item % (reduce(lambda a, b: a * b, [monkey.test_number for monkey in monkeys]))
                monkeys[target].give_item(item_reduced)
                inspections[id] += 1

        print(f'After round {round}:')
        for id, monkey in enumerate(monkeys):
            print(f'monkey {id} inspected {inspections[id]} items and holds: {monkey.items}')

    inspections.sort()
    return inspections[-1] * inspections[-2]


if __name__ == '__main__':
    raw_input = puzzle_connector.load_puzzle_input(2022, 11)
    #raw_input = 'Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n    If true: throw to monkey 2\n    If false: throw to monkey 3\n\nMonkey 1:\n  Starting items: 54, 65, 75, 74\n  Operation: new = old + 6\n  Test: divisible by 19\n    If true: throw to monkey 2\n    If false: throw to monkey 0\n\nMonkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by 13\n    If true: throw to monkey 1\n    If false: throw to monkey 3\n\nMonkey 3:\n  Starting items: 74\n  Operation: new = old + 3\n  Test: divisible by 17\n    If true: throw to monkey 0\n    If false: throw to monkey 1\n'
    tokenized = tokenize(raw_input)

    solution_1 = solve_part_1(tokenized)
    print("Solution 1: " + str(solution_1))
    #puzzle_connector.submit_puzzle_solution(2022, 11, str(solution_1), 1)

    solution_2 = solve_part_2(tokenize(raw_input))
    print("Solution 2: " + str(solution_2))
    puzzle_connector.submit_puzzle_solution(2022, 11, str(solution_2), 2)
