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
    sens_dists = {(int(c[0]), int(c[1])): manhattan_distance(
        (c[0], c[1],), (c[2], c[3])) for c in coords}

    return sens_dists


def clear_area(sensor, distance, Y_indices, max_xy=None, p1=True):
    """Clears the area around the sensor"""
    x, y = sensor
    i = 0
    y_coords = [y]

    if p1 and P1_Y not in range(y-distance, y+distance+1):
        return Y_indices

    if not p1 and (y-distance <= 0) and (y+distance+1 >= max_xy):
        return Y_indices

    while x-distance+i <= x:
        for cy in y_coords:
            if p1 and cy == P1_Y:
                for cx in range(x-distance+i, x+distance-i):
                    Y_indices[P1_Y].add(cx)
            elif not p1:
                for cx in range(x-distance+i, x+distance-i+1):
                    if 0 <= cx <= 20 and 0 <= cy <= 20:
                        Y_indices[cy].add(cx)
        if len(y_coords) == 1:
            y_coords = [y+1, y-1]
        else:
            y_coords = [y_coords[0]+1, y_coords[1]-1]
        i += 1
    return Y_indices


def part_one(input):
    Y_indices = {P1_Y: set()}
    for sensor, distance in input.items():
        Y_indices = clear_area(sensor, distance, Y_indices)
    return len(Y_indices[P1_Y])


def part_two(input):
    max_xy = 20
    Y_indices = {y: set() for y in range(max_xy+1)}
    for sensor, distance in input.items():
        print("Clearing area of sensor: " + str(sensor) +
              " with distance: " + str(distance))
        Y_indices = clear_area(sensor, distance, Y_indices, max_xy, p1=False)
    bx, by = find_beacon(Y_indices, max_xy)
    return bx * 4_000_000 + by


def find_beacon(Y_blocked_pos, max_xy):
    for y in range(max_xy):
        for x in range(max_xy):
            if x not in Y_blocked_pos[y]:
                return (x, y)


P1_Y = 10
input = input_data("day15/example.txt")

print("--------------------------------------")
print("Day 15: Beacon Exclusion Zone")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: " + str(part_two(input)))
print("--------------------------------------")
