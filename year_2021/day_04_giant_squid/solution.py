import copy


class BingoCard:
    def __init__(self, card_values):
        self.card_values = card_values

    def __str__(self):
        string_rep = ""
        for line in self.card_values:
            string_rep += str(line) + "\n"
        return string_rep

    """Replaces the cards number with a cross to show it as marked"""

    def mark_card(self, drawn_number):
        for i in range(len(self.card_values)):
            for j in range(len(self.card_values[i])):
                if self.card_values[i][j] == drawn_number:
                    self.card_values[i][j] = "X"

    """Checks if win condition is met - returns true or false"""

    def check_win_cond(self):
        for i in range(0, 5):
            # Check row for win condition
            if all(element == "X" for element in self.card_values[i]):
                return True

            # Check columns for win condition
            column_matches = True
            for j in range(0, 5):
                if(self.card_values[j][i] != "X"):
                    column_matches = False
                    break
            if(column_matches):
                return True

        # If no win found, return false
        return False

    """Calculates final score of the card, sum of remaining numbers * last drawn number"""

    def calculate_score(self, last_drawn):
        score = 0
        for row in self.card_values:
            for number in row:
                if number != "X":
                    score += int(number)
        return score * int(last_drawn)


"""Imports the data from the text file and converts it to BingoCard instances"""


def importData(filename):
    # Reads data from input file line by line and strips empty lines & whitespace
    file = open(filename, "r")
    input = file.readlines()
    file.close()
    input = [line.strip() for line in input if line.strip() != ""]

    # Removes draw order from list
    draw_order = input[0].split(",")
    del input[0]

    bingo_cards = []
    two_d_card = []
    count = 0

    # For each line of bingo cards, adds 5 to temporary 2D list then generates a BingoCard instance from this and adds to bingo_cards list.

    for i in range(len(input)):
        two_d_card.append(input[i].split())
        count += 1
        if(count == 5):
            bingo_cards.append(BingoCard(copy.deepcopy(two_d_card)))
            two_d_card.clear()
            count = 0

    return [draw_order, bingo_cards]


"""Iterates through the cards and marks them for each drawn number. When one meets the win condition, returns the score"""


def find_winner(cards, draw_order):
    for number in draw_order:
        for card in cards:
            card.mark_card(number)
            if(card.check_win_cond() == True):
                return card.calculate_score(number)


"""Iterates through the cards and marks them for each drawn number. When one meets the win condition, returns the score"""


def find_last_winner(cards, draw_order):

    # Sets up list to show which cards have been solved, initialized to false for all.
    solved = [False for card in cards]
    final_card_index = None

    for number in draw_order:
        if(final_card_index == None):
            # For all cards, marks each number drawn.
            for card in cards:
                card.mark_card(number)
                # If a card meets the win condition, set as solved
                if(card.check_win_cond() == True):
                    solved[cards.index(card)] = True
                    # If only one remains unsolved, final card index has been found
                    if solved.count(False) == 1:
                        final_card_index = solved.index(False)
        else:
            # When final card index has been found, continues to mark only this card until win condition met
            cards[final_card_index].mark_card(number)
            if(cards[final_card_index].check_win_cond() == True):
                # Returns final score when win condition met
                return cards[final_card_index].calculate_score(number)


data = importData("Day 4 Giant Squid\input.txt")
draw_order, cards = data[0], data[1]

print("--------------------------------------")
print("DAY FOUR: GIANT SQUID")
print("Part One Answer: " + str(find_winner(cards, draw_order)))
print("Part Two Answer: " + str(find_last_winner(cards, draw_order)))
print("--------------------------------------")
