from typing import List


def main():
    with open('./input.txt') as file:
        lines = file.readlines()
        just_numbers = map(only_numbers, lines)
        calibration_values = [int(f'{nums[0]}{nums[-1]}') for nums in just_numbers]
        print(sum(calibration_values))


def only_numbers(string: str) -> List[str]:
    return [c for c in string if c.isdigit()]


if __name__ == '__main__':
    main()
