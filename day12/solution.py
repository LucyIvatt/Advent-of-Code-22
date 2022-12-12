from dijkstar import Graph, find_path, NoPathError
from numpy import inf


def input_data(filename):
    """Returns the data imported from file - grid of ascii values representing heights
    """
    with open(filename) as f:
        input = f.read().splitlines()

    s, e = None, None
    grid = []
    for i in range(len(input)):
        grid_line = []
        for j in range(len(input[i])):
            if input[i][j] == "S":
                grid_line.append(ord("a"))
                s = (i, j)
            elif input[i][j] == "E":
                grid_line.append(ord("z"))
                e = (i, j)
            else:
                grid_line.append(ord(input[i][j]))
        grid.append(grid_line)
    graph = gen_graph(grid)
    return grid, graph, s, e


def gen_graph(grid):
    """Creates graph from ascii values in grid
    """
    graph = Graph()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for nb in get_neighbours(i, j, grid):
                cur, new = grid[i][j], grid[nb[0]][nb[1]]
                if new - cur <= 1:
                    graph.add_edge((i, j), nb, 1)
    return graph


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


def part_one(graph, s, e):
    """Returns the shortest path between S and E"""
    return find_path(graph, s, e).total_cost


def part_two(grid, graph, e):
    a_nodes = [(i, j) for i in range(len(grid))
               for j in range(len(grid[i])) if grid[i][j] == ord("a")]
    min_dist = inf
    for node in a_nodes:
        try:
            dist = find_path(graph, node, e).total_cost
            if dist < min_dist:
                min_dist = dist
        except NoPathError:
            continue
    return min_dist


grid, graph, s, e = input_data("day12/input.txt")

print("--------------------------------------")
print("Day 12: Hill Climbing Algorithm")
print("Part One Answer: " + str(part_one(graph, s, e)))
print("Part Two Answer: " + str(part_two(grid, graph, e)))
print("--------------------------------------")
