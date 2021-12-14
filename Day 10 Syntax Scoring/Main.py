def importList(filename):
    report = []
    with open(filename, "r") as file:
        for line in file:
            report.append(line.strip())
    return report


def find_syntax_errors(report):
    opening_chars = ["(", "[", "{", "<"]
    closing_chars = [")", "]", "}", ">"]

    error_counts = {")": 0, "]": 0, "}": 0, ">": 0}

    for line in report:
        opening_sequence = []
        for char in line:
            if char in opening_chars:
                opening_sequence.append(char)
            else:
                if char != closing_chars[opening_chars.index(opening_sequence[-1])]:
                    error_counts[char] += 1
                    break
                else:
                    del opening_sequence[-1]
    return error_counts


def calculate_error_score(error_counts):
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    final_score = 0

    for k in error_counts.keys():
        final_score += score_table[k] * error_counts[k]

    return final_score


def part_one():
    report = importList("Day 10 Syntax Scoring\input.txt")
    errors = find_syntax_errors(report)
    return calculate_error_score(errors)


print("--------------------------------------")
print("DAY 10:SYNTAX SCORING")
print("Part One Answer: " + str(part_one()))
# print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")
