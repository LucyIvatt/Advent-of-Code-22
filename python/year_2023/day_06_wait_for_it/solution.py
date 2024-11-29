from helpers.aoc_utils import input_data, time_function
from collections import defaultdict
from math import prod

puzzle_input = input_data("year_2023/day_06_wait_for_it/input.txt")


def ways_to_win(times, distances):
    return prod([sum(1 for hold_time in range(time) if hold_time * (time - hold_time) > distance)
                 for time, distance in zip(times, distances)])


def extract_num_list(input_str):
    return [int(num) for num in input_str.split(":")[1].split()]


def extract_num(input_str):
    return int(''.join(char for char in input_str if char.isdigit()))


def part_one(puzzle_input):
    times, distances = map(extract_num_list, puzzle_input[:2])
    return ways_to_win(times, distances)


def part_two(puzzle_input):
    time, distance = map(extract_num, puzzle_input[:2])
    return ways_to_win([time], [distance])


def main():
    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 06: wait_for_it")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
