from collections import Counter


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def __str__(self):
        return "Coordinate One: " + str(self.x1) + "," + str(self.y1) + "\n" + \
            "Coordinate Two: " + str(self.x2) + "," + str(self.y2)

    def calculate_included_coords(self):
        included_coords = []
        if self.x1 == self.x2:
            for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                included_coords.append((self.x1, y))
        elif self.y1 == self.y2:
            for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                included_coords.append((x, self.y1))
        return included_coords


def importList(filename):
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [line.strip().split(" -> ") for line in input]
    lines = []
    for pair in input:
        coordinate_one = pair[0].split(",")
        coordinate_two = pair[1].split(",")
        lines.append(
            Line(coordinate_one[0], coordinate_one[1],
                 coordinate_two[0], coordinate_two[1]))
    return lines


def generate_all_coordinates(lines):
    all_coordinates = []
    for line in lines:
        all_coordinates.extend(line.calculate_included_coords())
    return all_coordinates


def calculate_overlap(all_coordinates):
    overlap_count = 0
    count = Counter(all_coordinates)
    for value in count.values():
        if value > 1:
            overlap_count += 1
    return overlap_count


def part_one():
    input = importList("Day 5 Hydrothermal Venture\input.txt")
    all_coords = generate_all_coordinates(input)
    return calculate_overlap(all_coords)


print("--------------------------------------")
print("DAY FIVE: HYDROTHERMAL VENTURE")
print("Part One Answer: " + str(part_one()))
print("Part Two Answer: " + str())
print("--------------------------------------")
