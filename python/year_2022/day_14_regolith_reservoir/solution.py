import copy

DIR = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0),
       "up-left": (-1, -1), "up-right": (1, -1), "down-left": (-1, 1), "down-right": (1, 1)}


class VoidError(Exception):
    pass


def input_data(filename):
    """Returns the data imported from file - strings of pairs (separated by newline)
    """
    with open(filename, 'r') as file:
        input = file.read().strip().split("\n")
    return [[corner.split(",") for corner in line.split(" -> ")] for line in input]


def simulate_sand(scan, sand, p2=False):
    """Simulates the sand falling down the scan. Returns a boolean if the sand is falling into the void.
    """
    sx, sy = sand
    if not p2:
        conditional = 0 <= sx < len(scan[0]) and 0 <= sy < len(scan)
    else:
        conditional = scan[sand[0], sand[1]] == "+"
    while conditional:
        try:
            if check_dir(scan, sx, sy, "down", p2):
                dx, dy = DIR["down"]
                sx, sy = sx+dx, sy+dy
            elif check_dir(scan, sx, sy, "down-left", p2):
                dx, dy = DIR["down-left"]
                sx, sy = sx+dx, sy+dy
            elif check_dir(scan, sx, sy, "down-right", p2):
                dx, dy = DIR["down-right"]
                sx, sy = sx+dx, sy+dy
            else:
                if 0 <= sx < len(scan[0]) and 0 <= sy < len(scan):
                    scan[sy][sx] = "o"
                    if (sx, sy) == sand:
                        return scan, True
                    return scan, False
                else:
                    return scan, True
        except VoidError:
            return scan, True
    return scan, True


def check_dir(scan, sx, sy, dir, p2=False):
    """Checks if the sand can move in a given direction. Returns a boolean if the sand can move in the given direction.
    """
    dx, dy = DIR[dir]

    if sy+dy >= len(scan) or sy+dy < 0 or sx+dx >= len(scan[0]) or sx+dx < 0:
        raise VoidError("The sand has fallen into the void.")

    if scan[sy+dy][sx+dx] == ".":
        return True
    else:
        return False


def draw_scan(input, p2=False):
    """Builds a grid of the scan from the input data. Returns the grid.
    """
    # Calculates the bounds of the grid
    y_coords = [int(corner[1]) for line in input for corner in line] + [0]

    if p2:
        y_bounds = (min(y_coords), max(y_coords)+2)
        y_height = y_bounds[1] - y_bounds[0] + 1
        x_bounds = (500 - y_height, 500 + y_height)
    else:
        x_coords = [int(corner[0])
                    for line in input for corner in line] + [500]
        x_bounds = (min(x_coords), max(x_coords))
        y_bounds = (min(y_coords), max(y_coords)+2)

    # Builds the grid
    scan = [["." for _ in range(x_bounds[0], x_bounds[1]+1)]
            for _ in range(y_bounds[0], y_bounds[1]+1)]

    for line in input:
        # Iterates through the corners of the line in pairs

        for c in range(len(line)-1):
            c1_x = int(line[c][0]) - x_bounds[0]
            c1_y = int(line[c][1]) - y_bounds[0]
            c2_x = int(line[c+1][0]) - x_bounds[0]
            c2_y = int(line[c+1][1]) - y_bounds[0]

            if c1_x == c2_x:
                # swaps the y coordinates if c1_y > c2_y
                if c1_y > c2_y:
                    c1_y, c2_y = c2_y, c1_y
                # Adds the rocks to the grid
                for y in range(c1_y, c2_y+1):
                    scan[y][c1_x] = "#"

            elif c1_y == c2_y:
                # swaps the x coordinates if c1_x > c2_x
                if c1_x > c2_x:
                    c1_x, c2_x = c2_x, c1_x
                # Adds the rocks to the grid
                for x in range(c1_x, c2_x+1):
                    scan[c1_y][x] = "#"
    if p2:
        for x in range(len(scan[-1])):
            scan[-1][x] = "#"

    # Adds the sand entrance
    scan[0][500-x_bounds[0]] = "+"
    return scan, x_bounds


def part_one(input):
    grid, x_bounds = draw_scan(input)
    resting_sand = 0
    while True:
        grid, end = simulate_sand(grid, (500-x_bounds[0], 0))
        if end:
            break
        else:
            resting_sand += 1
    return resting_sand


def part_two(input):
    grid, x_bounds = draw_scan(input, p2=True)
    resting_sand = 0
    while True:
        grid, end = simulate_sand(grid, (500-x_bounds[0], 0))
        resting_sand += 1
        if end:
            break

    return resting_sand

if __name__ == "__main__":
    input = input_data("python/year_2022/day_14_regolith_reservoir/input.txt")

    print("--------------------------------------")
    print("Day 14: Regolith Reservoir")
    print("Part One Answer: " + str(part_one(input)))
    print("Part Two Answer: " + str(part_two(input)))
    print("--------------------------------------")
