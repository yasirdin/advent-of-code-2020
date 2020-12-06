import logging
from typing import List, Tuple


logging.basicConfig(level=logging.INFO)


def parse_txt_file(filepath: str) -> List[int]:
    with open(filepath) as f:
        return [str(line) for line in f.readlines()]


def parse_line(line: str) -> tuple:
    policy, password = tuple(line.split(':'))
    # Parse the policy
    numbers, letter = tuple(policy.split(' '))
    min_number, max_number = tuple(numbers.split('-'))
    min_number, max_number = int(min_number), int(max_number)
    # Parse the password
    password = password.strip(' ')  # Strip whitespace

    return min_number, max_number, letter, password

input = parse_txt_file('./day-2.txt')


def part_one(input: List[str]) -> int:
    valid_password_counter = 0
    for line in input:
        min_number, max_number, letter, password = parse_line(line)
        # Check password against policy
        if (min_number <= password.count(letter) <= max_number):
            valid_password_counter += 1

    return valid_password_counter

logging.info(f'Part one answer: {part_one(input=input)}')


def part_two(input: List[str]) -> int:
    valid_password_counter = 0
    for line in input:
        min_number, max_number, letter, password = parse_line(line)
        # Translate min and max to play nice with index 0
        min_number, max_number = min_number - 1, max_number - 1
        # Check if letter exists exactly once in each of the positions
        if (int(password[min_number] == letter) + int(password[max_number] == letter)) == 1:
            valid_password_counter += 1

    return valid_password_counter

logging.info(f'Part two answer: {part_two(input=input)}')
