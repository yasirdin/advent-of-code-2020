import logging
from typing import List

from utils import parse_txt_file

logging.basicConfig(level=logging.INFO)


def parse_txt_file(filepath: str) -> List[int]:
    with open(filepath) as f:
        return [int(line) for line in f.readlines()]


input = parse_txt_file('./day-1.txt')

# Find the two entries which add to 2020.
# What do you get if you multiply them together?
def part_one(input: List[int]) -> int:
    for cost in input:
        other_cost = 2020 - cost
        if other_cost in input:
            return other_cost * cost

logging.info(f'Part one answer: {part_one(input=input)}')

# What is the product of three numbers which sum to 2020?
def part_two(input: List[int]) -> int:
    for first_cost in input:
        sum_of_other_two_numbers = 2020 - first_cost
        for second_cost in input:
            for third_cost in input:
                if (second_cost + third_cost) == sum_of_other_two_numbers:
                    return first_cost * second_cost * third_cost

logging.info(f'Part two answer: {part_two(input=input)}')
