import numpy as np


class Pair:
    def __init__(self, p1, p2):
        pass

    def build_tree(self, pi):
        pass


def compare(x, y):
    """1 if x < y (Correct order), 0 if x == y, -1 if x > y (incorrect order)"""
    # When both values are integers
    if type(x) == int and type(y) == int:
        if x < y:
            return 1
        elif x == y:
            return 0
        else:
            return -1

    # When one value is a list and the other is an integer - convert integer to list
    if type(x) == list and type(y) == int:
        y = [y]
    elif type(x) == int and type(y) == list:
        x = [x]

    # When both values are lists
    if type(x) == list and type(y) == list:
        if len(y) < len(x):
            return -1
        elif len(y) > len(x):
            if np.all(np.asarray(y[:len(x)]) >= np.asarray(x)):
                return 1
            else:
                return -1
        else:
            if np.all(np.asarray(y) >= np.asarray(x)):
                if np.any(np.asarray(y) > np.asarray(x)):
                    return 1
                else:
                    return 0
            else:
                return -1


def input_data(filename):
    """Returns the data imported from file -
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()

    # split input on blank lines and remove \n characters
    input = [x.strip() for x in input if x.strip() != ""]
    input = [(input[i], input[i+1]) for i in range(0, len(input), 2)]
    return input
# TODO: Enter solutions


def part_one(input):
    """Returns the solution to part one - sum of indicies 
    of pairs in correct order"""
    for pair in input:
        print(pair)


input = input_data("day13/example.txt")
part_one(input)

print("--------------------------------------")
print("Day 13: Distress Signal")
print("Part One Answer: ")
print("Part Two Answer: ")
print("--------------------------------------")
