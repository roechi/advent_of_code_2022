from requests import get, post
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def load_puzzle_input(year: int, day: int) -> str:
    cookie = getenv('AOC_COOKIE')
    assert cookie

    response = get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': cookie})
    return response.content.decode(encoding='utf-8')


def submit_puzzle_solution(year: int, day: int, solution: str, level: int):
    cookie = getenv('AOC_COOKIE')
    assert cookie

    response = post(f'https://adventofcode.com/{year}/day/{day}/answer', data={'level': level, 'answer': solution}, cookies={'session': cookie})
    if 'Did you already complete it?' in response.text or 'one gold star' in response.text:
        print(f'Part {level} solved! Correct answer is {solution}')
    else:
        print(f'Part {level} not solved! {solution} is not the correct solution')
