import unittest

from year_2023.day_09_mirage_maintenance.solution import input_data, solution


class TestDay09(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data(
            "year_2023/day_09_mirage_maintenance/example.txt")
        cls.puzzle_input = input_data(
            "year_2023/day_09_mirage_maintenance/input.txt")

    def test_p1_example(self):
        """
        Tests Day 09 Part 1 using the example given in the scenario
        """
        self.assertEqual(solution(self.__class__.example), 114)

    def test_p1_actual(self):
        """
        Tests the Day 09 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.__class__.puzzle_input), 1974913025)

    def test_p2_example(self):
        """
        Tests Day 09 Part 2 using the example given in the scenario.
        """
        self.assertEqual(solution(self.__class__.example, True), 2)
        pass

    def test_p2_actual(self):
        """
        Tests the Day 09 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        # self.assertEqual(solution(self.__class__.puzzle_input, True), 0)
        pass


if __name__ == '__main__':
    unittest.main()
