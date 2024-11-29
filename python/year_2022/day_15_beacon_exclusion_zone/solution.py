import re


def manhattan_distance(point1, point2):
    """Returns manhattan distance between two points."""
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))


def input_data(filename):
    """Returns the data imported from file - dictionary of sensor locations
    and manhattan distances to nearest beacon.
    """
    with open(filename, 'r') as file:
        input = file.read().strip().split("\n")

    coords = [[int(x) for x in re.findall(r'-?\d+\.?\d*', line)]
              for line in input]
    return {(int(c[0]), int(c[1])): manhattan_distance(
        (c[0], c[1],), (c[2], c[3])) for c in coords}


def clear_area(sensor, distance, Y_indices, bound, p1=True):
    """Clears the area around the sensor."""
    x, y = sensor
    i = 0
    y_coords = [y]

    # if the sensor will not affect the y coordinate thats being checked in part 1 - skip
    if p1 and bound not in range(y-distance, y+distance+1):
        return Y_indices

    # if the sensor will not affect the y coordinates that are being checked in part 2 - skip
    if not p1 and (y-distance <= 0) and (y+distance+1 >= bound):
        return Y_indices

    for i in range(distance):
        start, end = x-distance+i, x+distance-i
        for cy in y_coords:
            # Only updates the y coordinate being checked in part 1
            if p1 and cy == bound:
                Y_indices[bound].append((start, end))
            elif not p1:
                # Clamps the start and end values to between 0 and 4,000,000 if out of range
                if start < 0:
                    start = 0
                elif end > bound:
                    end = bound

                # Updates the interval dictionary if the y coordinate is within the range
                if 0 <= cy <= bound:
                    Y_indices[cy].append((start, end))

        # Updates the y coordinate after each loop
        if len(y_coords) == 1:
            y_coords = [y+1, y-1]
        else:
            y_coords = [y_coords[0]+1, y_coords[1]-1]

    return Y_indices


def is_overlaping(a, b):
    "Determines if two ordered intervals are overlapping or adjacent."
    # Overlapping
    if b[0] >= a[0] and b[0] <= a[1]:
        return True
    # Adjacent
    elif a[1]+1 == b[0]:
        return True
    else:
        return False


def merge_intervals(intervals):
    """Takes in the intervals and merges them if they are overlapping or adjacent."""
    # Sorts the intervals by the start x coordinate
    intervals = [[x, y] for x, y in intervals]
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        # Merge intervals if they are overlapping or adjacent
        pop_element = merged.pop()
        if is_overlaping(pop_element, intervals[i]):
            new_element = pop_element[0], max(pop_element[1], intervals[i][1])
            merged.append(new_element)
        else:
            merged.append(pop_element)
            merged.append(intervals[i])
    return merged


def part_one(input, p1_y):
    """Returns the number of impossible position when y=p1_y."""
    Y_indices = {p1_y: list()}
    for sensor, distance in input.items():
        Y_indices = clear_area(sensor, distance, Y_indices, p1_y)
    intervals = merge_intervals(Y_indices[p1_y])
    return sum(x2-x1 for x1, x2 in intervals)


def part_two(input, max_xy):
    """Returns the tuning frequency of the distress beacon by finding its location"""
    Y_indices = {y: [] for y in range(max_xy+1)}
    for sensor, distance in input.items():
        Y_indices = clear_area(sensor, distance, Y_indices, max_xy, p1=False)

    # Merges the intervals for each y coordinate, stops if it finds the one with a gap
    for k, v in Y_indices.items():
        Y_indices[k] = merge_intervals(v)
        if len(Y_indices[k]) > 1:
            bx = Y_indices[k][0][1]+1
            by = k
            break

    # Returns the tuning frequency
    return bx * 4_000_000 + by

if __name__ == "__main__":
    input = input_data("python/year_2022/day_15_beacon_exclusion_zone/input.txt")

    print("--------------------------------------")
    print("Day 15: Beacon Exclusion Zone")
    print("Part One Answer: " + str(part_one(input, p1_y=2_000_000)))
    print("Part Two Answer: " + str(part_two(input, max_xy=4_000_000)))
    print("--------------------------------------")
