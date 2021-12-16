from collections import defaultdict


class CaveStructure():

    def __init__(self, connections):
        self.graph = defaultdict(set)
        self.add_connections(connections)
        self.valid_paths = []
        self.find_all_valid_paths()

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.graph[node1].add(node2)
            self.graph[node2].add(node1)

    def find_all_valid_paths(self):
        for node in self.graph["start"]:
            self.find_valid_paths(node, ["start"])

    def find_valid_paths(self, current_node, current_path):
        # Base case
        if (current_node == "end"):
            current_path.append("end")
            self.valid_paths.append(current_path)

        # Recursive Case
        elif (current_node.islower() and current_node not in current_path) or (current_node.isupper()):
            # If non-visited small cave, or large cave, add node to path.
            current_path.append(current_node)

            # Does same for all neighbors
            for next_node in self.graph[current_node]:
                self.find_valid_paths(next_node, current_path.copy())

        # Else: dead end has been found


def importList(filename):
    connections = []
    with open(filename, "r") as file:
        connections = [line.strip().split("-") for line in file]
    return connections


def part_one():
    connections = importList("Day 12 Passage Pathing\input.txt")
    cave_structure = CaveStructure(connections)
    paths = cave_structure.valid_paths
    return (len(paths))


print("--------------------------------------")
print("DAY 12: PASSAGE PATHIN")
print("Part One Answer: " + str(part_one()))
# print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")
