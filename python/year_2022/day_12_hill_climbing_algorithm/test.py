import unittest

from python.year_2022.day_12_hill_climbing_algorithm.solution import input_data, part_one, part_two


class TestDay12(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pathStart = "python/year_2022/day_12_hill_climbing_algorithm"
        cls.example = input_data(f"{pathStart}/example.txt")
        cls.input = input_data(f"{pathStart}/input.txt")

    def test_day_12_p1_example(self):
        """
        Tests Day 12 Part 1 using the example given in the scenario
        """
        _, graph, s, e = self.__class__.example
        self.assertEqual(part_one(graph, s, e), 31)

    def test_day_12_p1_actual(self):
        """
        Tests the Day 12 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        _, graph, s, e = self.__class__.input
        self.assertEqual(part_one(graph, s, e), 456)

    def test_day_12_p2_example(self):
        """
        Tests Day 12 Part 2 using the example given in the scenario.
        """
        grid, graph, _, e = self.__class__.example
        self.assertEqual(part_two(grid, graph, e), 29)

    def test_day_12_p2_actual(self):
        """
        Tests the Day 12 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        grid, graph, _, e = self.__class__.input
        self.assertEqual(part_two(grid, graph, e), 454)


if __name__ == '__main__':
    unittest.main()
