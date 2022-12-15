def importList(filename):
    file = open(filename, "r")
    input = file.readline().strip()
    file.close()
    input = input.split(",")
    return [int(x) for x in input]

def find_minimum_fuel(input):
    input.sort()
    valid_positions = range(input[0], input[-1] + 1)
    fuel_costs = [0 for position in valid_positions]
    for pos in valid_positions:
        for crab_location in input:
            fuel_costs[pos] += abs(crab_location - pos)
    return min(fuel_costs)

def find_minimum_fuel_two(input):
    input.sort()
    valid_positions = range(input[0], input[-1] + 1)
    fuel_costs = [0 for position in valid_positions]
    for pos in valid_positions:
        for crab_location in input:
            fuel_costs[pos] += non_constant_movement_cost(abs(crab_location - pos))
    return int(min(fuel_costs))

def non_constant_movement_cost(n):
    return 0.5 * n**2 + 0.5 * n

def part_one():
    input = importList("Day 7 The Treachery of Whales\input.txt")
    return find_minimum_fuel(input)

def part_two():
    input = importList("Day 7 The Treachery of Whales\input.txt")
    return find_minimum_fuel_two(input)

print("--------------------------------------")
print("DAY SEVEN: THE TREACHERY OF WHALES")
print("Part One Answer: " + str(part_one()))
print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")