from functools import reduce
from helpers.aoc_utils import input_data, time_function
import re
from collections import defaultdict

PATTERN = re.compile(r'(.+)([=-])(\d*)')


def hash_alg(string):
    return reduce(lambda h, char: (h + ord(char)) * 17 % 256, string, 0)


class Lens():
    def __init__(self, label, value, box):
        self.label = label
        self.focal = value
        self.box = box

    def __repr__(self):
        return f"Lens({self.focal})"

    def focusing_power(self, pos):
        print(f"{1 + self.box=}")
        print(f"{pos=}")
        print(f"{self.focal=}")
        return (1 + self.box) * pos * self.focal


def part_one(puzzle_input):
    return sum(hash_alg(step) for step in puzzle_input[0].split(","))


def part_two(puzzle_input):
    steps = [step for step in puzzle_input[0].split(",")]
    boxes = defaultdict(dict)

    for step in steps:
        match = PATTERN.match(step)
        label, op, num = match.groups()
        hc = hash_alg(label)

        if op == "=":
            if label in boxes[hc].keys():
                boxes[hc][label].focal = int(num)
            else:
                boxes[hc][label] = Lens(label, int(num), hc)
        elif op == "-":
            if label in boxes[hc].keys():
                boxes[hc].pop(label)

    total_focus_power = 0
    for box in boxes.values():
        for pos, (label, lens) in enumerate(box.items()):
            total_focus_power += lens.focusing_power(pos+1)

    return total_focus_power


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
