from requests import get, post
from os import getenv
from dotenv import load_dotenv

load_dotenv()
user_header = 'github.com/roechi/advent_of_code_2022/blob/main/connector/puzzle_connector.py by roechi@posteo.de'

def load_puzzle_input(year: int, day: int) -> str:
    cookie = getenv('AOC_COOKIE')
    assert cookie

    cookies = {'session': cookie}
    headers = {'User-Agent': user_header}
    response = get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies, headers=headers)
    return response.content.decode(encoding='utf-8')


def submit_puzzle_solution(year: int, day: int, solution: str, level: int):
    cookie = getenv('AOC_COOKIE')
    assert cookie

    cookies = {'session': cookie}
    headers = {'User-Agent': user_header}
    response = post(f'https://adventofcode.com/{year}/day/{day}/answer', data={'level': level, 'answer': solution}, cookies=cookies, headers=headers)
    if 'Did you already complete it?' in response.text or 'one gold star' in response.text:
        print(f'Part {level} solved! Correct answer is {solution}')
    else:
        print(f'Part {level} not solved! {solution} is not the correct solution')
