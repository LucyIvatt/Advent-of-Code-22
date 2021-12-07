def importList(filename):
    instructions = []

    file = open(filename, "r")
    for line in file.readlines():
        instructions.append(line.strip().split())
    
    return instructions

def calculatePositionPart1(instructions):
    horizontal_pos = 0
    depth = 0 

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1])

        if(direction == "forward"):
            horizontal_pos += distance
        elif (direction == "down"):
            depth += distance
        elif (direction == "up"):
            depth -= distance
        else:
            raise ValueError("Invalid direction value")

    return [horizontal_pos, depth]

def calculatePositionAndAimPart2(instructions):
    horizontal_pos = 0
    depth = 0 
    aim = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1])

        if(direction == "forward"):
            horizontal_pos += distance
            depth += (aim * distance)
        elif (direction == "down"):
            aim += distance
        elif (direction == "up"):
            aim -= distance
        else:
            raise ValueError("Invalid direction value")

    return [horizontal_pos, depth, aim]


instructions = importList("Day 2 Dive\input.txt")
part_one = calculatePositionPart1(instructions)
part_two = calculatePositionAndAimPart2(instructions)

print("--------------------------------------")
print("DAY TWO: DIVE!")
print("Part One Answer: " + str(part_one[0] * part_one[1]))
print("Part Two Answer: " + str(part_two[0] * part_two[1]))
print("--------------------------------------")