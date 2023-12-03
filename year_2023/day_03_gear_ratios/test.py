import unittest

from year_2023.day_03_gear_ratios.solution import input_data


class TestDay03(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("year_2023/day_03_gear_ratios/example.txt")
        cls.puzzle_input = input_data("year_2023/day_03_gear_ratios/input.txt")

    def test_p1_example(self):
        """
        Tests Day 03 Part 1 using the example given in the scenario
        """
        pass

    def test_p1_actual(self):
        """
        Tests the Day 03 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

    def test_p2_example(self):
        """
        Tests Day 03 Part 2 using the example given in the scenario.
        """
        pass

    def test_p2_actual(self):
        """
        Tests the Day 03 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

if __name__ == '__main__':
    unittest.main()
