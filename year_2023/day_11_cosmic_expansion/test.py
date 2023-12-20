import unittest

from year_2023.day_11_cosmic_expansion.solution import input_data, solution


class TestDay11(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data(
            "year_2023/day_11_cosmic_expansion/example.txt")
        cls.puzzle_input = input_data(
            "year_2023/day_11_cosmic_expansion/input.txt")

    def test_p1_example(self):
        """
        Tests Day 11 Part 1 using the example given in the scenario
        """
        self.assertEqual(solution(self.__class__.example, 2), 374)

    def test_p1_actual(self):
        """
        Tests the Day 11 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.puzzle_input, 2), 9_947_476)

    def test_p2_example(self):
        """
        Tests Day 11 Part 2 using the example given in the scenario.
        """
        self.assertEqual(solution(self.__class__.example, 100), 8410)

    def test_p2_actual(self):
        """
        Tests the Day 11 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.puzzle_input,
                         1_000_000), 519_939_907_614)


if __name__ == '__main__':
    unittest.main()
