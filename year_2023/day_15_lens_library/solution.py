from helpers.aoc_utils import input_data, time_function
import re
from collections import defaultdict

PATTERN = re.compile(r'(.+)([=-])(\d*)')


class Lens():
    def __init__(self, lens):
        self.input = lens

        match = PATTERN.match(lens)
        self.label, self.op, self.num = match.groups()

    def __hash__(self):
        hash_code = 0
        for char in self.input:
            hash_code += ord(char)
            hash_code *= 17
            hash_code %= 256
        return hash_code


def parse_step(input_str):
    match = PATTERN.match(input_str)
    A, B, C = match.groups()
    return A, B, C


def part_one(puzzle_input):
    sequence = [Lens(x) for x in puzzle_input[0].split(",")]
    return sum(hash(step) for step in sequence)


def part_two(puzzle_input):
    sequence = [Lens(x) for x in puzzle_input[0].split(",")]
    boxes = defaultdict(dict)

    # for step in sequence:
    #     hash_code = hash_algorithm(step)
    #     label, operation, num = parse_step(step)

    #     if operation == "=":
    #         boxes[hash_code]["value"] = int(num)


def main():
    puzzle_input = input_data("year_2023/day_15_lens_library/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 15: lens_library")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
