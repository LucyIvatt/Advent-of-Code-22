def input_data(filename):
    """Returns the data imported from file - list of elves calories, None 
    is used as a separator between elves.
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [int(line.strip()) if line.strip() !=
             "" else None for line in input]
    input.append(None)
    return input


def find_highest_cals(input, num_elf):
    """Returns the sum of the highest calorie counts of the top 'num_elf' elves.
    """
    highest = [0 for _ in range(num_elf)]
    current = 0

    for line in input:
        # increments current elf count by each calorie amount
        if line != None:
            current += int(line)

        # If no more calories for this elf and its higher than one of the current elves then
        # replaces the lowest calorie count with the new one

        else:
            if any(current > elf for elf in highest):
                lowest_elf = highest.index(min(highest))
                highest[lowest_elf] = current
            current = 0
    return sum(highest)


input = input_data("2022/01 Calorie Counting/input.txt")

print("--------------------------------------")
print("Day 1: Calorie Counting")
print("Part One Answer: " + str(find_highest_cals(input, 1)))
print("Part Two Answer: " + str(find_highest_cals(input, 3)))
print("--------------------------------------")
