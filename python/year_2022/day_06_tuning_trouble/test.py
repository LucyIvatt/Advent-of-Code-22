import unittest

from day06.solution import input_data, solution


class TestDay6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day06/example.txt")
        cls.input = input_data("day06/input.txt")

    def test_day_6_p1_example(self):
        """
        Tests Day 6 Part 1 using the example given in the scenario
        """
        self.assertEqual(solution(self.__class__.example, 4), 7)

    def test_day_6_p1_actual(self):
        """
        Tests the Day 6 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.input, 4), 1953)

    def test_day_6_p2_example(self):
        """
        Tests Day 6 Part 2 using the example given in the scenario.
        """
        self.assertEqual(solution(self.__class__.example, 14), 19)

    def test_day_6_p2_actual(self):
        """
        Tests the Day 6 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.input, 14), 2301)


if __name__ == '__main__':
    unittest.main()
