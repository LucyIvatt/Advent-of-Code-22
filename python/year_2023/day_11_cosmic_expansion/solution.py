from python.helpers.aoc_utils import input_data, time_function, manhattan_distance
from itertools import combinations


def get_expand_locations(puzzle_input):
    rows = [r for r, row in enumerate(puzzle_input) if "#" not in row]
    cols = [c for c in range(len(puzzle_input[0])) if all(
        row[c] != "#" for row in puzzle_input)]
    return rows, cols


def solution(puzzle_input, expansion_size):
    rows, cols = get_expand_locations(puzzle_input)
    galaxy_locations = [(i, j) for i, row in enumerate(puzzle_input)
                        for j, value in enumerate(row) if value == "#"]

    pairs = list(combinations(galaxy_locations, 2))
    shortest_paths = 0

    for pair in pairs:
        r1, r2 = sorted([pair[0][0], pair[1][0]])
        c1, c2 = sorted([pair[0][1], pair[1][1]])

        shortest_paths += manhattan_distance(pair[0], pair[1])

        for r in rows:
            if r1 <= r <= r2:
                shortest_paths += expansion_size - 1

        for c in cols:
            if c1 <= c <= c2:
                shortest_paths += expansion_size - 1

    return shortest_paths


def main():
    puzzle_input = input_data("python/year_2023/day_11_cosmic_expansion/input.txt")

    p1, p1_time = time_function(solution, puzzle_input, 2)
    p2, p2_time = time_function(solution, puzzle_input, 1_000_000)

    print("--------------------------------------")
    print("Day 11: cosmic_expansion")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
