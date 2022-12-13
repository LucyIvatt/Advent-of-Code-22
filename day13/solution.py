from functools import total_ordering
from numpy import prod


@total_ordering
class Packet():
    def __init__(self, string, divider=False):
        self.packet = eval(string)
        self.divider = divider

    def __str__(self):
        return str(self.packet)

    def __eq__(self, other):
        return self.compare(self.packet, other.packet) == 0

    def __lt__(self, other):
        return self.compare(self.packet, other.packet) == 1

    @staticmethod
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

        # When both values are lists - need to recursively compare each element
        if type(x) == list and type(y) == list:
            i = 0
            while i < len(x) and i < len(y):
                # If there are still comparable elements, recursively compare them
                result = Packet.compare(x[i], y[i])

                if result == 1:
                    return 1
                if result == -1:
                    return -1
                i += 1

            if i == len(x) and i < len(y):
                return 1
            elif i == len(x) and i == len(y):
                return 0
            elif i < len(x) and i == len(y):
                return -1


def input_data(filename):
    """Returns the data imported from file - strings of pairs (separated by newline)
    """
    with open(filename, 'r') as file:
        return file.read().strip().split("\n\n")


def part_one(input):
    """Returns the solution to part one - sum of indicies
    of pairs in correct order"""
    sum = 0
    for i, block in enumerate(input):
        p1, p2 = [Packet(x) for x in block.split("\n")]
        if p1 < p2:
            sum += i + 1
    return sum


def part_two(input):
    packets = [Packet(x, divider=True) for x in ["[[2]]", "[[6]]"]]
    for block in input:
        packets.extend([Packet(x) for x in block.split("\n")])
    packets = sorted(packets)
    return prod([packets.index(packet)+1 for packet in packets if packet.divider == True])


input = input_data("day13/input.txt")


print("--------------------------------------")
print("Day 13: Distress Signal")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: " + str(part_two(input)))
print("--------------------------------------")
