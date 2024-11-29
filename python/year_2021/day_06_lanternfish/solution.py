def importList(filename):
    file = open(filename, "r")
    input = file.readline()
    file.close()
    input = input.split(",")
    return [int(x) for x in input]
    
# Slow/Resource Excessive Method
def simulate_days(input, days):
    for day in range(days):
        for i in range(len(input)):
            if input[i] == 0:
                input[i] = 6
                input.append(8)
            else:
                input[i] -= 1
    return input

# Faster Method 
def calculate_fish_count(input, days):
    fish_count = [0 for age in range(0, 9)]
    for fish in input:
        fish_count[fish] += 1
    
    for day in range(days):
        new_fish_count = [0 for age in range(0, 9)]

        # Shuffle ages by 1 day
        for age in range(1, 9):
            new_fish_count[age - 1] = fish_count[age]
        
        new_fish_count[6] += fish_count[0]
        new_fish_count[8] += fish_count[0]
        fish_count = new_fish_count
    
    return sum(fish_count)

def part_one():
    input = importList("Day 6 Lanternfish\input.txt")
    return calculate_fish_count(input, 80)

def part_two():
    input = importList("Day 6 Lanternfish\input.txt")
    return calculate_fish_count(input, 256)

print("--------------------------------------")
print("DAY SIX: LANTERNFISH")
print("Part One Answer: " + str(part_one()))
print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")