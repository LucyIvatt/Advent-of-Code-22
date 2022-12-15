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
                Y_indices[P1_Y].append((x-distance+i, x+distance-i))

            elif not p1:
                if x-distance+i < 0:
                    sx = 0
                else:
                    sx = x-distance+i

                if x+distance-i > max_xy:
                    bx = max_xy
                else:
                    bx = x+distance-i

                if 0 <= cy <= max_xy:
                    Y_indices[cy].append((sx, bx))
        if len(y_coords) == 1:
            y_coords = [y+1, y-1]
        else:
            y_coords = [y_coords[0]+1, y_coords[1]-1]
        i += 1
    return Y_indices


def part_one(input):
    Y_indices = {P1_Y: list()}
    for sensor, distance in input.items():
        Y_indices = clear_area(sensor, distance, Y_indices)

    intervals = [[x, y] for x, y in Y_indices[P1_Y]]
    intervals = merge(intervals)
    sum = 0
    for x1, x2 in intervals:
        sum += x2-x1
    return sum


def is_overlaping(a, b):
    if b[0] >= a[0] and b[0] <= a[1]:
        return True
    elif a[1]+1 == b[0]:
        return True
    else:
        return False

# merge the intervals


def merge(arr):
    # sort the intervals by its first value
    arr.sort(key=lambda x: x[0])

    merged_list = []
    merged_list.append(arr[0])
    for i in range(1, len(arr)):
        pop_element = merged_list.pop()
        if is_overlaping(pop_element, arr[i]):
            new_element = pop_element[0], max(pop_element[1], arr[i][1])
            merged_list.append(new_element)
        else:
            merged_list.append(pop_element)
            merged_list.append(arr[i])
    return merged_list


def part_two(input):
    max_xy = 4_000_000
    Y_indices = {y: [] for y in range(max_xy+1)}
    for sensor, distance in input.items():
        print("Clearing sensor: " + str(sensor))
        Y_indices = clear_area(sensor, distance, Y_indices, max_xy, p1=False)
    for k, v in Y_indices.items():
        intervals = [[x, y] for x, y in Y_indices[k]]
        Y_indices[k] = merge(intervals)
        if len(Y_indices[k]) > 1:
            bx = Y_indices[k][0][1]
            by = k
            print(bx, by)
            break
    return bx * 4_000_000 + by


P1_Y = 10
input = input_data("day15/example.txt")

print("--------------------------------------")
print("Day 15: Beacon Exclusion Zone")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: " + str(part_two(input)))
print("--------------------------------------")
