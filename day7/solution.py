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


def solution(input):
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

    dir_sizes = dict()
    for dir in directories:
        dir_sum = 0
        for file in findall(dir, filter_=lambda node: node.n_type == Type.File):
            dir_sum += file.size
        dir_sizes[dir] = dir_sum

    p1_ans = sum((x for x in dir_sizes.values() if x <= 100_000))

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
