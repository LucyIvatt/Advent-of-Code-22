import unittest

from python.year_2023.day_07_camel_cards.solution import input_data, HandType, Hand, solution


class TestDay07(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("python/year_2023/day_07_camel_cards/example.txt")
        cls.puzzle_input = input_data("python/year_2023/day_07_camel_cards/input.txt")

    def test_classify_hand(self):
        test_cases = {"AAAAA 1": HandType.FIVE_OF_KIND,
                      "AA8AA 1": HandType.FOUR_OF_KIND,
                      "23332 1": HandType.FULL_HOUSE,
                      "TTT98 1": HandType.THREE_OF_KIND,
                      "23432 1": HandType.TWO_PAIR,
                      "A23A4 1": HandType.ONE_PAIR,
                      "23456 1": HandType.HIGH_CARD}

        for hand, classification in test_cases.items():
            card = Hand(hand)
            self.assertEqual(card.hand_type, classification)

    def test_p1_example(self):
        """t
        Tests Day 07 Part 1 using the example given in the scenario
        """
        self.assertEqual(solution(self.__class__.example), 6_440)

    def test_p1_actual(self):
        """
        Tests the Day 07 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.puzzle_input), 251_058_093)

    def test_p2_example(self):
        """
        Tests Day 07 Part 2 using the example given in the scenario.
        """
        self.assertEqual(solution(self.__class__.example, True), 5_905)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 07 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(
            solution(self.__class__.puzzle_input, True), 249_781_879)
        pass


if __name__ == '__main__':
    unittest.main()
