import logging
import re
from typing import Dict, List, NamedTuple, Optional, Tuple

logging.basicConfig(level=logging.INFO)

# We use a dictionary here since each passport has
# varying rates of completion.
Passport = Dict[str, str]


def parse_txt_file(filepath: str) -> List[str]:
    with open(filepath) as f:
        text = f.read().split('\n\n')  # Split on empty line
        # Remove remaining "\n" and strip leading and trailing whitespace, if any
        return [
            passport_string.replace('\n', ' ').strip(' ') for passport_string in text
        ]


input: List[str] = parse_txt_file('./day-4.txt')


def get_passport_from_string(passport_string: str) -> Passport:
    passport_fields = passport_string.split(' ')

    passport: Passport = {}
    for field in passport_fields:
        key, value = field.split(':')
        passport[key] = value

    return passport


def check_passport_valid_one(passport: Passport) -> int:
    mandatory_fields = [
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
    ]
    if set(mandatory_fields).issubset(set(passport.keys())):
        return 1
    else:
        return 0


def part_one(input: List[str]) -> int:
    passports = list(map(get_passport_from_string, input))
    number_of_valid_passports: int = sum(list(map(check_passport_valid_one, passports)))
    return number_of_valid_passports


logging.info(f'Part one answer: {part_one(input=input)}')


def check_valid_height(height: str) -> bool:
    number, unit = height[:-2], height[-2:]
    if (unit == 'cm'):
        return (150 <= int(number) <= 193)
    elif (unit == 'in'):
        return (59 <= int(number) <= 76)
    else:
        return False


def check_passport_valid_two(passport: Passport) -> int:
    mandatory_fields = [
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
    ]
    if set(mandatory_fields).issubset(set(passport.keys())):
        return int(all([
            1920 <= int(passport['byr']) <= 2002,
            2010 <= int(passport['iyr']) <= 2020,
            2020 <= int(passport['eyr']) <= 2030,
            check_valid_height(height=passport['hgt']),
            re.match(r"^#[0-9a-f]{6}$", passport['hcl']),
            passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            re.match(r"^[0-9]{9}$", passport['pid'])
        ]))
    else:
        return 0


def part_two(input: List[str]) -> int:
    passports = list(map(get_passport_from_string, input))
    number_of_valid_passports: int = sum(list(map(check_passport_valid_two, passports)))
    return number_of_valid_passports


logging.info(f'Part two answer: {part_two(input=input)}')
