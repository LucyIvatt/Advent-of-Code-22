from helpers.aoc_utils import input_data, time_function, manhattan_distance
from itertools import combinations


def get_expand_locations(puzzle_input):
    rows, cols = [], []

    # Checks and expands rows
    for r in range(len(puzzle_input)):
        if "#" not in puzzle_input[r]:
            rows.append(r)

    # Checks and expands columns
    for c in range(len(puzzle_input[0])):
        if not any(row[c] == "#" for row in puzzle_input):
            cols.append(c)
    return rows, cols


def solution(puzzle_input, expansion_size):
    rows, cols = get_expand_locations(puzzle_input)

    galaxy_locations = []
    for i, row in enumerate(puzzle_input):
        for j, value in enumerate(row):
            if value == "#":
                galaxy_locations.append((i, j))

    pairs = list(combinations(galaxy_locations, 2))
    sps = 0

    for pair in pairs:
        pair_sp = 0
        r1, c1 = pair[0]
        r2, c2 = pair[1]

        r1, r2 = sorted([pair[0][0], pair[1][0]])
        c1, c2 = sorted([pair[0][1], pair[1][1]])

        pair_sp += manhattan_distance(pair[0], pair[1])

        for r in rows:
            if r in range(r1, r2+1):
                pair_sp += expansion_size - 1

        for c in cols:
            if c in range(c1, c2+1):
                pair_sp += expansion_size - 1

        sps += pair_sp

    return sps


puzzle_input = input_data("year_2023/day_11_cosmic_expansion/input.txt")

p1, p1_time = time_function(solution, puzzle_input, 2)
p2, p2_time = time_function(solution, puzzle_input, 1_000_000)

print("--------------------------------------")
print("Day 11: cosmic_expansion")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
