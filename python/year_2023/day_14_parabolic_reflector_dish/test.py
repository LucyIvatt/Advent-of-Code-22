import unittest

from year_2023.day_14_parabolic_reflector_dish.solution import input_data, part_one, part_two


class TestDay14(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data(
            "year_2023/day_14_parabolic_reflector_dish/example.txt")
        cls.puzzle_input = input_data(
            "year_2023/day_14_parabolic_reflector_dish/input.txt")

    def test_p1_example(self):
        """
        Tests Day 14 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 136)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 14 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 110_677)
        pass

    def test_p2_example(self):
        """
        Tests Day 14 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 64)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 14 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 90_551)
        pass


if __name__ == '__main__':
    unittest.main()
