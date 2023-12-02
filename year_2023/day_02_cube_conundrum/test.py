import unittest

from year_2023.day_02_cube_conundrum.solution import part_one, part_two
from helpers.aoc_utils import input_data


class TestDay02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("year_2023/day_02_cube_conundrum/example.txt")
        cls.puzzle_input = input_data("year_2023/day_02_cube_conundrum/input.txt")

    def test_p1_example(self):
        """
        Tests Day 02 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 8)


    def test_p1_actual(self):
        """
        Tests the Day 02 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 2149)


    def test_p2_example(self):
        """
        Tests Day 02 Part 2 using the example given in the scenario.
        """    
        self.assertEqual(part_two(self.__class__.example), 2286)


    def test_p2_actual(self):
        """
        Tests the Day 02 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 71274)

if __name__ == '__main__':
    unittest.main()
