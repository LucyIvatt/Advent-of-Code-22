import re
from collections import defaultdict 
from helpers.aoc_utils import input_data, get_adjacent_coords

DIGIT_REGEX = r'\b\d+\b'

def process_matches(puzzle_input, p2=False):
    result = defaultdict(list) if p2 else 0

    for i, line in enumerate(puzzle_input):
        for match in re.finditer(DIGIT_REGEX, line):
            number_positions = [(i, y) for y in range(match.start(), match.end())]
            adj_coords = get_adjacent_coords(coords=number_positions, x_limit=len(line), y_limit=len(puzzle_input), diagonal=True)

            if not p2 and any(puzzle_input[line][char] != '.' for line, char in adj_coords):
                result += int(match.group()) # sums part numbers that are adjacent to a symbol which is not '.'
            
            if p2: # adds part numbers to dictionary with their adjacent gear as the key
                for adj_line, char in adj_coords:
                    if puzzle_input[adj_line][char] != '.':
                        result[(adj_line, char)].append(int(match.group()))
    return result

def part_one(puzzle_input):
    '''Adds together all part numbers that have a gear symbol adjacent to them.'''
    return process_matches(puzzle_input)

def part_two(puzzle_input):
    '''Adds gear symbols to a dictionary based on their location, with values being the part numbers that are adjacent.
        Returns sum of the part numbers for gears with more than 1 part.'''
    return sum(numbers[0] * numbers[1] for numbers in process_matches(puzzle_input, p2=True).values() if len(numbers) > 1)

puzzle_input = input_data("year_2023/day_03_gear_ratios/input.txt")

print("--------------------------------------")
print("Day 03: gear_ratios")
print(f"Part One Answer: {part_one(puzzle_input)}")
print(f"Part Two Answer: {part_two(puzzle_input)}")
print("--------------------------------------")
