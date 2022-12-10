import unittest

# TODO: import other solution methods
from day10.solution import input_data, part_one


class TestDay10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day10/example.txt")
        cls.input = input_data("day10/input.txt")

    def test_day_10_p1_example(self):
        """
        Tests Day 10 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 13_140)

    def test_day_10_p1_actual(self):
        """
        Tests the Day 10 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

    def test_day_10_p2_example(self):
        """
        Tests Day 10 Part 2 using the example given in the scenario.
        """
        pass

    def test_day_10_p2_actual(self):
        """
        Tests the Day 10 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass


if __name__ == '__main__':
    unittest.main()
