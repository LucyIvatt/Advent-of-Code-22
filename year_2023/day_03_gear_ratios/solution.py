import re
from collections import defaultdict 
from helpers.aoc_utils import input_data, get_adjacent_and_diagonal_coords

DIGIT_REGEX = r'\b\d+\b'

def part_one(puzzle_input):
    part_num_sum = 0
    for i, line in enumerate(puzzle_input):
        for match in re.finditer(DIGIT_REGEX, line):
            number_positions = [(i, y) for y in range(match.start(), match.end())]
            adj_coords = get_adjacent_and_diagonal_coords(number_positions, len(line), len(puzzle_input))

            if any(puzzle_input[line][char] != '.' for line, char in adj_coords):
                part_num_sum += int(match.group())

    return part_num_sum

def part_two(puzzle_input):
    gear_dict = defaultdict(list)
    for i in range(len(puzzle_input)):
        matches = re.finditer(DIGIT_REGEX, puzzle_input[i])

        for match in matches:
            number_coords = [(i, y) for y in range(match.start(), match.end())]
            adj_coords = get_adjacent_and_diagonal_coords(number_coords, len(puzzle_input[i]), len(puzzle_input))

            for line, char in adj_coords:
                if puzzle_input[line][char] != '.':
                    gear_dict[(line, char)].append(int(match.group()))
        
    return sum(numbers[0] * numbers[1] for numbers in gear_dict.values() if len(numbers) > 1)
    

puzzle_input = input_data("year_2023/day_03_gear_ratios/input.txt")



print("--------------------------------------")
print("Day 03: gear_ratios")
print(f"Part One Answer: {part_one(puzzle_input)}")
print(f"Part Two Answer: {part_two(puzzle_input)}")
print("--------------------------------------")
