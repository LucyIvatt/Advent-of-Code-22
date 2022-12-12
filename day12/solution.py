from dijkstar import Graph, find_path


def input_data(filename):
    """Returns the data imported from file -
    """
    with open(filename) as f:
        input = f.read().splitlines()

    s_loc, e_loc = None, None
    grid = []
    for i in range(len(input)):
        grid_line = []
        for j in range(len(input[i])):
            if input[i][j] == "S":
                grid_line.append(ord("a"))
                s_loc = (i, j)
            elif input[i][j] == "E":
                grid_line.append(ord("z"))
                e_loc = (i, j)
            else:
                grid_line.append(ord(input[i][j]))
        grid.append(grid_line)
    return grid, e_loc, s_loc


def get_neighbours(i, j, grid):
    """Returns the neighbours of a given cell in a grid
    """
    neighbours = []
    if i > 0:
        neighbours.append((i - 1, j))
    if i < len(grid) - 1:
        neighbours.append((i + 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if j < len(grid[0]) - 1:
        neighbours.append((i, j + 1))
    return neighbours


def part_one(grid, s_loc, e_loc):
    graph = Graph()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for nb in get_neighbours(i, j, grid):
                cur, new = grid[i][j], grid[nb[0]][nb[1]]
                if new - cur <= 1:
                    graph.add_edge((i, j), nb, 1)
    return find_path(graph, s_loc, e_loc).total_cost


grid, e_loc, s_loc = input_data("day12/input.txt")

print("--------------------------------------")
print("Day 12: Hill Climbing Algorithm")
print("Part One Answer: " + str(part_one(grid, s_loc, e_loc)))
print("Part Two Answer: ")
print("--------------------------------------")
