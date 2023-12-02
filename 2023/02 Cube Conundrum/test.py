import unittest

# TODO: import other solution methods
from solution import input_data


class TestDay02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("/02 Cube Conundrum/example.txt")
        cls.puzzle_input = input_data("/02 Cube Conundrum/input.txt")

    def test_day_02_p1_example(self):
        """
        Tests Day 02 Part 1 using the example given in the scenario
        """
        pass

    def test_day_02_p1_actual(self):
        """
        Tests the Day 02 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

    def test_day_02_p2_example(self):
        """
        Tests Day 02 Part 2 using the example given in the scenario.
        """
        pass

    def test_day_02_p2_actual(self):
        """
        Tests the Day 02 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

if __name__ == '__main__':
    unittest.main()
