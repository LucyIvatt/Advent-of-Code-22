def importList(filename):
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [int(line.strip()) if line.strip() !=
             "" else None for line in input]
    return input


def find_highest_cals(input, num_elf):
    highest = [0 for elf in range(num_elf)]
    current = 0

    for line in input:
        if line != None:
            current += int(line)
        else:
            if any(current > elf for elf in highest):
                lowest_elf = highest.index(min(highest))
                highest[lowest_elf] = current
            current = 0

    return sum(highest)


input = importList("day1/input.txt")
print(find_highest_cals(input, 1))
print(find_highest_cals(input, 3))
