from helpers.aoc_utils import input_data, time_function, Direction


def save_state(grid):
    return hash(tuple(map(tuple, grid)))


def tilt_puzzle(puzzle_input, di):
    r_start = 1 if di == Direction.NORTH else 0
    r_end = (len(puzzle_input) -
             1) if di == Direction.SOUTH else len(puzzle_input)
    c_start = 1 if di == Direction.WEST else 0
    c_end = len(puzzle_input[0]) - \
        1 if di == Direction.EAST else len(puzzle_input[0])

    while True:
        isUpdating = False
        for row in range(r_start, r_end):
            for col in range(c_start, c_end):
                if puzzle_input[row][col] == 'O':
                    dr, dc = di.value
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
    tilted = tilt_puzzle(puzzle_input, Direction.NORTH)
    return calculate_load(tilted)


def part_two(puzzle_input):
    puzzle_input = [list(string) for string in puzzle_input]
    cycle = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]
    cycle_num = 1_000_000_000
    states = {}

    c = 0
    while c < cycle_num:
        for direction in cycle:
            puzzle_input = tilt_puzzle(puzzle_input, direction)

        state = save_state(puzzle_input)

        #fmt: off
        if state in states and c < 500:
            loop_length = c - states[state]
            print(f"loop! c={c} is also {states[state]}, so loop length is {loop_length}")
            print(f"you can fit {cycle_num // loop_length} full loops in, which puts you at {(cycle_num // loop_length) * loop_length}")
            distance_to_goal = cycle_num - c
            loop_length = c - states[state]
            c = cycle_num - distance_to_goal % loop_length
        #fmt: on

        states[save_state(puzzle_input)] = c
        c += 1

    return calculate_load(puzzle_input)


puzzle_input = input_data(
    "year_2023/day_14_parabolic_reflector_dish/input.txt")

p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 14: parabolic_reflector_dish")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
