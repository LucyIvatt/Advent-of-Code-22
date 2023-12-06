from helpers.aoc_utils import input_data, time_function
from itertools import groupby


class Bound():
    def __init__(self, bound_string):
        self.dest, self.source, self.range = map(
            int, bound_string.split())

    def value_in_range(self, value):
        return (value >= self.source) and (value < (self.source + self.range))

    def map(self, value):
        return value + (self.dest - self.source)

    def __repr__(self):
        return f"Bound({self.dest=}, {self.source=}, {self.range=})"


def part_one(puzzle_input):
    seeds = [int(num) for num in puzzle_input[0].split(":")[1].split()]

    mappings = [list(group) for key, group in groupby(
        puzzle_input[1:], key=lambda x: x == "") if not key]

    for group in mappings:
        bands = [Bound(bound) for bound in group[1:]]
        for seed_i in range(len(seeds)):
            for band in bands:
                if band.value_in_range(seeds[seed_i]):
                    seeds[seed_i] = band.map(seeds[seed_i])
                    break

    return min(seeds)


def part_two(puzzle_input):
    pass


puzzle_input = input_data(
    "year_2023/day_05_if_you_give_a_seed_a_fertilizer/example.txt")

p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 05: if_you_give_a_seed_a_fertilizer")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
