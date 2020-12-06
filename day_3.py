import logging
from typing import List, Tuple

from utils import parse_txt_file

logging.basicConfig(level=logging.INFO)


def parse_txt_file(filepath: str) -> List[str]:
    with open(filepath) as f:
        return [str(line) for line in f.read().splitlines()]  # .readlines() results in "\n" characters


input: List[str] = parse_txt_file('./day-3.txt')


def part_one(input: List[str], slope: Tuple[int, int]) -> int:
    right, down = slope

    line_length = len(input[0])

    tree_counter = 0
    for index, down in enumerate(range(down, len(input), down), 1):
        right_updated = (index * right) % line_length
        position = input[down][right_updated]
        if position == '#':
            tree_counter += 1

    return tree_counter


test_input = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#',
]

# Test using test input
assert part_one(input=test_input, slope=(3, 1)) == 7

logging.info(f'Part one answer: {part_one(input=input, slope=(3, 1))}')

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def part_two(input: List[str], slopes: List[Tuple[int, int]]) -> int:
    tree_counts = [
        part_one(input=input, slope=slope) for slope in slopes
    ]

    from functools import reduce
    # functools.reduce applies a function of two arguments cumulatively
    # to the items of an iterable from left to right, so as to reduce the
    # iterable to a single value.
    return reduce(lambda x, y: x*y, tree_counts)


logging.info(f'Part two answer: {part_two(input=input, slopes=slopes)}')
