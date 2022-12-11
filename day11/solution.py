import operator
import re

OPERATIONS = {"+": operator.add, "-": operator.sub,
              "*": operator.mul, "/": operator.truediv}


class Monkey:
    def __init__(self, items, op, op_num, test_num, true_m, false_m):
        print(items, op, op_num, test_num, true_m, false_m)
        self.items = [int(item) for item in items]

        self.op = OPERATIONS[op]
        self.op_num = int(op_num) if op_num != "old" else "old"

        self.test_num = int(test_num)
        self.true_m = int(true_m)
        self.false_m = int(false_m)

    def inspect(self, item):
        if self.op_num == "old":
            item = self.op(item, item)
        else:
            item = self.op(item, self.op_num)

        item = item // 3  # integer division

        if item % self.test_num == 0:
            return (item, self.true_m)
        else:
            return (item, self.false_m)


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
    return input

# TODO: Enter solutions


input = input_data("day11/example.txt")

print("--------------------------------------")
print("Day 11: Monkey in the Middle")
print("Part One Answer: ")
print("Part Two Answer: ")
print("--------------------------------------")
