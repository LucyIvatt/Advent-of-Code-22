import unittest

from day03.solution import input_data, part_one, part_two


class TestDay3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day03/example.txt")
        cls.input = input_data("day03/input.txt")

    def test_day_3_p1_example(self):
        """
        Tests Day 3 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 157)

    def test_day_3_p1_actual(self):
        """
        Tests the Day 3 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.input), 7_997)

    def test_day_3_p2_example(self):
        """
        Tests Day 3 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 70)

    def test_day_3_p2_actual(self):
        """
        Tests the Day 3 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.input), 2_545)


if __name__ == '__main__':
    unittest.main()
