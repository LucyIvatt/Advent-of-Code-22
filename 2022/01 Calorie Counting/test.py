import unittest

from day01.solution import input_data, find_highest_cals


class TestDay1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day01/example.txt")
        cls.input = input_data("day01/input.txt")

    def test_day_1_p1_example(self):
        """
        Tests Day 1 Part 1 using the example given in the scenario
        """
        answer = find_highest_cals(self.__class__.example, 1)
        self.assertEqual(answer, 24_000)

    def test_day_1_p1_actual(self):
        """
        Tests the Day 1 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        answer = find_highest_cals(self.__class__.input, 1)
        self.assertEqual(answer, 65912)

    def test_day_1_p2_example(self):
        """
        Tests Day 1 Part 2 using the example given in the scenario.
        """
        answer = find_highest_cals(self.__class__.example, 3)
        self.assertEqual(answer, 45_000)

    def test_day_1_p2_actual(self):
        """
        Tests the Day 1 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        answer = find_highest_cals(self.__class__.input, 3)
        self.assertEqual(answer, 195_625)


if __name__ == '__main__':
    unittest.main()
