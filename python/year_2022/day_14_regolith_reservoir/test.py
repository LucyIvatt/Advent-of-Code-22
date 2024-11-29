import unittest

from python.year_2022.day_14_regolith_reservoir.solution import input_data, part_one, part_two


class TestDay14(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pathStart = "python/year_2022/day_14_regolith_reservoir"
        cls.example = input_data(f"{pathStart}/example.txt")
        cls.input = input_data(f"{pathStart}/input.txt")

    def test_day_14_p1_example(self):
        """
        Tests Day 14 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 24)

    def test_day_14_p1_actual(self):
        """
        Tests the Day 14 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.input), 961)

    def test_day_14_p2_example(self):
        """
        Tests Day 14 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 93)

    def test_day_14_p2_actual(self):
        """
        Tests the Day 14 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.input), 26_375)


if __name__ == '__main__':
    unittest.main()
