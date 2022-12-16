import re


class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections


def input_data(filename):
    """Returns the data imported from file -
    """
    with open(filename, 'r') as file:
        input = file.read().strip().split("\n")
    input = [reading.split(";") for reading in input]

    valves = []
    for reading in input:
        cur_valve = re.search(r'[A-Z][A-Z]', reading[0]).group()
        flow_rate = re.search(r'\d+', reading[0]).group()
        connections = re.findall(r'[A-Z][A-Z]', reading[1])
        valves.append(Valve(cur_valve, flow_rate, connections))

    return valves


def part_one(input):
    for i in input:
        print(i.name, i.flow_rate, i.connections)


input = input_data("2022/16 Proboscidea Volcanium/example.txt")
part_one(input)

print("--------------------------------------")
print("Day 16: Proboscidea Volcanium")
print("Part One Answer: ")
print("Part Two Answer: ")
print("--------------------------------------")
