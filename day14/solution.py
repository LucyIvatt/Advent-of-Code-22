DIR = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0),
       "up-left": (-1, -1), "up-right": (1, -1), "down-left": (-1, 1), "down-right": (1, 1)}


def input_data(filename):
    """Returns the data imported from file - strings of pairs (separated by newline)
    """
    with open(filename, 'r') as file:
        return file.read().strip().split("\n")


def simulate_sand(scan, sand, x_bounds, y_bounds):
    """Simulates the sand falling down the scan. Returns a boolean if the sand is falling into the void.
    """
    sx, sy = sand
    while x_bounds[0] < sand[0] < x_bounds[1] and y_bounds[0] < sand[1] < y_bounds[1]:
        if check_dir(scan, sand, DIR["down"]) == ".":
            dx, dy = DIR["down"]
            sx, sy = sx+dx, sy+dy
        elif check_dir(scan, sand, DIR["down-left"]) == ".":
            dx, dy = DIR["down-left"]
            sx, sy = sx+dx, sy+dy
        elif check_dir(scan, sand, DIR["down-right"]) == ".":
            dx, dy = DIR["down-right"]
            sx, sy = sx+dx, sy+dy
        else:
            scan[sx][sy] = "o"
            return scan, False
    return scan, True


def check_dir(scan, sand, dir):
    """Checks if the sand can move in a given direction. Returns a boolean if the sand can move in the given direction.
    """
    sx, sy = sand
    dx, dy = DIRS[dir]
    if scan[sx+dx][sy+dy] == ".":
        return True
    else:
        return False


def build_grid(input):
    """Builds a grid of the scan from the input data. Returns the grid.
    """
    # TODO: build grid from input data
    grid = []
    for line in input:
        pass

    return grid


input = input_data("day14/example.txt")
print(input)

print("--------------------------------------")
print("Day 14: Regolith Reservoir")
print("Part One Answer: ")
print("Part Two Answer: ")
print("--------------------------------------")
