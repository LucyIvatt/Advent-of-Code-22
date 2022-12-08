import unittest

# TODO: import other solution methods
from day8.solution import input_data, part_one, part_two


class TestDay8(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day8/example.txt")
        cls.input = input_data("day8/input.txt")

    def test_day_8_p1_example(self):
        """
        Tests Day 8 Part 1 using the example given in the scenario
        """
        self.assertEquals(part_one(self.__class__.example), 21)

    def test_day_8_p1_actual(self):
        """
        Tests the Day 8 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEquals(part_one(self.__class__.input), 1_711)

    def test_day_8_p2_example(self):
        """
        Tests Day 8 Part 2 using the example given in the scenario.
        """
        self.assertEquals(part_two(self.__class__.example), 8)

    def test_day_8_p2_actual(self):
        """
        Tests the Day 8 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.input), 301_392)


if __name__ == '__main__':
    unittest.main()
