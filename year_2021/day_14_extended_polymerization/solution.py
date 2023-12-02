from collections import defaultdict, Counter


def importList(filename):
    with open(filename, "r") as file:
        input = file.read().split("\n\n")

    polymer_template = input[0].strip()
    insertion_rules = defaultdict(lambda: "")

    for insertion_rule in input[1].split("\n"):
        split_rule = insertion_rule.split(" -> ")
        insertion_rules[split_rule[0]] = split_rule[1]

    return polymer_template, insertion_rules


def simulate_step(template, rules):
    """Unused Resource Intensive Method"""
    new_template = ""
    for i in range(len(template) - 1):
        c1 = template[i]
        c2 = template[i + 1]
        new_template += c1 + rules[c1 + c2]
    return new_template + template[-1]


def calculate_element_counts(template, rules, steps):
    """More efficient method"""
    # Initializes pair & element count dictionaries
    pair_counts = {}
    element_counts = {}
    for i in range(len(template) - 1):
        increase_dict_count(element_counts, template[i], 1)
        pair = template[i] + template[i+1]
        increase_dict_count(pair_counts, pair, 1)
    increase_dict_count(element_counts, template[-1], 1)

    for step in range(steps):
        # for each different type of pair in the polymer
        new_pair_counts = {}
        for pair in pair_counts:
            # Insert the element to generate the 2 new sub pairs
            sub_pairs = [pair[0] + rules[pair], rules[pair] + pair[1]]
            # add 1 to that elements count, for every instance of the current pair type
            increase_dict_count(
                element_counts, rules[pair], pair_counts[pair])

            # Add the new sub pairs to the new count
            for sub_pair in sub_pairs:
                increase_dict_count(
                    new_pair_counts, sub_pair, pair_counts[pair])

        # Replace the old pairs count with the new count
        pair_counts = new_pair_counts
    return element_counts


def increase_dict_count(dictionary, key, increase):
    """Creates a key value pair if one doesn't exist in the dictionary,
     or adds the increase to the current value"""
    if key in dictionary:
        dictionary[key] += increase
    else:
        dictionary[key] = increase


def final_score(element_counts):
    """Returns the quantity of the most common element minus the quantity of the 
    least common element"""
    max_count_char = max(element_counts, key=element_counts.get)
    min_count_char = min(element_counts, key=element_counts.get)
    return element_counts[max_count_char] - element_counts[min_count_char]


def part_one(template, rules):
    element_counts = calculate_element_counts(template, rules, 10)
    return final_score(element_counts)


def part_two(template, rules):
    element_counts = calculate_element_counts(template, rules, 40)
    return final_score(element_counts)


template, rules = importList("Day 14 Extended Polymerization\input.txt")

print("--------------------------------------")
print("DAY 14: EXTENDED POLYMERIZATION")
print("Part One Answer: ", part_one(template, rules))
print("Part Two Answer: ", part_two(template, rules))
print("--------------------------------------")
