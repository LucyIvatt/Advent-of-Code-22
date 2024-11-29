import unittest

from year_2023.day_16_the_floor_will_be_lava.solution import input_data, part_one, part_two


class TestDay16(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data(
            "year_2023/day_16_the_floor_will_be_lava/example.txt")
        cls.puzzle_input = input_data(
            "year_2023/day_16_the_floor_will_be_lava/input.txt")

    def test_p1_example(self):
        """
        Tests Day 16 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 46)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 16 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 6_921)

    def test_p2_example(self):
        """
        Tests Day 16 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 51)

    def test_p2_actual(self):
        """
        Tests the Day 16 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 7_594)


if __name__ == '__main__':
    unittest.main()
