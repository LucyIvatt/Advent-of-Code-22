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


class Hand:
    def __init__(self, input_string, jokers=False):
        self.hand = input_string.split()[0]
        self.bid = int(input_string.split()[1])
        self.jokers = jokers
        self.hand_type = self.classify_hand()

    def __repr__(self):
        return f"Card({self.hand=}, {self.hand_type=}, {self.bid=})"

    def classify_hand(self):
        if self.jokers:
            num_jokers = self.hand.count("J")
            if num_jokers == 5:
                return HandType.FIVE_OF_KIND
            card_counts = Counter([card for card in self.hand if card != "J"])
            values = sorted(list(card_counts.values()))
            values[-1] += num_jokers

        else:
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

    def __lt__(self, other):
        if self.hand_type.value < other.hand_type.value:
            return True
        elif self.hand_type.value > other.hand_type.value:
            return False
        elif self.hand_type == other.hand_type:
            for ci in range(len(self.hand)):
                comparison_list = value_order_jokers if self.jokers else value_order
                if comparison_list.index(self.hand[ci]) < comparison_list.index(other.hand[ci]):
                    return True
                elif comparison_list.index(self.hand[ci]) > comparison_list.index(other.hand[ci]):
                    return False
                else:
                    continue


value_order = ['2', '3', '4', '5', '6', '7',
               '8', '9', 'T', 'J', 'Q', 'K', 'A']

value_order_jokers = ['J', '2', '3', '4', '5', '6', '7',
                      '8', '9', 'T', 'Q', 'K', 'A']


def solution(puzzle_input, jokers=False):
    hands = [Hand(hand, jokers) for hand in puzzle_input]
    sorted_hands = sorted(hands)
    return sum(hand.bid * (sorted_hands.index(hand) + 1) for hand in sorted_hands)


puzzle_input = input_data("year_2023/day_07_camel_cards/input.txt")

p1, p1_time = time_function(solution, puzzle_input)
p2, p2_time = time_function(solution, puzzle_input, True)

print("--------------------------------------")
print("Day 07: camel_cards")
print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
print("--------------------------------------")
