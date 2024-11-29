import unittest

from year_2023.day_06_wait_for_it.solution import input_data, part_one, part_two


class TestDay06(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("year_2023/day_06_wait_for_it/example.txt")
        cls.puzzle_input = input_data("year_2023/day_06_wait_for_it/input.txt")

    def test_p1_example(self):
        """
        Tests Day 06 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 288)

    def test_p1_actual(self):
        """
        Tests the Day 06 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 252_000)
        pass

    def test_p2_example(self):
        """
        Tests Day 06 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 71_503)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 06 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 36_992_486)
        pass


if __name__ == '__main__':
    unittest.main()
