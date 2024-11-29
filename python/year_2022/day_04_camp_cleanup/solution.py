def input_data(filename):
    """Returns the data imported from file - lists containing pairs of elf assignments [(start, end), (start2, end2)]
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [[(int(x[0].split("-")[0]),
               int(x[0].split("-")[1])),
              (int(x[1].split("-")[0]),
              int(x[1].split("-")[1]))]
             for x in (line.strip().split(",") for line in input)]
    return input


def part_one(input):
    """Counts number of assignment pairs where one fully overlaps with the other."""
    count = 0
    for elf1, elf2 in input:
        # Orders the elves by starting area id
        if elf2[0] < elf1[0]:
            elf1, elf2 = elf2, elf1

        # Checks for full overlap
        if (elf1[0] == elf2[0]) or (elf2[1] <= elf1[1]):
            count += 1
    return count


def part_two(input):
    """Counts number of assignment pairs which overlap at any point."""
    count = 0
    for elf1, elf2 in input:
        # Orders the elves by starting area id
        if elf2[0] < elf1[0]:
            elf1, elf2 = elf2, elf1

        # Checks for partial overlap
        if not (elf1[1] < elf2[0]):
            count += 1
    return count

if __name__ == "__main__":
    input = input_data("python/year_2022/day_04_camp_cleanup/input.txt")

    print("--------------------------------------")
    print("Day 4: Camp Cleanup")
    print("Part One Answer: " + str(part_one(input)))
    print("Part Two Answer: " + str(part_two(input)))
    print("--------------------------------------")
