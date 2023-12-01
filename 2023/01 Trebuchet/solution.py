import re

# def part_one_original(puzzle_input):
#     digits = ["".join(filter(str.isdigit, string)) for string in puzzle_input]
#     return sum((int(f'{digit[0]}{digit[-1]}') for digit in digits))

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

def find_numbers(string, words_included=False):
    number_locations = {}

    if words_included:
        # Saves location index of worded numbers
        for word, number in NUMBER_DICT.items():
            for match in re.finditer(word, string):
                number_locations[match.start()]= str(number)

    # Saves location of digits
    for i in range(len(string)):
        if string[i].isdigit():
            number_locations[i]=string[i]
    
    # Sorts the numbers values by their indexes
    return [value for key, value in sorted(number_locations.items())]

def solution(puzzle_input, words_included=False):
    number_lists = [find_numbers(string, words_included) for string in puzzle_input]
    return sum((int(f'{numbers[0]}{numbers[-1]}')) for numbers in number_lists)

puzzle_input = input_data("2023/01 Trebuchet/input.txt")

print("--------------------------------------")
print("Day 01: Trebuchet")
print(f"Part One Answer: {solution(puzzle_input)}")
print(f"Part Two Answer: {solution(puzzle_input, True)}")
print("--------------------------------------")
