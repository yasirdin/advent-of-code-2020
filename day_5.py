import logging
from typing import List, NamedTuple

logging.basicConfig(level=logging.INFO)


def parse_txt_file(filepath: str) -> List[str]:
    with open(filepath) as f:
        return f.read().splitlines()


input : List[str] = parse_txt_file('./day-5.txt')


class Seat(NamedTuple):
    row: int
    column: int

    @property
    def seat_id(self) -> int:
        return self.row * 8 + self.column


ROWS = list(range(0, 127 + 1))
COLUMNS = list(range(0, 7 + 1))


def get_seat(characters: str) -> Seat:
    rows = ROWS
    columns = COLUMNS

    for index, character in enumerate(characters, 0):
        if index < 7:
            number_of_rows = len(rows)
            if number_of_rows > 1:
                slice_index = int(number_of_rows / 2)
                rows = rows[:slice_index] if character == 'F' else rows[slice_index:]
        else:
            number_of_cols = len(columns)
            if number_of_cols > 1:
                slice_index = int(number_of_cols / 2)
                columns = columns[:slice_index] if character == 'L' else columns[slice_index:]

    return Seat(row=rows[0], column=columns[0])


assert get_seat(characters='FBFBBFFRLR') == Seat(row=44, column=5)
assert get_seat(characters='FBFBBFFRLR').seat_id == 357
assert get_seat(characters='BFFFBBFRRR') == Seat(row=70, column=7)
assert get_seat(characters='BFFFBBFRRR').seat_id == 567
assert get_seat(characters='FFFBBBFRRR') == Seat(row=14, column=7)
assert get_seat(characters='BBFFBBFRLL') == Seat(row=102, column=4)


def part_one(input: List[str]) -> int:
    return max([get_seat(characters).seat_id for characters in input])


logging.info(f'Part one answer: {part_one(input=input)}')


def part_two(input: List[str]) -> int:
    seat_ids = [get_seat(characters).seat_id for characters in input]

    my_seat = [
        seat for seat in range(min(seat_ids), max(seat_ids))
        if seat not in seat_ids
    ]

    return my_seat[0]


logging.info(f'Part two answer: {part_two(input=input)}')
