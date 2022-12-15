import re
from collections import defaultdict


def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))


def input_data(filename):
    """Returns the data imported from file - dictionary of sensor locations
    and manhattan distances to nearest beacon.
    """
    with open(filename, 'r') as file:
        input = file.read().strip().split("\n")

    coords = [[int(x) for x in re.findall(r'-?\d+\.?\d*', line)]
              for line in input]

    beacon_locations = [(int(c[2]), int(c[3])) for c in coords]
    sens_dists = {(int(c[0]), int(c[1])): manhattan_distance(
        (c[0], c[1],), (c[2], c[3])) for c in coords}

    all_y = [y for coord in coords for y in (coord[1], coord[3])]
    all_x = [x for coord in coords for x in (coord[0], coord[2])]

    y_bounds = (min(all_y), max(all_y))
    x_bounds = (min(all_x), max(all_x))

    return beacon_locations, sens_dists, x_bounds, y_bounds


def convert_coord(x, y, min_x, min_y):
    return (x-min_x, y-min_y)


def build_grid(beacon_locations, sens_dists, x_bounds, y_bounds):
    """Builds a grid of the scan from the input data. Returns the grid."""
    min_x, max_x = x_bounds
    min_y, max_y = y_bounds

    x_length = max_x-min_x+1
    y_length = max_y-min_y+1

    grid = [["." for _ in range(x_length)] for _ in range(y_length)]
    for loc in beacon_locations:
        x, y = convert_coord(*loc, min_x, min_y)
        grid[y][x] = "B"
    for loc in sens_dists.keys():
        x, y = convert_coord(*loc, min_x, min_y)
        grid[y][x] = "S"
    return grid


def clear_area(grid, sensor, distance, min_x, min_y):
    """Clears the area around the sensor that is within the manhattan distance.
    """
    x, y = convert_coord(*sensor, min_x, min_y)
    y_coords = [y]
    i = 0
    while x-distance+i <= x:
        for cx in range(x-distance+i, x+distance+1-i):
            for cy in y_coords:
                if cx < 0 or cx >= len(grid[0]) or cy < 0 or cy >= len(grid):
                    continue
                elif grid[cy][cx] == ".":
                    grid[cy][cx] = "#"
        i += 1
        if len(y_coords) == 1:
            y_coords = [y+1, y-1]
        else:
            y_coords = [y_coords[0]+1, y_coords[1]-1]
    return grid


def clear_area_2(sensor, distance, Y_blocks):
    """Clears the area around the sensor"""
    x, y = sensor
    i = 0
    y_coords = [y]
    while x-distance+i <= x:
        for cy in y_coords:
            Y_blocks[cy].append((x-distance+i, x+distance+1-i))

        if len(y_coords) == 1:
            y_coords = [y+1, y-1]
        else:
            y_coords = [y_coords[0]+1, y_coords[1]-1]
        i += 1
    return Y_blocks


def part_one(input):
    # beacon_locations, sens_dists, x_bounds, y_bounds = input
    # grid = build_grid(*input)
    # for sensor, distance in sens_dists.items():
    #     grid = clear_area(grid, sensor, distance, x_bounds[0], y_bounds[0])

    # print("\n\n")

    # _, y = convert_coord(0, 10, x_bounds[0], y_bounds[0])
    # return grid[y].count("#")

    Y_blocks = defaultdict(list)
    beacon_locations, sens_dists, x_bounds, y_bounds = input
    for sensor, distance in sens_dists.items():
        Y_blocks = clear_area_2(sensor, distance, Y_blocks)

    print(Y_blocks[10])


input = input_data("day15/example.txt")

print("--------------------------------------")
print("Day 15: Beacon Exclusion Zone")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: ")
print("--------------------------------------")
