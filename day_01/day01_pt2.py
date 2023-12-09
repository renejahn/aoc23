from typing import Callable, List
from functools import reduce


DIGIT_STRING_TRANSLATION_MAP = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

REPLACE_FUNCS = [lambda s: s.replace(k, v) for k, v in DIGIT_STRING_TRANSLATION_MAP.items()]


def main():
    with open('./input.txt') as file:
        lines = file.readlines()
        numerized_lines = map(numerize_string_digits, lines)
        just_numbers = map(only_numbers, numerized_lines)
        calibration_values = [int(f'{nums[0]}{nums[-1]}') for nums in just_numbers]
        print(sum(calibration_values))


def numerize_string_digits(string: str) -> str:
    replace_multiple = compose_functions(REPLACE_FUNCS)
    return replace_multiple(string)


def only_numbers(string: str) -> List[str]:
    return [c for c in string if c.isdigit()]


def compose_functions(funcs: List[Callable[[str], str]]) -> Callable[[str], str]:
    return reduce(
        lambda f, g: lambda x: f(g(x)),
        funcs,
        lambda x: x)


if __name__ == '__main__':
    main()
