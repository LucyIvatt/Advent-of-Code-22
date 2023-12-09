from helpers.aoc_utils import input_data, time_function
from enum import Enum
from collections import Counter

CARD_ORDER, CARD_ORDER_JOKERS = '23456789TJQKA', 'J23456789TQKA'


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
        self.hand, self.bid = input_string.split()
        self.bid = int(self.bid)

        self.jokers = jokers
        self.card_values = CARD_ORDER_JOKERS if self.jokers else CARD_ORDER

        self.hand_type = self.classify_hand()

    def __repr__(self):
        return f"Hand({self.hand=}, {self.hand_type=}, {self.bid=})"

    def classify_hand(self):
        card_counts = Counter(
            [card for card in self.hand if card != "J"]) if self.jokers else Counter(self.hand)
        values = sorted(list(card_counts.values()))

        if self.jokers:
            num_jokers = self.hand.count("J")

            if num_jokers == 5:
                return HandType.FIVE_OF_KIND
            else:
                values[-1] += num_jokers

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
        # Compares based on hand type first
        if self.hand_type != other.hand_type:
            return self.hand_type.value < other.hand_type.value

        # Otherwise uses card values
        for self_card, other_card in zip(self.hand, other.hand):
            if self_card != other_card:
                return self.card_values.index(self_card) < self.card_values.index(other_card)


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
