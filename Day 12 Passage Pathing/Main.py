from collections import defaultdict


class CaveStructure():

    def __init__(self, connections):
        self.graph = defaultdict(set)
        self.add_connections(connections)
        self.paths_p1 = []
        self.paths_p2 = []
        self.find_all_paths(True)
        self.find_all_paths(False)
        self.path_count_p1 = len(self.paths_p1)
        self.path_count_p2 = len(self.paths_p2)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.graph[node1].add(node2)
            self.graph[node2].add(node1)

    def find_all_paths(self, part_one):
        for node in self.graph["start"]:
            self.find_paths(node, ["start"], part_one)

    def find_paths(self, current_node, current_path, part_one=True, duplicated_yet=False):
        # Base case
        if (current_node == "end"):
            current_path.append("end")
            if(part_one and current_path not in self.paths_p1):
                self.paths_p1.append(current_path)
            elif(not part_one and current_path not in self.paths_p2):
                self.paths_p2.append(current_path)

        # Recursive Case
        elif (current_node.islower() and current_node not in current_path) or (current_node.isupper()):
            # If non-visited small cave, or large cave, add node to path.
            current_path.append(current_node)

            # Does same for all neighbors
            for next_node in self.graph[current_node]:
                if(next_node != "start"):
                    self.find_paths(next_node, current_path.copy(),
                                    part_one, duplicated_yet)

        elif not part_one and current_node.islower() and not duplicated_yet:
            current_path.append(current_node)

            # Does same for all neighbors
            for next_node in self.graph[current_node]:
                if next_node != "start":
                    self.find_paths(
                        next_node, current_path.copy(), part_one, True)

        # Else: dead end has been found


def importList(filename):
    with open(filename, "r") as file:
        connections = [line.strip().split("-") for line in file]
    return connections


connections = importList("Day 12 Passage Pathing\input.txt")
cave_structure = CaveStructure(connections)

print("--------------------------------------")
print("DAY 12: PASSAGE PATHING")
print("Part One Answer: " + str(cave_structure.path_count_p1))
print("Part Two Answer: " + str(cave_structure.path_count_p2))
print("--------------------------------------")
