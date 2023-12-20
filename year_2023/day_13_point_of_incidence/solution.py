from helpers.aoc_utils import input_data, time_function
from itertools import groupby


def find_mirrors(pattern):
    # Horizontal
    for row in range(1, len(pattern)):
        dy = row if row <= (len(pattern) / 2) else len(pattern) - row

        if all(pattern[top] == pattern[bottom] for top, bottom in zip(range(row-dy, row), reversed(range(row, row+dy)))):
            return 100 * row

    # Vertical
    trans_pattern = [list(map(str, column)) for column in zip(*pattern)]

    for col in range(1, len(pattern[0])):
        dx = col if col <= (len(pattern[0]) / 2) else len(pattern[0]) - col
        if all(trans_pattern[top] == trans_pattern[bottom] for top, bottom in zip(range(col-dx, col), reversed(range(col, col+dx)))):
            return col


def part_one(puzzle_input):
    patterns = [list(group) for key, group in groupby(
        puzzle_input, key=lambda x: x == "") if not key]

    return sum(find_mirrors(pattern) for pattern in patterns)


def part_two(puzzle_input):
    pass


puzzle_input = input_data("year_2023/day_13_point_of_incidence/input.txt")

p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 13: point_of_incidence")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
