from helpers.aoc_utils import input_data, time_function

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.


def hash_algorithm(input_str):
    hash_code = 0
    for char in input_str:
        hash_code += ord(char)
        hash_code *= 17
        hash_code %= 256
    return hash_code


def part_one(puzzle_input):
    sequence = [x for x in puzzle_input[0].split(",")]
    return sum(hash_algorithm(step) for step in sequence)


def part_two(puzzle_input):
    pass


def main():
    puzzle_input = input_data("year_2023/day_15_lens_library/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 15: lens_library")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
