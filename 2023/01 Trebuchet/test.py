import unittest

from solution import input_data, part_one, part_two


class TestDay01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("2023/01 Trebuchet/example.txt")
        cls.example2 = input_data("2023/01 Trebuchet/example2.txt")
        cls.puzzle_input = input_data("2023/01 Trebuchet/input.txt")

    def test_day_01_p1_example(self):
        """
        Tests Day 01 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 142)

    def test_day_01_p1_actual(self):
        """
        Tests the Day 01 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 54081)

    def test_day_01_p2_example(self):
        """
        Tests Day 01 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example2), 281)

    def test_day_01_p2_actual(self):
        """
        Tests the Day 01 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        pass

if __name__ == '__main__':
    unittest.main()
