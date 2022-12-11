import operator
import re
from functools import reduce
import math


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

    def inspect(self, item, panic=False):
        self.inspect_num += 1
        if self.op_num == "old":
            item = self.op(item, item)
        else:
            item = self.op(item, self.op_num)

        if not panic:
            item = item // 3  # integer division
        else:
            # Get the prime factors of the integer
            factors = math.factors(item)

            # Reduce the number of prime factors by keeping only the first two
            reduced_factors = factors[:2]

            # Rebuild the integer using the reduced set of prime factors
            item = reduce(lambda x, y: x * y, reduced_factors)

        if item % self.test_num == 0:
            return self.true_m, item
        else:
            return self.false_m, item


def input_data(filename):
    file = open(filename, "r")
    input = file.read().split("\n\n")
    file.close()

    monkeys = {}
    for monkey in input:
        monkey = monkey.split("\n ")
        args = []

        for i in range(len(monkey)):
            if i == 1:
                args.append(re.findall(r'\d+', monkey[i]))
            elif i == 2:
                operation = re.search(r'[-+\/*] (\d+|old)', monkey[i]).group()
                args.extend(operation.split(" "))
            else:
                args.append(re.search(r'\d+', monkey[i]).group())

        monkeys[int(args[0])] = Monkey(*args[1:])
    return monkeys


def part_one(monkeys):
    for _ in range(20):
        for id, monkey in monkeys.items():
            for item in monkey.items:
                new_monkey, new_item = monkey.inspect(item)
                monkeys[new_monkey].items.append(new_item)
            monkey.items.clear()
    inspect_nums = sorted([monkey.inspect_num for monkey in monkeys.values()])
    monkey_business = inspect_nums[-1] * inspect_nums[-2]
    return monkey_business


def part_two(monkeys):
    for _ in range(1000):
        for id, monkey in monkeys.items():
            for item in monkey.items:
                new_monkey, new_item = monkey.inspect(item, panic=True)
                monkeys[new_monkey].items.append(new_item)
            monkey.items.clear()
    inspect_nums = sorted([monkey.inspect_num for monkey in monkeys.values()])
    monkey_business = inspect_nums[-1] * inspect_nums[-2]
    return monkey_business


input = input_data("day11/input.txt")

print("--------------------------------------")
print("Day 11: Monkey in the Middle")
print("Part One Answer: " + str(part_one(input)))
print("Part Two Answer: " + str(part_two(input)))
print("--------------------------------------")
