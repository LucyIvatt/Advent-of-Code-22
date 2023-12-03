import re
from helpers.aoc_utils import input_data, get_adjacent_and_diagonal_coords

DIGIT_REGEX = pattern = r'\b\d+\b'

def part_one(puzzle_input):
    for i in range(len(puzzle_input)):
        matches = re.finditer(pattern, puzzle_input[i])

        for match in matches:
            number_coords = [(i, y) for y in range(match.start(), match.end())]
            print(number_coords)





puzzle_input = input_data("year_2023/day_03_gear_ratios/example.txt")
part_one(puzzle_input)

print("--------------------------------------")
print("Day 03: gear_ratios")
print("Part One Answer: ")
print("Part Two Answer: ")
print("--------------------------------------")
