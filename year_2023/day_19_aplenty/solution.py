from helpers.aoc_utils import input_data, time_function
import re

PATTERN = re.compile(r'^([a-z])([<>]\d+):([a-z]+)$')


class Rule():
    def __init__(self, input_str) -> None:
        match = PATTERN.match(input_str)
        if match:
            self.final = False
            self.input = match.group(1)
            self.operation = match.group(2)
            self.destination = match.group(3)
        else:
            self.destination = input_str
            self.final = True

    def __repr__(self) -> str:
        if not self.final:
            return f"Rule({self.input=} {self.operation=} {self.destination=})"
        else:
            return f"Rule({self.destination=})"

    def process_part(self, part) -> str:
        if self.final:
            return self.destination
        else:
            val = part[self.input]
            if eval(f"{val}{self.operation}"):
                return self.destination
            else:
                return None


def part_one(puzzle_input):
    x = Rule("a<2006:qkq")
    part = {"x": 0, "m": 1, "a": 2, "s": 3}
    print(x)
    print(x.process_part(part))


def part_two(puzzle_input):
    pass


def main():
    puzzle_input = input_data("year_2023/day_19_aplenty/input.txt")

    p1, p1_time = time_function(part_one, puzzle_input)
    p2, p2_time = time_function(part_two, puzzle_input)

    print("--------------------------------------")
    print("Day 19: aplenty")
    print(f"Part One Answer: {p1} - [{p1_time:.4f} seconds]")
    print(f"Part Two Answer: {p2} - [{p2_time:.4f} seconds]")
    print("--------------------------------------")


if __name__ == "__main__":
    main()
# a<2006:qkq,
# m>2090:A,
# rfg
"""
a<2006:qkq,
m>2090:A,
rfg

object representing a rule: (maybe use eval?)
    - letter than is compared
    - operation
    - number
    - destination





parts = list of dicts for the parts (x, m, a, s as keys)

rules = dict of workflow with list of rules ({"in": rule1, rule2})

list of Accepted

for part in parts:
    current_location = 'in'
    while current_location is not R or A:
        rule_id = 0
        new_location = rules[current_location][rule_id].find_next_location
        if new location and current location are the same, increment rule id:
        otherwise reset rule id
        current_location = new_location
    
    if current_location == "A":
        append to list
        




"""
