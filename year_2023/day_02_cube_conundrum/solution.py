from functools import reduce
from collections import defaultdict 
import operator
from aoc_utils import input_data

CONSTRAINTS = {"red": 12, "green": 13, "blue": 14}


def parse_games(puzzle_input):
    game_dict = {}

    for line in puzzle_input:
        rounds_list = []
        game_id, rounds = line.strip().split(":")

        for turn in rounds.split(";"):
            cubes_dict = {colour: int(number) for number, colour in (cubes.strip().split(" ") for cubes in turn.split(", "))}
            rounds_list.append(cubes_dict)
            
        game_dict[game_id.split(" ")[1]] = rounds_list
    
    return game_dict


def part_one(puzzle_input):
    game_dict = parse_games(puzzle_input)
    id_sum = 0

    for game, rounds in game_dict.items():
        if all(number <= CONSTRAINTS[colour] for turn in rounds for colour, number in turn.items()):
            id_sum += int(game)

    return id_sum

def part_two(puzzle_input):
    game_dict = parse_games(puzzle_input)
    power_sum = 0

    for rounds in game_dict.values():
        min_cubes = defaultdict(int) 
        for turn in rounds:
            for colour, number in turn.items():
                min_cubes[colour] = max(min_cubes[colour], number)

        power_sum += reduce(operator.mul, min_cubes.values())
    
    return power_sum


puzzle_input = input_data("year_2023/day_02_cube_conundrum/input.txt")

print("--------------------------------------")
print("Day 02: Cube Conundrum")
print(f"Part One Answer: {part_one(puzzle_input)}")
print(f"Part Two Answer: {part_two(puzzle_input)}")
print("--------------------------------------")
