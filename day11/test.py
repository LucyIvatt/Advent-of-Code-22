import unittest

# TODO: import other solution methods
from day11.solution import input_data, part_one


class TestDay11(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day11/example.txt")
        cls.input = input_data("day11/input.txt")

    def test_day_11_p1_example(self):
        """
        Tests Day 11 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.example), 10_605)

    def test_day_11_p1_actual(self):
        """
        Tests the Day 11 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.input), 50_172)

    def test_day_11_p2_example(self):
        """
        Tests Day 11 Part 2 using the example given in the scenario.
        """
        pass

    def test_day_11_p2_actual(self):
        """
        Tests the Day 11 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass


if __name__ == '__main__':
    unittest.main()
