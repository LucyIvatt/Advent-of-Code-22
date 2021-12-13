def importList(filename):
    note_entries = []
    with open(filename, "r") as file:
        for line in file:
            line = line.split("|")
            note_entries.append((line[0].strip().split(" "), line[1].strip().split(" ")))
    return note_entries

def find_easy_digits(input):
    easy_digit_count = 0
    for entry in input:
        for value in entry[1]:
            if len(value) in [2, 3, 4, 7]:
                easy_digit_count += 1

    return easy_digit_count

def part_one():
    notes = (importList("Day 8 Seven Segment Search\input.txt"))
    return find_easy_digits(notes)

print("--------------------------------------")
print("DAY EIGHT: SEVEN SEGMENT SEARCH")
print("Part One Answer: " + str(part_one()))
# print("Part Two Answer: " + str(part_two()))
print("--------------------------------------")