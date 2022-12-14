import unittest

# TODO: import other solution methods
from day14.solution import input_data


class TestDay14(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day14/example.txt")
        cls.input = input_data("day14/input.txt")

    def test_day_14_p1_example(self):
        """
        Tests Day 14 Part 1 using the example given in the scenario
        """
        pass

    def test_day_14_p1_actual(self):
        """
        Tests the Day 14 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

    def test_day_14_p2_example(self):
        """
        Tests Day 14 Part 2 using the example given in the scenario.
        """
        pass

    def test_day_14_p2_actual(self):
        """
        Tests the Day 14 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

if __name__ == '__main__':
    unittest.main()
