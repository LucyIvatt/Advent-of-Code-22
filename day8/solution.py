import numpy as np
import operator


def input_data(filename):
    """Returns the data imported from file -
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [[int(num) for num in line.strip()] for line in input]
    return input


def part_one(input):
    # Adds the trees on the edge of the forest
    num_visible = len(input)*2 + (len(input[0])-2)*2

    # For each tree that is not on the edge of the problem
    for i in range(1, len(input)-1):
        for j in range(1, len(input[0])-1):
            if check_directions(input, i, j):
                num_visible += 1

    return num_visible


def part_two(input):
    scores = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            scores.append(check_directions(input, i, j, scenic_score=True))
    return max(scores)


def check_directions(input, i, j, scenic_score=False):
    tree_visible = False
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    viewing_distances = list()

    #3, 2
    # For each direction - up down left right
    for dir in directions:
        di, dj = map(operator.add, (i, j), dir)
        dir_visible, view_dist = False, 0

        if not (0 <= di < len(input)) or not (0 <= dj < len(input[1])):
            dir_visible = True

        # Ensures the new indexes are in range of the forest
        while 0 <= di < len(input) and 0 <= dj < len(input[1]):
            view_dist += 1

            if input[di][dj] >= input[i][j]:
                viewing_distances.append(view_dist)
                dir_visible = False
                break

            else:
                dir_visible = True
                di, dj = map(operator.add, (di, dj), dir)

        if dir_visible:
            viewing_distances.append(view_dist)
            tree_visible = True

    if scenic_score:
        return np.prod(viewing_distances)
    else:
        return tree_visible


input = input_data("day8/input.txt")

print("--------------------------------------")
print("Day 8: Treetop Tree House")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: " + str(part_two(input)))
print("--------------------------------------")
