def importList(filename):
    file = open(filename, "r")
    input = file.readlines()
    input = [int(line.strip()) for line in input]
    return input

def increaseDepthCount(input):
    count = 0
    for i in range(1, len(input)):
            if input[i] > input[i-1]:
                count += 1
    return count

def increaseDepthCountWindow(input):
    windows = []
    for i in range(0, len(input)):
        if i > 1:
            windows.append(input[i] + input[i - 1] + input[i - 2])
        
    return increaseDepthCount(windows)



input = importList("Day 1 Sonar Sweep\input.txt")

print("Part One Answer: " + str(increaseDepthCount(input)))
print("Part Two Answer: " + str(increaseDepthCountWindow(input)))