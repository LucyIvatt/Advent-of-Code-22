import re


class Instruction:
    def __init__(self, num_crates, start, end):
        # -1 for start and end to allow indexing from 0 not 1
        self.num_crates = int(num_crates)
        self.start = int(start) - 1
        self.end = int(end) - 1

    def __str__(self):
        return f"Num: {self.num_crates} Start:{self.start} End:{self.end}"


class Stack:
    def __init__(self):
        self.crates = []

    def add_crates(self, new_crates):
        self.crates.extend(reversed(new_crates))

    def remove_crates(self, num_crates):
        removed = self.crates[-num_crates:]
        self.crates = self.crates[:-num_crates]
        return removed

    def top_crate(self):
        return self.crates[-1]


def input_data(filename):
    """Returns the data imported from file -
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [line.replace("\n", "") for line in input]

    # Separates the crate stacks from the instructions
    separator = input.index("")
    stack_input = input[:separator-1]
    instruction_input = input[separator+1:]

    # Removes unneccesary characters
    # Represents crates as their letters (empty space means no crate present)
    stack_input = [[line[i]
                    for i in range(1, len(line), 4)]
                   for line in stack_input]

    # Creates empty stack for each column
    stacks = {i: Stack() for i in range(len(stack_input[0]))}

    # Adds crates in reverse order so index -1 is the top of the stack
    for line in reversed(stack_input):
        for i in range(len(line)):
            if line[i] != " ":
                stacks[i].add_crates(line[i])

    # Maps instruction input into Instruction class
    instructions = [re.findall('[0-9]+', line) for line in instruction_input]
    instructions = [Instruction(instr[0], instr[1], instr[2])
                    for instr in instructions]
    return stacks, instructions


def part_one(input):
    stacks, instructions = input

    for instr in instructions:
        # Removes the specified number of crates from the starting stack and adds to end stack
        moved = stacks[instr.start].remove_crates(instr.num_crates)
        stacks[instr.end].add_crates(moved)

    return "".join([stack.top_crate() for stack in stacks.values()])


input = input_data("day5/input.txt")

print("--------------------------------------")
print("Day 5: Supply Stacks")
print("Part One Answer: " + part_one(input))
print("Part Two Answer: ")
print("--------------------------------------")
