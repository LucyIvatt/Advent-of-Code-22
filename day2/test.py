import unittest

# TODO: import other solution methods
from day2.solution import input_data


class TestDay2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day2/example.txt")
        cls.input = input_data("day2/input.txt")

    def test_day_2_p1_example(self):
        """
        Tests Day 2 Part 1 using the example given in the scenario
        """
        pass

    def test_day_2_p1_actual(self):
        """
        Tests the Day 2 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

    def test_day_2_p2_example(self):
        """
        Tests Day 2 Part 2 using the example given in the scenario.
        """
        pass

    def test_day_2_p2_actual(self):
        """
        Tests the Day 2 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

if __name__ == '__main__':
    unittest.main()
