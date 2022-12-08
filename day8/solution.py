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


def check_directions(input, i, j) -> bool:
    ni, nj = i, j
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for dir in directions:
        visible = False
        ni += dir[0]
        nj += dir[1]
        while 0 <= ni < len(input) and 0 <= nj < len(input[1]):
            if input[ni][nj] >= input[i][j]:
                visible = False
                ni, nj = i, j
                break
            else:
                visible = True
                ni += dir[0]
                nj += dir[1]
        if visible:
            return True
    return False


input = input_data("day8/input.txt")

print("--------------------------------------")
print("Day 8: Treetop Tree House")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: ")
print("--------------------------------------")
