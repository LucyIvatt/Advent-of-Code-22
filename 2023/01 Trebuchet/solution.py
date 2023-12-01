import re

NUMBER_DICT = {'one':   1, 
               'two':   2, 
               'three': 3, 
               'four':  4, 
               'five':  5, 
               'six':   6, 
               'seven': 7, 
               'eight': 8, 
               'nine':  9}

def input_data(filename):
    """Returns the data imported from file - 
    """
    file = open(filename, "r")
    puzzle_input = file.readlines()
    file.close()
    return puzzle_input

def part_one(puzzle_input):
    digits = ["".join(filter(str.isdigit, string)) for string in puzzle_input]
    return sum((int(f'{digit[0]}{digit[-1]}') for digit in digits))

def find_numbers(string):
    number_locations = {}

    # Saves location index of worded numbers
    for word, number in NUMBER_DICT.items():
        for match in re.finditer(word, string):
            number_locations[match.start()]= str(number)
    # Saves location of digits
    for i in range(len(string)):
        if string[i].isdigit():
            number_locations[i]=string[i]
    return [value for key, value in sorted(number_locations.items())]

def part_two(puzzle_input):
    ans = 0
    for string in puzzle_input:
        ordered_numbers = find_numbers(string)
        ans += int(f'{ordered_numbers[0]}{ordered_numbers[-1]}')
    return ans

puzzle_input = input_data("2023/01 Trebuchet/input.txt")

print("--------------------------------------")
print("Day 01: Trebuchet")
print(f"Part One Answer: {part_one(puzzle_input)}")
print(f"Part Two Answer: {part_two(puzzle_input)}")
print("--------------------------------------")
