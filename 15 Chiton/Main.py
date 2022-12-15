from collections import defaultdict
from sys import maxsize
from queue import PriorityQueue
import time


class Weighted_Graph():
    def __init__(self, risk_map):
        self.graph = defaultdict(set)
        self.risk_map = risk_map
        self.add_all_connections()
        self.length = len(self.risk_map)

    def add_neighbors(self, x, y):
        neighbor_coords = get_neighbors(self.risk_map, x, y)
        for x2, y2 in neighbor_coords:
            self.graph[(x, y)].add(((x2, y2), self.risk_map[y2][x2]))

    def add_all_connections(self):
        for y in range(len(self.risk_map)):
            for x in range(len(self.risk_map[y])):
                self.add_neighbors(x, y)

    def get_nodes(self):
        return self.graph.keys()

    def find_shortest_paths(self, start_node, end_node):
        visited_nodes = defaultdict(lambda: False)
        shortest_paths = {node: maxsize for node in self.get_nodes()}
        shortest_paths[start_node] = 0

        pq = PriorityQueue()
        pq.put((0, start_node))

        while not pq.empty():
            item = pq.get()
            current_node = item[1]
            visited_nodes[current_node] = True
            if current_node == end_node:
                return shortest_paths

            for neighbor in self.graph[current_node]:
                coord = neighbor[0]
                weight = neighbor[1]
                if visited_nodes[coord] == False:
                    old_cost = shortest_paths[coord]
                    new_cost = shortest_paths[current_node] + weight
                    if new_cost < old_cost:
                        pq.put((new_cost, coord))
                        shortest_paths[coord] = new_cost
        return shortest_paths


def get_neighbors(array, x, y):
    neighbors_coords = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if new_x >= 0 and new_x < len(array):
            if new_y >= 0 and new_y < len(array[new_x]):
                neighbors_coords.append((new_x, new_y))
    return neighbors_coords


def generate_new_map(risk_map):
    extended_map = []

    # Extends in x direction
    for row in risk_map:
        extended_row = row
        for i in range(4):
            extended_row.extend(
                [x + 1 if x < 9 else 1 for x in extended_row[-len(risk_map):]])
        extended_map.append(row)

    # Extends in y direction
    for i in range(4):
        for row in extended_map[-len(risk_map):]:
            extended_map.append([x + 1 if x < 9 else 1 for x in row])

    return extended_map


def importList(filename):
    with open(filename, "r") as file:
        risk_map = [[int(x) for x in line.strip()]
                    for line in file.readlines()]
    return risk_map


def part_one(risk_map):
    start_time = time.time()
    graph = Weighted_Graph(risk_map)
    start_node, end_node = (0, 0), (graph.length - 1, graph.length - 1)
    shortest_risk_totals = graph.find_shortest_paths(start_node, end_node)
    end_time = time.time()
    return str(shortest_risk_totals[end_node]) + ", time taken: " + "{:.4f}".format(end_time - start_time) + "s"


def part_two(risk_map):
    start_time = time.time()
    new_map = generate_new_map(risk_map)
    graph = Weighted_Graph(new_map)
    start_node, end_node = (0, 0), (graph.length - 1, graph.length - 1)
    shortest_risk_totals = graph.find_shortest_paths(start_node, end_node)
    end_time = time.time()
    return str(shortest_risk_totals[end_node]) + ", time taken: " + "{:.4f}".format(end_time - start_time) + "s"


risk_map = importList("Day 15 Chiton\input.txt")

print("--------------------------------------")
print("DAY 15: CHITON")
print("Part One Answer: ", part_one(risk_map))
print("Part Two Answer: ", part_two(risk_map))
print("--------------------------------------")
