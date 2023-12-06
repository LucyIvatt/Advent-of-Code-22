from helpers.aoc_utils import input_data, time_function
from collections import defaultdict
from math import prod

puzzle_input = input_data("year_2023/day_06_wait_for_it/input.txt")


def calc_distance(time, hold_time):
    return hold_time * (time-hold_time)


def part_one(puzzle_input):
    times = [int(num) for num in puzzle_input[0].split(":")[1].split()]
    distances = [int(num) for num in puzzle_input[1].split(":")[1].split()]
    ways_to_win = defaultdict(int)

    for race in range(len(times)):
        for hold_time in range(int(times[race])):
            distance = calc_distance(times[race], hold_time)
            if distance > distances[race]:
                ways_to_win[race] += 1

    return prod(ways_to_win.values())


def part_two(puzzle_input):
    pass


p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 06: wait_for_it")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
