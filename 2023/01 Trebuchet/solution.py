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

def find_number_locations(puzzle_input):
    modified_input = []

    for string in puzzle_input:
        number_locations = {}

        # Saves location index of worded numbers
        for word, number in NUMBER_DICT.items():
            ind = string.find(word)
            if ind != -1: number_locations[ind]= str(number)
        
        # Saves location of digits
        for i in range(len(string)):
            if string[i].isdigit():
                number_locations[i]=string[i]

        modified_input.append(number_locations)
    return modified_input

def part_two(puzzle_input):
    modified_input = find_number_locations(puzzle_input)

    ans = 0
    for number_locations in modified_input:
        ordered_numbers = [value for key, value in sorted(number_locations.items())]
        calibration_value = str(ordered_numbers[0]) + str(ordered_numbers[-1])
        ans += int(calibration_value)
    return ans

puzzle_input = input_data("2023/01 Trebuchet/input.txt")

print("--------------------------------------")
print("Day 01: Trebuchet")
print(f"Part One Answer: {part_one(puzzle_input)}")
print(f"Part Two Answer: {part_two(puzzle_input)}")
print("--------------------------------------")
