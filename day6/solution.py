def input_data(filename):
    """Returns the data imported from file - datastream buffer string
    """
    file = open(filename, "r")
    input = file.readline().strip()
    file.close()
    return input


def solution(input, marker_length):
    """Returns index of final character in the first detected marker.
    (A marker is a substring of only unique characters)"""
    for i in range(len(input)-marker_length):
        chars = input[i:i+marker_length]
        if len(chars) == len(set(chars)):
            return i+marker_length


input = input_data("day6/input.txt")

print("--------------------------------------")
print("Day 6: Tuning Trouble")
print("Part One Answer: " + str(solution(input, 4)))
print("Part Two Answer: " + str(solution(input, 14)))
print("--------------------------------------")
