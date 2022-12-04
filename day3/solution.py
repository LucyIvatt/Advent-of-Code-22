import string

ITEMS = string.ascii_lowercase + string.ascii_uppercase
PRIORITIES = {ITEMS[i-1]: i for i in range(1, len(ITEMS)+1)}


def input_data(filename):
    """Returns the data imported from file - list of backpack strings
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [line.strip() for line in input]
    return input


def part_one(input):
    # splits backpack into 2 equal size sections
    def mid(line): return len(line) // 2
    input = [(line[:mid(line)], line[mid(line):]) for line in input]

    # uses set intersection to find common element
    sum_priorities = 0
    for sec_1, sec_2 in input:
        item = set(sec_1) & set(sec_2)
        sum_priorities += PRIORITIES[str(item.pop())]
    return sum_priorities


def part_two(input):
    sum_priorities = 0
    # Iterates through backpack in groups of 3
    for i in range(0, len(input), 3):
        # Computes itersection of 3 backpacks to find common badge
        badge = set(input[i]) & set(input[i+1]) & set(input[i+2])
        sum_priorities += PRIORITIES[str(badge.pop())]
    return sum_priorities


input = input_data("day3/input.txt")

print("--------------------------------------")
print("Day 3: Rucksack")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: " + str(part_two(input)))
print("--------------------------------------")
