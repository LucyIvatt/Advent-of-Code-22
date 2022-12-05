import unittest

# TODO: import other solution methods
from day5.solution import input_data, part_one


class TestDay5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day5/example.txt")
        cls.input = input_data("day5/input.txt")

    def test_day_5_p1_example(self):
        """
        Tests Day 5 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example, "CMZ"))

    def test_day_5_p1_actual(self):
        """
        Tests the Day 5 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

    def test_day_5_p2_example(self):
        """
        Tests Day 5 Part 2 using the example given in the scenario.
        """
        pass

    def test_day_5_p2_actual(self):
        """
        Tests the Day 5 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass


if __name__ == '__main__':
    unittest.main()
