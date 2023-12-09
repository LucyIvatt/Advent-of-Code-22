from helpers.aoc_utils import input_data, time_function
from enum import Enum
from collections import Counter


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_KIND = 5
    FIVE_OF_KIND = 6


class Card:
    def __init__(self, hand):
        self.hand = list(hand)
        self.hand_type = self.classify_hand()

    def __repr__(self):
        return f"Card({self.hand=}, {self.hand_type})"

    def classify_hand(self):
        card_counts = Counter(self.hand)
        values = sorted(list(card_counts.values()))
        match values:
            case [5]:
                return HandType.FIVE_OF_KIND
            case[1, 4]:
                return HandType.FOUR_OF_KIND
            case [2, 3]:
                return HandType.FULL_HOUSE
            case [1, 1, 3]:
                return HandType.THREE_OF_KIND
            case [1, 2, 2]:
                return HandType.TWO_PAIR
            case [1, 1, 1, 2]:
                return HandType.ONE_PAIR
            case [1, 1, 1, 1, 1]:
                return HandType.HIGH_CARD


value_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def part_one(puzzle_input):
    for hand in puzzle_input:
        test = Card(hand.split()[0])
        print(test)


def part_two(puzzle_input):
    pass


puzzle_input = input_data("year_2023/day_07_camel_cards/example.txt")

p1, p1_time = time_function(part_one, puzzle_input)
p2, p2_time = time_function(part_two, puzzle_input)

print("--------------------------------------")
print("Day 07: camel_cards")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
