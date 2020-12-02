from typing import List

def parse_txt_file(filepath: str) -> List[int]:
    with open(filepath) as f:
        return [int(line) for line in f.readlines()]
