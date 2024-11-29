import unittest

from python.year_2023.day_15_lens_library.solution import input_data, part_one, part_two


class TestDay15(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("python/year_2023/day_15_lens_library/example.txt")
        cls.puzzle_input = input_data(
            "python/year_2023/day_15_lens_library/input.txt")

    def test_p1_example(self):
        """
        Tests Day 15 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 1_320)

    def test_p1_actual(self):
        """
        Tests the Day 15 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 517_015)

    def test_p2_example(self):
        """
        Tests Day 15 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 145)

    def test_p2_actual(self):
        """
        Tests the Day 15 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 286_104)


if __name__ == '__main__':
    unittest.main()
