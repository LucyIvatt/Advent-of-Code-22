from functools import reduce

CONSTRAINTS = {"red": 12, "green": 13, "blue": 14}

def input_data(filename):
    """Returns the data imported from file - 
    """
    file = open(filename, "r")
    puzzle_input = file.readlines()
    file.close()

    return puzzle_input

def parse_games(puzzle_input):
    game_dict = {}
    for line in puzzle_input:
        rounds_list = []
        game_id, rounds = line.strip().split(":")
        for turn in rounds.split(";"):
            cubes_dict = {}
            for colour_set in turn.split(", "):
                number, colour = colour_set.strip().split(" ")
                cubes_dict[colour] = int(number)
            rounds_list.append(cubes_dict)
        game_dict[game_id.split(" ")[1]] = rounds_list
    return game_dict

def part_one(puzzle_input):
    game_dict = parse_games(puzzle_input)
    id_sum = 0

    for game, rounds in game_dict.items():
        game_valid = True
        for turn in rounds:
            for colour, number in turn.items():
                if number > CONSTRAINTS[colour]:
                    game_valid = False
                    break
        
        if game_valid: id_sum += int(game)
    
    return id_sum

def part_two(puzzle_input):
    game_dict = parse_games(puzzle_input)
    power_sum = 0

    for game, rounds in game_dict.items():
        min_cubes = {colour: 0 for colour in CONSTRAINTS.keys()}
        for turn in rounds:
            for colour, number in turn.items():
                if number > min_cubes[colour]: min_cubes[colour] = number
        power_sum += reduce((lambda x, y: x * y), min_cubes.values())
    


    
    
    return power_sum

puzzle_input = input_data("input.txt")

print("--------------------------------------")
print("Day 02: Cube Conundrum")
print(f"Part One Answer: {part_one(puzzle_input)}")
print(f"Part Two Answer: {part_two(puzzle_input)}")
print("--------------------------------------")
