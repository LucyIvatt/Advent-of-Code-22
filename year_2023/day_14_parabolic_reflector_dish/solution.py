from helpers.aoc_utils import input_data, time_function, Direction


def tilt_puzzle(puzzle_input):
    while True:
        isUpdating = False
        for row in range(1, len(puzzle_input)):
            for col in range(len(puzzle_input)):
                if puzzle_input[row][col] == 'O':
                    dr, dc = Direction.NORTH.value
                    if puzzle_input[row + dr][col + dc] == ".":
                        puzzle_input[row + dr][col + dc] = "O"
                        puzzle_input[row][col] = "."
                        isUpdating = True
        if not isUpdating:
            break
    return puzzle_input


def calculate_load(tilted):
    load = 0
    for row in tilted:
        load += row.count('O') * (len(tilted[0]) - tilted.index(row))
    return load


def part_one(puzzle_input):
    puzzle_input = [list(string) for string in puzzle_input]
    tilted = tilt_puzzle(puzzle_input)
    return calculate_load(tilted)


def part_two(puzzle_input):
    pass


puzzle_input = input_data(
    "year_2023/day_14_parabolic_reflector_dish/input.txt")

p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 14: parabolic_reflector_dish")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
