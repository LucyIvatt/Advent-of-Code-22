from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    Win = 6
    Draw = 3
    Loss = 0


OPPONENT = {"A": Move.ROCK,
            "B": Move.PAPER,
            "C": Move.SCISSORS}

MOVE = {"X": Move.ROCK,
       "Y": Move.PAPER,
       "Z": Move.SCISSORS}

OUTCOME = {"X": Result.Loss,
            "Y": Result.Draw,
            "Z": Result.Win}


def input_data(filename, fix_game=False):
    """Returns the data imported from file - pairs of opponents choice and your choice
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()

    input = [line.split() for line in input]

    if fix_game == True:
        input = [(OPPONENT[x], OUTCOME[y]) for x, y in input]
    else:
        input = [(OPPONENT[x], MOVE[y]) for x, y in input]
        
    return input


def calculate_score(input, fix_game=False):
    score = 0
    for game in input:
        if fix_game:
            outcome = game[0]
            score += game[0].value + outcome.value
        else:
            match game:
                # Loss
                case(Move.ROCK, Move.PAPER) | (Move.PAPER, Move.SCISSORS) | (Move.SCISSORS, Move.ROCK):
                    outcome = Result.Win
                # Draw
                case(Move.ROCK, Move.ROCK) | (Move.SCISSORS, Move.SCISSORS) | (Move.PAPER, Move.PAPER):
                    outcome = Result.Draw
                # Win
                case _:
                    outcome = Result.Loss
            score += game[1].value + outcome.value
    return score



input_1 = input_data("day2/input.txt")
input_2 = input_data("day2/input.txt", fix_game=True)

print("--------------------------------------")
print("Day 2: Rock Paper Scissors")
print("Part One Answer: " + str(calculate_score(input_1)))
print("Part Two Answer: " + str(calculate_score(input_2, fix_game=True)))
print("--------------------------------------")
