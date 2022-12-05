
def input_data(filename):
    """Returns the data imported from file - 
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()

    input = [line.replace("\n", "") for line in input]

    separator = input.index("")
    stack_input = input[:separator-1]
    instruction_input = input[separator+1:]

    stack_input = [[line[i]
                    for i in range(1, len(line), 4)] for line in stack_input]

    stacks = {i: list() for i in range(len(stack_input[0]))}

    # TODO: add input to initialised stacks

    return stacks, instruction_input


def part_one(input):
    pass


input = input_data("day5/example.txt")

print("--------------------------------------")
print("Day 5: Supply Stacks")
print("Part One Answer: ")
print("Part Two Answer: ")
print("--------------------------------------")
