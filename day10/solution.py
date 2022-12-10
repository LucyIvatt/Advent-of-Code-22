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
    """Returns the data imported from file - list containing both tuples of addx cmds and strings of noop cmds
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


def solution(input):
    # Initialises counters and display
    cycle_num, x = 1, 1
    ss_sum = 0
    current_instr = None
    crt_display = ""
    crt_line = ["." for _ in range(40)]

    for instruction in input:
        # Finishes the current instruction before moving to the next one
        while current_instr != None:
            # Adds next line to the CRT display
            if cycle_num in range(41, 241, 40):
                crt_display += "".join(crt_line) + "\n"
                crt_line = ["." for _ in range(40)]

            # if the cursor is on the sprite then draws a lit pixel
            cursor_loc = (cycle_num % 40)-1
            if x in range(cursor_loc-1, cursor_loc+2):
                crt_line[cursor_loc] = "#"

            # Runs a single cycle on the CPU
            current_instr, cycle_num, x, ss_sum = run_cycle(
                current_instr, cycle_num, x, ss_sum)

        # Once the last instruction has been completed, creates next operation.
        if instruction == "noop":
            current_instr = Operation("noop", amount=None, max_cycle=1)
        else:
            current_instr = Operation(
                "addx", amount=instruction[1], max_cycle=2)

    # Prints final CRT display and returns signal strength sum
    crt_display += "".join(crt_line)
    return ss_sum, crt_display


def run_cycle(current_instr, cycle_num, x, ss_sum):
    """Runs a single cycle on the cpu and returns the updated values of 
    the current instruction, cycle num, register value and signal strength sum."""
    # Increments overall cycle num and instructions cycle num
    cycle_num += 1
    current_instr.inc_cycle()

    # Checks if the instruction if finished and applies it
    if current_instr.finished():
        x = current_instr.run_op(x)
        current_instr = None

    # If the cycle 20th, 60th, 100th, 140th, 180th, and 220th - calculates signal strength and adds to sum
    if cycle_num in range(20, 260, 40):
        ss_sum += cycle_num * x
    return current_instr, cycle_num, x, ss_sum


input = input_data("day10/input.txt")
p1, p2 = solution(input)


print("--------------------------------------")
print("Day 10: Cathode-Ray Tube")
print("Part One Answer: " + str(p1))
print("Part Two Answer:")
print(p2)
print("--------------------------------------")
