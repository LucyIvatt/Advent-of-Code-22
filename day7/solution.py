from anytree import Node, RenderTree, Resolver
from anytree.search import findall
from enum import Enum


class Type(Enum):
    File = 0
    Directory = 1


def input_data(filename):
    """Returns the data imported from file -
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [line.strip().replace("/", "root") for line in input]

    # Converts input into a list of cd commands and lists of files/dirs representing the output of $ lst commands
    input_new = []
    i = 0
    while i < len(input):
        if "cd" in input[i]:
            input_new.append(input[i].replace("$ ", ""))
            i += 1
        elif "ls" in input[i]:
            j = 1
            while i+j < len(input) and "$" not in input[i+j]:
                input_new.append(input[i+j])
                j += 1
            i += j
    return input_new[1:]


def solution(input):
    # Creates tree representing the directory
    current_directory = ""
    root = Node("root", n_type=Type.Directory)
    r = Resolver('name')

    for line in input:
        x, y = line.split()
        if x == "cd":
            # Keeps track of current directory so the parent for each node is known
            current_directory += y + "/"
        elif x == "dir":
            # Adds type to the node to show it is a directory
            Node(y, parent=r.get(root, current_directory), n_type=Type.Directory)
        else:
            # Adds type and size to node to show it is a file
            Node(y, parent=r.get(root, current_directory),
                 n_type=Type.File, size=int(x))

    # Finds all directory nodes on the tree
    directories = findall(
        root, filter_=lambda node: node.n_type == Type.Directory)

    # Calculates the sizes of each directory
    dir_sizes = dict()
    for dir in directories:
        dir_sum = 0
        for file in findall(dir, filter_=lambda node: node.n_type == Type.File):
            dir_sum += file.size
        dir_sizes[dir] = dir_sum

    # Returns the sum of all directories smaller than 100_000
    p1_ans = sum((x for x in dir_sizes.values() if x <= 100_000))

    # Returns the size of the smallest directory that can be removed to install the update
    space_required = 30_000_000 - (70_000_000 - max(dir_sizes.values()))
    p2_ans = min((x for x in dir_sizes.values() if x >= space_required))

    return p1_ans, p2_ans


input = input_data("day7/input.txt")
p1_ans, p2_ans = solution(input)


print("--------------------------------------")
print("Day 7: No Space Left On Device")
print("Part One Answer: " + str(p1_ans))
print("Part Two Answer: " + str(p2_ans))
print("--------------------------------------")
