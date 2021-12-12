def importList(filename):
    file = open(filename, "r")
    input = file.readline()
    file.close()
    input = input.split(",")
    return [int(x) for x in input]
    
# Slow & Resource Excessive Method
def simulate_days(input, days):
    for day in range(days):
        for i in range(len(input)):
            if input[i] == 0:
                input[i] = 6
                input.append(8)
            else:
                input[i] -= 1
    return input

# Faster Method ? pls
def calculate_fish_count(input, days):
    pass

def part_one():
    input = importList("Day 6 Lanternfish\input.txt")
    print(input)
    fish = simulate_days(input, 80)
    return len(fish)

print("--------------------------------------")
print("DAY FIVE: HYDROTHERMAL VENTURE")
print("Part One Answer: " + str(part_one()))
print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")