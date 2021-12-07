def importList(filename):
    file = open(filename, "r")
    input = file.readlines()
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

def calculatePowerConsumption(gamma_rate, epsilon_rate):
    decimal_gamma = int(gamma_rate, 2)
    decimal_epsilon = int(epsilon_rate, 2)
    return decimal_gamma * decimal_epsilon         


input = importList("Day 3 Binary Diagnostic\input.txt")
rates = calculateGammaEpsilonRates(input)
power = calculatePowerConsumption(rates[0], rates[1])

print("--------------------------------------")
print("DAY THREE: BINARY DIAGNOSTIC")
print("Part One Answer: " + str(power))
print("Part Two Answer: ")
print("--------------------------------------")