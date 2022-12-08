import numpy as np
import operator


def input_data(filename):
    """Returns the data imported from file - 2D array of int tree heights
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [[int(num) for num in line.strip()] for line in input]
    return input


def solution(input):
    """Iterates through all trees in the forest and calculates their scenic score and 
    if they are visible or not. Returns the number of visible trees (p1) and highest scenic 
    score."""
    visible_trees, max_scenic_score = 0, 0

    for i in range(len(input)):
        for j in range(len(input[0])):
            visible, scenic_score = check_directions(input, i, j)
            if visible:
                visible_trees += 1
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return visible_trees, max_scenic_score


def check_directions(input, i, j):
    """For a given tree, checks all 4 directions and calculates the view distance.
    Returns if a tree is visible in any of the directions and returns its scenic score (product of
    view distances in the 4 directions).
    """
    tree_visible = False
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    viewing_distances = list()

    # For each direction - up down left right
    for dir in directions:
        di, dj = map(operator.add, (i, j), dir)
        dir_visible, view_dist = False, 0

        # if tree is on the edge of the forest it is visible by default
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

    return tree_visible, np.prod(viewing_distances)


input = input_data("day8/example.txt")
p1, p2 = solution(input)

print("--------------------------------------")
print("Day 8: Treetop Tree House")
print("Part One Answer: " + str(p1))
print("Part Two Answer: " + str(p2))
print("--------------------------------------")
