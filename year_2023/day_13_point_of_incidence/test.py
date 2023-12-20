import unittest

from year_2023.day_13_point_of_incidence.solution import input_data, part_one, part_two


class TestDay13(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data(
            "year_2023/day_13_point_of_incidence/example.txt")
        cls.puzzle_input = input_data(
            "year_2023/day_13_point_of_incidence/input.txt")

    def test_p1_example(self): 
        """
        Tests Day 13 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 405)

    def test_p1_actual(self):
        """
        Tests the Day 13 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 35_521)
        pass

    def test_p2_example(self):
        """
        Tests Day 13 Part 2 using the example given in the scenario.
        """
        self.assertEqual(part_two(self.__class__.example), 400)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 13 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_two(self.__class__.puzzle_input), 34_795)
        pass


if __name__ == '__main__':
    unittest.main()
