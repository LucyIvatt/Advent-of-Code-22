import random

class BingoCard:
    def __init__(self, card_values):
        self.card_values = card_values
    
    def __str__(self):
        string_rep = ""
        for line in self.card_values:
            string_rep += str(line) + "\n"
        return string_rep
    
    def mark_card(self, called_number):
        for i in range(len(self.card_values)):
            for j in range(len(self.card_values[i])):
                if self.card_values[i][j] == called_number:
                    self.card_values[i][j] = "X"

    def check_win_cond(self):
        # check columns for win condition
        for i in range(0, 5):
            # Check row for win condition
            if all(element == "X" for element in self.card_values[i]):
                return True

            # Check columns for win condition
            column_matches = True
            for j in range(0, 5):
                if(self.card_values[j][i] != "X"):
                    column_matches = False
                    break;
            if(column_matches):
                return True

        return False

    def calculate_score(self, last_called):
        score = 0
        for row in self.card_values:
            for number in row:
                if number != "X":
                    score += number
        return score * last_called

test_card = [[0, 0, 0, 0, 0,],
[0, 3, 0, 0, 0,],
[2, 3, 3, 3, 3,],
[0, 3, 0, 0, 0,],
[0, 2, 0, 0, 0,]
]

bingo_test = BingoCard(test_card)
print(bingo_test)
print(bingo_test.check_win_cond())
bingo_test.mark_card(2)
print(bingo_test)
print(bingo_test.check_win_cond())
bingo_test.mark_card(3)
print(bingo_test)
print(bingo_test.check_win_cond())
