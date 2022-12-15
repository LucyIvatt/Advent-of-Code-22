def importList(filename):
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [line.strip() for line in input]
    return input

def calculateGammaEpsilonRates(diagnostic_report):
    bit_counts = []
    gamma_rate = []
    epsilon_rate = []
    # Uses first data value to get length of binary nums instead of hardcoding
    for i in range(len(diagnostic_report[0])):
        bit_counts.append([0, 0])
        gamma_rate.append(0)
        epsilon_rate.append(0)

    # For each binary value, adds to count totals
    for i in range(0, len(diagnostic_report)):
        binary_val = diagnostic_report[i]
        for j in range(0, len(diagnostic_report[i])):
            if binary_val[j] == "0":
                bit_counts[j][0] += 1
            elif binary_val[j] == "1":
                bit_counts[j][1] += 1
            else:
                raise ValueError("Invalid bit value has been read")
    
    # For each bit in the rates, compares the count values
    for i in range(0, len(bit_counts)):
        if bit_counts[i][0] > bit_counts[i][1]:
            gamma_rate[i] = 0
            epsilon_rate[i] = 1
        else:
            gamma_rate[i] = 1
            epsilon_rate[i] = 0
    
    return ["".join(str(b) for b in gamma_rate), "".join(str(b) for b in epsilon_rate)]

def calculateOxygenRating(diagnostic_report):
    binary_num_length = len(diagnostic_report[0])

    for i in range(0, binary_num_length):
        most_common_bit = calculateMostCommonBit(diagnostic_report, i)

        remaining_binary_nums = []
        for binary_num in diagnostic_report:
            if most_common_bit == "equal":
                if (binary_num[i] == "1"):
                    remaining_binary_nums.append(binary_num)
            elif binary_num[i] == most_common_bit:
                remaining_binary_nums.append(binary_num)

        diagnostic_report = remaining_binary_nums
        if len(diagnostic_report) == 1:
            return diagnostic_report[0]

def calculateCO2Rating(diagnostic_report):
    binary_num_length = len(diagnostic_report[0])
    for i in range(0, binary_num_length):
        remaining_binary_nums = []
        most_common_bit = calculateMostCommonBit(diagnostic_report, i)
        for binary_num in diagnostic_report:
            if most_common_bit == "equal":
                if (binary_num[i] == "0"):
                    remaining_binary_nums.append(binary_num)
            elif binary_num[i] != most_common_bit:
                remaining_binary_nums.append(binary_num)
        diagnostic_report = remaining_binary_nums
        if len(diagnostic_report) == 1:
            return diagnostic_report[0] 

def calculateMostCommonBit(inputs, index):
    zero_count = 0
    one_count = 0

    for binary_num in inputs:
        if binary_num[index] == "0":
            zero_count += 1
        elif binary_num[index] == "1":
            one_count += 1
        else:
            raise ValueError("Invalid bit value has been read")

    if zero_count > one_count:
        return "0"
    elif one_count > zero_count:
        return "1"
    else:
        return "equal"

def binaryMultiplication(x, y):
    dec_x = int(x, 2)
    dec_y = int(y, 2)
    return dec_x * dec_y

input = importList("Day 3 Binary Diagnostic\input.txt")
rates = calculateGammaEpsilonRates(input)

power = binaryMultiplication(rates[0], rates[1])
life_support = binaryMultiplication(calculateOxygenRating(input), calculateCO2Rating(input))

print("--------------------------------------")
print("DAY THREE: BINARY DIAGNOSTIC")
print("Part One Answer: " + str(power))
print("Part Two Answer: " + str(life_support))
print("--------------------------------------")
