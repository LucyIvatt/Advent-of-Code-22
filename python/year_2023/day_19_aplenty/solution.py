from functools import reduce
from itertools import groupby
from helpers.aoc_utils import input_data, time_function, split_by_empty_line
import re
import time

PATTERN = re.compile(r'^([a-z])([<>]\d+):([a-zA-Z]+)$')


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
    workflows, parts = split_by_empty_line(puzzle_input)
    #fmt:off
    parts = [eval(reduce(lambda part, char: part.replace(f'{char}=',
                f"'{char}':"), ["x", "m", "a", "s"], part)) for part in parts]
    #fmt:on
    workflows_dict = {}
    for workflow in workflows:
        groups = re.match(r'^(.*?){(.*)}$', workflow).groups()
        workflow_id = groups[0]
        rules = [Rule(rule) for rule in groups[1].split(",")]
        workflows_dict[workflow_id] = rules

    accepted = []

    for part in parts:
        current_location = "in"
        rule_id = 0
        while current_location != "R" and current_location != "A":
            new_location = workflows_dict[current_location][rule_id].process_part(
                part)

            if new_location == None:
                rule_id += 1
            else:
                rule_id = 0
                current_location = new_location

        if current_location == "A":
            accepted.append(part)

    return sum(rating for part in accepted for rating in part.values())


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
