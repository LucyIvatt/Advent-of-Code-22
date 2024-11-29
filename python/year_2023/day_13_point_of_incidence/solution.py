from python.helpers.aoc_utils import input_data, time_function, transpose_list, split_by_empty_line
from itertools import groupby


def flip_symbol(pattern, row, col):
    """Flips the symbol at the specified location from (. -> #) or (# -> .)"""

    new = pattern[:]
    new[row] = new[row][:col] + \
        ('.' if new[row][col] == '#' else '#') + new[row][col+1:]
    return new


def scan_direction(pattern, horizontal=True, ignore=None):
    """Checks for either horizontal lines or symmetry or vertical. If value is passed via 
    ignore parameter, will not return a line of symmetry at this index.
    Returns tuple in the form (bool, int | None) where the bool represents if a value was found, 
    and int | None represents the found LoS location."""

    pattern = pattern if horizontal else transpose_list(pattern)
    size = len(pattern)

    for i in range(1, size):
        dx = min(i, size - i)
        top_range = range(i - dx, i)
        bottom_range = reversed(range(i, i + dx))

        if all(pattern[top] == pattern[bottom] for top, bottom in zip(top_range, bottom_range)):
            if ignore is None or i != ignore:
                return True, i

    return False, None


def part_one(puzzle_input):
    """Finds line of symmetry in each pattern and calculates score accordingly."""

    patterns = split_by_empty_line(puzzle_input)
    total_sum = 0

    for pattern in patterns:
        h_found, h_location = scan_direction(pattern, horizontal=True)
        if h_found:
            total_sum += 100 * h_location
        else:
            total_sum += scan_direction(pattern, horizontal=False)[1]

    return total_sum


def part_two(puzzle_input):
    """Finds line of symmetry in each pattern after flipping the correct symbol, 
    ignoring the original line of symmetry, and calculates score accordingly."""

    patterns = split_by_empty_line(puzzle_input)
    total_sum = 0
    for pattern in patterns:
        orig_h_loc = scan_direction(pattern, horizontal=True)[1]
        orig_v_loc = scan_direction(pattern, horizontal=False)[1]

        for r in range(len(pattern)):
            for c in range(len(pattern[0])):
                new_p = flip_symbol(pattern, r, c)

                h_found, h_loc = scan_direction(
                    new_p, horizontal=True, ignore=orig_h_loc)
                v_found, v_loc = scan_direction(
                    new_p, horizontal=False, ignore=orig_v_loc)

                if (h_found or v_found):
                    total_sum += h_loc * 100 if h_found else v_loc
                    break

            if (h_found or v_found):
                break

    return total_sum


def main():
    puzzle_input = input_data(
        "python/year_2023/day_13_point_of_incidence/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 13: point_of_incidence")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
