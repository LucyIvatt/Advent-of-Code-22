from itertools import groupby
import time
from enum import Enum


def input_data(filename):
    """Returns the data imported from file - 
    """
    with open(filename, "r") as file:
        puzzle_input = [line.strip() for line in file.readlines()]
        return puzzle_input


def get_adjacent_coords(coords, x_limit, y_limit, diagonal=False):
    '''Returns all of the adjacent coordinates, including diagonals) for a list of coordinates. Removes any duplicates and any coordinates
    that were present in the original input.'''
    if diagonal:
        directions = [(dx, dy) for dx in range(-1, 2)
                      for dy in range(-1, 2) if (dx, dy) != (0, 0)]
    else:
        directions = [(dx, dy) for dx in range(-1, 2)
                      for dy in range(-1, 2) if (dx, dy) != (0, 0) and (dx == 0 or dy == 0)]

    adjecent_coords = []

    for coord in coords:
        x, y = coord
        adjecent_coords += [
            (x + dx, y + dy) for dx, dy in directions
            if 0 <= x + dx < x_limit and 0 <= y + dy < y_limit
        ]

    return set([coord for coord in adjecent_coords if coord not in coords])


def time_function(func, *args):
    start_time = time.time()
    result = func(*args)
    elapsed_time = time.time() - start_time
    return result, elapsed_time


def find_element_location_2d_list(matrix, target):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == target:
                return (i, j)
    return None


def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


def transpose_list(lst):
    return [list(map(str, column)) for column in zip(*lst)]


class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, +1)
    SOUTH = (+1, 0)
    WEST = (0, -1)


def split_by_empty_line(puzzle_input):
    """Splits the puzzle input into patterns by empty line."""
    return [list(group) for key, group in groupby(puzzle_input, key=lambda x: x == "") if not key]
