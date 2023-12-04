from collections import Counter, defaultdict

from helpers.aoc_utils import input_data, time_function

puzzle_input = input_data("year_2023/day_04_scratchcards/input.txt")

def part_one(puzzle_input):
    points = 0
    for line in puzzle_input:
        card = line.strip().split("|")
        winning_numbers = [int(num) for num in card[0].split(":")[1].split()]
        losing_numbers = [int(num) for num in card[1].split()]

        matches = Counter(winning_numbers) & Counter(losing_numbers)

        if len(matches)-1 >= 0:
            points += pow(2, len(matches)-1)

    return points
    

def part_two(puzzle_input):
    card_copies = defaultdict(int)

    for i, line in enumerate(puzzle_input):
        card = line.strip().split("|")

        card_number = card[0].split(":")[0]
        card_copies[card_number] += 1
        winning_numbers = [int(num) for num in card[0].split(":")[1].split()]
        losing_numbers = [int(num) for num in card[1].split()]

        matches = Counter(winning_numbers) & Counter(losing_numbers)

        for j in range(i+1, min(i+len(matches)+1, len(puzzle_input))):
            new_card = puzzle_input[j].strip().split("|")
            new_card_number = new_card[0].split(":")[0]
            card_copies[new_card_number] += card_copies[card_number]
    
    return sum(card_copies.values())












p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 04: scratchcards")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
