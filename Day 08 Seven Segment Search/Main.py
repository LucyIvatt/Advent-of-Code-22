def importList(filename):
    note_entries = []
    with open(filename, "r") as file:
        for line in file:
            line = line.split("|")
            observations = ["".join(sorted(obs))
                            for obs in (line[0].strip().split(" "))]
            codes = ["".join(sorted(code))
                     for code in line[1].strip().split(" ")]
            note_entries.append((observations, codes))
    return note_entries


def find_easy_digit_count(input):
    easy_digit_count = 0
    for entry in input:
        for value in entry[1]:
            if len(value) in [2, 3, 4, 7]:
                easy_digit_count += 1
    return easy_digit_count


def find_number_code_mappings(observations):
    # Mapping of the length of the code to the numbers it could relate to
    simple_number_lengths = {2: 1, 3: 7, 4: 4, 7: 8}

    # For each line in the notes
    number_codes = dict()
    unknown = []
    for value in observations:
        # Calculate easy number code representations
        if len(value) in [2, 3, 4, 7]:
            number_codes[simple_number_lengths[len(value)]] = value
        else:
            unknown.append(value)

    for value in unknown:
        # Uses set overlap to differentiate 2s, 3s & 5s
        if len(value) == 5:
            if remaining_segments(value, number_codes[1]) == 3:
                number_codes[3] = value  # Value represents digit 3
            elif remaining_segments(value, number_codes[4]) == 3:
                number_codes[2] = value  # Value represents digit 2
            else:
                number_codes[5] = value  # Value represents digit 5

        # Uses set overlap to differentiate 0s, 6s & 9s
        elif len(value) == 6:
            if remaining_segments(value, number_codes[1]) == 5:
                number_codes[6] = value  # Value represents digit 6
            elif remaining_segments(value, number_codes[4]) == 2:
                number_codes[9] = value  # Value represents digit 9
            else:
                number_codes[0] = value  # Value represents digit 0
    return number_codes


def remaining_segments(code_one, code_two):
    for char in code_two:
        code_one = code_one.replace(char, "")
    return len(code_one)


def calculate_output_sum(input):
    output_value_sum = 0
    for line in input:
        output_value = ""
        mappings = find_number_code_mappings(line[0])
        for value in line[1]:
            for digit, code in mappings.items():
                if(value == code):
                    output_value += str(digit)
        output_value_sum += int(output_value)
    return output_value_sum


def part_one():
    notes = (importList("Day 8 Seven Segment Search\input.txt"))
    return find_easy_digit_count(notes)


def part_two():
    notes = (importList("Day 8 Seven Segment Search\input.txt"))
    return calculate_output_sum(notes)


print("--------------------------------------")
print("DAY EIGHT: SEVEN SEGMENT SEARCH")
print("Part One Answer: " + str(part_one()))
print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")
