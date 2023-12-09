from functools import reduce
from helpers.aoc_utils import input_data, time_function
import re
import math
import time

PATTERN = re.compile(r"(\w+) = \((\w+), (\w+)\)")


def find_num_steps(start, nodes, sequence, multiple_nodes=False):
    steps = 0
    current_node = start

    while True:
        for direction in sequence:

            if direction == "L":
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]

            steps += 1
            if not multiple_nodes and current_node == "ZZZ":
                return steps
            elif multiple_nodes and current_node.endswith("Z"):
                return steps


def part_one(puzzle_input):
    sequence = puzzle_input[0]
    nodes = {match.group(1): (match.group(2), match.group(
        3)) for input_string in puzzle_input[2:] if (match := PATTERN.match(input_string))}
    return find_num_steps("AAA", nodes, sequence)


def part_two(puzzle_input):
    sequence = puzzle_input[0]
    nodes = {match.group(1): (match.group(2), match.group(
        3)) for input_string in puzzle_input[2:] if (match := PATTERN.match(input_string))}
    start_nodes = [x for x in nodes.keys() if x.endswith("A")]

    steps = []
    for node in start_nodes:
        steps.append(find_num_steps(node, nodes, sequence, True))

    return math.lcm(*steps)


puzzle_input = input_data("year_2023/day_08_haunted_wasteland/input.txt")

p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 08: haunted_wasteland")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
