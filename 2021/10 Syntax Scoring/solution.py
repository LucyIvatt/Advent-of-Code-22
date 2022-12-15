import math

OPENING_CHARS = ["(", "[", "{", "<"]
CLOSING_CHARS = [")", "]", "}", ">"]


def importList(filename):
    report = []
    with open(filename, "r") as file:
        for line in file:
            report.append(line.strip())
    return report


def find_syntax_errors(report):
    error_counts = {")": 0, "]": 0, "}": 0, ">": 0}
    valid_lines = []

    for line in report:
        opening_sequence = []
        error_found = False
        for char in line:
            if char in OPENING_CHARS:
                opening_sequence.append(char)
            else:
                if char != CLOSING_CHARS[OPENING_CHARS.index(opening_sequence[-1])]:
                    error_counts[char] += 1
                    error_found = True
                    break
                else:
                    del opening_sequence[-1]
        if(not error_found):
            valid_lines.append(line)
    return (error_counts, valid_lines)


def calculate_error_score(error_counts):
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    final_score = 0

    for k in error_counts.keys():
        final_score += score_table[k] * error_counts[k]

    return final_score


def find_autocomplete_strings(valid_lines):
    autocomplete_strings = []
    for line in valid_lines:
        autocomplete_string = ""
        opening_sequence = []
        for char in line:
            if char in OPENING_CHARS:
                opening_sequence.append(char)
            else:
                del opening_sequence[-1]

        for opening_char in reversed(opening_sequence):
            autocomplete_string += CLOSING_CHARS[OPENING_CHARS.index(
                opening_char)]
        autocomplete_strings.append(autocomplete_string)
    return autocomplete_strings


def calculate_autocomplete_score(autocomplete_strings):
    score_table = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for autocomplete_string in autocomplete_strings:
        score = 0
        for char in autocomplete_string:
            score *= 5
            score += score_table[char]
        scores.append(score)
    scores.sort()
    return scores[math.floor(len(scores) / 2)]


def part_one():
    report = importList("Day 10 Syntax Scoring\input.txt")
    errors = find_syntax_errors(report)
    return calculate_error_score(errors[0])


def part_two():
    report = importList("Day 10 Syntax Scoring\input.txt")
    errors = find_syntax_errors(report)
    autocomplete_strings = find_autocomplete_strings(errors[1])
    return calculate_autocomplete_score(autocomplete_strings)


print("--------------------------------------")
print("DAY 10:SYNTAX SCORING")
print("Part One Answer: " + str(part_one()))
print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")
