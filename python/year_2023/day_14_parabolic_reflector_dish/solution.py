from helpers.aoc_utils import input_data, time_function, Direction

TOTAL_CYCLES = 1_000_000_000


def tilt_puzzle(puzzle_input, di):
    #fmt:off
    r_start = 1 if di == Direction.NORTH else 0
    r_end = (len(puzzle_input) - 1) if di == Direction.SOUTH else len(puzzle_input)
    c_start = 1 if di == Direction.WEST else 0
    c_end = len(puzzle_input[0]) - 1 if di == Direction.EAST else len(puzzle_input[0])
    #fmt:on

    while True:
        is_updating = False
        for row in range(r_start, r_end):
            for col in range(c_start, c_end):
                if puzzle_input[row][col] == 'O':
                    dr, dc = di.value
                    if puzzle_input[row + dr][col + dc] == ".":
                        puzzle_input[row + dr][col + dc] = "O"
                        puzzle_input[row][col] = "."
                        is_updating = True
        if not is_updating:
            break
    return puzzle_input


def calculate_load(tilted):
    return sum(row.count('O') * (len(tilted[0]) - index) for index, row in enumerate(tilted))


def part_one(puzzle_input):
    puzzle_input = [list(string) for string in puzzle_input]
    tilted = tilt_puzzle(puzzle_input, Direction.NORTH)
    return calculate_load(tilted)


def save_state(grid):
    return hash(tuple(map(tuple, grid)))


def part_two(puzzle_input):
    puzzle_input = [list(string) for string in puzzle_input]
    cycle = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]
    states = {}

    i = 0
    while i < TOTAL_CYCLES:
        # Runs a single NWSE cycle and calculates the hash of the new state
        for direction in cycle:
            puzzle_input = tilt_puzzle(puzzle_input, direction)
        state = save_state(puzzle_input)

        # Skips cycles when a loop is found
        if state in states and i < 500:
            loop_length = i - states[state]
            remaining_cycles = TOTAL_CYCLES - i
            i = TOTAL_CYCLES - (remaining_cycles % loop_length)

        # Saves the state to compare and find loops
        states[state] = i
        i += 1

    return calculate_load(puzzle_input)


def main():
    puzzle_input = input_data(
        "year_2023/day_14_parabolic_reflector_dish/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 14: parabolic_reflector_dish")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
