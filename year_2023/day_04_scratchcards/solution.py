from collections import Counter, defaultdict
from helpers.aoc_utils import input_data, time_function

puzzle_input = input_data("year_2023/day_04_scratchcards/example.txt")

from collections import Counter

def find_matches(card):
    winning_numbers = [int(num) for num in card[0].split(":")[1].split()]
    losing_numbers = [int(num) for num in card[1].split()]
    return Counter(winning_numbers) & Counter(losing_numbers)

def calc_points(matches):
    return pow(2, len(matches) - 1) if len(matches) - 1 >= 0 else 0

def part_one(puzzle_input):
    return sum(calc_points(find_matches(line.strip().split("|"))) for line in puzzle_input)


def part_two(puzzle_input):
    card_copies = {i:1 for i in range(1, len(puzzle_input)+1)}

    for i, line in enumerate(puzzle_input):
        card = line.strip().split("|") 
        matches = find_matches(card)

        for j in range(i+1, min(i+len(matches)+1, len(puzzle_input))):
            card_copies[j+1] += card_copies[i+1]
    
    print(sorted(card_copies.items()))
    
    return sum(card_copies.values())












p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 04: scratchcards")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
