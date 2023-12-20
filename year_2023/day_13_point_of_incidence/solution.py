from helpers.aoc_utils import input_data, time_function, transpose_list
from itertools import groupby


def scan_direction(pattern, horizontal=True):
    pattern = pattern if horizontal else transpose_list(pattern)

    for i in range(1, len(pattern)):
        dx = i if i <= (len(pattern) / 2) else (len(pattern) - i)
        if all(pattern[top] == pattern[bottom] for top, bottom in zip(range(i-dx, i), reversed(range(i, i+dx)))):
            return True, i
    return False, None


def part_one(puzzle_input):
    patterns = [list(group) for key, group in groupby(
        puzzle_input, key=lambda x: x == "") if not key]

    total_sum = 0

    for pattern in patterns:
        h_found, h_location = scan_direction(pattern, horizontal=True)
        if h_found:
            total_sum += 100 * h_location
        else:
            total_sum += scan_direction(pattern, horizontal=False)[1]

    return total_sum


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
