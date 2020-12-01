from typing import List

def parse_txt_file(filepath: str) -> List[int]:
    with open(filepath) as f:
        return [int(mass) for mass in f.readlines()]
