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
        print(opp_move)
        print(your_move)
        if your_move.value == (opp_move.value - 1) % 3:
            outcome = Result.Win
        elif your_move.value == (opp_move.value + 1) % 3:
            outcome = Result.Loss
        else:
            outcome = Result.Draw
        print(outcome)

        # Score of one match is shape + round outcome
        score += your_move.value + outcome.value
    return score


def part_2(input):
    input = [(OPPONENT[x], OUTCOME[y]) for x, y in input]
    score = 0

    for opp_move, outcome in input:
        match outcome:
            case(Result.Win):
                your_move = Move((opp_move.value + 1) % 3)
            case(Result.Draw):
                your_move = opp_move
            case(Result.Loss):
                your_move = Move((opp_move.value - 1) % 3)

        # Score of one match is shape + round outcome
        score += your_move.value + outcome.value
    return score


input_1 = input_data("day2/input.txt")
input_2 = input_data("day2/example.txt")

print("--------------------------------------")
print("Day 2: Rock Paper Scissors")
print("Part One Answer: " + str(part_1(input_1)))
print("Part Two Answer: " + str(part_2(input_2)))
print("--------------------------------------")
