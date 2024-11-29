from functools import reduce
from python.helpers.aoc_utils import input_data, time_function
import re
from collections import defaultdict

PATTERN = re.compile(r'(.+)([=-])(\d*)')


def hash_alg(string):
    return reduce(lambda h, char: (h + ord(char)) * 17 % 256, string, 0)


class Lens():
    def __init__(self, label, value, box):
        self.label = label
        self.focal_length = value
        self.box = box

    def focusing_power(self, pos):
        return (1 + self.box) * pos * self.focal_length


def part_one(puzzle_input):
    return sum(hash_alg(step) for step in puzzle_input[0].split(","))


def part_two(puzzle_input):
    boxes = defaultdict(dict)

    for step in puzzle_input[0].split(","):
        label, op, num = PATTERN.match(step).groups()
        hc = hash_alg(label)

        if op == "=":
            boxes[hc][label] = Lens(label, int(num), hc)
        elif op == "-":
            boxes[hc].pop(label, None)

    return sum(lens.focusing_power(pos + 1) for box in boxes.values() for pos, (_, lens) in enumerate(box.items()))


def main():
    puzzle_input = input_data("python/year_2023/day_15_lens_library/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 15: lens_library")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
