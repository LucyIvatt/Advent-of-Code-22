import time


def importList(filename):
    height_map = []
    with open(filename, "r") as file:
        for line in file:
            line_heights = []
            for char in line.strip():
                line_heights.append(int(char))
            height_map.append(line_heights)
    return height_map


def find_low_points(heatmap):
    low_points = []
    for i in range(len(heatmap)):
        for j in range(len(heatmap[i])):
            low_point = True
            for value in get_neighbors(heatmap, i, j):
                if heatmap[i][j] >= value:
                    low_point = False
                    break
            if low_point:
                low_points.append((i, j))
    return low_points


def sum_risk_levels(heatmap, low_points):
    risk_sums = 0
    for point in low_points:
        risk_sums += 1 + heatmap[point[0]][point[1]]
    return risk_sums


def find_lower_coords(heatmap, coords, found_coords):
    if len(coords) == 0:
        return set(found_coords)
    else:
        new_coords = []
        for x, y in coords:
            found_coords.append((x, y))
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                next_x, next_y = x + dx, y + dy
                # if the coordinate is in the valid range
                if next_x >= 0 and next_x < len(heatmap):
                    if next_y >= 0 and next_y < len(heatmap[next_x]):
                        if heatmap[next_x][next_y] > heatmap[x][y] and heatmap[next_x][next_y] != 9:
                            new_coords.append((next_x, next_y))
        return find_lower_coords(heatmap, new_coords, found_coords)


def get_neighbors(heatmap, x, y):
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if new_x >= 0 and new_x < len(heatmap):
            if new_y >= 0 and new_y < len(heatmap[new_x]):
                neighbors.append(heatmap[new_x][new_y])
    return neighbors


def part_one():
    input = importList("Day 9 Smoke Basin\input.txt")
    low_points = find_low_points(input)
    return sum_risk_levels(input, low_points)


def part_two():
    input = importList("Day 9 Smoke Basin\input.txt")
    low_points = find_low_points(input)
    basin_sizes = []

    for coord in low_points:
        basin_coords = find_lower_coords(input, [coord], [])
        basin_sizes.append(len(basin_coords))
    basin_sizes = sorted(basin_sizes, reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


print("--------------------------------------")
print("DAY NINE: SMOKE BASIN")
print("Part One Answer: " + str(part_one()))
print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")
