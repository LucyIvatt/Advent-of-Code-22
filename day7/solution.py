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

    condensed_input = []
    i = 0
    while i < len(input):
        if "cd" in input[i]:
            condensed_input.append(input[i].replace("$ ", ""))
            i += 1
        elif "ls" in input[i]:
            j = 1
            while i+j < len(input) and "$" not in input[i+j]:
                condensed_input.append(input[i+j])
                j += 1
            i += j
    return condensed_input[1:]


def part_one(input):
    current_directory = ""
    root = Node("root", n_type=Type.Directory)
    r = Resolver('name')

    for line in input:
        x, y = line.split()
        if x == "cd":
            current_directory += y + "/"
        elif x == "dir":
            Node(y, parent=r.get(root, current_directory), n_type=Type.Directory)
        else:
            Node(y, parent=r.get(root, current_directory),
                 n_type=Type.File, size=int(x))

    directories = findall(
        root, filter_=lambda node: node.n_type == Type.Directory)

    overall_sum = 0
    for dir in directories:
        dir_sum = 0
        for file in findall(dir, filter_=lambda node: node.n_type == Type.File):
            dir_sum += file.size
        if dir_sum <= 100_000:
            overall_sum += dir_sum

    return overall_sum


input = input_data("day7/input.txt")


print("--------------------------------------")
print("Day 7: No Space Left On Device")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: ")
print("--------------------------------------")
