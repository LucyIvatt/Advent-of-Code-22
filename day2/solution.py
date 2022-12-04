from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Win
# 1, 2, 3 --> 3, 1, 2
# mod(x+1) (+1)

# Loss
# 1, 2, 3 --> 2, 3, 1
# mod(x)+1 1, 2 , 0


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


def match_outcome(move1, move2):
    if move2.value == ((move1.value + 1) % 3) + 1:
        return Result.Win
    elif move2.value == ((move1.value) % 3) + 1:
        return Result.Loss
    else:
        return Result.Draw


def input_data(filename):
    """Returns the data imported from file - pairs of strategy guide information
    """
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [line.split() for line in input]
    return input


def part_1(input):
    input = [(OPPONENT[x], MOVE[y]) for x, y in input]
    score = 0

    # Win, Loss & Draw conditions
    for opp_move, your_move in input:
        outcome = match_outcome(your_move, opp_move)

        # Score of one match is shape + round outcome
        score += your_move.value + outcome.value
    return score


def part_2(input):
    input = [(OPPONENT[x], OUTCOME[y]) for x, y in input]
    score = 0

    for opp_move, outcome in input:
        match outcome:
            case(Result.Win):
                your_move = Move(((opp_move.value) % 3) + 1)
            case(Result.Draw):
                your_move = opp_move
            case(Result.Loss):
                your_move = Move(((opp_move.value + 1) % 3) + 1)

        # Score of one match is shape + round outcome
        score += your_move.value + outcome.value

    return score


input = input_data("day2/input.txt")

print("--------------------------------------")
print("Day 2: Rock Paper Scissors")
print("Part One Answer: " + str(part_1(input)))
print("Part Two Answer: " + str(part_2(input)))
print("--------------------------------------")
