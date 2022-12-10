import time


class Operation:
    def __init__(self, op, amount, max_cycle):
        self.op = op
        self.amount = amount
        self.cycle = 0
        self.max_cycle = max_cycle

    def __repr__(self):
        return f"OP({self.op}, {self.amount} - {self.cycle=})"

    def inc_cycle(self):
        self.cycle += 1

    def finished(self):
        return self.cycle == self.max_cycle

    def run_op(self, x):
        if self.op == "addx":
            return x + self.amount
        else:
            return x


def input_data(filename):
    """Returns the data imported from file - 
    """
    file = open(filename, "r")
    input = file.read().splitlines()
    file.close()
    data = []
    for cmd in input:
        if "addx" in cmd:
            split = cmd.split(" ")
            data.append((split[0], int(split[1])))
        else:
            data.append(cmd)
    return data


def part_one(input):
    cycle_num, x = 1, 1
    ss_sum = 0
    current_instr = None
    for instruction in input:
        while current_instr != None:
            current_instr, cycle_num, x, ss_sum = run_cycle(
                current_instr, cycle_num, x, ss_sum)
        if instruction == "noop":
            current_instr = Operation("noop", amount=None, max_cycle=1)
        else:
            current_instr = Operation(
                "addx", amount=instruction[1], max_cycle=2)

    while current_instr != None:
        current_instr, cycle_num, x, ss_sum = run_cycle(
            current_instr, cycle_num, x, ss_sum)
    return ss_sum


def run_cycle(current_instr, cycle_num, x, ss_sum):
    cycle_num += 1
    current_instr.inc_cycle()
    if current_instr.finished():
        x = current_instr.run_op(x)
        current_instr = None
    if cycle_num in range(20, 260, 40):
        ss_sum += cycle_num * x
        print(cycle_num)
        print(x)
        print(str(ss_sum) + "\n")

    # print(f"{cycle_num=}")
    # print(f"{x=}")
    # print(f"{current_instr=}")
    # print("\n")

    return current_instr, cycle_num, x, ss_sum


input = input_data("day10/input.txt")


print("--------------------------------------")
print("Day 10: Cathode-Ray Tube")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: ")
print("--------------------------------------")
