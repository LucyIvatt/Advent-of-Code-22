import unittest

# TODO: import other solution methods
from day15.solution import input_data, part_one, part_two


class TestDay15(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day15/example.txt")
        cls.input = input_data("day15/input.txt")

    def test_day_15_p1_example(self):
        """
        Tests Day 15 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example, p1_y=10), 26)

    def test_day_15_p1_actual(self):
        """
        Tests the Day 15 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.input,
                         p1_y=2_000_000), 5_878_678)

    def test_day_15_p2_example(self):
        """
        Tests Day 15 Part 2 using the example given in the scenario.
        """
        self.assertEqual(
            part_two(self.__class__.example, max_xy=20), 56_000_011)

    def test_day_15_p2_actual(self):
        """
        Tests the Day 15 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.input,
                         max_xy=4_000_000), 11_796_491_041_245)


if __name__ == '__main__':
    unittest.main()
