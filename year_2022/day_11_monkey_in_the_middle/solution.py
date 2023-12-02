import operator
import re
from copy import deepcopy
from math import prod, gcd


OPERATIONS = {"+": operator.add, "-": operator.sub,
              "*": operator.mul, "/": operator.truediv}


class Monkey:
    def __init__(self, items, op, op_num, test_num, true_m, false_m):
        self.items = [int(item) for item in items]

        self.op = OPERATIONS[op]
        self.op_num = int(op_num) if op_num != "old" else "old"

        self.test_num = int(test_num)
        self.true_m = int(true_m)
        self.false_m = int(false_m)

        self.inspect_num = 0

    def inspect(self, item, modulo=None):
        """ Inspects an item and returns the monkey to send it to and the items new worry level."""
        self.inspect_num += 1

        # Applies the operation to the item
        if self.op_num == "old":
            item = self.op(item, item)
        else:
            item = self.op(item, self.op_num)

        # Reduces worry level
        if modulo is not None:
            item %= modulo
        else:
            item //= 3

        # Sends item to the correct monkey
        if item % self.test_num == 0:
            return self.true_m, item
        else:
            return self.false_m, item


def input_data(filename):
    """ Reads the input file and returns a dictionary of monkeys."""
    # Reads file and splits on each monkey.
    file = open(filename, "r")
    input = file.read().split("\n\n")
    file.close()

    monkeys = {}
    for monkey in input:
        monkey = monkey.split("\n ")
        args = []

        # Parses the arguments by finding the numbers and operation.
        for i in range(len(monkey)):
            if i == 1:  # List of items
                args.append(re.findall(r'\d+', monkey[i]))
            elif i == 2:  # Operation
                operation = re.search(r'[-+\/*] (\d+|old)', monkey[i]).group()
                args.extend(operation.split(" "))
            else:  # All other arguments
                args.append(re.search(r'\d+', monkey[i]).group())

        # Creates a monkey object and adds it to the dictionary.
        monkeys[int(args[0])] = Monkey(*args[1:])
    return monkeys


def solution(monkeys, part_two=False):
    monkeys = deepcopy(monkeys)

    # Sets the number of rounds and the modulo if required.
    if not part_two:
        round_num = 20
        modulo = None
    else:
        round_num = 10_000
        modulo = prod(monkey.test_num for monkey in monkeys.values())

    # Plays out the number of rounds required
    for _ in range(round_num):
        for monkey in monkeys.values():
            for item in monkey.items:
                new_monkey, new_item = monkey.inspect(item, modulo)
                monkeys[new_monkey].items.append(new_item)
            monkey.items.clear()

    # Finds the two monkeys with the highest inspect numbers and calculates monkey business.
    inspect_nums = sorted([monkey.inspect_num for monkey in monkeys.values()])
    monkey_business = inspect_nums[-1] * inspect_nums[-2]
    return monkey_business


input = input_data("day11/input.txt")

print("--------------------------------------")
print("Day 11: Monkey in the Middle")
print("Part One Answer: " + str(solution(input)))
print("Part Two Answer: " + str(solution(input, part_two=True)))
print("--------------------------------------")
