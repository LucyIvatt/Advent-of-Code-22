DIRECTION = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}


def input_data(filename):
    """Returns the data imported from file -
    """
    file = open(filename, "r")
    input = [line.strip() for line in file.readlines()]
    file.close()
    input = [(pair[0], int(pair[2])) for pair in input]
    return input


def update_element(element, direction, times=1):
    x, y = element
    dx, dy = direction
    for _ in range(times):
        x += dx
        y += dy
    return (x, y)


def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))


def part_one(input):
    h, t = (0, 0), (0, 0)
    t_positions = set()

    i = 0
    for instr in input[:7]:
        for _ in range(instr[1]):
            h = update_element(h, DIRECTION[instr[0]])  # Updates H position

            # Checks if h within 2 in any direction, if so moves t directly towards once
            for dir in DIRECTION.values():
                if update_element(t, dir, 2) == h:
                    t = update_element(t, dir)
                    break

            if h[0] != t[0] and manhattan_distance(h, t) > 2:
                if t[0] < h[0]:
                    t = update_element(t, DIRECTION["R"])
                else:
                    t = update_element(t, DIRECTION["L"])

                if t[1] < h[1]:
                    t = update_element(t, DIRECTION["U"])
                else:
                    t = update_element(t, DIRECTION["D"])
            t_positions.add(tuple(t))

            board = ""
            for i in reversed(range(-7, 7)):
                line = ""
                for j in range(-10, 10):
                    if (j, i) == h:
                        line += "H"
                    elif (j, i) == t:
                        line += "T"
                    elif (j, i) == (0, 0):
                        line += "s"
                    elif (j, i) in t_positions:
                        line += "X"
                    else:
                        line += "."
                board += line + "\n"
            print(board)

    return len(t_positions)


input = input_data("day9/input.txt")

print("--------------------------------------")
print("Day 9: Rope Bridge")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: ")
print("--------------------------------------")
