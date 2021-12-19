PROBE_START_POS = (0, 0)


def importList(filename):
    with open(filename, "r") as file:
        target_area = file.readline().replace("target area: ", "")
        xy = target_area.split(", ")
        x, y = xy[0].replace("x=", "").split(
            ".."), xy[1].replace("y=", "").split("..")
        x, y = [int(val) for val in x], [int(val) for val in y]
        return ([i for i in range(x[0], x[1]+1)], [j for j in range(y[0], y[1]+1)])


def part_one(target_area):
    for i in target_area:
        axis = "X: " if i == 0 else "Y: "
        print(axis, i)


target_area = importList("17 Trick Shot\input.txt")

print("--------------------------------------")
print("DAY 16: TRICK SHOT")
print("Part One Answer: ", part_one(target_area))
# print("Part Two Answer: ", part_two(target_area))
print("--------------------------------------")
