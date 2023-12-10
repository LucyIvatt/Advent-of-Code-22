from helpers.aoc_utils import input_data, time_function, find_element_location_2d_list
from enum import Enum
import math
import time


class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, +1)
    SOUTH = (+1, 0)
    WEST = (0, -1)


# Directions in to direction out
SYMBOL_DIRS = {
    "|": {Direction.NORTH: Direction.NORTH, Direction.SOUTH: Direction.SOUTH},
    "-": {Direction.WEST: Direction.WEST, Direction.EAST: Direction.EAST},
    "7": {Direction.NORTH: Direction.WEST, Direction.EAST: Direction.SOUTH},
    "F": {Direction.WEST: Direction.SOUTH, Direction.NORTH: Direction.EAST},
    "J": {Direction.SOUTH: Direction.WEST, Direction.EAST: Direction.NORTH},
    "L": {Direction.SOUTH: Direction.EAST, Direction.WEST: Direction.NORTH},
}


def get_start(maze):
    start_pos = find_element_location_2d_list(maze, "S")

    diffs = [direction.value for direction in Direction]

    adj_coords = {Direction(direction): (start_pos[0] + direction[0], start_pos[1] + direction[1])
                  for direction in diffs}

    for direction, coord in adj_coords.items():
        symbol = maze[coord[0]][coord[1]]
        if symbol != "." and direction in SYMBOL_DIRS[symbol].keys():
            return coord, SYMBOL_DIRS[symbol][direction], direction, symbol


def part_one(puzzle_input, start_dir):
    maze = [[char for char in row] for row in puzzle_input]
    current_pos, prev_dir, next_dir, symbol = get_start(maze)

    node_list = ["S", symbol]

    while True:
        next_dir = SYMBOL_DIRS[symbol][next_dir]

        current_pos = (current_pos[0] + next_dir.value[0],
                       current_pos[1] + next_dir.value[1])

        symbol = maze[current_pos[0]][current_pos[1]]

        if symbol == "S":
            node_list.append("S")
            break

        node_list.append(symbol)

    return math.floor(len(node_list) / 2)


def part_two(puzzle_input):
    pass


puzzle_input = input_data("year_2023/day_10_pipe_maze/input.txt")

p1, p1_time = time_function(part_one, puzzle_input, Direction.EAST)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 10: pipe_maze")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")


# def find_connections(coord, maze, ignore_dir):
#     diff = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

#     adj_coords = {Direction(i): (coord[0] + diff[i][0], coord[1] + diff[i][1])
#                   for i in range(4)
#                   if (0 <= coord[0] + diff[i][0] < len(maze)) and
#                   (0 <= coord[1] + diff[i][1] < len(maze[i]))}

#     adj_values = {direction: maze[adj_coords[direction][0]][adj_coords[direction][1]]
#                   for direction in adj_coords.keys()}

#     for direction, value in adj_values.items():
#         valid_symbols = get_valid_symbols(direction)
#         if (value in valid_symbols or value == "S") and (direction != ignore_dir):
#             connection = (adj_coords[direction], value, direction)

#     return connection
