from helpers.aoc_utils import input_data, time_function, transpose_list
from itertools import groupby
import copy


def scan_direction(pattern, horizontal=True, ignore=None):
    pattern = pattern if horizontal else transpose_list(pattern)

    for i in range(1, len(pattern)):
        dx = i if i <= (len(pattern) / 2) else (len(pattern) - i)
        if all(pattern[top] == pattern[bottom] for top, bottom in zip(range(i-dx, i), reversed(range(i, i+dx)))):
            if ignore == None:
                return True, i
            else:
                if i != ignore:
                    return True, i
    return False, None


def part_one(puzzle_input):
    patterns = [list(group) for key, group in groupby(
        puzzle_input, key=lambda x: x == "") if not key]

    total_sum = 0

    for pattern in patterns:
        h_found, h_location = scan_direction(pattern, horizontal=True)
        if h_found:
            total_sum += 100 * h_location
        else:
            total_sum += scan_direction(pattern, horizontal=False)[1]

    return total_sum


def part_two(puzzle_input):
    patterns = [list(group) for key, group in groupby(
        puzzle_input, key=lambda x: x == "") if not key]

    total_sum = 0

    for pattern in patterns:
        o_h_found, orig_h_loc = scan_direction(pattern, horizontal=True)
        o_v_found, orig_v_loc = scan_direction(pattern, horizontal=False)

        for r in range(len(pattern)):
            for c in range(len(pattern[0])):
                new_p = copy.deepcopy(pattern)

                row = new_p[r]

                if row[c] == "#":
                    new_p[r] = row[:c] + "." + row[c+1:]
                else:
                    new_p[r] = row[:c] + "#" + row[c+1:]

                h_found, h_loc = scan_direction(
                    new_p, horizontal=True, ignore=orig_h_loc)
                v_found, v_loc = scan_direction(
                    new_p, horizontal=False, ignore=orig_v_loc)

                if h_found and h_loc != orig_h_loc:
                    total_sum += h_loc * 100
                    break
                elif v_found and v_loc != orig_v_loc:
                    total_sum += v_loc
                    break
            if (h_found and h_loc != orig_h_loc) or (v_found and v_loc != orig_v_loc):
                break

    return total_sum


puzzle_input = input_data("year_2023/day_13_point_of_incidence/input.txt")

p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 13: point_of_incidence")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
