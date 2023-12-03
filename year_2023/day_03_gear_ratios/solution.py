import re
import string
from helpers.aoc_utils import input_data, get_adjacent_and_diagonal_coords

DIGIT_REGEX = pattern = r'\b\d+\b'

def part_one(puzzle_input):
    part_num_sum = 0
    for i in range(len(puzzle_input)):
        matches = re.finditer(pattern, puzzle_input[i])

        for match in matches:
            number_coords = [(i, y) for y in range(match.start(), match.end())]
            adj_coords = get_adjacent_and_diagonal_coords(number_coords, len(puzzle_input[i]), len(puzzle_input))
            has_symbols = any(puzzle_input[line][char] != '.' for line, char in adj_coords)
            
            if has_symbols:
                part_num_sum += int(match.group())
    return part_num_sum

puzzle_input = input_data("year_2023/day_03_gear_ratios/input.txt")


print("--------------------------------------")
print("Day 03: gear_ratios")
print(f"Part One Answer: {part_one(puzzle_input)}")
print("Part Two Answer: ")
print("--------------------------------------")
