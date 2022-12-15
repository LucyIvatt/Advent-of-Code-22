class Paper():

    def __init__(self, dots, width, height):
        self.dots = set(dots)
        self.width = width
        self.height = height
        self.dot_count = len(self.dots)

    def __str__(self):
        paper_view = [["." for x in range(self.width)]
                      for y in range(self.height)]
        for x, y in self.dots:
            paper_view[y][x] = "#"

        string = ""
        for line in paper_view:
            line_string = ""
            for char in line:
                line_string += char
            string += line_string + "\n"
        return string

    def fold(self, direction, index):
        new_dots = set()
        if direction.lower() == "y":
            for x, y in self.dots:
                if y > index:
                    new_dots.add((x, index-(y-index)))
                else:
                    new_dots.add((x, y))
            self.height = index

        elif direction.lower() == "x":
            for x, y in self.dots:
                if x > index:
                    new_dots.add((index-(x-index), y))
                else:
                    new_dots.add((x, y))
            self.width = index
        self.dots = new_dots
        self.dot_count = self.visible_dot_count()

    def visible_dot_count(self):
        return len(self.dots)


def importList(filename):
    with open(filename, "r") as file:
        input = file.read().split("\n\n")

    dot_x_coords = []
    dot_y_coords = []

    for coord in input[0].split("\n"):
        split_coord = coord.split(",")
        dot_x_coords.append(int(split_coord[0]))
        dot_y_coords.append(int(split_coord[1]))

    instructions = [ins.replace("fold along ", "").split("=")
                    for ins in input[1].split("\n")]
    instructions = [(x, int(y)) for x, y in instructions]

    return zip(dot_x_coords, dot_y_coords), instructions, max(dot_x_coords) + 1, max(dot_y_coords) + 1


def part_one(page, instructions):
    page.fold(instructions[0][0], instructions[0][1])
    return page.dot_count


def part_two(page, instructions):
    for instruction in instructions:
        page.fold(instruction[0], instruction[1])
    return(str(page))


dots, instructions, width, height = importList(
    "Day 13 Transparent Origami\input.txt")
page = Paper(dots, width, height)

print("--------------------------------------")
print("DAY 13: TRANSPARENT ORIGAMI")
print("Part One Answer: " + str(part_one(page, instructions)))
print("Part Two Answer: ZUJUAFHP")
print(part_two(page, instructions))
print("--------------------------------------")
