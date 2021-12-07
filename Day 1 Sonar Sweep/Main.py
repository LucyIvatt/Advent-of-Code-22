def importList(filename):
    file = open(filename, "r")
    input = file.readlines()
    input = [int(line.strip()) for line in input]
    return input

def increaseDepthCountPart1(input):
    count = 0
    for i in range(1, len(input)):
            if input[i] > input[i-1]:
                count += 1
    return count

def increaseDepthCountWindowPart2(input):
    windows = []
    for i in range(0, len(input)):
        if i > 1:
            windows.append(input[i] + input[i - 1] + input[i - 2])
        
    return increaseDepthCountPart1(windows)



input = importList("Day 1 Sonar Sweep\input.txt")

print("--------------------------------------")
print("DAY ONE: SONAR SWEEP")
print("Part One Answer: " + str(increaseDepthCountPart1(input)))
print("Part Two Answer: " + str(increaseDepthCountWindowPart2(input)))
print("--------------------------------------")