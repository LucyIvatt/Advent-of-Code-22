import unittest

from year_2023.day_10_pipe_maze.solution import input_data, part_one, part_two


class TestDay10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("year_2023/day_10_pipe_maze/example.txt")
        cls.example2 = input_data("year_2023/day_10_pipe_maze/example2.txt")
        cls.puzzle_input = input_data("year_2023/day_10_pipe_maze/input.txt")

    def test_p1_example(self):
        """
        Tests Day 10 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example), 4)
        pass

    def test_p1_example(self):
        """
        Tests Day 10 Part 1 using the example given in the scenario
        """
        self.assertEqual(part_one(self.__class__.example2), 8)
        pass

    def test_p1_actual(self):
        """
        Tests the Day 10 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(part_one(self.__class__.puzzle_input), 7_097)

    def test_p2_example(self):
        """
        Tests Day 10 Part 2 using the example given in the scenario.
        """
        # self.assertEqual(part_two(self.__class__.example), 0)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 10 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        # self.assertEqual(part_two(self.__class__.puzzle_input), 0)
        pass


if __name__ == '__main__':
    unittest.main()
