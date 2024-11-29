from python.helpers.aoc_utils import input_data, time_function
import re
import math

PATTERN = re.compile(r"(\w+) = \((\w+), (\w+)\)")


def find_num_steps(start, nodes, sequence, multiple_nodes=False):
    steps, current_node = 0, start

    while True:
        for direction in sequence:
            left_node, right_node = nodes[current_node]
            current_node = left_node if direction == "L" else right_node

            steps += 1

            if not multiple_nodes and current_node == "ZZZ":
                return steps
            elif multiple_nodes and current_node.endswith("Z"):
                return steps


def parse_input(puzzle_input):
    sequence = puzzle_input[0]
    nodes = {match.group(1): (match.group(2), match.group(
        3)) for input_string in puzzle_input[2:] if (match := PATTERN.match(input_string))}
    return sequence, nodes


def part_one(puzzle_input):
    sequence, nodes = parse_input(puzzle_input)
    return find_num_steps("AAA", nodes, sequence)


def part_two(puzzle_input):
    sequence, nodes = parse_input(puzzle_input)
    start_nodes = [node for node in nodes.keys() if node.endswith("A")]

    steps = [find_num_steps(node, nodes, sequence, True)
             for node in start_nodes]
    return math.lcm(*steps)


def main():
    puzzle_input = input_data("python/year_2023/day_08_haunted_wasteland/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 08: haunted_wasteland")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
