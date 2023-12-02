import unittest

from day11.solution import input_data, solution


class TestDay11(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = input_data("day11/example.txt")
        cls.input = input_data("day11/input.txt")

    def test_day_11_p1_example(self):
        """
        Tests Day 11 Part 1 using the example given in the scenario
        """
        self.assertEqual(solution(self.example), 10_605)

    def test_day_11_p1_actual(self):
        """
        Tests the Day 11 Part 1 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.input), 50_172)

    def test_day_11_p2_example(self):
        """
        Tests Day 11 Part 2 using the example given in the scenario.
        """
        self.assertEqual(solution(self.example, part_two=True), 2_713_310_158)

    def test_day_11_p2_actual(self):
        """
        Tests the Day 11 Part 2 using my generated input. Used to check any edits
        made to the program have not broken it.
        """
        self.assertEqual(solution(self.input, part_two=True), 11_614_682_178)


if __name__ == '__main__':
    unittest.main()
