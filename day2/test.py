import unittest

from day2.solution import input_data, match_outcome, part_1, part_2, Move, Result


class TestDay2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day2/example.txt")
        cls.input = input_data("day2/input.txt")

    def test_match_outcome_win(self):
        move1 = [Move.ROCK, Move.PAPER, Move.SCISSORS]
        move2 = [Move.SCISSORS, Move.ROCK, Move.PAPER]
        for i in range(3):
            self.assertEqual(match_outcome(move1[i], move2[i]), Result.Win)

    def test_match_outcome_loss(self):
        move1 = [Move.ROCK, Move.PAPER, Move.SCISSORS]
        move2 = [Move.PAPER, Move.SCISSORS, Move.ROCK]
        for i in range(3):
            self.assertEqual(match_outcome(move1[i], move2[i]), Result.Loss)

    def test_match_outcome_draw(self):
        move = [Move.ROCK, Move.PAPER, Move.SCISSORS]
        for i in range(3):
            self.assertEqual(match_outcome(move[i], move[i]), Result.Draw)

    def test_day_2_p1_example(self):
        """
        Tests Day 2 Part 1 using the example given in the scenario
        """
        answer = part_1(self.__class__.example)
        self.assertEqual(answer, 15)

    def test_day_2_p1_actual(self):
        """
        Tests the Day 2 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        answer = part_1(self.__class__.input)
        self.assertEqual(answer, 13_221)

    def test_day_2_p2_example(self):
        """
        Tests Day 2 Part 2 using the example given in the scenario.
        """
        answer = part_2(self.__class__.example)
        self.assertEqual(answer, 12)

    def test_day_2_p2_actual(self):
        """
        Tests the Day 2 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        answer = part_2(self.__class__.input)
        self.assertEqual(answer, 13_131)


if __name__ == '__main__':
    unittest.main()
