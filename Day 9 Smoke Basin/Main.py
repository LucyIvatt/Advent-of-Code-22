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
    risk_level_sum = 0

    for i in range(len(heatmap)):
        for j in range(len(heatmap[i])):
            low_point = True
            for value in get_neighbors(heatmap, i, j):
                if heatmap[i][j] >= value:
                    low_point = False
                    break
            if low_point:
                risk_level_sum += 1 + heatmap[i][j]
                low_points.append(heatmap[i][j])
    return [low_points, risk_level_sum]


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
    return low_points[1]


print("--------------------------------------")
print("DAY NINE: SMOKE BASIN")
print("Part One Answer: " + str(part_one()))
# print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")
