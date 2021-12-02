def calculateDepthMeasurementIncreaseCount(input):
    previous = None
    increase_count = 0

    for line in input:
        value = int(line.strip())
        if previous != None:
            if value > previous:
                increase_count += 1
        previous = value
    
    return increase_count


input = open("input.txt", "r")
print(calculateDepthMeasurementIncreaseCount(input))