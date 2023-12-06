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
    seeds = {int(num): int(num)
             for num in puzzle_input[0].split(":")[1].split()}

    mappings = [list(group) for key, group in groupby(
        puzzle_input[1:], key=lambda x: x == "") if not key]

    for group in mappings:
        bands = [Bound(bound) for bound in group[1:]]
        for orig, seed in seeds.items():
            for band in bands:
                if band.value_in_range(seed):
                    seeds[orig] = band.map(seed)
                    break

    return min(seeds.values())


def find_overlapping_boundaries(bounds, extremes):
    overlapping_boundaries = []

    for bound in bounds:
        # Check for overlap with each extreme
        for extreme in extremes:
            if bound.source <= extreme <= (bound.source + bound.range):
                # Add overlapping boundaries to the list
                overlapping_boundaries.append(extreme)

    return overlapping_boundaries


def part_two(puzzle_input):
    numbers = [int(num) for num in puzzle_input[0].split()[1:]]
    extreme_seeds = {lower: [lower, lower + r]
                     for lower, r in zip(numbers[::2], numbers[1::2])}

    mappings = [list(group) for key, group in groupby(
        puzzle_input[1:], key=lambda x: x == "") if not key]

    bands = [Bound('5 0 3'), Bound('5 2 3')]
    extremes = [1, 3]

    overlaps = find_overlapping_boundaries(bands, extremes)
    print(overlaps)

    # print(extreme_seeds)

    # for group in mappings:
    #     bands = [Bound(bound) for bound in group[1:]]
    #     for orig, extremes in extreme_seeds.items():

    #         overlaps = find_overlapping_boundaries(bands, extremes)
    #         print(set(extremes + overlaps))

    # for seed in extreme_seeds:
    #     for band in bands:
    #         if band.value_in_range(seed):
    #             seeds[orig] = band.map(seed)
    #             break

    # print(seeds)
    # pass


puzzle_input = input_data(
    "year_2023/day_05_if_you_give_a_seed_a_fertilizer/example.txt")

p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 05: if_you_give_a_seed_a_fertilizer")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
