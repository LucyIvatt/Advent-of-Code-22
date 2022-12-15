import time
PROBE_START_POS = (0, 0)


def importList(filename):
    with open(filename, "r") as file:
        target_area = file.readline().replace("target area: ", "")
        xy = target_area.split(", ")
        x, y = xy[0].replace("x=", "").split(
            ".."), xy[1].replace("y=", "").split("..")
        x, y = [int(val) for val in x], [int(val) for val in y]
        return ([i for i in range(x[0], x[1]+1)], [j for j in range(y[0], y[1]+1)])


def check_velocity_valid(vx, vy, x_targets, y_targets):
    cur_x, cur_y = PROBE_START_POS
    max_y = 0

    while cur_x < max(x_targets) and cur_y > min(y_targets):
        # Calculate new values on each step
        cur_x += vx
        cur_y += vy

        vy -= 1
        vx -= 1 if vx > 0 else 0

        max_y = cur_y if cur_y > max_y else max_y

        # Hit target

        if cur_x in x_targets and cur_y in y_targets:
            return True, max_y
    return False


def part_one(target_area):
    start_time = time.time()
    max_ys = []
    for vx in range(max(target_area[0])):
        for vy in range(min(target_area[1]), -min(target_area[1])):
            check = check_velocity_valid(
                vx, vy, target_area[0], target_area[1])
            if check != False:
                max_ys.append(check[1])
    end_time = time.time()
    return str(max(max_ys)) + ", time taken: " + "{:.4f}".format(end_time - start_time) + "s"


def part_two(target_area):
    start_time = time.time()
    valid_vs = []
    for vx in range(max(target_area[0]) + 1):
        for vy in range(min(target_area[1]), -min(target_area[1])):
            check = check_velocity_valid(
                vx, vy, target_area[0], target_area[1])
            if check != False:
                valid_vs.append((vx, vy))
    end_time = time.time()
    return str(len(valid_vs)) + ", time taken: " + "{:.4f}".format(end_time - start_time) + "s"


target_area = importList("17 Trick Shot\input.txt")

print("--------------------------------------")
print("DAY 16: TRICK SHOT")
print("Part One Answer: ", part_one(target_area))
print("Part Two Answer: ", part_two(target_area))
print("--------------------------------------")
