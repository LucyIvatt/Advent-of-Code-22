import unittest

from year_2023.day_07_camel_cards.solution import input_data, HandType, Card


class TestDay07(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("year_2023/day_07_camel_cards/example.txt")
        cls.puzzle_input = input_data("year_2023/day_07_camel_cards/input.txt")

    def test_classify_hand(self):
        test_cases = {"AAAAA": HandType.FIVE_OF_KIND,
                      "AA8AA": HandType.FOUR_OF_KIND,
                      "23332": HandType.FULL_HOUSE,
                      "TTT98": HandType.THREE_OF_KIND,
                      "23432": HandType.TWO_PAIR,
                      "A23A4": HandType.ONE_PAIR,
                      "23456": HandType.HIGH_CARD}

        for hand, classification in test_cases.items():
            card = Card(hand)
            self.assertEqual(card.hand_type, classification)

    def test_p1_example(self):
        """t
        Tests Day 07 Part 1 using the example given in the scenario
        """
        # self.assertEqual(part_one(self.__class__.example), 0)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 07 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        # self.assertEqual(part_one(self.__class__.puzzle_input), 0)
        pass

    def test_p2_example(self):
        """
        Tests Day 07 Part 2 using the example given in the scenario.
        """
        # self.assertEqual(part_two(self.__class__.example), 0)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 07 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        # self.assertEqual(part_two(self.__class__.puzzle_input), 0)
        pass


if __name__ == '__main__':
    unittest.main()
